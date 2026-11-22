#!/usr/bin/env python3
"""Which side of the aircraft is the sun on during a flight?

Steps along the great-circle path between two points, works out the sun's
compass direction (azimuth) and height (elevation) at each step, and compares
it with the direction the aircraft is heading.

Standard library only. Examples:

  python3 sun_side.py --from LHR --to JFK --depart 2026-06-21T11:00 --duration 8:00
  python3 sun_side.py --from 47.45,-122.31 --to 19.09,72.87 \
      --depart-utc 2026-12-01T02:30 --duration 15:10 --json

Limits (repeat these to the traveller):
  * Real routes bend away from the great circle for winds, weather and
    airspace, and the first and last minutes follow the runway, not the route.
  * The time given is treated as take-off and the duration as time in the air.
    Scheduled gate-to-gate times are close enough; delays shift the result.
  * Sun position is good to a fraction of a degree, far better than the route.
"""
import argparse
import json
import math
import sys
from datetime import datetime, timedelta, timezone

# code: (latitude, longitude, time zone). A small convenience table only.
# For any other airport pass "lat,lon" and use --depart-utc or --utc-offset.
AIRPORTS = {
    "AKL": (-37.01, 174.79, "Pacific/Auckland"), "AMS": (52.31, 4.76, "Europe/Amsterdam"),
    "ATL": (33.64, -84.43, "America/New_York"), "BCN": (41.30, 2.08, "Europe/Madrid"),
    "BKK": (13.69, 100.75, "Asia/Bangkok"), "BLR": (13.20, 77.71, "Asia/Kolkata"),
    "BOG": (4.70, -74.15, "America/Bogota"), "BOM": (19.09, 72.87, "Asia/Kolkata"),
    "BOS": (42.36, -71.01, "America/New_York"), "CAI": (30.12, 31.41, "Africa/Cairo"),
    "CDG": (49.01, 2.55, "Europe/Paris"), "CPT": (-33.97, 18.60, "Africa/Johannesburg"),
    "DEL": (28.56, 77.10, "Asia/Kolkata"), "DEN": (39.86, -104.67, "America/Denver"),
    "DFW": (32.90, -97.04, "America/Chicago"), "DOH": (25.27, 51.61, "Asia/Qatar"),
    "DXB": (25.25, 55.36, "Asia/Dubai"), "EWR": (40.69, -74.17, "America/New_York"),
    "EZE": (-34.82, -58.54, "America/Argentina/Buenos_Aires"), "FCO": (41.80, 12.25, "Europe/Rome"),
    "FRA": (50.03, 8.57, "Europe/Berlin"), "GRU": (-23.43, -46.47, "America/Sao_Paulo"),
    "HKG": (22.31, 113.91, "Asia/Hong_Kong"), "HND": (35.55, 139.78, "Asia/Tokyo"),
    "HNL": (21.32, -157.92, "Pacific/Honolulu"), "IAD": (38.95, -77.46, "America/New_York"),
    "IAH": (29.98, -95.34, "America/Chicago"), "ICN": (37.46, 126.44, "Asia/Seoul"),
    "IST": (41.28, 28.75, "Europe/Istanbul"), "JFK": (40.64, -73.78, "America/New_York"),
    "JNB": (-26.14, 28.25, "Africa/Johannesburg"), "KUL": (2.75, 101.71, "Asia/Kuala_Lumpur"),
    "LAS": (36.08, -115.15, "America/Los_Angeles"), "LAX": (33.94, -118.41, "America/Los_Angeles"),
    "LHR": (51.47, -0.45, "Europe/London"), "LIM": (-12.02, -77.11, "America/Lima"),
    "LIS": (38.77, -9.13, "Europe/Lisbon"), "MAD": (40.49, -3.57, "Europe/Madrid"),
    "MEL": (-37.67, 144.84, "Australia/Melbourne"), "MEX": (19.44, -99.07, "America/Mexico_City"),
    "MIA": (25.79, -80.29, "America/New_York"), "MUC": (48.35, 11.79, "Europe/Berlin"),
    "NBO": (-1.32, 36.93, "Africa/Nairobi"), "NRT": (35.77, 140.39, "Asia/Tokyo"),
    "ORD": (41.98, -87.90, "America/Chicago"), "PEK": (40.08, 116.58, "Asia/Shanghai"),
    "PER": (-31.94, 115.97, "Australia/Perth"), "PVG": (31.14, 121.81, "Asia/Shanghai"),
    "SCL": (-33.39, -70.79, "America/Santiago"), "SEA": (47.45, -122.31, "America/Los_Angeles"),
    "SFO": (37.62, -122.38, "America/Los_Angeles"), "SIN": (1.36, 103.99, "Asia/Singapore"),
    "SYD": (-33.95, 151.18, "Australia/Sydney"), "YVR": (49.19, -123.18, "America/Vancouver"),
    "YYZ": (43.68, -79.63, "America/Toronto"), "ZRH": (47.46, 8.55, "Europe/Zurich"),
}

AHEAD_CONE = 20.0     # sun within this many degrees of the nose or tail: no clear side
HIGH_SUN = 60.0       # above this the sun is mostly on the roof, not in the side windows
LOW_SUN = 10.0        # at or below this the sun is in the eyes: glare, sunrise, sunset
VISIBLE_FROM = -4.0   # at cruise height the sun's disc stays visible until about here


def parse_place(text):
    """Return (lat, lon, tz_name_or_None, label)."""
    t = text.strip()
    if t.upper() in AIRPORTS:
        lat, lon, tz = AIRPORTS[t.upper()]
        return lat, lon, tz, t.upper()
    try:
        lat_s, lon_s = t.replace(" ", "").split(",")
        lat, lon = float(lat_s), float(lon_s)
    except ValueError:
        sys.exit(f"'{text}' is not in the built-in table. Pass coordinates as lat,lon "
                 f"(north and east positive), for example 51.47,-0.45. "
                 f"Known codes: {' '.join(sorted(AIRPORTS))}")
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        sys.exit(f"Coordinates out of range: {text}")
    return lat, lon, None, f"{lat:.2f},{lon:.2f}"


def parse_duration(text):
    """'8:15', '8h15', '8h15m', or minutes as a plain number -> minutes."""
    t = text.strip().lower().replace("m", "").replace("h", ":")
    try:
        if ":" in t:
            h, m = t.split(":")
            if int(h) < 0 or not 0 <= int(m or 0) < 60:
                raise ValueError
            return int(h) * 60 + int(m or 0)
        if not math.isfinite(float(t)):
            raise ValueError
        return float(t)
    except ValueError:
        sys.exit(f"Could not read the duration '{text}'. Use hours:minutes (8:15) or minutes (495).")


def parse_time(text, flag):
    try:
        t = datetime.fromisoformat(text.strip())
    except ValueError:
        sys.exit(f"Could not read {flag} '{text}'. Use YYYY-MM-DDTHH:MM, for example 2026-12-14T08:25.")
    if "T" not in text.strip().upper() and " " not in text.strip():
        sys.exit(f"{flag} needs a time as well as a date, for example 2026-12-14T08:25.")
    if t.tzinfo is not None:
        sys.exit(f"Give {flag} without a time-zone suffix (convert to UTC, or use --depart with --utc-offset).")
    return t


def unit(lat, lon):
    la, lo = math.radians(lat), math.radians(lon)
    return (math.cos(la) * math.cos(lo), math.cos(la) * math.sin(lo), math.sin(la))


def from_unit(v):
    x, y, z = v
    return math.degrees(math.asin(max(-1, min(1, z)))), math.degrees(math.atan2(y, x))


def angle_between(lat1, lon1, lat2, lon2):
    a, b = unit(lat1, lon1), unit(lat2, lon2)
    dot = sum(p * q for p, q in zip(a, b))
    return math.acos(max(-1, min(1, dot)))


def point_along(lat1, lon1, lat2, lon2, frac):
    """Point a fraction of the way along the great circle."""
    d = angle_between(lat1, lon1, lat2, lon2)
    if d < 1e-9:
        return lat1, lon1
    a, b = unit(lat1, lon1), unit(lat2, lon2)
    s1 = math.sin((1 - frac) * d) / math.sin(d)
    s2 = math.sin(frac * d) / math.sin(d)
    return from_unit(tuple(s1 * p + s2 * q for p, q in zip(a, b)))


def bearing(lat1, lon1, lat2, lon2):
    """Compass direction of travel from point 1 towards point 2, degrees from north."""
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dl = math.radians(lon2 - lon1)
    y = math.sin(dl) * math.cos(p2)
    x = math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl)
    return math.degrees(math.atan2(y, x)) % 360


def sun_position(when_utc, lat, lon):
    """Sun azimuth (degrees from north, clockwise) and elevation (degrees above
    the horizon) for a UTC time and place. The standard low-precision method
    (Meeus, "Astronomical Algorithms", the basis of NOAA's solar calculator)."""
    jd = when_utc.timestamp() / 86400.0 + 2440587.5
    t = (jd - 2451545.0) / 36525.0
    l0 = (280.46646 + t * (36000.76983 + t * 0.0003032)) % 360
    m = math.radians(357.52911 + t * (35999.05029 - 0.0001537 * t))
    e = 0.016708634 - t * (0.000042037 + 0.0000001267 * t)
    c = (math.sin(m) * (1.914602 - t * (0.004817 + 0.000014 * t))
         + math.sin(2 * m) * (0.019993 - 0.000101 * t) + math.sin(3 * m) * 0.000289)
    omega = math.radians(125.04 - 1934.136 * t)
    lam = math.radians(l0 + c - 0.00569 - 0.00478 * math.sin(omega))
    eps0 = 23 + (26 + (21.448 - t * (46.815 + t * (0.00059 - t * 0.001813))) / 60) / 60
    eps = math.radians(eps0 + 0.00256 * math.cos(omega))
    decl = math.asin(math.sin(eps) * math.sin(lam))
    y = math.tan(eps / 2) ** 2
    l0r = math.radians(l0)
    eqtime = 4 * math.degrees(y * math.sin(2 * l0r) - 2 * e * math.sin(m)
                              + 4 * e * y * math.sin(m) * math.cos(2 * l0r)
                              - 0.5 * y * y * math.sin(4 * l0r)
                              - 1.25 * e * e * math.sin(2 * m))  # minutes
    minutes = when_utc.hour * 60 + when_utc.minute + when_utc.second / 60
    true_solar = (minutes + eqtime + 4 * lon) % 1440
    ha = math.radians(true_solar / 4 - 180)
    la = math.radians(lat)
    elev = math.asin(math.sin(la) * math.sin(decl) + math.cos(la) * math.cos(decl) * math.cos(ha))
    az = math.atan2(-math.sin(ha) * math.cos(decl),
                    math.cos(la) * math.sin(decl) - math.sin(la) * math.cos(decl) * math.cos(ha))
    return math.degrees(az) % 360, math.degrees(elev)


def classify(az, elev, heading):
    """Return (label, relative angle). Relative angle: 0 = dead ahead,
    +90 = straight out of the right-hand windows, -90 = left-hand windows."""
    rel = (az - heading + 180) % 360 - 180
    if elev < VISIBLE_FROM:
        return "below horizon", rel
    if abs(rel) <= AHEAD_CONE or abs(rel) >= 180 - AHEAD_CONE:
        if elev > HIGH_SUN:
            return "overhead", rel
        return ("ahead" if abs(rel) <= AHEAD_CONE else "behind"), rel
    side = "right" if rel > 0 else "left"
    return (side + " (high)" if elev > HIGH_SUN else side), rel


def run(lat1, lon1, lat2, lon2, depart_utc, minutes, step):
    rows = []
    n = max(1, math.ceil(minutes / step))
    for i in range(n + 1):
        frac = i / n
        lat, lon = point_along(lat1, lon1, lat2, lon2, frac)
        if frac < 1:
            heading = bearing(lat, lon, lat2, lon2)
        else:  # at the destination, keep the direction of arrival
            plat, plon = point_along(lat1, lon1, lat2, lon2, 1 - 1e-4)
            heading = bearing(plat, plon, lat2, lon2)
        when = depart_utc + timedelta(minutes=minutes * frac)
        az, elev = sun_position(when, lat, lon)
        label, rel = classify(az, elev, heading)
        rows.append({"minute": round(minutes * frac), "utc": when.strftime("%Y-%m-%d %H:%M"),
                     "lat": round(lat, 2), "lon": round(lon, 2), "heading": round(heading),
                     "sun_azimuth": round(az), "sun_elevation": round(elev, 1),
                     "sun_relative": round(rel), "sun": label})
    return rows


def segments(rows):
    segs = []
    for r in rows:
        low = r["sun"] != "below horizon" and r["sun_elevation"] <= LOW_SUN
        if segs and segs[-1]["sun"] == r["sun"] and segs[-1]["low"] == low:
            segs[-1]["end"] = r["minute"]
        else:
            if segs:
                segs[-1]["end"] = r["minute"]
            segs.append({"sun": r["sun"], "start": r["minute"], "end": r["minute"], "low": low})
    return segs


def hm(minutes):
    return f"{int(minutes) // 60}:{int(minutes) % 60:02d}"


def main():
    # let "--from -33.95,151.18" work: argparse would read a leading minus as an option
    argv = sys.argv[1:]
    for i in range(len(argv) - 1):
        nxt = argv[i + 1]
        if argv[i] in ("--from", "--to") and nxt[:1] == "-" and nxt[1:2].isdigit():
            argv[i] = argv[i] + "=" + nxt
            argv[i + 1] = None
    argv = [x for x in argv if x is not None]
    ap = argparse.ArgumentParser(description="Which side of the aircraft is the sun on?")
    ap.add_argument("--from", dest="origin", required=True, help="airport code from the built-in table, or lat,lon")
    ap.add_argument("--to", dest="dest", required=True, help="airport code from the built-in table, or lat,lon")
    when = ap.add_mutually_exclusive_group(required=True)
    when.add_argument("--depart", help="local departure time at the origin, YYYY-MM-DDTHH:MM")
    when.add_argument("--depart-utc", help="departure time in UTC, YYYY-MM-DDTHH:MM")
    ap.add_argument("--utc-offset", type=float,
                    help="origin's offset from UTC in hours on that date (e.g. 5.5 or -7); "
                         "needed with --depart when the origin is given as coordinates")
    ap.add_argument("--duration", required=True, help="flight time, e.g. 8:15 or 495 (minutes)")
    ap.add_argument("--step", type=float, default=None, help="minutes between samples (default: about 24 samples, at most 15 minutes)")
    ap.add_argument("--steps", action="store_true", help="also print the table of every sample")
    ap.add_argument("--json", action="store_true", help="print JSON instead of text")
    a = ap.parse_args(argv)

    lat1, lon1, tz1, name1 = parse_place(a.origin)
    lat2, lon2, _, name2 = parse_place(a.dest)
    minutes = parse_duration(a.duration)
    if minutes <= 0:
        sys.exit("Duration must be more than zero.")
    if a.step is not None and not (math.isfinite(a.step) and a.step > 0):
        sys.exit("--step must be more than zero.")
    if angle_between(lat1, lon1, lat2, lon2) * 6371 < 1:
        sys.exit("Origin and destination are the same place, so there is no direction of travel.")
    if a.depart_utc and a.utc_offset is not None:
        sys.exit("--utc-offset goes with --depart (local time), not with --depart-utc.")

    if a.depart_utc:
        depart_utc = parse_time(a.depart_utc, "--depart-utc").replace(tzinfo=timezone.utc)
    else:
        local = parse_time(a.depart, "--depart")
        if a.utc_offset is not None:
            depart_utc = (local - timedelta(hours=a.utc_offset)).replace(tzinfo=timezone.utc)
        elif tz1:
            try:
                from zoneinfo import ZoneInfo
                depart_utc = local.replace(tzinfo=ZoneInfo(tz1)).astimezone(timezone.utc)
            except Exception:
                sys.exit("No time zone data on this machine. Add --utc-offset HOURS or use --depart-utc.")
        else:
            sys.exit("With coordinates, give --utc-offset HOURS with --depart, or use --depart-utc.")

    step = a.step or min(15.0, max(5.0, minutes / 24))
    rows = run(lat1, lon1, lat2, lon2, depart_utc, minutes, step)
    segs = segments(rows)
    counts = {}
    for r in rows:
        counts[r["sun"]] = counts.get(r["sun"], 0) + 1
    share = {k: round(100 * v / len(rows)) for k, v in counts.items()}
    km = angle_between(lat1, lon1, lat2, lon2) * 6371

    left = sum(v for k, v in counts.items() if k.startswith("left"))
    right = sum(v for k, v in counts.items() if k.startswith("right"))
    dark = round(100 * counts.get("below horizon", 0) / len(rows))
    lp, rp = round(100 * left / len(rows)), round(100 * right / len(rows))
    if left == right == 0:
        shade = "the sun is never clearly on one side on this estimate, so the side does not matter for sun"
    elif left == right:
        shade = "no difference between the sides on this estimate"
    else:
        sunny, other = ("left", "right") if left > right else ("right", "left")
        shade = f"sun on the {sunny} for about {max(lp, rp)}% of the flight"
        if min(lp, rp):
            shade += f" and on the {other} for about {min(lp, rp)}%"
        shade += f"; the {other} is the shadier side"
        if max(lp, rp) < 20:
            shade += ", but the sun is on a side so briefly that it matters little"
    low_fb = [g for g in segs if g["low"] and g["sun"] in ("ahead", "behind")]
    if low_fb:
        shade += ". Low sun " + " and ".join(sorted({g["sun"] for g in low_fb})) + " for part of the flight (see the list)"
    if dark >= 50:
        shade += f". Dark for about {dark}% of the flight"
    shade += (f". Sun height at take-off {rows[0]['sun_elevation']:.0f} degrees, at landing "
              f"{rows[-1]['sun_elevation']:.0f} degrees (0 is the horizon; within a few degrees of 0 "
              f"means a delay could move sunrise or sunset into or out of the flight)")

    # Sanity guard: a duration far too short for the distance usually means hours were typed as minutes.
    if minutes > 0 and km / (minutes / 60.0) > 1300:
        sys.exit(f"A flight of {round(km)} km in {hm(minutes)} is not possible. "
                 f"Give the duration as hours:minutes (for example 8:00) or in minutes (480).")

    caveats = ["Great-circle estimate: real routes bend for winds, weather and airspace, "
               "and the minutes after take-off and before landing follow the runway.",
               "Departure time is treated as take-off; taxi time and delays shift the result."]
    if a.json:
        print(json.dumps({"from": name1, "to": name2, "depart_utc": depart_utc.strftime("%Y-%m-%d %H:%M"),
                          "duration_min": minutes, "distance_km": round(km), "segments": segs,
                          "share_percent": share, "summary": shade, "steps": rows,
                          "caveats": caveats}, indent=1))
        return

    print(f"{name1} -> {name2}  {round(km)} km great circle  take-off {depart_utc:%Y-%m-%d %H:%M} UTC  flight {hm(minutes)}")
    print("\nSun by part of flight (time since take-off):")
    for s in segs:
        note = "  (sun low: glare, or sunrise/sunset view)" if s["low"] else ""
        print(f"  {hm(s['start']):>5} to {hm(s['end']):>5}  {s['sun']}{note}")
    print("\nShare of samples: " + ", ".join(f"{k} {v}%" for k, v in sorted(share.items(), key=lambda kv: -kv[1])))
    print("Summary: " + shade)
    if a.steps:
        print("\n  time   lat     lon   heading  sun-az  sun-el  rel   sun")
        for r in rows:
            print(f"  {hm(r['minute']):>5} {r['lat']:6.1f} {r['lon']:7.1f}   {r['heading']:3d}     {r['sun_azimuth']:3d}   {r['sun_elevation']:5.1f}  {r['sun_relative']:4d}   {r['sun']}")
        print("  rel = sun direction against the nose: 0 ahead, +90 right windows, -90 left windows.")
    print()
    print("'(high)' = sun above 60 degrees: warmth on that side but little direct sun in the eyes.")
    print("'overhead' = high sun with no clear side.")
    print("'below horizon' = sun more than 4 degrees down (night, or deep twilight). From cruise height")
    print("the sun can still be seen on the horizon when it is up to about 4 degrees down.")
    for c in caveats:
        print("Note: " + c)


if __name__ == "__main__":
    main()

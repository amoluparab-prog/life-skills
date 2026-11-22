#!/usr/bin/env python3
"""When does direct sun reach a window that faces a given compass direction?

For a place, a date (or a range of dates) and the direction a wall or window
faces, works out sunrise, sunset and the times the sun is in front of that
wall. Without --facing it prints all eight compass sides, so the sides of a
building can be compared.

Standard library only. Examples:

  python3 sun_facing.py --lat 38.71 --lon -9.14 --date 2027-03-12 --tz Europe/Lisbon --facing SE
  python3 sun_facing.py --lat -33.86 --lon 151.21 --date 2027-01-05 --end 2027-01-09 --utc-offset 11 --facing 250
  python3 sun_facing.py --lat 60.17 --lon 24.94 --date 2027-06-20 --utc-offset 3

Limits (repeat these to the traveller):
  * It knows nothing about what stands in front of the window: other buildings,
    hills, trees, a balcony or overhang above. Low floors in dense streets may
    get far less sun than shown.
  * The facing direction is usually read off a map, so it is an estimate; an
    error of 20 degrees moves the times by roughly half an hour to over an hour.
  * Times are for a clear sky. Sun position is good to a fraction of a degree
    and sunrise and sunset to a minute or two (more near the poles).
"""
import argparse
import json
import math
import sys
from datetime import date, datetime, timedelta, timezone

COMPASS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
           "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
WORDS = {"NORTH": "N", "SOUTH": "S", "EAST": "E", "WEST": "W"}
EIGHT = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

HORIZON = -0.833   # sun's centre at sunrise and sunset, allowing for refraction
MIN_UP = 2.0       # below this the sun is too low to count as direct sun on a window
MAX_OFF = 80.0     # sun further than this from the facing direction only grazes the wall
STRONG_OFF = 45.0  # within this the sun shines well into the room


def parse_facing(text):
    """'SE', 'south-east', 'north west', 'NNW' or degrees from north -> degrees."""
    t = text.strip().upper().replace("-", " ").replace("_", " ")
    try:
        deg = float(t)
        if not math.isfinite(deg):
            raise ValueError
        return deg % 360
    except ValueError:
        pass
    key = "".join(WORDS.get(w, w) for w in t.split())
    if key in COMPASS:
        return COMPASS.index(key) * 22.5
    sys.exit(f"Could not read the facing direction '{text}'. Use a compass point "
             f"(N, NE, SSW, south-east) or degrees clockwise from north (0 to 360).")


def compass_name(deg):
    return COMPASS[int((deg % 360) / 22.5 + 0.5) % 16]


def parse_date(text, flag):
    try:
        return date.fromisoformat(text.strip())
    except ValueError:
        sys.exit(f"Could not read {flag} '{text}'. Use YYYY-MM-DD, for example 2027-03-12.")


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


def day_samples(day, lat, lon, to_utc):
    """One sample a minute from local midnight to the next: (minute, azimuth, elevation)."""
    start = to_utc(datetime(day.year, day.month, day.day))
    end = to_utc(datetime(day.year, day.month, day.day) + timedelta(days=1))
    n = int(round((end - start).total_seconds() / 60))  # 1380 or 1500 on clock-change days
    out = []
    for i in range(n + 1):
        az, el = sun_position(start + timedelta(minutes=i), lat, lon)
        out.append((i, az, el))
    return out, start


def spans(flags):
    """Runs of True in a list -> [(first index, last index)]."""
    res, begin = [], None
    for i, f in enumerate(flags):
        if f and begin is None:
            begin = i
        if not f and begin is not None:
            res.append((begin, i - 1))
            begin = None
    if begin is not None:
        res.append((begin, len(flags) - 1))
    return res


def off_angle(az, facing):
    return abs((az - facing + 180) % 360 - 180)


def analyse_day(day, lat, lon, to_utc, to_local):
    samples, start = day_samples(day, lat, lon, to_utc)

    def clock(i):
        return to_local(start + timedelta(minutes=i)).strftime("%H:%M")

    up = [el > HORIZON for _, _, el in samples]
    noon_i = max(range(len(samples)), key=lambda i: samples[i][2])
    info = {"date": day.isoformat(), "noon": clock(noon_i),
            "noon_height": round(samples[noon_i][2], 1),
            "noon_direction": compass_name(samples[noon_i][1])}
    if all(up):
        info["daylight"] = "sun up all day"
    elif not any(up):
        info["daylight"] = "sun does not rise"
    else:
        # found independently, because near the polar circles the sun can set
        # just after midnight and rise again an hour or two later
        rise = next((i for i in range(1, len(up)) if up[i] and not up[i - 1]), None)
        sset = next((i for i in range(1, len(up)) if not up[i] and up[i - 1]), None)
        info["sunrise"] = None if rise is None else clock(rise)
        info["sunset"] = None if sset is None else clock(sset)
        if rise is not None:
            info["sunrise_direction"] = f"{compass_name(samples[rise][1])} ({round(samples[rise][1])})"
        if sset is not None:
            info["sunset_direction"] = f"{compass_name(samples[sset][1])} ({round(samples[sset][1])})"
    return info, samples, noon_i, clock


def facing_result(facing, samples, noon_i, clock):
    lit = [el >= MIN_UP and off_angle(az, facing) <= MAX_OFF for _, az, el in samples]
    strong = [f and off_angle(az, facing) <= STRONG_OFF for f, (_, az, _) in zip(lit, samples)]
    lit_spans, strong_spans = spans(lit), spans(strong)
    total = sum(b - a + 1 for a, b in lit_spans)
    before = sum(1 for i, f in enumerate(lit) if f and i < noon_i)
    after = total - before
    if total < 20:
        kind = "no direct sun to speak of"
    elif before >= 0.8 * total:
        kind = "morning sun"
    elif after >= 0.8 * total:
        kind = "afternoon and evening sun"
    elif len(lit_spans) > 1 and before >= 60 and after >= 60:
        kind = "sun early and late, not at midday"
    elif before >= 0.65 * total:
        kind = "mostly morning sun"
    elif after >= 0.65 * total:
        kind = "mostly afternoon sun"
    else:
        kind = "sun through the middle of the day"
    res = {"facing": round(facing, 1), "facing_name": compass_name(facing), "kind": kind,
           "minutes_of_direct_sun": total,
           "direct_sun": [[clock(a), clock(b)] for a, b in lit_spans],
           "strongest": [[clock(a), clock(b)] for a, b in strong_spans]}
    if total:
        best = min((i for i, f in enumerate(lit) if f), key=lambda i: off_angle(samples[i][1], facing))
        res["most_direct_at"] = clock(best)
        res["sun_height_then"] = round(samples[best][2])
    return res


def hours(minutes):
    return f"{minutes // 60} h {minutes % 60:02d} min"


def spans_text(pairs):
    return ", ".join(f"{a} to {b}" for a, b in pairs) if pairs else "none"


def main():
    # let "--lat -33.86" style values through: argparse reads a leading minus as an option
    argv = sys.argv[1:]
    for i in range(len(argv) - 1):
        nxt = argv[i + 1]
        if argv[i] in ("--lat", "--lon", "--utc-offset") and nxt[:1] == "-" and nxt[1:2].isdigit():
            argv[i] = argv[i] + "=" + nxt
            argv[i + 1] = None
    argv = [x for x in argv if x is not None]

    ap = argparse.ArgumentParser(description="When does direct sun reach a window facing a given direction?")
    ap.add_argument("--lat", type=float, required=True, help="latitude, north positive (south negative)")
    ap.add_argument("--lon", type=float, required=True, help="longitude, east positive (west negative)")
    ap.add_argument("--date", required=True, help="first day, YYYY-MM-DD (the arrival day)")
    ap.add_argument("--end", help="last day, YYYY-MM-DD; the first and last days are both shown")
    ap.add_argument("--facing", action="append",
                    help="direction the window faces: a compass point (SE, north-west) or degrees "
                         "clockwise from north. Repeat for several sides. Omit to see all eight sides.")
    zone = ap.add_mutually_exclusive_group()
    zone.add_argument("--tz", help="time zone name of the place, e.g. Asia/Tokyo")
    zone.add_argument("--utc-offset", type=float, help="the place's offset from UTC in hours on those dates, e.g. 5.5 or -7")
    ap.add_argument("--json", action="store_true", help="print JSON instead of text")
    a = ap.parse_args(argv)

    if not (-90 <= a.lat <= 90 and -180 <= a.lon <= 180):
        sys.exit("Latitude must be between -90 and 90 and longitude between -180 and 180.")
    first = parse_date(a.date, "--date")
    last = parse_date(a.end, "--end") if a.end else first
    if last < first:
        sys.exit("--end is before --date.")
    if (last - first).days > 366:
        sys.exit("The dates are more than a year apart. Check them.")

    notes = []
    if a.tz:
        try:
            from zoneinfo import ZoneInfo
            zi = ZoneInfo(a.tz)
        except Exception:
            sys.exit(f"Time zone '{a.tz}' is not known on this machine. Use --utc-offset HOURS instead.")
        to_utc = lambda naive: naive.replace(tzinfo=zi).astimezone(timezone.utc)
        to_local = lambda utc: utc.astimezone(zi)
        zone_label = a.tz
    else:
        if a.utc_offset is None:
            # no zone given: fall back to the sun's own clock so the result is still usable
            off = round(a.lon / 15 * 4) / 4
            notes.append(f"No time zone given, so times use UTC{off:+g}, a guess from the longitude. "
                         f"The real clock time may differ by an hour or more: rerun with --tz or --utc-offset.")
        else:
            off = a.utc_offset
            if not -14 <= off <= 14:
                sys.exit("--utc-offset must be between -14 and 14 hours.")
        tzinfo = timezone(timedelta(hours=off))
        to_utc = lambda naive: naive.replace(tzinfo=tzinfo).astimezone(timezone.utc)
        to_local = lambda utc: utc.astimezone(tzinfo)
        zone_label = f"UTC{off:+g}"

    facings = [parse_facing(f) for f in a.facing] if a.facing else [EIGHT.index(n) * 45.0 for n in EIGHT]
    days = [first] if last == first else [first, last]
    caveats = [
        "Nothing in front of the window is taken into account: nearby buildings, hills, trees, "
        "or a balcony or overhang above can block the sun, most of all on low floors.",
        "The facing direction is an estimate if it was read off a map; 20 degrees of error moves the times by roughly half an hour to over an hour, depending on latitude and season.",
        "Clear-sky times. Direct sun counts from 2 degrees above the horizon and within 80 degrees of "
        "the facing direction; 'strongest' is within 45 degrees.",
    ]
    out = {"lat": a.lat, "lon": a.lon, "time_zone": zone_label, "days": [], "notes": notes, "caveats": caveats}
    for day in days:
        info, samples, noon_i, clock = analyse_day(day, a.lat, a.lon, to_utc, to_local)
        info["sides"] = [facing_result(f, samples, noon_i, clock) for f in facings]
        out["days"].append(info)

    if a.json:
        print(json.dumps(out, indent=1))
        return

    print(f"Place {a.lat:.2f},{a.lon:.2f}   clock times in {zone_label}")
    for n in notes:
        print("NOTE: " + n)
    for info in out["days"]:
        print(f"\n{info['date']}")
        if "daylight" in info:
            print(f"  {info['daylight'].capitalize()}.")
        else:
            rise = (f"sunrise {info['sunrise']} in the {info['sunrise_direction']}"
                    if info["sunrise"] else "sun already up at midnight")
            sset = (f"sunset {info['sunset']} in the {info['sunset_direction']}"
                    if info["sunset"] else "sun still up at midnight")
            print(f"  {rise[0].upper()}{rise[1:]}; {sset}.")
        print(f"  Sun highest at {info['noon']}: {info['noon_height']:.0f} degrees up, to the {info['noon_direction']}.")
        for s in info["sides"]:
            label = f"{s['facing_name']} ({s['facing']:g})"
            if a.facing:
                print(f"  Window facing {label}: {s['kind']}.")
                print(f"    Direct sun: {spans_text(s['direct_sun'])}  (total {hours(s['minutes_of_direct_sun'])})")
                if s["minutes_of_direct_sun"]:
                    print(f"    Strongest:  {spans_text(s['strongest'])}")
                    high = " (a high sun lights the sill more than the room)" if s["sun_height_then"] >= 60 else ""
                    print(f"    Most direct at {s['most_direct_at']}, sun {s['sun_height_then']} degrees up{high}.")
            else:
                print(f"  {label:<10} {s['kind']:<36} {spans_text(s['direct_sun'])}")
    print("\nLimits:")
    for c in caveats:
        print("  * " + c)


if __name__ == "__main__":
    main()

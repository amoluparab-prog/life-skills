# room-picker

Status: tested and reviewed (two test rounds, two independent reviews, every rubric line at 4). Edits made after the second test round and after each review, including a small change to the description, were checked by the author and the reviewers but not rerun by a fresh test session; see the testing record. Version 0.1.0.

## What it does

Helps a traveller work out which room to ask for at a hotel, guesthouse, resort or similar stay they have booked or are about to book, and how to ask for it. It works anywhere: it asks where the property is and looks up local detail (floor naming, how people contact a property, rules on accessible rooms) at the time, with no country as the default.

1. Asks, in one message and only for what is missing: the property and town, the dates, the room type and how it was booked, who is staying, and the top two or three things that matter (quiet, sleep, light, view, lift distance, step-free access, space to work, family needs). It asks whether any wish is in fact a need.
2. Looks up what public sources show about the building: the property's own site, a map with satellite and street views, recent guest reviews, local listings. Every statement is labelled **confirmed** (a named, dated source says it), **likely** (inferred, or from an old source) or **unknown**. Each unknown that matters becomes a question for the property.
3. Computes when direct sun reaches each side of the building on the dates, with a small bundled script, and passes on its limits.
4. Ranks up to three positions to ask for and what to avoid, as positions ("courtyard side, upper floors, away from the lift"), each with its cost.
5. Drafts a short polite request and says when to send it: when booking, again a few days before arrival, and at check-in.
6. Gives a check for the first ten minutes in the room and wording to ask for a change.

Rules it keeps: it never invents a floor plan, a room number or a numbering pattern; a request is a request and the property decides, so it never promises an outcome; no invented occasions, illnesses or complaints to win an upgrade; an access or medical need is stated plainly as a need, with written confirmation asked for, and is never ranked below a wish; it does not book, pay or contact the property. The traveller sends the request.

When little is known it says so. With no property named it gives general positions, a request that can be sent without knowing the building, and its questions, and it does not compute the sun for a made-up place. With no map view it gives the sun by compass direction and asks the traveller to check which side of the building that is.

## The sun script

`scripts/sun_facing.py` (Python standard library only) takes a latitude, a longitude, an arrival date and optionally a departure date, a time zone, and one or more facing directions (a compass point or degrees). It prints sunrise and sunset and, for each side, when direct sun reaches a window facing that way and when it is strongest.

```
python3 scripts/sun_facing.py --lat 38.71 --lon -9.14 --date 2027-03-12 --end 2027-03-15 --tz Europe/Lisbon --facing SE --facing NW
```

It is an estimate. It knows nothing about buildings, hills, trees or balconies in the way; the facing direction is usually read off a map, and 20 degrees of error moves the times by roughly half an hour to over an hour; times are for a clear sky; and it describes a side of a building, not which rooms are on that side. It was checked against cases that can be reasoned by hand (see the testing record), not against observations in real rooms.

## How it differs from similar public skills

A web search on 22 November 2026 found public skills for hotel search and booking, a skill for vetting hotels for an event's guest block, a hotel stay planner and a hotel receptionist role. None was found that picks a room position inside a property already chosen, computes sun on a side of the building, or drafts the request. room-picker is deliberately narrow: after the property is chosen, which room position to ask for and how. Nothing was copied from those skills.

## Example

> We've booked a standard double at the Hotel Example Quay in Lisbon, 12 to 15 March, through a booking site. I'm a light sleeper and I'd love morning sun. Which room do I ask for?

(The hotel is invented; the sun figures are the script's real output for those coordinates and dates.)

The reply, in outline: a one-line answer first. Then what was found about the building, each item labelled: say, six floors and a street-level bar open late (confirmed, the property's site), a tram street on the north-west side and a courtyard on the south-east (likely, from the map and reviews), lift position unknown. The sun: a south-east window gets direct sun from about 07:10 to 14:25; a north-west window gets none until about 15:45. So ask for the courtyard side on a higher floor, away from the lift and not directly above the bar; the cost is no street view. Then the request, to send now, again a few days before arrival, and to repeat at check-in:

> Hello, I have a booking for 12 to 15 March (name, reference). I sleep lightly, so if possible I would be grateful for a room on the courtyard side, on a higher floor and away from the lift. I understand it depends on availability. Thank you.

It closes with the ten-minute check, the wording for asking to move, and the unknowns as questions for the property.

## Not for

Choosing which hotel, area or city to stay in, or planning a whole trip (trip-companion in this collection); a flight seat (seat-picker in this collection); finding or choosing a flat or house to live in; meeting rooms and event venues.

## Sources and credits

Public pages, opened by the author on 22 November 2026 and summarised in the author's own words. Across the two reviews, every one was also opened by a reviewer and found to match.

1. Benjamin Markham, "Inhospitable Hospitality: How to Avoid a Noisy Hotel", Acentech, 21 Jun 2017: https://www.acentech.com/resources/inhospitable-hospitality-avoid-noisy-hotel/
2. AARP, "How to secure a quiet hotel room" (no byline or date shown): https://www.aarp.org/travel/travel-tips/lodging/secure-a-quiet-hotel-room/
3. Marshall Loeb, "A quick guide for finding a quiet hotel room", CBS News / MarketWatch, 28 Dec 2007: https://www.cbsnews.com/news/a-quick-guide-for-finding-a-quiet-hotel-room
4. Christopher Elliott, "How to find the best, and avoid the worst, hotel room", Elliott Report, 21 Oct 2018: https://www.elliott.org/advice/how-to-find-the-best-hotel-room/
5. Pierre Boettner, "When it comes to room assignments, details matter", Hospitality Net, 3 Mar 2016: https://www.hospitalitynet.org/opinion/4074675.html
6. John Morris, "Rules for ADA hotel room reservations", Wheelchair Travel, 19 Nov 2017, updated 18 Feb 2025: https://wheelchairtravel.org/hotels-ada-room-reservations/ (the legal part is specific to one country; the skill uses only the practice: name the exact feature, get it confirmed in writing, look up local rules)
7. NOAA Global Monitoring Laboratory, "Solar Calculation Details": https://gml.noaa.gov/grad/solcalc/calcdetails.html (method from Jean Meeus, "Astronomical Algorithms")

One further page could not be opened and was not used. Three others were seen only as search results and not relied on.

The script uses the standard low-precision sun-position method named in source 7, written from general knowledge and checked numerically, not compared line by line with a published listing.

The author's own judgement, not taken from a source: the three labels and what counts for each; the timing "when booking, two to four days before, at check-in" (sources say early, a check before arrival, and at check-in; the day range is the author's); the ten-minute check beyond noise; the general patterns for where lifts, stores and service areas sit (only partly from sources 1 to 3); corner rooms as a trade-off; the remark that third-party and group bookings may carry less weight; the ship cabin line; allowing a well-known city's coordinates from memory for sun times if said; and the script's thresholds (direct sun counted from 2 degrees up and within 80 degrees of the facing direction, "strongest" within 45 degrees, and a sun above about 60 degrees lighting the sill more than the room).

## Testing record

See [testing/room-picker.md](../testing/room-picker.md).

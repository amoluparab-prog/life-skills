# seat-picker

Status: tested and reviewed (two test rounds, two independent reviews, every rubric line at 4 or above). Small edits made after the last test round and the last review were checked by the author only; see the testing record. Version 0.1.0.

## What it does

Helps a traveller choose the best seat on one specific flight from the seats that are actually still available.

1. Asks, in one message and only for what is missing: the flight (airline, number and date, or route, date and time), the cabin, the seats available (a screenshot of the airline's seat map or a typed list), who is travelling, and what matters (window or aisle, legroom, sleep, quick exit, views, sun, lavatories and galleys, children, height, nervous flyer, budget for a paid seat).
2. Looks up the aircraft and the cabin layout for that flight. It never states a layout from memory, says when an airline flies several versions of the same aircraft, and reminds the traveller that aircraft get swapped.
3. Checks public seat-map references for misaligned or missing windows, limited recline, reduced under-seat space, lavatories and galleys, bassinet positions and exit rows. What is available always comes from the airline's own seat map.
4. Computes which side of the aircraft the sun will be on with a small bundled script (great-circle path, sun position at each step), and passes on its limits.
5. Names a likely side for views only when a source supports it, and marks it as likely.
6. Recommends up to three available seats, each with the reason and the trade-off, names seats to avoid, and gives dates to re-check. If the session has reminder or calendar tools it offers reminders; it does not create them unasked.

Rules it keeps: the traveller selects and pays for the seat; exit rows carry legal duties, so they are never suggested for a party with children or anyone needing assistance; children stay beside an adult from their party before any other preference; anything uncertain is said to be uncertain.

## Which seat-map sites it prefers (checked November 2026)

- The airline's own seat map: the only source for availability.
- aeroLOPA: to-scale maps with window positions; preferred for seat detail.
- SeatMaps.com: wide coverage and flight-number lookup; fine for a quick check, reported to be generic or wrong for some airlines.
- ExpertFlyer: shows the configuration scheduled for a flight and seat alerts; the useful parts are paid.
- SeatGuru: closed in 2025, with no updates since early 2020. Not used.

These change. The skill tells Claude to search again if a site has gone or looks stale.

## The sun-side script

`scripts/sun_side.py` (Python standard library only) takes an origin and a destination (an airport code from a small built-in table, or `lat,lon`), a departure time and a duration. It steps along the great-circle path and reports for each part of the flight whether the sun is on the left, on the right, ahead, behind, high, or below the horizon.

```
python3 scripts/sun_side.py --from LHR --to JFK --depart 2026-12-14T08:25 --duration 8:10
```

It is an estimate. Real routes bend away from the great circle for winds, weather and airspace, the first and last minutes follow the runway, and a delay shifts everything. It was checked against cases that can be reasoned by hand (see the testing record), not against observations on real flights.

## How it differs from similar public skills

A public "seatmaps" skill exists in borski/travel-hacking-toolkit: it looks up seat maps and seat dimensions by browser automation, for research. Other public skills cover flight booking screens or ExpertFlyer lookups. seat-picker is narrower: advice from the seats the traveller can actually still take, weighed against what they said matters, with a computed sun side, and no tooling beyond web search and Python. Nothing was copied from those skills.

## Example

> BA 117 Heathrow to New York on 14 December, economy. Free seats left: 28A, 30K, 35C, 41A, 41K, 52K. I'm 6'2", want to sleep, hate the sun in my eyes. Won't pay extra.

The reply, in outline: a one-line answer first. Then the aircraft and layout version found for that flight, with the source and how sure it is. Up to three of the six seats, best first, each with a reason and a trade-off; for this traveller a right-side window clear of the lavatories comes first. Which of the six to avoid and why. The sun result (for an 08:25 departure the script puts the sun on the left for the whole flight, low for the first half, so the K side is shadier), with its limits. Dates to re-check the seat map and when check-in opens.

## Not for

Concert, theatre, cinema or stadium seats; train, bus or ferry seats; finding, comparing or booking flights; planning a whole trip (trip-companion in this collection).

## Sources and credits

Public pages, read on 21 November 2026 through a summarising fetch tool (not verbatim) unless marked otherwise.

1. One Mile at a Time, "aeroLOPA & SeatMaps: The Best Websites For Airplane Seat Maps", 26 Dec 2025: https://onemileatatime.com/guides/aerolopa-seatmaps/
2. One Mile at a Time, "End Of An Era: SeatGuru Officially Shuts Down", 31 Oct 2025: https://onemileatatime.com/news/seatguru-shuts-down/
3. Going, SeatGuru alternatives guide, 20 Aug 2026: https://www.going.com/guides/seatguru-alternative
4. Australian Frequent Flyer, "Where to Find Accurate Airline Seat Maps", 12 Sep 2026: https://www.australianfrequentflyer.com.au/find-accurate-airline-seat-maps/
5. Executive Traveller, "SeatGuru has shut down, so is there an alternative?" (no date on the page): https://www.executivetraveller.com/news/seatguru-alternatives
6. aeroLOPA, the site's own description: https://www.aerolopa.com/seatguru-alternative
7. SeatMaps.com home page, the site's own description: https://www.seatmaps.com/
8. One Mile at a Time, "Which Side Of Plane Will The Sun Be On?", 6 Sep 2024: https://onemileatatime.com/insights/which-side-of-plane-sun/
9. US 14 CFR 121.585, Exit seating (read on Cornell LII): https://www.law.cornell.edu/cfr/text/14/121.585
10. FAA, "Flying with Children": https://www.faa.gov/travelers/fly_children
11. FAA, "About Child Restraint Systems": https://www.faa.gov/travelers/fly_children/about-child-restraint-systems
12. FAA Advisory Circular AC 120-87C, "Use of Child Restraint Systems on Aircraft", 24 Sep 2015: https://www.faa.gov/documentlibrary/media/advisory_circular/ac_120-87c.pdf
13. Emirates, seat selection terms (one airline's exit-row criteria, as an example): https://www.emirates.com/english/book/about-booking-online/emirates-seat-selection/terms-and-conditions
14. Emirates, "Travelling with infants" (one airline's bassinet page, as an example): https://www.emirates.com/es/english/family/on-board/travelling-with-infants/
15. US EPA Hydrologic Micro Services, solar calculator algorithms (says NOAA's solar calculator is based on Meeus, "Astronomical Algorithms"): https://qed.epa.gov/hms/meteorology/solarcalculator/algorithms/
16. NOAA Global Monitoring Laboratory, "Solar Calculation Details": https://gml.noaa.gov/grad/solcalc/calcdetails.html . The author could not open this page (the fetch was blocked); the second reviewer opened it and confirmed it names Meeus as the basis.

The script's sun-position coefficients are the standard low-precision ones from that method, written from general knowledge and checked numerically, not compared line by line with a published listing. The SunFlight site could not be opened by the author or the reviewer; what the skill says about it rests on source 8.

The author's own judgement, not taken from a source: that flight-status and schedule pages show what recently flew a flight number; matching row numbers and seat letters to pick the layout version; the usual suspects for poor seats (limited recline ahead of exits and in the last row, bulkheads with fixed armrests and no floor storage, equipment boxes under some seats), which the skill tells Claude to confirm per layout; "seat A is on the left on almost every airline"; bassinets being usually at bulkhead rows; the observation that seat-map sites keep seat detail in images; and the script's thresholds (a 20 degree cone for "ahead" and "behind", 60 degrees for "high", 10 degrees for "low", and the sun counted as visible down to 4 degrees below the horizon at cruise height).

## Testing record

See [testing/seat-picker.md](../testing/seat-picker.md).

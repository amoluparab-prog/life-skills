# day-in-city

Status: version 0.1.0. Three test rounds and three independent reviews were run. Correctness scored 3 at the third review with one required fix; that fix was made and a separate short re-check of that one line scored it 4. The other five lines scored 4 or 5. The edits made after the last test round have not been rerun.

## What it does

Plans one good day or half day out in a city or town, for a visitor or a local, in an order that works. You give the place and the date, and as much as you like about who is going (ages, mobility, energy), interests, budget, food needs, pace, and where and when the day starts and ends. It gives back, in this order:

1. The day: place, date and weekday, who, pace, assumptions, daylight and weather.
2. "If you only do three things."
3. A timed route: a few main stops and optional extras, with an arrive and leave time for each, and the distance, minutes and slack to the next.
4. Where and when to eat, with a backup.
5. What to book ahead, by when, and where.
6. A rain or tired version.
7. Costs per person and for the group, in the local currency.
8. Good to know: dress rules, customs, safety and access notes, each with its source.
9. To check before you go.
10. Sources read, with the date.

Rules it keeps:

- Opening hours, closed days, prices, ticket rules and step-free access are never assumed. Each fact is labelled "checked" (page and date), "from memory, to check" or "unconfirmed".
- No invented places. A place it doubts exists is left out.
- The stated pace and needs are limits. A full day holds 2 main stops at an easy pace, 3 at a steady pace and 4 at a full one; a half day 1 or 2. Every leg carries slack, and a stated walking limit is kept.
- Customs, dress rules and safety notes come only from the venue, the tourism office, the transit operator or government travel advice.
- No country is the default: it asks where, and looks up local hours, prices, currency and customs each time.
- It books nothing, pays nothing and contacts no one. Calendar entries only if asked.

If the place or the date is missing it asks for those and waits. With no web access it still plans, from well-known places only, says at the top that nothing was checked live, and puts the checks that could break the day first in the to-check list.

## How it differs from similar public skills

Many public skills plan whole trips, for example onewave-ai and gked2121 "itinerary-optimizer" (multi-stop trip routing with time allocations and buffer time), ailabs-393 "travel-planner" (a whole-trip planner with stored preferences, budget and packing) and apljacob "travel-agent" (a seven-phase trip workflow ending in a PDF). Others seen in a search listing but not opened: d-wwei "road-trip-planner", and "travel-planner" or "trip-planner" skills by auldsyababua, travisjneuman, alleneee, skywain, inematds and one listed on smithery. None found is scoped to a single day. This one is narrower on purpose: one day or half day in one place, built around the actual date (closed days, hours, daylight, weather) and the slowest person in the party, with a label on every fact, a rain or tired version, and no bookings. Nothing was copied from those skills.

## Example (place and venues invented)

> We have Saturday free in Port Calder with our kids, 6 and 9. Staying at the Gull Street guesthouse. One of us is vegetarian. Not too rushed.

The reply, in outline: assumptions on top (this coming Saturday, 09:30 to 18:00, easy pace at a 6-year-old's walking speed, two main stops). Three things: the Tidewater Museum's boat hall, the harbour ferry, the Saltmarket for lunch. Route: leave 09:30, 900 m walk with 10 minutes of slack; Tidewater Museum 10:00 to 12:00 at opening, with a sit-down snack (hours and family ticket checked on the museum's own page); lunch at the Saltmarket food hall 12:20 to 13:20 (vegetarian stalls checked; backup the museum cafe, from memory, to check); harbour ferry loop 13:40 to 14:25 as the sit-down break; Calder Gardens 14:45 to 16:00; a free hour; back by 17:25. Nothing must be booked. Rain or tired: swap the gardens for the museum's upper floors or the covered market. Costs per person and for four. To check: cafe hours, gardens entry, whether the lighthouse opens.

## Not for

A multi-day trip with flights and stays (trip-companion in this collection), a layover with an onward flight or train to catch (layover-plan), a weekend at home (weekend-plan), choosing dishes at a restaurant (menu-pick), a conference's sessions and people (event-plan), or which hotel room to ask for (room-picker). It will plan several days in one place, one day at a time, giving the shared notes once and a route for each day, but flights, stays and preparation are not its job.

## Sources and credits

Public pages, read on 22 November 2026 through a summarising fetch tool (not verbatim).

1. Reid's Guides, "Drawing up a daily itinerary": https://reidsguides.com/reidsengland/places/general/itineraries/itinerary-tips/the-daily-itinerary
2. Reid's Italy, "Getting the most out of each day": https://reidsitaly.com/itineraries/general/planning_days.html
3. Frommer's, "How to craft the perfect itinerary for any destination": https://www.frommers.com/trip-ideas/arts-and-culture/how-to-craft-the-perfect-itinerary-for-any-destination (read once; later the same day the link led to a category listing page, so this source is unverified)
4. Grantourismo, "How to Plan a Perfect Day Every Day on Your Next Trip: 10 Itinerary Planning Secrets": https://grantourismotravels.com/how-to-plan-a-perfect-day-on-your-next-trip-itinerary-planning/
5. Women on the Road, "A One-Day Trip To... How To Visit Any City If You Only Have One Day": https://www.women-on-the-road.com/?p=3425
6. Queensland Department of Transport and Main Roads, "Pedestrian characteristics": https://www.tmr.qld.gov.au/travel-and-transport/pedestrians-and-walking/guidance-and-resources/pedestrian-and-walking-guidance-and-resources/pedestrian-characteristics

The first two independent reviewers re-fetched sources 1, 2, 4, 5 and 6 and found them to support what is credited to them, with one exception: source 5 says to look for time-limited events and mentions pre-bought tickets, but does not plainly say to book them ahead (source 2 carries the booking rule). Source 3 could not be re-checked by either of them. The third reviewer made no fetches.

What the sources support: checking hours and closed days for the actual day before ordering, restaurants included (1, 2); earliest-opening first, late-closing last, the most popular sight at opening (1, 2, 4); grouping by area and budgeting travel time (1, 2); minor stops between major ones so they can be cut (1, 2); written arrive and leave times, small breaks and free time (1, 2, 4); eating near the sights with a backup and a market or shop option (4); a rest in the middle of the day (2, 4); a sunset stop (4, 5); one neighbourhood, not the whole city, and an indoor backup for rain (5); booking timed-entry sights ahead (2); and that walking speed varies widely with age and ability, from 1 to 6 km an hour (6).

The author's own judgement, not taken from a source: the caps on main stops by pace; planning speeds of 4 and 3 km an hour; slack of a quarter of each leg with a 10-minute floor, and wait plus 10 minutes for a timetabled ride on a day trip; a half day as four to five hours; about 500 m a walk for a walking difficulty given without a number; about two hours as the least worth having in a town on a half-day trip; 15 minutes for getting in; the 1 km walk cap for a small child; an hour's rest; the free hour; never two museums in a row and no more than two to three hours in one place (first seen in source 3, now unverified); the day-trip rule; the three labels and the no-web path; the access, customs and safety sourcing rules; the allergy wording; the rain and tired versions; the cost table; and the "three things" list. No tourism-board, venue or transit page is a source for the method; those are looked up each time the skill is used.

Testing in brief: three rounds, ten prompts in fresh sessions, all passed, and three independent reviews. Final scores: Relevance 5, Trigger clarity 4, Correctness 3, Usability 4, Brevity 4, Provenance 4.

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/day-in-city.md](../testing/day-in-city.md)

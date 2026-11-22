---
name: seat-picker
description: Helps a traveller choose the best seat on a specific flight from the seats actually still available. Looks up the aircraft and cabin layout, checks public seat maps for bad windows, limited recline, lavatories, galleys, bassinets and exit rows, computes which side of the plane the sun will be on, notes likely views, then recommends up to three available seats with trade-offs and names seats to avoid. Use when the user says things like "which seat should I pick on this flight", "is 23A a good seat on this plane", "which side of the plane for the view" or "to avoid the sun", "here's the seat map, what's the best one left", or shares an airline seat map. Not for concert, theatre, cinema or stadium seats; not for train, bus or ferry seats; not for finding, comparing or booking flights; and not for planning a whole trip (flights, stays, packing, getting to the airport), which is a trip planner's job. It never selects or pays for a seat; the traveller does that.
---

# Seat picker: the best seat still available on a flight

A good seat depends on four things that are easy to get wrong from memory: which aircraft actually flies the route, how that airline fitted its cabin, where the sun and the scenery will be, and what this traveller cares about. So look each one up or compute it, say how sure you are, and only recommend seats the traveller can still take.

## 1. Get the inputs (one message, only what is missing)

- **The flight:** airline, flight number and date; or route, date and departure time.
- **Cabin** (economy, premium economy, business, first).
- **Seats available:** a screenshot of the airline's seat map or a typed list, with prices if seats are charged.
- **Who is travelling:** how many, any children (ages) or anyone needing assistance, heights if legroom matters.
- **What matters most:** window or aisle, legroom, sleep, quick exit, views, avoiding sun, distance from lavatories and galleys, nervous flyer, and whether they will pay for a seat and how much.

Do not hold the answer hostage to a full form. Answer the question actually asked first, in a line or two, with whatever can already be looked up (airline and route are enough to start), then ask for the rest in the same reply, grouped as two or three short questions. Without a list of available seats, recommend kinds of seat (for example "a right-side window ahead of the wing") and ask for the list; do not invent seat numbers. If the user is away or says "just pick", state your assumptions (for example: solo adult, prefers a window, will not pay extra) and go on. If a screenshot cannot be read with confidence, say which rows are unclear and ask for a typed list; never guess which seats are free.

## 2. Find the aircraft and layout: look it up, never recall it

Airlines fit the same aircraft type in several ways, and layouts change, so a layout from memory is often wrong.

1. Find the aircraft type scheduled for that flight and date. What the traveller's own booking or app shows is the best source, so ask; otherwise use flight-status and schedule pages, and recent schedule-change reports. If sources disagree, go with the most recent dated one and say so. If the traveller's times differ from the public schedule, use theirs and mention the difference.
2. Find which version of the layout it is. Match the traveller's row numbers and seat letters (and, with a full map, the last row and exit rows) against the public maps. If more than one version fits, say so and give advice that holds for all, or list the difference.
3. If their seats fit no version (a row that does not exist, or a row in another cabin), say so plainly: the aircraft may have been swapped, a seat mistyped, or the row may be a pricier cabin. Recommend firmly only the seats you can place, make the rest conditional, and ask what aircraft type and last row their map shows.
4. Tell the traveller that airlines swap aircraft, sometimes on the day, so the seat map is worth re-checking a day or two before departure.

## 3. Check the seat-map references

What is available comes only from the airline's own seat map. For what each seat is like, use public references (checked November 2026; these change, so if one is gone or looks stale, search for what is current):

- **aeroLOPA**: maps drawn to scale with window positions. Prefer it for window alignment, legroom and how close a seat is to a lavatory or galley.
- **SeatMaps.com**: wide coverage, lookup by flight number or route, photos. Good for a quick check, but reported to be generic or wrong for some airlines, so confirm anything important elsewhere.
- **ExpertFlyer**: shows the configuration scheduled for a flight and can alert when a seat opens; the useful parts are paid.
- **SeatGuru**: closed in 2025 and not updated since early 2020. Do not rely on it or on old pages quoting it.

Look for: missing or misaligned windows, limited or no recline (often the row in front of an exit and the last row), reduced under-seat space (equipment boxes), fixed armrests and no floor storage at bulkheads, lavatory and galley noise and queues, bassinet positions, and exit-row conditions. If you cannot confirm a detail for this layout, say "not confirmed" instead of filling it in.

Seat-level detail on these sites is mostly in the map image, so fetching the page as text gives little more than row ranges. View the map as an image if you can (a browser or screenshot tool). If you cannot, say which details are not confirmed, give the traveller the link and tell them what to look at (is the window beside the seat, is a lavatory behind it). Details from a site not listed here are "reported", not confirmed.

## 4. Compute the sun side (do not guess)

Run the bundled script; intuition fails on long and polar routes.

```
# run from this skill's folder
python3 scripts/sun_side.py --from LHR --to JFK --depart 2026-12-14T08:25 --duration 8:10
python3 scripts/sun_side.py --from 12.99,80.17 --to SIN --depart 2026-12-14T23:10 --utc-offset 5.5 --duration 4:25
```

`--from` and `--to` take an airport code from the small built-in table or `lat,lon` (look the coordinates up). `--depart` is local time at the origin; with coordinates add `--utc-offset`, or use `--depart-utc`. `--duration` is the scheduled flight time (work it out from the departure and arrival times in UTC if needed; it is treated as time in the air, which is close enough). A latitude may be negative. Add `--steps` for the full table or `--json`. The output lists, for each part of the flight, whether the sun is left, right, ahead, behind, high, or below the horizon. Left and right are as seated facing forward; seat A is on the left on almost every airline, but confirm on the map.

Turn it into advice: to avoid glare and heat, pick the other side; for a sunrise or sunset, pick the sun's side during the "sun low" part. Always pass on the limits: it is a great-circle estimate, real routes bend for winds and airspace, and a delay shifts everything. If the sun is close to ahead or behind, or the split is near even, say the side does not matter much. If most of the flight is dark, say so, since that matters more for sleep than the side, and note when the sun is within a few degrees of the horizon at take-off or landing, because a delay could change it. If you cannot run code, say the sun side could not be computed and tell them to search for a public sun-side calculator (SunFlight is one; aeroLOPA's app has one among its paid features); do not offer a guess as a result.

## 5. Views: only when grounded

Skip this if the traveller did not ask about views. Name a side for scenery or the city on approach only if a source you found supports it for this route and airport, and call it "likely": the runway in use and the approach path change with wind and air traffic control. If you cannot ground it, say so. A window over the wing or with a misaligned frame spoils the view whichever side it is on.

## 6. Recommend

Lead with a one-line answer to what was asked, then give, in this order:

1. **The flight as you understand it:** aircraft, layout version, how sure you are, and where it came from.
2. **Up to three available seats**, best first, each with the reason and the trade-off, tied to what the traveller said matters. Fewer than three is fine when fewer are worth taking; if nothing left is good, say so and name the least bad.
3. **Seats to avoid** among those available, with why.
4. **Sun and views** in two or three lines, with the caveats.
5. **What to re-check and when.** If the session has reminder or calendar tools, offer (do not create unasked) two reminders: when online check-in opens (look up the airline's rule) and to re-check the seat map a day or two before departure. Without such tools, give the dates so they can set them.

## Rules

- **The traveller selects and pays.** Do not select, change or buy a seat, even with browser tools. Use the prices their seat map shows, and if they gave a budget but no prices, make the pick conditional ("24K if it is under 40 euros, otherwise 38H"); an airline's published price may be quoted only as a rough guide, labelled as such.
- **Exit rows carry legal duties.** The occupant must be willing and able to open the exit and help in an evacuation. Under US rules that excludes anyone under 15, anyone caring for small children, and anyone who cannot follow crew instructions or handle the door; other countries and airlines set their own (some say 16), so look up the operating airline's rule, and crew can reseat people. Mention this whenever you suggest an exit row, and never suggest one for a party with children or someone needing assistance.
- **Safety first for children and anyone needing assistance.** Keep each child beside an adult from their party before any other preference. Children cannot sit in exit rows, so neither can a child car seat; US guidance prefers a window seat for one and advises against an aisle seat, and airlines set their own approved positions, so tell them to confirm with the airline. Bassinets are fitted at a few positions only (usually bulkhead rows), are limited in number, must be requested from the airline, and have age, size or weight limits; look them up, and if the airline does not publish them, say so. For assistance needs, an aisle seat near a lavatory may matter more than quiet; ask.
- **No web access:** say you cannot verify the layout, ask the traveller for the aircraft type shown on their booking and what the airline's map marks (exits, lavatories, wings), give advice that holds on any aircraft (rows near exits and lavatories, sun side), and tell them where to check the rest.
- **Not a flight:** for train, bus, theatre or stadium seats, say this skill covers flights only; help in general terms if asked.

## Worked example

User: "BA 117 Heathrow to New York on 14 December, economy. Free seats left: 28A, 30K, 35C, 41A, 41K, 52K. I'm 6'2", want to sleep, hate the sun in my eyes. Won't pay extra."

1. Look up the aircraft scheduled for BA 117 on that date and match the traveller's rows to the layout version. Say what you found and that it can change.
2. On the to-scale map for that layout, check each of the six seats: window alignment, recline, what is behind and beside it.
3. Run `sun_side.py --from LHR --to JFK --depart 2026-12-14T08:25 --duration 8:10` using the real scheduled time. It reports the sun on the left for the whole flight, and low for the first half, so the right side (K seats) is the shadier one.
4. Reply in the order above: up to three seats from the six, for example a right-side window clear of the lavatories first for sleep and shade, with the trade-off (harder to get out; no extra legroom without paying); which of the six to avoid and why; the sun result with its limits; and the re-check dates.

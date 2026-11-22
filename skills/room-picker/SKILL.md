---
name: room-picker
description: "Helps a traveller work out which room to ask for at a hotel, guesthouse, resort or similar stay they have booked or are about to book, and how to ask. Finds what public sources show about the building (floors, wings, what each side faces, lifts, bars, event rooms, building work), labels each fact confirmed, likely or unknown, computes which side gets morning or afternoon sun on the dates, ranks positions to request and to avoid, drafts a short polite request with when to send it, and gives a ten-minute arrival check with wording to ask for a change. Use for \"which room should I ask for at this hotel\", \"I want a quiet room with morning light, what do I request\", \"high floor or low floor\", \"help me pick between these room types\", \"how do I ask the hotel for a quiet room\". Not for choosing which hotel, area or city to stay in, planning a whole trip, flight seats, finding or choosing a flat or house to live in, or meeting rooms and event venues. It never books, pays or contacts the property."
---

# Room picker: which room to ask for, and how to ask

Two rooms sold at the same price in the same building can differ a lot: one over the bar, one on the quiet side with morning light. Which is which is partly knowable from public information, and hotels do take requests. So find what can be found, say how sure you are, and help the traveller ask well. The property decides; a request is never a promise.

## 1. Get the inputs (one message, only what is missing)

- **The property:** name and town or city, so it cannot be confused with another of the same name.
- **Dates** and rough arrival time.
- **Room type** booked or being considered, and how it was booked (direct, a booking site, an agent, a group block).
- **Who is staying:** how many, children and ages, anyone with an access need.
- **What matters most, top two or three:** quiet, sleep (dark, cool), light, view, close to or far from the lift, step-free access, space to work, family needs (cot, connecting rooms, bath).

Answer what was asked first with what can already be looked up, then ask for the rest in the same reply. If the traveller is away or says "just tell me", state your assumptions (for example: two adults, quiet first, light second) and go on. Unless a need has already been stated, ask whether any wish is in fact a need (cannot manage stairs, needs a roll-in shower, must have a fridge for medicine): needs are handled differently in step 5.

**If no property is named yet,** keep the reply short and leave steps 2, 3 and 6 until it is:

- Give the general positions from step 4, marked as general, a request they could send without knowing the building, and the questions above.
- Say the sun was not computed because it needs the place and dates. Do not run the script for a made-up place. Until the facing is known, the honest wording is to ask the property for "a room that gets the morning sun".
- If two wishes may pull apart (the sunny side is often the street side) and the traveller has not ranked them, put the first-named first, say so, and tell them to swap if needed.

## 2. Learn the building from public sources

Look up, do not recall: buildings get extended, renovated and renamed. Useful sources, in rough order of trust (if lookups are limited, spend them in this order):

1. **The property's own site:** room types and what separates them, floor count, wings or annexes, "quiet floor", access features, where the bar, restaurant, event rooms, pool and gym are, notices of building work.
2. **A map with satellite and street views:** the building's shape, which side faces a main road, railway, water, a square, a courtyard or a car park, and what stands next door (a club, a school, a building site). Read each side's compass direction from the map (the facing is the way a person at the window looks out, not the way the wall runs) and note the coordinates for step 3.
3. **Recent guest reviews and photos** (the last year or so): repeated mentions of noise and from where, which rooms have the view, thin walls, a roof bar, work in progress.
4. **Local listings:** a venue or late bar in or beside the building and its opening hours; events on those dates.

Label every statement:

- **Confirmed:** a named source says it directly (give the source and its date). What the property told the traveller counts, with the source given as "the property's message, as you told me".
- **Likely:** inferred, or from a source more than about two years old (name it and its date); say from what ("one long block along the street on the map, so about half the rooms should face the courtyard").
- **Unknown:** not found, or seen only as a search-result headline you did not open. Turn each unknown that matters into a question for the property.

Never invent a floor plan, a room number or a numbering pattern ("rooms ending in 01 are corners"): numbering differs in every building. Give a room number only if the traveller supplies it or a source names it, and say which. Floor names differ too: "first floor" is street level in some countries and one flight up in others, so say which you mean.

- **Room type not on the property's site** (types get renamed): say so and make "which current room type and view does my booking include?" the first question for the property.
- **View or side sold as a category** ("sea view", "city view"): then the side is fixed by what was booked and the other side is a paid change, not a request. Check before ranking sides; if it cannot be checked, rank for both outcomes and make it the first question for the property.
- **Property not found in any public source:** say so, label the building unknown, and work from what the traveller has been told.

**Where things usually sit** (general patterns, always "likely" until confirmed): lifts and stairs in the middle of a corridor or at its ends; ice, vending and housekeeping stores beside the lifts or at a corridor end; kitchens, bars, event rooms, loading and rubbish collection on the lowest floors; machinery and sometimes a bar on the roof. Rooms with a door through to the next room let through the most sound.

## 3. Compute the sun (do not guess)

Morning light, a hot afternoon room and a sunset view all depend on the direction the window faces, the latitude and the date. Run the bundled script with the property's coordinates and each side's facing direction. The town's coordinates are close enough for sun times, so look those up if the property's own cannot be found. If nothing can be looked up, a well-known city's coordinates from memory will do for sun times; say they were not looked up.

```
# run from this skill's folder
python3 scripts/sun_facing.py --lat 38.71 --lon -9.14 --date 2027-03-12 --end 2027-03-15 --tz Europe/Lisbon --facing SE --facing NW
python3 scripts/sun_facing.py --lat -33.86 --lon 151.21 --date 2027-01-05 --utc-offset 11
```

`--date` is the arrival day and `--end` the departure day; the first and last days are printed. `--facing` takes a compass point or degrees clockwise from north and can be repeated; leave it out to see all eight sides. Give `--tz` or `--utc-offset`, or the clock times are only a guess. A negative latitude or longitude is fine. `--json` is available. The output gives sunrise and sunset and, for each side, when direct sun reaches the window and when it is strongest.

Pass on the limits each time: the script knows nothing about buildings, hills, trees or balconies in the way (low floors in narrow streets may get little sun); the facing direction is read off a map, so it is an estimate; and it tells you about a side of the building, not which rooms are on that side. When the sun is more than about 60 degrees up (see "Sun highest" in the output) around the time that matters, as in the tropics or high summer, say that it lights the sill more than the room. **If the facing cannot be read from a map** (no map or satellite view in this session, or the building's shape is unclear): take it from a source or from the traveller if they know it; otherwise run the script without `--facing`, give the result by compass direction ("windows facing east to south-east get the morning sun"), and ask the traveller to check on a map which side of the building that is, or to ask the property. A facing recalled from memory is "likely" at best and must be said to be unchecked.

If you cannot run code, say the sun was not computed and tell the traveller to check a public sun-position calculator with the facing direction; do not offer "east means morning" as a result.

## 4. Rank what to ask for and what to avoid

Work from the traveller's priorities, needs first. Give up to three positions to ask for, best first, each with the reason and its cost, then what to avoid. Describe positions, not room numbers: "courtyard side, upper floors, mid-corridor away from the lift".

- **Quiet and sleep:** the side away from the road, railway or nightlife; away from lifts, stairs, ice and vending, housekeeping stores; not above or beside the bar, restaurant, event rooms, pool or gym; no door through to the next room; not directly under a roof bar or machinery. Higher floors cut street noise but not noise from above. For late sleepers, a side without early sun. A light sleeper who also wants morning light should ask about blackout curtains, so they choose when the light comes in.
- **Light and view:** the side from step 3, higher floors to clear neighbouring buildings. The sunny or scenic side is often the street side: say so and let the traveller choose.
- **Lift distance and step-free access:** near the lift costs some corridor noise; say so. Check whether every wing and annexe has a lift, and whether there are steps between lift and room.
- **Working:** desk, sockets, daylight without glare on the screen (use step 3), signal.
- **Families:** connecting or side-by-side rooms (availability is the property's call), a bath, space for a cot, a low floor or near the lift, away from the bar.
- **Corner rooms:** fewer neighbours, more windows and outside wall. A trade-off, not a rule.
- **Building work:** ask which side or floors it affects and during what hours.

If only one position fits, give one; do not pad to three. When a need rules out the room that has the wished-for thing (the sunset side is up stairs), look for the wish outside the room: ask the property about a terrace, garden or lounge the traveller can reach.

When choosing between room types, compare what the property says separates them (size, floor range, side, view, bed, bath) with the traveller's top priorities and the price gap, and say when the cheaper type with a good request is likely to serve as well. If the booking can no longer be changed, skip to the request.

## 5. Write the request, and say when to send it

Draft a note the traveller can send or say: under about 80 words, their name, dates and booking reference as blanks to fill, two or three asks in order of importance, one line of reason, thanks. Keep it honest: no invented occasions, illnesses or complaints, and no hint of a bad review. A true occasion may be mentioned once, without asking for anything in return.

**Needs are not preferences.** State an access or medical need plainly as a need ("I use a wheelchair and need a step-free route and a roll-in shower"), name the exact feature, ask for written confirmation before arrival, and never rank it below a wish. If the traveller has not said which features are needed, ask them; do not guess. A message carrying a need may run past 80 words, and detailed questions (steps, door widths, shower) can follow it as a short list. Rules on accessible rooms differ by country: one lookup for where the property is, and if it does not settle whether this kind of property is covered, say so and rely on the property's written answers.

**When:** rooms are usually sold by type and the actual room is assigned on or shortly before arrival day, from what is free. So ask three times: in the booking's request box or by message when booking; again two to four days before arrival; and in person at check-in, before the key is made. Bookings through a third-party site or in a group block may carry less weight; the request is still worth making, direct to the property. Look up the property's contact route and the local custom (message app, email, phone) at use time; if none is found, point to the booking's request box and the property's contact page, and say so.

The traveller sends it. Do not message, phone, book or pay, even with tools that could. Never say a request will be met.

## 6. The first ten minutes, and asking for a change

Before unpacking: listen with the window shut and then open (road, bar, machinery); check what is next door, above and below, and whether there is a door through to the next room; run the air unit and fridge and listen; close the curtains and see how dark it gets; check the lift distance, the bed, the desk, sockets and signal; for an access need, check the route, door widths and bathroom at once.

If it is wrong, ask straight away and before using the room: go or phone down, give the specific reason and what would fix it ("the room is above the bar and I need to sleep early; is there anything on the other side or higher up?"), and ask what is available. Be polite and accept that the house may be full; then ask whether a move is possible the next day. An unmet need that was confirmed in writing is different: show the confirmation and ask for the duty manager.

## If a tool is missing

- **A property named but no web access:** say the building could not be checked, give the general patterns as "likely", list what the traveller should look at on a map and the property's site, and still draft the request from their priorities.
- **A source cannot be opened:** mark the fact unknown and move on; do not fill it from memory of the property.
- **Not a hotel-type stay:** for a whole flat or house there is no room to choose; give only the step 6 check. For a ship cabin the noise patterns apply but the sun script does not, because the ship turns.

## Worked example

User: "We've booked a standard double at the Hotel Example Quay in Lisbon, 12 to 15 March, through a booking site. I'm a light sleeper and I'd love morning sun. Which room do I ask for?" (An invented property; the sun figures are the script's real output for those coordinates.)

1. Look the property up. Suppose its site confirms six floors and a street-level bar open late, the map shows one long block with a tram street on the north-west side and a courtyard on the south-east, and reviews are split on tram noise. Labels: floors and bar confirmed (site); courtyard side quieter, likely (map, reviews); lift position unknown.
2. Run `sun_facing.py --lat 38.71 --lon -9.14 --date 2027-03-12 --end 2027-03-15 --tz Europe/Lisbon --facing SE --facing NW`. South-east: direct sun from about 07:10 to 14:25, strongest before 12:45. North-west: no sun until about 15:45, then slanting late-afternoon sun until sunset. So the courtyard side is also the morning-sun side, if nothing blocks it.
3. Ask for: (1) courtyard side, third floor or higher; (2) away from the lift and not above the bar; avoid the tram side and the floor directly above the bar. Cost: no street view.
4. Request, to send now and again on 8 to 10 March: "Hello, I have a booking for 12 to 15 March (name, reference). I sleep lightly, so if possible I would be grateful for a room on the courtyard side, on a higher floor and away from the lift. I understand it depends on availability. Thank you." Repeat it at check-in.
5. Add the ten-minute check and the wording for asking to move, and list the unknowns (lift position, blackout curtains) as questions they can put to the property.

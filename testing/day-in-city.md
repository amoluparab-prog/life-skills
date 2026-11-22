# Testing record: day-in-city

Status: version 0.1.0. Three test rounds and three independent reviews were run. Correctness scored 3 at the third review with one required fix; that fix was made and a separate short re-check of that one line scored it 4. The other five lines scored 4 or 5. The edits made after the last test round have not been rerun.

## How it was tested

Every test ran in a brand-new session that had not seen the drafting. Each session was given a list of 17 skill names and descriptions (this skill among its neighbours, and only this one available to open), chose a skill from the descriptions alone, followed the skill if chosen, saved its reply, and logged what was unclear. All sessions ran on 22 November 2026. Nothing was booked and no calendar entry was made. In rounds 1 and 2 three of the neighbours in the list (weekend-plan, menu-pick, event-plan) were not yet written, so one-line stand-in descriptions were used for them; round 3 used their real descriptions.

The skill is not a guided conversation (one reply, or one short question when the place or date is missing), so no full-conversation simulation was run.

## Round 1 (first draft)

| # | Prompt (short) | Web | Expected | Chosen (confidence) | Result |
|---|---|---|---|---|---|
| T1 | One perfect day in Lisbon, Saturday 5 December 2026, a couple, food and views, no pork, 09:00 to 19:00 | off | day-in-city | day-in-city (97) | Pass. Said nothing was checked live; 3 main stops and 3 extras; times added up inside the window with 10 minutes of slack on all 8 legs (the session's own sum check); lunch with backup; rain version, costs, three things, to-check list. |
| T2 | Half day by the Vienna State Opera, Monday 30 November 2026, 13:00 to 18:30, mother aged 74, no stairs, 10-minute walks, paintings and cake | on, 5 lookups | day-in-city | day-in-city (96) | Pass on the "to check" path only. Both page fetches were refused and both searches returned titles only, so no live page was read. One main stop; longest walk 9 minutes at 3 km an hour; a likely Monday closure flagged from memory; nothing called step-free. |
| T3 | Singapore layover, 13:05 to 21:40, onward flight | off | layover-plan | layover-plan (92) | Pass: day-in-city not chosen. |
| T4 | A weekend at home with chores, kids 5 and 8, one short park outing | off | weekend-plan | weekend-plan (93) | Pass: day-in-city not chosen. |

Pass criteria. T1: chosen; says nothing was checked live; every place and fact labelled; main stops within the pace cap; times add up with slack on every leg; lunch on the route with a backup and no pork; rain or tired version; labelled costs; three-things list; to-check list led by opening on that day; no question before planning; nothing booked. T2: chosen; 1 or 2 main stops; no walk over 10 minutes; nothing closed on Mondays planned as open; step-free claimed only from a venue or operator page; a sit-down break; labels and sources. T3 and T4: day-in-city not chosen.

Changes made after round 1, from the sessions' logs: the three labels defined and a single shared label allowed; unconfirmed places only as optional extras; slack is pausing time and a walking limit is measured on the walk alone; meals and breaks are not main stops; the 15 minutes for getting in sits inside the stop; rounding and hills; a needed break never inside an optional extra; what to do when an access need cannot be checked; a default for a window that starts at a meal time; safety notes with no source; "all ten parts, each as short as it can be".

## Round 2 (second draft)

| # | Prompt (short) | Web | Expected | Chosen (confidence) | Result |
|---|---|---|---|---|---|
| T5 | Saturday 28 November 2026 in Edinburgh, kids 4 and 10, lunch by 12:30, a rest after lunch, nut allergy, low cost, back by 17:00 | on, 6 lookups | day-in-city | day-in-city (96) | Pass, with live pages. Two official venue pages and a weather lookup were read; facts from them were labelled with the page and date, the rest "from memory, to check". Lunch at 11:45, an assumed one-hour rest, 2 main stops, back at 16:00 with the free hour in hand, slack on all four legs, times added up. Allergy wording given. Weak points: the rest began 45 minutes after lunch ended because of the trip back, and the holiday and event check for the date was left to the to-check list when lookups ran out. |
| T6 | "Half-day itinerary near my hotel", tomorrow afternoon, old buildings and coffee, bad knee; no place given | off | day-in-city | day-in-city (95) | Pass. Asked for the city and hotel and wrote no route. |
| T7 | Ten days in Japan from Toronto: flights, stays, preparation | off | trip-companion | trip-companion (95) | Pass: day-in-city not chosen. |

Pass criteria. T5: chosen; lunch at or before 12:30 and a rest after it; 2 or 3 main stops; back by 17:00; allergy wording; labels as defined; checked facts carry page and date. T6: chosen; asks for the place in one short message and invents no plan. T7: day-in-city not chosen.

Changes made after round 2: ask and wait when the place or date is missing; a need given without a number gets the careful reading, stated as an assumption; a half-day default of four to five hours; a lookup tool counts as checked and own calculations are estimates; with few lookups, the main stops' hours first; for a low budget, free stops and a picnic or market lunch.

## Independent reviews

Three fresh reviewers scored the skill against the Forge rubric (1 to 5). Each later one was given the review before it and the changes since; the third was also given the round 3 results.

| Line | Review 1 | Review 2 | Review 3 (final) |
|---|---|---|---|
| Relevance | 5 | 5 | 5 |
| Trigger clarity | 3 | 3 | 4 |
| Correctness | 3 | 3 | 3 |
| Usability | 3 | 3 | 4 |
| Brevity | 4 | 4 | 4 |
| Provenance | 3 | 3 | 4 |

Review 1 found: three skill names in the description for skills not yet written; several days in one place not visible in the description; a clash between the "unconfirmed" label and "leave it out"; a worked example that broke the rounding rule and the pace cap; no instructions for a day trip to another town; one failed page treated as no web; two rules on unsourced safety notes; a step 1 clash when the person is away and gave no place; and one source link that no longer reached its article. All were changed in the text.

Review 2 confirmed most of those as fixed, checked the worked example's arithmetic as correct on every leg, found no direct contradiction left, and scored the same four lines at 3 for new, smaller findings: an ambiguous word ("stay") in the new description sentence; optional extras on a half day with no time to take them from; "Good to know" possibly empty with no web; two small departures in the worked example; the research note still crediting the unverified source; and this record and the docs page not yet written at the time. All of these were changed afterwards.

Review 3 was done after round 3 and the four changes that followed it. It checked every fix asked for by review 2 as made, re-added the worked example's five legs and found them right, and found no flat contradiction. It held Correctness at 3 for one of the four untested changes: the sentence letting a half-day trip to another town run longer did not say what happens when the person stated the start or end time, so it pulled against the rule that a day that does not fit the time window loses stops. The reviewer gave the exact wording to settle it (lengthen to about two hours in the town; a stated start or end time still holds; if neither can move, say plainly what fits) and said the line would score 4 with it. That wording has been applied. It is **unreviewed and untested**, so the score stays as given, 3.

## Round 3 (extra round, on the text as it stood after review 2)

One extra round of three prompts was allowed, aimed at the text changed after round 2 and at the points the second review left open. The skills list for this round used the real, published descriptions of weekend-plan, menu-pick and event-plan in place of the earlier stand-ins.

| # | Prompt (short) | Web | Expected | Chosen (confidence) | Result |
|---|---|---|---|---|---|
| T8 | Half-day trip by train from Florence to Lucca "one day next week", two adults and a 4-year-old, vegetarian, back for dinner; the person is away and cannot answer | off | day-in-city | day-in-city (90) | Pass, with one rule broken openly. Planned for the next day that fitted the words and said so; said at the top that nothing was checked live; one main stop, no extras (they did not fit, as the half-day rule says); every walk under 1 km and ending at a seat, with a buggy and a taxi as fallbacks; return journey counted in the day; "Good to know" given as the one line saying nothing could be sourced; times added up. The day ran to 5 hours 50 minutes against the four to five hour half day, because the train with wait and quarter slack took 3 hours 50 on its own; the reply said so. It could not name the last train back without a timetable and put that check first. |
| T9 | Three days in Kyoto, Tuesday 1 to Thursday 3 December 2026, flights and hotel already booked, the writer and a mother of 68 with a bad knee, temples, gardens and tea | on, 5 lookups | day-in-city | day-in-city (85) | Pass. One places lookup returned weekly hours for seven places; all four fetches of official pages were refused and not retried, so this run exercised the partial-failure path: hours labelled checked with the source named, everything else "from memory, to check", failed pages named under Sources. Each day stayed in one area, two main stops or fewer, no walk over about 700 m, slack on every leg, times added up on all three days (the session's own sum check). Weak points: the reply was about 1,760 words because all ten parts were given for each day; the holiday and event check was skipped when lookups ran out and not mentioned; on day 3 the afternoon break was the lunch sitting. |
| T10 | Routing only, eight first messages judged one by one from the descriptions | off | see below | see below | 8 of 8 as expected, three of them at modest confidence. |

T10 in detail (skill chosen, confidence): "plan my stay, four nights, nowhere to sleep yet": trip-companion (88). "Three days in a city, flights and hotel booked, what each day": day-in-city (70). "Best things to do in a city", no day in view: none (65). "Plan my Saturday" from a local with washing and a food shop: weekend-plan (90). A ten-year resident wanting "a proper day out" doing the tourist sights: day-in-city (72). A menu photo at a restaurant: menu-pick (96). A free day in the city during a three-day summit: day-in-city (68). Nine and a half hours between flights: layover-plan (93).

Pass criteria. T8: chosen; a date picked and stated without asking; no-web statement; half-day extras rule followed; child walking cap with a named fallback; return journey handled; "Good to know" not left blank. T9: chosen over trip-companion; one day at a time; knee read carefully and stated; labels correct when some pages fail. T10: day-in-city for the booked three days, the resident's day out and the free day at a summit; not day-in-city for the other five.

What the round showed, and the four small changes made after it (not tested):

- For several days the skill did not say whether all ten parts are given per day. Now: assumptions, daylight and weather, "Good to know", the to-check list and Sources once for the stay; the rest per day. Where closed days decide nothing, one area per day.
- For a day trip: if the timetable cannot be read, say so and put that check first; a timetabled ride gets its wait plus 10 minutes of slack, not a quarter; if the journey leaves under about two hours in the town on a half day, say so and let the day run longer.
- "Short slow walks" for a bad knee now has a figure (about 500 m each, then a seat or a ride).
- When lookups run out, whatever could not be looked up (holiday, events, strikes) goes in the to-check list.

The description was **not** changed after this round, so the published description is the one that was routed in T10. The routing session noted three phrases that nearly pulled the wrong way; they are listed under open items and left as they are because the routing came out right.

## Open items

- **Draft: review open.** Correctness stood at 3 at the third and last review. The one fix it asked for has been applied but not re-scored.
- **Untested text.** The four changes made after round 3 (several days, day trip, the 500 m figure, lookups that run out) and the review 3 fix to the day-trip sentence have not been run in a test. T8 and T9 ran before them. The worked example is checked by reviewers' arithmetic only.
- **Three phrases in the description nearly pulled the routing session the wrong way** in T10, though every choice came out as expected: "a multi-day trip with flights and stays" (a booked three-day visit has flights and stays too), "a conference day" (a free day during a conference is not one), and "a weekend at home" beside "for a visitor or a local". The description was left as routed. Rewording them, and naming weekend-plan, menu-pick and event-plan in it, should wait for the next routing run; the description is at the 1,024-character limit.
- Three of the eight routing calls sat at 68 to 72 confidence, and each prompt was run once.
- Source 3 is unverified (its link now leads to a listing page).
- Replies are long: 1,200 to 1,400 words for one day, and about 1,760 for three days in T9. The several-days change was made to shorten that and is untested.
- Smaller points a test session had to settle for itself, with no rule: morning or afternoon for a half day, a crowded sight that opens before the default start, what "Eat" holds when no meal falls inside the window, and a wait figure for a taxi.

## What the tests do not show

- Live venue pages were read in one test only (T5: two official venue pages and a weather lookup). In T2 and T9 every page fetch was refused; T9 had one places lookup that returned weekly hours. No transit operator page, no timetable, no ticketing page, no map or journey planner and no official access page was ever read in a test.
- The calendar path was never exercised. The day-trip, several-days, away and partial-failure paths were each exercised once, in round 3, on the text before the last changes.
- No test used a small or little-documented town or a party with a wheelchair user, and only one (T9) was outside Europe and Singapore. Dress rules at a religious site were never sourced in a test.
- Travel times in the test replies were estimates; nobody walked the routes, and no plan was checked against the real opening hours on the day.
- Each prompt was run once, so the trigger results are single runs. Rounds 1 and 2 used stand-in descriptions for three neighbours.

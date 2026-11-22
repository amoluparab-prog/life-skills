# Testing record: seat-picker

Status: two test rounds and two independent reviews, 21 November 2026. Every rubric line is at 4 or above. Edits made after the second test round and after each review were checked by the author only (listed below).

## How it was tested

Each prompt was run by a fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (seat-picker among forge, bedrock, trip-companion, skill-creator, docx, deep-research and event-outfit), chose a skill from the descriptions alone, then opened seat-picker only if it had chosen it, followed it with live web search and Python, saved its reply and logged anything unclear. Prompts and pass criteria were written before any run. One prompt (02) simulated a whole conversation from a persona sheet, to test pacing.

## Prompts and pass criteria


**01 full-inputs (should trigger).** "I'm on Lufthansa LH 454 Frankfurt to San Francisco on 9 December, economy. The seat map shows these still free: 24A, 24K, 31D, 38H, 45A, 45K, 52C. I'm 6'3", I want to sleep and I hate having the sun in my face. I won't pay extra unless it's under 40 euros. Which one should I take?"
Pass: chooses seat-picker; looks the aircraft up and names source and confidence (no layout from memory); notes aircraft swaps; consults a current seat-map reference and not SeatGuru; runs sun_side.py and reports the result with its limits; recommends three seats only from the seven listed, each with reason and trade-off; names seats to avoid; flags any listed seat it cannot match to the layout; mentions exit-row duties if it suggests one; does not offer to select or pay; gives re-check timing.

**02 thin-conversation (should trigger; simulated conversation with a persona sheet).** "Is 23A a good seat? Delta, [city] to Amsterdam next month."
Pass: chooses seat-picker; first reply asks for the missing inputs in one message without a long form, and gives something useful already or says what it is looking up; by the end, a verdict on 23A, three seats from the persona's free list with trade-offs, a computed sun result, views only if grounded and marked likely; no more than three user turns needed.

**03 baby-exit-row (should trigger).** "Flying Mumbai to Dubai with my husband and our 10-month-old on Emirates EK 501, 5 December, leaves 4:30am, economy. Should we grab the exit row for the legroom or go for the bassinet seats? And which side of the plane avoids the sun?"
Pass: chooses seat-picker; says clearly the exit row is not allowed or suitable with an infant and why; explains bassinet seats (bulkhead, request from the airline, limits to confirm); runs the script and reports the sun is below the horizon for most or all of the flight, with limits; asks for the available seats; keeps the family together.

**04 near-miss-trip (should not trigger; aimed at trip-companion).** "Help me plan my trip to Tokyo in March: flights from Chicago, where to stay for 6 nights, what to pack, and when I should leave for the airport."
Pass: chooses trip-companion, not seat-picker.

**05 near-miss-concert (should not trigger; the boundary named in the seed).** "I'm booking tickets for a concert at the Royal Albert Hall. Which seats are better, the stalls or the circle? There are a few left in both."
Pass: chooses no skill (or at least not seat-picker).

## Results

### Round 1 (fresh relay sessions, 21 Nov 2026)

| Prompt | Chose | Confidence | Result |
|---|---|---|---|
| 01 full-inputs | seat-picker | 97 | Partial pass. Looked up the aircraft (sources disagreed: 747-8 vs A350-900; took the newest dated report), ran the script (sun on the left 91%, right is shadier), gave three seats from the list with trade-offs, avoid list, limits, re-check dates. Gaps: the typed seat list fits no layout of the scheduled aircraft and the skill had no instruction for that; aeroLOPA's seat detail is in images a text fetch cannot read, so window and recline stayed "not confirmed". |
| 02 thin-conversation | seat-picker | 97 | Partial pass. First reply gave a partial answer on row 23 plus four questions; recommendation reached after two user turns; script run (mostly dark). Gaps: persona's seats contradicted the public map (row 23 is a higher cabin, row 27 does not exist), so only one firm pick, "top three" could not be met; turn 2 long for a yes/no question; script summary line misleading when left and right are both tiny. |
| 03 baby-exit-row | seat-picker | 93 | Pass on safety (exit row ruled out, with the airline's own rule; bassinet explained; family kept together), script run (dark all flight). Gaps: no availability given, so no seat numbers; skill's "top three" did not cover that; nine A380 layouts could not be told apart; US age (15) differs from the airline's (16). |
| 04 near-miss-trip | trip-companion | 95 | Pass. |
| 05 near-miss-concert | none | 96 | Pass. |

Note on 01 and 02: the test seat lists were invented by the skill's author without checking them against the real layouts, so the mismatch was an accident of the test. It exposed a real gap, so it was kept.

### Fixes after round 1
SKILL.md: answer the question asked first and group the questions; kinds of seat when no availability is given; traveller's booking beats public schedule; newest dated source wins a conflict; new step for seats that fit no layout version; note that map sites keep seat detail in images, with a fallback; "up to three" seats; duration guidance; say when the flight is mostly dark; skip views when not asked and dark; airline's published prices only as a labelled guide; look up the operating airline's exit-row rule and bassinet limits.
Script: summary now gives shares of the flight, says when the sunny spell is too short to matter and when most of the flight is dark, and prints sun height at take-off and landing; the "sun low" flag is now per part of the flight instead of sticking to a whole segment. All hand-reasoned cases rerun and unchanged.

### Round 2: reruns of 01, 02, 03 (the description did not change, so 04 and 05 were not rerun)

| Prompt | Chose | Confidence | Result |
|---|---|---|---|
| r2-01 full-inputs | seat-picker | 97 | Pass. Resolved the aircraft conflict by the newest dated source and said so; used the new step for seats that fit no layout (rows 45 and 52 handled conditionally, asked for aircraft type and last row); ran the script and described the long low-sun stretch; pick made conditional on the 40 euro budget; exit row not suggested; no seat selected. Still open: the to-scale map image could not be viewed (text fetch gives row ranges only; the image host was refused by the network proxy), so seat-level details were "reported" from a site not on the skill's list and marked as such. |
| r2-02 thin-conversation | seat-picker | 97 | Pass. First reply answered the 23A question in a paragraph and asked three grouped questions; recommendation after two user turns: one firm pick (44A), two conditional on a zero price, 40B and 27J set aside with reasons; computed sun (82% dark, side does not matter); a grounded "possible" northern-lights side; re-check dates; reminders offered, not created. Still open: window alignment, wing and recline for the pick "not confirmed" because the map image could not be opened; reply 2 is still long for a yes/no question. |
| r2-03 baby-exit-row | seat-picker | 93 | Pass. Exit row ruled out using the airline's own rule (16+, no infants); bassinet explained with request route and limits marked unconfirmed; recommended a kind of seat and asked for the seat list; script run (dark all flight, landing shortly before sunrise). Still open: with eight or nine A380 layouts and no seat map from the traveller, bassinet rows could not be named; one figure (check-in opening) was given from general knowledge with a "confirm" label instead of being looked up. |

### After round 2
- Removed a stray scripts/__pycache__ folder left by a test run.
- Three small wording edits to SKILL.md, **not retested** (the two-round limit is reached): skip views whenever the traveller did not ask; lead the reply with a one-line answer; make the pick conditional when a budget is given without prices.

### What these tests do not show
- No test used a real screenshot of a seat map; reading availability from an image is untested.
- No test session could open a seat-map image, so the "view the map as an image" path is untested; every seat-level detail in the test replies is unconfirmed or "reported".
- The test seat lists were invented and did not match the real layouts, so no run shows the plain case where every listed seat fits.
- Reminder creation was only offered, never carried out.
- The sun script was checked against hand-reasoned cases, not against observations on real flights.
- Triggering was run once per prompt; no repeat runs.

### After review 1 (edits not retested by a fresh session; the two-round limit is reached)
- Description: "three" became "up to three" (one word; the trigger phrases and exclusions are unchanged).
- SKILL.md: sun-calculator fallback reworded; duration note; child car seat and bassinet lines reworded to match sources; one redundant rule removed.
- Script: accepts a negative latitude after `--from`/`--to`; clear one-line errors for bad input; each part of the flight now ends where the next begins; the summary mentions low sun ahead or behind. Hand-reasoned cases rerun by the author and unchanged; these are author checks, not fresh-session tests.

### After review 2 (author checks only)
- SKILL.md: "SunFlight is a long-standing free one" cut to "SunFlight is one".
- Script: rejects nan, inf, negative minutes and a date without a time; one error message corrected.

## Independent reviews

Two fresh reviewers scored the skill against a six-line rubric, strictly, from the brief, the skill, the research note with sources, and the test log. The second had the first review and the changed files.

| Line | Review 1 | Review 2 |
|---|---|---|
| Relevance | 5 | 5 |
| Trigger clarity | 4 | 4 |
| Correctness | 3 | 4 |
| Usability | 4 | 4 |
| Brevity | 4 | 4 |
| Provenance | 3 | 4 |

Review 1 required: accept a negative latitude on the script's command line (a real bug: southern-hemisphere coordinates failed); reword the sun-calculator fallback; source or soften the lines on non-US exit-row ages, child car seats and bassinets; make the description say "up to three"; cite only sources that were read for the sun maths; add the missing sources. All were done; review 2 marked one as partly fixed (two unsupported adjectives about SunFlight, since removed). Review 2 confirmed all eight script issues from review 1 as fixed and found no error in the sun or great-circle maths.

## Script checks (by the author; the reviewers reran several)

- Sun at 0N 0E at the March 2026 equinox noon: elevation 89.9 degrees. London at solar noon on 21 June: 61.9 degrees, due south (expected 90 - 51.5 + 23.4).
- New York JFK to London Heathrow: 5,541 km (published figure about 5,540).
- Eastbound at 40N at local midday: sun on the right. Westbound: left. Northbound in the morning: right; in late afternoon: left.
- Perth to Sydney at midday in June (sun in the north): left. Night flight: below horizon. Westbound on the equator at an equinox sunset: ahead.
- Date-line crossing (San Francisco to Tokyo): continuous path. Southern-hemisphere coordinates typed on the command line: accepted.
- Bad input (unknown code, bad duration or date, time-zone suffix, same origin and destination): a one-line message each.

## Open items

- The edits listed under "After round 2", "After review 1" and "After review 2" have not been run by a fresh session.
- No test session could open a seat-map image, so window alignment and recline stayed "not confirmed" in every test reply. The skill handles this honestly, but its best path is unproven.
- Reading availability from a real seat-map screenshot is untested.
- A guard was added to the sun-side script after both reviews: it now refuses a duration that is impossible for the distance (for example 8 typed for eight hours, which it would read as eight minutes). Checked by hand on three routes, not by a fresh session.
- Reply length: the second turn of the conversation test was long for a yes/no question.
- Optional, from the reviews: repeat trigger runs; near-miss tests for a train seat and for flight booking; tell Claude to read the step table when the sun is close to the nose or tail.

# Testing record: room-picker

Status: two test rounds and two independent reviews, 22 November 2026. Every rubric line is at 4. Edits made after the second test round and after each review, including a small change to the description, were not rerun by a fresh test session (listed below).

## How it was tested

Each prompt was run by a fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (room-picker among forge, trip-companion, bedrock, seat-picker, event-outfit, home-finder, big-buy, skill-creator, docx and deep-research), chose a skill from the descriptions alone, then opened room-picker only if it had chosen it, followed it, saved its reply and logged anything unclear. Prompts and pass criteria were written before any run. Sessions were told to treat the user as a stranger, to contact no business, and to keep web lookups to about six. The skill is not a guided conversation, so no multi-turn simulation was run.

## Prompts and pass criteria

**T1 full-property (should trigger; live web).** A "Deluxe Room" booked direct at a large, well-documented real hotel in Singapore, 3 to 6 February 2027, two adults, a light sleeper who would love morning light. "Which room should I ask for, and how do I ask?"
Pass: chooses room-picker; building facts each labelled confirmed, likely or unknown with a source; no invented room number or floor plan; the sun script actually run with the limits passed on; up to three positions to ask for and what to avoid; a request under about 80 words with no promise; when to send it; arrival check and change wording; hotel not contacted.

**T2 thin-no-web (should trigger; web access barred, so it can pass without live pages).** "I want a quiet room with morning light. What do I request?"
Pass: chooses room-picker; something useful first (general positions marked as general), missing inputs asked for in one grouped message; no invented property or facts; no "east means morning" given as a computed result; a request draft; no promise.

**T3 need-and-pressure (should trigger; rules under pressure).** An invented guesthouse in a real town in Sri Lanka, 10 to 14 January 2027; two room types as described in the owners' email (ground floor facing east, second floor facing west, no lift); the traveller's mother uses a wheelchair and loves a sunset; the traveller asks for a false anniversary to be put in the message.
Pass: chooses room-picker; step-free access treated as a need that decides the choice and stated plainly, with written confirmation of the specifics asked for; the false anniversary refused plainly and briefly; script run for east and west and reported honestly; facts not given by the user labelled unknown; property not contacted.

**T4 near-miss-area (should not trigger; aimed at trip-companion).** Which of two areas of a city to stay in with children, and which hotels are quietest.
Pass: does not choose room-picker.

**T5 thin-no-web-r2 (round two rerun of T2).** Pass: as T2, and a clearly shorter reply; no script run for an invented place; sun said to be not computed and why; request using "a room that gets the morning sun".

**T6 full-property-r2 (round two rerun of T1).** Pass: as T1, and the renamed room type and whether the view is a paid category raised before ranking sides; the facing read from a source or given by compass direction, with anything recalled said to be unchecked; script run with arrival and departure dates.

**T7 near-miss-flat (should not trigger; aimed at home-finder, worded close to a trigger phrase).** "I'm moving to Porto for a year and want a quiet flat with morning light. There are three listings I like in the same building, on different floors and sides. Which one should I ask the agent for, and what should I check at the viewing?"
Pass: does not choose room-picker.

## Results

### Round 1 (four fresh sessions)

| Prompt | Chose | Confidence | Result |
|---|---|---|---|
| T1 full-property | room-picker | 97 | Pass, with gaps. Labels and sources given, no room numbers, script run, request about 75 words, timing, arrival check, hotel not contacted. Gaps: the session had no map tool, so coordinates and facing came from recall and were labelled "likely" (the skill had no path for web without a map); the booked room type is no longer on the hotel's site (skill silent); no review content obtained. |
| T2 thin-no-web | room-picker | 95 | Pass. General positions marked likely, request draft, grouped questions, no invented property. Gaps: skill silent on "code runs but place and dates are missing", so the session ran the script for an illustrative city; reply long (about 760 words) for a one-line question. |
| T3 need-and-pressure | room-picker | 95 | Pass. Ground-floor room chosen on the need; anniversary refused in three sentences; script run; need stated plainly with written confirmation; property not found in any source and labelled unknown; a sunset for the mother looked for outside the room. Gaps: no label for facts from the property's own email; no rule for coordinates when the property is not found; the 80-word cap against the needs rule; floor naming by country. |
| T4 near-miss-area | trip-companion | 70 (95 that room-picker does not apply) | Pass. |

### Fixes after round 1
No property named: short reply, sun not computed, no made-up place, "a room that gets the morning sun". Facts from the property's message count as confirmed with that source named. Floor naming differs by country; renamed room types; view sold as a category; property not found. Town coordinates are enough for sun times; the script's date arguments are arrival and departure day. No map: facing from a source or the traveller, otherwise all sides by compass direction and the traveller checks. Blackout curtains for a light sleeper who wants morning light. One position is fine; a wish blocked by a need can be looked for outside the room. Needs: ask which features, the message may pass 80 words, one lookup for local rules.

### Round 2 (three fresh sessions)

| Prompt | Chose | Confidence | Result |
|---|---|---|---|
| T5 thin-no-web-r2 | room-picker | 95 | Pass. About 550 words; script not run; sun said to be not computed and why; request with "gets the morning sun"; grouped questions; no promise. Logged as unclear: the no-property and no-web branches overlapped; two wishes given without a ranking. |
| T6 full-property-r2 | room-picker | 98 | Pass. Renamed room type and view category raised first, ranking given for both outcomes; facing taken from a named 2018 review and said not to be measured from a map; script run for arrival to departure; the hotel's own notice of building work from January 2027 found and built into the asks; request about 70 words; no contact made. Shortfalls: coordinates from memory (lookups used up), no map view, no review from the last year, one remark from memory flagged as unchecked and one climate remark from memory not flagged, seven lookups against "about six". |
| T7 near-miss-flat | home-finder | 80 | Pass. |

T3 and T4 were not rerun (limit of three prompts in round two; the description had not changed at that point).

### After round 2 (not rerun by a fresh session)
- The no-property branch holds with or without web access; unranked wishes: first-named first, and say so.
- A source more than about two years old is "likely"; a search-result headline not opened is "unknown".

### After review 1 (not rerun by a fresh session; the two-round limit was reached)
- Removed an unsourced line about arriving early in the day.
- Worked example: "only a grazing sun" replaced with "no sun until about 15:45, then slanting late-afternoon sun".
- Script caveat: "about an hour" replaced with "roughly half an hour to over an hour, depending on latitude and season".
- Added: high sun lights the sill more than the room; a well-known city's coordinates from memory are acceptable if said; the facing is the way the window looks out; lookup priority; what to do when a view category cannot be checked or no contact route is found; a ship cabin line.
- The no-property paragraph split into bullets; "plant" replaced with "machinery".
- Description: exclusions shortened, and "finding a flat or house" became "finding or choosing a flat or house" (1,002 characters). The trigger phrases are unchanged.

### After review 2 (author checks only)
- Worked example: "ground-floor" and "first floor" reworded so the example keeps the skill's own floor-naming rule.
- The high-sun sentence now points to the "Sun highest" line of the script's output.

## Independent reviews

Two fresh reviewers scored the skill strictly against a six-line rubric, from the brief, the skill and script, the research note with sources, and the test log. The second had the first review and the changed files.

| Line | Review 1 | Review 2 |
|---|---|---|
| Relevance | 4 | 4 |
| Trigger clarity | 4 | 4 |
| Correctness | 4 | 4 |
| Usability | 4 | 4 |
| Brevity | 4 | 4 |
| Provenance | 4 | 4 |

Neither review required a fix. Review 1 listed three small wording corrections (the early-arrival line, "grazing sun", "about an hour") and several optional gaps; all three corrections and most of the gaps were acted on. Review 2 confirmed every change as described, found no factual error and no contradiction, and held all six scores. Between them the reviewers opened all seven sources and found them to match the research note.

## Script checks (by the reviewers, by hand)

- Lisbon, 12 March 2027: sunrise 06:53, sunset 18:41, noon height 48 degrees (expected 90 - 38.7 - 3.5); matches the worked example.
- Sydney, 5 January 2027: noon sun 79 degrees up to the north (expected 78.7); a south window gets sun early and late only. Sydney, 21 June 2027: noon 33 degrees; north window all day, south window none.
- Tromso, 21 June 2027: sun up all day, midnight sun 3 degrees up on the north side. 21 December 2026: sun does not rise.
- Reykjavik at midsummer: rise 02:56, set 00:04, against published times about a minute different.
- Quito at the March equinox: sun overhead at noon; east morning, west afternoon.
- Singapore, 10 February 2027: noon 74 degrees (expected 74.3).
- Bad input (latitude 95, a date in the wrong format, an unknown facing or time zone): one plain sentence each.

## What these tests do not show

- **Paths never exercised with live pages or tools:** no test session had a map or satellite view, so reading a building's facing from a map, the skill's main path, has never been run. No session obtained recent guest reviews. The "cannot run code" path was not run.
- Not tested: family, working-space and lift-distance priorities; a booking made through a third-party site; a choice between several room types with a price gap; a ship cabin; the change-of-room wording in use.
- Every edit listed under "After round 2", "After review 1" and "After review 2", including the description change, was checked by the author and (for the first two) by a reviewer, not by a fresh test session.
- Triggering was run once per prompt; no repeat runs. Three near-miss boundaries were not tried: a flight seat, a whole trip plan, a meeting room.
- The script was checked against hand-reasoned cases, not against observations in real rooms.

## Open items

- Run one session with a map view, one with code barred, and rerun T3, T7 and one should-trigger prompt against the current text and description.
- Ship cabins are covered by one sentence in the body and are not named in the description.
- Optional, from the reviews: give the no-map fallback its own paragraph; say that general remarks from memory (climate, local habits) are from memory; the script's "strongest" span ignores the sun's height, and near the polar circles a sunset just after midnight prints after the sunrise.

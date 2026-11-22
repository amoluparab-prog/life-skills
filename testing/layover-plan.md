# Testing record: layover-plan

Status: two test rounds and two independent reviews, 22 November 2026. Every rubric line is at 4 or above. Edits made after the second test round and after each review were checked by the author only (listed below).

## How it was tested

Each prompt was run once by a fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (layover-plan among trip-companion, seat-picker, room-picker, event-outfit, forge, bedrock, skill-creator, docx, deep-research, and one-line stand-ins for the planned day-in-city and weekend-plan), chose a skill from the descriptions alone, then opened layover-plan only if it had chosen it, followed it, saved its reply and logged anything unclear. Prompts and pass criteria were written before any run. The user could not answer follow-up questions in any run. Web runs were limited to about six lookups; two runs had no web access at all, to test the "to confirm" path.

The skill is not a guided conversation (one batch of questions at most, then the plan), so no full conversation was simulated.

## Prompts and pass criteria

**01 full-daytime (should trigger; web allowed).** "I land at Singapore Changi at 06:05 on Tuesday 12 January 2027 from Sydney, into Terminal 3, and my flight on to London leaves at 16:10 from Terminal 1. It's all one ticket and my suitcase is checked through to London. Australian passport, no visas for anywhere. I'll have slept a bit on the plane, I like food markets and gardens, and I don't want to spend much. My mum is with me, she's 71 and fine but walks slowly. What can we do with the day?"
Pass: chooses layover-plan; a table of steps in minutes that adds up to the 605 minute gap; clock times that agree with it; one verdict; turn-back and latest set-out times; the entry rule cited to an official page read in the run or marked to confirm; a 90 margin for mobility; cost of a miss; a stay plan; airport facilities named only if read on a page; a confirm list; nothing booked.

**02 five-hours-no-web (should trigger; no web access).** "Is it worth leaving the airport on a 5 hour connection in Frankfurt? I'm flying Delhi to Toronto next month, Indian passport, land 07:20 and leave 12:25. I'd love to see a bit of the old town if I can."
Pass: chooses layover-plan; states no entry or transit rule as fact; sums shown; verdict stay airside; says staying airside may itself need a transit visa, to confirm, and with whom; puts the missing facts as questions and goes on with stated assumptions; no invented facility names.

**03 near-miss-day (should not trigger).** "We're in Lisbon for a week and next Saturday is completely free, nothing booked and no travel that day. Two adults, we like tiles, viewpoints and seafood. Can you plan the day for us?"
Pass: does not choose layover-plan.

**04 near-miss-missed (should not trigger).** "My first flight was late and I've just missed my connection in Chicago. The next flight they're offering is tomorrow afternoon. What are my options and what should I ask the airline for?"
Pass: does not choose layover-plan.

**05 five-hours-no-web-r2 (round 2 rerun of 02).** Same prompt, after the round 1 fixes.
Pass: as 02, with the transit visa item at the top by instruction, stay-verdict clock times, no outside plan, shorter.

**06 overnight-kids-separate (round 2, new; should trigger; web allowed).** "Plan my long stopover please. We land at Istanbul Airport (IST) at 21:40 on Friday 5 February 2027 from Manchester and our next flight, to Tbilisi, leaves at 09:15 the next morning. They're two separate bookings on different airlines, so we have to pick up our two suitcases and check them in again. It's me, my husband and our kids aged 4 and 8, all British passports. We'll be shattered. Is it worth going into the city, or getting a hotel, or do we just camp in the airport? We'd rather not spend a fortune."
Pass: chooses layover-plan; entry rule cited to an official page or marked to confirm, flagged at the top because they must enter to collect bags; a bag-drop line in the sums; margin 90; steps down for night, children and tiredness; separate-ticket cost of a miss; night points; no invented hotel or lounge names; nothing booked.

**07 near-miss-short (round 2, new; should not trigger).** "I'm looking at a flight to Lima with a 55 minute connection in Amsterdam, or another one with a 2 hour 40 connection in Madrid that costs a bit more. Is 55 minutes enough to change planes, and which would you book?"
Pass: does not choose layover-plan.

## Results

| Round | Prompt | Chose | Confidence | Result |
|---|---|---|---|---|
| 1 | 01 full-daytime | layover-plan | 97 | Pass, with findings |
| 1 | 02 five-hours-no-web | layover-plan | 97 | Pass, with findings |
| 1 | 03 near-miss-day | day-in-city | 93 | Pass (stayed quiet) |
| 1 | 04 near-miss-missed | trip-companion | 82 | Pass (stayed quiet) |
| 2 | 05 five-hours-no-web-r2 | layover-plan | 97 | Pass |
| 2 | 06 overnight-kids-separate | layover-plan | 93 | Pass, with findings |
| 2 | 07 near-miss-short | none | 75 | Pass (stayed quiet) |

**01.** Table added to 605 (the session checked it in code). Margin 90 for the slow walker. Verdict: go into the city, turn-back 12:10, latest set-out 09:30. The visa rule was quoted, with its date, from a page of the layover country's foreign ministry (its high commission site); the immigration authority's own page was an interactive form the fetch could not read, and a second page there was refused. Arrival card, gate closing, bags and the cost of a miss were marked to confirm. The airport's own transit tour was found on the airport site and offered as a swap. Airport facilities were described by kind, none named. City sights were named from general knowledge with hours marked unchecked. It used eight lookups against a limit of about six, and ran to about 1,350 words.

**02.** No rule stated as fact. The session moved the airport transit visa question to the top on its own judgement. Free time was zero before any ride; verdict stay; no outside plan; no facility names; four questions at the end. About 1,090 words.

**03, 04.** Chose the neighbour and did not open the skill. 04 noted that the unplanned wait after rebooking could later be a layover-plan question.

Changes after round 1: airline and flight numbers added to the questions; another site of the same government allowed when the main page cannot be read; a fallback ride figure; slow walkers count as limited mobility, with 15 added to the walking lines; anything unconfirmed that could stop the journey goes at the top; clock times defined for a stay verdict, and no outside plan when the sums fail; city sights may come from general knowledge with hours unchecked, airport facility names only from a page; a lookup order; working shown for the latest set-out time; lines that do not apply are left out; airport-run transit tours added; an unplanned wait after a missed connection is in scope once rebooked.

**05.** Transit visa and the onward country's entry document at the top, no rule stated as fact; sums shown with the fallback ride (free time minus 120); verdict stay; stay clock times as defined; the gap that would have been needed stated. About 1,010 words.

**06.** Entry rule for the layover country and an insurance rule for the onward country both quoted, with dates, from the traveller's own government's travel advice pages read in the run; the layover country's own government site was not read. Journey-stopping items at the top. Table added to 695. Margin 90. Stepped down from 150 nominal free minutes to "do not go into the city" for night, tiredness and children. Separate-ticket cost of a miss stated. A hotel inside the terminal was named from the hotel's own site read in the run, with its limits; the price was not found and the reply said so. A free option of resting in the public side of the terminal was given with night safety points. The desk opening time was flagged as the thing that decides the morning. Six lookups, none refused. About 1,260 words.

**07.** Chose no skill, citing the exclusion in the description.

Changes after round 2 (not retested): 30 minutes for a bag-drop queue; desk opening times added to the lookups, and a paragraph on separate tickets or bags to re-check (stay means the public side of the terminal until the desk opens; say so if the margin is squeezed); one step down per reason; where to sleep added to the stay plan for overnight waits; the onward country's entry rule; 60 for transfer checks when staying airside; a 20 minute ride guess for somewhere near; rewording so that facilities are described by kind when nothing was read.

## Independent reviews

Rubric lines scored 1 to 5 by a fresh reviewer told to score strictly.

| | Relevance | Trigger clarity | Correctness | Usability | Brevity | Provenance |
|---|---|---|---|---|---|---|
| Review 1 | 5 | 4 | 3 | 4 | 4 | 4 |
| Review 2 (a new reviewer, given review 1 and the changed files) | 5 | 4 | 4 | 4 | 4 | 4 |

Review 1 required three Correctness fixes: the worked example's traveller was "tired" but the verdict did not step down; the example said one flight a day but used the smaller margin; and the sentence on separate tickets was too absolute. All three were fixed, and review 2 confirmed them and rechecked the example's arithmetic independently. Review 1 also opened sources 1 and 2 and found the research note said "before departure" where the source says "before boarding"; corrected.

Changes after review 1 (not retested): the three fixes; "normally the traveller" pays on separate tickets; own-government advice alone keeps the layover country's site on the confirm list; free time worked out with the ride to that place; the bag-drop cut-off is a check; under two hours it says how to find the way, not a route; step-downs stop at stay; an unknown later flight counts as none, which raises the margin to 90; an aim of under about 800 words.

Changes after review 2 (not retested): later flights added to the airline lookups; own-government advice counts as confirmed but is said to be that; an allowance for a change of terminal, and the worked example now says "same terminal"; the example's margin source reworded.

## Open items

- Every edit after round 2 and after both reviews is untested. "Unknown later flight counts as none" changes the sums in a case like 02 and 05 (margin 90, not 60); the verdict there would not change.
- The full daytime path (01) was not rerun after the round 1 fixes.
- Not taken from the reviews: naming trip-companion in the description for short-connection and rebooking questions (no room in the character limit); splitting the long paragraph after the allowance table.
- The default allowances are the author's judgement and sit somewhat below one published rule of thumb; see the docs page.

## What these tests do not show

- No run read the layover country's own immigration authority page successfully. No airline page and no transit operator timetable was read in any run. Airport pages were read only for a transit tour and ground transport.
- Stations (rail, coach, ferry) were never tested.
- Each prompt ran once. The two near misses that passed at 75 and 82 confidence were not repeated.
- The user could not answer in any run, so asking and waiting is untested.
- Whether the turn-back times hold up on a real layover. Nothing was checked against real queues.
- Replies ran 1,000 to 1,350 words, long for a phone; the 800-word aim was added afterwards and is unproved.

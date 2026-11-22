# Testing record: weekend-plan

Version 0.1.0. All runs on 22 November 2026.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of 13 installed skill descriptions (weekend-plan among its neighbours, including trip-companion, day-in-city, host-plan, week-plan and layover-plan), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used, every point it found unclear and where every place, price, time and weather statement came from. Prompts and pass criteria were written before any run. Two rounds were run: four prompts, then three. Web lookups were either switched off or capped at six per session. Because the tests ran inside a real account, sessions were told not to touch any calendar, message or personal-device tool and never to use a location tool: the made-up user stated the town in words, and where the skill would add calendar entries the session listed them and stopped. Every person in the prompts is invented; the towns are real.

## Prompts and pass criteria

### T1 (should trigger; user away; web off)
Prompt: "Ideas for the long weekend with two kids and not much money? I've taken Monday off so we have Sat 28, Sun 29 and Mon 30 November. We live in Hamilton, New Zealand (Hamilton East). Me, my partner Rewi, and the kids, Tama who is 3 and Ana who is 8. Honestly a brutal week at work for both of us, we mostly want to recover but the kids will go feral if we stay in all three days. Budget about 60 dollars for the whole weekend not counting normal groceries. We have one car but I'd rather not drive more than half an hour. Tama naps roughly 12:30 to 2:30. Ana has cricket Saturday 9 to 10:30. The lawns have to be mowed and there is a mountain of washing. Heading into a meeting now and won't be able to answer questions, just give me a plan I can read tonight."
Pass: picks weekend-plan; asks nothing; says early that nothing could be looked up; no dated event, price, opening time or forecast from memory; ideas given as kinds of thing, any named permanent place marked unconfirmed; at most one main thing a day; a named rest block of half a day or more; one chore block of two hours or less with an end time; nap and cricket respected; cost shown and at or under 60; at-home alternative, meals, buy list and reset present; a "to check" list; no calendar entries; no location tool.

### T2 (should trigger; full conversation, one session playing both sides from a persona sheet; web on)
Opening message: "what should we do this weekend". The persona (a couple in Utrecht; one partner walks with a stick for about 20 minutes at a time; both vegetarian; 60 euros; public transport; her mother comes for Sunday lunch; a heavy week) gives the place and everything else only when asked, and after the plan asks for two calendar entries.
Pass: picks weekend-plan; the first message asks for the place and the other missing items in one short message and uses no place before it is stated; at most two messages before the plan; at most one main thing a day, rest, one chore block before Sunday lunch, the lunch kept fixed; every named place carries a status with the page and date read, and "confirmed" only for pages really read; forecast with source and time read; access fits the partner; vegetarian; nothing alcohol-centred; cost at or under 60 with the sum; on the calendar request, shows the exact list and waits for a yes.

### T3 (near miss, aimed at day-in-city; web off)
Prompt: "We're visiting Porto next Saturday, just for the day (we're staying with friends out in Braga and coming in by train), with our two kids who are 6 and 10. Can you plan us a great day: what to see in what order, where to eat, what to book? We arrive about 9:30 and need the 19:00 train back."
Pass: does not pick weekend-plan; picks day-in-city.

### T4 (near miss, aimed at trip-companion; web off)
Prompt: "Ideas for the long weekend? We want to get away, thinking of flying somewhere warm Friday to Monday with the kids (5 and 7), from Manchester. Need help picking where, finding flights and somewhere to stay, and what we need to sort before we go. Budget about 1200 pounds all in."
Pass: does not pick weekend-plan; picks trip-companion.

### T5 (round 2; should trigger; user away; web on)
Prompt: "Can you plan our weekend? We're in Alexandria, Egypt (Smouha). Days off are Friday 27 and Saturday 28 November. Me, my husband Karim and our kids Laila (11) and Omar (6), plus my father-in-law who is 74 and gets tired walking more than about 15 minutes. Friday prayer is fixed, Karim, his father and Omar go around noon, back about 1:30, and Friday lunch is always at my mother-in-law's after that until about 4. The kids keep asking to go to the sea. Week was long (school exams). We'd like one proper family outing and otherwise calm. Budget around 1500 pounds for everything. We have a car. Omar is in bed by 8:30. The balcony needs clearing out at some point, an hour maybe. I'm about to go into the exam hall to invigilate so I can't answer anything, just send the plan."
Pass: picks weekend-plan; treats Friday and Saturday as the days off; prayer and lunch untouched, no comment on them, no extra main thing on Friday; one outing; a sea idea carries water and daylight safety lines with sunset looked up or marked to check; statuses fact by fact and "confirmed" only for pages read; forecast dated or to check; chore block of about an hour; bedtime kept; nothing alcohol-centred; cost in Egyptian pounds at or under 1,500 with the sum.

### T6 (round 2; should trigger; user away; web off; no place given)
Prompt: "plan a relaxing Saturday for me near home. this coming Saturday. just me, I live alone, knackered after a run of night shifts (I'm a nurse), back on shift Sunday night. I don't want to spend more than about 25. I've got a bike. phone's going off now til tonight so don't ask me things, just give me something"
Pass: picks weekend-plan; uses no location tool and guesses no place; gives the shape, at-home alternative, meals and reset; ideas as kinds of thing with no named place; cost as caps at or under 25; one main thing at most; mostly rest; the place is the first thing asked at the end; no health advice.

### T7 (round 2; near miss, aimed at host-plan; web off)
Prompt: "What should we do this weekend, it's my husband's 40th on Saturday and I've got 14 people coming to ours for dinner at 7. Two vegetarians and my niece has a nut allergy. I need a menu, how much to buy and a timeline for the day so I'm not stuck in the kitchen."
Pass: does not pick weekend-plan; picks host-plan.

## Results

### Round 1 (first draft)

| Test | Chose | Confidence | Result |
|---|---|---|---|
| T1 | weekend-plan | 96 | Pass on every criterion. Nothing looked up and said so in the second line; four permanent places named from memory, all marked unconfirmed; no forecast, price, hours or dated event; 0, 1 and 1 main things across the three days; Saturday afternoon named as rest; chore block 1 hour 45 minutes with a hard stop; nap and cricket kept; spending caps 45 of 60, labelled as caps. |
| T2 | weekend-plan | 96 | Pass. One message of seven short questions with the place first; the plan came in the second message. Two museum pages were really read and their hours (and one price) marked confirmed; the other price and all access details were marked to check. The national weather service's page was refused, so no forecast was given. Lunch kept; vegetarian; no alcohol; 37 of 60 euros confirmed with fares to check; calendar list shown and a yes awaited. Weak points: access for a person with a stick could not be read inside the lookup limit and sits only on the "to check" list; sunset was not looked up. |
| T3 | day-in-city | 93 | Pass (did not trigger). |
| T4 | trip-companion | 92 | Pass (did not trigger). The session noted that the opening words match one of weekend-plan's example phrases; the exclusion decided it. |

Changed after round 1: how to mark a permanent place whose own page shows standing hours ("confirmed (regular hours)") and a place with some facts read and some not; what to do when must-do chores exceed the chore block and whether it may run alongside a fixed commitment; spending caps when no price may be given; a fixed commitment that fills much of a day is that day's centre; what to do when only some pages fail; a clock time for a calendar entry made from a rough slot.

### Round 2 (second draft)

| Test | Chose | Confidence | Result |
|---|---|---|---|
| T5 | weekend-plan | 95 | Pass with weak points. Friday and Saturday taken as the days off; prayer and family lunch untouched, with no comment and nothing added to Friday; one outing on Saturday; one-hour chore block; bedtime kept; water and daylight lines given; two pages of one venue read and marked "confirmed (regular hours)" fact by fact; no alcohol; caps of 1,500 of 1,500 Egyptian pounds. Weak points: the forecast and sunset came from another country's national weather service (the reply said so and put the Egyptian service under "to check"); only one of three ideas rested on pages read; no price was confirmed, so the whole sum was caps and reached the full budget; the daylight line as then written cut a city seaside outing short at 4 pm. |
| T6 | weekend-plan | 97 | Pass. No location tool, no place guessed, nothing named; three kinds of outing with search words; one main thing plus the reset; the morning named as rest; caps of 16 to 25 of 25 with no currency symbol; the town was the first item under "to check"; the reset was adapted to a night shift; no health advice. |
| T7 | host-plan | 92 | Pass (did not trigger). |

Seven of seven prompts passed. No prompt was rerun.

Changed after round 2 and not rerun: the wording on where safety notes come from; naming another official weather service when the local one could not be read; the place-missing case now gives every part of the plan; spending caps for any price that could not be read.

## Independent reviews

Two different fresh reviewers scored the skill against a six-line rubric, strictly, with the brief, the research note, the test log and the replies.

| Line | Review 1 | Review 2 (final) |
|---|---|---|
| Relevance | 5 | 5 |
| Trigger clarity | 4 | 4 |
| Correctness | 4 | 4 |
| Usability | 4 | 4 |
| Brevity | 4 | 4 |
| Provenance | 3 | 4 |

Review 1 fetched four of the sources and found the claims about variety, the four parts of recovery and the water-safety lines matched them, and one claim overstated (that a rough time slot "keeps both" benefits; the source only reports the authors suggesting it). Its required fixes, all applied: publish a source list saying what was and was not read; label the trail, hill and sunset lines as general know-how and credit the water lines to their source; soften the rough-slot claim; mark the prices, travel time and forecast in the worked example; limit "finish an hour before sunset" to unlit places, since evening outings in town are normal in many places. Several of its optional suggestions were also taken (what counts as a second planned thing, what to do with no calendar tool, lookup order, narrower wording on weather warnings, holiday hours).

Review 2 found review 1's fixes done except for two slips, scored no line under 4, and required four corrections as consistency errors, not by score: a line about being beside water was credited to the wrong source and told people to stay off piers in any weather; a sunset time was still asked for on morning outings; the worked example broke some of the skill's own rules (no safety note on one outdoor idea, no cost sum, no forecast for two of the days, no holiday-hours check); the holiday rule depended on the session happening to know that a day was a holiday. All four were applied as the reviewer worded them.

## Open items

- Every edit after round 2 is untested: the four clarifications after round 2, the fixes and suggestions from review 1, and the four corrections from review 2. The review 2 corrections are also unreviewed.
- The description's exclusion for day-in-city is narrower than that skill's own scope (it also plans a day out for a local). It passed its near-miss test and was left unchanged; a request such as "plan us a day out in our own city on Saturday" could go to either skill.
- The rule on places named from memory is worded slightly differently in two places ("a permanent place you know of", "a permanent public place you are sure exists").
- Nothing says what to do when the days off are further ahead than any forecast reaches.

## What the tests do not show

- No run confirmed a dated event on an organiser's or council's own page. Every "confirmed" in the tests is a venue's standing timetable. The paths "event listed for that date, confirmed" and "seen on a listing site only, unconfirmed" were never exercised with live pages.
- No run read the national weather service of the user's own country (refused once, replaced by another country's service once), and no weather warning was ever met.
- Page reads came through a tool that returns a summary of the page, so a "read" fact could be mis-summarised.
- No real calendar was written; the calendar step was shown as text only.
- One model, one run per prompt; no trigger choice was repeated. Near misses were aimed at day-in-city, trip-companion and host-plan; week-plan and layover-plan were on the list but not aimed at.
- Not run at all: a single mid-week day off; public transport fares; a person asking for an alcohol-centred idea; the line for someone describing more than a tiring week; a public holiday; a trail or hill outing; anything involving swimming.
- The towns in the tests are in New Zealand, the Netherlands and Egypt; nothing shows how well official listings can be found elsewhere.

# Testing record: learn-plan

Status: **draft: review open.** Two test rounds (seven fresh-session runs, all passed, most with findings) and three independent reviews, 22 November 2026. At the third and last review Usability scored 3; every other line is at 4 or above. The final text has not been rerun: the tests ran on two earlier versions, and the edits made after round 2 and after each review were read by the reviewers or checked by the author only. The two fixes the third review required are in the text and are unreviewed.

## How it was tested

Each prompt was run by a fresh session that had not seen the skill being written. It was given a list of installed skill descriptions (learn-plan among forge, bedrock, skill-creator, docx, deep-research, and dream-pathway, week-plan, launchpad, video-to-actions and trip-companion with their real descriptions from this collection), chose a skill from the descriptions alone, opened learn-plan only if it had chosen it, followed it, saved its reply and logged anything unclear, with a self-check of every resource named, the hours sum, the goal, the pass marks, any promise, links and questions asked. Prompts and pass criteria were written before any run. Web lookups were capped at six per run where allowed. The fetch tool in these sessions returns a summary of a page, not the page itself. The sessions were told to create no reminders or calendar entries and to book nothing.

## Prompts and pass criteria

**T1 Spanish in a month, no web tool, user away (should trigger; passes without live pages).** "I want to learn conversational Spanish in a month. I'm a complete beginner. I can do about 40 minutes a day, most days. I learn best by listening and speaking, I get bored with textbooks. Can spend a little but not much. I'm about to board a long flight so I can't answer anything, please just send me the plan and I'll start when I land."
Pass: chooses learn-plan; one reply, no questions, assumptions stated; a line saying nothing was looked up; hours sum right; goal a stranger could test; says what a month will not reach, no fluency promised; three to five sub-skills and a leave-out list; sessions mostly recall and practice; resources by kind with search words, at most two names from memory marked unchecked, none invented; a numeric pass mark each week; missed-days rule; review point; no country or currency guessed.

**T2 guitar, full conversation (should trigger; one session played both sides from a persona sheet).** "teach me guitar basics, 30 minutes a day". The persona: an adult in Nairobi with an old untuned acoustic guitar, who gave up as a teenager, wants to play and sing two songs at a family gathering in six weeks, has weekdays only, reads slowly and prefers to be shown, gets tingling in one wrist after long days typing, has no money for courses, and is mildly impatient with questions; then two follow-ups: "I missed five days in week 2. What now?" and "honestly, will I be good by the birthday?"
Pass: chooses learn-plan; at most four questions in one round; goal built on the two songs; sum right; short sessions, warm-up, stop on pain, returning pain referred to a health professional, no condition named or guessed; a short, show-me format; resources labelled checked or unchecked; numeric checks; missed days answered by the rule with no doubling; the last question answered honestly with no promise.

**T3 a twelve-year-old who wants to be a concert pianist (should not trigger; aimed at dream-pathway).** Pass: does not choose learn-plan.

**T4 a sixty-day plan to land a data analyst job through people (should not trigger; aimed at launchpad).** Pass: does not choose learn-plan.

**T5 Excel "properly", no web tool, user away, no date (should trigger; passes without live pages).** "make me a plan to learn Excel properly. I use it at work every day but only for typing in lists and adding up a column, and I keep getting handed other people's spreadsheets I can't follow. most days I can find half an hour at lunch. I'm off to a site visit with no signal till tonight so don't wait for me, just write it."
Pass: chooses learn-plan; no questions; vague goal restated as a testable one; four weeks and five days assumed and said; sum right (10 hours); numeric checks; at most two names from memory, marked; about 700 to 1,000 words.

**T6 an eight-year-old to swim before a beach holiday, live web (should trigger; children and physical risk).** A parent in Brisbane, five weeks, 20 minutes a day, a public pool nearby, user away.
Pass: chooses learn-plan, not dream-pathway; written to the parent; in-water teaching left to a qualified instructor, no technique given; no promise he will swim; short playful sessions; providers named only from pages opened; nothing booked.

**T7 rewiring a kitchen in an old house in France, live web (should trigger; licence and physical risk).** Six weeks, an hour a day, 200 euros, user away.
Pass: chooses learn-plan; official requirements stated from a page opened or marked "to confirm" with the official body; no way round; no wiring technique; goal restated to what can be done safely and planned.

## Results

### Round 1
| Prompt | Chose | Confidence | Result |
|---|---|---|---|
| T1 | learn-plan | 97 | Pass with findings. No questions; no-lookup line first; 24 days x 40 min = 16 hours, right; goal testable; no fluency promised; five sub-skills and a leave-out list; session about 75% recall and practice; resources by kind with search words, two names from memory, each marked unchecked; four checks with numbers; missed-days rule; review on day 14; no country, currency or link. Findings: "five minutes to read" pulled against the list of required parts (about 1,230 words); "most days" and "a month" had no default; no start date so no review date; unclear whether "one or two names" is per stage; backup "of a different kind" strained; a listening preference against the input cap; one sample session per week against length; pass marks for open conversation; "leave-out end" undefined; the worked example omits parts the steps require. |
| T2 | learn-plan | 97 | Pass with findings. Four numbered questions in one round (nine parts in all), persona did not complain; goal restated around two songs; 30 x 30 min = 15 hours, right; slow reading met with short lines and video, wrist with split sessions, stop on tingling or pain and "a question for a health professional"; no condition named; two resources opened and labelled, the lesson "unchecked"; six checks with numbers; five missed days answered with the two-to-six rule plus a shrunken goal; "will I be good" answered "good, no", no promise. Findings: multi-part questions; calendar days or sessions in the missed-days bands; no rule for a fixed date; no label for a page opened without a price; search listings are not checks; where warm-up minutes come from; a country-specific app store link; a session that added up to 31 minutes. The session ran its lookups before writing the transcript, knowing the persona. |
| T3 | dream-pathway | 93 | Pass. The exclusion line decided it. |
| T4 | launchpad | 90 | Pass. The exclusion line decided it. |

Fixes after round 1: a cap of two names from memory per plan; a search listing is not a check; label "checked today, price not seen"; app named for the person's own store, no store link; warm-up minutes come from the new-thing part; questions of one or two facts each; defaults for "a month", "most days" and an unknown start day; session shape given once and a practice task per week; the input cap holds whatever the preference, which picks the format; backup of a different kind "where possible"; pass marks for open tasks count something; "leave-out end" replaced; missed-days bands counted in planned sessions (one, two to four, five or more) with a fixed-date rule; length guidance of 700 to 1,000 words, cut words not parts; the short form keeps rules 4 to 6; the worked example marked as shortened and its missed-sessions line updated. The description did not change, so T3 and T4 were not rerun.

### Round 2
| Prompt | Chose | Confidence | Result |
|---|---|---|---|
| T5 | learn-plan | 97 | Pass with findings. No questions; no-lookup line; goal restated as reading an unseen workbook and building a summary within 30 minutes; 20 x 30 min = 10 hours, right; four weeks and five days assumed and said; one name from memory, marked unchecked, the rest by kind; four checks with numbers; session numbers used in place of dates; 930 words; no country or currency. Findings: whether "properly" counts as a goal that does not fit the hours; how an assumed date is treated when five or more sessions are missed; "day numbers" ambiguous for a five-day week. |
| T6 | learn-plan | 85 | Pass with findings. Written to the parent; all in-water teaching left to a qualified swim teacher, no technique given; "I can't tell you he will be swimming by the holiday" and "plan the beach holiday as if he cannot swim"; 30 x 20 min = 10 hours; three pages opened and labelled "checked today, price not seen", one name from memory marked unchecked; nothing booked; 1,038 words. Findings: "no pass-or-fail talk" for a child clashed with numeric pass marks (the session kept marks for the parent only); with no technique allowed, the week table and checks were thin, and the skill did not say what they should hold; confidence lower because of "fitness programme" in the exclusions. |
| T7 | learn-plan | 80 | Pass with findings. Did not plan the solo rewire: said it does not fit, offered a smaller goal or a longer supervised route, and planned a reviewed design plus a first supervised lesson; no wiring technique; what it found for France (an owner may do the work, an inspection certificate applies in some cases, fee seen on a supplier's page opened in the session) was labelled "to confirm" with the official body; no way round offered; euros; five checks with numbers; 1,113 words. Findings: rule 6 presumed a licence that the place may not require; rule 4 did not list mains electricity; no instruction for a goal that cannot be practised safely alone; the rules 4 to 6 material had to move to the top; over the word range. |

Round 2: 3 of 3 pass. Two-round limit reached.

### Edits after round 2 (not retested)
Rule 4: mains electricity and gas added to the list; what the practice tasks and the plan hold when an instructor teaches the risky parts; a goal that cannot be practised safely alone is handled like one that does not fit the hours. Rule 5: checks shown to the child as showing what they can do, marks kept for the adult (replaces "no pass-or-fail talk"). Rule 6: rewritten so requirements are looked up for the person's place or marked "to confirm", never stated from memory, with a line for when none is found. Day or session numbers. "Fixed by an event" in the missed-sessions rule. Rules 4 to 6 material goes first when it changes the goal; word range a little longer when those rules apply.

### Edits after review 1 (not retested)
Description: "missed days" became "a missed-sessions rule". Rule 2: a name seen only in a search listing counts as one of the two memory names. Rule 4: kitchen knives and hot oil moved out of the instructor list to an everyday-risk line; non-lesson days have no new thing; an unsafe solo goal is met by a safer goal or a qualified person, never more time alone; "body-based" narrowed to skills learned through the body, not desk work. Rule 5: 10 to 20 minute playful sessions only under about 13, with that figure used in the sum; teenagers keep the usual session; "light version" defined. Step 1: "every day" is six. Step 4: first session has no recall; the mixing and spacing lines hedged to match the sources. Step 5: a rule 6 lookup comes first and counts. Step 6: checks for a child or a rule 4 part happen with the instructor or adult there. Step 7: the repeated "never double" line cut. Plan order: short form also when long text is hard for the person. No-tool section: defers to rule 2. Worked example: session shape moved above the table, column renamed "Practice task", directions removed from the goal and weeks and added to leave-outs, numbers to 100, "last four days", two scenes.
Reviewer's request for a cooking test and an instructor or child test against the current text could not be met within the limit; carried as an open item.

### Edits after review 2 (scored by review 3; not retested)
Step 6: for a part taught by an instructor, the instructor sets or confirms the check task and pass mark, and the skill sets no technique target. Step 7: bands restated as one session, two sessions up to just under a week of the plan, and a whole week or more, so they cannot overlap. Step 2 and rule 5: an instructor's lessons are added to the hours sum at their own length or said to be left out; the 10 to 20 minute cap is for home sessions. Description: "a fitness, weight or diet programme". First session: recall time goes to the new thing and its practice. Worked example: missed-sessions line and week 4 check reworded.

### Extra round after review 2
One further test round (up to three runs) was allowed before the third review. It was not run: the three fixes review 2 required were wording changes, so the text went straight to the third review, which was told plainly that there were no new test results and that the instructor-led child path and the cooking path had never been run on the present wording. The reviewer capped untested wording at 4, and at 3 where its own walk-through found a guess that changes the plan.

### Edits after review 3 (author checks only; not reviewed, not retested)
Rule 5: "use the shorter figure in the sum" became "use the length you plan, not the length offered", and a lesson day has no home session. Worked example: the missed-sessions line says "two to five (this plan has six sessions a week)" in place of "two to four", to agree with step 7.

## Review scores

| Line | Review 1 | Review 2 | Review 3 (final) |
|---|---|---|---|
| Relevance | 5 | 5 | 5 |
| Trigger clarity | 4 | 4 | 4 |
| Correctness | 3 | 4 | 4 |
| Usability | 3 | 3 | 3 |
| Brevity | 4 | 4 | 4 |
| Provenance | 3 | 4 | 4 |

Review 1 asked for sixteen fixes: rule 4 made cooking unplannable; the mixing claim had lost its source's caveat; "cold, no help" clashed with supervised skills; the worked example contradicted the steps; several guesses from the test logs were still open; the research leaned on secondary pages. All were made except the request for more test runs, which the two-round limit ruled out; a first-hand source (the paper's abstract) was added.
Review 2 confirmed those fixes and held Usability at 3 for three guesses on the instructor-led and child path: who sets the check for an instructor-taught part, overlapping missed-session bands in plans with fewer than five sessions a week, and whether lessons count in the hours sum. All three were then edited (above).
Review 3 (a third reviewer, given review 2, the changes since and the fact that no new tests were run) walked a case through each edit. It found the first fixed, the second fixed in step 7 but not carried into the worked example (whose six-sessions-a-week plan left five missed sessions in no band), and the third fixed for lessons but not for home sessions ("the shorter figure" could be read two ways, and nothing said whether a lesson day also has a home session, so a child's hours sum could come out at about 8 or about 14). It held Usability at 3 and required those two fixes. Both have been made (above) and are unreviewed, so the line stays open.

## Open items

1. **Usability is at 3** as last scored. The two fixes review 3 required are made but unreviewed; no further review is planned in this pass.
2. The final text has not been run by a fresh session. First runs to make: a cooking plan (everyday-risk line in rule 4) and an instructor-led child case with a stated lesson length and more than 20 minutes a day offered (rules 4 and 5, step 6), then a three-sessions-a-week plan with a missed-sessions follow-up (step 7).
3. Near misses not tested: explaining one concept, a fitness or diet programme, coursework or exams for someone, week-plan, video-to-actions.
4. "A fitness programme" in the exclusions lowered one run's confidence for swimming (85); the wording was adjusted, untested.
5. Review 3 optional points not taken: mixing shown from week 2 in the worked example; an example of where a plain target ends and a technique target begins; a line for a plan with one session a week and for a missed lesson; whether cooking counts as a skill learned through the body. Review 2 optional points not taken: a set sentence for explaining why sessions start with recall (two replies wrote "far better" where the skill says "better"); splitting rule 4 in two.
6. Small guesses still open, from the logs: a budget with no currency; whether official fees sit inside the budget; whether practice material such as a song counts as a resource; assumptions that need more than three lines.
7. Research was read through page summaries; four of six sources are secondary; no original paper was read.

## What the tests do not show

- Whether anyone learns more with these plans. Nothing here measures learning; the tests check that the skill fires, follows its rules and produces a plan that hangs together.
- **Live-page paths never exercised or only thinly:** no run opened a resource page that showed a price, so "checked today" with a price seen was never produced (two runs produced "checked today, price not seen"); no run found a local class, library or conversation group on a page; no official body's own page answered a licence question (one supplier's page was opened and its content marked "to confirm"; the official body's page opened did not answer); one page failed to open and was not retried. T1 and T5 ran with no web at all, by design.
- The conversation test was one session playing both sides, and it made its lookups before writing the transcript, already knowing the persona.
- No test covered: a child writing alone, a teenager, a plan longer than six weeks, a person who names a resource they already own, a request to do coursework, a language other than English, or a real person missing real sessions.
- Trigger tests were single runs against one list of neighbours; a different set of installed skills could change the choice.

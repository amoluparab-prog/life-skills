# Testing record: week-plan

Version 0.1.0. All runs on 22 November 2026. Every person, organisation and calendar entry in the prompts is invented. No test read or changed a real calendar: calendars were pasted as made-up text, and where the skill would write to a calendar the session only listed what it would create.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (week-plan among forge, bedrock, life-admin, meet-prep, skill-creator, docx, trip-companion, weekend-plan, learn-plan, host-plan, idea-triage and deep-research, with only week-plan on disk), chose a skill from the descriptions alone, and only then opened the skill and followed it. The descriptions used for weekend-plan and learn-plan were stand-ins, because those skills were not yet written. Each session saved its reply and a log of its choice, confidence, tools used, every unclear point, and its own line-by-line check of the sums. Web tools were switched off in every test. Sessions were told not to touch calendars, mail, contacts or location.

Because the skill is a guided conversation, two tests simulated a whole conversation: one session played both sides from a persona sheet, so pacing was tested and not only the first reply.

## Prompts and pass criteria

### T1 (should trigger) overloaded, away, everything pasted, no web, no calendar tool
"I'm overloaded, what should I focus on this week? Can't chat, I'm about to board, so just give me the plan." Followed by a Monday to Friday working week of 9:00 to 17:30, ten pasted meetings, three carried-over items (one a month old), four work items with times (three guesses, one timed), an unanswered invitation, a school concert and two swims.

Pass: chooses week-plan; asks nothing; assumptions marked; a verdict per carried item and the month-old one not silently kept; three outcomes with one personal; guesses raised by half and the timed hour left alone; correct sums (window 42.5, fixed 12.5, routine 7.5, free 22.5, open 4.5, usable 18); the overload shown and cut; no evenings added; decline and defer drafts; preparation for the presentation; one non-negotiable from the person's own words; daily check; no calendar action, opinion or health advice. This is the test designed to pass without live page access.

### T2 (should trigger) full conversation, a Sunday to Thursday week, pretend calendar tool
Opening: "do a weekly review with me". Persona: runs a two-person practice from home, cares for her father two afternoons, keeps Friday and Saturday free for family and prayer, declines the calendar read and pastes six entries, has one item carried five weeks, and at the end says "ok put those blocks in my calendar".

Pass: chooses week-plan; at most three rounds before the plan; calendar read offered once and not done after "no"; no Monday to Friday assumption; no re-asking; the five-week item asked about without judgement; correct sums; options when over; the walk placed first; an exact list and a wait for yes before any calendar write; about fifteen minutes of the persona's time.

### T3 (near miss, weekend-plan)
"Brutal week at work. Plan a relaxing weekend for me near home, Saturday and Sunday, nothing that needs much money." Pass: does not choose week-plan.

### T4 (near miss, meet-prep)
"Big thing this week is Wednesday: my first one-to-one with the new operations director, 45 minutes. Help me get ready for it, what should I ask and what should I bring?" Pass: does not choose week-plan.

### T1r (round 2) rerun of T1, same message
Pass: as T1, plus the short answer and main assumption first, cuts in the stated order, added halves kept, the invitation shown as not fixed with its cost.

### T5 (round 2, should trigger) full conversation, week already started, calendar read requested
Opening, on a Wednesday at 08:10: "help me plan my week, well what's left of it. you can read my calendar". Persona: a teacher and football coach. The "calendar" was text supplied in the prompt. Reports due Friday 16:00, two carried-over items (one four weeks), an unanswered invitation, a birthday dinner on Friday evening. His choice of cut does not close the gap. He ends with "add them to my calendar please" and then "yes but not the marking ones".

Pass: chooses week-plan; reads only because asked; plans from now; the plan is the third assistant message; correct sums; invitation not fixed, cost shown, decline draft; a further cut made and said, with no taking back of added halves; nothing past 16:30 Friday; change list names the calendar and waits for yes.

### T6 (round 2, near miss) team sprint
"Help me plan next week's sprint for my team. Six engineers, two-week sprint starting Monday, here's the backlog..." Pass: does not choose week-plan.

## Results

### Round 1

| Test | Chose | Confidence | Result |
|---|---|---|---|
| T1 | week-plan | 97 | Pass. Sums correct (needed 26 against 18 usable, over by 8); write-up and expenses deferred, invitation declined by draft; concert as the non-negotiable; no evenings added. The reply ran longer than the "one page" the text then asked for. 19 unclear points logged. |
| T2 | week-plan | 97 | Pass with one miss. Sunday to Thursday respected; calendar read offered once and not done; no judgement; sums correct; exact list and a yes before the (described) calendar write. The miss: four assistant messages before the plan, not three, and when her choice did not close the gap the session took the added half back off a guess to make the week fit. Persona time estimated at 13 to 15 minutes. |
| T3 | weekend-plan | 95 | Pass. |
| T4 | meet-prep | 93 | Pass. |

Changes after round 1: the three rounds reshaped as gather, sort and count, plan, with rough times and the non-negotiable asked in round 1; what to do when the person's choice does not close the gap, an order for cuts, and a ban on taking the half back or using the open fifth; rules for the away path (how outcomes are proposed, cut order, long-carried items); what counts as fixed; planning from now when the week has started; placement by due date first; an "Also this week" list; one place for assumptions.

### Round 2

| Test | Chose | Confidence | Result |
|---|---|---|---|
| T1r | week-plan | 98 | Pass. Same sums as round 1; halves kept; invitation shown as not fixed and declined by draft; needed 18.0, spare 0.0. It stated the invitation's cost as its full 2 hours, where four fifths is exact (found by the first reviewer, fixed in the text after). |
| T5 | week-plan | 96 | Pass. Read only because asked; planned from Wednesday 08:10; plan was the third assistant message; sums correct (free 5h50, usable 4h40, needed 17h25); two further cuts made and said at the top; invitation left unanswered with a decline draft; six events listed with the calendar's name before a yes. Persona time estimated at 11 to 13 minutes plus 2 for the calendar step. |
| T6 | none | 93 | Pass. |

Trigger choice across both rounds: 7 of 7 correct.

## Independent reviews

Each review was done by a fresh session with the brief, the skill, the research note, the test log and replies, and the rubric, told to score strictly.

| Line | Review 1 | Review 2 |
|---|---|---|
| Relevance | 5 | 5 |
| Trigger clarity | 4 | 4 |
| Correctness | 3 | 4 |
| Usability | 4 | 4 |
| Brevity | 4 | 4 |
| Provenance | 4 | 4 |

Review 1 fetched four of the five sources and confirmed the claims drawn from them, and found the worked example's sums right. Its seven required fixes: a per-deadline check as well as the weekly sum; redoing the sum when a fixed commitment changes (declining a meeting closes four fifths of its length); an example whose smaller report no longer looked like taking the added half back; never accepting or declining invitations and no guests on blocks; block length when free slots are short; the 30-minute gap rule; labelling the half and the fifth as rules of thumb. All seven were applied.

Review 2 (a different session, given review 1 and the changed files) found six fully fixed and the deadline check partly fixed, and required three one-sentence corrections: make the deadline check add up everything due by a deadline; make rounding optional so it agrees with the example; show the deadline check in the example. All three were applied after the review, with five of its small optional wording points.

## Open items

- Not rerun in a test session: the small edits after round 2, the fixes after review 1 and the three corrections after review 2. The second reviewer read the first two sets and judged them low risk, apart from the rounding line and the deadline check, both of which were then corrected; those corrections have been read by nobody but the author. One rerun of T1r or T5 would settle it.
- The trigger results were measured on a slightly earlier description (the exclusion "a single day's plan" was added later).
- The second reviewer noted that "plan next week" for a team still overlaps the trigger words, and that putting a to-do list in order is not named as an exclusion. The description is at 1,017 of 1,024 characters.

## What the tests do not show

- No test used a live web page. The public-holiday lookup path (person names a place, web tool available) was never exercised; only the "To check" path was.
- No real calendar tool was called. Reading and adding were simulated in text, so tool errors, several calendars, time zones and recurring events are untested.
- The "about fifteen minutes" figure rests on a model's estimate for invented personas who had everything to hand. The reviewers judged it reachable with a calendar and list to hand, and tight when the week is far over and has to be recut.
- Both conversations were played by one session on both sides, which is easier than a real person who goes off script.
- Not tested: shift or night work, a week with a public holiday, someone who mentions distress beyond workload, a person with no fixed hours, weeks where a deadline check fails while the weekly sum passes, and fewer than three outcomes stated by the rule (T5 produced that behaviour before the rule was written).
- Two of the seven research pages were refused and never read; nothing in the skill relies on them.

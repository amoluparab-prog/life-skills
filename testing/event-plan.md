# Testing record: event-plan

Version 0.1.0. All runs on 22 November 2026. Every event, person and organisation in the prompts is invented.

## How it was tested

Each prompt ran once, in its own fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (event-plan among forge, meet-prep, host-plan, skill-creator, trip-companion, docx, launchpad, event-outfit, deep-research, first-wave-launch, video-to-actions, week-plan and bedrock, with only event-plan on disk), chose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of anything unclear. Sessions were told to create no calendar entries, reminders or messages.

The skill is a one-shot plan with at most one round of questions, so no full-conversation simulation was run.

## Prompts and pass criteria

### T1 (should trigger) pasted two-day agenda, no web tool
> I'm going to this conference next week, help me plan it. It's the Hartsmere Water Utilities Forum, 2 and 3 December 2026 [...] My employer is sending me; I run the leak detection team. I want to come back with a clear view on acoustic sensors versus satellite leak detection, and to meet two or three utilities who have already rolled out either. I already know Petronella Vasquez-Lindqvist from Aldmoor Water, she's on a panel. I'm vegetarian and I have to be on the 17:40 train home on day 2. [two-day agenda with rooms, speakers, a clash at 11:00, a sign-up workshop, a site visit returning at 17:30, and four exhibitors]

Pass: chooses event-plan; no needless questions; agenda dated with a recheck note; two or three countable goals; the clash settled with a reason and a plan for the talk not chosen; at most three musts a day; open slots; the workshop flagged for sign-up; the site visit ruled out by the train; nothing outside the pasted agenda; people labelled, each with an opening question; five requests at most; introduction; day plans; note template; week-after drafts with blanks; both reminders once. This is the test that passes with no live page access.

### T2 (should trigger) link only, user away, a job as the goal, up to three web calls
> how do I get the most out of this summit? [link to an invented agenda page] It's the Northquay Logistics Summit, 19-20 January 2027 [...] I was made redundant in October after nine years in warehouse operations [...] I'd like to find out who is hiring for operations manager roles and get in front of them. I don't know anyone going. I'm offline until tomorrow so just give me what you can.

Pass: chooses event-plan, not launchpad; asks nothing; says plainly the agenda was not read; invents no session, speaker, exhibitor or employer; gives goals, introduction, note method and week-after in full and the rest in short form with blanks; a To do list; no attendee-list collecting.

### T3 (near miss, aimed at meet-prep) one booked meeting at a summit
> At the rail procurement summit next week I've got one thing that matters: a 20-minute coffee on Tuesday with Ferran Achterberg, head of procurement at Dunmere Rail. [...] Brief me for that meeting, what do I open with and what do I ask him?

Pass: chooses meet-prep.

### T4 (near miss) organising a conference
> I'm organising a two-day regional conference for about 300 dentists next March. Help me plan it: the agenda, which speakers to invite, the run of show and a sponsor package.

Pass: does not choose event-plan.

### T5 (should trigger, round 2) one-day trade show abroad, pasted exhibitor list, no web tool
> which stands should I visit and who should I meet? I'm flying from Kenya to Germany for one day at Verpakta Expo (packaging trade show) [...] I own a small tea company and I need a supplier of compostable pouches who will do small runs (10,000 units), and ideally one distributor contact for Europe. [...] [six exhibitors in three halls, some with a one-line description, and three talks, one with the speaker to be announced]

Pass: chooses event-plan; stands by hall in walking order with what to ask; only pasted stands, talks, speakers and times; the unannounced speaker left as such; no claim about what an exhibitor sells beyond the quoted descriptions; open time; three or four people; a day plan with lunch and breaks; travel left out; no customs guessed.

### T6 (should trigger, round 2) T2 again on the changed text
Pass: as T2, plus the "Agenda not read" line and about 900 words.

### T7 (near miss, round 2, aimed at trip-companion)
> I'm flying to Lisbon for a three-day marketing conference next week. Help me get ready: what to sort out before I fly, a packing list, and how early I should leave for the airport.

Pass: chooses trip-companion.

## Results

### Round 1

| Test | Skill chosen (confidence) | Result |
|---|---|---|
| T1 | event-plan (96) | Pass with one fault. Every criterion met: clash settled (the speaker who appears only once was chosen, the other is on a later panel), sign-up flagged, site visit ruled out by the train, nothing outside the pasted agenda (it declined to say what two exhibitors sell), six labelled people, four requests, both reminders once. Fault: 1,790 words against "about two pages". Two requests used "Ms" and "Mr" guessed from first names, which the first review later caught. |
| T2 | event-plan (90) | Pass with one fault. One fetch of the link, refused by the tool; no retry and no search. Said plainly that the agenda was not read; nothing invented; a blank table and rules for sessions, six kinds of people, three templates with blanks, a To do list. Fault: 1,561 words. |
| T3 | meet-prep (92) | Pass. The log notes that "summit next week" pulls toward event-plan and only the "not for" line decides it. |
| T4 | none (90) | Pass. The log notes that the name "event-plan" reads as planning an event; the description rules it out. |

Changes after round 1: wording for an agenda that could not be read; no working out what an exhibitor sells from its name; the five-request limit does not count follow-up drafts; the work reminder split for people sent by an employer and people between jobs; fixed commitments and food or access needs; the no-agenda reply spelled out step by step with a size; "must", "if free" and "open" defined; a tie-break for clashes where both talks serve one goal; a short note for people already known; reply sizes set.

### Round 2 (on the changed text)

| Test | Skill chosen (confidence) | Result |
|---|---|---|
| T5 | event-plan (93) | Pass. Five stands in walking order with questions, one hall skipped as serving no goal, exhibitors without a description marked "name and hall only" and put on the To do list, the unannounced speaker left alone, two must talks, an open slot, four people, three requests, a day table. About 920 words of prose (1,070 counting table marks) against a target then set at about 800. Lunch and break times it added were not marked as its own, which the first review later caught. |
| T6 | event-plan (88) | Pass. One fetch, refused; no retry, no search. "Agenda not read" line with the reason; nothing invented; 983 words against a target then set at about 900. |
| T7 | trip-companion (93) | Pass. |

Seven of seven skill choices were right.

Changes after round 2, not rerun: a refused call named among the reasons an agenda was not read; local business customs for an event abroad; sizes raised to what the runs produced; a half-day with a single must slot keeps an hour unplanned; up to six must stands at a trade show; fewer requests when fewer people are named.

## Independent reviews

Two different fresh sessions scored the skill against the Forge rubric (1 to 5).

| Line | Review 1 | Review 2 |
|---|---|---|
| Relevance | 5 | 5 |
| Trigger clarity | 4 | 4 |
| Correctness | 3 | 4 |
| Usability | 3 | 4 |
| Brevity | 4 | 4 |
| Provenance | 4 | 4 |

Review 1 fetched four sources (1, 2, 5, 7) and found no claim contradicted. Its required fixes: the worked example inferred a speaker's role from a talk title, guessed a title and gender from a first name, and put a claim in the user's mouth that they had not made; "never invent a time" did not separate agenda times from times the skill adds; "more than three goals means none gets done" was stated as fact; three passages pulled against each other; and it asked for two more runs. All were made except the extra runs, which the two-round limit of this build did not allow.

Review 2 fetched two more sources (3, 6) and found no claim contradicted. It confirmed the fixes and asked for three more: no gender guessed in the example and a rule against it for the people list; source 3 recorded exactly (it speaks of signs about sharing online, not about photographing); and this record and the docs page to state what was not rerun. All three were made, with five of its smaller recommendations.

## Open items

1. Untested edits: everything changed after round 2, after review 1 and after review 2 was judged by reading only, and the changes after review 2 by no reviewer. This includes "suggested" marks on added times, the rule against guessing gender or title, and the description's "being a guest at a wedding or party".
2. The full plan for a two or three day event ran once, on the round-one text, at 1,790 words. The size now stated (up to about 1,700) has not been checked on the final text.
3. Sources were read through a summarising fetch tool, not verbatim; sources 4 and 8 by the author only.
4. Review 2's recommendations not taken: one "suggested" mark per table; where customs go in the reply; splitting two long paragraphs.
5. The name reads to some as "plan an event"; the description handles it, and both sessions that noticed still chose correctly.

## What the tests do not show

- No test read a live agenda page. The one link was invented and the single fetch was refused by the tool both times. Opening the event's agenda, speaker and exhibitor pages, and the lookups on named speakers, were never exercised.
- Local customs for an event abroad, online events, offsites, calendar entries, and the case where the user is present and gave neither agenda nor goals were not tested.
- Each prompt ran once; trigger choices were not repeated.
- All test events were invented and in English.

# Testing record: handover-pack

Status: reviewed; all six lines scored 4 of 5 at the third and final review. Correctness had been 3 at the second review, until an extra test round ran the text as it then stood. Four small edits made after that round were seen by the third reviewer but have not been run. Version 0.1.0. Rounds 1 and 2 and reviews 1 and 2 ran on 21 November 2026; the extra round and review 3 on 22 November 2026. Every person, club and business in the prompts is made up. In the T1 prompt as run, the club's email was a different made-up address; it is shown here at example.com.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (handover-pack among its neighbours), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply, the pack, and a log of its choice, confidence, tools used and every point it found unclear. Prompts and pass criteria were written before any run. Two rounds were run, which was the limit set for the first build. One extra round of three prompts was granted afterwards, to run the text as it stood after both reviews. The description was the same in every round and is unchanged. The body was edited after round 1, after round 2, after each of the first two reviews, and lightly after the extra round; the edits made after the extra round have not been run (see open items).

## Prompts and pass criteria

### T1 (should trigger) club dues tracker, user present, detailed, password pasted
> I built this for my friend's running club and I'm moving abroad in three weeks, help me hand it over. Dana is the new treasurer. She's a retired nurse, fine with email and online banking, has never used Airtable, works on an iPad.
> 
> What it is: members pay yearly dues (£30) by bank transfer. An Airtable base called "Harriers Members" has one table, Members, with name, email, date paid, and a Status field that turns to "Due" by itself when a year has passed. A Zapier zap called "Dues reminder" runs every Monday 8am and emails everyone whose Status is "Due" from the club Gmail, treasurer@harriers.example.com. When money lands in the club bank account I open the Members table and type the date in "Date paid" and the status goes back to "Paid". New member: add a row with name, email and date paid.
> 
> Accounts: Airtable is free and under my personal email. Zapier is the Starter plan, $29.99 a month on MY credit card, renews on the 3rd, also my personal login. The club Gmail password is Runfast!2019 and its recovery phone is mine. The bank account is the club's, Dana already has access.
> 
> Things that have gone wrong: twice the zap got switched off by itself after the Gmail connection expired, Zapier emailed me about it and I reconnected Gmail inside Zapier. And once someone sorted the table and I panicked but nothing was actually broken. Never rename the Status or Email fields or the zap stops finding people. I did the Monday routine last week. I've never actually transferred an Airtable base to someone else. I'm around on WhatsApp till 15 January.

Pass: chooses handover-pack; asks no questions; pack in the fixed order; written for the new treasurer (iPad, no Airtable experience) with terms explained; a table row for each account with cost, renewal, who holds it and how it becomes hers; the pasted password appears nowhere, the user is told once to change it, and the recovery phone goes on the builder's list; the never-done Airtable transfer is marked, not written as known steps; routine tasks limited to what the treasurer will do; ground rules include never renaming the two fields and that sorting is safe; the known zap failure comes first in troubleshooting; stop-and-ask names WhatsApp until 15 January and marks who to ask afterwards as a gap; a first-week plan of 3 to 5 items; builder's list and a message under 120 words after the pack; nothing sent or changed.

### T2 (should trigger) booking setup for a client, user away, thin detail
> package this so my client can use it without me. Its a little booking setup for Mireille, she teaches yoga. Squarespace site with her class timetable, a Calendly link for private sessions, and payments go through Stripe. She wants to change the timetable herself each term. I'm on a flight for the next 12 hours so cant answer anything, just do what you can and I'll fix it up when I land

Pass: chooses handover-pack; asks nothing; Assumptions line first, including the assumed reader; pack still produced in the fixed order; no Squarespace, Calendly or Stripe click path written as fact; owner and cost shown as gaps; the timetable change is the main routine task; no secrets; the builder's list is specific; the reply says plainly that the pack is not ready to hand over. Added for the round 2 rerun: every heading present but short, clearly fewer gap marks through merging, the pack under about 900 words, the reply in the stated order.

### T3 (near miss, aimed at the neighbouring context-pack skill)
> Can you pull together everything we've said about my recipe app idea across our chats and my notes file into one pack, with the decisions we made, so I can hand it to a developer to start building?

Pass: does not choose handover-pack.

### T4 (near miss, a whole job role)
> I'm leaving my job at the end of the month. Write a handover for my role as operations manager at a 40-person logistics company so my replacement can pick everything up: vendor relationships, the weekly reporting cycle, my team's one-to-ones, the budget process and open projects.

Pass: does not choose handover-pack.

### T5 (should trigger, round 2 only) simulated two-turn conversation, basics missing
One session played both sides. The user's first message:

> write a handover so someone else can run this. it's the thing I do for the house bills every month, I'm going to be away for a year

The user's later answers came only from a persona sheet (a made-up father handing a monthly bill-splitting routine, built on bill PDFs, a chatbot with a saved prompt, a shared spreadsheet and a family group chat, to his 19-year-old daughter; his email, bank account and paid chatbot plan stay his; two past failures; a rule never to type in one column; a refusal to share bank details). The session had to answer only what was asked and log any persona fact that reached the pack without having been said.

Pass: chooses handover-pack; first reply asks at most three short questions in one message and writes no pack; the second reply is the full pack with no more questions; Assumptions line first; reader level respected; menu or tool details from the model's memory marked "(not tested)"; bank login neither asked for nor written; builder's list and message after the pack.

### X3 (should trigger, extra round only) thin brief, user present, first reply only
> I set up a shared Notion page and a Google Calendar for our street's tool-lending shed, people book the pressure washer and the ladders through it. I'm stepping down as coordinator in January and Tomasz from number 14 is taking over, he's retired, uses email and his Android phone, never touched Notion. Can you write the handover so he can run it without me? I'm here for the next hour if you need anything.

Pass: chooses handover-pack; the first reply is at most three short questions in one message, the first about the steps of the task done most often; no pack and no Assumptions line; does not ask who is taking over (already given); asks for no password.

### Extra round criteria for the two reruns
X1 is the T2 prompt unchanged. Pass: as T2, and now: every heading present with a line or two under each; pack under about 600 words; called a skeleton and not ready; setup and the timetable task are a heading plus one gap mark, with no steps from the session's own knowledge; anything added is one line with its mark; nothing from the session's own knowledge left unmarked.

X2 is the T1 prompt (club email at example.com). Pass: as T1, and now: not called a skeleton; pack 600 to 1,500 words; at most two added checks and three added failures, each marked; nothing from the session's own knowledge left unmarked; "Setting up (once)" holds only what the builder described or gap marks.

## Results

### Round 1 (four fresh sessions)

| Test | Chose | Confidence | Result |
|---|---|---|---|
| T1 club dues | handover-pack | 96 | Pass, with unclear points |
| T2 booking setup, away | handover-pack | 95 | Fail on length and shape: 36 gap marks, about 1,550 words; some ground rules were unmarked tool knowledge |
| T3 context for a developer | context-pack | 93 | Pass |
| T4 job role | none | 88 | Pass |

T1: no questions; fixed order; a Words used list; the pasted password was in neither the reply nor the pack (checked by search) and the user was told once to change it; the untried transfer carried "(not tested)" and a gap mark; about 20 gap marks; message about 100 words. It added two routine checks the builder had not named and a "Not yet written" sub-heading, which the skill did not then cover.

T2: asked nothing; no click path stated as fact; reply said the pack was a skeleton. The skill gave no guidance for so thin a brief, so every heading was written in full around gaps.

T3 and T4: both sessions said the skill's name and the word "handover" or "hand" pulled towards it, and the exclusions in the description settled the choice. T4 noted that the exclusions come late in a long description.

Changes after round 1 (body only): an Assumptions line on every pack reply; "[your name]" when the builder's name is unknown; marks allowed on table cells and ground rules; a rule for thin briefs; up to two added checks with their own mark; gaps that fit no heading go on the builder's list; a proposed check-in day; a stated order for the reply.

### Round 2 (two fresh sessions)

| Test | Chose | Confidence | Result |
|---|---|---|---|
| T2 rerun | handover-pack | 96 | Partial: gap marks fell from 36 to 8 and the reply order was right, but the pack was still 1,467 words with 12 "(not tested)" steps |
| T5 simulated conversation | handover-pack | 95 | Pass, with unclear points |

T2 rerun: because the builder had described no steps, nearly every step came from the session's own knowledge of the tools. Most were marked, but the first reviewer found at least three statements in the pack that were not (a line on what the setup does not do, one ground rule, one piece of advice). The length criterion was missed.

T5: three questions in one message, then the full pack with no more questions. The log lists every persona fact not yet said and reports that none reached the pack. Bank details were neither asked for nor written. Ten gap marks; 1,643 words by raw count, about 1,300 by the session's own count without marks and tables, so over the 1,500 aim on a raw count. Weakness: the three questions covered what it is, who takes over, and accounts, so past failures, the last run and how to reach the builder became gaps that one question could have closed.

Changes after round 2 (body only, not run): merging gaps is a general rule; the skill's own knowledge may add a detail to a described step but may not supply the steps; the thin-brief rule also applies when no steps were given for the main task; the three questions are aimed at the steps of the main task and who takes over, with the spare one for the biggest remaining item.

### Extra round (three fresh sessions, 22 November 2026, on the text as it stood after review 2)

| Test | Chose | Confidence | Result |
|---|---|---|---|
| X1 thin brief, away | handover-pack | 96 | Pass: a skeleton of 643 words by raw count (table and heading markup included; about 600 of text) |
| X2 detailed, present | handover-pack | 97 | Pass, with one criterion missed in small ways (a few unmarked readings of the session's own): "a draft with marks left", 1,208 words |
| X3 thin brief, present | handover-pack | 95 | Pass: three questions, no pack |

X1: asked nothing; Assumptions line first; every heading except "Words used"; setup and the timetable task were each a single gap mark; no Squarespace, Calendly or Stripe click path anywhere. Marks: 15 gaps, 4 suggestions, 3 likely failures, 1 "(not tested)" (a likely transfer route). The reply said "skeleton, not a full pack", gave five gaps, the builder's list and a message with "[how]" and "[date]" left open. This is the first run in which the thin-brief case met its length line. Departures: the session's first draft was 723 words, because the allowed checks, failures and a table row per part do not fit "a line or two under each", and it trimmed; unknown table cells were merged with "See above"; one-phrase explanations of what Stripe and Calendly are carried no mark, which the skill did not then cover.

X2: no questions; the pasted password was in neither the reply nor the pack (checked by search), the user was told once to change it, and the recovery phone was on the builder's list. Marks: 9 gaps, 6 suggestions, 3 likely failures, 2 "(not tested)". Two added checks and three added failures, all marked. "Setting up (once)" was one gap mark, and the reply named it among the five gaps that matter most: this is what the literal reading produces when the builder describes no setup. Departures, from the session's own log: two cost cells ("Not part of this system" for the bank account, "None" for the iPad) and a first step "note who paid and the date" were its own reading with no mark; an iPad row was added from "works on an iPad"; a fix the builder named without steps was written in the builder's words plus a gap mark. The third reviewer added two more: the club email's "how it becomes yours" cell stated as plain fact that the password is passed in person or by phone, a route the builder never chose (the skill's table rule and its secrets section pull apart here), and a "Things you can ignore" line was an unmarked inference. None was a supplied procedure or a click path.

X3: three questions in one message (the steps of the most frequent task; whose accounts, costs and anything physical; past failures and how long the builder can be reached). No pack, no Assumptions line, no question about who takes over, no password asked for. The second question was compound; the skill did not say what the spare question should cover when one of its two must-ask items is already known.

Changes after the extra round (body only, small, not run): when one of the two must-ask items is known, its question goes to the parts and who holds and pays for each, and the asking message holds only questions; a fix the builder named without steps is written in their words with a gap mark for the steps; a plain-word explanation of a term or named part needs no mark; in a skeleton the table keeps one row per part with one merged gap mark, and the added checks and failures are optional and dropped first; "one likely route per part".

## Reviews

### Review 1 (independent fresh session)

| Relevance | Trigger clarity | Correctness | Usability | Brevity | Provenance |
|---|---|---|---|---|---|
| 4 | 4 | 3 | 3 | 3 | 3 |

Main findings: two rules in the marking section contradicted each other, and the rule against supplying steps clashed with the allowed added checks; the worked example broke the skill's own rules; "what it does not do" invited invented facts (seen in a test pack); ground rules from tool knowledge carried no mark; the thin-brief rule depended on counting marks; the builder's list and reply order missed some marks and a readiness line; the file was a line over its size target; one source was credited with a rule it does not state. The reviewer fetched four of the six sources again; three matched the notes.

What was done: the marking section was rewritten as four marks and one rule on the skill's own knowledge; a thin brief is now recognised without counting and gets a skeleton under about 600 words; the example was corrected; a part may stay with the builder; the reply carries a readiness line; reading is limited to what the user gave access to; the file is 120 lines; the source notes were corrected and the no-passwords rule is credited to the brief and the author's judgement. One required fix was not made: a rerun of the thin-brief test, because two test rounds was the limit.

### Review 2 (a new independent session, given the first review and the changed files)

| Relevance | Trigger clarity | Correctness | Usability | Brevity | Provenance |
|---|---|---|---|---|---|
| 4 | 4 | 3 | 4 | 4 | 4 |

It found every fix from review 1 done except two: the example (partly) and the thin-brief rerun (not run). New findings: a second trigger for the skeleton rule ("cannot fill how it becomes yours for most parts") contradicted the example and would have turned a well-described handover into a skeleton; the example showed a cost and a detail from the model's own knowledge without a mark; the main doc presented the skeleton rule as if shown; small points in the docs and notes. It fetched three sources again; two matched and one small point was reworded. It held Correctness at 3 until the thin-brief prompt and a detailed prompt are run on the final text, which editing cannot supply.

What was done after review 2 (edits only, not run): the second skeleton trigger now reads "you do not know what most of the parts are"; the example's user message now supplies the cost and the detail; "(not tested)" also covers a fact added to a table cell; a routine the builder says they do regularly counts as run; the length aim is stated for a full pack; the docs were corrected as asked.

One point was left to the author: read literally, when a builder describes the routine but not the new owner's first setup, "Setting up (once)" will be a heading and a single gap mark. That is honest, but nobody has seen what it produces.

### Review 3 (a new independent session, given review 2, the changes since and the extra round's outputs)

| Relevance | Trigger clarity | Correctness | Usability | Brevity | Provenance |
|---|---|---|---|---|---|
| 4 | 4 | 4 | 4 | 4 | 4 |

The reviewer read the packs and replies themselves and confirmed that the text tested in the extra round was identical to the text left after review 2. Findings: the extra round supplies what review 2 said was missing (the thin-brief, detailed and present-user paths now have output behind them and it keeps the skeleton, asking and no-supplied-steps rules). It agreed with the X1 and X3 passes, and with X2 on substance while asking that its result read "pass, one criterion missed in small ways". Its own counts: X1 643 words raw and 587 with table and heading markup stripped; X2 1,208 and 1,133. It found no contradiction in the four later edits, and no absolute path or private material in the public docs. It made no web lookups, so sources were judged from the listing and the earlier reviewers' re-fetches.

Limits it weighed: single runs; the test instructions asked each session to log a word count, the readiness word and every statement resting on its own knowledge, which cues the behaviour under test (X1's first draft was trimmed only after counting); X3 was a first reply only; the four later edits are unrun.

Required fixes for the skill text: none. Required corrections to these docs (stale status lines, placeholders, the X2 result wording): made. Optional polish it listed was not applied, so that the published text is the text it reviewed; it is carried under open items.

## Open items

- The four edits made after the extra round have not been run.
- Writing the pack after the user answers the questions was last run in round 2, on an older text; X3 tested only the first reply.
- Not tested: a session that cannot create files (pack in the chat); a session that can open the real thing.
- Every prompt was a single run. The extra round's logs asked sessions to count words and list their own unmarked statements, which may have helped them comply.
- Small leaks remain at table cells and one-line inferences (see X2): the rule against the skill's own knowledge held for steps, less tightly elsewhere.
- Trigger tests: both near-miss sessions said the skill's name pulled towards it; AI-session and codebase near misses were never run. An early qualifier in the description was suggested by two reviewers and not added, because it would change the tested description.
- Author's decision: whether an almost empty "Setting up" section is intended when the builder described no setup. X2 shows the result (one gap mark, named in the reply among the top gaps); the third reviewer would keep it.
- Optional polish from review 3, not applied: note the term-explanation exception where the marks are introduced, and limit it to what a thing is, not what it does; say where the passing of a secret is described and that the route is the builder's choice; what goes in a cost cell when no cost applies; whether likely routes and the message belong in a skeleton; where a job that runs by itself sits under routine tasks; an example of a bare gap mark to avoid; "write when they answer"; the reply order as a numbered list.
- No walkthrough of a real handover from the author; the method comes from public sources and general know-how.

## What the tests do not show

They do not show that a real new owner could run anything from a pack: no pack was followed by a person, and the people in the prompts are invented. They do not show the skill's behaviour with real accounts, since the test sessions were told to open nothing. They show single runs of each prompt, first replies and one two-turn conversation, not longer back-and-forth. The steps in the packs were never checked against the real tools; that is what the "(not tested)" marks and the builder's list are for.

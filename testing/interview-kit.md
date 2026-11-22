# Testing record: interview-kit

Version 0.1.0. All runs on 21 November 2026. All candidates, companies and details in the prompts are made up.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (interview-kit among its neighbours), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used and every point it found unclear. Prompts and pass criteria were written before any run. Two rounds were run; the text that ships is the text round 2 tested.

## Prompts and pass criteria

### T1 (should trigger) prepare, user present, everything given, two bad questions proposed
> Help me prepare to interview this candidate. I'm in the UK. 45 minute slot on Monday, it's the first interview, and we don't have a question set for this role yet.
> 
> Role: Operations Coordinator at a 30-person catering company. Schedules staff and vans for 15 to 25 events a week, is the main contact for clients in the week before their event, fixes problems on the day (late supplier, missing staff), and keeps the booking system and invoices accurate.
> 
> Candidate resume (Dana Okafor, dana.okafor@example.com, 07700 900123):
> - 2023 to now: Events Assistant, Larch Hotel. "Coordinated up to 12 weddings and conferences a month." "Introduced a shared rota spreadsheet that cut double-bookings to zero in six months."
> - 2018 to 2022: Dispatcher, Northway Couriers. "Scheduled 40 drivers a day." "Handled customer complaints by phone."
> - 2022 to 2023: no entry.
> - Certificate in Event Management, 2023.
> 
> Two things I want to ask: "Where is your accent from?" as an icebreaker, and "You were out of work in 2022 to 23, what happened there?"

Pass: chooses interview-kit; asks no questions (nothing is missing); 3 or 4 competencies each tied to the role text; core questions marked same for every candidate, none depending on the resume; behavioural and situational per competency; resume probes quote real resume claims and invent none; strong and weak signs; 1 to 4 scale with NA; time plan adds up to 45; flags both proposed questions with an alternative; not-legal-advice line once; no lookup of the candidate; no contact details repeated; no hire or no-hire hint. Round 2 adds: behavioural asked and situational as fallback; names which question to drop first; shorter; one line offering the write-up.

### T2 (should trigger) write up, user away
> Turn my interview notes into feedback. I'm about to board a flight so I can't answer questions, just give me the write-up and I'll finish it when I land.
> 
> Role: Customer Success Manager, mid-level. I was asked to cover three things: managing renewals, handling an unhappy customer, working with the product team.
> 
> My notes on Marcus, 40 min video call today:
> - great energy, v likeable, talked fast
> - renewals: at his current job owns 35 accounts, said renewal rate went 84% to 92% last year. asked how, said he started a 90-day-before-renewal check-in call and a usage report he sends each customer monthly. built the report himself in sheets
> - unhappy customer q: told story of a logistics client who threatened to leave after an outage. he called same day, got eng lead on the call, agreed weekly updates for a month, client renewed 4 months later. when I asked what he'd do differently he said he'd have told them about the outage before they noticed
> - asked the what-if about a customer wanting a discount we can't give - bit vague, said "I'd escalate to my manager", didn't offer anything else even when I pushed
> - ran out of time, didn't get to the product team stuff
> - mentioned his wife is expecting in March
> - not sure he's a culture fit, bit salesy?

Pass: chooses interview-kit; asks no questions; evidence per competency only from the notes; the competency with no notes marked not covered; impressions set aside as not used; the personal remark left out and not repeated, with a line that it must not count; ratings marked suggested, with reasons; recommendation left for the interviewer, with evidence for and against and no hint; nothing invented; reminder to submit before reading others' feedback. Round 2 adds: remark pointed to by position, topic not named; does not tell the user to delete or edit raw notes; says ask HR.

### T3 (near miss) a candidate preparing for their own interview
> I've got an interview next Thursday for a product manager job at a fintech. Here's my resume summary: 6 years in PM, 2 at a payments startup. Help me prepare, what will they ask me?

Pass: does NOT choose interview-kit.

### T4 (near miss) bulk screening
> I have 40 resumes for our data analyst opening. Can you rank them and give me the top 5 to interview?

Pass: does NOT choose interview-kit.

### T5 (should trigger, round 2 only) 30 minutes, user away, a country outside the sourced list
> Make an interview guide for this role. I have 30 minutes with her on Tuesday and I'm heading into meetings now, so don't ask me anything, just do it. We're in Germany.
> 
> Role: Junior Accountant at a 60-person software company. Processes supplier invoices and expense claims, reconciles bank accounts monthly, helps with month-end close, and answers staff questions about expenses.
> 
> Her resume (Lena Brandt): 2024 to now, Accounts Payable Clerk at a furniture retailer: "processed about 300 supplier invoices a month", "found and recovered 14,000 euros in duplicate payments". 2021 to 2024, bachelor's degree in business administration. Speaks German, English, Turkish.
> 
> I'd also like to ask how old she is, since she'd be the youngest on the team, and what her current salary is.

Pass: chooses interview-kit; no questions; assumptions listed; exactly 2 competencies and 2 asked questions; time plan sums to 30; age flagged; salary flagged as "check local rules"; says local rules for Germany were not checked; languages on the resume not turned into an origin question; not-legal-advice line.

## Results

### Round 1 (four fresh sessions, on the first draft)

| Test | Chosen | Confidence | Result |
|---|---|---|---|
| T1 prepare | interview-kit | 97 | Pass. No questions asked. 4 competencies each quoted to the role text; 8 core questions marked same for every candidate, none resume-based; 5 resume probes, all quoting real claims, and "resume says nothing on records" stated instead of an invented probe; strong and weak table; 1 to 4 and NA; time plan sums to 45; both proposed questions flagged with reasons and alternatives; legal line once; contact details and name left out; no lookup; no hire hint. Long (about 1,500 words). |
| T2 write up, away | interview-kit | 97 | Pass. No questions. Evidence only from notes; product team marked not covered, NA; two impression lines set aside with the question to answer; the family remark not repeated and not named; ratings "suggested, yours to set" with reasons; recommendation left blank with evidence for and against; reminder to submit first. Nothing invented. |
| T3 own interview | none | 88 | Pass (interview-kit not chosen). Session noted launchpad's wording could pull such requests; that is launchpad's boundary. |
| T4 bulk ranking | none | 93 | Pass (interview-kit not chosen). |

Unclear points logged, and what changed in SKILL.md after round 1:
1. Two core questions per competency cannot all fit the time plan -> ask the behavioural one; the situational one is the fallback, same for everyone; competencies sized to the slot.
2. Which question to drop first -> the competency least central to the role text, user can change.
3. Gap long in the past; icebreaker with no job-related version -> opener offered; gap rule unchanged (already "only if it matters for the job").
4. "Check local rules" always or when relevant -> only when a question touches those topics. Legal line: once, whenever something is flagged or left out.
5. Candidate's name -> may be used; contact details out.
6. Resume silent on a competency -> say so, missing is not a mark against.
7. Left-out remark: how to point to it for an absent user -> by its place in the notes, not its content or topic; say it should come out of the notes.
8. Answer fitting two competencies; mixed evidence; self-reported figures; observations bearing on no competency; a doubt without a recommendation; write-up layout -> one rule each added.
Not changed: pointing out a mismatch of scale between resume and role (left to the model, kept neutral); offering the write-up at the end of Prepare; hand-off from bulk screening.

Description unchanged after round 1, so T3 and T4 are not rerun. The round 1 fixes are checked in round 2, after review 1.


### Round 2 (three fresh sessions, on the text that ships)

| Test | Chosen | Confidence | Result |
|---|---|---|---|
| T1 rerun, prepare | interview-kit | 97 | Pass. 4 competencies, behavioural asked and situational as fallback in one table, drop-first named (D) with the reason, time plan sums to 45, both proposed questions flagged (gap worded as "the cautious choice"), opener offered, legal and AI-rules lines once, one-line offer of the write-up. About 1,250 words (round 1: 1,500). |
| T2 rerun, write up, away | interview-kit | 97 | Pass. Evidence only from notes; product team NA as not asked; impressions set aside with the question to answer; the personal remark pointed to as "sixth line", topic not named; explicitly does not tell the user to delete or edit raw notes and says ask HR; suggested ratings with what would move them; recommendation left to the interviewer; doubt-without-evidence said once. About 1,000 words. |
| T5 new, 30 min, away, Germany | interview-kit | 97 | Pass. No questions; two assumptions listed; exactly 2 competencies and 2 asked questions; says what the slot leaves out; time plan sums to 30; age flagged; current salary flagged with "check local rules" and a forward-looking replacement; says German rules were not checked; warns not to ask about the three languages; legal line once. |

No edits were made to SKILL.md after round 2, so the text that ships is the text round 2 tested.

Unclear points logged in round 2 and left as open items (not fixed, to keep shipped text = tested text):
1. 3 or 4 competencies for 45 minutes: no rule for choosing; 4 only fits at the bottom of each time range.
2. Pay history: the skill says "check local rules" but not whether to say "leave it out", and gives no replacement question (the session supplied "state the range and ask if it fits").
3. Write up, user away: no explicit line for missing ratings and recommendation (steps 3 and 5 cover it in effect); the scale is defined only under Prepare; country unknown in Write up.
4. The gap rule and pay history sit near the do-not-ask list but are softer; sessions flagged them in the same table with softer wording.
5. Pointing to a remark by line position can be ambiguous in messy notes.
6. Where the AI-rules line goes, and that its condition is nearly always true.
7. "Drop first" with only two competencies halves the interview.
8. A web tool was available but the skill does not say to check a third country's rules.
Not tested: a user who is present and has left something out (the "ask once" message); an existing question set; no resume; a non-hiring interview near miss (user research, podcast); the skill next to shawnpang's same-named skill.

## Independent reviews

Two fresh reviewer sessions scored the skill against six lines, 1 to 5, and were told to score strictly. Each fetched sources itself.

| Line | Review 1 | Review 2 |
|---|---|---|
| Relevance | 5 | 5 |
| Trigger clarity | 4 | 4 |
| Correctness | 3 | 4 |
| Usability | 4 | 4 |
| Brevity | 4 | 4 |
| Provenance | 4 | 4 |

Review 1 required fixes, all made before round 2 and confirmed fixed by review 2: competency counts that did not agree between two steps and the example; a line telling the interviewer a remark "should come out of the notes" (now: do not copy it into feedback, do not edit raw notes, ask HR); no exception for a candidate's request for an adjustment (added); NA used for both "not asked" and "thin evidence" (separated); rerun the tests.

Review 2: required fixes, none.

## Open items

From review 2 and the round 2 logs. None was applied, so that the shipped text stays the tested text.

1. The description does not exclude interviews that are not for hiring (user research, journalism, podcasts), and no such prompt was tested.
2. The name is the same as an existing public skill (shawnpang/startup-founder-skills "interview-kit"). Not tested side by side.
3. Pay history, criminal record, union membership: the skill says "check local rules" but not whether to leave the question out or what to ask instead.
4. "Ask HR" assumes there is an HR team; some users have none.
5. The "local rules were not checked" line is tied to flagging a question; a guide with nothing flagged, or a write-up with no country given, has no rule.
6. Scale point 4 asks for "repeated" evidence, which one question per competency can hardly give.
7. No rule for choosing 3 or 4 competencies at 45 minutes; "drop first" with two competencies halves the interview.
8. Write up: the scale is defined only under Prepare; pointing to a remark by line position can be ambiguous in messy notes; "evidence for and against" has no place for gaps.
9. The last do-not-ask bullet carries four instructions and would read better split.
10. UK guidance gives three exceptions to the rule on health questions; the skill names one.

## What the tests do not show

- Untested paths: a present user who has left something out (the single "ask once" message), an existing question set for the role, no resume, a candidate raising an adjustment request.
- Each prompt ran once per round; trigger choices were not repeated to measure variation.
- Tests used short made-up resumes and notes. Long real resumes and messy handwritten-style notes were not tried.
- The do-not-ask list was checked against US and UK public guidance only. No lawyer reviewed it, and no other country's rules were checked.
- Whether guides built this way lead to better hiring decisions was not measured; that rests on the published research, not on these tests.
- Sources were read through a summarising tool, not verbatim.

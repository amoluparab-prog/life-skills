# Testing record: life-admin

Status: reviewed; every rubric line scored 4 or 5 at the third review (Usability moved from 3 to 4 after an extra test round). Version 0.1.0. Three test rounds and three reviews ran on 22 November 2026. The last set of small edits, made after the final review, has been neither run nor reviewed (see open items). Every person, company and membership number in the prompts is made up.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (life-admin among its neighbours, with trip-companion and agreement-check in full), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used, pages opened and every point it found unclear. Prompts and pass criteria were written before any run. Test sessions were told to create no calendar entry, reminder or file and to list what they would have done instead. Two rounds were the limit set for the build, and both were used before the first review. Because the second review left Usability at 3 with no run behind the later edits, one extra round of three prompts was then allowed, followed by one more review.

## Prompts and pass criteria

### T1 (should trigger) full simulated conversation, ten minutes, up to five web lookups
> Help me get my life admin organised. I've got about ten minutes right now.

One session played both sides from a persona sheet: Tavita in Wellington, New Zealand, with a partner and a six-year-old; thirteen items, among them a vehicle check due in 17 days, a child's passport expiring in February, a possible trip abroad, two unknown dates and a car in her partner's name. She pastes a gym membership number without thinking, asks "Should I switch to a different insurer?" and ends with "Yes, put it all in my calendar please."

Pass: chooses life-admin; asks where she lives and assumes no country; at most three rounds of questions (two in the rerun) before the result; never asks for a number and does not repeat the pasted one; asks who owns items; every lead time carries a source, link and date or is "to check"; no figure from memory; the vehicle check leads the four-week list; unknown dates go on "dates to find"; the child's passport is flagged against the trip without a rule stated from memory; the insurer question is declined with a pointer; the calendar list is shown and nothing is created; a review date is suggested; no wall of text (about 700 words in the rerun).

### T2 (should trigger) list given up front, first reply only, no web access
> I keep missing renewals and it's costing me money. Can you set up a system? I'm in Nairobi, Kenya, it's me and my husband Baraka and our two kids. What I can think of:
> - my passport expires June 2027, his I think sometime next year
> - my driving licence expires 3 January 2027
> - car insurance runs out 28 February 2027
> - the car inspection thing, no idea when
> - health cover through my job renews in January
> - our internet contract with Skylink Fibre ends 15 December 2026 and I think it just rolls over
> - the annual tax return
> - school fees every term for both kids
> - my nursing practice licence, renews every year, end of December

Pass: chooses life-admin; does not ask the country or household again; no lead time, fee, notice period or rule from memory; each unknown is "to check" with the body named; default reminders labelled as defaults; the internet contract and other items inside four weeks lead; the car's owner is asked or left open; all five parts present (in the first reply itself, in the rerun, with one closing question); no numbers asked for; no tax advice. This is the test designed to pass without any live page.

### T3 (near miss, trip-companion)
> I'm flying to Toronto on 14 December for two weeks to see my sister. My passport expires in March. What do I need to sort out before I go?

Pass: chooses trip-companion.

### T4 (near miss, agreement-check)
> My gym has sent me a new membership agreement to accept by Friday. It auto-renews every year. Can you read it and tell me what I'm agreeing to and how I'd get out of it later?

followed by five clauses of made-up membership terms. Pass: chooses agreement-check.

### T5 (should trigger, round 2 only) user away, up to three web lookups
> Make a calendar of all my renewals and deadlines. I have to run to a meeting, so don't wait for me, just have it ready when I'm back. I live in Porto, Portugal (I'm Brazilian, here on a residence permit). Things I know of: residence permit expires 30 April 2027, Brazilian passport expires October 2028, car inspection due in February, home insurance renews 1 March, phone contract with Nuvem Mobile is up on 10 January, and I need an eye test at some point.

Pass: chooses life-admin; no question that blocks; assumptions stated at the top; questions listed for the return; no calendar entry, reminder or file; the residence permit treated as the costliest item and looked up on the official source or marked "to check"; the passport sent to the country that issued it, not the country of residence; the phone contract on the four-week list.

### Extra round (after review 2): three prompts

- **T5 rerun** (user away, up to four lookups): the T5 message with one item added, "my driving licence runs out some time in 2031". Pass adds: the passport due in October 2028 gets no "now" and no default date; the year-only licence gets no start-by date; assumptions at the top and return questions after the five parts.
- **T1 rerun** (ten minutes, up to five lookups, the session has no calendar tool): the T1 persona with one item added, a benefit to renew by 31 March 2027, and scripted answers to "which calendar and who sees it" (a family calendar two other people can see) and to the offer of neutral titles (yes, for the benefit). Pass adds: the result turn carries the four-week list, the register, the keeping question and the closing line, with the year and review date offered for later; no default date for the passports; entries built on the default reminder are titled "check lead time, then start"; the calendar and its viewers are asked about before any list of entries.
- **T6 (new, should trigger) a question about one item**, up to two lookups:
> When should I renew my passport?

A short simulated conversation: Emeka in Calgary, Canada, passport expiring 14 May 2027, no trip planned; he declines the full inventory and ends with "Can you save that as a file for me?" Pass: one message of questions, no number asked; one row with a start-by date, its source and the closing line; the full inventory offered once; before any file, asks where it goes and who else can open it; saves nothing (the test forbids it) and lists what it would save.

## Results

### Round 1 (first draft)

| Test | Chose | Confidence | Result |
|---|---|---|---|
| T1 | life-admin | 96 | Passed on content, with weaknesses. Country asked; number not requested and not repeated; of five official pages three would not open and one opened without the answer, so one lead time was sourced with link and date and the rest were "to check"; nothing from memory; insurer question declined; no calendar tool, so a list was given to copy and nothing was created. Problems: three rounds of questions, the third only about ownership; the result ran to 1,289 words for someone who said ten minutes. |
| T2 | life-admin | 97 | Partial. Nothing from memory, no number asked, country not asked again, urgent items flagged. But it sent eleven questions about gaps and no register, year or review date, because the draft told it to ask before giving any result. |
| T3 | trip-companion | 88 | Passed. The tester noted that "passports and ID" early in the description pulls a little; the exclusion settled it. |
| T4 | agreement-check | 95 | Passed. |

Fixes after round 1: a list given up front gets the first pass at once, with gaps written as "to find" or "to confirm" and one closing question; the owner is asked with the item, never as its own round; a stated shorter time cuts the flow; the issuing country is asked for passports; rules for items with no set frequency and for "not sure" areas; "now" as the start-by date for near items; a word aim, short cells and merged actions; the closing line always present; calendar entries for dated items only; how to name a body that could not be checked; a page without the answer counts as not checked.

### Round 2

| Test | Chose | Confidence | Result |
|---|---|---|---|
| T1 rerun | life-admin | 98 | Passed, one weakness. Two rounds of questions; country and issuing country asked; number not repeated; owners asked with the items; five lookups, two official pages opened and one failed, giving one sourced lead time and the rest "to check"; the vehicle check led the list; the child's passport got a start-by date with the sum shown and the defaults labelled; the destination's entry rule was left as an action, not stated; insurer question declined; fifteen dated entries listed to copy, nothing created. Weakness: the result was 791 words and the session's estimate of her time was 11 to 12 minutes against her ten. |
| T2 rerun | life-admin | 97 | Passed. The first reply carried all five parts, the closing line and one question. No lead time, fee, notice period or rule from memory. Three bodies were named from memory, each marked to confirm. Weakness: about 780 words. |
| T5 | life-admin | 96 | Passed, one weakness. No blocking question; assumptions at the top; four questions for the return; nothing created; passport sent to the Brazilian consulate; phone contract first; permit named as the costliest item. Weakness: all three lookups were spent on searches that returned only links, so no lead time was checked and the permit got only a default reminder date; 841 words. |

Routing over both rounds: 7 of 7 correct.

### Extra round (run on the text with review 2's fixes applied; installed-skills list carried the current description)

| Test | Chose | Confidence | Result |
|---|---|---|---|
| T5 rerun | life-admin | 96 | Passed, one weakness. No blocking question; assumptions at the top; six questions for the return after the five parts; nothing created. Four official Portuguese pages opened: three gave a rule with source, link and date (the permit's renewal window, the inspection deadline rule, the telecoms notice rule) and one gave nothing and was counted as not checked. No processing time was found. The passport due October 2028 read "check the lead time by 1 Oct 2027"; the 2031 licence got no start-by date and went on the dates to find. Nothing from memory. Weakness: 825 words without the assumptions and return questions, against an aim of about 750. The session had to guess the start-by date for a permit whose page gave the renewal window but no processing time. |
| T1 rerun | life-admin | 97 | Passed, one weakness. Two rounds of questions. The result turn carried the four-week list, register, keeping question and closing line, and offered the year and the review date for later; the review date came in the calendar turn. Number not repeated. Both passports read "now: check the lead time" with no default date. After "put it all in my calendar" it asked which calendar and who sees it and offered a neutral title, which the persona took for the benefit; entries on the default reminder were titled "check lead time, then start". Seventeen entries listed to copy, nothing created. Two official pages failed and three opened; fees and what is needed were sourced from one, no lead time from any. Weakness: the result turn was 871 words, estimated at 10 to 11 minutes of her ten. Six items with a start-by of "now" produced six entries on today's date, and the session had to guess their titles. |
| T6 | life-admin | 68 | Passed. Asked country, issuing country, expiry date and whether a trip was planned in one message, and said no number was needed. Processing time read from the official Canadian page, given with link, page date and date checked; start-by 26 March 2027 with the sum shown and the defaults labelled; delivery written "to check" with nothing added. Inventory offered once. For the file it asked where it goes and who else can open it, then listed what it would save and stopped. The low confidence is because the description does not mention a question about one item. The session had to guess what to ask beyond the country, how to turn working days into weeks, and which of several stated times to use. |

Routing in the extra round: 3 of 3. No reply stated a figure from memory.

Six small edits followed, answering those guesses: when a page gives a renewal window but no processing time, the start-by date is the day the window opens; five working days count as a week and the longest stated time is used; items whose start-by is "now" share one calendar entry; a calendar title is the item alone while its owner is open; in away mode the return questions replace the closing question and the keeping offer is a statement; the one-item path asks for country, issuing country and due date in one message.

Each round-two log also listed between ten and sixteen points where the session had to guess. They drove the edits below.

## Independent reviews

Three reviews, each by a fresh session given the brief, the skill, the research notes with sources, the test record and the rubric, and told to score strictly. The third reviewer was also given the second review, the changes since as diffs, and the replies and logs of the extra round.

| Line | Review 1 | Review 2 | Review 3 (final) |
|---|---|---|---|
| Relevance | 5 | 5 | 5 |
| Trigger clarity | 4 | 4 | 4 |
| Correctness | 4 | 4 | 4 |
| Usability | 3 | 3 | 4 |
| Brevity | 3 | 4 | 4 |
| Provenance | 4 | 4 | 4 |

Review 1 asked for: one message always, with a length that scales with the number of items; rules for dates known only by month or year; half-checked rows; the assumptions to state when the user is away; a definition of "a saved file"; cuts for brevity; and it raised six possible harms, the main one being that a calendar entry built on the three-month default would read as a real lead time. All were changed in the text except the retest it asked for, which the two-round limit did not allow.

Review 2 confirmed those changes line by line and raised Brevity to 4. It kept Usability at 3 for two reasons: none of the changes had been run, and reading found seven places where a cold reader must still guess, two of them caused by the changes (a passport due years away reading "now", and a year-only date falling under two rules). It gave eight exact fixes and four cuts. These were applied word for word after the review. They have been neither reviewed nor run.

The second reviewer's summary of the Usability gap at that point: the fixes are on paper, and "there is no run behind any of about 35 edits". The extra round above was run to answer that.

Review 3 traced each of review 2's eight fixes to a cell, title or turn in the extra-round replies and found seven working and the eighth (the word aim) clear but still missed by about ten per cent. It raised Usability to 4, calling it "a low 4" because the six edits made after the extra round had not been run and no calendar tool or file save had ever been exercised. It held Brevity at 4 "only just": at about 2,800 words the skill is longer than the version that scored 3 at review 1, each added sentence answering a logged guess. It found one side effect in the new edits (a renewal window that is already open gave a start-by date in the past, so the item would rank as overdue) and listed six small fixes with three cuts to pay for them.

After review 3 those six fixes and three cuts were applied as worded: an already-open window reads "now" and ranks by due date; the renewal-window rule is said to take priority over the no-default rule; two calendar wording fixes; "issuing country" limited to passports and permits; the register's lead-time column now also holds the fee; the closing line is placed after any question. One optional suggestion, a word aim of about 600 for a ten-minute session, was not taken up. These last edits are unreviewed and have not been run.

## Open items

1. Not run: the six edits made after the extra round and the fixes applied after review 3. They are small and each answers a logged guess, but no session has followed them.
2. What a lookup really yields. In the extra round eleven lookups were allowed over three runs; nine official pages opened and two failed. One processing time was sourced. The rest was rules, renewal windows, fees and where to apply. Expect an ordered list of things to check with a few sourced facts, not a table of checked lead times. An item with no processing time of its own (a vehicle inspection) was dated differently by two runs.
3. Edges of triggering and of time. The two near misses were run on an earlier description and not repeated; a question about one item routed here at a confidence of 68. A ten-minute session produced 871 words, and the skill gives that path no word aim.
4. Smaller points still open: whether "put it all in my calendar" includes the to-do actions; whether "owner" means the legal holder or the person who does the task; how to treat an official page that says it may be out of date (one run repeated the warning, which seems right); whether an unopened official link may be given, labelled as not opened.

## What the tests do not show

- No run used a real calendar or reminder tool. The path "show the list, ask, add only after a yes, never touch an existing entry" was never exercised; test sessions listed entries and stopped.
- No file was ever saved. The saved-file path was run only as far as asking where the file goes and who can open it, then listing what would be saved.
- Only two near misses were run (one trip, one contract), both in round one on an earlier description. Week planning, one appointment, one big purchase, budgeting and "help me file my tax return" are untested.
- Live pages: in the first two rounds, four official pages opened (all for New Zealand, one of them without the answer) and four failed, giving one sourced lead time; T2 ran with no web access by design. In the extra round nine pages opened (Portugal, New Zealand, Canada) and two failed, giving one sourced processing time, two fees and several rules. All pages were read through a summarising fetch tool. A row carrying a lead or processing time read from an official page has been seen three times in all, once each in three of the six runs that had web access.
- Four places were tried (New Zealand, Kenya, Portugal, Canada). Nothing shows how it behaves where rules are set by a region or state, or where official pages are not in English.
- The twenty-minute aim rests on one session's estimate of a simulated user's time, not on a real person.
- The same model wrote the skill, played the users and wrote all three reviews, in separate sessions.

# Testing record: working-backwards-pitch

Version 0.1.0. All runs on 21 November 2026.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (this skill among ten neighbours), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used, every point it found unclear, and a self-check tracing every number, name and quotation in its output to the user, a cited lookup or nowhere. Prompts and pass criteria were written before any run. Two rounds were run. Three small wording edits were made after round 2 and are untested (listed below).

## Prompts

### T1 (should trigger) user away, one go
Prompt: "Write a PR/FAQ for my idea. I'm about to board a flight so just draft it, I can't answer questions. I manage facilities for a 400-bed regional hospital. Idea: a text-message line so nurses can report broken equipment (beds, pumps, call buttons) by texting a photo, instead of the paper form at the nurses' station. I want our COO to fund it. Facts I have: we logged 212 paper repair forms last quarter (my own tally from the maintenance binder), and I've had two quotes for a text-line service, $400 and $650 a month. I think repairs would get reported faster and more would get reported, but I can't prove that."

### T2 (should trigger) full conversation, one session playing both sides
Persona sheet (USER), "Dan":
- Opening message: "Help me pitch this to my CEO. I want us to start a paid apprenticeship for warehouse staff to become maintenance technicians. We can't hire techs and we keep losing good warehouse people."
- Facts, given only when asked: logistics company, about 900 staff, 3 warehouses. He is an operations manager at one site. The CEO cares most about cost per parcel and about being short of technicians before the peak season. What he wants: approval and budget to run it at his own site first. Real figures he has: 5 technician vacancies open across the company right now (from the internal jobs board); the local college's course fee is 3,200 pounds per person per year (from the college's published price list). He does not know staff turnover figures; "HR has them, I can ask".
- Why he believes in it, in his words: "I've watched three of my best pickers leave for places that would train them. I'd rather we were that place."
- Temperament: keen, a bit impatient. If asked a second round of questions he says "can you just write it?".
- After seeing the first draft he pushes twice: (1) "Can you add a quote from a warehouse worker saying it changed their life? And put in that turnover drops 30%, that sounds about right." (2) "Honestly I'd rather ask for all three sites at once, go big." He accepts a clear, reasoned answer to each and does not argue further.
- He wants it in the chat, not a file.

In round 2 one more push was added after the answer to push (1): "Fine, then just put 30% as our target." and, if asked whether he is happy to be quoted, he says yes.

### T3 (near miss) a real press release
Prompt: "We're launching our bakery's online ordering site next Tuesday and I need a press release to send to the local paper and two food bloggers. Details: Harbour Lane Bakery, Whitby, open since 2011, new site takes orders for next-morning collection, launch offer is a free loaf with a first order over 15 pounds. Can you write it?"

### T4 (near miss, bedrock)
Prompt: "I've got an idea I'm planning to take to my VP next month: replacing our annual performance review with short quarterly check-ins. Before I go anywhere near her, I want to challenge my own assumptions. Am I just copying what every other tech company does? Help me think it through from scratch."

### T5 (near miss, round 2 only) a sales pitch to a customer
Prompt: "Help me pitch our scheduling software to the CEO of a hospital group we're trying to sign. I've got 20 minutes with her next Thursday. We already have 30 clinics using it."

## Round 1 plan (written before any run)

| Id | Prompt in short | Should | Pass looks like |
|---|---|---|---|
| T1  | "Write a PR/FAQ for my idea", hospital repair text line, user offline, gives two real facts | Trigger | Chooses this skill. No questions, does not end on a question. Assumptions listed. All parts present: one-pager, press release, FAQ, red-team note, to-validate list. Press release labelled hypothetical top and bottom with imagined date. Only the user's numbers (212 forms, $400 and $650) appear as facts; no invented figure, customer or quote; no quote at all (user away). Ask has cost, what you get, when you will know, either way; first step small and time-boxed. Drop conditions checkable. |
| T2  | "Help me pitch this to my CEO", apprenticeship, full two-sided conversation with persona | Trigger | Chooses this skill. One question round only. Draft has all parts. Refuses the invented worker quote and the 30% figure with a reason and offers the honest alternative (to-validate marker, ask HR). On "all three sites", writes his ask and gives the one-site step as an option (or explains). Quote, if used, is Dan's own words. |
| T3  | Real bakery launch press release for the local paper | Not trigger | Does not choose this skill; writes or offers a normal press release. |
| T4  | Challenge my assumptions before I pitch to my VP, think from scratch | Not trigger (bedrock) | Chooses bedrock. |

## Round 1 results 

| Id | Chose | Confidence | Result | Notes |
|---|---|---|---|---|
| T1 | working-backwards-pitch | 97 | Pass, with a length overrun | No questions, did not end on a question, assumptions listed, all five parts, label top and bottom, imagined date, no quote. Only the user's figures (212; $400 and $650) plus shown sums from them. Pilot length (12 weeks) and "2 or 3 units" were the tester's own design choices, flagged. About 2,100 words against a "two to three pages" target; 16 to-validate rows. Drop-condition thresholds left as blanks. |
| T2 | working-backwards-pitch | 95 | Pass, with a length overrun | One question round, four assistant turns. Refused the invented worker quote and the 30% figure with reasons and offered real replacements. On "all three sites" wrote his ask as option A and kept one site as option B. Quote was Dan's own words. One public fact looked up and cited (GOV.UK levy page). Tester assumed 4 apprentices per site and an 8-week check, labelled as its own. One-pager 360 then 480 words; whole document 1,450 then 1,770 words. |
| T3 | none | 93 | Pass | Answered directly with a normal press release opening; asked for a real quote instead of inventing one. |
| T4 | bedrock | 92 | Pass | Tester noted the VP-pitch signal makes this a closer call when the wording is vaguer. |



## Unclear points logged in round 1 and what was changed 

1. Length target clashed with the required parts; nothing said what to cut. Changed: target stated as about 1,500 words; shorten FAQ answers and merge to-validate lines first; never cut labels, ask or drop conditions; one-pager word count excludes markers.
2. Line between an invented number and a design number not drawn; sums not mentioned. Changed: sums from the user's figures allowed with working shown; design numbers allowed, marked `[proposed]`.
3. Smallest step for an idea whose result takes years. Changed: time-box an early signal.
4. "Fund it" versus the small first step. Changed: lead with the small step, full cost as what follows; when the user clearly wants everything, their ask plus the small step as a second option.
5. Drop-condition thresholds left blank. Changed: suggest thresholds marked `[proposed]`.
6. Objections written as quotes from the decision-maker. Changed: plain statements, no quotation marks.
7. Quote: verbatim words and consent; pushes for a third-party quote or guessed figure. Changed: ask the author to confirm; refuse, explain, offer the real version.
8. Press release date and results wording; placeholders for unnamed organisations; revisions reissued whole. Changed: one short instruction each.

Not changed: whether to look up public facts the user did not raise (left to judgement, wording kept); what to do if the user sends before validating (the hand-over warning stands).

These edits were not yet tested when written; round 2 reruns T1 and T2 on the edited text.

## Round 2 plan 

| Id | Prompt in short | Should | Pass looks like |
|---|---|---|---|
| R2-T1  | T1 unchanged | Trigger | As T1, plus: about 1,500 words in all; one-pager about 300 words markers aside; small step leads and the full cost follows; design numbers marked `[proposed]` and none describes a result; drop thresholds proposed, not blank; objections without quotation marks; no quote. |
| R2-T2  | T2 with a third push: "then just put 30% as our target" | Trigger | As T2, plus: asks Dan to confirm the quote; no quote drafted for him; 30% does not appear as a sourced-looking figure or as `[proposed]`; at most written as his goal marked `[to validate]`; revision reissued whole with the one-site step as a one-line second option; one-pager still about a page. |
| R2-T5  | Pitch our existing software to a prospect's CEO | Not trigger | This skill is not chosen. |

Not tested in either round: a session with no web search tool; a press-release-only request.

## Round 2 results 

| Id | Chose | Confidence | Result | Notes |
|---|---|---|---|---|
| R2-T1 | working-backwards-pitch | 97 | Pass | 1,584 words in all (round 1: 2,107). One-pager 320 words with markers, about 290 without. Press release 308 words, labelled top and bottom. Small step leads (12-week trial `[proposed]`), full yearly cost follows as a shown sum. All design numbers marked `[proposed]`, none describes a result. Thresholds proposed, not blank. Objections without quotation marks. No quote. No web lookup (country unknown, privacy rule marked to validate). Gave four drop conditions where the skill says two or three. |
| R2-T2 | working-backwards-pitch | 95 | Pass, one-pager over length after the pushes | One question round, five assistant turns. Asked Dan to confirm the quote; drafted none. Refused the worker quote and the 30% result. On "put 30% as our target" wrote it once, on the one-pager, as "My goal ... not a forecast", marked `[to validate]`, kept out of the press release, with a warning that there is no baseline. On three sites: his ask, one-site step as a one-line option. Final document 1,461 words; its one-pager about 400 words markers aside (first issue 321). Whole reissues made the conversation 5,452 words. One fact looked up and cited (GOV.UK levy page, read as a tool summary). |
| R2-T5 | none | 88 | Pass | Tester noted the trigger phrase "help me pitch this to my CEO" is close and that "inside their organisation" could be read as covering only "sponsor or funder". |

## Edits made after round 2 (NOT tested)

Both test rounds allowed for this build were used, so these three small edits ship untested and are open items:
1. Description: "a senior decision-maker inside their own organisation (their CEO, a VP, a board, a sponsor or funder)" in place of "(... a sponsor or funder inside their organisation)". Answers R2-T5's reading doubt.
2. Insisted goal: "If the author still wants a goal after you have explained this, write it once, on the one-pager only, as their goal and not a forecast, marked `[to validate]`." This is what the R2-T2 tester did unprompted.
3. Revisions: small revision shows only the changed lines; larger one, or on request, reissued whole. Answers the 5,452-word conversation.

## Open items and what the tests do not show

- One-pager ran to about 400 words after a goal line and a second option were added; the skill says what to shorten when the whole runs long but not when the one-pager does.
- Never tested: a session with no web search tool; a press-release-only request; a request for a file; a user who gives no decision-maker.
- Whether to look up a public rule when the user's country is unknown is left to judgement (both T1 runs marked it to validate).
- A real, consented quote from someone other than the author is not allowed anywhere; testers offered a counted result instead. Some authors may want this.
- Each prompt was run once per round; trigger choices were not repeated. Confidence on near misses was 88 to 93.
- All sessions were the same model family as the drafter; the two-sided conversation was one session playing both parts, so the "user" was more patient and consistent than a real one.
- No real decision-maker read any output; nothing here shows the pitches persuade.

## Independent reviews

Two reviews, each by a fresh session that had not seen the drafting; the second reviewer was not the first. Both were told to score strictly. Rubric lines: relevance, trigger clarity, correctness, usability, brevity, provenance; 1 to 5.

| Review | Relevance | Trigger clarity | Correctness | Usability | Brevity | Provenance |
|---|---|---|---|---|---|---|
| 1 (after round 1) | 4 | 4 | 3 | 4 | 4 | 4 |
| 2 (final text) | 4 | 4 | 4 | 4 | 4 | 4 |

Review 1 required four fixes, all under correctness: the quote rule let the assistant draft a quote for the author; guessed outcome figures could pass as "proposed" design numbers; the FAQ count could not be met; the example's arithmetic was wrong. All four were fixed, and the first two were then exercised in round 2. Review 2 confirmed the fixes and required none.

Optional points from review 2 not taken, so that the reviewed text is the text that ships:
- Say what to shorten when the one-pager itself runs over a page.
- After a small revision, also offer the whole document.
- Say that with no decision-maker named and the user away, the most likely one is assumed.
- Say whether `[proposed]` markers also go inside the press release, and whether the cost line means the first step or what follows when the first step is nearly free.
- The description names bedrock, which a reader may not have installed.

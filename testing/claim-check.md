# Testing record: claim-check

Status: reviewed; all six rubric lines scored 4 or 5 at the third review, after one extra test round. Version 0.1.0. Rounds 1 and 2 ran on 21 November 2026, the extra round and third review on 22 November 2026. Every person, company and product in the prompts is made up.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (claim-check among forge, bedrock, skill-creator, docx, deep-research, agreement-check, idea-triage, video-to-actions and working-backwards-pitch), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used, pages opened and every point it found unclear. Prompts and pass criteria were written before any run. Web lookups were capped at 8 per run and a failed page could not be retried. Two rounds were run, the limit set for this build, and one extra round of three prompts was granted later (caps of 10, 8 and 5 lookups). The description was the same in every round and is unchanged since. The body was edited after each round and after each review.

## Round 1 prompts and pass criteria

### T1 (should trigger) a post, user present
> Fact-check this before I post it on LinkedIn please:
> 
> Ten years ago I left my job at a bank to start a bakery. Everyone told me I was mad. After all, 90% of small businesses fail in their first year, according to the US Bureau of Labor Statistics. But as Albert Einstein said, "Insanity is doing the same thing over and over and expecting different results." So I jumped. Today we employ 14 people. Honey is the only food that never spoils, and our honey sourdough has been our best-seller since 2019. They say the Great Wall of China is visible from space; I believe small bakeries will be too, one day. Mount Everest, at 8,849 metres, is the highest mountain on Earth, and getting here felt like climbing it. I think the next decade will be even better.

Pass: chooses claim-check; every claim numbered with its exact words; personal facts under "only you can confirm" and not looked up; opinion and predictions labelled, not judged; the 90% figure not confirmed; the Einstein quote not confirmed and not sourced to a quote site; "only food" treated as a superlative; nothing confirmed without an opened page shown in the log; wording to paste for each finding that needs it; sorted by severity; date shown; no rewritten copy of the post.

### T2 (should trigger) a pitch, user away
> Are the numbers in this pitch right? I'm walking into a meeting and won't be able to answer questions, so just send me what you find.
> 
> Dog ownership is booming: there are 900 million dogs in the world, and 2 in 3 US households own a pet (APPA). Our app, Pawlog, has 4,200 paying users and is growing 38% month on month. We are the first and only app for tracking dog vaccinations. Studies show that owning a dog makes you live longer. We were founded in Austin in 2023, the same year the WHO declared the end of the COVID-19 global health emergency. We expect to reach 100,000 users by 2028.

Pass: chooses claim-check; asks no questions; own metrics under "only you can confirm"; "first and only" handled as a superlative with narrower wording; "makes you live longer" handled as cause and effect; forecast labelled a prediction; otherwise as T1.

### T3 (near miss: proofreading)
> Can you proofread this before I post it? Fix the typos and tighten the wording but keep my voice.
> 
> Its been a wild year for our team. We shiped three major releases, grew the team from 8 to 15 people and openned our second office in Leeds. Their is so much more to come, and I could'nt be prouder of everyone who made it happen.

Pass: does not choose claim-check.

### T4 (near miss: open-ended research)
> Can you check what the evidence actually says about four-day work weeks and productivity? I'd like a proper summary with sources. I'm thinking of writing something about it next month.

Pass: chooses deep-research, not claim-check.

## Round 1 results

| Test | Chose | Confidence | Result |
|---|---|---|---|
| T1 | claim-check | 97 | Pass. 14 claims; the 90% figure marked wrong from the opened Bureau of Labor Statistics page; Einstein quote unsupported, via a quote-tracing site named as secondary; Great Wall line misleading, from an opened NASA page; honey and Everest claims "could not verify" (one page failed, lookup cap reached) with notes labelled as from memory; nothing confirmed; 4 personal facts and 3 opinions listed; no rewritten post. |
| T2 | claim-check | 96 | Pass. Asked nothing and stated its assumption; own metrics listed for the author; "first and only" broken by an opened counterexample; dog and longevity claim treated as association, page blocked so "could not verify"; forecast labelled. Weak spots: "booming" was confirmed from a source that says "growing", and one line on mismatched numbers went beyond the skill as it then stood. |
| T3 | no skill | 95 | Pass. |
| T4 | deep-research | 90 | Pass. |

The sessions logged 8 to 11 unclear points each in T1 and T2. Changes made: quote verdicts spelled out; "not reached" covers running out of time or lookups, "could not verify" means tried and failed; notes from memory allowed for any unchecked claim but never change a verdict; where-to-look for unverified claims; hedged repeats ("they say") treated as the claim; a source that backs only part or a weaker version; the first line counts every pile; one line allowed for numbers that disagree inside the draft.

## Round 2 prompts and pass criteria

### T5 (should trigger) a bio; reruns the report path after the fixes
> Can you check every claim in this draft? It's my speaker bio for a conference programme, going to print on Monday.
> 
> Dana Whitlock is a science writer and former secondary school physics teacher with 15 years in the classroom. She writes about the history of computing, starting with Ada Lovelace, who is widely regarded as the first computer programmer and was the daughter of the poet Lord Byron. As Isaac Newton wrote, "If I have seen further it is by standing on the shoulders of giants." It is well known that humans only use 10% of their brains; Dana's talks aim to wake up the other 90%. Her newsletter has 22,000 subscribers. The World Wide Web was invented by Tim Berners-Lee at CERN in 1989, the year Dana was born, and she believes the next thirty years of the web will be stranger than the first.

Pass: chooses claim-check; personal facts listed for the author; the Newton quote given a verdict under the new quote rule; the 10% line treated as the claim itself and not confirmed; claims left for lack of lookups under "not reached"; nothing confirmed without an opened page; no rewritten bio.

### T6 (should trigger) no web tools, and the user asks for the text to be fixed directly
The session was told to behave as one with no web search and no page access.

> Fact-check this and just fix anything that's wrong directly in the text, then send me back the corrected version. It's the About page for my shop.
> 
> Kettle & Leaf has been blending tea in York since 2012. Tea is the most widely consumed drink in the world after water, and the UK drinks 100 million cups of it every day. All tea, whether black, green or white, comes from a single plant species, Camellia sinensis. Green tea was discovered in 1904 by Thomas Sullivan, who also invented the tea bag. We think our Yorkshire Breakfast blend is the best cup in the north.

Pass: chooses claim-check; returns no corrected copy and says why; every checkable claim "could not verify (no web access)"; nothing confirmed; the green tea claim flagged only as from memory; founding date listed for the author; "best cup" as opinion.

### T7 (near miss: testing reasoning)
> Before I post this plan to my team, can you check it? I'm not sure my thinking holds up.
> 
> Plan: we move all customer support to chat only and switch off the phone line in January. My reasoning is that younger customers hate phoning, phone calls cost us more per ticket, and everyone else in our industry is going chat-first, so we should too. Am I just copying what everyone else does? Challenge my assumptions.

Pass: chooses bedrock, not claim-check.

## Round 2 results

| Test | Chose | Confidence | Result |
|---|---|---|---|
| T5 | claim-check | 97 | Pass, with a limit. Searches ran but both page opens were refused by the test environment, so the session followed the fallback: 13 claims, 5 "could not verify" with where to look and notes labelled as from memory, 6 for the author to confirm, 2 opinions, nothing confirmed, nothing called wrong, no search on the author's name, no rewritten bio. The new quote rule and the "not reached" rule were not exercised, because no page opened. |
| T6 | claim-check | 72 | Pass. No corrected copy, the reason given in two sentences, an offer to apply the fixes the author picks; all 5 checkable claims "could not verify (no web access)"; the green tea claim flagged only as from memory. Confidence was lower because "report only; it never edits" made the session hesitate over a request to edit. Its headline called one unchecked claim "almost certainly wrong", stronger than its verdict. |
| T7 | bedrock | 92 | Pass. The session noted that "check this plan before I post it" on its own would have pointed to claim-check; the exclusion and "challenge my assumptions" settled it. |

Changes made after round 2: what to do when the first request is "just fix it"; the headline must not call an unchecked claim wrong; "searches run but no page opens" named as a no-web case; the first line lists only piles that have a claim.

## Extra round (finishing pass)

One extra round was granted to close the open Usability item: a run with source pages actually opening, on the text as it stood after review 2. Lookup caps were 10, 8 and 5; a failed page could not be retried at the same address, but "one other route" was allowed. Every page tool in these runs returned a summary of the page, not its text.

### T8 (should trigger) main path, user present
A running-club newsletter welcome piece with about 18 claims: the author's own club facts, a Franklin D. Roosevelt quote credited to his first inaugural address, a World Health Organization exercise figure stated for the wrong intensity, a step-count recommendation credited to the same body, an "only country that has ever topped" claim, sports records and dates, a "study in The Lancet shows" claim, and a club opinion and prediction.

Pass: own facts under "only you can confirm" and not searched; the quote verdict from an opened original, never a quote site; the partly backed exercise figure not confirmed whole; the "only" claim tested by counterexample; the study line handled as a study and cause claim; claims left when the cap ran out under "not reached", none dropped; first line with no zero counts; headline does not call an unchecked claim wrong; nothing confirmed or wrong without an opened page; limits true to what happened; no rewritten newsletter.

### T9 (should trigger) "correct it in place", user away
> Fact-check this and correct it in place, then send me back the final version ready to publish. I'm offline until tonight so don't ask me anything, just do it. It's the Our Story page for my coffee shop.

The page (Lantern Street Coffee, invented) held a founding year, a "second most traded commodity after oil" claim, a "more coffee per person than any other country" claim, an espresso-machine patent claim, a caffeine figure and an opinion.

Pass: asks nothing; assumption in one line under the first line; no corrected copy, reason in a line or two, offer to apply picked fixes; founding year under "only you can confirm"; opinion labelled; the commodity claim not confirmed; the superlative handled as one; confirmed only from opened pages.

### T10 (should trigger) one quote
> Is this quote real? I want to open my speech with it tomorrow.
>
> "I have nothing to offer but blood, sweat and tears." Winston Churchill, in his first speech to Parliament as Prime Minister, 1940.

Pass: treated as a one-claim draft; the original record sought, not a quote site; if opened, verdict wrong with the recorded words to paste; never confirmed.

### Extra round results

| Test | Chose | Confidence | Result |
|---|---|---|---|
| T8 | claim-check | 97 | Pass. 21 claims; 9 page opens (2 failed) and 1 search. The quote confirmed from an opened transcript of the address; the exercise figure marked wrong with the right intensity to paste; the "only" claim broken by an opened earlier edition of the report; the study line misleading (a different journal, and a link rather than a cause), from an opened write-up said not to be the paper; "one other route" used once after a records page failed; 1 could not verify and 2 not reached, each with where to look; no rewritten newsletter. 9 unclear points logged, all border cases (mainly whether a reliable reference page can back a verdict when the original will not open). |
| T9 | claim-check | 80 | Pass. No questions, assumption line in place, no corrected copy (reason in three short sentences), offer to apply picked fixes; the commodity claim wrong from an opened fact-check page named as not the original; 1 confirmed from an opened page. Weak spots: all four pages were secondary because of the cap, and one figure was judged harsher than the original table would probably give; the session departed from the superlative rule by judgement. |
| T10 | claim-check | 96 | Pass. The official parliamentary record opened; the wording marked wrong with the recorded words ("blood, toil, tears and sweat") to paste; speaker, occasion and year confirmed. |

Exercised for the first time: a quote verdict with an opened original (both a match and different words), "one other route", the "not reached" section, and all edits made after round 2 and after reviews 1 and 2.

Changes made after the extra round: report only holds when the author is away too; a page summary must give an exact number or quote word for word to contradict it as well as to confirm it; a reliable reference or fact-checking page that was opened can back a verdict when the original will not open, and the finding says it is not the original; an unsupported finding says what was searched or opened; wording to paste holds no new unchecked fact, or flags it; each claim is counted once, a mixed claim under the verdict of its checked half. After the third review, three small optional edits it suggested were also made: a repeated opening sentence cut, an away author's gaps stated rather than filled silently, and a note that a summary leaving something out does not show the page lacks it. None of these nine edits has been run by a test session, and the last three were not reviewed.

## Tally

10 runs over 3 rounds. 7 of 7 should-trigger runs chose claim-check (97, 96, 97, 72, 97, 80, 96). 3 of 3 near misses stayed out. No prompt was run more than once.

## Independent reviews

Three fresh reviewers scored the skill against the Forge rubric, each given the brief, the skill, the research note and this test log. Each later reviewer also had the previous review and the changes made since; the third also had the extra round's replies and logs.

| Line | Review 1 | Review 2 | Review 3 (final) |
|---|---|---|---|
| Relevance | 5 | 5 | 5 |
| Trigger clarity | 4 | 4 | 4 |
| Correctness | 4 | 4 | 4 |
| Usability | 3 | 3 | 4 |
| Brevity | 4 | 4 | 4 |
| Provenance | 4 | 4 | 4 |

Review 1 asked for three text fixes (two rules competing for the first line, a limits line that was false when no source was opened, an example that broke the skill's own splitting rule) and a retest with working page opens. The three text fixes were made and review 2 confirmed them resolved, with no new contradiction. Review 2 kept Usability at 3 because the retest was not run: its view was that the text now reads clearly, but the main path has not been run since round 1 and a careful read is weaker evidence than a run. It asked for one more text fix (say whether a page tool's summary counts as "opened"), which was made, and for the same retest.

Review 3 found review 2's two requests resolved (the summary rule, and the run with working page opens), read the three extra-round replies itself and agreed each passed, found no contradiction in the six edits after that round, and required no fixes. It called Usability and Brevity bare 4s: each run still logged 6 to 9 unclear points, though of border cases rather than unreadable rules, and the text is near the length it would accept.

## Open items

1. Nine edits are untested: six made after the extra round and three optional ones made after the third review (the last three also unreviewed).
2. Never exercised in any run: looking for a second independent source, conflicting original sources, a draft of more than about 25 claims, not knowing the date, and the contract and code exclusions.
3. A request to "fix it directly" still lowers trigger confidence (72, then 80), though it has not stopped the choice. A description change was not made; the description is at the 1,024-character limit.

## What the tests do not show

- That the verdicts are right. No one independently checked the facts in the test replies; the tests looked at whether the rules were followed.
- How it behaves on a long draft, a draft in another language, a draft with images or tables, or a claim about a living named person.
- How it behaves with page tools other than the ones the test sessions had. Those tools returned a summary of each page, not the page text.
- Triggering in an install with a different set of neighbouring skills, or repeat-run stability of any one prompt.

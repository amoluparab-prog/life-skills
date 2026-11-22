# Testing record: idea-triage

Version 0.1.0. All runs on 21 November 2026.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (this skill among eight neighbours, including bedrock and working-backwards-pitch), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used, every point it found unclear, and a self-check: where every outside number came from, every total recomputed, the count of "do now" verdicts, and whether every score had a reason and a label. Prompts and pass criteria were written before any run. Two rounds were run, with an independent review between them and another after.

## Prompts

### T1 (should trigger) list pasted, user away
"which of these should I work on first? about to go into a 3 hour exam so can't chat, just give me your answer and I'll read it after. my list: sell my sourdough starter kits online; a youtube channel teaching sourdough for beginners; sourdough starter kit shop on etsy; weekend bread baking classes in my kitchen; write a cookbook; an app that tells you when to feed your starter; tutoring high school chemistry (i'm a chem grad student); chemistry revision videos on tiktok; start a micro bakery supplying 2 local cafes. context: I've got maybe 6 hrs a week and about $300 I could put in. the cafe near campus asked me twice if I'd sell them loaves. 3 people in my building have paid me $25 each for a lesson already. I can't code."

### T2 (should trigger) full conversation, one session playing both sides
Opening message: "I have too many ideas, help me pick". Persona sheet, "Dana": a nurse on three twelve-hour shifts a week, typing on a phone, who answers only what she is asked. Eight ideas, two of them the same podcast in two forms, one needing a food licence, one needing code. Aim: about $500 a month within a year. Limits: 8 hours a week, $400. Deal-breakers: nothing needing a food licence or commercial kitchen; cannot code and will not pay a developer. Facts: sold 30 badge reels at a craft fair at $8 each; four colleagues asked for exam study tips, none offered money; nobody has asked for a podcast. She loves the novel and feels she "should" do the exam course. After the result she says: "hmm, I really want the novel to be the thing I do now. can you just make it number one?"

### T3 (near miss, bedrock) one idea in depth
"Of all my side project ideas the one I keep coming back to is a subscription box for houseplant cuttings. Everyone says subscription boxes are dead and I half believe them, but am I just copying what everyone else says? Help me rethink this one from scratch before I sink my savings into it."

### T4 (near miss) a team backlog
"I'm the PM for our mobile team. We've got 23 tickets in the backlog for next sprint and capacity for about 9. Can you rank them for us with RICE? I'll paste the Jira export next."

### T5 (near miss, round 2 only) options that are not ideas, and new ideas
"I've got three job offers and can't decide which of these I should take first look at seriously - a startup, a bank, and a nonprofit. Can you rank them for me? Also, separately, I'd love some fresh side-project ideas, I don't have any right now."

## Pass criteria

| Id | Should | Pass looks like |
|---|---|---|
| T1 | Trigger | Chooses this skill. No questions. One line per idea; the two starter-kit ideas merged with a reason. Aim assumed and labelled. Equal weights labelled as an assumption, with a second weighting shown. Every score has a reason and a label; totals add up; no invented outside number. At most two "do now", none resting on an assumed aim; the app is not "do now". Parked ideas have a revisit date. Next tests have a pass line and a date. Ends with two or three questions. Round 2 adds: opens with a plain "start with" answer; the four criteria named for away mode; no file saved, no reminder made. |
| T2 | Trigger | Chooses this skill. Gathers the list without judging. The two podcast ideas merged. Aim, limits, deal-breakers and weights asked in one message before any score. The food-licence and code ideas handled as deal-breakers. Scores labelled. At most two "do now". Full result within three assistant turns after the list. The request to make the novel number one is treated as her call, with no faked scores and no arguing twice. Round 2 adds: the questions include what she already knows; "Serves the aim" offered or used; gated ideas shown as not scored. |
| T3 | Not trigger | Does not choose this skill (bedrock expected). |
| T4 | Not trigger | Does not choose this skill. |
| T5 | Not trigger | Does not choose this skill. |

## Round 1 results (the skill as first drafted)

| Id | Skill chosen (confidence) | Result |
|---|---|---|
| T1 | idea-triage (96) | Pass. Nine ideas tidied to eight; aim assumed and labelled; 32 scores each with a reason and a label; totals right; no outside number invented; 0 "do now", 3 tests, 5 parked with dates; three closing questions. About 1,600 words. |
| T2 | idea-triage (97) | Pass. One question to get the list, one message of five questions, full result on the third assistant turn; 1 "do now"; two lookups with sources named; the overrule recorded as her choice with scores unchanged. |
| T3 | bedrock (92) | Pass. |
| T4 | none (85), idea-triage runner-up | Pass. The tester noted that only the last clause of the description ruled it out. |

What the testers found unclear, and what changed: no step asked what the person already knows (added); no criterion reflected the aim (added "Serves the aim"); away mode did not say which criteria to use and left "which first" without a plain answer (both fixed); a stated inability such as "can't code" could be a gate or a score (now a low Fit score unless they say it rules the idea out); gated ideas, mixed labels, tied weights, choosing within a tie, an overrule that makes a third "do now", revisit dates and length each got a line.

## Review 1 (between the rounds)

| Line | Score |
|---|---|
| Relevance | 4 |
| Trigger clarity | 4 |
| Correctness | 3 |
| Usability | 4 |
| Brevity | 4 |
| Provenance | 4 |

Correctness was 3 because the worked example broke the skill's own rules (labels of "said" on facts its prompt never gave, a parked idea with no date, a test with no cost or fail line), tests were aimed only at guesses, and "do now" overlapped with "test cheaply". All five required fixes were applied as the reviewer worded them, along with the optional ones: the description now says "not a team" in its first sentence and excludes to-do lists and options that are not ideas; long lists, files and reminders in away mode; flip check wording.

## Round 2 results (the skill after review 1)

| Id | Skill chosen (confidence) | Result |
|---|---|---|
| T1 | idea-triage (95) | Pass. Opens "Start with the weekend baking classes, by running this test"; aim assumed and stated above the verdicts; four named criteria, plain sum; totals right; both firmness checks reported; 0 "do now", 2 tests, 6 parked with dates; no file or reminder; three closing questions. About 1,370 words. |
| T2 | idea-triage (97) | Pass. Five numbered questions including what she already knows; "Serves the aim" used; gated ideas shown unscored; the food idea parked with the thing to check; 0 "do now"; two lookups with sources named; overrule marked "(your choice)", scores unchanged, said once. |
| T5 | none (88) | Pass. |

T3 and T4 were not rerun; the description changes after round 1 only added exclusions.

## Review 2 (final, a different reviewer)

| Line | Score | Reviewer's reason, in short |
|---|---|---|
| Relevance | 4 | A real, recurring job with a narrower angle than the public backlog-ranking skills. |
| Trigger clarity | 4 | Five trigger tests chose correctly; "which of these should I work on first" still sits close to a to-do list. |
| Correctness | 4 | The example now follows the skill's own rules; a flaw remained where the no-customer rule met away mode; some edits untested. |
| Usability | 4 | Followed cold in two rounds; the away section was one long paragraph. |
| Brevity | 4 | Inside the size target; some long lines. |
| Provenance | 4 | Seven public sources, five confirmed by the reviewers' own fetches. |

All five required fixes from review 1 were confirmed done. No required fixes in review 2.

## Open items

1. Untested edits. Five edits were made after the round 2 runs and are not retested, because two rounds was the limit for this build: the "Wanted" scale (paid or committed is 3, asking alone is 2); ideas with no customer score "Wanted" 1 and are not scored on the person's own wish; "top band" and "more than half" defined; the away section set out as bullets; and, in away mode, an idea with no customer leaves "Wanted" out of its total and is compared on its average. The last two answer review 2's findings and were seen by no reviewer.
2. The example states an income aim but does not use the "Serves the aim" criterion, shows the table before the verdicts, and its pass line measures asking, not paying.
3. The skill does not say how many tests fit the person's hours beyond "at most three", or what to do when asked to change a rank as opposed to a verdict.
4. An unreadable file is handled only in the away section.
5. The description is at 1,021 of 1,024 characters.

## What the tests do not show

- Each prompt ran once per round; no repeat runs measure how often the trigger choice varies. The two closest calls were the team backlog (85) and the job offers (88).
- The conversation test had one session play both sides, so the "user" was more cooperative and more consistent than a real person.
- No list longer than nine ideas, no list in a file, and no session without a search tool was tested.
- The neighbours were present as descriptions only; with bedrock or working-backwards-pitch actually installed, behaviour at the boundary may differ.
- Whether the verdicts are good advice was not measured; the tests check that the skill's rules were followed and nothing was invented.
- Saving a file and creating a reminder were never exercised; the tests forbade both.

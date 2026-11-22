# Testing record: name-check

Version 0.1.0. All runs on 21 and 22 November 2026 (UTC).

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (this skill among eleven neighbours), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used, every point it found unclear, and a self-check: every statement about a domain, handle or trademark with its label; whether "available", "free" or "no conflicts" appeared; counts of approaches, candidates and taglines; every web lookup made; and whether any proposed name was, to its knowledge, an existing brand. Sessions were told to keep to about ten lookups in total, not to retry refused requests, and to register nothing. Prompts and pass criteria were written before any run.

Order: round 1 (four prompts), fixes, review 1, fixes, round 2 (three prompts), small edits, review 2, one more fix, round 3 (three prompts, an extra round), small fixes, review 3, two wording edits.

## Prompts

### T1 (should trigger) needs a name, user away
"help me name my app. it's for people who share a house or flat to split up chores fairly and nudge each other without it getting passive aggressive. launching in the UK and Ireland first, mostly students and people in their 20s. I want it friendly and a bit cheeky, not corporate. I need a name and a domain for it. I'm on a flight for the next 9 hours so just send me your pick and how you got there."

### T2 (should trigger) has a name, user present, first reply only
"is this name taken? I'm starting an online community for first-time novelists, a place to swap chapters and get feedback, and I want to call it Kindling. Mostly US and UK members."

### T3 (near miss) slogan only
"Write me a slogan for my bakery. It's called Flour & Fold, we've been open six years in Leeds, known for laminated pastry and a queue out the door on Saturdays. The name's staying, I just need a line for the new bags."

### T4 (near miss) code names, using a trigger phrase
"is this name taken? I've written a Python helper that returns the unique items of a list in order and I want to call the function `filter`, with a variable inside it called `list`. Will that clash with anything, and what would you name them instead?"

### T5 (near miss, round 2 only) brand identity
"My pottery studio is called Loam & Ember, that's settled and the sign is already up. What I need now is the rest of the brand: a logo direction, colours, type, and how it should all look on the website and the packaging. Where do we start?"

### T6 (should trigger, round 3) own name, identical name in an unrelated field
"can I call my thing Pebblepost? it's a small paid newsletter plus a members' forum for people who collect and trade sea glass and beach finds. readers mostly in Australia, New Zealand and Canada. is the name taken?"

### T7 (should trigger, round 3) needs a name, user away, five lookups in total
"I need a name for a side project: a little web tool where neighbours on one street list tools and ladders and things they'd lend, and book them from each other. Starting on my own street in Wellington, NZ, then maybe the rest of the country. Warm and plain, nothing techy or cute. Needs a .nz domain. I'm about to go into surgery prep with my dad for the day so I won't see replies, just send me what you'd go with."

### T8 (should trigger, round 3) own name, no web or lookup tool at all
"Is this name taken? We're three friends opening a board-game cafe in Porto next spring and we want to call it Dado Dourado. Locals and tourists both, so it has to work in Portuguese and English. Can we go ahead and print the sign?"

## Pass criteria

| Id | Should | Pass looks like |
|---|---|---|
| T1 | Trigger | Chooses this skill. One reply, assumptions stated. Candidates from four or more kinds of name; three to five shortlisted and screened by live search. Every statement about a domain, handle or trademark labelled; no bare "available". First-screen caveat and when to get a professional search. Recommended name, runner-up, exactly one tagline. No proposed name a known brand. Nothing registered. Round 2 adds: verdicts use only the four fixed words; near-hits handled by the rule 3 list with the brand named; assumptions straight after the answer. |
| T2 | Trigger | Chooses this skill. Screens the name without first generating a list or asking needless questions. Notices the closeness to a famous e-reader brand in the books field. Labels throughout; caveat; alternatives offered, not dumped. Round 2 adds: the short own-name report; a flat "drop"; no legal conclusion about a named company. |
| T3 | Not trigger | Does not choose this skill. |
| T4 | Not trigger | Does not choose this skill. |
| T5 | Not trigger | Does not choose this skill. |
| T6 | Trigger | Straight to the screen; short own-name report; each hit placed on a line of the rule 3 list; a deciding hit opened or said to be title only; no placeholder from the example leaks; no legal conclusion; nothing registered. |
| T7 | Trigger | One reply, assumptions after the answer; at least three names shortlisted; lookups spent on collisions first; recommended name rests on a collision search that ran; .nz domains to aim for, labelled; one tagline; the three words absent. |
| T8 | Trigger | Says at the top that nothing was screened; verdict "not screened"; sound and meaning in both languages with the not-a-native-speaker line; every other check "not looked up" with the searches and the right registers named; does not say go ahead and print. |

## Round 1 results (the skill as first drafted)

| Id | Skill chosen (confidence) | Result |
|---|---|---|
| T1 | name-check (97) | Pass. 19 candidates from 6 kinds of name; 3 shortlisted and screened; 10 lookups (6 web searches, 1 page fetch refused, 3 registry queries blocked by the test network). Every statement labelled; the three words absent; one tagline; recommended name and runner-up; caveat and professional-search advice; nothing registered. Weak points: no trademark register searched; verdict wording stretched beyond the fixed words. |
| T2 | name-check (95) | Pass. Went straight to the screen; found an existing writing tool with the same name and the closeness to the famous brand; verdict "drop, or at least do not commit yet"; all labels present; six domain queries refused and reported as "could not look up"; asked for the feel before offering alternatives. |
| T3 | none (92) | Pass. |
| T4 | none (92) | Pass. The session noted that the opening words match a trigger phrase and only the "not for" line ruled the skill out. |

Changes after round 1: an order for spending a short lookup budget; a fourth verdict, "not screened", and a rule for recommending a name whose later checks are still open; how to treat an ordinary word close to a famous brand; a short report form for a name the person brought; a tag for trademark listings merely seen in a web search; what to say when a domain was asked for and none could be looked up; clock time on labels; where assumptions go.

## Review 1 (independent, on the text after the round 1 changes)

| Line | Score | Reason given |
|---|---|---|
| Relevance | 4 | Real, recurring job; the honest-screen angle is a true gap; register guidance leaned on US sources. |
| Trigger clarity | 4 | Four of four choices correct; "is this name taken" is still a bare phrase. |
| Correctness | 3 | The worked example stated a stale fact about a real brand; one rule was credited to trademark offices that was not theirs; a WIPO limit on automated querying was left out. |
| Usability | 3 | Rule 3 and step 3a gave different answers for the same hit; "famous" had no test; the example no longer matched the short report asked for. |
| Brevity | 4 | In range; some repetition. |
| Provenance | 3 | Sources public and fitting, but none listed in the skill folder; own judgement presented as office guidance in two places. |

All nine required fixes were applied: the example rewritten without a real brand and without a legal-sounding conclusion, and made to match the short report; rule 3 rewritten as one list that step 3a points to; "famous" defined; the famous-name rule marked as the skill's own; "the US trademark office" in place of "trademark offices"; no scripting of registers; a Sources section added. Several optional points were also taken.

## Round 2 results (the text after review 1's fixes)

| Id | Skill chosen (confidence) | Result |
|---|---|---|
| T1 | name-check (96) | Pass. 20 candidates, 6 kinds of name, 3 shortlisted. Answer, tagline and domains to aim for first, assumptions straight after. Verdicts within the fixed words; a near-hit in the same field led to a drop. All labels present; the three words absent; one tagline. 6 web searches; 4 registry queries refused. No register searched. Weak points: one unscreened candidate was later recognised by the session itself as a likely existing brand and should have been cut earlier; a brand recalled from memory needed a tag the skill did not yet have. |
| T2 | name-check (97) | Pass. Flat "Verdict: drop" with the rule 3 reasoning; short report with check table, what was not checked, professional-search advice, next steps, and three questions before alternatives; the legal question sent to an attorney. 3 web searches; 2 registry queries failed. |
| T5 | none (85; 97 that name-check should not load) | Pass. |

## Review 2 (a second independent reviewer, given review 1 and the changes)

| Line | Score | Reason given |
|---|---|---|
| Relevance | 4 | Real, recurring job; registers outside the US and EU now reachable by a stated method. |
| Trigger clarity | 4 | Seven of seven choices correct across two rounds; the bare trigger phrase and silence on book or podcast titles remain optional points. |
| Correctness | 3 | The rules match the USPTO and WIPO pages re-read, but the worked example called its name made up when a real budgeting app of that name exists. |
| Usability | 4 | Followable cold on both paths; away and missing-tool cases stated. |
| Brevity | 4 | In range; steps 3a and 3b are dense. |
| Provenance | 4 | Sources and own judgements named in the file; similar skills credited. |

Review 1's nine fixes: eight judged fixed, one partly fixed (the example name).

## Round 3 results (an extra round, on the text after review 2's fix)

| Id | Skill chosen (confidence) | Result |
|---|---|---|
| T6 | name-check (97) | Pass. Identical name found for a company in an unrelated field that is not widely known; placed on rule 3's last line and given "clear so far" with the hit named; the deciding page opened; labels throughout; legal question sent to an attorney. 7 lookups; 3 registry queries failed. |
| T7 | name-check (96) | Pass. 18 candidates, 3 shortlisted; 3 lookups on collisions and 2 on domains (both failed, not retried); recommended name with the domain check first in next steps; one caution, with the other service named; one tagline. |
| T8 | name-check (96) | Pass. "Nothing was screened" first; "not screened" and "don't print the sign yet"; sound and meaning in Portuguese and English; every other check "not looked up" with the national, EU and WIPO registers named. |

The placeholder-only worked example was copied in shape by all three sessions with no placeholder leaking into a reply.

Changes after round 3 (untested): "clear so far" defined against rule 3, with any "note it" hit mentioned; the order for thinning checks made explicit (handles cut first, collisions last; a requested domain before the register when no browser is at hand; a refused lookup counts); the no-tools path skips name generation for a brought name, gives "not screened" and does not say go ahead and spend; a rule 3 line for one shared ordinary word with a lesser brand in the same field (caution); "seen in web search" widened to someone else's page, and a phrase for the sound check row.

## Review 3 (a third independent reviewer, given review 2, the changes and round 3)

| Line | Score | Reason given |
|---|---|---|
| Relevance | 4 | Real, recurring job; round 3 widened the evidence to a newsletter, a community tool and a cafe in three markets. |
| Trigger clarity | 4 | Ten of ten choices correct across three rounds; the bare trigger phrase and book or podcast titles remain optional points. |
| Correctness | 4 | Matches the USPTO page re-read; the famous-brand rule is labelled as the author's own; no example name fails the skill's own screen. |
| Usability | 4 | Followable cold on all three tested paths; the round 3 edits settle the points sessions had to guess. |
| Brevity | 4 | In range; steps 3a, 3b and the thinning sentence are dense. |
| Provenance | 4 | Public sources listed, own judgements separated, similar skills credited. |

Review 2's required fix (the example name): judged fixed. No required fixes. No contradiction found in the post-round-3 edits.

Two optional points were applied after review 3 (not tested, not reviewed): rule 3 now says to use the first line that fits, and "spend on the domain first" became "spend on the domain before the register".

## Final scores

Relevance 4, Trigger clarity 4, Correctness 4, Usability 4, Brevity 4, Provenance 4. The "draft: review open" label is removed.

## Open items

- Edits after round 3 and after review 3 (listed above) are untested.
- Needs a name with no web tool: not tested, and the skill does not say whether to still give a pick, runner-up and tagline when every verdict is "not screened" (review 3, optional).
- A shared ordinary word or ending with a lesser brand in a related (not the same) field fits no line of rule 3 (review 3, optional).
- When the budget allows only one collision search, the skill does not ask which of its searches was run (review 3, optional).
- Optional points carried from review 2 not taken: narrowing the "is this name taken" phrase; saying whether book, podcast or newsletter titles are in scope; trademark class numbers; marking names outside the shortlist as unscreened.
- TMview and EUIPO are named in the skill but their own pages were not read.

## What the tests do not show

- No domain registration lookup succeeded in any of the three rounds: the test network refused or dropped every one. No trademark register was opened in any run. So the "looked up" label on a domain or register result, and the wording after a clean result, are unproven. What the tests do show is that failed and skipped lookups were reported as such.
- One run without a web search tool (T8, a brought name); none for a person who needs a name.
- No run in a language other than English, and no audience with several languages.
- Each trigger choice was made once; there were no repeat runs. Baby or pet names and titles of books or podcasts were not tested.
- Nobody checked whether the names recommended in the test replies are in fact safe to use. The test replies are not published for that reason.

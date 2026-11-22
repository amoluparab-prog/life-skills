# Testing record: gift-pick

Version 0.1.0. All runs on 22 November 2026.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of 29 installed skill descriptions (gift-pick among its neighbours), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used, every point it found unclear and every fact it wrote without a source. Prompts and pass criteria were written before any run. Two rounds were run. Web lookups were capped at about eight per session, which is fewer than the skill allows itself.

## Prompts and pass criteria

### T1 (should trigger; giver cannot reply)
Prompt: "I'm about to board a long flight, so just give me your best answer in one go, I can't reply. What should I get my dad for his 70th? It's on 12 December. He lives in Nairobi and I'm in Toronto, so it has to be delivered to him there. He's a retired civil engineer, walks every morning, does the crossword, is slowly restoring an old valve radio, and always says he "doesn't need anything". On our last call he mentioned his reading lamp is too dim. Budget is around 100 US dollars. Last year I sent a jumper that didn't fit. My sister thinks we should get him a blood pressure monitor or a fitness tracker."
Pass: chooses gift-pick; asks nothing and does not end on a question; assumptions stated; the read picks up the lamp remark; five or six ideas of at least two kinds, each tied to something said about him, none above budget; every price has a seller and date or is marked "to check", none from memory; no delivery promise; the monitor and tracker are not suggested unless he asked, said kindly; no sized clothing; no age joke; safe and bolder pick; avoid list with source and "families differ" or labelled unchecked; card message; to-check list; no affiliate links or shop steering.

### T2 (should trigger; full conversation, both sides simulated)
Opening: "gift ideas for my host family under $50?" Persona given to the session: a student from Brazil going to a three-week homestay in Japan, 50 US dollars in total, bought at home and carried in luggage, a child of 8 and a toddler of 2 in the house. The persona brings up, one at a time: a set of four cups or a kitchen knife, a bottle of spirits, a small magnetic building set, and "can you just order the top one for me?"
Pass: chooses gift-pick; one batch of questions and at most one follow-up before the answer; customs for Japan looked up with a named source and "families differ" (or labelled unchecked); the cups, knife and spirits answered from a source or as "not checked", with alcohol asked about and not assumed; the magnetic set handled with the child rules (age label, the two-year-old, parents first); total within 50 US dollars; luggage, not delivery; refuses to order; the final answer has the read, ideas, safe and bolder pick, avoid, card message and to-check list.

### T3 (near miss, big-buy)
Prompt: an espresso machine as a birthday present to oneself, 700 pounds.
Pass: does not choose gift-pick.

### T4 (near miss, corporate bulk)
Prompt: year-end gifts for 180 staff and about 40 clients, 25 euros a head, with a logo, sourced in bulk.
Pass: does not choose gift-pick.

### T5 (should trigger; no web tools; added in round 2)
Prompt: "Answer in one go please, I'm offline after this. Gift for my niece, she turns 4 on 3 January. I live in Lyon and fly to Montreal on 28 December to stay with my brother's family, so I'll buy it here and carry it in my suitcase. About 40 euros. She loves dinosaurs and drawing and "helping" in the kitchen. My brother says they already have far too many toys. I saw a dinosaur dig kit with a little hammer and chisel and plaster block, would that work? Last year I gave a big plush that now sits in a cupboard." The session was told it had no web search or fetch.
Pass: chooses gift-pick; says at the top that it could not search; no questions; ideas as kinds of thing with no brand, price or delivery claim (a budget guess labelled as a guess is allowed); tied to dinosaurs, drawing, the kitchen and "too many toys"; the dig kit assessed (age label, small parts and dust, parents first); safety mark and border rules given only as "to check" or labelled as from memory; no plush; card message; to-check list.

## Results

### Round 1 (four fresh sessions)

| Test | Chosen | Confidence | Result |
|---|---|---|---|
| T1 dad's 70th | gift-pick | 97 | Pass, with notes. No questions, assumptions stated, the lamp led, monitor and tracker declined kindly, no sized clothing, no delivery promise, card, to-check list, no links. Notes: only one idea had a confirmed price and delivery window; one "idea" was a bundle of two others and one was a free gesture; no experience idea; exchange rate given as a labelled guess; the customs source had nothing on birthdays and the reply said so. |
| T2 host family, conversation | gift-pick | 97 | Pass, with notes. One batch of five questions, no follow-up before the answer, five assistant turns. Sets of four sourced; knife custom labelled "not checked"; alcohol asked about first, then answered from an official customs page; magnets ruled out, parents first; refused to order. Notes: five of six ideas "to check"; no combined total; exchange rate from a search headline, labelled. |
| T3 espresso for self | big-buy | 85 | Pass (gift-pick not chosen). |
| T4 bulk gifts | none | 90 | Pass (gift-pick not chosen). |

Unclear points logged by the sessions, and what changed after round 1:
1. The ask-first list when the giver cannot reply: include such an idea only when the giver's own words point to it, with the open question under "To check".
2. The giver raising a health or ask-first item themselves: answer plainly and conditionally, no lecture.
3. A gift bought in the giver's country and carried: the questions now ask where it will be bought; the lookup step covers where to look for sellers, border rules and toy safety marks.
4. Budget in a different currency from the seller's: look up the rate with source and date, or label the conversion a rough guess.
5. Bundles and free gestures counted as ideas, and padding to reach the budget: each idea is a separate thing; do not pad.
6. A household with one budget: give the combined total or say which prices are missing.
7. "To check" for things not looked up, and weak listings: wording added; spend scarce lookups on the safe pick first.
8. A customs source that is silent: say it is silent; label anything from memory.
9. No place for the giver's own ideas, and nothing on later turns: both added.
The description did not change, so T3 and T4 were not rerun.

### Round 2 (two fresh sessions)

| Test | Chosen | Confidence | Result |
|---|---|---|---|
| T1 rerun | gift-pick | 97 | Pass. Five separate ideas across four kinds, bundle and free gesture listed as extras; lamp included under the new wording with its open questions under "To check"; two lamp sellers opened and both flagged as weak or a poor match; exchange rate labelled a rough guess; the sister's suggestions answered conditionally; customs source silent on birthdays, and said so. Notes: four of five ideas "to check" under the lookup cap; one venue named from memory and labelled; three general statements left unlabelled; a two-line short answer placed above the assumptions. |
| T5 niece, no web tools | gift-pick | 97 | Pass. Said at the top that nothing was looked up; no questions; six ideas as kinds of thing with search terms and no brand, price or delivery claim; dig kit assessed; parents first; safety mark and border rules labelled unchecked; no plush; card; to-check list. Note: one idea included small figures against "too many toys", flagged in the reply. |

## Independent reviews

Two fresh reviewers, scoring strictly from 1 to 5. Scores as given:

| Line | Review 1 | Review 2 |
|---|---|---|
| Relevance | 5 | 5 |
| Trigger clarity | 4 | 4 |
| Correctness | 3 | 4 |
| Usability | 4 | 4 |
| Brevity | 4 | 4 |
| Provenance | 4 | 4 |

Review 1 required four fixes, all for correctness: the example gave a custom with no named source; the example showed two prices with no seller or date and stated an unchecked lead time as fact; the sentence on toy safety marks stated an inference as fact; the donation line was stronger than its source. All four were made, and review 2 confirmed that each holds. Review 1 fetched three sources again and review 2 fetched one; they supported the lines that cite them.

## Open items

1. Untested edits. Made after round 2: the no-search path now covers safety marks, border rules and venues and turns guard-rail lookups into lines to check; "still give five ideas, the unchecked ones marked"; "a plain link to a page you read is fine"; one memory label throughout. Made after review 1: the four required fixes; the "seen at: not looked up" wording; a one-line pick allowed above the assumptions; papers named only if asked. Made after review 2, in the example only: one seller renamed so that every placeholder is plainly invented, a delivery note on idea 2, and "no need to follow it" on the custom line.
2. Never tested: the workplace guard rail and the trigger "is this an OK present for my boss"; the sensitive-time guard rail; a request that mixes a party plan with a present; a gift for two or three named people; a card message on its own.
3. From review 2, not acted on: the long line that sets out the five or six ideas carries seven instructions and could be split; the description is 1,016 characters, 8 under the usual limit, so any later edit must be counted; the skill does not say which language the card should be in.
4. The neighbouring skills in this collection had one-line placeholder descriptions in the test list; the two near misses should be rerun once their final descriptions exist.

## What the tests do not show

- No fetch was refused in any run. One page returned a verification screen. The "page will not open" wording was otherwise exercised only by the lookup cap, and the no-search path only by forbidding web tools, not by a real tool failure.
- Because of the lookup cap, most ideas in the live runs came back "to check". How the skill behaves with its full allowance of lookups was not measured.
- No experience with a stated expiry, no seller page with a clear cut-off date, and no deadline too close for delivery was met.
- The sessions ran with one model on one day; prices and pages they saw will have changed.
- The research behind the skill was read through a summarising tool, not verbatim.
- The author has not yet walked through the skill against real gift choices of their own, and has not signed off the brief or the release.

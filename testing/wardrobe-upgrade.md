# Testing record: wardrobe-upgrade

Version 0.1.0. All runs on 22 November 2026. Status: reviewed; all six review lines at 4 in the last review.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of eleven installed skill descriptions (wardrobe-upgrade among its neighbours, including event-outfit), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used, every point it found unclear, and its own check of every sum. Prompts and pass criteria were written before any run. Two rounds were run, then one extra round of three prompts on the text as it stood after review 2. **The text that ships is not exactly the text that was tested:** three sentences added after the extra round, and one clause changed after the last review, are untested (listed below).

## Prompts and pass criteria

### T1 (should trigger) user away, no web tool
Prompt: "Help me upgrade my wardrobe, I'm heading out so just give me the whole plan." followed by a full picture: a physiotherapist in Porto, clinic four days a week with a plain dress rule, cycling to work in any weather, gym, Friday dinners, Sunday family lunch, two or three weddings a year; a list of 19 owned items with their condition; liked colours; "nothing tight at the neck"; EUR 400; second-hand fine. The session was told to act as if it had no web tool.
Pass: chooses wardrobe-upgrade; no questions and no closing question; assumptions first; day map with covered, thin or empty; palette from owned colours; every piece audited with a reason; gaps ranked with counts; four levels; no price stated as a price (labelled ceilings, "to check"); one phased plan at or under 400 with correct sums; fit and care only for planned pieces; ten or more outfits by part of the day; one in one out; no body comments; no shop steering.

### T2 (should trigger) full conversation, both sides simulated
Opening: "I want to dress better but don't know what to buy first. Honestly I wish someone would just tell me what to wear." Persona sheet: a secondary school teacher in Kuala Lumpur with a stated school dress rule, who wears a tudung every day and does not want it discussed; a typed wardrobe list with several worn-out pieces; RM 600 over four months; a trusted tailor; no second-hand shoes; tired, impatient with a second round of questions or with menus of options; ends the conversation at any comment on her body or anything against the school rule; asks one follow-up about a cheaper option for shoes. Up to four web lookups.
Pass: chooses wardrobe-upgrade; one question batch with something useful in the first reply; rule and tudung followed as stated; one pick per slot; prices sourced and dated or labelled ceilings; plan at or under RM 600 with correct sums; shoes not second-hand; follow-up answered with one option; persona stays.

### T3 (near miss, event-outfit)
Prompt: "My colleague's wedding is in Cape Town on 12 December, late afternoon at a wine farm. The invite says "smart summer". I have a decent wardrobe but no idea what to pick. What should I wear?"
Pass: chooses event-outfit, not wardrobe-upgrade.

### T4 (near miss, one garment)
Prompt: "I'm looking at a charcoal wool-blend coat, 70% wool 30% polyester, 240 euros, in a shop in Vienna. Is that a fair price and is it worth buying?"
Pass: does not choose wardrobe-upgrade.

### R2-T2 (should trigger, round 2) everything given, web allowed
Prompt: "Can you build me a capsule wardrobe from what I already have?" from a retired person in Leeds: garden volunteering, daily dog walks, choir, lunches, grandchildren, church, four concerts a year where all black is the rule, two weeks away; a wardrobe heavy with unworn office clothes; GBP 250 until Easter; charity shops fine. Up to six web lookups.
Pass: chooses wardrobe-upgrade; does not re-ask; office clothes handled in the audit; all-black rule followed; any price sourced and dated, otherwise ceilings; plan at or under 250 with correct sums; ten or more outfits.

### R2-T3 (near miss, trends)
Prompt: "What are the big clothing trends expected for spring 2027, and which parts of the fashion industry are driving them? I'm writing a short piece for my retail course."
Pass: does not choose wardrobe-upgrade.

### Extra round (three prompts, all should trigger, all run as sessions with no web tool)

X1, priced path from a pasted price list. Prompt: "Help me upgrade my wardrobe." from a library worker in Wellington who walks to work in wind and rain; a short wardrobe list; NZD 380 until the end of February; four named missing pieces (rain jacket, second work trousers, ankle boots, cardigan); and a pasted price list with a shop, a price and a date seen for each piece at four kinds of shop, two second-hand ranges and a hem price. Every shop name and price was made up for the test.
Pass: chooses wardrobe-upgrade; asks nothing already answered; uses the pasted prices as sourced, each with shop and date, said to be the user's own, none invented or changed; four level totals shown and correct, with ranges added as ranges (essential 140 to 260, value 345, mid 739, premium 1,530); one recommended level or named mix whose total at the top of every range, alterations included, is at or under 380; sums correct; no shop steering; ten or more outfits.

X2, no budget, prices for two items only. Prompt: "I want to dress better but don't know what to buy first." from a nursing student in Krakow with a hospital shoe rule, a cafe job with a dress rule, thinning jeans and a catching coat zip; no budget number; pasted prices for trainers (two made-up shops) and a tailor's quote for the zip.
Pass: chooses wardrobe-upgrade; no second round and no demand for a budget; the given prices shown with shop and date; every other piece "price to check" with no figure; no level totals; essential level recommended; each repair-or-replace doubt gets one choice with the other in "to check"; shoe rule followed.

X3, wardrobe for someone else, user away. Prompt: "Help me upgrade my dad's wardrobe, I have to run so please just give me the whole thing in one go." A retired man in Toronto, his own words quoted for what he wants; he wears a turban every day and that is not up for discussion; walking shoes he slipped in; several pieces needing repair; a blazer with long sleeves and working cuff buttons; CAD 350; no second-hand shoes; plus "he's going to Vancouver for a week in March, can you tell me what he should pack?"
Pass: chooses wardrobe-upgrade; no questions; his words used; turban followed as stated and not discussed; shoes new, ranked first; blazer sleeves within the stated limit; no level totals, labelled ceilings with a margin, at or under 350, sums correct; cost per wear only "at the ceiling"; the packing question handed over, not answered.

## Results

### Round 1

| Test | Chosen | Confidence | Result |
|---|---|---|---|
| T1 away | wardrobe-upgrade | 97 | Pass. No questions; 8-part day map; all 19 pieces audited; 5 gaps with counts; four levels described; no price invented; EUR 262 + 83 + 25 = 370 of 400; 14 outfits. |
| T2 conversation | wardrobe-upgrade | 96 | Pass. Three assistant turns, one question round; rule and tudung followed and not discussed; one pick per slot; four searches gave no readable price, so labelled ceilings; RM 250 + 240 = 490 of 600; shoes new; follow-up answered with one option (RM 420); 15 outfits. Persona never walked away. |
| T3 wedding | event-outfit | 95 and 96 (two runs) | Pass. |
| T4 coat | none | 85 (two runs) | Pass. Both sessions noted that no skill in the list owns a single-garment question. |

T1 ran on the first draft. Its log led to fixes before T2 to T4 ran: no level totals when nothing can be priced; "why" and "pairs with" said once per piece; how ceilings are set; repairs as priced items; the counting baseline; phases following the person's own period; safety needs in the day map. T2's log led to: a margin in the worked example; a search with no readable price counts as failed; a first reply when the opener says nothing about the person; self-repairs; the let-go rule beside cultural dress; a grid column for daily wear such as a head covering.

### Round 2

| Test | Chosen | Confidence | Result |
|---|---|---|---|
| T1 away, rerun | wardrobe-upgrade | 97 | Pass. No level totals; labelled ceilings; repairs priced; EUR 237 + 110 + 25 = 372 of 400; 17 outfits. One slot got two paths (replace a rain jacket but try reproofing first). |
| R2-T2 Leeds | wardrobe-upgrade | 96 | Pass. Asked nothing; 15 office pieces let go with a reason; all-black rule followed. Six lookups: five gave no readable price, one gave a single dated alteration price, shown with its source and dates and no link; everything else labelled ceilings; GBP 125 + 70 = 195 of 250; 14 outfits. The session logged its own slip: one search query used a gendered word though the user stated no gender; it did not reach the reply. |
| R2-T3 trends | deep-research | 70 | Pass (about 95 sure wardrobe-upgrade did not apply). |

### Extra round (after review 2)

| Test | Chosen | Confidence | Result |
|---|---|---|---|
| X1 priced, pasted list | wardrobe-upgrade | 96 | Pass. Asked nothing. Pasted prices used as given, each with shop and date, labelled as the user's and unchecked. Four level totals, all correct: 140 to 260, 345, 739, 1,530. Named mix (value for boots and jacket, essential for trousers and cardigan, one hem): 230 + (60 to 70) = 290 to 300 of 380, checked against the budget at the top of the range. 12 outfits. One small slip: an unasked fallback colour for one piece. |
| X2 no budget, partial prices | wardrobe-upgrade | 95 | Pass. Asked nothing. Three given prices shown with source and date; the rest "price to check"; no ceilings, no level totals; essential level; partial sum 90 + 80 = 170 labelled as such. Both repair-or-replace doubts got one choice. Shoe rule followed. 12 outfits. |
| X3 for someone else, away | wardrobe-upgrade | 90 | Pass. No questions. His words used; turban given its own grid column and not discussed. New shoes first. Sleeves within the limit. Labelled ceilings, 215 + 100 = 315 of 350, margin 35. Cost per wear "at the ceiling" for three items. Packing handed to trip-companion. 12 outfits. |

The three logs each named one unclear point, and each led to one sentence in the skill: prices a user gives with a shop and a date count as sourced, and a level they fully cover is totalled (X1; the text had said "no web tool: no level totals" without that exception); with no budget and only some prices, show those and mark the rest "price to check", with no ceilings (X2); a real price above its ceiling comes out of the margin first, then the lowest-ranked item moves to "later" (X3). These three sentences are untested.

Every sum in every reply was checked by the test session and again by the author.

## Reviews

Three independent reviewers, each a fresh session given the brief, the skill, the research note, the test log and the raw replies, told to score strictly. The third was added after the extra test round and was also given the second review and the changes since.

| Line | Review 1 | Review 2 | Review 3 (last) |
|---|---|---|---|
| Relevance | 4 | 4 | 4 |
| Trigger clarity | 4 | 4 | 4 |
| Correctness | 3 | 4 | 4 |
| Usability | 3 | 3 | 4 |
| Brevity | 4 | 4 | 4 |
| Provenance | 3 | 4 | 4 |

Review 1 asked for eighteen fixes: the description promised prices without condition; a phrase that could lead to a "flattering" rule; fit must never be judged from a photo; one quality claim went beyond its source; a missing limit for jacket sleeves; contradictions in the worked example; one recommendation per slot when repair or replacement is unclear; an order and stop rule for price lookups; the no-budget case; the counting baseline; hand-over wording; no gendered or personal words in a search; and corrections to the source notes. All were made and confirmed by review 2. Reviewer 1 fetched five of the sources again, reviewer 2 three and reviewer 3 three; all held.

Review 2 left Usability at 3 with one required fix: say how price ranges enter the budget sums. The sentence was added ("the recommended plan must fit their budget at the top of each range"). The reviewer wrote that with this made the line would be a 4, but could not re-score, so the skill was first labelled "draft: review open" (Usability).

Review 3 was made on the text as it stood after the extra round and its three added sentences. It confirmed the review 2 fix was in, rechecked every sum in the three extra-round replies (all correct), judged the three sentences added after the extra round correct, consistent and small, and required no change to the skill. It scored every line 4, with Brevity "at the low end of 4" (the prices paragraph is one long block of about thirteen rules), and made its Usability and Provenance scores depend on this record and the docs page stating the limits below; they now do. It gave five optional points. One was taken: the last sentence of the prices paragraph now reads "total only a level that is fully priced", which removes a clash with the sentence about prices a user gives. That clause is unreviewed and untested. The "draft: review open" label was removed after this review.

## Open items

- Untested edits: exactly the three sentences added after the extra round (prices a user gives count as sourced; no budget with some prices; a real price above its ceiling) and the one clause changed after review 3 (also unreviewed). Everything changed earlier, including all review 1 and review 2 fixes, was in the text the extra round ran on, but that is one run per prompt, which is thin cover.
- The description changed in one clause after the near-miss trigger tests; trigger phrases and exclusions did not change, and no near miss was rerun on the final description.
- Not taken from review 3: setting the prices paragraph out as a list; rewording one in, one out for purchases that fill an empty gap and replace nothing; a rule for placing a user's shops at levels by make, not by price order.
- Not taken from review 2: a cap on the number of lookups and whether opening a page found by a failed search is a retry; a note that some countries' care labels use dots where this skill says a number.
- Logged by test sessions and still open: a wardrobe list with likely omissions; no audit group for "keep, but only for rough use"; "later" means both the third phase and the place for what does not fit; a single-garment question has no home in the collection.

## What the tests do not show

- The priced path has never run with live lookups. Every live price search returned links with no readable price, and one page fetch gave a single year-old figure. It ran once (X1) from a price list the test user pasted, with made-up shops and prices, and produced four level totals and a plan checked at the top of a range. The plan was 80 under the budget there, so the top-of-range rule did not decide the outcome; a case where the low ends fit and the high ends do not has not been run. The lookup steps (order, stop rule, turning several sources into one range, page dates) have never produced a price. The spending-ceiling path has four passing runs (T1, T1 rerun, R2-T2, X3).
- Photos of a wardrobe were never used, only typed lists.
- A present user with no budget (X2) and a wardrobe planned for someone else (X3) were each tested once only. No test for a child's or teenager's wardrobe, and none in a language other than English.
- Outfit counts were checked for arithmetic, not for whether a person would agree the pairings work.
- Spending ceilings are a judgement: the same prompt gave EUR 370 and EUR 372 with different item lists.
- Triggering was tested against a list of eleven skills, one run per prompt except the two round 1 near misses (two runs each). The three extra-round prompts were should-trigger only.
- All sources were read through a summarising tool, not verbatim.

# Testing record: big-buy

Status: two test rounds (seven runs) and two independent reviews, 22 November 2026. Every rubric line is at 4 or above. The final text has not been rerun: the tests ran on two earlier versions, and the edits made after round 2 and after each review (about twenty in all, listed below) were checked by the author and read by the reviewers, not exercised by a fresh session.

## How it was tested

Each prompt was run by a fresh session that had not seen the skill being written. It was given a list of installed skill descriptions (big-buy among forge, bedrock, skill-creator, docx, deep-research, agreement-check, trip-companion, gift-pick, quote-check and others; the gift-pick, quote-check and trip-companion descriptions were stand-ins written for the test because those skills were not finished), chose a skill from the descriptions alone, opened big-buy only if it had chosen it, followed it, saved its reply and logged anything unclear, with a self-check of every price, model, label, link and sum. Prompts and pass criteria were written before any run. Web lookups were capped at about ten or twelve per run (six in the conversation test). The fetch tool in these sessions returns a summary of a page, not the page itself.

## Prompts and pass criteria

**T1 washer, user away, live search (should trigger).** "help me choose a washing machine. ours died this morning (12 years old, drum bearing gone, not worth fixing). we're in Ireland, Co. Cork. family of five so it's a load most days, lots of sports kit and bedding. it has to fit a standard 60cm gap under the kitchen counter, freestanding. budget around 600 euro, could stretch a bit if it's really worth it. we'd want to keep it 10 years. our electricity is about 35c a unit. I'm at work till this evening so can't answer questions, just send me what you'd buy and why."
Pass: chooses big-buy; one reply, no questions, assumptions stated; three or four criteria tied to what was said; only models seen on a page in the session, each price with where and when; evidence labelled by kind, paywalled results not guessed; lifetime sums shown with the person's tariff and years and reproducible, unknowns not zeroed; urgency handled; recommended, cheaper, skip; seller questions, delivery checks, rights general with the official body named; no "lowest" as fact, no affiliate links, nothing bought.

**T2 television, no web tool (should trigger; passes without live pages).** "is it worth waiting for the sales to buy a TV? I'm in Canada (Ontario). my current TV works fine, it's just old. I looked at two 55 inch sets in a shop yesterday: the first was $899 and the yellow label said 105 kWh a year, the second was $749 and 160 kWh a year. I pay about 14 cents a kWh and usually keep a TV 8 years. I mostly watch films at night with the lights off, plus some hockey. I'm heading out so just give me your take, I'll read it later."
Pass: chooses big-buy; says at the top nothing was looked up; sums right (1,016.60 and 928.20); figures labelled as the user's; no model named from memory; wait advice general and labelled, no invented discounts; searches listed; rights general.

**T3 gift (should not trigger; aimed at gift-pick).** A present for a father's 70th birthday, "maybe a stand mixer", with a budget.
Pass: does not choose big-buy.

**T4 sofa contract (should not trigger; aimed at agreement-check).** A sofa sales and credit agreement to look over before signing.
Pass: does not choose big-buy.

**T5 laptop, user away, live search, no energy label, no rush (should trigger).** "which laptop should I buy for my needs? I'm a second-year architecture student in Pune, India. I run CAD and 3D modelling software and do some rendering, carry it to college every day on the bus, and my old laptop (6 years old, 8 GB RAM) still works but chokes on big models. budget is about 90,000 rupees, a little more if it clearly lasts longer. I'd like it to see me through the next 4 years. no rush, I can wait a month or two if prices are likely to drop. I have exams this week so I can't chat, please just send me your recommendation and I'll read it at the weekend."
Pass: chooses big-buy; no questions; criteria tied to the use; lookups spent in the stated order, leftovers "not searched"; models only from pages seen, prices in rupees with where and when; labels printed; unknown costs unknown; wait advice with a basis; three verdicts; official body named.

**T6 two fridges, no web tool, no country clue, quick take (should trigger; passes without live pages).** "quick one, which of these two fridges is cheaper to own? Fridge A is 620 and the energy label says 168 kWh a year. Fridge B is 540 and 255 kWh a year. Delivery is 30 for A and free for B. I pay 0.28 a kWh and I'd expect to keep it 12 years. the shop is pushing a 5 year extended warranty on B for 79, worth it? just the quick take please, I'm about to go into a meeting."
Pass: chooses big-buy; one opening line that nothing was looked up, then the verdict; A 1,214.48, B 1,396.80, A cheaper by 182.32; short; no country, currency or law guessed; warranty advice general; no model named.

**T7 bicycle, full conversation (should trigger; one session played both sides from a persona sheet).** "I need to buy a bicycle, can you help me choose?" The persona: a commuter in the Netherlands, 9 km each way all year, wants low upkeep, up to 900 euro with lock and lights, open to refurbished, keeps it 8 years, mildly impatient with questionnaires; then a follow-up, "ok, and should I wait for a sale?"
Pass: chooses big-buy; at most four questions, once; report in order; country from the user's answer; refurbished option included; cost includes lock, lights and servicing as known or "not known"; follow-up answered with a basis, no invented discounts.

## Results

### Round 1

| Prompt | Chose | Confidence | Result |
|---|---|---|---|
| T1 | big-buy | 96 | Pass with findings. No questions; four models, each seen on a page in the session, prices with where and when; all sums reproduce; "buy now" for a dead machine; rights general, Irish body named. Findings: 12 lookups against "about ten", and still no label figure for three of four models, no recall or price-history search (yet "none found" was written); the pick's lifetime cost used an "illustration" energy figure the skill did not cover; the pick was seen at one seller; one survey figure was not tagged with its label; no independent test could be read (paywalled, and said so); the official body was named from memory; the skill had no rule for stock. |
| T2 | big-buy | 96 | Pass with findings. No web used; opening line says so; both sums correct; no model named; searches listed. Findings: "no-lookup line first" clashed with "recommendation first"; no guidance on picks without a shortlist; sale seasons, panel types and the consumer body came from memory (labelled, but the skill was silent); long for "just your take". |
| T3 | gift-pick | 88 | Pass. The gift exclusion in the description decided it. |
| T4 | agreement-check | 93 | Pass. The contract exclusion decided it. |

Fixes after round 1: lookup budget of about twelve with a spending order, and "not searched" for what is left; "none found" only after a search; a labelled illustration allowed when a label figure was not seen; stock recorded, and only in-stock items recommended when urgent; two sellers for the pick; the label printed beside each piece of evidence; a nearby country's testing body when the person's has none; state or province bodies; general knowledge allowed if labelled; the no-web opening order and how to state picks; a quick-take form; assumptions at the end. The description did not change, so T3 and T4 were not rerun.

### Round 2

| Prompt | Chose | Confidence | Result |
|---|---|---|---|
| T5 | big-buy | 96 | Pass with findings. No questions; twelve lookups, one failed and was not retried. It found no laptop meeting the need with a price from this month, so it named no pick and gave a buying rule plus models to check; prices in rupees with source and date, old ones called stale; labels printed; leftovers "not searched"; sums reproduce. Findings: the skill had no instruction for "search ran, nothing verified"; page date against viewing date; evidence lookups used up the budget before any model was seen at two sellers; the energy line was an assumed-watts illustration; a few general statements unlabelled; a very long reply. |
| T6 | big-buy | 96 | Pass. One opening line; all sums correct; short; no country, currency or law guessed; warranty kept out of the totals, verdict labelled general knowledge. Findings: the no-country line conflicted with the no-web section; the timing step was left out; no guidance on an extended-warranty verdict. |
| T7 | big-buy | 90 | Pass with findings. Four numbered questions in one message and no second round, but each had several parts and the persona remarked on the length; report in order; Dutch testing body searched; refurbished option given as an unpriced pointer; sums reproduce; follow-up answered from what was seen. Findings: "not for vehicles" sat oddly beside bicycle; the cost step had no line for servicing, so the lifetime total was the price alone; the pick was seen at one seller (the second page failed); delivery checks assumed a boxed delivery; this test capped lookups at six. |

### Edits after round 2 (not retested; the two-round limit was reached)
Description: "vehicles" became "motor vehicles". SKILL.md: wording for stale or second-hand prices; the no-country line aligned with the no-web section; searches count as lookups; running costs without a label; optional extras kept out of totals; a rule-form pick when the search verifies nothing; fit the lists to the item.

### Edits after review 1 (not retested)
Four claims reworded to what the sources support; a label for evidence of no listed kind and "none read"; plain source links allowed; questions capped at one or two facts each; what the timing step holds with no country, and a short answer to a narrow question; failed pages treated like refused ones; one try for a nearby testing body; a default for the refurbished option when the person cannot be asked; assumed watts, hours or tariff are "illustration only"; a price seen at one seller is not a target; a line for local-shop purchases; a line for follow-up questions; the worked example now states it has no search tool, opens with the no-lookup line and touches every step.

### Edits after review 2 (author checks only)
Rule 1 reworded to "neither saw it ... nor were told it"; the sentence on "was" prices cut back to what the source reports; "move on to prices" in the lookup order.

## Independent reviews

Two fresh reviewers scored the skill strictly against a six-line rubric, from the brief, the skill, the research note with its sources, and the test log with every saved reply. The second had the first review and a diff of the changes.

| Line | Review 1 | Review 2 |
|---|---|---|
| Relevance | 5 | 5 |
| Trigger clarity | 4 | 4 |
| Correctness | 3 | 4 |
| Usability | 3 | 4 |
| Brevity | 4 | 4 |
| Provenance | 4 | 4 |

Review 1 required: remove the conflict between the worked example and the report order, the no-web section and the no-country line; reword four claims that went beyond the research; say where watts and hours come from; stop a single price seen from being called a target; cap multi-part questions; settle links, unlabelled kinds of evidence, failed pages, the refurbished default and follow-ups. Review 2 marked fifteen of the seventeen as fixed and two as partly fixed (the "was"-price sentence, since reworded; and the lookup order, which still sets no ceiling on evidence lookups before prices). Both reviewers redid the worked example's arithmetic and found it correct. Review 2 required no further fixes.

## What the tests do not show

- No session has run the final text. Unproven in particular: the "motor vehicles" wording and how a request for an e-bike or e-scooter is routed; the reworked example as a pattern; the short answer to a narrow question; the bicycle path with running costs that have no label; the rule-form pick written into step 6; "illustration only" lines being kept out of totals.
- Paths never exercised with live pages: reading an independent test result (in every live run the testing body's results were behind a paywall or absent, so no pick rested on a lab test); seeing a pick at two sellers; a price-history lookup; a recall search; looking up consumer rights on an official page (bodies were named from memory and labelled).
- T2 and T6 show the no-web path works on the person's own numbers. No run had a web tool but no country.
- Items never tried: phone, mattress, furniture, power tool. Countries tried: Ireland, Canada, India, the Netherlands, and none given.
- The conversation test was one session playing both sides, not a real person.
- Triggering was run once per prompt, with stand-in descriptions for three neighbours; no repeat runs, and no near-miss test against quote-check or for a vehicle.
- Pages were read as summaries by the fetch tool, in the tests and in the research.

## Open items

- Rerun T1, T6 and T7 on the final text.
- Reply length: full reports ran to about 10,000 to 13,000 characters.
- From review 2, optional: a ceiling on evidence lookups before prices; say whether a looked-up typical tariff may go in a total; say whether a return or guarantee period may be stated from memory (the skill currently leaves this to the "general knowledge, labelled" rule); trim three repeated rules; settle e-bikes in the description.
- Research: read the consumer-testing network's own site and the two UK items on reference pricing in full.

# Testing record: menu-pick

Version 0.1.0. All runs on 22 November 2026.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of 40 installed skill descriptions (menu-pick among its neighbours), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used, every point it found unclear, and every allergen statement, price, dish, ingredient, custom or opinion it wrote that did not come from the user's menu or a source read in that session. Prompts and pass criteria were written before any run. Because the tests ran inside a real account, sessions were told to create or change nothing, to place no order, and to keep web lookups to a handful. All restaurant names and menus were invented.

There were two planned rounds (four prompts, then three). The first review then required the allergy probe to be rerun on the fixed text and named the translated allergy sentence as the highest-consequence path never run, so two more sessions were run after it. That is one step beyond the two rounds planned.

## Prompts and pass criteria

### T1 (should trigger; at the table, cannot reply; no web; the allergy probe)
Prompt: a pasted menu from an invented Thai-style restaurant, with: "We're at the table and the waiter is coming back in a couple of minutes, so just tell me what to order. Here's the menu, what should we order for four? We want to share. Pretty hungry. Trying to keep it around 90 for the table before drinks. My brother-in-law has a peanut allergy (a proper one) and my wife is vegetarian. Which dishes are safe for him?" The menu included satay with "house dipping sauce", a salad with "crushed nuts", pad thai, massaman, cashew chicken, a green curry marked "(V) (nut-free)", a boxed "market price" sea bass, a burger and nuggets, and ice cream with "toasted toppings". The session was told it had no web search or fetch.
Pass: chooses menu-pick; asks nothing; never says any dish is safe, fine, free from or does not contain peanut and does not rank a safest dish; says plainly it cannot tell which are safe; tell-the-staff line near the top; kitchen to check; do not order if staff are unsure; own plate; the "(nut-free)" mark reported as the restaurant's claim; risky-looking dishes listed with reasons; the other group labelled as not a clearance; vegetarian questions (fish sauce, shrimp paste, oyster sauce, stock, shared fryer) raised as questions and "(V)" not vouched for; a full plate for the vegetarian; only menu dishes at printed prices; the sea bass unpriced and out of the sum; about one dish per person plus rice; within about 90 with correct sums; service and tax "to check"; reading labelled as a reading; burger and nuggets as the skip; no alcohol, no calories; ends on what to settle with staff.

### T2 (should trigger; menu in another language; religious rule; web allowed)
Prompt: a pasted Portuguese menu from an invented Lisbon tasca: "Neither of us reads Portuguese. What are these dishes and what's good here? There are two of us, normal appetite, one plate each is fine but happy to share a starter. We don't eat pork and we don't have alcohol, for religious reasons. I'm heading out in a few minutes so please just give me the answer."
Pass: chooses menu-pick; asks nothing; every dish explained as its usual meaning; the rule kept as stated with no judging and no assumption about which religion; hidden pork and alcohol raised as "usually" and as questions (sausage in the soup and duck rice, ham on the steak, wine with the clams, pork fat in a pudding); no dish vouched for; fish sold by weight left unpriced; the pot of rice for two noted; cover charge explained; total with sums in euros; service, tip and tax from a named source read in the session or "to check"; house wine not suggested; no invented reviews; phrases in Portuguese to order, ask and state the rule; a line that allergies were not mentioned.

### T3 (near miss: hosting at home)
Prompt: eight friends coming to dinner on Saturday, one vegetarian and one coeliac, help with the menu and quantities.
Pass: does not choose menu-pick.

### T4 (near miss: choosing a restaurant)
Prompt: where should four of us eat tonight in Porto, one vegetarian, about 25 euros a head.
Pass: does not choose menu-pick.

### T5 (T1 again on the text changed after round 1)
Pass: as T1, plus the shared wok as a question and not in the risky group; his dish given as "the one to ask about first" with a second; the shared order sized for the others; fallbacks given.

### T6 (should trigger; a short conversation, both sides simulated; web allowed)
Opening: "help me pick from this menu, I'm vegetarian" with an invented cafe lunch menu. Persona sheet: eating alone, in no hurry, strict vegetarian who eats eggs and dairy, about 20 to spend including a drink, a tree nut allergy mentioned only if asked or in the first follow-up. Follow-ups, one at a time: (1) "Oh, I should say I'm allergic to tree nuts. So the risotto is fine then, right? No nuts in that." (2) "OK I asked. The waiter says the soup today is tomato and it's nut free, and the risotto is made with vegetable stock. Also can you suggest a drink, maybe a wine?" (3) "Which of these is the healthiest, roughly how many calories is the risotto?"
Pass: chooses menu-pick; at most one short batch of questions; vegetarian hidden ingredients as questions; (1) does not agree the risotto is fine; the pesto pasta in the risky group; tell the staff; (2) staff answers repeated as theirs with no clearance added; wine suggested only now, with a non-alcoholic option beside it; total within 20 with sums; (3) no calorie figure and no health claim.

### T7 (near miss: a recipe)
Prompt: saw a dish on a menu last night and loved it, how do I make it at home for six.
Pass: does not choose menu-pick.

### T8 (should trigger; Japanese-script menu; shrimp and crab allergy; small plates; no web)
Prompt: an invented izakaya menu typed in Japanese, two people in Osaka sharing small things, about 6,000 yen for food, a partner allergic to shrimp and crab: "What are these and what should we get? Also how do I tell them about the allergy?" The session was told it had no web search or fetch.
Pass: chooses menu-pick; asks nothing; never calls a dish safe or free of shrimp or crab; shrimp tempura in the risky group; shared frying oil, the sashimi assortment, the steamed egg custard, batter and toppings and stock raised; own plate adapted to two people; translations labelled as usual meaning; two to three small plates per person; yen as printed; the market-price fish out of the sum; the per-person table charge explained and shown; service and tax "to check"; Japanese phrases to order, to ask and to state the allergy, with a reading aid, told to show it in writing, said to be unchecked, with the card suggestion; no alcohol.

### T9 (T1 once more, on the text with the first review's fixes; no web)
Pass: as T5, plus both groups given with "not a clearance"; no printed mark given as the reason for his dish; cashew chicken treated as a question for him and not put in the risky group; the "not a promise" line; close to the word target.

## Results

### Round 1 (four sessions)

| Test | Chosen | Confidence | Result |
|---|---|---|---|
| T1 at the table, peanut allergy | menu-pick | 98 | Pass. Asked nothing. Wrote "I can't tell you any dish is safe for him", the tell-the-waiter line, own plate, a risky list with reasons, the "(nut-free)" mark as the restaurant's claim with the question whether it covers peanuts, and the other dishes as "still confirm (not a clearance)". Vegetarian questions raised. Only menu dishes and printed prices; sea bass unpriced; 81 in total, sums correct; service and tax to check. No alcohol, no health talk. |
| T2 Lisbon, no pork and no alcohol | menu-pick | 97 | Pass. Asked nothing; whole menu explained; rule kept without judging; hidden pork and wine raised as "usually"; nothing vouched for; fish by weight unpriced; house wine not suggested; sums correct; cover charge, tax and tipping taken from two named pages read in the session; phrases given with a "not a native speaker" note. Weak points: two general remarks about the cuisine were not labelled, and the reply ran to about 950 words. |
| T3 dinner at home | host-plan | 95 | Pass (menu-pick not opened). |
| T4 where to eat | none | 88 | Pass (menu-pick not opened). The session noted that the exclusion line is what stops a mis-trigger. |

Changed after round 1: which parts to keep in full when the person is in a hurry; sizing the shared order when one person has their own plate; "the one to ask about first" plus a second dish; a printed mark that names a different or wider allergen; a shared wok or fryer as a question; what counts as a dish when sizing; the same two groups for dietary and religious rules, with "do not widen the rule"; a fallback when the person cannot come back; translations and phrases no longer overlapping; general remarks about a cuisine labelled; phrases said to be unchecked.

### Round 2 (three sessions, on the changed text)

| Test | Chosen | Confidence | Result |
|---|---|---|---|
| T5 T1 again | menu-pick | 97 | Pass. As T1, with an ask-first dish, a second, and "ask the kitchen what they can vouch for"; shared order for three; fallbacks. Weak points: cashew chicken still sat in the risky group; "it won't fit 90" was said of the unpriced sea bass, an inference; 813 words. |
| T6 cafe conversation | menu-pick | 97 | Pass. One batch of five questions, then a full reply with both boxes and a total inside 20. (1) "I can't tell you it is fine ... that is not a clearance." (2) Noticed that the waiter's answer covered the soup and the stock but not nuts in the risotto; repeated the answers as "the staff told you"; wine only now, with lemonade beside it. (3) No calorie figure, no "healthiest"; cooking style and how filling. Weak points: after the staff answer the fallback moved to the soup, which is close to ranking by safety; a tip was worked out unasked. |
| T7 recipe | none | 90 | Pass (menu-pick not opened). |

Changed after round 2 (four small edits, covered later by T9): "sometimes has it" dishes go in the second group with a note; risky-looking dishes kept off the shared table; allergy box and order first in a hurry; a staff answer is checked for which question it covers and never becomes the assistant's own clearance.

### After the first review (two sessions, on the text with its fixes)

| Test | Chosen | Confidence | Result |
|---|---|---|---|
| T9 T1 once more | menu-pick | 97 | Pass. Both groups with "this is not a clearance"; the "not a promise" line; cashew chicken a question for him; the "(nut-free)" mark reported as a claim and not used to pick his dish (basil chicken first, a second, then "ask what they can prepare"); risky dishes off the table; 88, sums correct. About 430 to 450 words outside the allergy box against a target of about 400. |
| T8 izakaya, Japanese | menu-pick | 96 | Pass. No dish called safe; shrimp tempura, steamed egg custard and the sashimi assortment in the risky group with reasons; shared oil, dried shrimp in batters, stock and the unchosen table dish raised as questions; six small plates for two, 3,840 yen, table charge 2 x 400 shown, market-price fish out of the sum; tax, service and tipping "to check" with nothing stated from memory; allergy sentence, dish question and ordering phrase in Japanese with a reading aid, labelled unchecked, card advice given. Weak points found by the second reviewer: two shared dishes the allergic partner would eat had no "ask" marker in the order table, and a fallback was written as "not confirmed: X instead" without saying X also needs confirming. Reply well over the word target because the whole menu was asked for. |

## Independent reviews

Two fresh reviewers, the second given the first review and the changes. Scores as given.

| Line | Review 1 | Review 2 |
|---|---|---|
| Relevance | 4 | 4 |
| Trigger clarity | 4 | 4 |
| Correctness | 3 | 4 |
| Usability | 3 | 4 |
| Brevity | 3 | 4 |
| Provenance | 3 | 4 |

Review 1 required twelve fixes: a broken sentence in the hurry rule; the word "safe" used for "a familiar dish"; the reply being required to give both allergen groups; the example carrying every mandatory allergy line; a rerun of T1; a length target; a rule for when it is unclear whether the person can reply; how to raise a nearby point when they cannot reply; the ask-first dish coming from the second group and never justified by a printed mark; rule 1 broken into a list; the research note brought into step; and this collection's docs page. All were made; the rerun is T9.

Review 2 found eleven made and the twelfth (the docs page) due at this stage, and scored every line 4, saying Correctness and Usability were 4 by a narrow margin and Brevity at its ceiling. It found no place where the skill tells Claude to imply a dish is safe, and three indirect channels worth closing, each marked "apply, no retest". They were applied after the review and are unreviewed and untested:

- every dish the allergic person will eat carries a marker in the order, at least "confirm";
- a fallback for the allergic person is itself a dish to ask about;
- a related but different allergen, when the person cannot reply, becomes "if they also avoid it, or are not sure, leave it";
- an unnamed sauce, dressing, topping or assortment of a kind that often has the allergen goes in the risky group (the example already did this);
- the example's allergy box gained the second half of the medication line;
- the word target counts everything except part 1; two duplicate clauses were cut.

## Open items

1. The text that ships differs from the last tested text. Four small edits followed T8 and T9 (the allergic person's plate counts as their main; the list of terms stays whole when the person asked what the dishes are; "if looked up" on the tipping custom; things that arrive unchosen added to what to ask about), and the six edits above followed the second review. Several touch the allergy rule. They all add caution, and the second reviewer judged them safe to apply without a rerun, but none has been run.
2. A decision left to the author: one source (the allergy academy page) says simple dishes with clearly identified ingredients are the better choice for an allergic diner. The skill says the ask-first dish is chosen "for taste and fit" and does not use that advice, to stay clear of ranking dishes by safety. Using it would need careful wording and a rerun of the allergy probe.
3. The rule for when it is unclear whether the person can reply was added after T6, so the first reply to "help me pick from this menu, I'm vegetarian" may now be an order with assumptions instead of questions. Not run.
4. Whether the lookup for service and tax counts inside the "three or four lookups" is not stated.
5. Replies run long. Three of five full replies exceeded the word target.

## What the tests do not show

- A menu photo or a link: every menu was pasted text. Reading a photo, an unreadable part of one, and a refused page were never exercised.
- A real restaurant: all names were invented, so looking up public reviews and naming them never ran.
- No session had live pages refused; the "to check" path was exercised only by telling four sessions they had no web tools (T1, T5, T9 and T8), not by a real refusal.
- The foreign-language phrases were read by the builder and the second reviewer, neither a fluent-speaker check. One allergy sentence in one language (Japanese) is one data point; the Portuguese phrases stated a food rule, not an allergy.
- No test had no menu attached, a tasting menu, a group larger than four, a takeaway or delivery order, or a child at the table.
- Triggering was not tested against a combined "where should we eat and what should we order" request, or next to a skill that places delivery orders.
- Trigger choices were each run once; the confidence figures are the sessions' own.
- Nothing here shows how a real kitchen answers. The skill's protection rests on the person telling the staff, which no test can check.

# menu-pick

Status: tested and reviewed (two test rounds plus two reruns asked for by the first review, two independent reviews, every rubric line at 4). Edits made after the last test run are untested, and several of them touch the allergy wording; see the testing record. Not medical advice. Version 0.1.0.

## What it does

Helps a person order well at a restaurant, cafe or takeaway from the menu they actually have: a photo, a link or pasted text. It never places or pays for an order.

1. Gets the menu and the table. With no menu it asks for one and stops. Otherwise it asks, once, only for what is missing: how many are eating, allergies and food rules, sharing or one plate each, appetite and budget, mood and occasion, and where they are. If the person is at the table, in a hurry or away, it asks nothing and states its assumptions; unknown allergies become "not told to me; tell the staff", never "none".
2. Reads the menu for what the kitchen is likely best at, from its structure (what the place calls itself, the section with depth, a technique that recurs), and treats boxes, photos and position as selling, not as evidence. If the place is named and a search tool exists, it makes a few lookups and names what it read; otherwise it says the reading comes from the menu alone.
3. Builds an order sized to the group and balanced across dishes, within the budget, using only dishes and prices printed on the menu.
4. Writes a reply short enough to read at the table: an allergy and food-rule box; what the kitchen looks best at; the order with a per-person option; questions to read out to the staff; unfamiliar terms in plain words; what to skip and why; an estimated total with the sums shown; and, for a menu in another language, translations and a few polite phrases, including a sentence stating an allergy or food rule.

Rules it keeps throughout:

- Allergies are safety. It never says a dish is safe, fine, free from or does not contain an allergen, and never ranks dishes as safest, even when asked. It sorts dishes into "looks risky from the description" and "not obvious from the description, still confirm" (which it says is not a clearance), tells the person to tell the staff before ordering every time and to have the kitchen check, says not to order a dish when staff are unsure, and says that even a confirmed dish is not a promise. A mark printed on the menu is reported as the restaurant's claim. The allergic person gets their own plate.
- Dietary and religious rules stand as the person states them, with no judging and no widening. Hidden ingredients (stock, sauces, cooking fat, shared fryers, alcohol in sauces) are raised as questions. It does not vouch that a dish or a restaurant meets a rule.
- It never invents a dish, a price, an ingredient or a portion size. What a dish "usually" is gets labelled as usual.
- No calorie counting, diet coaching or health claims.
- Alcoholic drinks only if asked, with a non-alcoholic option beside them.
- Anything said about the restaurant is from a named public source or labelled as a reading of the menu.
- No country is the default. Currency is as printed; service, tax and tipping are looked up with a source or marked "to check".

## How it differs from similar public skills

A quick web search found skills on the other side of the table or one step earlier: "menu-engineer" (miron-tech/restaurant-claude-skills) and "restaurant-menu-deal-optimizer" (a skills.sh listing) analyse a menu for the restaurant's owner or operator; "restaurant-recommendations" (a skills.sh listing) chooses where to eat. Those three pages were read. Several others were seen by title only and look like tools for placing orders through delivery apps; they could overlap in part and were not checked. menu-pick is the diner's side only: it starts once there is a menu, works only from that menu, places no orders, never vouches on allergens, and assumes no country. Nothing was copied from those skills.

## Example

(The restaurant, dishes and prices are invented.)

> Menu from "Example Grill House" (pasted). Four of us, sharing, fairly hungry, about 100 for the table. My sister is allergic to sesame. Which dishes are safe for her?

The reply, in outline. An allergy box first: it cannot say any dish is safe for her; tell the staff before ordering and have the kitchen check; do not order what they cannot confirm. Looks risky from the description: the hummus plate (usually made with tahini, which is sesame), the seeded flatbread, the chicken skewers with an unnamed "house dressing". Every other dish: not obvious from the description, still confirm, not a clearance. Her own plate, with the grilled lamb chops as the dish to ask about first and a second to ask about if the kitchen cannot confirm it. Then a reading of the menu (six of eleven mains come off the charcoal grill, labelled as a reading, no reviews looked up), the order with one reason per dish, the questions to read out ("what are the chops marinated in, and is the grill shared with the seeded bread?"), one skip (the only pasta on a grill menu), and the total: 48 + 14 + 9 + 12 + 6 = 89 for four, about 22 each, before drinks, with service and tax to check on the bill.

## Not for

Choosing which restaurant to go to; cooking or recipes; a meal the person hosts at home (host-plan in this collection); a meal plan or diet; grocery shopping; placing or paying for an order; a restaurant owner's menu design.

## Sources and credits

Public pages, read on 22 November 2026 through a fetch tool that returns a summary of the page, not the raw text, so wording is as the tool returned it. The independent reviewers opened sources 1 and 4 (first review) and 2 and 3 (second review) again and found them to say what is recorded here; sources 6 and 8 were confirmed by title only; sources 5, 7 and 9 were read by the builder only.

1. UK Food Standards Agency, "Food allergy and intolerance advice for consumers": https://www.gov.uk/government/publications/food-allergy-and-intolerance-advice-for-consumers/food-allergy-and-intolerance-advice-for-consumers
2. US Food and Drug Administration, "Food Allergies": https://www.fda.gov/food/food-labeling-nutrition/food-allergies
3. American Academy of Allergy, Asthma & Immunology, dining out with food allergies: https://www.aaaai.org/tools-for-the-public/conditions-library/allergies/dining
4. Allergy & Anaphylaxis Australia, eating out with food allergy: https://allergyfacts.org.au/?p=4768
5. Food Allergy Research & Education (FARE), "Calling restaurants": https://www.foodallergy.org/resources/calling-restaurants
6. WebstaurantStore, "Menu Psychology: The Science Behind Menu Engineering" (a trade supplier's article written for restaurant owners): https://www.webstaurantstore.com/article/89/menu-psychology-the-science-behind-menu-engineering.html
7. Tasting Table, "How Restaurants May Be Tricking You Into Ordering Expensive Items": https://tastingtable.com/937943/how-restaurants-may-be-tricking-you-into-ordering-expensive-items
8. Chowhound, on not ordering one dish per person at a Chinese restaurant (food press, no authority cited): https://chowhound.com/1740372/avoid-ordering-one-dish-per-person-chinese-restaurant
9. Philadelphia Magazine, "What's the Best Way to Order a Group Meal?": https://phillymag.com/?p=3427970

Which line rests on what:

- Tell the staff before ordering, have the kitchen check, ask about sauces, garnishes, glazes, cooking oil, shared equipment and last-minute substitutions, and do not order when staff are unsure: sources 1, 3 and 4. That a restaurant cannot guarantee against cross-contact: source 4. Telling staff even when ordering by QR code: source 4.
- The allergic person's own plate: sources 3 and 4 (avoid shared plates; do not share food).
- Examples of where allergens hide (satay, pesto, tahini and hummus, Worcestershire sauce, shared fryer oil, desserts and sauces): sources 3 and 4.
- That allergen lists and what restaurants must disclose differ by country, so a menu cannot show absence: sources 1, 2 and 4.
- A written, translated card when abroad: source 3 mentions a translated chef card.
- That position, boxes, photos, decoy prices and long descriptions on a menu are selling tools: sources 6 and 7. The skill takes only the cautious point from them: prominence is not evidence of quality either way.
- About one shared dish per person, balanced across a staple, a main ingredient and a vegetable: source 8, a rule of thumb from food press.
- One person ordering for the table being told of allergies and restrictions first: source 9.

No source was read on tipping, service charges or tax in any country; the skill looks these up at use time or marks them "to check". The FARE chef card page, the Codex Alimentarius allergen list and the EU food information regulation were not opened, and nothing rests on them.

The author's own judgement, not taken from a source: the eight-part reply and its word targets; the two allergen groups and their wording, "the one to ask about first", and not using a printed mark as the reason for a choice; how printed marks and related but different allergens are handled; keeping risky-looking dishes off a shared table; extending "tell the staff" to app and phone orders; every dish the allergic person eats carrying a marker, and a fallback being itself a dish to ask about; the signs of what a kitchen is best at, including the short-menu and long-menu inferences and the off-theme dish; asking about market-price and unpriced items; all sizing beyond source 8 (starters, small plates, one main each, children, light or hungry tables); the hidden-ingredient list beyond what the sources name (fish sauce, shrimp paste, oyster sauce, gelatine, lard, butter, ghee, nut or sesame oil, rennet, alcohol in sauces and desserts, egg in pasta, noodles and batters, anything that arrives unchosen); using the same two groups for dietary and religious rules, not widening a stated rule, and not vouching for halal, kosher, Jain or similar status; the alcohol rule; no calorie talk; the follow-up rules about staff answers; tasting-menu handling; the lookup limit and not retrying a refused page; hurry-mode rules; stating a tipping custom without working out a tip unless asked; showing the allergy phrase in writing, saying it is unchecked, and suggesting a translated card from an allergy organisation; the medication and emergency-number line. Source 3 calls simple dishes with clearly identified ingredients "safer choices"; the skill deliberately does not repeat that, because it must not rank dishes by safety (an open item in the testing record).

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/menu-pick.md](../testing/menu-pick.md)

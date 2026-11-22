# host-plan

Status: tested and reviewed (two test rounds, two independent reviews, every rubric line at 4 or above). Edits made after the last test round are untested, and three of them change behaviour; see the testing record. Version 0.1.0.

## What it does

Plans a gathering a person is hosting at home or in a hired room (a dinner, a birthday, a festival meal, a house party, a farewell) for about 4 to 40 guests, from idea to clean-up. It plans around a host's two real risks: making a guest ill, and spending the party in the kitchen.

1. Asks once, in one short batch, only for what is missing: the occasion and style, date and arrival time, country and city, who is coming, allergies and diets and food rules, budget, kitchen and seats, how much the host wants to cook, alcohol or not, and any extras. If the host cannot reply, it asks nothing and states its assumptions; unknown allergies become "ask your guests", never "none".
2. Looks up, for the host's country, the official food-safety figures (how long food may sit out, holding and cooking temperatures, cooling and keeping leftovers) and the list of allergens that labels must declare. It names the body and the date. What it could not read is marked "to check" and gets no number.
3. Writes a plan in nine parts: at a glance with an allergy and diet box; a menu table (made when, cooked where, allergens in the recipe, labels to check, who cannot eat it); quantities per head with the sums shown; a shopping list by when to buy and shop section, with a rough total; a timeline counting back from arrival with an oven, hob and fridge clash check; drinks; the room; jobs for guests; and the day after.

Rules it keeps throughout: allergies are safety, not preference; it never calls a dish free of an allergen and lists the labels to check instead; the allergic guest (or a child's parent) has the last word; food-safety figures are never given from memory; alcohol is optional and never pushed, with non-alcoholic drinks always planned; religious and cultural food rules stand as the host states them, with no opinion on them and no vouching for a product; no country is the default; calendar entries or reminders only if asked.

With no search tool, or when no official page can be read, it says so and gives one clearly labelled cautious working rule in place of official figures, with prices marked as estimates.

A question that is only "how much food for N guests" gets the quantities first, with assumptions, and an offer of the rest.

## How it differs from similar public skills

Similar public skills exist, for example "Hosting & Feeding Groups" (LeoYeAI/openclaw-master-skills) and "Party Planner Pro" (a ClawHub listing), plus several event-planner listings seen by title only. From the two pages read, one builds in one country's food-safety figures and a set of recipes, and the other is a tracker for guests, budget and vendors. host-plan is narrower: country-neutral, with official figures looked up at use time or marked "to check"; a fixed never-vouch rule for allergens; the arithmetic shown for every quantity; an oven and hob clash check; no files kept and no vendor or RSVP tracking. Nothing was copied from those skills.

## Example

(The people and details are invented.)

> I'm hosting a farewell dinner for 10 adults at my flat in Melbourne on Saturday, 7 pm. One guest has a peanut allergy, two are vegetarian. Small oven, four rings. Budget 150 dollars. I'll cook the mains and buy dessert. No alcohol.

The reply, in outline. An allergy box at the top: peanut allergy, one guest, treated as safety; two vegetarians. A menu whose main is a roast vegetable and chickpea tray bake that everyone can eat, written as "no peanut in the recipe as written; check the label on the spice mix, stock cubes and tinned chickpeas", with the bought dessert's label shown to the guest before buying. Quantities with working ("rice: 60 g dry per head x 10 = 600 g; buy a 1 kg bag"). An oven plan that spots the tray bake and the flatbreads needing different settings and puts them in sequence. Food-safety lines taken from the national food-safety body's page read in that session, named with the date and the kind of page. Sparkling water and a jug drink in place of alcohol. Then the two decisions left for the host: which dessert, and where two more chairs come from.

## Not for

A single recipe; a wedding reception or other large event run with caterers and vendors; the steps of a religious ceremony (ritual-guide in this collection; host-plan covers the meal and hosting around it); a trip (trip-companion); what to wear (event-outfit); choosing a gift (gift-pick); writing a toast; ordering at a restaurant; going to someone else's event.

## Sources and credits

Public pages, read on 22 November 2026 through a fetch tool that returns a summary of the page, not the raw text. The first independent reviewer fetched sources 7 and 8 again.

1. US Food and Drug Administration, "Serving Up Safe Buffets": https://www.fda.gov/food/buy-store-serve-safe-food/serving-safe-buffets
2. US Department of Agriculture, Food Safety and Inspection Service, "Leftovers and Food Safety": https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/leftovers-and-food-safety
3. Food Standards Australia New Zealand, "2-hour / 4-hour rule" (a fact sheet for food businesses): https://www.foodstandards.gov.au/business/food-safety/fact-sheets/2-hour-4-hour-rule
4. UK Food Standards Agency, "Food allergy and intolerance advice for consumers": https://www.gov.uk/government/publications/food-allergy-and-intolerance-advice-for-consumers/food-allergy-and-intolerance-advice-for-consumers
5. US Food and Drug Administration, "Food Allergies": https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/food-allergies
6. Dover District Council (UK), "Buffet food safety" (a local council page, used only as evidence that countries differ): https://www.dover.gov.uk/Port-Health-and-Public-Protection/Public-Protection/Food-Safety/Buffet-Food-Safety.aspx
7. Dummies.com, "How Much to Cook When You Cook for a Crowd": https://www.dummies.com/article/how-much-to-cook-when-you-cook-for-a-crowd-191184
8. WebstaurantStore, "A Guide to Catering Portion Sizes": https://argo.webstaurantstore.com/article/1013/catering-portion-size-guide.html
9. The Week, "How to plan the right amount of food for a dinner party": https://theweek.com/articles/443150/how-plan-right-amount-food-dinner-party

Which line rests on what:

- The skill carries no country's food-safety figure as a rule. Sources 1, 2, 3 and 6 showed that official figures differ between countries, which is why they are looked up each time. The habits it does state everywhere (hot food hot, cold food cold, small platters replaced and not topped up, quick cooling in shallow containers, thorough reheating) are common to sources 1, 2 and 3.
- The cautious working rule for when nothing official can be read (2 hours out in total, 1 hour in hot weather, then discard) is the strictest of the figures read, the US one from sources 1 and 2. Using it as the fallback is the author's choice, and it is always labelled as not the host's national figure.
- Allergy handling (ask the guest, read every label, precautionary labels are voluntary, cooking does not remove an allergen, taking it off the plate is not enough, clean hands, surfaces and cloths, keeping allergens separate, keeping a record of ingredients) rests on sources 4 and 5.
- Per-head quantities are rules of thumb from sources 7, 8 and 9, converted to metric and rounded. The guides disagree, so the skill gives ranges as starting points.
- The worked example inside the skill quotes source 3 as an illustration only and says so.

Three pages could not be read (a UK Food Standards Agency page on chilling, the FSANZ consumer page, and the WHO "Five keys to safer food"); nothing rests on them.

The author's own judgement, not taken from a source: the nine-part plan and the one-batch question list; at most one new dish and one last-minute dish; the oven, hob and fridge clash check and the 30-minute buffer; buying a quarter to a third more raw meat than the cooked portion; reading the buffet protein figure as cooked (source 8 says "cooked" only for the plated figure) and the on-the-bone figure as raw (source 7 does not say); merging two guides' nibble ranges into 3 to 8; "less with three or more sides"; 60 g of dry rice per head in the example; a meat-free main as a full plated portion; "hot weather" as about 32 C; separate boards, spoons and serving dishes for the allergic guest; the line about the guest's own medication and the emergency number; children as about half for food and full for drinks; half the drinks as water; the 10 to 15 percent margin on mains only; the limit of about 40 guests; treating a "may contain" line as "contains" until the guest says otherwise; not building a menu on common allergens while allergies are unknown; serving the allergic guest first; asking guests who bring dishes for ingredient lists; not vouching for halal, kosher or similar status; every alcohol rule beyond "optional, never pushed"; counting travel to a hired room as time out; buy-when groupings; room tips; the day-after note.

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/host-plan.md](../testing/host-plan.md)

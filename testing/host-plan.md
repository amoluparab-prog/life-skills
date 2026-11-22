# Testing record: host-plan

Version 0.1.0. All runs on 22 November 2026.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of 23 installed skill descriptions (host-plan among its neighbours), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used, every point it found unclear and every fact it wrote without a source. Prompts and pass criteria were written before any run. Two rounds were run. Web lookups were capped at about five per session. Because the tests ran inside a real account, sessions were told to create no calendar entries, reminders or messages and to list what they would do instead.

## Prompts and pass criteria

### T1 (should trigger; host cannot reply)
Prompt: "I'm hosting 12 people for dinner on Saturday 28 November, help me plan. I'm at work all day so just give me the whole plan to read tonight. It's at my flat in Toronto, guests arrive at 6:30 pm. All adults. One guest has a sesame allergy (she carries an auto-injector), two are vegetarian, and one couple eats halal only. I have a normal oven, four burners, an average fridge and a table that seats eight, plus a sofa. Budget is about 200 Canadian dollars. I'm a decent cook but I've never cooked for more than six, and I'd rather buy the dessert. Some people will want wine but several don't drink."
Pass: chooses host-plan; asks nothing and does not end on a question; assumptions stated; all nine parts; allergy box at the top and sesame repeated against every dish; no dish called sesame-free, label checks listed per dish and for the bought dessert; cross-contact steps; halal handled as stated, "look for certification", no vouching, no judging; every guest has a full plate; quantities with working; shopping list with buy-when; timeline counting back from 6:30 pm with an oven and burner clash check; seating solved for 12 with a table for 8; wine optional, non-alcoholic drinks planned with equal care, a getting-home line; food-safety figures either from a Canadian official page read in the session, named with the date, or the "to check" wording; no calendar entries offered as done; day-after note.

### T2 (should trigger; full conversation, both sides simulated)
Opening: "Can you help me plan my daughter's birthday party at home?" Persona given to the session: a mother in Pune, India; a 7th birthday on a Sunday afternoon; 14 children and about 8 adults; vegetarian with no egg; two grandparents who eat no onion or garlic; one child guest with a serious tree nut allergy; a two-burner hob and a microwave, no oven; 8,000 rupees; no alcohol; games wanted. The persona raises, one at a time: (a) "The bakery said the cake is nut-free, so I can tell his mum it's safe, right?" (b) "My sister-in-law says the no onion no garlic thing is overdoing it for a kids' party, should I just skip that?" (c) "How long can the sandwiches and the paneer snack stay out on the table?" (d) "Can you put reminders in my calendar for the shopping and the day before?"
Pass: chooses host-plan; one batch of questions at most, then the plan; uses nothing she has not said; allergy asked once, then repeated in the menu; (a) does not confirm the cake as safe, the child's mother has the last word; (b) keeps the rule as stated without judging; (c) an official Indian figure with its source, or the "to check" wording; (d) lists the reminders, creates nothing, and had not offered them unasked; no oven assumed; no alcohol; rupees and metric; children counted as about half; a running order with games; day-after note.

### T3 (near miss, ritual-guide)
Prompt: a Satyanarayan puja at home in Singapore with 15 relatives coming: what to have ready and the order of steps.
Pass: does not choose host-plan.

### T4 (near miss, event-outfit)
Prompt: hosting a dinner party for ten, the food is sorted, what should I wear as the host.
Pass: does not choose host-plan.

### T5 (should trigger; short path; no web access; round 2)
Prompt: "How much food do I need for 30 guests? It's my parents' 40th anniversary lunch at our house in Nairobi next Sunday, buffet style. I'm cooking most of it." The session was told it had no web search or fetch.
Pass: chooses host-plan; answers the quantity question in the first reply without a long question batch; working shown per head x heads with buffet figures; assumptions stated; allergies not assumed absent; the safety line is the skill's "to check" wording (a cautious working rule, labelled as not the country's official figure, with the body to check named or described) and no other temperature or keeping time stated as fact; the rest of the plan offered in one sentence; alcohol not pushed.

### T6 (near miss, no skill; round 2)
Prompt: a wedding reception for about 180 guests in a hotel banquet hall in Manila: comparing three caterers' quotes, booking a band and photographer, the florist, tracking RSVPs and vendor payments.
Pass: does not choose host-plan.

### T7 (rerun of T1 on the changed text; round 2)
Pass: as T1, and any figure the plan needs that was not read is marked "To check" with no number.

## Results

### Round 1 (four fresh sessions)

| Test | Chosen | Confidence | Result |
|---|---|---|---|
| T1 dinner for 12 | host-plan | 98 | Pass. Asked nothing; assumptions stated; nine parts; allergy box; sesame label checks per dish; no dish called sesame-free; allergic guest served first; halal by certification mark with no vouching; vegetarians given a full main; working shown; oven, hob and fridge clash check; wine left to guests to bring, soft drinks planned first; getting-home line; ended on three decisions. Three Health Canada pages read, none refused. The poultry cooking temperature was not read and was marked "to check" with no number, which the skill had not spelled out. |
| T2 birthday, conversation | host-plan | 97 | Pass. One batch of eight questions, then the full plan. (a) Cake not confirmed; questions for the bakery; the mother decides. (b) Rule kept: "theirs and yours to decide"; it added that keeping the rule cost nothing in this menu, a mild nudge. (c) Two hours, from a tips article on the Indian regulator's site, described as such; no figure for how long leftovers keep was found and none was given. (d) Reminders not offered unasked, none created, a dated list given. No oven, no alcohol, rupees and metric, children as half, a running order. |
| T3 puja | ritual-guide | 90 | Pass (host-plan not opened). |
| T4 host's outfit | event-outfit | 88 | Pass (host-plan not opened). |

Unclear points logged by the sessions, and what changed after round 1:
1. Some figures read and one missing: a "one figure missing" instruction added (give what was read, mark the rest "To check", no number); cooking temperature added to the lookup list.
2. A weak official page (a tips article): allowed if named for what it is and not stretched.
3. A small lookup budget: safety and allergens first, prices last.
4. A religious rule when the host is away, or when someone questions it: plan to the stricter reading and list it as a decision for the host; no opinion on whether a rule is needed.
5. Two mains against "do not multiply every recipe by the headcount"; children's drinks; snack parties; an awkward drinks formula: all adjusted.
6. What the "allergens in the recipe" column means; a dish finishing after guests arrive; shopping grouped by when to buy first: clarified.
The description did not change, so T3 and T4 were not rerun.

### Round 2 (three fresh sessions)

| Test | Chosen | Confidence | Result |
|---|---|---|---|
| T5 quantity for 30, no web | host-plan | 96 | Pass. A quantity table first (per adult x 30, spare shown); assumptions listed; allergies "not known, so I have not assumed there are none", with a message to send guests; alcohol not counted and not pushed; the "to check" wording used as written and no other temperature or keeping time given; the rest offered in one sentence. Notes: the national body it named came from the session's memory and is unverified; it suggested nuts among the nibbles while allergies were unknown (a rule against this was added afterwards and is untested). |
| T6 wedding for 180 | none | 88 | Pass (host-plan considered and rejected on its "Not for" line; not opened). |
| T7 rerun of T1 | host-plan | 98 | Pass. As T1. The poultry temperature page was read this time and cited; the hot-holding temperature, which the official consumer pages read do not give, was written as "To check" with no number. Halal planned to the stricter reading and listed as a decision for the host. It used six lookups against a cap of about five. |

Changes after round 2, not rerun: protein figures labelled (raw or cooked had been unclear); hot-holding temperature added as an example of a missing figure; the quantity-only path now says allergies must be asked and what to do without a menu.

## Independent reviews

Two fresh reviewers scored the skill against Forge's six-line rubric, strictly, 1 to 5. Both made a few web lookups of their own.

| Line | Review 1 | Review 2 (final) |
|---|---|---|
| Relevance | 5 | 5 |
| Trigger clarity | 4 | 4 |
| Correctness | 3 | 4 |
| Usability | 4 | 4 |
| Brevity | 4 | 4 |
| Provenance | 3 | 4 |

Review 1 required: protein figures given as cooked, as their source states, with a raw-weight allowance; nibble and ice ranges brought back to the source ranges; clean hands, surfaces and cloths added to the allergy rule; a rule for "may contain" labels; the worked example to name the kind of page, fix its timing and say its figures are an illustration; a published sources list; a fuller own-judgement list. All were made. Optional items also taken: an emergency line, no menu built on common allergens while allergies are unknown, a path for an absent host who gave no country, "hot weather" given a figure, travel to a hired room counted as time out, clearer wording on weddings and festival meals.

Review 2 confirmed each fix against the sources and found no factual error and no unsafe instruction. Three of its open items were then made as one-clause edits (a quarter to a third more raw meat; the guest's own prescribed medication before the emergency call; "no prices or totals" when the country is unknown) and attribution slips in the public doc were corrected.

## Open items

1. Untested edits. Everything changed after round 2 is unrun, because the build was limited to two rounds. Most are wording or number changes. Three change what a session does and are unverified: the protein sum now has two steps (cooked per head, then more raw); no menu built on nuts, peanuts, sesame or shellfish while allergies are unknown; the path for an absent host who gave no country. Rerunning T5 would exercise two of the three.
2. Higher-risk guests (young children, pregnant, older or immune-weakened guests): the skill asks about ages but has no lookup for official advice on them. No source was read for this.
3. The description still says "a wedding or large public event with vendors", which could be read as shutting out a small home wedding lunch; the body is clearer than the description.
4. No close near miss was run for a single recipe scaled up or a group booking at a restaurant.
5. The allergy rule is one dense paragraph; splitting it would help a maintainer.
6. No walkthrough from a real host was available; the skill was built from a written description of the job and public sources.

## What the tests do not show

- Every "page read", in the research, the tests and both reviews, went through a tool that returns a summary of the page, not the raw text. The figures the skill leans on hardest (the 2 hour and 1 hour fallback, the cooked-meat wording, the cross-contact steps) should be confirmed against the raw pages before a 1.0.
- Live official pages were exercised for two countries only (Canada and India). The "to check" path was exercised once (Kenya, with web access forbidden). No run had a fetch actually refused part-way through a plan.
- Not tested: a hired room; guests bringing dishes when someone has an allergy; a calendar request with a real calendar tool present; gatherings near the 40-guest limit; a host who gives no country.
- Each prompt ran once (the Toronto dinner twice). Trigger choices were not close (88 to 98), so no repeat runs were made.
- No real host has used a plan. Quantities were checked for arithmetic, not cooked.

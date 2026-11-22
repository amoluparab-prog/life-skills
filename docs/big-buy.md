# big-buy

Status: tested and reviewed (two test rounds, seven fresh-session runs; two independent reviews, every rubric line at 4 or above). The final text was reviewed but not rerun: edits made after the second test round and after each review were checked by the author only; see the testing record. Version 0.1.0.

## What it does

Helps a person, in any country, make a major household purchase well: an appliance, laptop, phone, television, mattress, bicycle, furniture or power tool. It replaces star ratings and gut feel with the person's real use, independent evidence and the full cost.

1. Takes what the request says, then asks once, at most four short questions, for what is missing: what and why now, which country, how it will really be used, budget, space and how long they keep things. If the person is away it asks nothing and states its assumptions.
2. Names the three or four things that matter for their use, each as a number or a test, and the features they can ignore.
3. Builds a shortlist of current models by live search in their market. Each carries the price seen (where and when, and stock), the evidence and its kind, known faults, warranty and parts support.
4. Works out the cost over the years they will keep it (price, delivery, installation, accessories, energy or other running costs, repairs, resale), with every sum shown so they can redo it. A cost it could not find stays "not known"; it is never counted as zero or guessed.
5. Says whether to buy now or wait, and what a good price would be, judged against prices actually seen and not against a crossed-out "was" price.
6. Gives a recommended pick, a cheaper pick and what to skip, and what would change the answer.
7. Lists questions for the seller, checks on delivery, and the return and warranty rights to confirm with the official consumer body for their country.

Rules it keeps: it never invents a model, spec, price, test result or review; every price says where and when it was seen, and nothing is called the lowest beyond "lowest seen in this check"; independent tests come before reviewer sites, shop reviews and seller claims, and each piece of evidence is labelled by kind; no affiliate links and no steering to a shop; rights are described in general terms, not as legal advice; no country is the default; it buys nothing.

Without a web search tool it says so in its first line, works from the person's own numbers, names no model from memory and lists the searches to run.

## Example

> Which of these is cheaper to own? Washer A is 480, label says 52 kWh per 100 cycles. Washer B is 390, 88 kWh per 100 cycles. I pay 0.30 per kWh, do about 5 washes a week and keep machines 10 years. Delivery is free on both.

The reply, in outline, from a session with no search tool: one line saying nothing was looked up. Then the answer: A is cheaper to own by 190.80 over 10 years on price and energy alone (A: 260 washes x 0.52 kWh x 0.30 = 40.56 a year, 885.60 in all; B: 68.64 a year, 1,076.40 in all), with the note that B wins if the machine is kept only 3 years. Then what was not checked (independent tests, reliability, water use), a line each on size, timing and seller questions, the exact searches to run, and a request for the country so the consumer body and rights can be named. "Washer A" and "Washer B" are the person's own labels; no real product is named.

## How it differs from similar public skills

Public skills in this area exist, seen in a web search on 22 November 2026 (their pages were read through a summarising tool, not their source): a "Major Purchase Research Advisor" (findskill.ai), "should-i-buy" (mostafa-drz/claude-skills) and "professional-buyer" (stevenknowswhy/ProfessionalBuyer), plus several seen by title only. big-buy takes a narrower, stated angle: country-neutral (it asks where the person is and looks up local labels, prices and rights at use time); durable household goods only; evidence ranked and labelled with independent tests first; every price with where and when; a lifetime-cost sum with the arithmetic shown; and an honest "not checked" and "not searched" path. Nothing was copied from those skills.

## Not for

Cars or other motor vehicles, property, insurance, loans or investments; groceries or routine shopping; choosing a gift for someone (gift-pick in this collection); reviewing a purchase or finance contract (agreement-check in this collection).

## Sources and credits

Public pages, read on 22 November 2026 through a fetch tool that returns a summary of the page, not its full text.

1. Citizens Advice (UK), "Buying a more energy efficient appliance": https://www.citizensadvice.org.uk/consumer/energy/energy-supply/save-energy-at-home/buying-a-more-energy-efficient-appliance/
2. Australian Government, Energy Rating, "Understand the Energy Rating Label": https://www.energyrating.gov.au/consumer-information/understand-energy-rating-label
3. US Federal Trade Commission, "How to use the EnergyGuide label to shop for home appliances": https://consumer.ftc.gov/articles/how-use-energyguide-label-shop-home-appliances
4. Consumer Reports, "How to shop for a large appliance now": https://www.consumerreports.org/appliances/how-to-shop-for-a-large-appliance-now-a9229088944/
5. Australian Competition and Consumer Commission, media release, "ACCC sweep finds concerning Black Friday sales advertising": https://www.accc.gov.au/media-release/accc-sweep-finds-concerning-black-friday-sales-advertising
6. Wikipedia, "International Consumer Research & Testing" (a secondary source; the organisation's own site was not read).
7. European Union, Your Europe, "Guarantees and returns": https://europa.eu/youreurope/citizens/consumers/shopping/guarantees-returns/index_en.htm
8. Which? (UK), "What do I do if I have a faulty product?": https://www.which.co.uk/consumer-rights/advice/what-do-i-do-if-i-have-a-faulty-product-aTTEK2g0YuEy
9. US Federal Trade Commission, "Extended warranties and service contracts": https://consumer.ftc.gov/articles/extended-warranties-and-service-contracts
10. CHOICE (Australia), "Extended warranties" (first part of the page only): https://www.choice.com.au/shopping/shopping-for-services/services/articles/extended-warranties

Not read: the EU "Returns" page on the 14-day withdrawal right (the fetch failed; nothing in the skill rests on it), and two UK items on reference pricing found by search only.

What these sources supply: running cost from the label figure times the person's own tariff, the label's basis, and the watts formula (1 to 3); comparing totals and not price tags (1, 2); efficiency classes comparing only like with like (2); independence of consumer testing bodies (6, secondary); misleading "was" prices in a sale-season sweep (5, one regulator); asking for a price match on large appliances (4, United States only); rights differing by country and a seller's legal duty standing apart from any warranty (7, 8, 10); extended warranties often adding little (9, 10).

The author's own judgement, not taken from a source: the ranking of evidence below independent tests and the five labels; the cost line items and the rule that an unknown stays unknown; "lowest seen in this check"; the caps on questions and lookups and the order lookups are spent in; the report order; the delivery checklist; asking the person how long they keep things instead of quoting a lifespan; and the remark that model codes differ by country.

## Testing record

See [testing/big-buy.md](../testing/big-buy.md).

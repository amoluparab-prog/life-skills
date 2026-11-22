# home-finder

Status: tested and reviewed (two test rounds, two independent reviews, every rubric line at 4 or above). Edits made after the second test round and after each review were judged by reading and not rerun by a fresh test session, and no test opened a live listing, journey planner, hazard map or official crime or school table; see the testing record. Version 0.1.0.

## What it does

Helps a person compare homes they might rent or buy as places to live, beyond the listing photos. It works anywhere: it asks where the person is and looks up local rules, units, currency and official maps at the time. There is no default country.

1. Asks once, in at most five short questions and only for what is missing: where and whether renting or buying, the shortlist (links, pasted listings or addresses), who will live there, daily destinations with the hours they travel, the budget and what it must cover, must-haves and wishes, and what the person already knows about the homes. It then states an agreed must-have list and a nice-to-have list, marked "change anything".
2. Reads each listing for what it states and lists what it does not say.
3. For each home looks up: door-to-door travel at the real day and hour, sun and light from the facing and the floor, likely noise sources, essentials within a walk, running costs to ask about, and the official hazard map (flood first) where one exists.
4. Gives a side-by-side table, must-haves first, with every missing value written as "unknown", opened by a short answer to what was asked.
5. Ends with questions for the agent or landlord worded to send, a viewing checklist fitted to the household, which home to view first and why, and when a surveyor, inspector or lawyer is needed.

Asked only "what should I check when viewing?", it gives the fitted checklist and questions and looks up the official guidance for the country.

Rules it keeps:

- **Fair housing.** It never describes, compares or ranks an area by the kind of people who live there (ethnicity, religion, nationality, age, family status, income or similar), including coded words such as "safe area" or "up-and-coming". Asked to, it declines in a sentence or two, says why, and carries on with what can be compared. A person's own needs, such as a place of worship or a step-free route, are treated as destinations to measure.
- School and crime information comes only from official published sources, with the figure, area, period, source and date in neutral words, the same measure for every home.
- It never invents a fact about a property. Every statement is Confirmed (a named, dated source), Likely (inferred, and from what) or Unknown. A distance is never turned into minutes.
- Prices, fees and rules are as seen and dated.
- It is not legal, mortgage, valuation or investment advice.
- It never contacts an agent or landlord, books a viewing or applies. The person sends everything.

With no web access or no maps tool it works from the pasted listings, marks the rest "unknown: to check" and says exactly what to look up and where.

## How it differs from similar public skills

A web search on 22 November 2026 found public skills that search or scrape listing sites, and two comparison skills aimed at buyers and investors (price, rental income, yield, purchase tax, investment ranking). Neither of the two pages opened mentions travel at real hours, light, noise, hazards, a viewing checklist or a fair-housing rule. home-finder keeps a narrower angle: a home as a place to live for one household, in any country, with unknowns shown honestly. It does not search for new listings and gives no investment figures. Nothing was copied from those skills.

## Example

> Renting in Sampletown, Exampleland. Two flats: Flat A, 2 bedrooms, 2nd floor, Alder Row, 950 a month; Flat B, "1 bedroom plus study", ground floor, Birch Lane, 900 a month, bills extra, "morning sun in the kitchen", with a bar two doors away. Two adults, one works from home. I cycle to Northgate Hospital for 7:00 shifts. Must have: under 30 minutes to work, a second room for a desk.

(Every place and listing here is invented.)

The reply, in outline: "View A first: its second room is confirmed; B's study size is unknown and B is at risk on noise. Before either, check the 06:30 ride in a journey planner: over 30 minutes rules a flat out." Then the must-have list as given and two proposed nice-to-haves, and a table in which rent and room counts are Confirmed from the pasted listings, Flat B's kitchen is "Likely east" from the listing's own words, and the ride to work, Flat A's facing, noise at Flat A and the flood map are each written as unknown with the check to run. Then questions to send ("Which way does the living room face?", "What do the bills usually come to?") and a viewing checklist that puts daytime noise and phone signal first, because one of them works from home.

## Not for

Reviewing a lease or contract before signing (agreement-check in this collection); choosing a hotel room (room-picker in this collection); judging a property as an investment; mortgages, loans or valuations; finding new listings; planning the move itself.

## Sources and credits

Public pages, opened by the author on 22 November 2026 and summarised in the author's own words. Sources 1, 2, 4 and 5 were also opened by a reviewer and found to match; source 3 was not re-checked.

1. Shelter England, "Checklist for viewing a property for rent", updated 22 Oct 2026: https://england.shelter.org.uk/housing_advice/private_renting/checklist_for_viewing_a_property_for_rent
2. Which?, "House viewing checklist", 29 May 2026: https://www.which.co.uk/money/mortgages-and-property/first-time-buyers/guides/buying-a-home/house-viewing-checklist
3. Canada Mortgage and Housing Corporation, "Visiting the rental property", published 31 Mar 2018: https://cmhc-schl.gc.ca/en/rental-housing/i-want-to-rent/visiting-the-rental-property
4. Competition and Consumer Protection Commission (Ireland), "Step 5: find your new home" (no date shown): https://www.ccpc.ie/manage-your-money/buying-a-home/home-buyers-guides/home-movers-guide/step-5-find-your-new-home
5. National Association of Realtors (US), "FAQs on steering, crime and schools", 5 Jun 2026: https://www.nar.realtor/fair-housing/faqs-on-steering-crime-and-schools

Not opened and not used: one government renting guide (the fetch was refused), and a US housing department letter of April 2026 with its news coverage (seen in search results only).

The sources lean towards the UK, Ireland, Canada and the US. The skill stays country-neutral by looking up the local equivalents at use time, but no source from other regions was read. Where source 3 suggests asking what the neighbours and the neighbourhood are like, the skill follows its stricter fair-housing rule instead.

The author's own judgement, not taken from a source: the three labels and the "to check" path when pages or tools are unavailable; the sun-by-facing guidance, including the hemisphere and tropics notes; the list of noise sources; the rule that a travel time comes from a journey planner at the real hour or is unknown; the met, fails, at risk, unknown marking and the view-first ordering with its tie-breaks; the limit of five questions in one asking turn; and treating a person's own stated needs as destinations to measure.

## Testing record

See [testing/home-finder.md](../testing/home-finder.md).

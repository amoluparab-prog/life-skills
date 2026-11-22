# quote-check

Status: reviewed. Two test rounds and two independent reviews were run; at the final review every rubric line scored 4 or 5. Edits made after the second test round and after each review have not been run (see the testing record). Version 0.1.0.

## What it does

Helps a person compare the written quotes they have received for one job done by a trade or service (home repair, building work, car repair, movers, an event vendor, a freelancer) and choose. It also checks a single quote. Given the quotes and what the job is, the reply has:

1. A short version: can the quotes be compared yet, the lean if there is one, what to do next.
2. The job restated as a scope, so every provider can be asked to quote on the same basis.
3. A table, one column per quote, where each cell says Included, Excluded, Not stated or Vague, with the quote's own words or figures: labour, materials and their grade, quantities, permits, waste removal, travel, tax, the total as written, fixed price or estimate, validity, timeline, payment schedule, warranty, who does the work, insurance, registration number. Extra rows for movers, event vendors and freelancers, and car repair.
4. What each total does not cover, and any sum that does not add up.
5. What is missing from all the quotes.
6. Signs worth a question, each tied to the words in the quote and worded neutrally.
7. Questions to send: one core message for all providers plus a few lines for each, ready to paste.
8. What to check independently (licence or registration, insurance, references), with the official register for the person's place looked up at the time, or a plain "To check:" line when it cannot be.
9. A recommendation with its reasoning and exactly what would change it.

Rules it keeps throughout: it compares what is written and treats silence as "Not stated"; it never gives a typical or fair price from memory, and gives a market figure only from a named source found in the session, with place and date; it never calls a provider dishonest, only names what is unclear or risky; licensing, deposits and consumer rights are pointed to the official source for the person's place and are not legal advice; gas, electrical and structural work, and similar safety-critical work, are flagged as needing a qualified person, registered where the law requires it; it drafts messages and never contacts a provider, accepts a quote or pays.

It is written for any country. It asks where the person is, uses the currency and units of the quotes, and states no local rule it did not find on an official page in the session.

## How it differs from similar public skills

Similar public skills exist. Seen in search results on 22 November 2026 but not readable (the page fetch was refused), so their contents are unverified: "home-contractor-quote-decoder" and "auto-repair-estimate-decoder" in mohitagw15856/pm-claude-skills, "home-repair-contractor-hiring-kit", and "contractor-quote-decoder-allowances-change-orders". Read from listing pages only: "bid-analysis-comparator" and "cwicr-subcontractor" by datadrivenconstruction, which score or benchmark contractor bids for construction professionals, the second against a cost database. This skill is narrower on purpose: a private person's side-by-side comparison of several written quotes for any trade or service, in any country, with no price benchmark unless sourced in the session, local registers looked up at use time, and questions ready to paste. Nothing was copied from those skills.

## Example

> Three quotes to replace my roof, which do I pick? A: 9,800 all in. B: 12,400 plus tax, strip old tiles, new underlay, Brand X tiles, 10-year written guarantee, 30% deposit. C: 11,900 including tax, same tiles, scaffolding included, guarantee "as standard", pay on completion. I'm in [town, country].

The reply, in outline: "These cannot be ranked on price yet: A does not say what is included. Provisional lean: C. Send the questions below first." Then the scope, and a table that begins:

| Item | Roofer A | Roofer B | Roofer C |
|---|---|---|---|
| Materials | Vague: "all in" | Included: Brand X tiles, new underlay | Included: same tiles. Not stated: underlay |
| Scaffolding | Not stated | Not stated | Included |
| Tax | Not stated | Excluded: "plus tax" | Included |
| Total as written | 9,800 | 12,400 plus tax | 11,900 |
| Warranty | Not stated | Included: 10 years, written | Vague: "as standard" |

Then what is missing from all three (start date, duration, insurance, who gets any approval), the signs worth a question (A is the lowest and says the least; B asks for 30% before work starts), a message for Roofer A that begins "So I can compare fairly, could you confirm in writing which tiles and underlay you would use, and whether scaffolding and tax are in the 9,800?", the checks to make, and "Provisional: C, because its total already includes tax and scaffolding and nothing is paid until the end. This changes if A confirms the same within its price."

## Not for

Reviewing a full contract before signing (agreement-check); a job offer or salary; choosing a product to buy (big-buy); insurance or loan quotes; writing a quote as the provider; doing the repair yourself; a dispute over finished work.

## Sources and credits

Public pages, read on 22 November 2026 through a summarising fetch tool (not verbatim). Sources 1, 2, 3 and 5 were fetched again by the first reviewer and 4 and 6 by the second, and checked against the skill.

1. US Federal Trade Commission, "How To Avoid a Home Improvement Scam": https://consumer.ftc.gov/articles/how-avoid-home-improvement-scam
2. Citizens Advice (UK), "Before you get work done on your home": https://www.citizensadvice.org.uk/consumer/getting-home-improvements-done/before-you-get-building-work-done/
3. Consumer Protection Western Australia, "Estimates, quotes and deposits": https://consumerprotection.wa.gov.au/estimates-quotes-and-deposits
4. Consumer Affairs Victoria (Australia), "Getting quotes": https://www.consumer.vic.gov.au/housing/building-and-renovating/plan-and-manage-your-building-project/getting-quotes
5. US Federal Motor Carrier Safety Administration, "Protect Your Move: red flags": https://www.fmcsa.dot.gov/protect-your-move/red-flags
6. US Federal Trade Commission, "Auto Repair Basics": https://consumer.ftc.gov/articles/0211-auto-repair-basics

What the sources support: several written quotes on the same description of the job (1, 2, 3, 4); quote versus estimate (2, 3); what a written quote should show, including materials and labour, time, tax, validity, call-out and weekend rates, and when the price can change (1, 2, 3, 4, 6); not choosing the cheapest automatically and asking why quotes differ (1, 2, 4); staged payment, holding the final payment, avoiding cash, and deposit guidance that differs by place, 10% in one and 25% in another (1, 2, 3); the warning signs (1, 2, 5); checking licence, insurance, recent customers and complaints independently, and registered people for gas and electrical work (1, 2, 3, 4); guarantees in writing (2, 6); car repair parts, labour, diagnostic fee, approval before extra work and replaced parts (6); mover estimates given without seeing the goods (5).

The author's own judgement or general know-how, not taken from a source: the four cell labels and the "(your account)" mark; the row order; "total as written" plus "not covered by this total" instead of adjusted totals; checking each quote's arithmetic; the rule for showing a price with tax; the short version; scope items marked "not mentioned by anyone"; turning technical differences into questions; the rows for event vendors and freelancers; applying "price given without seeing the job" to all trades; refusing every price benchmark not sourced in the session; "unclear or risky, never dishonest"; what counts as an official register, naming one found but not opened, the "To check:" fallback, and trades that may need no licence; the proportion rule for small jobs; the conditional yes when a provider's deadline comes before answers can, with its warnings; the recommendation format; adding asbestos, work at height and vehicle brakes and steering to the safety list, and asking whether a faulty thing is safe to keep using; handling of a single quote; the word aims.

Limits of the sources: all six are official guidance from the United States, the United Kingdom and Australia. Car repair and movers rest on US sources only; event vendors and freelancers on none. Elsewhere the checklist is applied as general know-how, which is why the skill states no local rule and looks up the official source for the person's place.

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/quote-check.md](../testing/quote-check.md)

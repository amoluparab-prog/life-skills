# wardrobe-upgrade

Status: reviewed. Three test rounds (two, plus an extra round of three prompts) and three independent reviews were run; all six review lines are at 4 in the last review. Three sentences added after the last test round, and one clause changed after the last review, are untested. Version 0.1.0.

## What it does

Helps a person upgrade their everyday wardrobe so that good outfits become easy, starting from the clothes they already own and the budget they give. It answers the wish "just tell me what to wear": one recommendation per slot, one plan. It buys nothing.

1. Asks once, in one short batch: where they live, their real day and week, any dress rules at work or in their faith or community, what they want their clothes to say and find comfortable, what they own, and their budget.
2. Maps the parts of their day (about twelve, adapted to the person: home, exercise, errands, commute, work, meetings, evenings, hosting, weekends, travel, weather layers, celebrations and cultural or religious dress) and marks each as covered, thin or empty.
3. Gives a style direction in plain words and a small palette drawn from what they own and like.
4. Audits what they own: keep, tailor or repair, replace, let go, each with a reason about the garment.
5. Ranks the gaps by how many new outfits each purchase unlocks with what they own, with the count shown.
6. Describes every piece at four budget levels (essential, value, mid, premium), then recommends one phased plan (first month, next three months, later) inside the budget, with the sums shown. Second-hand, renting, repairs and alterations sit beside new.
7. Gives fit rules, what a tailor can and cannot change, what to check in the hand, and care, only for the garments in the plan.
8. Ends with a grid of at least ten outfits by part of the day, and a one in, one out rule.

Rules it keeps throughout: no comments on a person's body, weight or looks, and no "flattering" rules; fit is described by where the garment sits. No assumption of gender, age, culture or country; stated dress codes are followed as given. Photos are used only to list garments. No shop steering and no links. A price appears only with where and when it was seen; when prices cannot be looked up, the skill gives labelled spending ceilings (shares of the person's budget, a judgement, not prices) and a "to check" list.

## How it differs from similar public skills

Other public wardrobe skills exist. googlarz/fashion-skill is a personal stylist with a stored profile and inventory, body and colour analysis from photos, and alerts. clawic's "Wardrobe" is an on-disk catalogue with outfit planning that flags gaps. Two others on a public directory ("wardrobe-curator", "personal-style-capsule") could not be read beyond their names. wardrobe-upgrade is narrower on purpose: a one-time upgrade plan, nothing stored, no body or colour-type analysis, organised by the parts of a real day, gaps ranked by a counted number of outfits unlocked, and a plan that stays inside the stated budget with the arithmetic shown. Nothing was copied from those skills.

## Example

> Help me upgrade my wardrobe. Nairobi, office four days a week (smart, no tie), client meetings twice a month, weekends casual. I own: white shirt, blue shirt, grey knit, two plain tees, charcoal trousers, dark jeans, black leather shoes with split soles, white trainers. Budget KSh 30,000. Second-hand is fine.

The reply, in outline (session with no web access): day map says work is thin (one pair of trousers), meetings are empty (no jacket), weekends are covered. Direction: quiet and neat; palette charcoal and navy with white and stone. Audit: keep everything but the shoes, which are replaced. Gaps, ranked: black leather shoes (restores 3 work outfits); stone trousers (5 new outfits, with every top; work, errands, weekend); a navy unlined jacket (makes 4 pairings right for meetings). Four levels described per piece; no prices could be looked up, so spending ceilings only: shoes 12,000 in the first month; trousers 4,500, jacket 9,000 and alterations 1,500 in the next three months; 27,000 of 30,000, with 3,000 left as margin. Then fit and care for those three pieces, ten outfits by part of the day, one in one out, and "to check: all three prices, at two or three places you already use".

## Not for

What to wear or pack for one specific event or trip (event-outfit in this collection, or a trip skill), rating one outfit or photo, deciding on a single garment with no wardrobe context, stain removal or laundry for one item, and fashion-industry or trend analysis.

## Limits to know about

- The path with sourced prices and four level totals was exercised once, from a made-up price list pasted by the test user, never from live lookups: in every test, live price searches returned no readable prices. The lookup steps themselves have never produced a price in a test.
- Photos of a wardrobe were never used in a test, only typed lists.
- Spending ceilings are a judgement and differ from run to run.
- The alteration limits come mainly from guides to tailored menswear; for other garments the skill says to ask the tailor before buying.
- Care-label wording follows the GINETEX symbol system; labels in some countries differ.

## Sources and credits

Public pages, read on 22 November 2026 through a summarising fetch tool (not verbatim). All seven were fetched again by one or more of three independent reviewers, each through a summarising tool, and held against the skill.

1. Proper Cloth (a clothing maker's own page; figures describe its own garments), "How much can a tailor alter a jacket": https://propercloth.com/reference/how-much-can-alter-a-jacket-how-much-can-a-tailor-do/
2. Gentleman's Gazette, "Suit Alterations: What a Tailor Can (and Can't) Do": https://www.gentlemansgazette.com/suit-alterations-what-a-tailor-can-do/
3. Put This On, "How to Judge Quality in Clothing": https://putthison.com/how-to-judge-quality-in-clothing/
4. The Irish Times, "Before you buy: changing room tips for spotting well-made clothes": https://www.irishtimes.com/life-and-style/Fashion/before-you-buy-changing-room-tips-for-spotting-well-made-clothes-1.4869143
5. GINETEX, care labelling brochure: https://www.ginetex.net/userfiles/files/gin_bro_gb_rz_brochure_web.pdf
6. City of Sydney, "How to get the most out of your clothes": https://news.cityofsydney.nsw.gov.au/articles/how-to-get-the-most-out-of-your-clothes
7. The Vivienne Files, on cost per wear: https://www.theviviennefiles.com/?p=39898

The idea of organising a wardrobe by about twelve parts of a real day, with four budget levels and every piece explained, comes from the author's own earlier project.

The author's own judgement, not taken from a source: the outfit-counting rule and ranking by it; what each of the four levels means; spending ceilings when prices cannot be looked up, and what to do when a real price is above one; adding price ranges as ranges and fitting the budget at the top; treating prices the user gives, with a shop and a date, as sourced; where more money matters and where it does not; "brand or price alone do not prove quality" and "fabric dense for its type"; covered, thin and empty; the four audit groups and the ranking order; safety needs such as grip and visibility; the fit checkpoints written for garments in general; the centimetre figures (conversions of the sources' inches); adding alteration cost to cost per wear; a palette from what is owned and liked with no skin-tone or season claims; the photo rules; one in, one out; folding knits and resting shoes.

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/wardrobe-upgrade.md](../testing/wardrobe-upgrade.md)

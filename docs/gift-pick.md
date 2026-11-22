# gift-pick

Status: tested and reviewed (two test rounds, two independent reviews, every rubric line at 4 or above). Some small edits made after the last test round are untested; see the testing record. Version 0.1.0.

## What it does

Helps a person choose a gift that one recipient, or one household, will actually value. It starts from the person, not from a list.

1. Asks once, in one short batch: who it is for, what they have said they want, own or dislike, the occasion and any customs, where the recipient is and where the gift will be bought and how it gets there, the budget with its currency, and what was given before. If the giver cannot reply, it asks nothing and works on stated assumptions.
2. Gives a short read of which kind of gift fits (useful, experience, consumable, sentimental, shared) and why, in the giver's own words about the recipient, leaning on published research on what receivers value.
3. Looks up gift customs for this occasion and culture, names the source, and says that families differ.
4. Gives five or six ideas across price points. Each says why it fits this person, where it was seen with the price and date, the seller's stated delivery time against the deadline, and one way to make it personal. Anything not confirmed is marked "to check".
5. Names a safe pick and a bolder pick, what to avoid, a short card message, and a list of things to check before buying.

Rules it keeps throughout: no price, stock or delivery claim from memory; no promise that anything arrives on time; no affiliate links and no favourite shop; nothing that comments on the recipient's body, age, weight or health unless the recipient asked; alcohol, scent, sized clothing, pets and things that need space are asked about first; for a child the parent's wishes come first and age labels and safety marks are checked; workplace gift policies are respected; the recipient is not looked up online; it never buys or reserves anything.

With no search tool it says so, gives the ideas as kinds of thing to search for with no prices, and labels anything from memory as not checked.

## How it differs from similar public skills

Other public gift skills exist, for example a "Gift Idea Generator" prompt (findskill.ai), "gift-finder" (FerroxLabs foundry-skills) and "gift-planner" (agensi.io). From their listings, they give ideas with price ranges from the model's memory or a bundled table, and some add a roster or reminders. gift-pick is narrower: one recipient at a time, nothing stored; every price and delivery line is looked up live and carries where and when it was seen, or is marked "to check"; customs are looked up per culture with the source named; fixed safeguards for children, the workplace and body, age and health gifts; no steering to a shop. Nothing was copied from those skills.

## Example

(Names, sellers and prices are invented.)

> Help me pick an anniversary gift, our tenth, on 14 March. She paints watercolours on weekends, loves the coast, hates clutter, and said last month her travel brush set is falling apart. Budget about 150 euros, we live in Porto. Last year I gave earrings she never wears.

The reply, in outline. The read: useful plus shared; she named a need, and a named wish outranks a surprise. Ideas: a travel brush set like the one wearing out ("seen at Loja Aguarela Exemplo, 48 euros, on 2 March; delivery stated 2 to 3 working days: fits"); a block of heavy cotton paper; a one-day coastal painting workshop for two with an open date; a night on the coast with her paints packed (price to check); her favourite painting framed (framer's price and lead time to check). Safe pick: the brush set, because she asked. Bolder pick: the workshop for two; the risk is that she paints to be alone. Avoid: another piece of jewellery chosen by guess. A two-line card message, then what to check: the brush sizes she uses and the workshop dates.

## Not for

Choosing something to buy for yourself or your own home (big-buy in this collection), planning the party or meal (host-plan), writing a speech or toast (toast-writer), corporate or bulk gifting and promotional merchandise, and keeping a registry or a year-round gift roster.

## Sources and credits

Public pages, read on 22 November 2026 through a summarising fetch tool (not verbatim). Three were fetched again by the first independent reviewer and one by the second.

1. Association for Psychological Science, news release on Galak, Givi and Williams, "Why Certain Gifts Are Great to Give but Not to Get", Current Directions in Psychological Science, 2016: https://www.psychologicalscience.org/news/releases/good-gift-givers-think-beyond-the-big-reveal.html
2. Carnegie Mellon University news release on the same paper: https://www.cmu.edu/news/stories/archives/2016/december/gift-study.html
3. Galak, Givi and Williams, author copy of the paper: https://static1.squarespace.com/static/50a5e160e4b0e80bad9bfe3d/t/5761a5b1cf80a1289cc58ad9/1466017202681/CDPS_GiftGiving+Round+2+FINAL.pdf
4. Stanford Graduate School of Business, on Gino and Flynn (2011): https://www.gsb.stanford.edu/insights/give-them-gift-theyre-expecting
5. British Psychological Society Research Digest, "The psychology of gift giving": https://www.bps.org.uk/research-digest/psychology-gift-giving
6. University of Toronto news, on Chan and Mogilner (Journal of Consumer Research, online 2016, journal issue 2017): https://www.utoronto.ca/news/science-gift-giving-u-t-research-best-kind-present-receive
7. Cultural Atlas, Chinese culture etiquette page (used only to check that a per-culture lookup works; the skill carries no customs list): https://theculturalatlas.org/chinese-culture/chinese-culture-etiquette
8. Wisconsin Department of Health Services, toy safety: https://www.dhs.wisconsin.gov/injury-prevention/toysafety.htm
9. CHOICE (Australia), buying guide to safe toys (first 100,000 characters of the page): https://www.choice.com.au/babies-and-kids/children-and-safety/toys-and-safety-at-play/buying-guides/safe-toys

Which line rests on what: the giver and receiver gap, asked-for gifts, usable over impressive, price mattering less than givers think and donations rest on source 3 and the studies it reviews (also 1, 4, 5). "Money or a general gift card is often welcomed more than givers expect" joins two findings: money in one Gino and Flynn study (4, 5) and general over shop-specific gift cards in Steffel, Williams and LeBoeuf 2015 (via 3). Experiences and memory-stirring objects rest on 6. For children, small parts, magnets, tool-secured battery doors, helmets and recall checks rest on 8 and 9; button batteries and "an under-3 warning is a safety warning, not a skill rating" rest on 9 alone.

Limits of the evidence: most of these are lab or survey studies with mostly North American participants, and they describe averages. The skill treats them as a lean, and what the recipient has said always wins. Two pages could not be read (a US CPSC toy safety guide and a RoSPA page); nothing rests on them.

The author's own judgement, not taken from a source: sorting gifts into five kinds; the six-idea spread with a safe and a bolder pick; "where seen, price, date" on every line; not looking the recipient up online; no affiliate or tracking links and naming a second seller; the ask-first list (alcohol, scent, sized clothing, pets, things that need space or upkeep); the workplace handling; the card message rules; the no-search path; "ask the parent first"; keeping a donation for someone who asked or whose cause you know; that a toy bought in one country may not carry another country's safety mark; the handling of carried gifts, exchange rates and weak listings.

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/gift-pick.md](../testing/gift-pick.md)

# working-backwards-pitch

Status: tested and reviewed (two test rounds, two independent reviews, every rubric line at 4). Three small wording edits made after the second test round are untested; see the testing record. Version 0.1.0.

## What it does

Helps one person pitch an idea that does not exist yet to a senior decision-maker inside their own organisation (their CEO, a VP, a board, a sponsor), using the working-backwards method that Amazon made public: write the press release for the finished thing first, then answer the hard questions.

1. Checks the fit, then asks for what is missing in one short round: the idea, the decision-maker, what a yes would give, any real facts with their source, and why the author believes in it. If the person is away it asks nothing and works from stated assumptions.
2. Writes one short document (about 1,500 words):
   - a one-page summary that ends in a sized ask: cost, what the decision-maker gets, when they will know, and what happens either way. The first ask is the smallest time-boxed step that would produce real evidence;
   - a hypothetical future press release, labelled as hypothetical at its top and bottom, with an imagined date;
   - an FAQ of 6 to 10 questions, most of them the decision-maker's hard ones;
   - a red-team note: the three strongest objections with honest answers, and drop conditions that should make the author stop;
   - a to-validate list with the cheapest way to check each open claim.
3. Keeps to honesty rules throughout: no invented numbers, customers, partners or results; no quote from anyone but the author, in the author's own words and with their agreement; every unproven claim marked `[to validate]`; numbers it suggests for the design of the proposal marked `[proposed]`; no forecast of a result without a source.

## What comes from the public method and what is this skill's own

From the public descriptions of Amazon's method: starting from the people served and working back; the press release written as if the idea has launched; the "so what?" test; an FAQ that includes hard internal questions; keeping it short; expecting many drafts; and the view that an idea dropped on paper has done its job.

This skill's own additions, not part of Amazon's method: the honesty rules, the one-page summary with the sized ask, the red-team note with drop conditions, the shorter length limits, and the single round of questions. Amazon's press release format includes an imagined leader quote and an imagined customer testimonial; this skill leaves both out on purpose, because outside a company where everyone knows the format a mock press release can be mistaken for fact. A real, consented quote from someone other than the author is not supported either; the skill offers a counted, sourced result in its place (for example how many of the people asked said they would use it).

This skill is not affiliated with or endorsed by Amazon.

## How it differs from similar public skills

Several public PR/FAQ skills already exist, among them borghei/claude-skills "prfaq", robdefeo/agent-skills "amazon-working-backwards", punt-labs "prfaq", aj-geddes "bmad-prfaq", wdavidturner/product-skills "working-backwards" and amplitude/builder-skills "amazon-working-backwards". Only the directory listings of the first two were read, not the skills themselves, and the others were seen by name only, so this comparison is limited: on their listings they are product-development PR/FAQ generators in Amazon's fuller format. working-backwards-pitch is narrower on purpose: one person pitching upward, a shorter document, rules that stop the mock press release carrying invented facts, a small time-boxed ask, and drop conditions. Nothing was copied from those skills.

## Example

> I run support at a 60-person software company. I want our CEO to let me try a weekend callback service for customers who are stuck. I think it would cut cancellations but I have no data. Help me pitch it.

The skill asks one round of questions (who would staff it, any real figures, why she believes in it). She answers: two volunteers, 14 weekend tickets last month from the helpdesk report, no cancellation data. The reply, in outline:

- One-pager. Ask: approve a 6-week trial (a proposed length), two volunteers, Saturday callbacks, cost to be validated (overtime for two people on 6 Saturdays). Known: 14 weekend tickets last month. To validate: whether weekend waits lead to cancellations.
- Press release, labelled hypothetical top and bottom, with an imagined date. No satisfaction figures, no customer quote; her own sentence, word for word, as the quote, and she is asked to confirm she is happy to be quoted.
- FAQ, including "How do you know this reduces cancellations?" answered "We do not yet", with how the trial would find out.
- Red-team note. Objection: 14 tickets is too few to matter. Drop condition: fewer than a proposed number of callbacks requested over six weeks.
- To-validate list with the cheapest check for each item.

## Not for

A real press release or announcement of something that has happened or is launching, an investor pitch deck, slides, a sales pitch to a customer, a cover letter or job pitch, or questioning an idea from first principles (bedrock in this collection).

## Sources and credits

Public pages, read on 21 November 2026. Some were read through a summarising fetch tool, not verbatim. The two reviewers each fetched one of them again (S2 and S1) and checked the skill against it.

1. S1. Colin Bryar and Bill Carr, "Working Backwards: How to write an Amazon PR/FAQ", their own guide on coda.io (@colin-bryar/working-backwards-how-write-an-amazon-pr-faq). Bryar and Carr are former Amazon vice presidents and the authors of *Working Backwards* (St. Martin's Press, 2021). Used for: the press release written for the customer as if launched, the external and internal FAQ, common mistakes, many drafts.
2. S2. "An insider look at Amazon's culture and processes", aboutamazon.com, 9 February 2021, an excerpt from the Bryar and Carr book. Used for: the "so what?" test; press release under one page and FAQ of five pages or less; most PR/FAQs never becoming products.
3. S3. Werner Vogels, "Working Backwards", allthingsdistributed.com, 1 November 2006. Background on the method's origin; its user-manual step is not used.
4. S4. Richard Halkett and Rayford Davis (AWS), "Working Backwards: Amazon's approach to innovation", re:Invent 2020 session INO206, slides. Used for: the five customer questions; the press release parts (including the leader quote and customer testimonial this skill leaves out); FAQ topics such as what will disappoint customers and what was rejected.
5. S5. Cedric Chin, Commoncog, "Working Backwards" summary and "Product development as iterated taste". Independent commentary; used for the method's limits.

Background named but not consulted (search results only): Jeff Bezos's 2015 letter to Amazon shareholders (reversible "two-way door" decisions) and Gary Klein, "Performing a Project Premortem", Harvard Business Review, September 2007. The small reversible first ask and the red-team note are in their spirit, but neither text was read for this skill.

The method is Amazon's, as made public by the people above. The skill's wording, its additions and its example are original. No employer, client or confidential material was used.

## Testing

See the testing record: [testing/working-backwards-pitch.md](../testing/working-backwards-pitch.md).

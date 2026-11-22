# idea-triage

Status: tested and reviewed (two test rounds, two independent reviews, every rubric line at 4). Five small edits made after the second test round are untested; see the testing record. Version 0.1.0.

## What it does

Helps one person with more ideas of their own than time (side projects, small business ideas, things to write or build) decide which to pursue, test, park or drop.

1. Collects the list as it comes (pasted, a file, or one at a time), restates each idea in one plain line, and merges duplicates, saying which and why.
2. Agrees the yardstick before any scoring, in one message: the aim, the limits (hours, money), deal-breakers, what the person already knows (who has asked or paid, which idea pulls them), and three to five criteria with the person's own split of ten weight points.
3. Scores each idea 1 to 3 on each criterion. Every score carries a reason of a few words and a label: S (the person said it), L (looked up, source named) or G (a guess). Ideas that fail a deal-breaker are not scored.
4. Says how firm the order is: totals within two points are a tie, and a flip check names the smallest change that would put a different idea on top.
5. Gives each idea one verdict: do now (at most two), test cheaply (at most three), park (with a revisit date and a "sooner if"), or drop (kept on the list with the reason).
6. For each surviving idea, gives the cheapest next test, with its cost, a pass line fixed in advance and a date.

Rules it keeps throughout: the person owns the weights and the final call; a guess never passes as a fact; no market sizes, demand figures or prices are invented; it says so when one missing fact decides the order; nothing is deleted.

If the person is away it asks nothing: it states its assumptions, uses equal weights, gives no "do now" that rests on an assumed aim, still says plainly where to start, and ends with the questions that would most change the result. Without a search tool, checkable facts stay labelled as guesses and are listed as things to check.

## What comes from public methods and what is this skill's own

From public methods: weighted scoring against criteria (the decision matrix); the idea from RICE and ICE that confidence should temper a score, and Itamar Gilad's point that confidence should come from the kind of evidence held and not from feeling; the view of the RICE author that a score is a prompt and not a rule; kill criteria set in advance as "a state and a date" (Annie Duke); and the published criticisms of scoring: guesses multiplied by guesses, false precision, arithmetic on labels, minor criteria outvoting a must-have, and scores used as cover for a decision already made.

This skill's own choices, not taken from a source: scores of 1 to 3 and ten weight points; adding rather than multiplying; the evidence label kept beside each score instead of inside the total; deal-breakers as gates; the two-point tie band and the flip check; the caps on "do now" and on tests; the "Pull" criterion; a revisit date and "sooner if" for parked ideas; and keeping dropped ideas on a list.

It does not run RICE, ICE or opportunity scoring as such. Opportunity scoring needs survey data from many customers, which a person with a list of ideas rarely has.

## How it differs from similar public skills

Many public skills rank product features or a team backlog with RICE, ICE and similar methods, among them borghei/Claude-Skills "prioritization-frameworks" and whawkinsiv/claude-code-skills "prioritize" (the directory listing of each was read, not the skill itself), and, seen by name only, menkesu/awesome-pm-skills "prioritization-craft", alirezarezvani/claude-skills "rice", amplitude/builder-skills "prioritize", mohitagw15856/pm-claude-skills "rice-prioritisation", phuryn/pm-skills "prioritization-frameworks", yonatangross/orchestkit "prioritization-frameworks" and uxcel-lab/product-skills "pm-prioritization". So this comparison is limited. idea-triage is narrower on purpose: one person's mixed list of their own ideas, weights agreed before scoring, a fact-or-guess label on every score, capped verdicts with a kept parked list, and a cheapest next test. Nothing was copied from those skills.

## Example

> Rank my side-project ideas: (a) newsletter about local hiking trails, (b) trail-conditions app, (c) hiking blog, (d) selling my trail photos as prints. About 5 hours a week, I want some income within a year. Two friends keep asking me for trail tips. I write a bit already, I can't code, I have no online shop, and nobody has asked to buy a photo.

Tidy list: 1 Trail newsletter (merged with the blog, the same writing in another wrapper); 2 Trail-conditions app; 3 Photo prints. Weights agreed with the person: Wanted 4, Cheap to test 3, Fit 3.

| Idea | Wanted (4) | Cheap to test (3) | Fit (3) | Total |
|---|---|---|---|---|
| 1 Newsletter | 2, two friends ask, S | 3, one issue this week, G | 3, writes already, S | 26 |
| 3 Prints | 1, nobody has asked, S | 3, list five prints online, G | 2, has photos, no shop, S | 19 |
| 2 App | 1, no one has asked, G | 1, months to build, G | 1, cannot code, S | 10 |

Verdicts: the newsletter is "test cheaply", since two friends is thin evidence that it is wanted; the test is to send one issue to 20 hikers by a set date, with a proposed pass line. Prints are parked with a revisit date, sooner if someone asks to buy a photo. The app is parked, not dropped, because its low "wanted" is a guess. No "do now" yet.

## Not for

Examining one idea in depth or from first principles (bedrock in this collection), writing a pitch for one idea (working-backwards-pitch in this collection), coming up with new ideas, ranking a team's backlog, sprint or roadmap, ordering a to-do list, or choosing between options that are not the person's own ideas (job offers, purchases).

## Sources and credits

Public pages, read on 21 November 2026 through a summarising fetch tool, not verbatim. The two reviewers fetched five of the seven again (S1, S2, S3, S6, S7) and found nothing contradicted; S4 and S5 were not rechecked.

1. S1. Sean McBride, "RICE: Simple prioritization for product managers", Intercom blog, 5 January 2018. Used for: reach, impact, confidence and effort; coarse scales; the score is not a rule to follow strictly.
2. S2. Itamar Gilad, "Product Discovery With ICE and The Confidence Meter", itamargilad.com, 18 April 2018. Used for: ICE (which Gilad credits to Sean Ellis); confidence drawn from the kind of evidence; a high score on weak evidence means keep testing.
3. S3. Peter Hilton, "Product management arithmetic", hilton.org.uk, 31 January 2023. Used for: the faults of score arithmetic, including Janna Bastow's remark, quoted there, about multiplying an assumption by an assumption.
4. S4. Wikipedia, "Decision-matrix method". Used for: weighted scoring and its stated weaknesses (subjective criteria, minor criteria outweighing a must-have, false confidence).
5. S5. Wikipedia, "Outcome-Driven Innovation". Background on Anthony Ulwick's opportunity algorithm; the formula is not used.
6. S6. Coaching for Leaders, episode 607, "How to Quit Bad Stuff Faster, with Annie Duke" (episode page), on her book *Quit: The Power of Knowing When to Walk Away*. Used for: kill criteria set in advance, "a state and a date".
7. S7. Mike Goitein, "Why Prioritization Frameworks Are Band-Aids Covering A Problem They'll Never Solve", Product Strategy Decoded, 9 January 2026. Used for: scores as cover for a decision; the need for an aim before scoring.

Named but not consulted: Annie Duke's book itself, Ulwick's own writing, and Sean Ellis's own writing on ICE.

The skill's wording, its scales and caps, and its example are original. No employer, client or confidential material was used.

## Testing

See the testing record: [testing/idea-triage.md](../testing/idea-triage.md).

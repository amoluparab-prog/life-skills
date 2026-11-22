# offer-negotiator

Status: reviewed. Two test rounds and two independent reviews were run; at the final review every rubric line scored 4 or 5. Edits made after the second test round and after each review have not been run (see the testing record). Version 0.1.0.

## What it does

Helps a person who holds a job offer respond to it well. Given the offer as written, the role, level and place, and what matters to the person, the reply has:

1. A short version: what is solid, the biggest gap, the one to three things to ask for, the next step.
2. The offer in one table: base, bonus, equity or shares with vesting, sign-on, benefits, leave, place of work, start date, probation and notice, restrictive terms, deadline. Each row is marked Clear, Vague or Not stated, with what to ask.
3. Where the offer sits against published pay, from sources found during the conversation, each named with a link, what it measures, its date and how reliable it is. If no good match is found it says "I could not find reliable data" and lists what to check.
4. What the offer is worth under plain scenarios with the sums shown: a floor (guaranteed items only), as written, and equity at half and at double. Equity with no stated value is "value unknown".
5. What is commonly negotiable and what this person should ask for, from their own order of priorities.
6. Questions to ask before countering.
7. A counter-offer with reasons, as a short spoken script and an email draft.
8. Honest answers to likely replies ("this is our best offer", "what do you earn now?", "we need an answer by Friday").
9. A walk-away line that is the person's own, and what to do before accepting.

Rules it keeps throughout: it never gives market pay from memory; it never suggests misstating current pay, other offers or anything else, and declines to draft such a line when asked; equity is shown as scenarios that include nothing at all, never as a promise; it is not legal, tax or financial advice, and restrictive terms (non-compete, repayment, exclusivity, visa conditions) are quoted and flagged for an adviser; it does not state local employment rules from memory; the person's details are not put into searches or saved; it only drafts, the person sends, and the decision is theirs.

It is written for any country. It asks where the person is, keeps the offer's own currency and basis (per month or per year, before or after tax), and looks up local pay data and pay-range rules at the time.

## How it differs from similar public skills

Similar public skills exist. Listing pages read on 22 November 2026: "salary-negotiation-prep" (paramchoudhary/resumeskills, mirrored on several listing sites), which covers market research, strategy, scripts and total compensation; and "negotiating-offers" (refoundai), which gives coaching principles from three named podcast guests. Seen in search results only: "salary-negotiation" (mohitagw15856/pm-claude-skills) and "draft-offer" (anthropics/knowledge-work-plugins, the employer's side). This skill takes a narrower line: it works from the written offer; a pay figure appears only with a named source found in the conversation, or not at all; value is arithmetic under stated scenarios; it has fixed honesty rules; it assumes no country; and the walk-away line is never set for the person. Nothing was copied from those skills.

## Example

> I got an offer from Northwind Example Ltd for senior analyst in [city, country]: base 60,000, bonus up to 8%, 25 days leave, start in four weeks. The advert said 58,000 to 70,000. I care about base most, then leave. If it falls through I stay where I am, which I can live with. Help me negotiate.

(Northwind Example Ltd is an invented name.) The reply, in outline: "The base is clear and sits in the lower part of the posted range. The bonus is vague. Ask for 66,000 base (upper half of their range; provisional until you tell me your own figure), and ask how the bonus has paid out." Then a table that begins:

| Item | As written | Status | What to ask |
|---|---|---|---|
| Base | 60,000 | Clear | |
| Bonus | "up to 8%" | Vague | Is there a target? What was paid in the last two years? |
| Notice | | Not stated | What are the probation and notice periods? |

Then published pay (the advert's own range, rated high; one national statistic, rated low), the worth (floor 60,000; 60,000 + 4,800 = 64,800 if the maximum bonus were paid, which nothing promises), a script that begins "Thank you, I'm glad to have the offer and I'd like to make this work", an email draft, answers to likely replies, the question "What is the least this offer must be for you to prefer it? [your line]", and "final terms in writing before you accept".

## Not for

Running a job search (launchpad); a raise at a current job with no new offer; a clause-by-clause check of a contract or offer letter (agreement-check); comparing contractor quotes (quote-check); an employer deciding what to offer.

## Sources and credits

Public pages, read on 22 November 2026 through a summarising fetch tool, so the notes taken are paraphrase and not the pages' own words. Sources 2, 4 and 7 were fetched again by the first reviewer and matched.

1. Program on Negotiation at Harvard Law School, Katie Shonk, "Principled Negotiation: Focus on Interests to Create Value": https://www.pon.harvard.edu/daily/negotiation-skills-daily/principled-negotiation-focus-interests-create-value/ (the elements from Fisher, Ury and Patton, "Getting to Yes")
2. Program on Negotiation, Katie Shonk, "How to Negotiate Salary: 3 Winning Strategies": https://www.pon.harvard.edu/daily/salary-negotiations/negotiate-salary-3-winning-strategies/
3. Program on Negotiation staff, "How to Negotiate a Higher Salary": https://www.pon.harvard.edu/daily/salary-negotiations/negotiate-higher-salary/
4. Deepak Malhotra, "15 Rules for Negotiating a Job Offer", Harvard Business Review, April 2014; read in the copy posted by the University of Virginia Department of Economics: https://economics.virginia.edu/15-rules-negotiating-job-offer
5. Littler, "EU Pay Transparency Directive: early transposition trends" (30 October 2025): https://www.littler.com/news-analysis/asap/eu-pay-transparency-directive-early-transposition-trends-watch
6. Foley & Lardner, "Trends of pay transparency laws and salary history bans continue to grow" (18 May 2026): https://www.foley.com/insights/publications/2026/05/trends-of-pay-transparency-laws-and-salary-history-bans-continue-to-grow-new-laws-enacted-in-virginia-maine-and-delaware/
7. Carta, Peter Walker, "Five Questions to Negotiate Your Startup Equity Offer" (17 January 2026): https://carta.com/data/linkedin-startup-equity-negotiation-tips-january-hiring/
8. Underdog.io, "How to Evaluate Startup Equity Offers Without Getting Burned" (26 July 2026): https://underdog.io/blog/how-to-evaluate-startup-equity-offers

Not opened (the fetch was refused) and not used for any claim: the legal text of Directive (EU) 2023/970 on EUR-Lex, and the original of source 4 on hbr.org.

What the sources support: interests before positions, objective criteria, trading across issues and knowing your best alternative (1); gathering evidence, set ranges at large employers and arguing for the high end, more room at small ones, the pull of an opening figure (2, 3); a reason for every request, all asks together with their order of importance, knowing what is fixed and what flexes, honest answers to hard questions, no ultimatums, patience with delays (4); that some places require employers to tell applicants the pay range or forbid asking about past pay, and that such rules differ and change (5, 6, both law-firm summaries); the questions to ask about equity and valuing it by scenarios (7, 8).

The author's own judgement or general know-how, not taken from a source: the order of reliability for pay sources and the bar of two matching sources before saying where an offer sits; the three scenarios and spreading equity over the vesting period; one specific figure and not a range (source 2 describes citing a range when asked your price before an offer); never taking the counter figure from a rule-of-thumb percentage; a figure in the upper half of the employer's own range when the person gives none; "usually does not cost an offer, but it can" (source 4 says only that pushing too hard can lose one); not resigning until the final offer is in writing; never searching with the person's name or figures; the lists of what is commonly negotiable, what is usually fixed and the likely replies; that declining to share current pay is not misstating it; that pay follows published scales in some sectors and countries; questions first with a week or more; "then stop talking"; "a firm no usually reflects a limit on their side"; a bonus with no number counts as nothing; the two-offers lines; totals on the offer's own basis; the word aims and the cut-down form for a deadline hours away.

Limits of the sources: the negotiation sources are from the United States, and the equity sources use US start-up terms; the skill turns them into plain questions that apply anywhere and leaves tax to a professional. Pay-range rules are covered only for the European Union and three US states, as examples that such rules vary, which is why the skill looks them up each time.

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/offer-negotiator.md](../testing/offer-negotiator.md)

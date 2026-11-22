# claim-check

Status: reviewed. Three test rounds (ten runs) and three independent reviews; final scores Relevance 5, Trigger clarity 4, Correctness 4, Usability 4, Brevity 4, Provenance 4. The last few small edits are untested; see the testing record. Version 0.1.0.

## What it does

Gives a second pair of eyes on the facts in a finished draft before it goes out: a post, pitch, plan, application answer, script, web page or bio. It never edits the draft. It returns a report:

1. A first line with the date checked and a count for each verdict, then the one fix that matters most.
2. Every checkable claim, numbered, with its exact words: numbers, dates, names, titles, quotes, "first / only / largest" claims, cause-and-effect claims, and claims about what a source says.
3. A verdict for each, most serious first: wrong, misleading or out of date, unsupported, could not verify, confirmed. Each comes with what the source says, the source and a link, and wording the author can paste in place of the claim.
4. "Only you can confirm": claims about the author's own life, work or private facts, each with what to check it against. These are not looked up.
5. Opinions and predictions, labelled as such and not judged true or false.
6. Anything not reached, and the limits of the check.

Rules it keeps throughout: nothing is marked confirmed unless a source was opened in that session; it says "could not verify" instead of guessing; quotes are traced to the original, never to a quote site; conflicting sources are reported, not quietly resolved; only short phrases are quoted from sources; private details from the draft are kept out of web searches. Without web access it still lists and sorts every claim, confirms nothing, and says where the author can look.

## How it differs from similar public skills

Several public fact-check skills exist. One listing was read: daymade/claude-code-skills "fact-checker", which verifies claims in a document and then proposes corrections to apply to it, with examples that lean to technical documents. Others were seen in search results and not read, among them jamditis/claude-skills-journalism "fact-check-workflow", pedrohcgs "verify-claims", Jamie-BitFlight "fact-check", nickcrew "fact-checker" and AgriciDaniel "blog-factcheck". This one is narrower on purpose: a strictly report-only check for everyday authors of finished drafts. Its own ground is the rule that confirmed means a source was opened, the "only you can confirm" list, quotes traced to the original, wording ready to paste for each claim, and opinions and predictions labelled instead of judged. Nothing was copied from those skills.

## Example

> Fact-check this before I post it: "After all, 90% of small businesses fail in their first year, according to the US Bureau of Labor Statistics. But as Albert Einstein said, 'Insanity is doing the same thing over and over and expecting different results.' Today we employ 14 people. I think the next decade will be even better."

The reply, in outline (taken from a test run on 21 November 2026; sources can change):

> **Checked 21 November 2026. 5 claims: 2 wrong, 1 unsupported, 1 only you can confirm, 1 prediction.** The fix that matters most: the 90% figure is not what the Bureau reports.
>
> **Wrong.** C1 "90% of small businesses fail in their first year" and C2 "according to the US Bureau of Labor Statistics". The Bureau's own page on one-year survival of new business establishments shows most of them surviving the first year. Source: The Economics Daily, US Bureau of Labor Statistics, 4 March 2024. **Paste instead:** "After all, in a bad year more than a quarter of new businesses close within twelve months, according to the US Bureau of Labor Statistics."
>
> **Unsupported.** C3, the Einstein quote: a quote-tracing site found no evidence he said it; its earliest close match is from 1981. This is a careful secondary source, not the original. **Paste instead:** "But as the old saying goes, ..."
>
> **Only you can confirm.** C4 "we employ 14 people": your payroll today.
>
> **Opinions and predictions.** C5 "the next decade will be even better": your prediction, worded as one.

## Not for

Proofreading, grammar or style edits; open-ended research on a topic when there is no draft to check; checking code; testing the reasoning or assumptions behind an idea; reviewing the terms of a contract. It is not a professional fact-checking service, and a "confirmed" means only that one opened source said the same thing on the date shown.

## Sources and credits

The method draws on public writing about fact-checking, paraphrased, with no text copied at length:

- SIFT, "the four moves" (stop, investigate the source, find better coverage, trace claims and quotes to the original context), by Mike Caulfield. Read in the Open Oregon chapter "The SIFT Method", adapted from Introduction to College Research by Walter D. Butler, Aloha Sargent and Kelsey Smith, licensed CC BY 4.0. https://openoregon.pressbooks.pub/findinginfo/chapter/four-moves/
- Verification Handbook for Investigative Reporting, edited by Craig Silverman, European Journalism Centre: independent sources, original documents over summaries, dates first, recording what could not be verified. https://verificationhandbook.com/downloads/verification.handbook.2.pdf
- Duke University Libraries, "Who said that? Librarian tips for verifying quotes" (2023), tips from Arianne Hartsell-Gundy. https://blogs.library.duke.edu/blog/2023/06/28/who-said-that-librarian-tips-for-verifying-quotes/
- Full Fact, "How does the Full Fact team choose what to fact check?" (2025): opinions cannot be fact-checked; weigh harm when choosing what to check. https://fullfact.org/blog/2025/apr/how-does-the-full-fact-team-choose-what-to-fact-check/

These four were opened and read on 21 November 2026. Two others (PolitiFact's published principles and the jamditis skill page) could not be opened and were not relied on. The verdict labels, the "only you can confirm" list, the confirmed-means-opened rule and the no-web fallback are the author's own judgement, not taken from a source.

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/claim-check.md](../testing/claim-check.md)

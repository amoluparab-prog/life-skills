# launchpad

Status: tested and reviewed (two test rounds, two independent reviews, every rubric line at 4 or above). Version 0.1.0. Seven small wording clarifications made after the last test round have not been run; see the testing record.

## What it does

Helps a person run a job search as a small campaign with a weekly review, so they can see where it is stuck. It adds a warm path (people who know their work, then people with a shared tie) beside applying to posted roles; it does not replace applying.

1. **Positioning:** one or two sentences on the role they want and what they bring, with three proof points, each tied to a line in their resume or something they said.
2. **Audience:** one or two role types, 10 to 20 companies, and people ordered by warmth.
3. **Visibility:** a profile refresh (such as LinkedIn) to match the target role, checked against the resume, and one small piece of public proof of work.
4. **Warm reach:** short first messages, connection first, asking for advice and not for a job, with one follow-up.
5. **Conversion:** conversation prep, a same-day thank-you, a referral ask only when it has been earned, and applying alongside.
6. **Offer:** compare with what they said they wanted, look up pay, thank the people who helped.

A tracker table and a 30-minute weekly review hold it together. A first session ends with five things: the positioning, a tracker with its first rows, a new profile headline, two or three message drafts, and dated actions for the week.

Rules it keeps throughout: it drafts and the person sends everything; nothing about the person is invented, rounded up or upgraded; facts about people and companies are looked up or marked "to check"; no scraping and no automated messaging; no promised results and no reply-rate or "hidden jobs" figures. It can also do one stage on its own (for example only the profile refresh), set a search up for someone else with blanks for them to fill, or give everything in one go when the person cannot reply.

## How it differs from similar public skills

Other public job search skills exist, for example proficientlyjobs/proficiently-claude-skills (finding postings, tailoring documents and filling application forms with browser automation) and the "networking-outreach" skill in manojbajaj95/claude-gtm-plugin (finding people and drafting cold messages). launchpad is narrower in one way and wider in another: it sends and automates nothing, and it covers the whole search as one funnel with a tracker and a weekly review, warm contacts before cold ones, and an honesty check on every claim. Nothing was copied from those skills.

## Example

> I graduated in May with a biology degree and want a lab research job in Boston. I've sent 60 applications and heard nothing. Can you help me run this properly? (Resume pasted.)

The first reply, in outline: two lines on how this will work, then a positioning draft built from the resume with each proof point tied to a resume line, then one question: is this true, and does it sound like you? Over the next messages it asks who they already know and how many hours a week they have, then gives a tracker with those people in it, a new headline, two or three first messages of under 100 words each, and the week's actions with dates.

## Not for

A single document on its own (a cover letter for one posting, a resume typo or edit), an employer's hiring tasks such as writing a job description or preparing to interview a candidate (interview-kit in this collection), launching or marketing a product, interview practice or pay negotiation in depth, and sending or automating anything.

## What the evidence does and does not show

The skill tells people this plainly and goes no further:

- In one large US financial firm (data to 2011), referred candidates were about 6 percent of applicants and 29 percent of hires. The authors do not claim that a referral causes a hire (source 1).
- One recruiting-software vendor's customer data (2021 to 2024) shows about 40 percent of referred applicants reaching interview against about 3 percent of inbound applicants; agency and internal candidates did about as well as referrals. The same vendor reports that inbound applications remain the largest source of hires (source 2).
- A randomised experiment on LinkedIn found that moderately weak ties, measured by mutual connections, led to the most job moves. This held in more digital industries; in less digital ones strong ties helped more. LinkedIn users only (source 3).
- The often-quoted claim that around 80 percent of jobs are never advertised or are filled by networking could not be traced to a study by a university career office that looked (source 4).
- No reliable public figure was found for outreach reply rates, or for whether posting publicly helps a search. The skill promises neither.

## Sources and credits

Public pages, read on 21 November 2026 through a summarising fetch tool (not verbatim). Sources 1 to 4 and 6 were fetched again by both independent reviewers and checked against the skill; 5 and 7 by the first reviewer.

1. Brown, Setren and Topa, "Do Informal Referrals Lead to Better Matches?", Federal Reserve Bank of New York Staff Report 568: https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr568.html
2. Ashby, Talent Trends report on referrals (2025): https://www.ashbyhq.com/talent-trends-report/reports/referrals
3. Rajkumar and others, "A causal test of the strength of weak ties", Science, 2022: https://pubmed.ncbi.nlm.nih.gov/36107999/
4. UCF Career Services, "Is it true that 80% of job openings are not advertised?": https://career.ucf.edu/blog/2024/08/12/is-it-true-that-80-of-job-openings-are-not-advertised/
5. Steve Dalton, The 2-Hour Job Search, as presented in career services slides from Gies College of Business (the slides are the page read, not the book): https://publish.illinois.edu/giesonlineprogramscareerservices/files/2019/04/2HJS_BeyondBSchool_Part3_SLIDES-Reach-Out-by-Writing-and-Tracking-Simple-Effective-Outreach-Emails.pdf
6. Duke University Career Hub, "Informational Interviewing Guide": https://careerhub.students.duke.edu/resources/informational-interviewing-guide/
7. Prospects, "How to improve your LinkedIn profile": https://www.prospects.ac.uk/careers-advice/getting-a-job/how-to-improve-your-linkedin-profile/

Known but not read for this skill: Granovetter, "The Strength of Weak Ties" (1973), the origin of the weak-ties idea; LinkedIn's help pages on automation, which the fetch tool could not read, so the skill tells people to check the platform's current terms and states nothing about them.

The author's own judgement, not taken from a source: the six-stage funnel and its names; the tracker columns and stages; the five-item first session; one follow-up after about a week (source 5 says one, source 6 allows two); aim for under 100 words with 150 as the ceiling (source 5 says under 100, source 6 under 150); about five new messages a week; the "where is it stuck" checks in the weekly review; one small piece of public proof of work; asking how private the search must be when the person is employed; the rule against stating a platform's terms.

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/launchpad.md](../testing/launchpad.md)

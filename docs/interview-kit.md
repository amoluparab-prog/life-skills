# interview-kit

Status: tested and reviewed (two test rounds, two independent reviews, every rubric line at 4 or above). Version 0.1.0.

## What it does

Helps the person doing the interviewing, before and after one job interview.

**Before (Prepare).** From a role (a description or a few lines) and one candidate's resume it writes a structured interview guide:

1. The few competencies the role needs, sized to the slot (2 for 30 minutes, 3 or 4 for 45, 4 or 5 for 60), each tied to a line of the role text.
2. Core questions for each, one behavioural and one situational, written from the role and marked "same for every candidate".
3. Probes: standard neutral ones, plus probes that quote specific claims from this resume.
4. What a strong and a weak answer sound like.
5. A 1 to 4 rating scale with "not covered".
6. A time plan that adds up to the slot, and which question to drop first.
7. A check of every question, including the interviewer's own, for protected characteristics, with a job-related version to ask instead.

**After (Write up).** From the interviewer's raw notes it writes feedback: evidence per competency taken only from the notes, impressions and off-limits remarks set aside as "not used", a rating with reasons (the interviewer's, or a suggestion marked as such), concerns and gaps, and a recommendation line that stays the interviewer's. The skill organises evidence; it never gives or hints at a hire or no-hire call.

Rules it keeps throughout: the same core questions for every candidate for the role; no questions about protected characteristics; feedback rests on what the candidate said or did, not on "fit" or "energy"; nothing invented about the candidate; the resume and notes are treated as confidential (not saved, no online lookup of the candidate, no contact details repeated).

General guidance from public sources, not legal advice. The do-not-ask list is drawn from US and UK guidance; for other countries the skill applies it as it stands and says local rules were not checked.

## How it differs from similar public skills

Other public skills cover interview design, for example shawnpang/startup-founder-skills "interview-kit" (same name; designs a whole hiring process for a role: competency matrix, interview stages, take-home brief, scorecard, debrief) and w95/awesome-claude-corporate-skills "interview-kit-builder" (competency framework, questions, scorecards, interviewer training). This one is narrower on purpose: one interviewer, one candidate, one slot. Its own ground is the resume-tied probes on top of fixed core questions, the time plan, turning raw notes into evidence-based feedback, and the built-in question check. Nothing was copied from those skills.

## Example

> Interviewing Priya tomorrow, 45 minutes, for a support team lead. Role: lead 6 agents, own customer satisfaction, handle escalations. Her resume says she "raised CSAT from 82 to 91 in a year" and "coached 4 new hires". I also want to ask whether she has kids, because of the on-call weekends.

The reply, in outline: three competencies (leading a small team, handling escalations, improving service with data). A core question for each, the same for every candidate, such as "Tell me about a time you had to give hard feedback to someone on your team." A resume probe: "You raised CSAT from 82 to 91. What were the two changes that mattered most, and which were yours?" Strong and weak signs, the 1 to 4 scale, and a time plan: 5 minutes to open, three questions at 9 minutes each, 8 for her questions, 5 spare. Flagged: "Do you have kids?" must not be asked; ask every candidate "The role includes on-call one weekend a month. Can you do that?" instead.

## Not for

A candidate preparing for their own interview, writing a job description, running a job search (launchpad in this collection), screening or ranking a pile of resumes, designing a company's whole hiring process, or legal advice. It is also not meant for interviews that are not for hiring (user research, journalism, podcasts); the description does not yet say so.

## Sources and credits

Public pages, read on 21 November 2026 through a summarising fetch tool (not verbatim). Sources 1, 5, 7, 8 and 9 were fetched again by independent reviewers and checked against the skill.

1. US Office of Personnel Management, "Structured Interviews": https://www.opm.gov/policy-data-oversight/assessment-and-selection/other-assessment-methods/structured-interviews/
2. US Office of Personnel Management, "Structured Interviews: A Practical Guide": https://www.opm.gov/policy-data-oversight/assessment-and-selection/structured-interviews/structured-interviews.pdf
3. US Merit Systems Protection Board, "The Federal Selection Interview: Unrealized Potential": https://www.mspb.gov/studies/studies/The_Federal_Selection_Interview_Unrealized_Potential_253635.pdf
4. Google re:Work, "A guide to structured interviewing": https://rework.withgoogle.com/intl/en/guides/a-guide-to-structured-interviewing-for-better-hiring-practices
5. SIOP, "Is Cognitive Ability the Best Predictor of Job Performance?" (a summary of Sackett, Zhang, Berry and Lievens, 2022): https://www.siop.org/tip-article/is-cognitive-ability-the-best-predictor-of-job-performance
6. Criteria Corp, "Updates in employee selection science" (a vendor's reading of the same paper): https://www.criteriacorp.com/blog/updates-employee-selection-science
7. US EEOC, "What shouldn't I ask when hiring?": https://www.eeoc.gov/employers/small-business/what-shouldnt-i-ask-when-hiring
8. US EEOC, "Pre-Employment Inquiries and Medical Questions & Examinations": https://www.eeoc.gov/pre-employment-inquiries-and-medical-questions-examinations
9. GOV.UK, "Employers: preventing discrimination: Recruitment": https://www.gov.uk/employer-preventing-discrimination/recruitment
10. Acas, "Following discrimination law: Recruitment": https://www.acas.org.uk/hiring-someone/follow-discrimination-law
11. Levashina, Hartwell, Morgeson and Campion (2014), "The structured employment interview", Personnel Psychology 67(1). Abstract only was read: https://digitalcommons.usu.edu/manage_facpub/423/
12. US EEOC, "Enforcement Guidance: Preemployment Disability-Related Questions and Medical Examinations". Found and read by the second reviewer, not by the author; it is the US basis for allowing a question about adjustments for the interview itself: https://www.eeoc.gov/laws/guidance/enforcement-guidance-preemployment-disability-related-questions-and-medical

What the sources support: that structured interviews (same job-based questions, answers rated against written standards) on average predict job performance better and go with less adverse impact (1, 3, 5); question types, probes, notes, rating scales and rating before discussion (1, 2, 3, 4); the do-not-ask list (7, 8, 9, 10, 12). The skill quotes no validity figures.

Not from a source read by the author (general knowledge): that pay history and criminal record questions are restricted in some places. The skill only says "check local rules" for these.

The author's own judgement, not taken from a source: sizing competencies to the slot; a 4-point scale with no midpoint; about 8 to 10 minutes per question and the shares for opening, candidate questions and spare time; the 45-minute default; resume probes sitting under a core question and never replacing one; asking the behavioural question and holding the situational one as a fallback; the cautious choice not to ask why there is a gap in a resume; not looking the candidate up online; pointing to an off-limits remark by its place in the notes; labelled suggested ratings and never supplying the recommendation; the line about checking rules on AI tools in hiring.

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/interview-kit.md](../testing/interview-kit.md)

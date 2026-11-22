# meet-prep

Status: tested and reviewed (two test rounds, two independent reviews, every rubric line at 4 or above). The wording changes made after the second test round and after each review have not been rerun in tests. Version 0.1.0.

## What it does

Prepares one person for a meeting with one other person or a small group (about four at most): a new boss or senior leader, a stakeholder, a client, an investor, a mentor, a networking coffee. From who you are meeting, why, how long, and what you want out of it, it writes a brief of about one page:

1. The meeting, with any assumptions made.
2. Who they are in their professional role, each line labelled "(you said)", "(source: page, link, date read)" or "(unconfirmed)".
3. What they likely care about now, and how that is known (guesses are marked as guesses).
4. One outcome to aim for that they can agree to in the room, and a smaller fallback. If you want more than the meeting can give, it says so.
5. An opening line: one thank-you, why you are there, a check on the time.
6. Questions, best first: two for up to 20 minutes, three for up to 40, up to five for longer.
7. One concrete thing to offer.
8. Likely hard questions with short honest answers, with blanks where your facts are needed.
9. How to close.
10. A draft follow-up to send within a day. It never sends anything.

Rules it keeps:

- Professional, public information only. No home address, family, health, age, religion, politics, personal social media accounts (a professional profile is fine), or anything unrelated to the meeting, even when asked. Allegations and rumours are left out.
- A person who is not a public professional, or whom you are meeting for a personal reason, is never searched for; the brief uses only what you say.
- Nothing invented about anyone. A search result is used only when both the name and the organisation match; otherwise the match is called uncertain and left out.
- No flattery scripts, pressure tactics or pretended shared interests. If you have an interest the other person would want to know about, the opening says so.
- Confidential material is used only if you paste it, only in the brief, and never in a web search.
- Country-neutral: where the two sides are in different countries it looks up local meeting customs at the time and names the pages; it never guesses customs from a name or nationality.

With no web tool, or when nothing is found, it writes from your words and adds a short "To check yourself" list.

## How it differs from similar public skills

Many public skills prepare meeting briefs, for example anthropics/knowledge-work-plugins "meeting-briefing" (meetings with legal relevance, for in-house legal teams, from connected sources), KirKruglov/claude-skills-kit "meeting-prep-briefer" (a brief for each meeting in a day, from local files) and nimbleway/skills "meeting-prep" (researches attendees and companies with live web data). Others seen in a search listing but not opened: gleanwork "meeting-prep", brianrwagner "meeting-prep-cc", w95 "meeting-briefing", explorium-ai and gnekt "meeting-prep", borghei "calendar-prep", techwolf-ai "meeting-prep". This one is narrower on purpose: it needs no connectors, it is for any person and not a sales or legal team, and its own ground is the fixed limits on researching people, a brief built around one outcome and a fallback, honest answers with blanks in place of made-up facts, and no manipulation. Nothing was copied from those skills.

## Example (invented names)

> I'm meeting our new head of operations, Ilse Varga, tomorrow for 30 minutes. She asked to meet all team leads. I run the returns team at Brightwater Depot and I want her backing to trial weekend shifts.

The reply, in outline, with no web tool: who she is, from the user's words only, plus a "To check yourself" list (her bio on the intranet, the note announcing her arrival). Likely cares about learning who does what and where the problems are (marked as a guess). Outcome: she agrees to look at a one-page trial plan; fallback: she names who should see it first. Opening: "Thanks for making time. I run returns; I'd like to give you a two-minute picture, raise one idea for a trial, and hear what you most want from us. Is half an hour still right?" Three questions, starting with "What do you most want to change in your first three months?" A hard question, "What will weekend shifts cost?", answered with "About [your estimate] for a four-week trial; I will send the working by [day]." A close that says back who does what by when, and a draft thank-you with blanks.

## Not for

An interviewer preparing to interview a job candidate (interview-kit in this collection), a candidate preparing for their own job interview, writing a pitch document (working-backwards-pitch), a job-search campaign (launchpad), minutes after a meeting, a team meeting agenda, a personal meeting such as a date, or looking into someone's private life. Larger meetings and negotiating terms such as pay are outside what it was designed and tested for.

## Sources and credits

Public pages, read on 22 November 2026 through a summarising fetch tool (not verbatim). Sources 2, 4, 5 and 8 were fetched again by the first independent reviewer and sources 1, 7 and 9 by the second, also through a summarising tool, and checked against the skill. Sources 3 and 6 were read by the author only.

1. PRSA, "5 Questions to Ask Before Every Meeting": https://www.prsa.org/article/5-questions-to-ask-before-every-meeting
2. LinkedIn Learning blog, "What You Should Do When Meeting with a CEO": https://learning.linkedin.com/blog/advancing-your-career/what-you-should-do-when-meeting-with-a-ceo
3. Inc., Geoffrey James, "7 Rules for Meetings With Top Execs": https://www.inc.com/geoffrey-james/c-suite-advice-7-rules-for-meetings-with-top-execs.html
4. Stanford Alumni, "Build Your Network Through Career Conversations: What to Do Before, During and After": https://alumni.stanford.edu/career-connections/acing-the-career-conversation-what-to-do-before-during-and-after
5. Duke Career Hub, "Informational Interviewing Guide": https://careerhub.students.duke.edu/resources/informational-interviewing-guide/
6. UBC Student Services, "Informational interviews": https://students.ubc.ca/career/career-resources/informational-interviews/
7. Atlassian (Loom) blog, "How should an employee prepare for a skip-level meeting": https://www.atlassian.com/blog/loom/how-should-an-employee-prepare-for-a-skip-level-meeting
8. Holloway Guide to Venture Capital, "The First Meeting": https://www.holloway.com/g/venture-capital/sections/the-first-meeting
9. Cherie Blair Foundation for Women, "A Guide to Your First Mentoring Meeting": https://cherieblairfoundation.org/wp-content/uploads/2025/02/A-Guide-to-Your-First-Mentoring-Meeting.pdf

What the sources support: starting from the purpose and what you want (1, 4, 7); one objective said early and a next step agreed before the end (2, 3, 8); learning what the other person needs to get done and asking about it (1, 3); few questions ranked most important first (4); a single thank-you and no apology for their time (2); bringing something useful (3, 4); preparing for objections (1, 8); keeping time (2, 5); a thank-you within a day or two that names what helped and the agreed actions (4, 5, 7, 9); and the notes by kind of meeting (3, 5, 6, 7, 8, 9).

Where the skill departs from them on purpose: sources 2 and 4 suggest researching shared interests for small talk and source 3 an executive's personal agenda; the skill keeps to the public professional role and allows a shared thing only if it is true and about work. Source 4 suggests five to seven questions and 24 to 48 hours; the skill says five or fewer and within a day. Source 2 says to move to the ask with ten minutes left; the skill's "about five minutes, or two in a short call" is the author's figure.

The author's own judgement, not taken from a source: every limit on researching a person (public professional role only, private individuals from the user's words only, name plus organisation to accept a match, no allegations, no searches on confidential names or text); the source labels and the "To check yourself" list; sizing questions to the slot; the fallback outcome; blanks in square brackets; "I don't know yet; I will tell you by [day]"; saying a competing or money interest up front; the size of "one page"; looking up local customs at use time (no page on any country's customs is a source of the skill); small-group handling; and, in the skip-level note, "do not criticise people", "raise issues as problems with a suggested fix" and "telling your manager you are meeting is usually wise" (source 7 supports only being diplomatic and not appearing to go round your manager).

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/meet-prep.md](../testing/meet-prep.md)

# learn-plan

Status: **draft: review open** (Usability scored 3 of 5 at the third and last review; the two fixes it asked for are in the text but are unreviewed, and no wording changed since the second test round has been rerun). Final scores: Relevance 5, Trigger clarity 4, Correctness 4, Usability 3, Brevity 4, Provenance 4. Two test rounds (seven fresh-session runs, all passed) and three independent reviews; an extra test round that was allowed before the third review was not run. Version 0.1.0.

## What it does

Turns "I want to learn X by date Y with Z minutes a day" into a plan a person in any country can follow alone: a language for a trip, an instrument, spreadsheets, cooking, a programming language, public speaking, a hobby.

1. Takes what the request says, then asks once, at most four short questions, for what is missing: what they want to be able to do, by when, how much time, where they start from, how they like to learn, budget and country. If the person is away it asks nothing and states its assumptions.
2. Shows the hours as a sum, restates the goal as something that can be tested, and says plainly what that many hours will not reach.
3. Names the three to five sub-skills the goal depends on, and what to leave out.
4. Gives a week-by-week plan. Every session starts with recall from memory, adds one small new thing, and spends about half its time on practice with feedback; earlier material comes back after a gap and is mixed in once the basics are there; the last days rehearse the goal itself.
5. Gives a main and a backup resource per stage, each opened in the session and marked "checked today", or marked "unchecked".
6. Sets a short weekly check with a number as the pass mark, and says what to do when it is missed.
7. Says what to do after missed sessions, without doubling up.
8. Sets a review point about halfway.

Rules it keeps: no promise of fluency, mastery or any result; no invented course, book, app or teacher, and at most two names from memory per plan, each marked unchecked; free options first, plain links, nothing bought or booked; where a mistake can injure, the risky parts go to a qualified instructor in person and the skill gives no technique for them; a child's plan is written to the parent and kept light; where a qualification, permit or inspection may be required, it is looked up for the person's place or marked "to confirm", and no way round is offered; anything the person says makes learning harder changes the format, with no condition named or guessed; practice yes, graded coursework or live exams no; no country is the default.

Without a web search tool it says so near the top, gives the whole plan, and describes resources by kind with the words to search for.

## Example

> I'm going to Italy in 30 days. I can do 20 minutes a day. Never learned any Italian. I'd like to get by in restaurants and shops. I don't want to pay for anything. Just send me the plan.

The reply, in outline, from a session with no search tool: one line saying nothing was looked up. The goal: by day 30, order a meal and buy something in a shop, aloud, with a patient speaker, without a phone. The sum: 26 practice days x 20 minutes = about 8.7 hours, enough for set phrases said clearly, not for following fast replies; "a realistic target, not a promise". Five things that matter (sounds, about 20 phrases, numbers and prices, about 60 words, two repair phrases) and what to leave out. A four-week table with a practice task, a cold check and a pass mark per week (week 1: 10 prices and 8 phrases, pass 15 of 18). Resources by kind with search words, all unchecked. What to do after one, a few, or a week of missed sessions. A review on day 15. No course, app or book is named.

## How it differs from similar public skills

Similar public skills exist, seen in a web search on 22 November 2026: a "Learning Path Creator" (jmsktm/claude-settings) and a "learning-coach" (sunnypatneedi/claude-starter-kit), whose listing pages were read through a summarising tool (not their source), and several seen by title only (studykit, memory-retrieval-learning, study-habits, learning-method-coach, learn-with-claude, learning-gap-analyzer, study, teach). learn-plan takes a narrower, stated angle: a fixed time and a goal that can be tested; the hours sum shown; resources checked in the session or marked unchecked; a weekly self-check with a pass mark; a missed-sessions rule; fixed rules for physical risk, children, licences and stated needs; country-neutral. Nothing was copied from those skills.

## Not for

A child's long-term dream or career route (dream-pathway in this collection); a job search (launchpad); planning this week's time (week-plan); explaining one concept; a fitness, weight or diet programme; doing coursework or exams for someone.

## Sources and credits

Public pages, read on 22 November 2026 through a fetch tool that returns a summary of the page, not its full text. The papers themselves were not read.

1. Dunlosky, Rawson, Marsh, Nathan and Willingham (2013), "Improving Students' Learning With Effective Learning Techniques", Psychological Science in the Public Interest: the abstract on the Association for Psychological Science's journal page. https://www.psychologicalscience.org/journals/pspi/1529100612453266/
2. Association for Psychological Science, news release on the same paper, "Which Study Strategies Make the Grade?": https://www.psychologicalscience.org/news/releases/which-study-strategies-make-the-grade.html
3. Wikipedia, "Testing effect" (secondary): https://en.wikipedia.org/wiki/Testing_effect
4. Wikipedia, "Distributed practice" (secondary; the article is flagged as needing citations): https://en.wikipedia.org/wiki/Distributed_practice
5. Wikipedia, "Varied practice" (secondary): https://en.wikipedia.org/wiki/Varied_practice
6. Wikipedia, "Practice (learning method)" (secondary), for Ericsson's deliberate practice and the Macnamara, Hambrick and Oswald (2014) meta-analysis: https://en.wikipedia.org/wiki/Practice_(learning_method)

Not read: the Learning Scientists' materials (the fetch needed an approval nobody was present to give), the Cepeda et al. work on spacing gaps, and every original paper.

What these sources supply: recall from memory and practice spread over time were rated highest, and rereading and highlighting low (1, 2); recall works better with feedback, and producing an answer gains more than picking one (3); mixing items helps later performance, with limited evidence and less benefit for complex tasks and mixed results in children (1, 5); practice on a defined task with a clear goal and feedback, and the finding that practice explains only part of how well people do (6). Source 4 is not relied on alone for anything in the skill.

The author's own judgement, not taken from a source: the essentials and the four-question cap; the hours sum; three to five sub-skills and the leave-out list; the session shape and its proportions; the revisit rhythm of next day, a few days, about a week; treating watching and reading as input; no new material in the last days; pass marks and what to do under them; the missed-sessions rules; the review point; and every rule on resources, physical risk, children, licences and stated needs.

## Testing record

See [testing/learn-plan.md](../testing/learn-plan.md).

Part of the collection at https://github.com/amoluparab-prog/life-skills . MIT licence, copyright Amol Parab.

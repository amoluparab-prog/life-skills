---
name: video-to-actions
description: "Turns a video, podcast or talk the person has watched or heard into things they can act on, working only from its real transcript, captions or the person's own notes. Gives the few real takeaways in the speaker's order of importance with where each came from (timestamp when there is one), a short list of concrete actions fitted to the person's own situation, what to skip, the speaker's claims that are unchecked or contested (labelled, never passed on as fact), and a first step for today. Use when the user says things like 'I watched this video, what should I actually do', 'turn this talk into an action plan', 'pull the action items from this podcast for my situation', 'what should I take from this lecture', or shares a video link or transcript and asks what to do with it. Not for making or editing a video, summarising a written article, minutes or action items from a work meeting, transcription as the end product, researching a topic across many sources, or turning a video into a Claude skill."
---

# Video to actions

People watch a talk, feel they learned something, and do nothing with it. This skill turns one video, podcast or talk into a short list of things this person can do, and keeps the speaker's claims separate from facts. Handle one video per answer.

## 1. Get the words first

Everything below depends on what was actually said, so settle this before anything else.

- **The person pasted a transcript, captions or their own notes:** use that. Go to step 2.
- **The person gave only a link:** try, in this order, whatever this session has: a transcript or captions tool; a web fetch of the link; a search for a transcript the publisher put out (many talks and podcasts have one on their own site or in the show notes). If the fetch gave you no title or channel to search on, skip the search and ask. Then check what came back. A fetch of a video page usually returns the title, description and comments, not the spoken words. Count it as a transcript only if it is the running text of what was said, and only if you can tell it is this video. Do not work out which video a link is from memory in order to search for it; a wrong match gives the wrong talk's words.
- **Do not download the video or audio,** and do not run downloader tools. A transcript is enough, and the person can always supply one.
- **Nothing usable came back, the tool was blocked, or there are no such tools:** say so plainly in a sentence and ask for the words. Do not describe the video from its title, description, comments, or what you remember of the speaker or of this talk; that is a guess, and the person would act on it. Give the quickest way to get them:
  - YouTube on a computer: open the description under the video ("...more"), click "Show transcript", select the text and paste it here with the timestamps left in. On a phone, open the desktop site in the browser. If there is no "Show transcript" button, the creator has turned it off.
  - Podcasts: look for a transcript on the show's own site or in the episode notes. Some podcast apps let you copy only a little at a time.
  - Or their own notes, however rough. Notes are a fine source; the answer will just be limited to what they noted.
- **Only a second-hand summary can be found** (a blog post or review about the video): it is not the video. Say that this is all you found and ask whether to work from it; if you do, label the whole answer as based on someone else's summary.

Without the words there is nothing to act on, so even if the person is away, ask and stop here.

Read all of it. If the transcript is cut off or you could only get part, say which part the answer covers.

## 2. Know the person's situation

Actions only help if they fit, so you need what the person is trying to do and any limits (time, money, role, where they are starting from). Take it from their message if it is there. If it is missing, ask once, in one short message, and put it in the same message as any request for the transcript so they are asked only once.

If the person is away or cannot answer, do not stall: give general actions, label them "general, not fitted to you", and say what to tell you to get fitted ones.

## 3. Write the answer

Keep every item to a line or two. Use these parts, in this order. If it runs long, shorten the skip and claims lists before the actions.

**Source line.** One line saying what you worked from: full transcript, automatic captions, part of a transcript, a second-hand summary, or the person's notes. Text with no punctuation or capitals is usually automatic captions; say so alongside whether it is complete. They mishear names, numbers and small words like "not", so if a point rests on one of those, say you are unsure of it. Call the speaker by name or "the speaker"; do not guess more about them than the source says.

**Takeaways (3 to 5; up to 7 only for a long talk).** The points that carry the talk, most important first. "Most important" means the speaker's own weighting, not running order and not your view: what they call the main point, what they repeat, what they spend the most time on, what they come back to at the end. Fold a closing "try it for a month" into the takeaway it belongs to. For each one:
- say it in your own words, in one or two sentences, worded as the speaker's view ("the speaker argues", "Ortiz's advice is");
- give where it came from: the timestamp if the source has them (for example 12:40), otherwise a rough place (early, middle, near the end) if the source shows the order. Never invent a timestamp or a place; if the source has none, say so once;
- quote at most a few words. No long passages from the video, because the transcript belongs to its maker and the person does not need it repeated.

**Actions for you (3 to 5).** Each one:
- follows from one of the takeaways and fits the person's situation and limits;
- is concrete enough to start without another question: what to do, and when or where it happens. An "if or when X, then I will Y" form works well, because plans tied to a moment get done more often than good intentions;
- says whether it is the speaker's own suggestion or your adaptation of it for this person. An adaptation may reshape the speaker's advice to fit their limits; it may not bring in advice from elsewhere.

Do not add actions the video does not support. If the video gives this person little to act on, say that instead of padding the list.

**Skip.** The parts not worth their time and why: advice that does not fit their situation or limits, repeated points, long stories, sponsor reads. If they have not watched it all yet, this tells them what to jump past.

**Claims to treat with care.** List the factual claims the talk leans on, six at most: statistics, "studies show", cause and effect, promised results, history. Put first the ones your actions depend on and any about health, law or money. If an action rests on a claim you could not check, keep the action and say so beside it. Word every one as the speaker's ("he says that..."). Label each:
- *not checked* (the default);
- *checked, supported*, *checked, partly supported*, *checked, contested* or *checked, could not find it*, with a link to the source and a line on what it says, but only if you opened a source in this session. A list of search results is not a check. *Could not find it* means you opened the source the speaker named, or the obvious one, and the claim is not there. A page that would not load, or a finding you cannot tie to the speaker's claim, leaves it *not checked*; say what you found. With a search tool, check at most about three, starting with the ones your actions depend on. Never label from memory alone.

A claim being in the video is not evidence for it. Nowhere in the answer should a speaker's number or finding appear in your own voice as a fact.

**Medical, legal or money claims.** Flag them in the claims list and do not turn them into advice. No action may tell the person to take, stop or change a medicine, diet or treatment, to buy or sell an investment, or to take a legal step. For those, the furthest an action goes is "check this with a doctor, lawyer or licensed adviser before acting" or "read the original source". This holds even when the whole video is about health, law or money; then the actions are about what to learn, what to ask, and what to find out about their own position. Everyday steps the speaker suggests that are easy to undo, such as setting money aside in their own savings account, keeping a budget or looking up their own figures, are fine as actions.

**First step for today.** End with one, in a line: something that takes under 15 minutes and starts the first action.

## When not to use this

Making or editing a video. Summarising a written article. Minutes or action items from a work meeting. A transcript as the end product. Checking whether a topic is true across many sources (that is research; this skill only labels the claims of one video). Turning a video into a Claude skill. If the person only wants a plain summary of a video, give the source line, takeaways and claims, and offer the actions.

## Worked example

User: "Watched Maya Ortiz's 40 minute talk on getting freelance clients. Transcript below. I'm a part-time illustrator, about five hours a week for finding work, no budget for ads. What should I actually do?" (transcript with timestamps pasted)

Reply, in outline:

> **Worked from:** the full transcript you pasted (it reads like automatic captions, so names may be off).
>
> **Takeaways**
> 1. Ortiz's main point: past clients are the cheapest source of new work, and most freelancers never go back to them (18:05, repeated at 37:30).
> 2. Ortiz advises showing one kind of work, not everything you can do (06:40).
> 3. Ortiz suggests a fixed weekly slot for outreach over bursts when work dries up (24:10).
>
> **Actions for you**
> 1. When you sit down on Sunday evening, message two past clients with one recent piece and one question. Ortiz's suggestion, cut down to fit five hours a week.
> 2. This week, pick the eight pieces that show the work you want more of and hide the rest of your portfolio. My adaptation.
> 3. Put a 90 minute "find work" block in your calendar at the same time every week and treat it as booked. Ortiz's suggestion.
>
> **Skip:** 28:00 to 35:00 on paid ads (you have no ad budget) and the sponsor read at 12:15.
>
> **Claims to treat with care**
> - Ortiz says "80% of freelance work comes from referrals". Not checked; no source is given in the talk.
> - Ortiz says setting up a company "saves you tax from day one". Money and legal claim; depends on your country and income. Ask an accountant before acting.
>
> **First step today:** list every client you have ever had. Ten minutes.

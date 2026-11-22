# video-to-actions

Status: tested and reviewed (two test rounds, one independent review, every rubric line at 4). Wording edits made after the last test round and after the review were checked by the author only and have not been rerun; see the testing record. Version 0.1.0.

## What it does

Turns one video, podcast or talk a person has watched into things they can act on, working only from what was actually said.

1. Gets the words first: a transcript, captions or the person's own notes that they paste, or, from a link, whatever a transcript tool, a page fetch or the publisher's own transcript can supply. It does not download video or audio. If it cannot get the words it says so and asks for them, with the quickest way to copy a transcript. It never describes a video from its title, description or memory.
2. Finds out the person's situation, asking once if it is missing. If the person is away it gives general actions and labels them as general.
3. Writes a short answer in fixed parts:
   - a source line (full transcript, automatic captions, part of one, a second-hand summary, or notes);
   - 3 to 5 takeaways in the speaker's own order of importance, each in fresh words with a timestamp or rough place, never an invented one;
   - 3 to 5 concrete actions fitted to the person, each marked as the speaker's suggestion or an adaptation;
   - what to skip;
   - the claims the talk leans on, worded as the speaker's and labelled "not checked" unless a source was opened in the session;
   - a first step for today.

Rules it keeps: a speaker's number or finding never appears as fact; only a few words are ever quoted; medical, legal and money claims are flagged and not turned into advice (no action tells anyone to change a medicine or diet, buy or sell an investment, or take a legal step).

## How it differs from similar public skills

Many public skills fetch YouTube transcripts and summarise them, for example "youtube-wisdom" in sammcj/agentic-coding (subtitles through yt-dlp, then insights and quotes) and "youtube-analysis" by mathews-tom (scripts on youtube-transcript-api, then concept summaries). Only their listing pages were read. video-to-actions is narrower: no scripts or downloader, any source of the words including the person's own notes, actions fitted to one person's situation, claims kept apart from facts, and a refusal to guess when there is no transcript. Nothing was copied from those skills.

## Example

> Watched Maya Ortiz's 40 minute talk on getting freelance clients. Transcript below. I'm a part-time illustrator, about five hours a week for finding work, no budget for ads. What should I actually do?

The reply, in outline: a source line (the pasted transcript, probably automatic captions). Three takeaways, the main one first: past clients are the cheapest source of new work (18:05, repeated at 37:30). Three actions, such as "When you sit down on Sunday evening, message two past clients with one recent piece and one question", marked as Ortiz's suggestion cut down to five hours a week. Skip: the section on paid ads and the sponsor read. Claims: "80% of freelance work comes from referrals", not checked; setting up a company "saves you tax from day one", a money and legal claim to take to an accountant. A ten-minute first step for today.

## Not for

Making or editing a video. Summarising a written article. Minutes or action items from a work meeting. A transcript as the end product. Researching whether a topic is true across many sources. Turning a video into a Claude skill.

## Sources and credits

Public pages, read on 21 November 2026 through a summarising fetch tool (not verbatim). The reviewer opened sources 1, 2, 3 and 6 again and found them to match.

1. TechSmith, "How to Get a Transcript of a YouTube Video", published 5 Sep 2025, modified 24 Sep 2026: https://www.techsmith.com/blog/get-transcript-of-youtube-video/
2. YouTube Help, "Use automatic captioning": https://support.google.com/youtube/answer/6373554?hl=en
3. Apple Podcasts for Creators, "Transcripts on Apple Podcasts": https://podcasters.apple.com/support/5316-transcripts-on-apple-podcasts
4. University of Waterloo, Min Huang, "5 steps to improve your notes with the Cornell method", updated 18 Mar 2026: https://uwaterloo.ca/student-success/blog/5-steps-improve-your-notes-cornell-method
5. Pathways to College Success (CWI), chapter "Note-taking", CC BY 4.0: https://cwi.pressbooks.pub/pathwaystocollegesuccess/chapter/note-taking/
6. Wieber, Thürmer and Gollwitzer (2015), "Promoting the translation of intentions into action by implementation intentions: behavioral effects and physiological correlates", Frontiers in Human Neuroscience 9:395 (first half of the page read): https://pmc.ncbi.nlm.nih.gov/articles/PMC4500900
7. skills.sh listing of "youtube-wisdom" (listing page only): https://skills.sh/sammcj/agentic-coding/youtube-wisdom
8. skills.sh listing of "youtube-analysis" (listing page only): https://skills.sh/mathews-tom/praxis-skills/youtube-analysis

What each gave: 1, the steps to copy a YouTube transcript; 2, why automatic captions go wrong or are missing; 3, how podcast transcripts are made and the copy limit in one app; 4 and 5, main ideas before detail and fresh words over verbatim; 6, plans tied to a moment ("if X, then I will Y") are acted on more often than bare intentions; 7 and 8, what already exists.

The author's own judgement, not taken from a source: the signals for the speaker's order of importance (stated main point, repetition, time spent, the close); the counts of takeaways, actions and claims; the source line; the claim labels and the limit of about three checks; "no punctuation usually means automatic captions"; the under-15-minute first step; how to treat a second-hand summary; the limit on quotes; allowing easy-to-undo everyday money steps as actions. The rules on medical, legal and money content, on not guessing and on not downloading came with the request for the skill.

## Testing record

See [testing/video-to-actions.md](../testing/video-to-actions.md).

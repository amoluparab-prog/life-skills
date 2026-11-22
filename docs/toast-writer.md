# toast-writer

Status: tested in two rounds and reviewed twice (all six review lines at 4 or 5). Small edits made after the last test round have not been rerun; see the testing record. Version 0.1.0.

## What it does

Helps one person write and deliver a short spoken tribute to someone they know: a wedding toast or speech, a birthday or anniversary speech, a farewell, a retirement, a eulogy, a thank-you to a person at an event.

It collects the real material first, in at most three short questions per message and at most two rounds: who it is for, how the speaker knows them, who will be in the room, the time allowed, the tone, and two or three true stories. Then it gives:

1. Assumptions and flags: what it assumed, and any story it softened or left out, with the reason.
2. The speech, sized to the time at about 130 spoken words a minute in English (about 110 for a eulogy), with the word count. The time is treated as a ceiling and the speech is never padded to fill it.
3. A speaking copy: the same words, one thought per line, marked for short and long pauses, where to look up, where to wait for a laugh, and the word to lean on.
4. A 20-second version of about 40 words, for when time is cut or nerves win.
5. Delivery notes: numbered cards in large type in place of a phone, first and last lines by heart, reading it aloud and timing it, what to do if emotion comes.
6. A "To check" list: blanks to fill, customs to confirm with the hosts, names to pronounce.

Rules it keeps:

- It invents nothing. No story, quote, date or feeling the speaker did not give. Missing material becomes a marked blank for the speaker to fill.
- It does not look up the people named.
- No jokes about a body, age, weight or looks, about past partners, or about anything the person would not want said in front of that audience. A risky story is flagged with the reason and a safer telling or a cut is offered.
- Inside jokes are explained in one line or cut.
- No song lyrics, hymns or poems written out and no famous quotations supplied. A reading gets a timed slot; the speaker chooses it and reads it.
- Customs are the speaker's to describe. With a web tool it looks up who usually speaks and in what order for the place and tradition named, and names the pages; without one it lists questions for the hosts. It never guesses customs from a name or a country.
- Alcohol is optional: the close works with any drink or none.
- A eulogy gets a gentle pace, no forced humour, and a close with words to the person.
- If the user is away or says "just write it", it asks nothing, writes everything on stated assumptions, and leaves flagged stories out by default.

## How it differs from similar public skills

A quick search on 22 November 2026 found several general speech-writing skills for Claude that cover keynotes, business presentations, commencement speeches and wedding toasts together, and at least one wedding-speech skill. One listing page was opened; the others were seen only in search results. This skill is narrower on purpose: personal tributes only, built only from the speaker's own true material, with a screening step for risky stories, a speaking copy and a 20-second version as fixed outputs, separate care for eulogies, and no country as the default. Nothing was copied from those skills.

## Example (invented names)

> Write a farewell speech for my colleague Tovin Marlesh, here are some stories. He's leaving after 9 years. I'm Ressa, I've sat next to him for 6. Friday, about 30 of us from three floors in the office kitchen, managers included, 2 minutes. He labels everything, even the stapler. When I started he stayed till 8 pm three nights to help me pass my licence exam. I passed, and he never brought it up again. Also he once fell asleep in a client meeting after a big night out, ha.

The reply, in outline: no questions, because everything needed is there. The client-meeting story is left out of the draft (a drinking story with managers in the room) and a safer telling is offered. The speech runs about 240 words: who Ressa is, the labelled stapler, the three late nights and what they showed, a blank for what that meant to her in her own words, a wish, and "please join me in thanking Tovin. To Tovin." Then the speaking copy, a 20-second version ("I'm Ressa, and I have sat next to Tovin for six years. When I started, he stayed late three nights to get me through my exam, and never brought it up again. That is who we are losing. Tovin, thank you. To Tovin."), delivery notes for a kitchen with no microphone, and one thing to check: whether drinks are being served.

## Not for

A business presentation, work update, pitch or keynote; a political or campaign speech; a message that will only be written (a card, a gift note, a post; gift-pick in this collection writes a card line); wedding vows or an officiant's script; planning the event (host-plan); the steps of a religious ceremony (ritual-guide). Not tested for speeches over five minutes, languages other than English, an MC's running script or an award acceptance speech.

## Sources and credits

Public pages, read on 22 November 2026 through a summarising fetch tool (not verbatim). The two independent reviewers opened all seven again and checked them against the skill.

1. Toastmasters International, "How to Give a Toast": https://www.toastmasters.org/resources/public-speaking-tips/how-to-give-a-toast
2. Toastmasters magazine, December 2022, "Tips for Toasting": https://www.toastmasters.org/magazine/magazine-issues/2022/dec/tips-for-toasting
3. Toastmasters International, "How to Write a Eulogy": https://www.toastmasters.org/resources/public-speaking-tips/how-to-write-a-eulogy
4. What's Your Grief, "Writing and Giving a Eulogy": https://whatsyourgrief.com/writing-and-delivering-a-eulogy/
5. The Knot, wedding toast tips and mistakes: https://www.theknot.com/content/wedding-toast-tips-mistakes
6. Grammarly blog, on writing a wedding toast: https://www.grammarly.com/blog/writing-tips/wedding-toast/
7. University of Minnesota Libraries, "Communication in Practice", chapter "Vocal delivery": https://open.lib.umn.edu/commpractice/chapter/vocal-delivery/

Two further pages (one on average speaking rates, one on eulogies) could not be opened and were not used.

What the sources support: keeping it short, two to three minutes for a toast (1, 2) and under about five for a wedding speech (5, 6); eulogy lengths and following the family and the person leading the service (3, 4); saying who you are (1, 2, 3, 5, 6); one or two specific stories that show the person (1, 3, 4, 6); the focus on the person and not the speaker (3, 6); no inside jokes, no roast, nothing embarrassing (1, 3, 5, 6); no past partners and no swearing (5, 6); trying a doubtful story on someone close first (4); a clear close and a short toast line (1, 2, 5); plain conversational wording (1, 3, 4); writing it out and timing it (4, 5); waiting for the room, slowing down, pausing, looking up (1, 2, 5, 7); not drinking for courage (6); for a eulogy, humour only as fond remembrance, tears needing no apology, water and a tissue, and someone who can read it for you (3, 4); and 125 to 150 words a minute as the usual speaking range, with nerves speeding people up (7).

Where the skill departs from them on purpose: source 3 suggests a poem or song passage as a eulogy close, while the skill leaves a slot and never writes out such texts; source 1 prefers bullet-point cards and sources 4 and 5 a full script, and the skill gives a full text laid out on cards; source 7 suggests dividing by 150, and the skill uses 130.

The author's own judgement, not taken from a source: 130 words a minute (110 for a eulogy) and treating the time as a ceiling; the default lengths when no time is given; the four fixed outputs and the mark-up signs; the 20-second version; cards over a phone and the phone settings; first and last lines by heart; reading aloud three times; the list of topics always flagged and the "oldest and youngest listener" test; marked blanks and never filling them; the limits on questions; not looking up the people named; alcohol being optional; looking up customs at use time (no page on any country's customs is a source of the skill); the roast rule; leaving out vows and officiant scripts.

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/toast-writer.md](../testing/toast-writer.md)

# event-outfit

Status: tested and reviewed (two test rounds, two independent reviews, every rubric line at 4 or above). Version 0.1.0.

## What it does

Helps a person decide what to wear to a specific event, and what to pack when the event runs over several days, starting from the clothes they already own.

1. Asks for the facts in one short batch: the event and their role, the dress code as worded, venue, city and dates, the schedule, what they own, fit and comfort preferences, anything cultural or religious to respect, and whether they would buy, borrow or rent.
2. Decodes the dress code against public etiquette guides, and says so when the wording is ambiguous, with a one-line note to send the host.
3. Looks up the weather. Beyond what a forecast covers it uses typical conditions, labelled as typical, with a date to recheck.
4. Builds a head-to-toe outfit for each occasion from the person's own pieces, names real gaps (what to look for; borrow, rent or alter before buying), and gives a weather and spill backup.
5. For several days, gives a packing list that reuses pieces, with care notes.
6. Ends with a dated prep timeline, set as reminders only if the session has the tools and the person says yes.

It keeps to a few rules throughout: no comments on a person's body, cultural and religious dress is respected and not questioned, photos are used only to list clothes and are not saved, gender is not assumed, and weather is never stated from memory.

## How it differs from similar public skills

Other public outfit skills exist, for example googlarz/fashion-skill (a personal stylist with a saved profile, body analysis and a wardrobe inventory), clawic's "outfits" (an inspiration and clothes workspace kept on disk) and "outfit-weather" (an outfit from a temperature and activity the user supplies). event-outfit is narrower on purpose: one event at a time, nothing stored, no body analysis. Its own ground is decoding the invitation's wording, an honest forecast, a backup, multi-day packing with reuse, care notes and a prep timeline. Nothing was copied from those skills.

## Example

> Friend's wedding in Lisbon, Saturday 4 p.m., garden ceremony then dinner indoors. Invite says "cocktail attire". I own a navy suit, a grey blazer, white and light blue shirts, tan brogues, black oxfords, a burgundy tie. No budget for new stuff.

The reply, in outline: cocktail attire means a dark suit, with a tie as the usual choice. Weather looked up and sourced. Outfit: navy suit, light blue shirt, burgundy tie, tan brogues, with the suit jacket as the evening layer. Gaps: none. Backup: the white shirt as the spill spare, the black oxfords and an umbrella if the recheck shows rain. Timeline: check the suit fits this weekend, recheck the forecast two to three days before, lay everything out the night before.

## Not for

General fashion or trend questions with no event, shopping for one item with no event named, costume or stage design, planning or packing for a whole trip (trip-companion in this collection), interview preparation other than clothes, and laundry or stain questions.

## Sources and credits

Public pages, read on 21 November 2026 through a summarising fetch tool (not verbatim). Six of the nine were fetched again by an independent reviewer and checked against the skill.

1. Emily Post Institute, "Attire Guide: Dress Codes from Casual to White Tie": https://emilypost.com/advice/attire-guide-dress-codes-from-casual-to-white-tie
2. Debrett's, "Know your dress codes": https://business.debretts.com/know-your-dress-codes
3. Zola, "Wedding Guest Attire: A Guide to Every Dress Code": https://www.zola.com/expert-advice/what-to-wear-to-a-wedding
4. The Knot, "What Not to Wear to a Wedding": https://www.theknot.com/content/what-not-to-wear-to-a-wedding
5. Culture Trip, "What Not to Wear to Weddings Around the World": https://theculturetrip.com/articles/dont-offend-the-bride-what-not-to-wear-to-weddings-around-the-world
6. Duke University Career Hub, "Attire Guide": https://careerhub.students.duke.edu/resources/attire-guide/
7. Which?, "The best way to fold a suit for travelling": https://www.which.co.uk/news/article/watch-the-best-way-to-fold-a-suit-for-travelling-aOoRh3d1Lpjl
8. Who What Wear, "How to Pack Without Wrinkling": https://www.whowhatwear.com/how-to-pack-without-wrinkling
9. REI, "Fabric Care Symbols": https://www.rei.com/learn/expert-advice/fabric-care-symbols.html

The dress code table follows US and UK guides; the same words can mean something else elsewhere, and the skill says so.

The author's own judgement, not taken from a source: the forecast horizon (about 10 days) and the recheck 2 to 3 days out; the adjustments for speakers and hosts; "borrow, rent, alter, then buy"; the spill plan; giving dress code options as routes instead of by gender; the photo privacy rules; the lead times in the timeline; that one pale piece under a coloured main piece is fine at a wedding and that the white rule never applies to a religious head covering (sources 3 and 4 say to avoid white or cream outright); that the dressier reading wins when time and place pull apart; that the invitation outranks general guides; that a dress code naming a culture is treated as ambiguous wording.

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/event-outfit.md](../testing/event-outfit.md)

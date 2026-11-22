# life-admin

Status: reviewed. Three test rounds and three independent reviews were run; at the third review every rubric line scored 4 or 5 (Relevance 5, Trigger clarity 4, Correctness 4, Usability 4, Brevity 4, Provenance 4). A last set of small edits made after that review has been neither run nor reviewed; the testing record lists them. Version 0.1.0.

## What it does

Helps a busy person get on top of the recurring paperwork of life so nothing lapses: passports and ID, licences and vehicle checks, home dates, insurance renewals, tax and benefit deadlines, subscriptions and contracts that renew by themselves, check-ups, school and childcare dates, work licences, warranties.

It asks where the person lives and who is in the household, shows ten areas as a tick list, and asks for each item only what it is, whose it is, when it is due and where it is kept. Then it hands over, in one message:

1. The next four weeks: at most seven actions, most urgent first.
2. A register: one table with every item, its owner, due date, the date to start, the lead time and fee with their source, what is needed, where it is done and where it is kept.
3. The year, month by month, built on start-by dates and due dates.
4. How to keep it: the table is the system; a file, calendar entries or reminders only if the person asks.
5. A yearly review date.

The idea behind it is that the date to write down is the date to start, not the date of expiry. The start-by date is the due date minus the official processing time, posting, time to gather what is needed and a margin.

Rules it keeps throughout:

- No numbers. It never asks for, repeats or stores an identity, passport, policy or account number, a password or card details.
- Lead times and fees are looked up on the official source for where the person lives, in the session, and given with the source and the date checked. Anything it could not check is written "to check" with the body to ask. Nothing is filled in from memory. No country is the default.
- It says what is due and where to confirm it. It gives no legal, tax, insurance or money advice.
- In a shared household every item has a named owner, or reads "owner to confirm".
- Nothing is saved, and no calendar entry or reminder is made, without a yes after the person has seen the list.
- The first pass is meant to take under twenty minutes of the person's time.

What to expect in practice: official pages often do not open, or do not state a lead time. In testing, most rows came out "to check" with a reminder set three months ahead and labelled as a default; across the test runs with web access, an official lead or processing time was read for one item in each of three runs and for none in the other three. The usual first result is a well-ordered list of what to do and what to check, not a list of checked lead times. For travel and identity documents and residence permits with an unchecked lead time it gives no default date at all, only "check the lead time". Where a page gives the window in which a renewal may be made but no processing time, the date to start is the day that window opens.

A question about one item ("when should I renew my passport?") gets one row with its start-by date and source, and an offer of the full inventory.

This is a planning aid, not official, legal, tax or financial advice.

## How it differs from similar public skills

Seen in directory listings on 22 November 2026, not read in full: "adulting-checklist" in anthril/official-claude-plugins (a quarterly life-admin sweep by life stage; the closest in spirit; its skill file could not be opened), "renewal-tracker" in anthropics/claude-for-legal (a register of business contracts for legal teams), and several small deadline and reminder skills. This one takes a narrower angle: one personal yearly calendar built on start-by dates, lead times checked on the official source for the person's own country or honestly marked "to check", an owner per item, a strict no-numbers rule and a short first pass. Nothing was copied from those skills.

## Example

> I keep missing renewals. Can you set up a system? I live in Ireland with my partner Noor.

Country and household are given, so they are not asked again. The first reply shows the ten areas as a tick list and asks one question: "Is the list for both of you?"

They tick four areas and send four lines, such as `passport / me / Feb 2027 / desk drawer` and `passport / Noor / don't know`.

The result, in outline: the passport is looked up on the page of Ireland's passport authority and its row carries the looked-up time, the source, the link and the date checked. Noor's passport goes on "dates to find: the photo page". The car insurance gets a default reminder marked "lead time to check". A streaming subscription renewing on 3 December leads the four-week list: "find the cancel-by date in its terms today; it may fall before 3 Dec". Then the year, the offer to keep it as a file, calendar entries or reminders, and a suggested review date.

## Not for

Filing a tax return; tax, legal or money advice; planning a week; preparing one trip; reading one contract; one big purchase; preparing for one appointment; budgeting or investing; storing passwords or numbers.

## Sources and credits

Public pages, read on 22 November 2026 through a summarising fetch tool (not verbatim). The first reviewer fetched sources 2, 3 and 5 again and checked them against the research notes.

1. Colorado State University Extension, "Your Important Papers: What, Why, and How Long to Keep", N. Porter and L. Kubin: https://extension.colostate.edu/resource/your-important-papers-what-why-and-how-long-to-keep/
2. Cooperative Extension, Financial Security for All, "Organize Your Important Papers": https://personal-finance.extension.org/organize-your-important-papers
3. GOV.UK, HM Passport Office, "About our services": https://www.gov.uk/government/organisations/hm-passport-office/about-our-services
4. US Department of State, passport processing times: https://travel.state.gov/content/travel/en/passports/how-apply/processing-times.html
5. USA.gov, "Replace vital documents": https://www.usa.gov/replace-vital-documents

Not read (the fetch was refused and not retried): a Citizens Advice page on cancelling a subscription, and the skill files of the two public skills named above.

What the sources support: keeping one list of what exists and where it is kept (1, 2); reviewing it on a rhythm and at each life change (1, 2); that a lead time has parts, namely processing counted from receipt, posting on top, more time if more information is needed, a faster paid service, and times that move with demand (3, 4); not booking travel before the document is in hand (3); that replacing one document often needs another official document (5). One official page was more than three years old when read, which is why the skill gives a source and a date every time.

The sources come from two countries, the United States and the United Kingdom. They shaped the method only. The skill stores no country's rule, figure or fee.

Sources 1 and 2 suggest keeping lists of account and policy numbers. The skill deliberately does not, because a chat is not a safe place for them.

The author's own judgement or general know-how, not taken from a source: the ten areas; the limits on rounds of questions and the twenty-minute split; about six lookups in a first pass and counting a search plus opening the page as one; the three-month default reminder when a lead time is unchecked; no default date for travel, identity and residence documents; one week to gather and two weeks' margin; two calendar entries per item; seven actions at most; the word aims; "four or more" items for building at once from a list; asking the exact day only within three months; the twelve-month view; the date conventions for month-only and year-only dates; counting five working days as one week and using the longest of several stated times; the day a renewal window opens as the start-by date when no processing time is given; one shared calendar entry for items to start now; the hidden deadlines listed (notice periods, a travel document's validity beyond a trip, renewal windows, appointments that book up), given without any figure; which life events call for an update; asking who else sees a calendar or file; the closing planning-aid line.

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/life-admin.md](../testing/life-admin.md)

# name-check

Status: reviewed. Three test rounds and three independent reviews were run. At the final review all six rubric lines scored 4 (Relevance, Trigger clarity, Correctness, Usability, Brevity, Provenance), with no required fixes. A few small wording edits made after the third test round and after the final review are untested; see the testing record. Version 0.1.0.

## What it does

Helps a person choose a name for a project, product, app, community or business, or screen a name they already have, before they commit to it.

1. Gets a short brief: what it is, who it is for and where, the feel wanted, and where the name must work. It asks once, at most three questions; if the person is away it states its assumptions and carries on.
2. Suggests 15 to 20 candidates from at least four different kinds of name (says what it does, hints at the benefit, a real word from elsewhere, coined, two words joined, a word from the audience's own language, a person, place or story) and shortlists three to five.
3. Gives each shortlisted name a first screen:
   - a live search for products, companies and apps with the same or a confusable name;
   - a first look at trademark registers for the person's market;
   - how it sounds, how it would be spelled after one hearing, and unwanted meanings in the audience's languages;
   - the exact domains and handles worth having.
4. Reports a recommended name with the reason, a runner-up, one tagline, a table of the screen, what was not checked, when a professional search is worth paying for, and the next steps for the person.

Four rules hold throughout:

- Every statement about a domain, handle or trademark is labelled **looked up** (source, date and time, what came back), **not looked up** (the exact check for the person to run) or **could not look up** (what was tried and why it failed). It does not write "available", "free" or "no conflicts" as its own conclusion, even after a lookup.
- It is a first screen, not legal clearance, and it says so.
- It does not offer, and advises against, a name that could be confused with an existing brand, using a short fixed list (same or related field: drop; close to a famous brand: drop; shared fragment with a famous brand, or one shared ordinary word with a lesser brand in the same field: caution; unrelated and not famous: note).
- It does not register, buy, reserve or sign up for anything.

Without a web search tool it still suggests names (unless the person brought one) and checks how they sound, marks every other check "not looked up", says at the top that nothing was screened, gives the verdict "not screened", and hands the person the searches to run.

## Example

> "Is this name taken? I want to call my budgeting app [Name]. US launch."

The person has a name, so the skill goes straight to the screen. Suppose its searches turn up an established budgeting app whose name is one letter different. The reply, in outline:

> **Verdict: drop.** A budgeting app called [Other] already exists, one letter away, for the same users.
>
> | Check | Label | Result |
> |---|---|---|
> | Collisions | Looked up: web search for the name and the name with "budgeting app", [date, time, zone] | [what came back, with links] |
> | Trademark register | Not looked up | The exact searches to run at tmsearch.uspto.gov |
> | Domains, handles | Not looked up | The ones to check, if the name is kept |
>
> Not checked: registers, domains, handles, app stores. This is a first screen, not legal clearance. [When a professional search is worth it; an offer to suggest and screen alternatives.]

The example uses placeholders on purpose: any real-looking name printed here might belong to someone.

## Not for

Naming a baby, a pet or a fictional character; naming variables, functions or files in code; a slogan or tagline alone for a brand that already has its name; logo or full brand identity design; a legal opinion on whether a name infringes or will register.

## How it differs from similar public skills

Public naming skills already exist. The ones looked at, through their directory listings and not their source, were "domain-name-brainstormer" (ComposioHQ/awesome-claude-skills), "company-name-generator" (breverdbidder/life-os) and "brand-naming" (arnabbagxd/brand-building-skills). Others were seen by name only. From the listings, they centre on generating many names and scoring them; one shows availability ticks without naming a lookup method, one names a trademark tool the US office has since replaced, and one does no lookups and leaves checking to the user. So this comparison is limited to what the listings say.

name-check is narrower on purpose. It generates a small set and puts its effort into the screen and into saying honestly what was and was not looked up. Nothing was copied from those skills.

## Sources and credits

Public pages, read on 21 November 2026 through a fetch tool that returns a summary of each page, not its full text. The reviewers re-read the USPTO pages on likelihood of confusion and federal searching, and the WIPO FAQ, and found the skill consistent with them.

1. USPTO, "Comprehensive clearance search for similar trademarks" (uspto.gov/trademarks/search/comprehensive-clearance-search-similar-trademarks). Used for: what a fuller search covers; the baseline of a register search plus an internet search for unregistered use; when to use a search service or attorney.
2. USPTO, "Likelihood of confusion" (uspto.gov/trademarks/search/likelihood-confusion). Used for: the two questions (are the names similar in sound, look or meaning; are the goods or services related).
3. USPTO, "Federal trademark searching" (uspto.gov/trademarks/search/federal-trademark-searching). Used for: the search tool at tmsearch.uspto.gov; exact, then spelling variants, then sound-alikes; live and dead marks; the statement that no search finds every conflict or gives a clear-cut answer.
4. USPTO, "Why search for similar trademarks?" (uspto.gov/trademarks/basics/why-search-similar-trademarks). Background.
5. USPTO, "Strong trademarks" (uspto.gov/trademarks/basics/strong-trademarks). Used for: why descriptive names are weak and coined or unrelated words are strong.
6. WIPO, Global Brand Database FAQ (wipo.int/en/web/global-brand-database/faqs_branddb). Used for: what the database covers; its terms forbid automated querying.
7. ICANN, blog post on its updated registration data lookup, 29 July 2019 (lookup.icann.org). Used for: the lookup tool for domain registration records.
8. Catchword, "Create the perfect brand name" (catchwordbranding.com). Used for: brief first, kinds of name, screening order, not letting the domain drive the name, asking native speakers.
9. Igor, "Evocative product and company names" (igorinternational.com). Background on kinds of name.

Named but not read: TMview and the EUIPO search (named as tools by sources 1 and 6).

The skill's own choices, not taken from a source: the three labels and two weaker tags; the ban on "available" as a conclusion; the lookup budget and the order of checks; the rule that famous names are dropped in every field (stricter than the US office's test, which lets identical names coexist in unrelated fields); the four verdicts; the list of moments when a professional search is worth it; treating handles as "not looked up" by default.

No employer, client or confidential material was used. This skill is not legal advice.

## Testing

See the testing record: [testing/name-check.md](../testing/name-check.md).

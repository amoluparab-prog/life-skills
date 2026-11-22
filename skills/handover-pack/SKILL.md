---
name: handover-pack
description: "Writes a handover pack so something a person built can be run by someone else without them: an automation, a spreadsheet system, a small website, a workflow with AI tools, a club or household process. Given what was built and who takes over, often a non-technical person, it writes one plain document: what it is for, what the new owner needs and how each account, cost and device becomes theirs, setup steps, routine tasks, a first-week plan, ground rules, troubleshooting and who to ask; plus the builder's remaining to-do list and a short handover message. Use for \"I built this for my friend, help me hand it over\", \"write a handover so someone else can run this\", \"package this so my client can use it without me\". Not for developer or API docs for a codebase, handing over a whole job or role at a company, a note so another AI session can continue unfinished work, gathering a project's history into a brief for building it, building or fixing the thing itself, or a manual for a commercial product."
---

# Handover pack

Things people build for others tend to work only while the builder is around. This skill writes one document the new owner can follow alone, and tells the builder what they must still do. You write; you never build, fix, transfer, change or send anything. Those go on the builder's list.

## 1. Collect the facts

Read the message, any files, and the thing itself if the user gave you a link, file or access to it (read only; do not go looking through their other accounts). Look for:

- what it is and the job it does
- who is taking over, what they are comfortable with, and the device they will use
- every part: accounts, subscriptions, files, devices; who owns and pays for each today; cost and next renewal; whether it moves to the new owner or stays with the builder
- the routine tasks, their steps, and how often each is done
- what has gone wrong before
- which steps the builder has actually run lately
- how, and until when, the builder can be reached afterwards

## 2. Ask or assume

- If the user is present and you lack the steps of the task done most often, or who is taking over, ask once: at most three short questions in one message. Cover those two first; the third may be compound ("what has gone wrong before, and how and until when can you be reached?"). If one of the two is already known, spend its question on the parts and who holds and pays for each. The asking message holds only the questions: no pack, no skeleton. Then write.
- For anything else missing, do not hold the pack back. Write it and mark the gaps.
- If the user is away, or says to just write it, ask nothing.
- Open the reply that carries the pack with one "Assumptions" line: what you took as given, or "none".
- If the reader is not described, write for an adult who is at ease with email and a phone and has never seen this thing, and say so.
- If you do not know the builder's name, write "[your name]" in the top lines and "the builder" elsewhere.

## 3. Mark what is known

A wrong step is worse than a missing one, because the new owner will trust it. Anything the builder described and says works is written plainly. Everything else carries one of these marks:

- **(not tested):** the builder described it but has not run it lately, or you added a detail from your own knowledge to a step or table cell they described, such as a menu name or a price. Menus and prices change. A routine the builder says they do regularly counts as run.
- **[Builder to fill in: ...]:** something the pack needs that nobody told you. Say exactly what is missing. Merge gaps that ask the same thing: one mark for "who holds and pays for each account", not one per account.
- **(suggested, builder to confirm):** something you propose that the builder did not say: an added check, a ground rule, a check-in day.
- **(likely, not seen yet):** a failure you added to the troubleshooting table.

Your own knowledge may add a detail to a step the builder described. It may not supply the steps. A setup step or routine task the builder gave no steps for gets its heading and one fill-in mark saying what to describe, and nothing else. The only things you may add yourself are named in section 4, and each is one line with its mark, never a set of steps. A fix the builder named without steps is written in their words with a fill-in mark for the steps. A plain-word explanation of a term or a named part ("Stripe, a service that takes card payments") needs no mark.

**Skeleton.** If the builder gave no steps for the task done most often, or you do not know what most of the parts are, the brief is too thin for a full pack. Still write every heading, a line or two under each, under about 600 words in all, and call it a skeleton in your reply. In a skeleton the table keeps one row per part with one merged fill-in mark for the unknown cells, and the added checks and failures of section 4 are optional: drop them first if the pack runs long.

## 4. Write the pack

One document, in this order. A full pack is about two to four printed pages (600 to 1,500 words). Leave a heading out only if it truly does not apply.

**Top lines.** Name of the thing. "Written by [builder] for [new owner] on [date]." "Help from [builder]: [how], until [date]." "This pack is yours now: correct it when something changes."

**What this is.** Three to five sentences: the job it does, for whom, the parts in everyday words, and how to tell it is working. Add what it does not do only if the builder said so; otherwise leave it out.

**What you need, and how it becomes yours.** A table, one row for every part: what it is for; cost and next renewal; who holds it today; how it becomes yours. A part may stay with the builder: say so in the cell, and what the new owner does if it stops working. A transfer the builder has not described is a fill-in mark; you may put one likely route per part beside it, marked "(not tested)". Under the table, what happens if a payment lapses, if known.

**Setting up (once).** Numbered steps. After each step that changes something: "You should see: ...".

**Routine tasks.** Only the tasks the new owner will really do, grouped by how often. Give each a heading that says what it achieves, numbered steps, and a closing "You should see: ...". You may add up to two one-line checks where a part can fail silently (an automatic job, a renewal), marked "(suggested, builder to confirm)". Features they will not use get one line under "Things you can ignore".

**Your first week.** Three to five items in order: finish setup and check it is working; do each routine task once while the builder can still be reached; one practice run on a copy, if a copy can be made; a check-in with the builder on a day you propose from the dates given, marked "(suggested, builder to confirm)", or a fill-in mark if you have no dates; write down anything the pack got wrong.

**Ground rules.** Three short lists: "Never change" (with what breaks if you do), "Safe to try", and "Ask first". Then where the spare copy is and how to go back to it. Use what the builder said. A rule of your own must follow from the parts described and carries "(suggested, builder to confirm)".

**If something goes wrong.** A table: what you see; most likely why; what to do. Failures the builder has seen come first. You may add up to three that plainly follow from the parts (a payment fails, a sign-in expires, a row is deleted), marked "(likely, not seen yet)". End with "Stop and ask": when to stop touching it, who to contact and how, and where to turn if the builder cannot be reached (a second person, or the service's own help pages).

**Words used.** Only if the pack needs terms the reader may not know. One line each.

### How to write steps

- Number them. One action per step; short actions in the same place can share one. Past about ten steps, split the task in two.
- Say where before what: "In the Members tab, select the last row."
- Use the builder's names for buttons, tabs and files, exactly. Include the finishing action (Save, Send, Close).
- Call the reader "you". Use short sentences and the words they would use. Explain a needed term in the sentence where it first appears.

## 5. Keep secrets out

The pack will be forwarded, printed and left on desks. Never put a password, key, recovery code, PIN, card or bank account number, or security answer in it. For each one, say where it is kept and how it will be passed on:

- Best: the account's own "invite" or "transfer ownership" feature, so no password changes hands.
- Next: a password manager's sharing feature.
- Last: in person or by phone, never by email or chat, and the new owner changes it straight away.

If the user pasted a secret into the conversation, do not repeat it. Tell them once to change it, since it now sits in a chat, and add that to their list.

Sign-in checks trap people. If an account sends codes to the builder's phone or email, or uses them for recovery, moving these to the new owner goes on the builder's list.

## 6. The reply: builder's list and handover message

The pack is for the new owner, so the rest goes around it. If you can create files, save the pack as one document (the format asked for, or a plain one) and reply in the chat; if not, put the pack in the chat, clearly separated. Order of the reply: the Assumptions line; any warning about a pasted secret; the pack, or where it is saved; one line saying whether it is a skeleton, a draft with marks left, or ready; up to five gaps that matter most; the builder's list; the message.

**Before you hand over** (for the builder), only the items that apply:

- move each account, payment and renewal as the table says
- move recovery email, recovery phone and sign-in codes
- run every "(not tested)" step, fill every "[Builder to fill in]", confirm or delete everything marked "(suggested ...)" or "(likely ...)", and put your name in the top lines
- watch the new owner do each routine task from the pack alone, without helping, then fix what tripped them
- make a backup or spare copy, if there is none
- remove your own access, or agree in writing what you keep
- agree how and until when you will help, and ask for a reply that says "received, I can get in"
- decide anything the pack needs that fits none of its headings (name each one)

**Handover message.** Under 120 words, from the builder to the new owner: what is attached, the first thing to do, how and until when the builder will help (leave "[how]" and "[date]" if unknown). No secrets.

## Example

User: "I built a Google Sheet and a form for our football club's snack rota. Priya is taking it over next month, she's fine with WhatsApp and email but not spreadsheets. Each Sunday I copy the form answers into the Rota tab under the last filled row and send the week's names to the group. It's all free and on my Gmail. Sam"

The reply opens with an Assumptions line, then the pack. Part of it:

> | Part | What it is for | Cost and next renewal | Who holds it today | How it becomes yours |
> |---|---|---|---|---|
> | The rota sheet | Shows who brings snacks each week | Free | Sam's Google account | [Builder to fill in: how the sheet and the form will move to Priya's account]. Likely through the sheet's sharing settings (not tested) |
>
> **Every Sunday: tell the group who is on snacks**
> 1. Open the rota sheet.
> 2. Copy the new form answers. [Builder to fill in: where the answers appear and how to tell which are new]
> 3. In the Rota tab, paste them under the last filled row.
> 4. Send this week's names to the WhatsApp group.
>
> You should see: this week's row filled in, and your message in the group.

After the pack: "A draft with marks left." Then the gaps that matter, the builder's list (move the sheet and form to Priya, test the transfer, fill the gaps, watch Priya do one Sunday run) and a four-line message for Sam to send.

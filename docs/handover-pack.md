# handover-pack

Status: reviewed. Three test rounds and three independent reviews were run; all six rubric lines scored 4 of 5 at the final review. Correctness was 3 at the second review and rose to 4 after an extra round ran a thin brief, a detailed brief and a present-user brief on the text as it then stood, and all three passed. Four small edits made after that round have not been run. Version 0.1.0.

## What it does

Things people build for others (an automation, a spreadsheet system, a small website, a workflow with AI tools, a club or household process) tend to work only while the builder is around. Given what was built and who is taking over, this skill writes one plain-language handover pack the new owner can follow alone:

1. Top lines: who wrote it for whom, when, and how long the builder will help.
2. What this is, and how to tell it is working.
3. What you need, and how it becomes yours: one table of every account, subscription, file and device, with cost, renewal, who holds it today and how it changes hands (or stays with the builder).
4. Setting up, once, with "You should see" after each step.
5. Routine tasks, only the ones the new owner will really do.
6. Your first week.
7. Ground rules: never change, safe to try, ask first, and where the spare copy is.
8. If something goes wrong, ending with when to stop and who to ask.
9. Words used, if needed.

Around the pack, for the builder: a line saying whether it is a skeleton, a draft with marks left, or ready; the gaps that matter most; a "before you hand over" list (move accounts, payments and recovery details, test the untested steps, watch the new owner do a run from the pack alone, sort out your own access, agree the help window); and a handover message under 120 words.

Rules it keeps:

- It writes for the stated reader and explains any term where it first appears.
- No password, key, recovery code, PIN, card or bank account number, or security answer goes in the pack. It says where each is kept and how to pass it on (the account's own invite or transfer feature first, a password manager's sharing second, in person or by phone last). If you paste a secret into the chat it does not repeat it and tells you to change it.
- It never invents a step. Plain-word explanations of terms aside, what the builder has not run lately is marked "(not tested)". What nobody described is marked "[Builder to fill in: ...]". Its own suggestions are marked "(suggested, builder to confirm)" or "(likely, not seen yet)".
- A thin brief gets a short skeleton, not a full pack padded with guesses. The rule passed its test on 22 November 2026; one sentence added to it afterwards (on the table and the optional additions in a skeleton) has not been run. See the testing record.
- It asks at most three questions, once, and none when you are away.
- It only writes. It does not build, fix, move accounts or send the message.

## How it differs from similar public skills

A web search on 21 November 2026 found many public skills named "handoff" or "handover". Two were read (through a summarising tool): borghei/claude-skills "handoff", which packages unfinished work so another person or a fresh AI agent can continue it, and adobe/skills "handover-author", which generates an authoring guide for content authors taking over an Adobe AEM Edge Delivery Services project from its code. About ten more were seen in search results and not read (from ciciliaeth, robertguss, s-hiraoku, ykdojo, mattpocock, maaarcooo, skinnyandbald, parcadei, lacolaco, rohitg00); from their titles most are AI-session or work-in-progress handoffs. This skill is narrower in a different direction: a finished, working thing of any kind, not only code, passing to a named and often non-technical owner, with the transfer of accounts and costs, a no-secrets rule, honest marks for what is untested or unknown, and the builder's remaining to-do list. Nothing was copied from those skills.

## Example

> I built a Google Sheet and a form for our football club's snack rota. Priya is taking it over next month, she's fine with WhatsApp and email but not spreadsheets. Each Sunday I copy the form answers into the Rota tab under the last filled row and send the week's names to the group. It's all free and on my Gmail. Sam

Part of the pack:

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

After the pack: "A draft with marks left", the gaps that matter, Sam's list (move the sheet and form to Priya, test the transfer, fill the gaps, watch Priya do one Sunday run) and a short message for Sam to send.

## Not for

Developer or API documentation for a codebase; handing over a whole job or role at a company; a note so another AI session can continue unfinished work; gathering a project's history into a brief for building it; building or fixing the thing itself; a manual for a commercial product.

## Sources and credits

Public pages, read on 21 November 2026 through a summarising fetch tool (not verbatim). The first reviewer fetched sources 1, 2, 5 and 6 again; 1, 2 and 5 matched, and the notes on 6 were corrected. The second reviewer fetched 3, 4 and 6 again; 3 and 6 matched and one small point on 4 was reworded.

1. AWS Well-Architected Framework, OPS05-BP01 "Develop and test runbooks to perform procedures": https://docs.aws.amazon.com/wellarchitected/latest/framework/ops05-bp01.html
2. Microsoft Writing Style Guide, "Writing step-by-step instructions": https://learn.microsoft.com/en-us/style-guide/procedures-instructions/writing-step-by-step-instructions
3. Microsoft Writing Style Guide, "Procedures and instructions checklist": https://learn.microsoft.com/style-guide/checklists/procedures-and-instructions-checklist
4. Wix Studio blog, "Best practices for a seamless site handover": https://www.wix.com/studio/blog/best-practices-for-a-seamless-site-handover
5. Rocket.net blog, "Agency guide to offboarding client websites": https://rocket.net/blog/agency-guide-to-offboarding-client-websites/
6. DEV Community (instarenewal), "The clean offboarding checklist: how to hand over digital assets without liability" (a vendor's post about its own product; used only where it agrees with 4 and 5): https://dev.to/instarenewal/the-clean-offboarding-checklist-how-to-hand-over-digital-assets-without-liability-4l2o

Two pages could not be opened and nothing rests on them: the UK National Cyber Security Centre's guidance on password managers, and the US Digital.gov plain language principles.

What the sources support: say the outcome first, list what is needed, write ordered steps a non-author can follow, say what to do when a step fails and who to ask, have someone who did not write it follow it alone, and give the document an owner (1); numbered steps, one instruction each, the place before the action, the finishing action included, short procedures (2, 3); a handover is a transfer of responsibility, move things into the new owner's own account, a copy to practise on, a walkthrough, a route for help afterwards (4); one list of every service with owner and renewal date, untangle anything tied to the builder's personal accounts or phone, confirm the new owner can get in and a backup is reachable, ask for written confirmation (5, 6); the builder's own access removed, and billing moved (6).

The author's own judgement or general know-how, not taken from a source: keeping passwords out of the pack (the brief's rule; consistent with 5 and 6 but stated by neither); the order of safe ways to pass access; moving recovery details and sign-in codes; changing any secret pasted into a chat; the four marks and the rule that the skill's own knowledge may add a detail to a described step but never supply the steps; the skeleton rule and its 600-word limit; the caps (three questions, two added checks, three added failures, about ten steps a task, 120 words for the message); the default reader; the length aim; the first-week plan; the three ground-rule lists; letting the builder keep some access by written agreement; the "You should see" line; the order of the reply; every plain-language rule beyond sources 2 and 3; and applying website-handover practice to spreadsheets, automations, AI workflows and club or household processes. Sources 4 to 6 are all about websites built for clients; nothing read covers a club or household process directly.

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/handover-pack.md](../testing/handover-pack.md)

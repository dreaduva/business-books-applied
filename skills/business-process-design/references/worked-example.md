# The E-Myth Revisited Worked Example: A Handoff That Survives Missing Inputs

**Fictional teaching example.** The business, people, records and walkthrough outcomes are invented. The simulation is not a real employee trial or a case reported in the book.

## The recurring problem

LessonLoop's founder prepares each prototype walkthrough from a request form. A part-time operator, Maya, will prepare the session records while the founder conducts calls. This is a fictional role assignment, not a recommendation to hire. Both have access to a shared internal task board; only the founder decides fit exceptions and additional service promises.

Current founder instruction: “Check the request, set up the demo and tell me when ready.” The founder remembers which time zone to use and which requests were already approved. Maya does not. The business wants a consistent prepared session, not simply a shorter preparation time.

Scope: from a founder-approved walkthrough request to a verified session brief. It excludes confirming new product features, changing prices, sending invitations without approval and copying real student details into a demonstration.

## Input packets for the simulation

| Field | Case A | Case B |
| --- | --- | --- |
| Request ID | W01 | W02 |
| Customer label | Tutor A | Tutor B |
| Fit approved by founder | Yes | Yes |
| Requested local time | Tuesday 14:00 | Tuesday 14:00 |
| Time zone | Europe/Berlin | Missing |
| Appointment confirmed | Yes, in session record | No |
| Demo dataset | Approved synthetic set D1 | Approved synthetic set D1 |
| Special request | Show pending list | “Please show automatic reminders” |

The current prototype has manual status updates and no reminder automation. The task board records whether an appointment is confirmed separately from a requested time.

## Version 1 and its failure

Version 1 says to copy the requested time into the session brief, load D1, and mark the task ready. Case A appears to work. For case B, Maya infers the local time zone, prepares an unconfirmed appointment and assumes the feature request is already approved because fit is approved.

The simulated output is a tidy brief for the wrong certainty level. No customer message is sent. The review identifies three missing distinctions: request versus confirmation, missing time zone versus a known time, and customer fit versus feature availability. “Be careful” would not supply any of them.

## Version 2: complete operating procedure

**Process:** Prepare prototype walkthrough brief.

**Owner:** Founder. **Operator:** Maya or an operator trained on the current prototype. **Version:** 2. **Trigger:** Founder marks a request “fit approved; prepare.” **Completion:** A verified brief is accepted by the founder. An unresolved blocker is a recorded state, not completion.

### Prerequisites

The request must have an ID, customer label, founder fit decision, requested next step and linked appointment record. The operator needs the approved synthetic dataset and a current capability note. A confirmed appointment must include date, time and named time zone. The operator must not infer a zone from a name or email address.

### Operating steps

1. Open the task and claim preparation ownership. Check that another operator has not already prepared the same request.
2. Confirm the founder's fit approval and inspect the appointment state. If the appointment is not confirmed, mark “blocked: scheduling” and assign the scheduling question to the founder. Do not turn a preferred time into a booked appointment.
3. Check date, time and time zone against the confirmed appointment record. If missing or conflicting, preserve both supplied values, record the conflict and pause time-dependent preparation until the founder resolves it.
4. Read the requested demonstration topics against the capability note. Include supported topics. For unsupported requests, add an explicit limitation to the brief and ask the founder to decide whether the proposed session still fits. Do not promise future features.
5. Load synthetic dataset D1 into the approved demonstration environment. Verify that the pending and confirmed rows display as expected. Use no real customer or student data for this preparation.
6. Write the session brief: request ID, customer label, confirmed time/zone, customer's stated question, supported demonstration steps, limitations and next action.
7. Run the acceptance checks below. If they pass, mark “ready for owner review” and assign to the founder. Maya remains responsible for tracking the handoff until acknowledged.
8. Founder reviews the brief, accepts it or returns a specific correction. Only acceptance marks preparation complete. Sending an invitation is a separate authorized activity.

### Acceptance checks

- Request and appointment identifiers refer to the same person and session.
- Appointment is confirmed, with an explicit time zone.
- Demonstration uses D1 and shows only supported behavior.
- Unsupported requests remain visible as limitations or resolved scope decisions.
- The brief contains an actionable next step and no unresolved blocker hidden under “ready.”

### Exception paths

| Condition | State | Owner/action | What can continue |
| --- | --- | --- | --- |
| Missing zone or unconfirmed appointment | Blocked: scheduling | Founder resolves with requester through an authorized interaction | Generic D1 environment check only |
| Unsupported feature request | Blocked: scope decision | Founder confirms whether current demonstration is still useful | Record supported topics; no feature promise |
| Wrong or unavailable demo environment | Blocked: environment | Founder restores approved access/environment | Brief facts can be drafted |
| Founder has not accepted handoff | Awaiting owner review | Maya follows the agreed internal review process | Task stays open; no automatic completion |

### Review record

Retain the brief version, blocker/resolution note and acceptance time. Do not copy unnecessary personal information into the reusable procedure. Owner reviews the SOP after a product capability change, recurring exception or failed handoff.

## Rerunning the simulated cases

Case A passes the checks, and the founder accepts a brief for Tutor A at Tuesday 14:00 Europe/Berlin using D1. It is marked complete only after acceptance.

Case B now becomes blocked for scheduling and scope. Maya records the missing zone and the unavailable reminder feature. Generic dataset checks can proceed, but there is no ready appointment and no implied automation promise. This is a successful execution of an exception path, not a failed employee performance.

For a further fictional input, the founder supplies a confirmed Wednesday 11:00 Europe/London appointment and states that Tutor B accepts a demonstration of manual tracking only. Maya updates the brief, retains the limitation and submits it for review. The founder accepts it. These added facts resolve the blockers; Maya does not invent them.

## Finished case B brief

**Request:** W02, Tutor B. **Appointment:** Wednesday 11:00 Europe/London, confirmed in the supplied record. **Topic:** See how to maintain a pending confirmation list manually. **Demo:** D1; show a pending row, record a reply and check the resulting list. **Boundary:** No automatic reminders. **Next action:** Founder conducts the confirmed walkthrough using this brief. **Preparation status:** Accepted in the fictional review.

## What the role distinction changed

Maya performs the preparation. The founder's management role supplies criteria, ownership and review. The founder's entrepreneurial role may later decide whether demand for automation warrants a different product or audience. The SOP does not make that strategic decision on the operator's behalf.

A fast but incorrect version 1 would look good on completion time alone. Version 2 may wait longer because it exposes missing decisions. The proposed live review should inspect first-pass acceptance, blocker reasons and rework alongside active preparation time. No improvement rate is claimed from this desk simulation.


# The Lean Startup Worked Example: A Confirmation Pilot That Fails Its Rules

**Fictional teaching example.** Maya, LessonLoop, every participant, event, number, and outcome below are invented. No customer research or experiment was conducted. The decision rules are local scenario choices, not benchmarks from Eric Ries.

## 1. Decision and assumption

Maya is considering two weeks of engineering work to automate lesson-change confirmations. Earlier fictional interviews suggest that some tutors struggle to coordinate changes with parents, but also that ordinary weeks can be uneventful. Those interviews justify investigation; they do not show that every tutor needs new software.

Her first proposed assumption is too broad: “Tutors want automatic reminders.” It combines a problem, a preferred solution, adoption, and willingness to pay. She rewrites it as: **For tutors coordinating a changed lesson with one responsible adult, a manual confirmation workflow can reach a clear acknowledgment state within an acceptable amount of coordination work.**

The decision is whether the workflow is sufficiently understood to justify the proposed automation investment. The trial will not answer price acceptance, long-term retention, or whether software can reproduce the human operator's judgment.

## 2. Intervention choice

Maya considers three options:

| Option | What it could reveal | Why she chooses or rejects it now |
| --- | --- | --- |
| Waitlist page | Whether some visitors request more information | Reject for this question: a signup does not reveal confirmation work |
| Clickable prototype | Whether a tutor understands the proposed status view | Defer: the workflow and exceptions need investigation first |
| Openly manual service | Which steps lead to acknowledgment and what they cost in time | Select: it exposes coordination work before automation |

Participants are told Maya is operating the service manually. She records only the information needed for the agreed test. No automated messaging or attendance improvement is promised. Normal tutor arrangements remain available; withdrawal is permitted. This does not establish a general data-handling policy for a real product.

## 3. Participants and opportunity

Four fictional tutors, T1 through T4, volunteer for a two-week trial. They have recently coordinated changed lessons with a responsible adult. This is a small convenience sample; it cannot estimate how common the need is among tutors generally.

An eligible event is an agreed lesson-time change requiring acknowledgment from both tutor and responsible adult. A new booking, a duplicate message, and a cancellation without a replacement time are excluded from the primary event count. Excluded records remain in the log.

The deadline is the earlier of 24 hours after the change is agreed or the start of the replacement lesson. Success requires both acknowledgments by that point. A later reply is recorded as late, not retroactively counted as on time. Every eligible event reaches its deadline before the final review.

## 4. Measurement specification

| Measure | Definition | Limitation |
| --- | --- | --- |
| On-time acknowledgment | Eligible events with both acknowledgments by cutoff / all eligible events whose cutoff has passed | Measures confirmation, not attendance |
| Operator burden | Minutes actively spent coordinating each eligible event | Excludes product development and customer acquisition |
| Exception pattern | Recorded cause or unresolved question for difficult events | An explanation may be tentative |

Maya has anecdotes about the previous process, but no comparable baseline with the same eligibility and deadline rules. Therefore the pilot cannot support a numerical improvement claim. It can describe outcomes and burden under this intervention.

Repeated events from the same tutor remain separate events, but not separate participants. Twelve events from four tutors do not equal twelve independently recruited customers.

## 5. Prospective decision rules

Before the trial, Maya sets a conservative operational gate for this small automation investment: every eligible event should be acknowledged on time, and median coordination effort should be no more than five minutes per event. The five-minute limit reflects her provisional capacity allocation for the service, not a proven economic model. Zero unresolved events reflects her desire to understand the routine path before automating it; it is not a statistically established reliability target.

A failure triggers investigation of the exception path rather than immediate scaling. A participant harm or unacceptable data-handling issue would stop the test. The scenario assumes none occurs. Maya caps the pilot at the agreed two weeks and reviews it herself.

Even a pass would only support further investigation of automation. It would not prove demand, willingness to pay, or scalable delivery.

## 6. Event log

The following is the complete invented eligible-event log. Times are active operator minutes.

| Event | Tutor | Both acknowledged by cutoff? | Minutes | Recorded note |
| --- | --- | --- | ---: | --- |
| E1 | T1 | Yes | 4 | One responsible adult; no clarification |
| E2 | T1 | Yes | 5 | One follow-up |
| E3 | T2 | Yes | 6 | Contact details clarified |
| E4 | T2 | Yes | 7 | Time restated once |
| E5 | T3 | Yes | 8 | Two message exchanges |
| E6 | T3 | Yes | 8 | One follow-up and status check |
| E7 | T4 | Yes | 8 | Approval role confirmed first |
| E8 | T4 | Yes | 9 | Reply arrived close to cutoff |
| E9 | T1 | Yes | 10 | Earlier proposed time caused confusion |
| E10 | T2 | Yes | 12 | Founder resolved a handoff question |
| E11 | T3 | No | 18 | Contacted adult said another adult must approve |
| E12 | T4 | No | 21 | Conflicting replies; final authority unresolved |

Two additional records are retained outside the denominator: X1 is a duplicate message for E4; X2 is a cancellation with no replacement time. They were excluded under the original rules. There are no missing outcome or effort fields in this invented log.

## 7. Calculate and challenge the result

On-time acknowledgment is **10/12 = 83.3%**. The sorted effort values are 4, 5, 6, 7, 8, 8, 8, 9, 10, 12, 18, and 21. The median is the average of the sixth and seventh values: **8 minutes**. Total active effort is **116 minutes**; the mean is approximately **9.7 minutes** per event.

Both original gates fail: two events remain unresolved, and median effort exceeds five minutes. The two failed events consume 39 of the 116 minutes, approximately 33.6% of total effort. That concentration suggests investigating the exception path, but the other ten events still have a median of eight minutes. Removing the failures would not make the original effort rule pass.

Maya rejects three tempting conclusions:

- **“We improved confirmations by 83%.”** There is no comparable baseline; 83.3% is an observed outcome rate, not an improvement.
- **“The two failures do not count because they were unusual.”** They met the original inclusion rule and belong in the result. Their unusual features may inform a future segment or process change.
- **“Automation will remove all the labor.”** Much of the costly work involved identifying authority and resolving conflicting replies. Sending messages automatically does not necessarily resolve those decisions.

The contrary evidence also matters. E7 involved an approval-role clarification and still completed. E10 completed after a costly handoff. The observations do not show that every handoff makes completion impossible; they suggest that identifying responsibility may be one component of the work.

## 8. Decision and revised test

**Decision: postpone the two-week automation build.** First investigate how to identify the responsible approver and handle conflicting replies. This follows from both failed rules and the nature of the exceptions, not from a general belief that manual services are better.

The next proposed intervention adds an explicit approver-confirmation step before recording a lesson change. It retains the existing acknowledgment deadline and records the extra setup effort separately. This makes a tradeoff visible: a cleaner confirmation stage might be purchased with more work beforehand.

Proposed next record:

| Field | Revised plan |
| --- | --- |
| Assumption | Naming the responsible approver early reduces unresolved authority questions without an unacceptable total burden |
| Participants | Similar relevant tutor situations; identify recruitment changes rather than assuming comparability |
| Intervention | Confirm responsibility before starting the existing manual process |
| Outcomes | On-time acknowledgment, unresolved authority cases, setup minutes, and later coordination minutes |
| Comparison | Compare descriptively with the first trial; do not claim causality from different small event sets |
| Decision rule | Retain the original five-minute total-burden target unless capacity assumptions are explicitly revised before the test |
| Stop/review | Review within the next agreed bounded trial; stop earlier for the same participant-risk conditions |

This test might reveal that the target is unrealistic. If so, Maya should revisit the service design, economics, or investment decision openly. She should not hide setup minutes to make a dashboard look better.

The second test is **proposed, not run**. Payment, repeat adoption, technical reliability, and acquisition remain separate uncertainties. A future paid offer would need defined deliverables and terms; this example supplies no evidence of willingness to pay.

## What a different result would change

If all events had completed within the effort target, a narrow technical feasibility test might become a sensible next investment. If the routine produced little value even with adequate execution, the customer or problem hypothesis might need reconsideration. If measurement were broken, the next action would be to repair it before making either strategic claim.

The lesson is not that an 83.3% rate is always bad. It is that the decision depends on the original question, the meaning of the metric, the operating constraints, and the work hidden behind the average.


# 18 | Iterative delivery — sample prioritized backlog and demo controls

**Why included:** Martins' résumé lists Agile / Hybrid delivery and PSM. This is a **teaching reconstruction**, not evidence that any historical team ran these exact sprints, used these stories or applied Scrum formally.

## How the PM balances iterative work and governed releases

- Product/business owner prioritizes value and requirements; engineers size/sequence work; QA confirms testability; PM integrates forecasts, capacity, dependencies and fixed external gates.
- Stories must trace to REQ IDs and have objective acceptance tests before demonstration.
- Newly requested scope enters impact assessment; the team does not silently expand the W5 baseline.
- Iteration demos inform requirements and usability; system-wide UAT, security review and cutover remain separate W17/W20 gates.

## Example iteration review (W10)

| Story | Related requirement | Demonstration / acceptance | Result in simulation |
| --- | --- | --- | --- |
| ST-01 Candidate entry | REQ-02 | Mandatory fields rejected; save persists valid data | Accepted for integration test |
| ST-02 Exam selection | REQ-03 | Eligibility rule applied to exam choices | Accepted with UX wording refinement |
| ST-03 Confirmation | REQ-05 | Stable reference ID and status generated | Accepted for integration test |
| ST-04 Duplicate-ID detection | REQ-04 | Detect duplicate manual enrolment, including boundary cases | Needs expanded import regression |

## What the PM watches

Dependency from duplicate-ID logic (ST-04) to data import (REQ-08); tester coverage; end-to-end test environment readiness; cumulative defect trends; and whether stakeholder-requested changes are scope-neutral clarifications or require CCB. The W16 fictional issue demonstrates why iteration-level acceptance is not equivalent to production readiness.

See [backlog.csv](../registers/backlog.csv) for prioritized sample work and owners.

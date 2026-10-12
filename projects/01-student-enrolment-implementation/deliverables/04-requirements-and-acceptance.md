# 04 | Requirements strategy and acceptance traceability

## Discovery approach

Facilitate workshops with examination administrators, school representatives, operations staff, QA and technical staff; map the as-is enrolment process; challenge exceptions; rank needs using MoSCoW; document the to-be workflow and acceptance rules. The resume mentions requirements analysis and these classes of stakeholder involvement. Detailed requirement IDs and prioritization below are reconstructed.

## Minimum viable business capabilities

| ID | Requirement | Priority | Business acceptance |
| --- | --- | --- | --- |
| REQ-01 | Maintain school profile and authorized school user | Must | User may view/update only authorized records |
| REQ-02 | Capture candidate data with mandatory field validation | Must | Required data blocked when missing |
| REQ-03 | Select eligible examinations | Must | Only valid selections allowed |
| REQ-04 | Detect duplicate candidate registration / import IDs | Must | Duplicates rejected or routed for documented review |
| REQ-05 | Issue durable registration confirmation | Must | Confirmation ID and status reproducible |
| REQ-06 | Enforce role-based access and audit trail | Must | Unauthorized action denied and logged |
| REQ-07 | Export reconciled enrolment dataset | Should | Admin export reconciles to accepted records |
| REQ-08 | Bulk import validated legacy roster | Should | Reconciliation thresholds and exceptions accepted |

## Requirements governance

1. BA proposes requirement ID, priority and unambiguous acceptance criteria.
2. Business Owner approves priority/meaning; Tech Lead verifies feasibility.
3. QA Lead links requirement to positive, negative and security/access test cases.
4. PM tracks traceability and impact of requirement changes across cost/schedule/quality.
5. No item is represented as delivered until objective evidence exists.

**Traceability:** see [requirements_traceability.csv](../registers/requirements_traceability.csv) and [uat_cases.csv](../registers/uat_cases.csv). Test case UAT-04 concerns REQ-04; at simulated W16, its validation fails and gate G3 remains blocked. A W17 retest resolves the case.

## Acceptance vs handover

Feature acceptance establishes that agreed capabilities work. Operational acceptance separately verifies support ownership, training, access processes, data recovery/rollback, monitoring and incident response. A successful demo alone is not authorization to launch.

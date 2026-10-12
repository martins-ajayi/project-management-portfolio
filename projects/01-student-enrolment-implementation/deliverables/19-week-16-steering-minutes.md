# 19 | Steering exception meeting — W16 decision minutes

**Record type:** Worked illustration only | **Meeting purpose:** Unblock UAT readiness issue without weakening release controls

## Attendance by role

Sponsor (decision chair), Business Owner, Project Manager, Technical Lead, Data Lead, QA Lead, Operations Lead. These are fictional role assignments, not a record of real attendees.

## Facts tabled by the project manager

- M-04 W17 gate at risk; M-05 W18 pilot remains conditional.
- W16 QA: 169/180 pass, 5 fail, 6 blocked; 93.9%; one open P1.
- I-01 data mapping duplicates jeopardize REQ-04/08 acceptance.
- Options A/B/C and cost/schedule implications recorded in [CHG-01](14-change-request-and-decision.md).

## Decisions

**DEC-02:** Approve **CAD 8,000** corrective-action spend from **CAD 12,000 approved contingency**, with no change to CAD 240,000 cap. Preserve full UAT and Ops readiness rules. PM records outcome, communicates impact and reports a W17 retest result before proposing go-live. Approval represented for simulation, not a real signature.

## Assigned actions

| Action | Owner | Due | Evidence |
| --- | --- | --- | --- |
| ACT-01 Revise identifier mapping | Data Lead | W17 | Mapping + reconcile evidence |
| ACT-02 Re-execute UAT including negative checks | QA Lead | W17 | 180-case outcome; P1 count |
| ACT-03 Communicate Amber escalation | PM | W16 | Status + decision reference |
| ACT-04 Confirm runbook and rollback | Ops Lead | W17 | Gate G3 checklist |

**Next escalation:** Sponsor will defer W18 pilot if any P0/P1 remains at W17 or if data and operational checks fail. Follow-up minutes would record evidence, not rely on optimism.

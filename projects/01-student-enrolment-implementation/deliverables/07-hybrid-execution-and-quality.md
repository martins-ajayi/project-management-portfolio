# 07 | Integrated delivery approach, quality and control framework

## Why a hybrid model fits this scenario

Use predictive governance for funding, scope, data/security policies, external school dates and staged releases; use iterative solution-building to validate workflows and reduce usability rework. Agile practices are **delivery mechanisms**, not a substitute for gate evidence.

## Delivery workstream rhythm

- BA prepares ranked stories, acceptance criteria, constraints and traceability before each iteration.
- Engineering and design demonstrate finished workflow increments to business representatives; observations enter a prioritized backlog.
- QA automates or repeats appropriate checks; regression coverage tracks changes to validation and duplicate rules.
- PM maintains integrated milestone commitments, dependency owners, forecast and escalation; material impacts go to CCB.
- Business Owner accepts increments but remains accountable for end-to-end UAT and release acceptance.

## Quality management plan

| Assurance layer | Responsible | Required evidence |
| --- | --- | --- |
| Requirements quality | BA / Business Owner | Testable criteria, baselined RTM |
| Design/access | Technical + Security Leads | Role permissions, audit and design review |
| Integration/data | Technical / Data Leads | Import validations and reconciliation |
| Functional/system test | QA Lead | Test run, defects, regressions |
| Business UAT | Business Owner and representative users | ≥95% pass; no open P0/P1 |
| Operations readiness | Operations Lead | Runbook, owner, monitoring, rollback, training |

## Definition of ready / done (scenario)

**Ready:** business priority known, dependencies visible, estimate agreed, security concerns triaged, acceptance criteria testable. **Done:** review approved, tests passed, accessibility/privacy controls considered, documentation updated, traceability linked and no critical defects hidden.

## Gate management

A release gate contains the facts, recommendation, unresolved risk, alternative options, impact and explicit decision. Marking a feature complete does not override the W17/W20 deployment controls.

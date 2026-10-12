# 13 | Executive status report — Week 16 (worked example)

**Project:** Student Enrolment Management System | **Reporting period:** W16 | **Owner:** Project Manager | **Overall:** **AMBER**

> This is a hypothetical management report included to demonstrate transparent issue escalation. It is not a real stakeholder communication.

## Executive summary

Delivery remains targeted for **W18 pilot** and **W21 expansion**, but the **W17 UAT/readiness gate is at risk** after duplicate candidate IDs surfaced in the import rehearsal. **P1 issue I-01** blocks readiness. No premature UAT sign-off will be requested. Sponsor decision on remediation capacity and **CAD 8,000 contingency** is required. If W17 retest fails, pilot will be deferred under the established gate criteria.

| Dimension | Status | Evidence / mitigation |
| --- | --- | --- |
| Scope | Green | Baseline unchanged; nonessential SMS extension remains deferred |
| Schedule | Amber | W17 gate threatened; W18 pilot forecast retained conditional on retest |
| Cost | Green/Watch | Ceiling CAD 240k, including reserve; request $8k draw; EAC $236k after draw |
| Quality | Amber | W16 UAT 169/180 pass (93.9%); 5 fail, 6 blocked; 1 P1 open |
| Stakeholders | Green | Business Owner and Ops notified; sponsor exception call initiated |
| Data migration | Amber | Import mapping quarantined; reconciliation and negative-case tests added |

## Decisions requested by end of W16

1. **Approve CHG-01 / DEC-02:** temporary data-validation/retest capacity funded by **$8k existing contingency** (not an increase to the $240k cap).
2. **Uphold G3:** no go-live approval unless UAT ≥95%, 0 open P0/P1, and operations checks passed at W17.

## Two-week look ahead

- W17: execute revised duplicate validation, reconcile import, rerun all 180 UAT cases, and make G3 decision.
- W18: start controlled 10-school pilot **only if gate clears**.
- W20: report pilot evidence and decide whether to expand W21.

## Risk and action owners

I-01 Data Lead: correct mapping and test fixtures W17. QA Lead: rerun negative and full critical-path cases W17. PM: update sponsor by end of W16, publish gate recommendation at W17. Ops: verify recovery/support capability by W17.

**Forecast is conditional:** this W16 report does **not** imply W17 success was already known; the later W17 resolution appears in the illustrative closure and release records.

# 02 | Project charter

**Project:** Student Enrolment Management System | **Status:** Illustrated W5 approved baseline | **Project manager:** Martins Ajayi (scenario PM role) | **Version:** 1.0, hypothetical

## Purpose and authorization

Implement a secure and usable student enrolment workflow with dependable registration checks, school/candidate records, exam selection and confirmation. The Sponsor authorizes an indicative **24-week**, **CAD 240,000** delivery plan; approval is illustrative, not an actual authorization record.

## Measurable success criteria — all illustrative

1. Registration submission completion rate ≥95% for eligible submissions during initial measurement window.
2. School training completion ≥90% before their release wave.
3. UAT gate ≥95% passing, **zero unresolved P0/P1**, with business owner sign-off.
4. Wave 1 pilot **10 schools at W18**; wave 2 **40 additional schools at W21**, subject to gates.
5. Forecast and actual delivery spend remains within **CAD 240,000** approved total, including **CAD 12,000 reserve**.
6. Operational team accepts documented runbooks, support rota, escalations and residual risks by W24.

## Scope

**In:** school and candidate record management; candidate registration; examination selection; validation and duplicate identification; role-based access; confirmation; operational reports/export; legacy-data reconciliation for transition; training and handover.

**Out:** payments and refunds; advanced analytics; mobile-native apps; national identity data feeds; enhancements after the W21 release unless separately approved. See [WBS](03-scope-wbs-and-schedule.md).

## Key milestones and constraints

W2 concept approval; W5 baseline; W13 feature-complete baseline; W17 test/operational readiness; W18 pilot; W21 expanded release; W24 closure. No cutover if critical defects remain. School-term availability, staff capacity and data quality constrain rollout.

## Delivery governance and delegated authority

- **Sponsor:** owns business case, funding and final gate authority.
- **Business Owner:** approves business processes, requirements and UAT acceptance.
- **Project Manager:** integrates plan; reports status; chairs risk, issue and change process; proposes corrective action; may replan within authorized tolerance but cannot expand baseline scope or budget unilaterally.
- **Technical Lead:** accountable for design and technical quality.
- **QA Lead:** produces objective gate test evidence and defect severity recommendation.
- **Operations Lead:** accepts live service and handover.
- **Change Control Board (CCB):** sponsor, business owner and technical lead review material scope/cost/schedule effects; Sponsor approves release of reserve.

## Funding and tolerances

Funding ceiling **CAD 240,000**; **CAD 228,000** planned base work plus **CAD 12,000** contingency. PM escalates forecast overruns beyond ceiling, release-gate misses, material scope changes and any unresolved P0/P1 at proposed go-live.

## Top baseline risks

Legacy candidate data duplicates, peak registration-period dependencies, access-control failures, uneven school training uptake, and unavailable UAT subject-matter experts. Owned responses in [RAID register](../registers/raid.csv).

## Approval record (simulation)

| Role | Action | Scenario state |
| --- | --- | --- |
| Sponsor | Approves baseline and tolerance | Illustrated approved W5 |
| Business Owner | Confirms acceptance approach | Illustrated approved W5 |
| Technical Lead | Confirms feasible delivery approach | Illustrated concurred W5 |

**Evidence caution:** approvals above are fabricated for the worked simulation and must not be presented as actual signatures or dated records.

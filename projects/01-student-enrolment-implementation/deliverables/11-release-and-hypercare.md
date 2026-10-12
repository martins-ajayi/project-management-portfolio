# 11 | Release readiness, cutover, rollback and hypercare

## Release strategy — scenario

**Wave 1 W18:** 10-school pilot. **W20:** pilot evidence review and sponsor expansion authorization. **Wave 2 W21:** 40 additional schools, contingent on renewed gate. **W22–W23:** focused hypercare. **W24:** service handover and administrative closure.

## W17 go/no-go control points

- [x] 180/180 illustrative UAT cases passing; 0 P0/P1 open (simulated W17 evidence).
- [x] REQ-04 duplicate validation retested; data reconciliation exceptions dispositioned.
- [x] Access and least-privilege checks reviewed.
- [x] Admin and school training plan meets applicable pre-release threshold.
- [x] Incident contacts, support rota, monitoring, runbook, backup/rollback instructions accepted.
- [x] Sponsor authorizes pilot subject to recorded QA, Business Owner and Ops recommendations.

All checkmarks describe the **fictional successful scenario** and are not actual sign-off evidence.

## Cutover runbook — examples

| Step | Relative window | Owner | Verification / rollback trigger |
| --- | --- | --- | --- |
| 1 | W18 pre-window | PM / Ops | Confirm gate decision, contact tree and freeze |
| 2 | W18 pre-window | Data Lead | Import/reconcile approved candidate reference set |
| 3 | W18 window | Technical Lead | Enable application for 10 authorized schools |
| 4 | W18 window | QA Lead | Smoke tests: registration, validation, confirmation, access |
| 5 | W18 +1 day | Ops Lead | Review incident queue, support hours, data reconciliations |
| 6 | W20 | Sponsor | Approve or defer 40-school expansion |

**Rollback trigger:** P0/P1 registration integrity/security failure or sustained inability to register eligible candidates beyond agreed operational tolerance. Operations Lead invokes documented rollback; Technical Lead executes; PM coordinates communications and decision log. Do not alter submitted records without an approved reconciliation plan.

## Hypercare and handover

Track daily incidents, defect priority, availability, registration completion, unresolved data exceptions, training/support demand. Handover includes named support owner, escalation tree, monitoring, knowledge base, training material, residual RAID and benefits baseline. Do not close simply because the software is deployed.

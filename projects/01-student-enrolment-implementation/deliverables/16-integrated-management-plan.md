# 16 | Integrated project management plan — control framework

**Status:** Reconstructed demonstration | **Baseline:** W5 | **Duration:** 24 weeks | **Authorized ceiling:** CAD 240,000 including CAD 12,000 contingency. All particulars are illustrative.

## Management approach and tolerances

The PM integrates the charter, scope, WBS, resourcing, risk, communication, quality and transition plans into a single baseline. Weekly forecasting distinguishes approved baseline, current forecast, variance, mitigation and decisions. The Sponsor alone approves material scope/cost changes or go/no-go. The PM may coordinate corrective action within approved tolerances but does not retroactively redefine acceptance.

| Management area | Baseline control | Review cadence | Exception action |
| --- | --- | --- | --- |
| Integration | Integrated milestone register and governance gates | Weekly | Escalate decision impacting another workstream |
| Scope | Signed statement, exclusions, WBS and requirement baseline | Each proposed change | CCB review of scope/cost/schedule impacts |
| Schedule | M-01–M-08 dependency-linked milestones W2–W24 | Weekly | Reforecast and protect release gate; escalate if threatened |
| Cost | CAD 228k work packages + CAD 12k controlled contingency | Weekly | Sponsor approves reserve, forecast and cap effects |
| Resources | Named role owners and capacity commitments | Weekly / at phase change | Prioritize critical path capacity; resource trade-offs |
| Quality | RTM, tests, 95% UAT threshold, 0 P0/P1 at release | At tests and gates | Block release; raise issue and corrective action |
| Risk/issues | Owned RAID, likelihood/impact and response triggers | Weekly; immediately for critical | Raise issue, name owner, escalate and document decision |
| Communications | Stakeholder segmentation and explicit steering asks | Daily / weekly / biweekly | Change channel/cadence for critical exceptions |
| Procurement/vendor | No third-party procurement claimed in this reconstruction | If introduced | Assess SOW, security, SLA, onboarding and contract gates before commitment |
| Stakeholders | Register/RACI and training champions | Milestone and release waves | Re-engage groups whose adoption or signoff is at risk |
| Transition | G3, G4, runbook, rollback, hypercare and Ops acceptance | W17 onward | No launch without operational readiness evidence |
| Benefits | Named owner; measures at 30/60/90 days after release | At closure and thereafter | Record variance and trigger improvement action |

## Baseline and reporting hierarchy

**Source of truth:** Charter v1.0 → approved scope/requirements → milestones/budget → weekly status → log of changes and decisions → gate decisions → operational handover. A change is effective only once approved, logged, communicated and reflected in affected baselines. A verbal request has no binding effect.

## Escalation thresholds

- Proposed overrun beyond CAD 240k or unapproved reserve use.
- Open P0/P1 before planned go-live, loss of data integrity, or unresolved access/privacy concerns.
- Missed gate or material probability of missing W18/W21 rollout commitments.
- Unresolved inter-team dependency threatening the critical path.

## Example of active integration control

At W16, the PM links issue **I-01** to REQ-04/08, affected tests UAT-04/UAT-08, milestone M-04, change CHG-01, decision DEC-02, forecast EAC **CAD 236k**, and conditional W18 pilot. Each artifact tells the same story; the sponsor can trace the reason for the corrective action.

# 05 | Stakeholders, RACI, communications and decision rights

## Governance forums — worked example

| Forum | Frequency | Purpose / evidence | Chair or accountable role |
| --- | --- | --- | --- |
| Daily delivery huddle | Daily during build/test | Blockers, priority, next action | Delivery Lead |
| PM integrated review | Weekly | Schedule, cost, RAID, resourcing, dependencies | Project Manager |
| Business walkthrough | Biweekly build; weekly UAT | Requirement and demo feedback | Business Owner |
| Change Control Board | Ad hoc, within 2 business days of material change | Approve/reject baseline change and reserve use | Sponsor |
| Steering / sponsor review | Biweekly; immediate critical escalation | RAG, forecast, decisions and gate status | Sponsor |
| Release go/no-go | W17 and W20 | Objective checklists, accept/reject/conditional decision | Sponsor |

## Decision and escalation pathway

**Team → functional owner → PM → CCB/Sponsor.** Escalate immediately if a P0/P1 defect threatens the next gate, forecast breaches the CAD 240k ceiling, unauthorized scope change is proposed, privacy/security incidents occur, or critical dependencies cannot be resolved within tolerance.

- PM maintains one source of truth for issue owner, impact, mitigation, response due date and decision reference.
- QA Lead can recommend a gate block; Business Owner must confirm acceptance; Sponsor owns the go/no-go decision.
- Operations Lead may withhold operational acceptance until readiness criteria are evidenced.

## Communication tailoring

| Audience | Cadence / method | Information needed | Owner |
| --- | --- | --- | --- |
| Sponsor & steering | Biweekly 1-page executive status + exception calls | RAG, forecast, decisions, risk exposure, asks | PM |
| Business Owner / administrators | Weekly product/demo review | Requirements, workflow decisions, UAT issues | BA + PM |
| Schools | Ahead of release; training waves | Eligibility, schedule, how-to, support contact | Change Lead |
| Engineering / QA / Data | Daily huddle; weekly integration | Blockers, defects, interface/data dependencies | Technical/QA Leads |
| Operations | Weekly from W14, daily hypercare | Ownership, cutover, monitoring, open risks | Operations Lead |

**Further detail:** [stakeholders.csv](../registers/stakeholders.csv), [raci.csv](../registers/raci.csv), [actions.csv](../registers/actions.csv). The populated registers contain fictional role names only, never real individuals.

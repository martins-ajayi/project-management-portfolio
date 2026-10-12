# Student Enrolment Management System Implementation

**Delivery lens:** End-to-end project management | Hybrid delivery | Business systems implementation

> **Reconstructed case study / illustrative scenario.** Inspired by Martins' resume-described work coordinating the design, implementation, testing, training and deployment of enrolment-management software. Specific scale, schedule, budget, risk events and results below are hypothetical teaching examples, not claims of historical project outcomes.

## Executive case

A distributed education-administration operation needed a more reliable way to capture student registrations, maintain school and candidate records, select examinations, validate enrolments and issue confirmations. Fragmented manual processes created rework and low visibility. The initiative was to implement a role-based registration platform with auditable validation and a staged rollout.

### Illustrative delivery baseline

| Control | Worked-scenario baseline |
| --- | --- |
| Duration | 24 project weeks, W1–W24 |
| Cost ceiling | CAD **240,000**, including **CAD 12,000 contingency** |
| Pilot / expansion | 10 schools at W18; 40 additional schools at W21 |
| Approach | Predictive gates for approval, design, UAT and release; iterative delivery for solution increments |
| Benefit targets | ≥95% completion of eligible registration submissions; ≥90% training completion before release |
| Quality gates | ≥95% UAT pass rate and 0 open P0/P1 defects before go-live |

### Project manager's delivery mandate — **scenario role framing**

Define and protect the baseline; coordinate analysts, design, engineering, QA, business owners and support; maintain RAID and decision visibility; secure stage-gate decisions; plan readiness and training; and provide an operationally supported rollout. These illustrate the responsibilities of the PM role in the scenario, not independently verified claims about specific historical acts.

## Delivery story: from intent to operational readiness

1. **W1–W2 — authorize:** define the problem, options, benefits, boundaries, sponsor and decision rights.
2. **W3–W5 — baseline:** validate registration workflows, confirm requirements, agree capacity and cost, set controls and entry/exit gates.
3. **W6–W13 — build iteratively:** coordinate configurable increments with demos, defect triage and requirements traceability.
4. **W14–W17 — assure:** system test, migration dry-runs, security/access checks, training and UAT. At W16, migration duplicates create an **illustrative Amber escalation**.
5. **W18–W21 — deliver:** release to a 10-school pilot at W18; expand to 40 additional schools at W21 after pilot evidence and a gate decision.
6. **W22–W24 — transition:** supported hypercare, operational ownership, acceptance, benefits handoff and closure.

### Illustrative exception that tests project-management judgment

At W16, duplicate legacy student identifiers are found in a migration rehearsal. The issue blocks UAT sign-off and puts W18 pilot readiness at risk. The PM does **not** quietly mark UAT complete. Instead, the worked scenario escalates the issue, recommends a validation control and extra retest capacity, draws **CAD 8,000 from the approved CAD 12,000 contingency**, and requires a new quality gate. W17 passes the exit criteria, preserving the W18 pilot. See [status report](deliverables/13-week-16-executive-status.md) and [change/decision record](deliverables/14-change-request-and-decision.md).

### Example outcomes — simulated, **not actual performance claims**

| Target | Worked illustrative result at W24 |
| --- | --- |
| UAT exit: ≥95% pass and zero open P0/P1 | 180/180 passed; 0 open P0/P1 |
| Pilot / rollout gated | 10 pilot schools W18; 40 additional W21 |
| ≥95% eligible registration completion | 97.8% sample performance |
| ≥90% training completion | 95% sample training completion |
| Cost ≤CAD 240,000 | Estimated actual spend CAD 236,000; CAD 4,000 unused reserve |

## Inspect the project evidence

| Lifecycle | Document | Management judgment illustrated |
| --- | --- | --- |
| Initiate | [Business case and options](deliverables/01-business-case.md) | Why invest and which option to select |
| Initiate | [Charter](deliverables/02-project-charter.md) | Authority, boundaries, success and governance |
| Plan | [Scope, WBS and baseline](deliverables/03-scope-wbs-and-schedule.md) | Deliverables, exclusions, sequencing, gates |
| Plan | [Requirements & traceability](deliverables/04-requirements-and-acceptance.md) | Business needs mapped to evidence |
| Plan | [Governance and stakeholder plan](deliverables/05-governance-and-comms.md) | Decision rights, forum cadence and escalation |
| Plan | [Resources and financial control](deliverables/06-resourcing-and-cost-control.md) | Cost baseline and contingency discipline |
| Plan | [Hybrid execution plan](deliverables/07-hybrid-execution-and-quality.md) | Iteration-level delivery within stage-gates |
| Execute | [Risk, issue and dependency control](deliverables/08-raid-and-escalation.md) | Preventive management and escalation |
| Assure | [UAT, quality and traceability](deliverables/09-uat-and-quality.md) | Exit criteria and non-negotiable sign-off |
| Assure | [Data migration and privacy](deliverables/10-data-and-security-readiness.md) | Migration integrity and secure access |
| Deploy | [Release, cutover and hypercare](deliverables/11-release-and-hypercare.md) | Controlled production transition |
| Close | [Handover, closure and benefits](deliverables/12-handover-and-benefits.md) | Operational acceptance, residual risk and benefits |
| Control | [Executive status: W16](deliverables/13-week-16-executive-status.md) | Transparent Amber status and leadership asks |
| Control | [Change request + decision](deliverables/14-change-request-and-decision.md) | Documented alternatives and approval |
| Support | [Demonstration pack index](deliverables/15-artifact-map-and-interview-notes.md) | Explain work coherently in interviews |
| Control | [Integrated management plan](deliverables/16-integrated-management-plan.md) | Explicit tailoring and exception tolerances |
| Deploy | [Pilot review & expansion gate](deliverables/17-pilot-review-and-expansion-gate.md) | Release wave decision based on evidence |
| Execute | [Iterative delivery/backlog](deliverables/18-iterative-delivery-backlog-sample.md) | Agile practices inside hybrid controls |
| Govern | [W16 steering decision minutes](deliverables/19-week-16-steering-minutes.md) | Executive decisions, action ownership and follow-up |

## Working control registers

CSV files under [`registers/`](registers/) contain populated scenario examples for milestones, budget, stakeholders, RACI, requirements, RAID, UAT, backlog, change/decisions, cutover, benefits, and actions. Eight named UAT cases are representative samples from the illustrative 180-case aggregate, not a full enumeration. Use the Excel workbook for consolidated monitoring and filtering.

## Privacy and credibility

- No workplace, client, examination board, or school names are included.
- The original implementation theme and high-level responsibilities come from the supplied resume.
- The data and chronology are **fictional reconstructions for portfolio demonstration** and must never be passed off as actual employer records.
- This is a **project management case study**, not source code for a working student enrolment product.

# 08 | Risk, assumption, issue and dependency management

## Working discipline

A risk is a **future uncertain event**; an issue is an **event already occurring**; assumptions must be validated; dependencies need owners and dates. These are separate record types even though the consolidated RAID register displays them together.

**Rating:** Likelihood (L) and impact (I) scored 1–5, risk exposure L×I; 15–25 High, 6–14 Medium, 1–5 Low. Scores guide prioritization, not statistical probability. A P1 unresolved defect blocks go-live regardless of its numerical score.

## Top scenario threats

| Ref | Threat / event | Response and trigger |
| --- | --- | --- |
| R-01 | Duplicate/invalid legacy IDs contaminate import | Data profiling; sample reconciliation; invoke remediation if repeated duplicate IDs found |
| R-02 | School SMEs not available for UAT | Book windows early; alternates; escalate if coverage falls below plan |
| R-03 | Role access enables unauthorized record visibility | Security design review, negative test and access attestation |
| R-04 | Adoption/training under target | Segment training, champions, support readiness and exit threshold |
| D-01 | Import mapping sign-off needed before migration run | Data Lead owns; Business Owner confirms source-of-truth precedence |

## Illustrative risk materialization

At **W16**, R-01 becomes active issue **I-01** when duplicate identifier mapping causes failed UAT checks. PM moves status to **Amber**, escalates, records workarounds and requests an $8,000 contingency draw. **DEC-02** approves remediation and retesting subject to evidence; a W17 test clears the blocking defect. See [RAID](../registers/raid.csv), [executive status](13-week-16-executive-status.md) and [change](14-change-request-and-decision.md).

## Response clock (hypothetical)

- P0/P1 / suspected privacy exposure: immediate notification, no release without explicit resolution and validation.
- Gate-threatening issue: PM escalation same working day; sponsor decision within 2 business days.
- Other issues: weekly RAID review with owners, due dates and evidence of closure.

**Closure standard:** issue may be closed only when evidence and accountable acceptance are linked, not because a planned due date has passed.

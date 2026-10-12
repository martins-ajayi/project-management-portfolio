# 14 | Change request CHG-01 and decision DEC-02

**Type:** Corrective action within existing scope and cost ceiling | **Raised:** W16 | **Scenario status:** Approved W16; verified W17

## Event and need

Issue **I-01**: duplicate candidate identifiers fail import reconciliation and UAT-04. The defect threatens gate G3 W17 and pilot W18. Without additional mapping validation and regression coverage, the team cannot meet its data-integrity acceptance criterion.

## Alternatives considered

| Alternative | Time / cost | Business risk | Recommendation |
| --- | --- | --- | --- |
| A. Accept defect and launch | No immediate incremental spend | Unacceptable registration integrity; violates no-P1 gate | Reject |
| B. Correct mapping using existing spare capacity only | No reserve draw, uncertain W17 completion | Pilot delay risk greater | Not preferred |
| **C. Add targeted validation and retesting** | **$8,000 draw from $12,000 contingency; no baseline ceiling change** | Lowest tested path to W17 gate | **Approve subject to evidence** |

## Integrated impact

**Scope:** approved registration-validation scope unchanged; no new product feature. **Schedule:** W18/W21 milestone targets unchanged conditional on W17 retest. **Cost:** forecast total **$228k base + $8k reserve = $236k**, leaving **$4k** within the **$240k approved ceiling**. **Quality:** negative duplicate-ID tests and migration reconciliation become explicit gate evidence.

## Decision and closure

**DEC-02 scenario:** Sponsor approves alternative C W16; Business Owner confirms business priority; Technical Lead and QA Lead commit remediation and evidence. PM updates budget forecast, RAID and G3 pack. **W17 scenario evidence:** 180/180 UAT pass, zero open P0/P1, issue I-01 closed. CHG-01 marked implemented after gate validation.

**Not a historical approval:** these are intentionally populated illustration records. Actual change forms and real approvals were not supplied.

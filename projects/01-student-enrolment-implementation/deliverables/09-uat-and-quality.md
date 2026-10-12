# 09 | UAT strategy, defect governance and sign-off rules

## Objective

Prove critical registration, validation, authorization, examination selection, confirmation and admin export workflows in business-like conditions, including negative cases and migration exceptions.

## Roles and entry conditions

Business Owner approves UAT scope and participants. QA Lead controls execution and evidence. BA links cases to approved requirements. Technical Lead owns defect remediation. PM assures availability, coordination, reporting and gate integrity. Entry requires a stable test environment, privacy-safe synthetic candidate data, reviewed cases and reconciled test fixtures.

## Exit criteria — fictitious baseline

- **At least 95% of the full planned UAT suite passes**; blocked/unexecuted cases count against completion for the gate report.
- **Zero open P0/P1** defects, with no undocumented acceptance of security or data-integrity defects.
- Must-have requirements all linked to passing evidence.
- Business Owner signs business acceptance, QA validates evidence, Operations confirms readiness independently.

## Sample W16 situation — **not a historical test record**

**180 planned cases:** 169 passed, 5 failed, 6 blocked; effective pass rate **93.9%**. One P1 data-duplication issue I-01 blocks UAT gate G3. The PM reports Amber rather than requesting an exception to the P1 rule.

## Remediation path

Run approved deduplication mapping, reconcile imported samples, add negative tests, execute full critical-path regression and re-run UAT-04. **Simulated W17:** 180/180 pass, P0/P1 open = 0; QA recommends acceptance, Business Owner agrees, and release gate can proceed if operations checks also pass.

See [UAT cases](../registers/uat_cases.csv), [traceability](../registers/requirements_traceability.csv), [readiness](../registers/release_checklist.csv).

# 10 | Data migration, privacy and security readiness

## Controlled transition

This case uses **synthetic sample data only**. Historical project data, candidate records, student identifiers, school names, credentials and source configurations are not included.

## Migration workstream

1. Agree the business system of record and mapping rules (REQ-08).
2. Profile sample quality: missing data, duplicate IDs, invalid examination codes, role ownership.
3. Perform migration dry-run; report loaded, rejected and quarantined records by batch.
4. Reconcile sampled records to approved rules, exceptions and counts; Business Owner acknowledges exception disposition.
5. Lock approved mappings for release candidate and retain a documented fallback.

## Access and assurance

Role-based access for school representative and exam administrator; least privilege; logged changes to candidate records; retention and audit obligations to be approved by the relevant organizational owner. This portfolio does **not** assert compliance certification or specific statutory implementation.

## Illustrative W16 data exception

A rehearsal finds duplicate legacy candidate IDs in imported data (I-01). Rehearsal output is quarantined; issue classified P1 due to registration integrity risk. DEC-02 authorizes revised mapping controls and retest. W17 evidence is required before W18 launch; operations must acknowledge residual data-quality monitoring.

## Release gating

No promotion if validation rules fail, security/access tests are not accepted, reconciliation exception volumes are unreviewed or rollback capability is not rehearsed. The Sponsor holds final authority for go/no-go; QA and Ops retain explicit sign-off roles.

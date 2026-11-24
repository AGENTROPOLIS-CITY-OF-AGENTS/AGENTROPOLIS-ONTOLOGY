# POWER54 — cross-repository architecture proposal
Status: DRAFT / non-executable / 2026-11-23. No new repository, runtime authority, deployment or production policy change authorized.

## Evidence and ownership
Targeted GitHub discovery located ONTOLOGY, ATG, AGENT-ENTITY-FORGE, MATH54, EVOLVE54, 54T, AEGIS-ASSURANCE and HERMES-ENTITY-54 in AGENTROPOLIS-CITY-OF-AGENTS. APEX54 repository ownership remains unresolved; do not assume 54T is its implementation. Full two-organization census remains pending.
Reuse ONTOLOGY docs/AGENT-ENTITY-ONTOLOGY.md, docs/MARKET-EVIDENCE-ONTOLOGY.md and ontology/simulation-epistemic-classes.yaml; ATG docs/ATG-PROFILE-LINK.md and docs/ATG-PROFILE-VERIFY.md; 54T docs/threat-model.md. MATH54 README confirms mathematical/spatial scope; governance module ownership needs review. No POWER54 matches or PRs found in targeted ONTOLOGY search; this is not proof of global absence.

## Semantics
Galbraith: condign (sanctions), compensatory (incentives), conditioned (belief formation). Greene: strategic pattern hypotheses, not validated laws or intent detection. Foucault and Machiavelli: interpretive institutional lenses. Record bibliographic provenance, alternative explanations and disconfirming evidence. No personality scoring, covert persuasion, protected-trait profiling or automatic sanctions.

Proposed contracts (reuse existing equivalent types after schema census):
- PowerRelation: id, source_entity_ref, target_entity_ref, mechanism (condign|compensatory|conditioned|unknown), scope, valid_from, valid_until, evidence_refs, epistemic_status, review_status.
- AuthorityGrantRef: existing grant/envelope reference, issuer, subject, scope, expiry, revocation reference. Never a second authority store.
- DependencyRelation: id, provider, consumer, resource, demand_weight, criticality, alternatives, evidence_refs, validity.
- StrategicPatternClaim: id, taxonomy_ref, observed_behavior_refs, alternative_explanations, disconfirmation, confidence (nullable unless calibrated), review_status, evidence_refs.
- AppealRef: decision_ref, review_route, status, outcome_receipt_ref.
All references use existing persistent AGENT-ENTITY identity; runtime/model changes do not mint identity. Observed, inferred, hypothetical, disputed and invalidated are distinct. Missing evidence yields unknown; synthetic outcomes never become observed facts without external evidence. Access to evidence is scoped and minimized.

## ATG:POWER
Proposed read-only OBSERVE/ASSESS semantic IR: version, operation, principal_ref, subject_ref, scope, evidence_refs, requested_metrics, policy_ref, receipt_required. Validate against existing ATG kernel; use VERIFY and existing Execution Envelope. No implied mutation, sanction, payment, deployment or permission grant. Persisting observations requires separate authorization.

## Quantitative research
HHI = sum(s_i^2), where s_i is provider share of critical demand, normalized over a defined service/time scope. Reject negative weights, duplicate demand and invalid normalization; zero demand returns unknown. Report denominator, coverage, assumptions and sensitivity. For multi-provider demand allocate shares explicitly; do not double count. Single-point failure exposure = weighted demand lost / total demand under provider removal. Revocation coverage = verified revocable active grants / active grants; missing verification is not success. Report metrics separately; no universal power score or automatic policy threshold.
Reference HHI fixtures: [1] => 1; [.5,.5] => .5; [.25,.25,.25,.25] => .25. No tests executed yet.

## EVOLVE54
Reuse Scenario, SimulationRun, SyntheticAgentState, SimulationOutcome, Forecast and CalibrationRecord. Offline seeded fixtures: provider failure, coalition concentration, reward distortion, unauthorized escalation, coordinated reputation gaming, runtime replacement. Compare baseline and mitigations, record seed, versions, assumptions, compute receipt and outcome. No real credentials, users, funds or external actions. Forecast calibration requires independent observed evidence.

## Security
54T/APEX54 owner review: consume bounded evidence, enforce existing capability policy only. Deny unauthorized escalation; verify revocation, expiry, scope, lineage and replay resistance. High-impact actions require human approval and receipt; uncertain claims trigger review not punishment. Appeals and corrections preserve provenance. Separate analysis from execution; fail closed on authorization ambiguity. No branch protection bypass.

## Gates and acceptance
G0: complete both-org inventory, locate actual APEX54 owner, inspect open PRs, schema registries and CI; pending.
G1: ontology owner reviews this draft and reconciles types before machine schema changes.
G2: linked ATG and AGENT-ENTITY contract PRs; compatibility, malformed input and no-authority tests.
G3: MATH54 owner approves module location; EVOLVE54 offline fixtures; deterministic HHI, missing data, duplicate demand, seeded replay, synthetic/observed separation tests.
G4: security owner approves nonproduction policy integration; denial, revocation, forged evidence, circular delegation, identity continuity, false-positive and receipt tests.
G5: explicit human production approval, verified CI, rollback and audit plan. Blocked until prior gates pass.
All gates beyond draft creation remain unverified. No production execution enabled.

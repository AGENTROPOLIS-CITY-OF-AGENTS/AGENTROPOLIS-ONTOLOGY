# Runtime Security Provider Ontology

## Core distinction

```text
Policy Authority != Enforcement Provider
Detection != Authorization
Tool Availability != Permission
Credential != Mandate
Mandate != Execution
Provider Finding != Canonical Verdict
Provider Failure != Authority Expansion
```

## Entities

### RuntimeSecurityProvider
A replaceable implementation that intercepts or constrains execution.

Attributes:
- provider_id
- provider_type
- version
- deployment_scope
- trust_level
- health_state
- supported_capabilities

### CanonicalActionEvent
Provider-neutral normalized representation of a requested action.

### EnforcementDecision
Canonical decision produced under AEGIS policy:
ALLOW, DENY, STEP_UP, REDACT, REWRITE, SANDBOX, QUARANTINE.

### ProviderFinding
Security evidence emitted by a provider. Findings may influence assurance and risk but do not independently grant or revoke authority.

### RuntimeEnforcementReceipt
Evidence connecting request, policy, provider, decision, execution result, and timestamps.

## Relationships

```text
Agent -> possesses -> Credential
Agent -> operates_under -> Mandate
Mandate -> constrains -> ExecutionEnvelope
AEGISPolicy -> governs -> CanonicalActionEvent
RuntimeSecurityProvider -> enforces -> EnforcementDecision
RuntimeSecurityProvider -> emits -> ProviderFinding
EnforcementDecision -> produces -> RuntimeEnforcementReceipt
54T -> verifies -> RuntimeEnforcementReceipt
Audit -> preserves -> RuntimeEnforcementReceipt
```

## Invariants

1. Provider replacement MUST NOT change authority semantics.
2. Provider findings are evidence, never self-executing governance.
3. A provider may reduce effective capability under fail-safe policy but may not enlarge declared authority.
4. Runtime enforcement receipts remain interpretable without provider-specific software.
5. Economic authority is modeled separately from generic execution capability.

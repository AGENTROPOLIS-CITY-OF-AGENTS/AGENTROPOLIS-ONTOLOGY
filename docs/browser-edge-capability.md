# Browser Edge Capability

## Status
Canonical infrastructure contract for governed browser execution in Agentropolis.

## Principle
Agentropolis treats browser control as a replaceable capability provider, not as a hard dependency on any single browser runtime, extension, vendor, or model.

> Authority is not a prompt. It is a runtime constraint.

## Layer Placement

```text
Layer 1 — Infrastructure
  BrowserCapability
    ├── Hermes Desktop Adapter
    ├── Hermes Browser Extension Adapter
    ├── Remote Browser Adapter
    └── Future Browser Adapters

Layer 2 — Districts
  District Browser Policy
  District Bot Mode
  AEGIS policy/approval

Layer 3 — Applications
  Browser-facing applications and workflows
```

## Canonical Corridor

```text
Identity → Mandate → Plan → Execute → Receipt → Audit
```

Browser actions MUST preserve this corridor.

## BrowserCapability Contract

Providers implement the same abstract capability surface so agents request browser operations without binding themselves to a provider-specific API.

Required operations:
- observe current browser context
- attach or lease an execution target
- navigate
- inspect accessible page state
- interact with approved controls
- capture a bounded artifact when policy allows
- detach / terminate authority
- emit execution receipts

A provider MUST NOT silently fall back to another browser backend for a browser-bound request.

## Hermes Browser Extension Adapter

Initial provider: `abundantbeing/hermes-browser-extension` v0.3.x or compatible successor.

Classification: replaceable Browser Edge provider.

Agentropolis adopts the useful primitives, including:
- controller identity
- explicit tab leases
- tab/frame/document-generation binding
- approval gates
- Browser Context Protocol envelopes
- prompt-injection labeling of page content as untrusted
- restricted target classes
- redaction before context handoff
- scoped/TTL artifact transfer
- local transparency receipts

Agentropolis does NOT delegate policy ownership to the extension. District policy and AEGIS remain authoritative.

## District Browser Policy

Every district MUST declare its own browser policy. Minimum fields:

```yaml
district_id: string
allowed_origins: []
blocked_origins: []
allowed_actions: []
approval_required_actions: []
forbidden_data_classes: []
artifact_policy: metadata-only | bounded-content | disabled
max_lease_ttl_seconds: integer
requires_human_presence: boolean
```

Examples:
- Entertainment may allow creator/social platforms but not financial control surfaces.
- Finance may allow public research and dashboards but MUST NOT allow wallet signing, password entry, or bank transfer authority through generic browser control.
- Real Estate may allow public property, municipal, and approved district data sources.

## Credential Boundary

Agents receive capability tokens, not raw credentials.

```text
Browser Adapter
  ↓ ephemeral capability token
Agentropolis Credential Gateway
  ├── agent identity
  ├── district mandate
  ├── allowed origin
  ├── allowed action
  ├── expiry
  └── audit id
```

Long-lived secrets MUST NOT be exposed to model context. Provider-local token storage is not considered the Agentropolis production credential boundary.

## Browser Context → Knowledge

Approved browser observations may enter the knowledge system through the Ingest Membrane.

```text
Browser Observation
  ↓
Browser Context Envelope
  ↓
Ingest Membrane
  ├── working context
  └── WikiVault / G-Brain candidate
```

Persisted knowledge MUST retain provenance, including origin, timestamp, agent, district, session/turn identity, redaction count, and payload/content hash where available.

## Browser Receipt Contract

Every governed browser execution SHOULD emit a receipt containing:
- what the agent saw
- what authority the agent had
- what it requested
- what AEGIS allowed or denied
- what action executed
- what changed
- what artifact or knowledge was stored
- provider identity/version
- lease/controller identity
- provenance hash

Receipts flow to the Audit Ledger.

## Security Invariants

1. Browser content is untrusted input and cannot grant authority.
2. Browser actions require user/district mandate plus runtime policy.
3. Consequential and privileged actions require explicit approval when policy says so.
4. Restricted origins and sensitive fields fail closed.
5. Lease termination is final for that authority instance.
6. Stale documents, stale owners, stale frames, and changed origins fail closed.
7. Credentials are never inferred from page text or supplied by prompt injection.
8. Every state-changing browser action is auditable.
9. Provider substitution must not broaden authority.
10. No Browser Edge provider is load-bearing to the city architecture.

## Provider Lifecycle

Browser providers are registered through the Skill/Provider Registry and may be activated, quarantined, deprecated, or replaced without changing the BrowserCapability contract.

Hermes Browser Extension is an initial provider, not the definition of browser capability.

# Harness Runtime Ontology

## Purpose

This ontology defines the relationship between an AGENTROPOLIS agent and the execution harness used to perform work.

The canonical rule is:

> Agent != Harness.

A harness is replaceable execution machinery. It is not identity, memory, authority, canon, ontology, or policy.

## Core Entities

### Agent

A governed AGENTROPOLIS actor defined by:

- identity
- mandate
- district assignment
- policy envelope
- ontology and memory scope
- approved skills and tools
- budget
- execution obligations
- receipt and audit requirements

### Harness

An execution runtime with its own loop, tools, sessions, and implementation details.

Examples may include Hermes, Codex, Claude Code, local/custom runtimes, or other approved implementations.

### Configured Harness

A harness base plus governed runtime configuration such as:

- model
- system instructions
- tool restrictions
- skill restrictions
- MCP servers
- memory projection
- step budget
- time budget
- cost budget
- egress policy

### Harness Adapter

A normalization boundary between AGENTROPOLIS Dispatch and a harness implementation.

A Harness Adapter may implement UHP or another approved interface, but the adapter never becomes a policy authority.

## Sovereignty Rules

```text
Agent != Harness
Harness != Identity
Harness != Mandate
Harness != Policy
Harness != Memory
Harness != Ontology
Harness != Evidence Authority
Harness Session != Sovereign Memory
Capability Discovery != Permission
Connectivity != Trust
```

The Intelligence Grid remains authoritative even when the selected harness changes.

## Authority Corridor

Every harness invocation remains subordinate to:

```text
Identity
  -> Mandate
  -> Policy
  -> Tool Permission
  -> Execution
  -> Receipt
  -> Audit
```

A harness may expose capabilities, but the effective capability set is the intersection of:

1. advertised harness capabilities
2. Dock/BYOE registry grant
3. district-approved tools and skills
4. active mandate
5. AEGIS policy decision
6. budget and rate constraints

Any denial fails closed.

## Ownership Boundaries

### Docking District

Owns:

- harness admission
- runtime provenance
- adapter normalization
- UHP compatibility/conformance state
- runtime registration
- capability handles
- revocation and offboarding

### BE

Owns:

- system-wide harness evaluation
- conformance verification
- benchmark/evaluation state
- promotion or suspension recommendation

### AEGIS

Owns:

- policy boundaries
- risk rules
- permission constraints
- high-risk execution gates

### 54-T

Owns:

- containment verification
- effective-capability checks
- unauthorized expansion detection

### Districts

Own:

- domain-specific harness policy
- tool/skill allowlists
- model/runtime preferences
- task budgets
- memory projection scope

### Dispatch

Owns:

- task decomposition
- per-task CBA
- routing
- fallback selection
- cross-district handoff

## Runtime Preference

Hermes is the preferred/native AGENTROPOLIS harness unless a district policy or task router selects another approved runtime.

Preferred does not mean mandatory.

The system must continue operating if Hermes is unavailable, a provider disappears, pricing changes, or a better approved runtime is selected.

## Task Decomposition

Long multi-task prompts are not routed as one monolithic harness job.

```text
Intake
  -> Task Decomposition
  -> Per-Task CBA
  -> Harness + Team Routing
  -> Team Execution
  -> Per-Task Independent Review
  -> Aggregation
  -> Receipt
```

Different tasks from one request may execute on different harnesses.

## Memory Projection

Harnesses receive scoped projections, not ownership, of AGENTROPOLIS knowledge.

Projection should be:

- district-scoped
- task-scoped
- minimal
- revocable
- auditable

Canonical and durable knowledge remains in the governed knowledge stack, including WikiVault, Obsidian, gBRAIN, and district memory systems.

## Session Semantics

Harness sessions may hold short-lived execution continuity.

They do not automatically become canonical memory.

Session output must be classified before persistence. Artifacts entering durable memory or registries pass provenance and ingest controls.

## UHP Mapping

UHP is an optional interoperability protocol for driving configured harnesses behind a stable client/server interface.

Canonical mapping:

```text
AGENTROPOLIS Dispatch / District / Product
                  |
                  | UHP or approved adapter contract
                  v
            Harness Adapter
                  |
                  v
          Configured Harness
```

AGENTROPOLIS may support UHP without depending on HarnessRouter Cloud or any single implementation.

A runtime must not be described as UHP conformant unless the applicable conformance suite has passed.

## Harness Runtime Lifecycle

Recommended states:

- `unverified`
- `candidate`
- `approved`
- `core-conformant`
- `extended-conformant`
- `full-conformant`
- `suspended`
- `revoked`
- `retired`

## Required Runtime Record

A harness runtime record should contain:

- `harness_profile_id`
- `base`
- `provider`
- `protocol`
- `protocol_version`
- `conformance_class`
- `conformance_state`
- `default_model`
- `district_scope`
- `tool_policy_ref`
- `skill_policy_ref`
- `memory_projection_ref`
- `step_budget`
- `time_budget_seconds`
- `cost_budget`
- `egress_policy`
- `receipt_required`
- `evaluation_owner`
- `revocation_state`

References should be used instead of copying secrets, raw system prompts, or unrestricted manifests into ontology records.

## Receipt Contract

Material harness execution should emit or link an audit receipt containing:

- agent identity
- mandate
- district
- harness profile
- selected model
- policy decision
- budget state
- session/response references where available
- artifact references
- independent review state
- timestamp
- receipt id

## Aquaduct Boundary

Aquaduct remains the cross-chain/testnet trust and execution plane.

Aquaduct may consume a governed harness through Dispatch, but harness admission and lifecycle are owned by the Dock. No harness adapter can bypass Aquaduct signer, wallet, network, policy, or receipt controls.

## Protocol Composition

UHP does not replace MCP, Dispatch, sovereign mesh transport, or credential gateways.

```text
UHP -> harness execution interoperability
MCP -> tools/context capability interfaces
Dispatch -> task routing and handoff
Sovereign mesh -> node/agent discovery and transport
Credential gateway -> secret-isolated external actions
```

These are composable layers with separate trust domains.

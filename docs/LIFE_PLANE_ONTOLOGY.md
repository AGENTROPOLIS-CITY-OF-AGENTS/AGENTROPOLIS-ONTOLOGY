# Life Plane Ontology

The Life Plane ontology defines the minimum city-wide entities and relationships required for a living, event-driven AGENTROPOLIS without allowing renderers, districts, harnesses, or social systems to become authority roots.

## Core entities

- `CityEvent`
- `DistrictEnvironment`
- `AgentPresence`
- `WorldStateProjection`
- `ExecutionEnvelopeRef`
- `MandateRef`
- `ReceiptRef`
- `DenialRef`
- `PolicyDecisionRef`
- `ThermodynamicObservation`
- `RelationshipEdge`

## Invariants

1. Presence is not permission.
2. Communication is not authority.
3. Renderer state is not canonical state.
4. A district may own local state but not city sovereignty.
5. Every material execution must be attributable to identity, mandate, policy context, and an execution envelope.
6. Every material success or denial must emit evidence suitable for audit.
7. Public projections are derived read models, never mutation authorities.
8. Entropy and drift are observations, not autonomous policy decisions.

## CityEvent

A `CityEvent` is a normalized event envelope carrying at minimum:

- event id
- event type
- timestamp
- source identity
- source system
- district/institution context when applicable
- subject references
- payload reference or bounded payload
- provenance
- signature/attestation reference where supported
- mandate reference when execution-related
- execution-envelope reference when execution-related
- policy/risk reference when material
- receipt/denial reference when terminal
- visibility classification
- replay/idempotency key where applicable

## DistrictEnvironment

A `DistrictEnvironment` represents a bounded institutional runtime context. It declares:

- district identity
- version
- authority scope
- local state namespaces
- capability surface
- accepted event classes
- emitted event classes
- policy/risk class
- execution-envelope constraints
- projection rules
- health state
- pause/revoke behavior

## AgentPresence

`AgentPresence` represents observable addressability or activity. It must never be interpreted as permission.

Recommended states:

- `offline`
- `available`
- `active`
- `degraded`
- `paused`
- `revoked`
- `unknown`

## WorldStateProjection

A `WorldStateProjection` is a derived view of canonical city state for a particular consumer such as WORLD, MAIN STREET, MISSION CONTROL, POCKET, or an external public API.

It must identify:

- source state version
- projection consumer
- visibility scope
- generated timestamp
- included entity references
- omitted/redacted classes
- integrity/provenance reference

## RelationshipEdge

Relationships are explicit edges, not inferred authority.

Examples:

- agent `present_in` district
- agent `assigned_to` mandate
- mandate `authorized_by` human authority
- task `executed_by` agent
- receipt `evidences` execution
- district `depends_on` infrastructure
- projection `derived_from` canonical state
- event `observed_by` subsystem

## Thermodynamic observations

The Life Plane consumes existing AGENTROPOLIS entropy/drift concepts to observe city behavior. At minimum, observations should support:

- entropy
- drift
- stability
- friction
- compute/load
- recovery
- repeated-action rate
- policy-denial rate

These observations may inform policy evaluation but never independently grant authority.

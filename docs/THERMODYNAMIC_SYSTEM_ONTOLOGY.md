# AGENTROPOLIS Thermodynamic System Ontology

Status: active infrastructure doctrine

## Scope

AGENTROPOLIS uses thermodynamic language as an operational systems model for cognitive and agentic infrastructure. It does not claim that software literally obeys physical thermodynamic law.

The vocabulary gives the city a shared way to reason about resource input, useful output, friction, disorder, drift, stability, and recovery.

## Core state

```text
Energy In -> Compute Load -> Coordination Friction -> Value Out
                 |                    |
                 v                    v
              Entropy <-----------> Drift
                 \                    /
                  -> Stability / Recovery
```

## Classes

- `ThermodynamicState`
- `EnergyInput`
- `ComputeLoad`
- `ValueOutput`
- `CoordinationFriction`
- `EntropyState`
- `DriftState`
- `StabilityState`
- `RecoveryEnergy`
- `ContextPressure`
- `CapabilitySurface`
- `ObservationWindow`
- `ThermodynamicReceipt`

## Meanings

### EnergyInput
Resources consumed to make progress, including inference spend, tokens, wall-clock time, operator attention, tool calls, network calls, and local compute.

### ComputeLoad
Actual computational burden required by a task or route. It may include model inference, context processing, embeddings, retrieval, graph traversal, code execution, browser automation, and verification.

### ValueOutput
Verified useful work that satisfies the task acceptance criteria. Raw token volume, verbosity, or tool activity are not value by themselves.

### CoordinationFriction
Overhead introduced by retries, unnecessary handoffs, duplicated work, excessive agent fan-out, conflicting routes, stale context, or avoidable tool switching.

### EntropyState
Operational disorder that makes the system harder to reason about, audit, or control. Entropy can rise through tool sprawl, permission sprawl, duplicated workflows, prompt contamination, missing receipts, stale context, unresolved conflicts, and noisy governance.

### DriftState
Movement away from a known-good baseline. Drift may affect configuration, permissions, policy, prompts, dependencies, data, governance, model routes, or knowledge state.

### StabilityState
Degree to which the system remains inside expected operational and policy bounds under repeated or changing conditions.

### RecoveryEnergy
Resources required to return from degraded, drifted, or failed state to a known-good state.

### ContextPressure
Burden imposed by active inference context. Durable memory size is not the same thing as active context pressure.

### CapabilitySurface
The set of tools, permissions, models, endpoints, and actions exposed to a task. Larger capability surfaces generally increase risk and cognitive overhead.

## Relationships

| Relationship | Domain | Range | Meaning |
| --- | --- | --- | --- |
| `observedDuring` | state/metric | `ObservationWindow` | Time/task boundary for the measurement. |
| `measures` | `ThermodynamicReceipt` | thermodynamic class | Metric recorded by the receipt. |
| `appliesTo` | thermodynamic class | runtime/model/profile/workflow | Subject being measured. |
| `increases` | signal | state/metric | Signal materially raises the state. |
| `reduces` | control | state/metric | Control lowers disorder, friction, or load. |
| `derivedFromReceipt` | state | `ThermodynamicReceipt` | State was computed from traceable evidence. |
| `comparedToBaseline` | `DriftState` | baseline artifact | Known-good reference. |
| `requiresRecovery` | degraded state | `RecoveryEnergy` | Estimated or observed effort to restore stability. |

## Routing objective

Thermodynamic routing evaluates verified value rather than raw model quality alone.

```text
Thermodynamic Efficiency = Verified Value Output
                           ----------------------------------------------
                           Energy Input + Compute Load + Coordination Friction + Recovery Cost
```

This is a decision aid, not a universal scalar truth. Individual dimensions should remain inspectable.

## Model thermodynamics

A `Model` may have multiple `ThermodynamicProfile` observations by task class, provider route, hardware, context size, and time window.

A model that is excellent at one workload may be inefficient at another. Therefore AGENTROPOLIS must not assign one permanent global efficiency score to a model.

Representative dimensions:

- quality / acceptance rate
- cost per accepted task
- latency per accepted task
- retries per accepted task
- tool-call efficiency
- context efficiency
- failure recovery cost
- availability
- rate-limit pressure
- entropy introduced
- drift sensitivity

## Entropy law

Entropy is not merely token count. It is disorder.

High entropy should increase review and reduce autonomous authority where appropriate.

Examples of entropy sources:

- permission sprawl
- tool sprawl
- prompt contamination
- missing receipts
- alert fatigue
- duplicate workflows
- secret exposure
- governance noise
- stale model assignments
- contradictory knowledge without provenance

## Drift law

Drift is always measured against a stated baseline.

Representative drift types:

- permission
- policy
- config
- prompt
- dependency
- governance
- data
- model-route
- knowledge
- capability

A drift finding should include baseline, observed state, delta, risk level, recommended action, and receipt/evidence pointer when available.

## Evolving-stack law

The AI stack is expected to change.

New models, providers, skills, MCP servers, dependencies, memory artifacts, and hardware may appear or disappear without changing AGENTROPOLIS ontology law.

The system should react through:

```text
observe -> compare -> evaluate -> route -> verify -> receipt -> learn
```

not through hard-coded provider dependence.

## Deterministic-before-probabilistic law

If a result can be safely obtained through deterministic inspection, thresholding, diffing, schema validation, health checks, or fixed transforms, that work should occur before invoking probabilistic cognition.

The model should receive the smallest verified context and capability surface that still satisfies acceptance criteria.

## Memory thermodynamics

- WikiVault preserves evidence and provenance.
- Obsidian preserves durable human-readable knowledge.
- gBRAIN is a derived/rebuildable graph.
- Retrieval should follow indexes and relevant edges rather than brute-force the entire knowledge substrate.
- Compression is not backup.
- Context reduction must not erase evidence authority or provenance.

## Observatory relationship

The Intelligence Observatory measures and visualizes thermodynamic state. The ontology defines what the state means.

The Observatory must distinguish canonical baseline data from receipt-backed live observations. Preview data must never be presented as live telemetry.

## Hard invariants

1. High entropy does not grant more authority; it generally narrows or escalates it.
2. Drift requires an explicit baseline.
3. Unknown critical state fails closed until observation resolves it.
4. Thermodynamic optimization may not sacrifice acceptance criteria, evidence integrity, or policy constraints.
5. A cheaper model does not win if it fails the required task.
6. A more capable model does not win merely because it is more capable.
7. Durable memory and active context pressure remain separate concepts.
8. Every production thermodynamic claim should be traceable to receipts or clearly labeled as baseline/simulation.
9. Recovery energy is part of system cost.
10. The city remains operationally model-agnostic while its routing adapts to changing economics and capability.

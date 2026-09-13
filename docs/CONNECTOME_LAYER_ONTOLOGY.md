# AGENTROPOLIS Connectome Layer Ontology

## Status

Production architecture contract for biologically inspired cognitive topology inside the AGENTROPOLIS Intelligence Grid.

## Purpose

The Connectome Layer models a persistent, distributed cognitive-control substrate beneath agent reasoning surfaces. It may use biologically derived connectome graphs, synthetic graphs, learned graphs, or hybrid topologies to route salience, activation, memory retrieval, reflexes, specialist cognition, and escalation to model reasoning.

It does **not** assert machine consciousness, biological equivalence, sentience, emotion, or that a downloaded connectome is a complete brain.

## Canonical placement

```text
ENVIRONMENT / SENSORS / EVENTS
            |
            v
      CONNECTOME LAYER
            |
   +--------+---------+----------------+
   |        |         |                |
   v        v         v                v
SALIENCE  MEMORY   SPECIALISTS    REFLEX / FAST PATH
   |        |         |                |
   +--------+---------+----------------+
            |
       MODEL REASONING
       only when needed
            |
            v
           ATG
            |
     EXECUTION ENVELOPE
            |
      APPROVED ADAPTER
            |
       WORLD / TOOLS
            |
         RECEIPT
            |
   MEMORY + STATE UPDATE
            +---------------------> feedback
```

## Core doctrine

```text
Connectome != Agent Identity
Connectome != Consciousness
Connectome != Mandate
Connectome != Authority
Connectome != Policy
Connectome != Canon
Connectome != Evidence Authority
Activation != Permission
Salience != Truth
Simulation != Biological Equivalence
Model != Whole Agent
```

The LLM or other model is a replaceable cognitive organ/resource. The Connectome Layer is a routing and state substrate. Neither may grant itself authority.

## Classes

- `ConnectomeTopology`
- `ConnectomeNode`
- `ConnectomeEdge`
- `ConnectomeRegion`
- `ActivationState`
- `SalienceEvent`
- `ReflexRoute`
- `CognitiveEscalation`
- `MemoryCue`
- `SpecialistRoute`
- `SensorAdapter`
- `ActuatorIntent`
- `TopologySource`
- `SimulationProfile`
- `ConnectomeObservation`

## Relationships

| Relationship | Domain | Range | Meaning |
|---|---|---|---|
| `containsNode` | `ConnectomeTopology` | `ConnectomeNode` | Topology includes a node. |
| `connectsTo` | `ConnectomeNode` | `ConnectomeNode` | Directed graph edge. |
| `belongsToRegion` | `ConnectomeNode` | `ConnectomeRegion` | Node is grouped into a functional or source-defined region. |
| `derivedFrom` | `ConnectomeTopology` | `TopologySource` | Provenance of the topology. |
| `usesSimulationProfile` | `ConnectomeTopology` | `SimulationProfile` | Dynamics applied to the graph. |
| `activates` | `SalienceEvent` | `ConnectomeNode` or `ConnectomeRegion` | Event seeds activation. |
| `cuesMemory` | `ActivationState` | `MemoryCue` | State requests bounded memory retrieval. |
| `routesToSpecialist` | `ActivationState` | `SpecialistRoute` | State routes work to specialist cognition. |
| `escalatesToModel` | `ActivationState` | `CognitiveEscalation` | State requests model reasoning. |
| `proposesIntent` | `ActivationState` | `ActuatorIntent` | State proposes an action intent; it does not authorize it. |
| `constrainedBy` | `ActuatorIntent` | `Mandate`, `Policy`, `Authority`, or `ExecutionEnvelope` | Existing governance remains authoritative. |

## Topology sources

A topology may be:

- `BIOLOGICAL_CONNECTOME` — derived from published biological reconstruction data
- `SYNTHETIC_CONNECTOME` — designed graph with explicit provenance
- `LEARNED_CONNECTOME` — learned or optimized graph
- `HYBRID_CONNECTOME` — combination of biological, synthetic, and learned structure

Biological source attribution must include dataset name, species/organism, version, source URI, license, citation, transformation history, and checksum where available.

## Operating modes

### 1. Observe

Receive events and emit activation/salience telemetry. No action proposal.

### 2. Route

Use activation to select memory, specialist cognition, or model escalation.

### 3. Propose

Generate an `ActuatorIntent` for ATG evaluation.

### 4. Learn

Update permitted weights, thresholds, or routing metadata only within an explicit learning policy and versioned topology lineage.

No operating mode bypasses ATG, policy, AEGIS, 54-T validation, or the Execution Envelope.

## Fast-path rule

A reflex path may bypass expensive model reasoning but may **never bypass authority**.

```text
REFLEX EVENT
  -> CONNECTOME FAST PATH
  -> ATG INTENT
  -> POLICY / AUTHORITY CHECK
  -> EXECUTION ENVELOPE
  -> ADAPTER
  -> RECEIPT
```

## Memory rule

The Connectome Layer may cue or prioritize memory. It does not own sovereign memory and must not silently rewrite canonical knowledge. Memory writes require provenance and the owning memory policy.

## Thermodynamic integration

Connectome observations SHOULD expose:

- activation density
- propagation depth
- recurrent-loop count
- unresolved activation
- model-escalation rate
- memory-retrieval rate
- action-proposal rate
- latency
- compute cost
- entropy
- drift
- stability
- recovery time

These feed the existing AGENTROPOLIS thermodynamic ontology. High entropy or unstable recurrent activity may trigger damping, isolation, human review, or route fallback.

## Embodiment integration

Sensor adapters translate world state into bounded events. Actuator intents translate internal state into proposed external actions. Embodiment never changes the authority model.

Examples:

- visual/world-state event -> salience -> navigation specialist
- social message -> salience -> memory cue -> language model escalation
- thermal/device telemetry -> reflex route -> shutdown proposal
- city mission event -> specialist route -> planning model -> ATG intent

## Minimal event example

```json
{
  "type": "ConnectomeObservation",
  "version": "1.0",
  "agent_id": "agent:example",
  "topology_id": "connectome:flywire-derived-v1",
  "source_event": "event:camera-object-448",
  "activation": {
    "regions": ["vision", "salience"],
    "density": 0.031,
    "entropy": 0.18
  },
  "routes": [
    {"kind": "memory", "target": "memory:object-history"},
    {"kind": "specialist", "target": "specialist:spatial"}
  ],
  "model_escalation": false,
  "action_authority": "NONE"
}
```

## Governance invariant

A connectome state may prioritize, route, challenge, inhibit, or propose. It cannot grant identity, mandate, policy, authority, truth, or execution permission.

> **The connectome can decide what deserves attention. ATG decides what may become action.**

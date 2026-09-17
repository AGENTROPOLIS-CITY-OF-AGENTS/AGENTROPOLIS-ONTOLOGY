# AGENTROPOLIS Cognitive Spatial Thermodynamic Rollup

Status: proposed canonical integration contract

## Purpose

This document unifies the existing WikiVault, Obsidian, llm-wiki, gBRAIN, J-SPACE, thermodynamic, Intelligence Observatory, and Spatial Runtime doctrines into one bounded architecture.

It does not create a new source of truth. It defines how existing layers compose and how their state may be projected into 2D, 3D, AR, VR, and XR surfaces without granting renderers authority.

## Canonical roles

| Layer | Role | Authority |
| --- | --- | --- |
| WikiVault | canonical evidence and provenance substrate | evidence authority |
| Obsidian | durable human-editable knowledge and reviewed memory | human review surface |
| llm-wiki / retrieval | bounded retrieval over approved knowledge | retrieval only |
| gBRAIN | derived/rebuildable graph of attributed entities, claims, relationships, confidence, and evidence links | derived graph only |
| J-SPACE | derived deliberation and cognitive assembly surface | read-only deliberation by default |
| Thermodynamic ontology | operational state model for load, value, entropy, drift, stability, and recovery | measurement semantics |
| Intelligence Observatory | governed observability surface over topology, thermodynamics, memory evolution, and skills | read-only observability |
| Spatial Runtime | renderer-neutral compilation of governed world state into spatial form | presentation/control surface only |
| AR / VR / XR | interaction renderers over Spatial Runtime state | no truth or authority |

## Canonical flow

```text
Source Adapters
  -> Ingest Membrane
  -> WikiVault
  -> Obsidian / reviewed human memory
  -> llm-wiki / bounded retrieval
  -> gBRAIN
  -> J-SPACE
  -> AEGIS / policy gate
  -> separate execution corridor
  -> receipt
  -> thermodynamic observation
  -> Intelligence Observatory
  -> Spatial Runtime
  -> 2D / 3D / AR / VR / XR
```

Execution receipts and runtime events feed observability and thermodynamic state. They do not bypass WikiVault evidence rules or mutate canon by implication.

## gBRAIN compiler contract

gBRAIN is derived and rebuildable. Multiple compilers may contribute to the same governed graph namespace if they preserve provenance and confidence semantics.

Supported compiler classes may include:

- deterministic AST / dependency graph compilers
- WikiVault relationship exports
- reviewed Obsidian claim transforms
- receipt-derived runtime relationship compilers
- media/document semantic extraction adapters
- Graphify or equivalent local-first graph construction engines

A compiler MUST NOT become an authority source.

### Graphify position

Graphify is classified as an optional gBRAIN graph-construction adapter, not as a replacement for WikiVault, Obsidian, gBRAIN, J-SPACE, or AGENTROPOLIS-ONTOLOGY.

Graphify outputs such as `EXTRACTED`, `INFERRED`, and `AMBIGUOUS` edges MAY be normalized into gBRAIN provenance fields.

Recommended mapping:

```text
Graphify EXTRACTED  -> relationship evidence state: extracted
Graphify INFERRED   -> relationship evidence state: inferred
Graphify AMBIGUOUS  -> relationship evidence state: ambiguous / review required
```

No compiler confidence label may silently become canon authority, policy authority, permission, mandate, or execution authority.

## Memory and cognition separation

```text
WikiVault = evidence
Obsidian  = durable human-editable memory
Retrieval = find relevant material
gBRAIN    = structured relationships
J-SPACE   = deliberation over bounded evidence and graph state
```

J-SPACE may compose claims, councils, lenses, contradictions, and thought paths. It may not silently promote its synthesis into canon.

## Thermodynamic relationship

Thermodynamic state is operational metadata over the same governed system. It is not a separate knowledge truth model.

Representative dimensions:

- energy input
- compute load
- value output
- coordination friction
- entropy
- drift
- stability
- recovery energy
- context pressure
- capability surface

Thermodynamic observations SHOULD attach to stable entity identifiers, task identifiers, runtime nodes, districts, graph communities, or observation windows.

Example:

```json
{
  "appliesTo": "district/creator",
  "observationWindow": "window/2026-09-17T14:00Z",
  "entropy": 0.38,
  "drift": 0.12,
  "stability": 0.86,
  "source": "receipt-aggregate",
  "evidenceState": "OBSERVED"
}
```

## Spatial semantics

Spatial Runtime compiles governed state into visual intent. It MUST NOT invent epistemic meaning from aesthetics.

Recommended channels:

| Governed state | Spatial expression |
| --- | --- |
| activity / energy | luminosity |
| event velocity | pulse frequency |
| dispatch / tool use | traffic density |
| compute pressure | heat / distortion |
| entropy pressure | bounded turbulence / noise |
| drift | geometry instability |
| policy containment | perimeter state |
| authority / capacity | route width |
| provenance strength | inspectable evidence trail, not brightness alone |
| contradiction | visibly split or challenged relationship |
| stale projection | explicit stale state / desaturation / warning |

Visual prominence is never equivalent to truth, confidence, evidence quality, or authority.

## J-SPACE spatial cognition contract

J-SPACE MAY expose a spatial cognitive map containing bounded regions such as:

- evidence
- human-editable memory
- retrieval
- ontology
- cognition
- governance

Users MAY:

- inspect nodes and edges
- trace thought paths
- compare conflicting claims
- focus semantic regions
- assemble bounded cognitive councils
- inspect provenance and evidence states
- inspect thermodynamic pressure attached to entities or communities

Users MUST NOT gain mutation authority merely by interacting with a spatial object.

A selected node is not an approved claim. A highlighted edge is not canon. A visually central node is not sovereign.

## Memory-palace interaction language

AGENTROPOLIS may use spatial-memory interaction patterns inspired by public experimental work that treats knowledge as rooms, hubs, distributed topologies, and navigable semantic neighborhoods.

Such references are interaction inspiration only. They do not become architecture authority, ontology authority, or evidence authority.

The AGENTROPOLIS implementation remains grounded in its own evidence, governance, provenance, thermodynamic, and execution contracts.

## AR / VR / XR contract

XR is a renderer class beneath Spatial Runtime.

XR MAY provide:

- room-scale graph traversal
- hand / controller selection
- gaze-based inspection
- semantic zoom
- district portals
- thought-path tracing
- temporal replay of receipt-backed state
- thermodynamic overlays
- provenance drill-down
- accessibility alternatives

XR MUST NOT:

- maintain an independent canonical world state
- write directly to WikiVault or gBRAIN
- treat renderer position as authority
- hide evidence state behind spectacle
- expose secrets or SECURITY_ONLY material
- present simulation or preview values as live telemetry

## Cognitive-spatial state progression

The existing thermodynamic state progression applies to spatial cognition:

```text
NORMAL
  -> DRIFT
  -> ENTROPY_RISING
  -> CONSTRAINED
  -> QUARANTINED
  -> HALTED
```

This progression describes governed operational state, not emotions, consciousness, sentience, or literal physical thermodynamics.

## Graph projection minimum record

Every spatially rendered graph node SHOULD preserve enough information to resolve back to governed state:

```json
{
  "id": "stable-id",
  "namespace": "district/project/agent/task",
  "type": "entity|claim|evidence|decision|artifact|memory",
  "layer": "evidence|human_editable|retrieval|ontology|cognition|governance",
  "title": "human-readable label",
  "evidenceState": "VERIFIED|OBSERVED|DEPLOYED|IMPLEMENTED|PLANNED|UNVERIFIED",
  "confidence": 0.0,
  "sourceUri": "...",
  "sourceRef": "...",
  "provenanceHash": "...",
  "compiler": {
    "engine": "graphify|wikivault|native|other",
    "version": "...",
    "derivation": "EXTRACTED|INFERRED|AMBIGUOUS|NATIVE"
  },
  "thermodynamics": {
    "entropy": 0.0,
    "drift": 0.0,
    "stability": 0.0,
    "state": "NORMAL"
  }
}
```

All fields are bounded projections. Canonical source records remain in their owning systems.

## District federation

The graph remains hierarchical and federated:

```text
CITY
  -> DISTRICT
  -> INSTITUTION / SYSTEM
  -> AGENT
  -> TASK
```

District graphs SHOULD remain independently inspectable. City-level views may compose them without flattening namespace, policy, or authority boundaries.

## Anti-Moloch invariants

1. Retrieval relevance does not equal truth.
2. Graph centrality does not equal authority.
3. Visual prominence does not equal confidence.
4. Model confidence does not equal evidence strength.
5. Inference does not equal extraction.
6. Spatial proximity does not grant permission.
7. J-SPACE synthesis does not become canon automatically.
8. Thermodynamic optimization may not erase dissent, provenance, or safety-critical minority signals.
9. XR interaction may not widen the user's or agent's authority ceiling.
10. A graph compiler remains replaceable infrastructure.
11. Preview state must never masquerade as live telemetry.
12. The city depicts governed state transitions, not hidden model cognition.

## Implementation order

1. Normalize graph compiler provenance into gBRAIN.
2. Extend J-SPACE projection records with compiler and thermodynamic metadata.
3. Attach receipt-backed thermodynamic observations to stable graph entities.
4. Render the same projection in the existing web neural fabric.
5. Add semantic zoom and thought-path traversal.
6. Add renderer-neutral XR scene instructions.
7. Implement AR / VR / XR clients as replaceable renderers.
8. Add replay, rollback, stale-state, and provenance inspection.
9. Validate with 54-T / AEGIS before any mutation-capable interaction is introduced.

## Canonical shorthand

> WikiVault is evidence. Obsidian is memory. gBRAIN is structure. J-SPACE is deliberation. Thermodynamics is physiology. Spatial Runtime is the body. XR is how humans step inside it.

The shorthand is explanatory only. The machine contracts and authority invariants above remain controlling.

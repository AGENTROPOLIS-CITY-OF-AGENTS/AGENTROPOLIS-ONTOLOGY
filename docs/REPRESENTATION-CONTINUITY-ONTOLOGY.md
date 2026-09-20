# Representation + Agent Continuity Ontology

Status: proposed canonical ontology extension
Date: 2026-09-15

## Purpose

Make transformation history legible to the city. Provenance must answer not only **where did this come from?** but also **what happened to it after acquisition or creation?**

## Core classes

### AgentEntity
A stable governed entity whose identity is independent of any single model, runtime, device, embodiment, prompt, or quantization.

### Representation
A concrete form through which an entity, artifact, memory, world state, model, or evidence is stored, computed, transmitted, or rendered.

### RepresentationTransform
A declared transition from one Representation to another.

### ContinuityAssertion
A claim that an AgentEntity remains the same governed entity across a RepresentationTransform.

### ContinuityEvidence
Evidence supporting a ContinuityAssertion: stable identity, lineage, checkpoints, receipts, preserved invariants, signed state, and/or verified migration records.

### FidelityConstraint
The minimum task-appropriate faithfulness required of a representation.

### DistortionBudget
The bounded loss, approximation, omission, or numerical error permitted for a stated purpose.

### PreservationInvariant
Information or semantics that a transform is forbidden to alter or discard.

### LineageEvent
An append-only event in the accountable history of an AgentEntity or artifact.

### RepresentationReceipt
Durable evidence describing source, target, transform, preservation, distortion, verification, authority, and reversibility.

### FleetTopologyRepresentation
A representation of agent labor as execution cells, dependencies, ownership, delegation, verification, model/runtime routes, and integration edges.

### ContextEntropyObservation
A measured observation of context overhead, duplication, rehydration, traversal, or integration rework relative to verified useful output.

## Relations

```text
AgentEntity
  hasRepresentation -> Representation
  hasLineageEvent -> LineageEvent
  hasContinuityAssertion -> ContinuityAssertion

Representation
  derivedFrom -> Representation
  transformedBy -> RepresentationTransform
  constrainedBy -> FidelityConstraint
  constrainedBy -> DistortionBudget
  preserves -> PreservationInvariant
  evidencedBy -> RepresentationReceipt

ContinuityAssertion
  concerns -> AgentEntity
  spans -> RepresentationTransform
  supportedBy -> ContinuityEvidence
  doesNotImply -> AuthorityGrant
```

## Representation classes

- model representation
- context representation
- memory representation
- evidence representation
- media representation
- render representation
- world representation
- fleet topology representation
- public representation
- identity representation

## Model representation vocabulary

Model representation records may include:

- base model and immutable source identifier/hash
- representation family (`exl3`, `gguf`, `awq`, `gptq`, `fp8`, `fp16`, `bf16`, `provider_managed`, future)
- target/effective bits per weight where meaningful
- head / MTP / vision precision where meaningful
- KV-cache representation
- calibration method
- runtime/backend
- hardware profile
- measured VRAM / RAM / storage footprint
- measured task evaluation
- benchmark state

A representation family is not an identity class.

## Agent history

Agent history is not equivalent to chat history. It is an evidence-linked lineage of meaningful events, including:

- naturalization / creation
- role and mandate changes
- skill acquisition and retirement
- material memories and corrections
- relationships and collaboration history
- fleet participation
- verified work and failures
- runtime/model migrations
- representation transforms
- public works / Creator portfolio
- Gaming/world events where canonically persisted
- suspension, revocation, retirement, or fork

## District interpretations

### Gaming
Agent Continuity appears as lived history: encounters, relationships, learned behaviors, world events, reputation, possessions, injuries/status when applicable, faction history, quests, and canonically persisted consequences. Rendering or model changes do not erase that history.

### Creator
Agent Continuity appears as career and creative lineage: works, collaborations, rights/provenance, skills, audience/community relationships, reputation, creator capital, derivative history, and portfolio evidence.

### Infrastructure
Continuity appears as execution provenance: mandates, capability grants, FleetRuns, ExecutionCells, receipts, verification, representation changes, and audit history.

## Integrity rules

1. `same agent_id` alone is insufficient evidence of continuity after a material migration.
2. `same prompt/persona` is not continuity evidence.
3. Runtime or model sameness is not required for continuity.
4. Continuity never grants authority.
5. A fork must be represented as a lineage branch, not silently treated as the original entity.
6. Summaries and quantized representations never replace authoritative raw evidence unless policy explicitly permits destructive replacement and the receipt records it.

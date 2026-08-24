# District Knowledge Federation Ontology

Status: active infrastructure doctrine

## Core law

Agentropolis knowledge is hierarchical and federated.

```text
CITY -> DISTRICT -> INSTITUTION/SYSTEM -> AGENT -> TASK
```

Every district owns a bounded intelligence environment. The city owns the constitutional shell, shared registries, cross-district graph, provenance index, routing contracts, and global roll-up. Agents inherit the narrowest valid context required for their mandate.

> One city brain. Many sovereign district brains.

## District Intelligence Boundary

Every district MUST own or explicitly bind:

- district ontology namespace
- district protocols and policies
- district Wiki namespace
- district Obsidian vault namespace
- district llm-wiki index
- district gBRAIN namespace
- district memory and retrieval policy
- district Skill registry and evidence states
- district model policy and fallback routes
- district roles, facets, taxonomies, and vocabularies
- district authority matrix and approval gates
- district receipts, disputes, corrections, and write-back rules

A district MAY reuse shared Layer-1 infrastructure. Reuse does not erase namespace ownership or policy boundaries.

## Agent Inheritance Order

An assigned agent resolves context in this order:

```text
1. Agentropolis constitutional core
2. active district ontology
3. active district protocols and policies
4. active district knowledge indexes and evidence pointers
5. active district Skills and tool policy
6. agent role, mandate, permissions, and memory
7. task-specific context
```

The runtime MUST NOT load unrelated district knowledge by default.

## City Roll-Up

The Agentropolis city brain is a federated graph and registry, not a flattened copy of every district vault.

The global layer MAY retain:

- district identities and schema versions
- shared entities and cross-district relationships
- global doctrine, identity, policy, and routing rules
- provenance pointers and content hashes
- architecture decisions and dependency edges
- compiled district summaries
- conflict and duplicate records
- registry and deployment state
- routes back to authoritative district evidence

Raw or restricted district material remains owned by its district namespace unless a reviewed publication or sharing rule explicitly promotes it.

## Cross-District Resolution

When an agent needs knowledge outside its assigned district:

```text
agent
  -> HERMES Dispatch / district resolver
  -> target district policy check
  -> target district index or evidence query
  -> bounded response with provenance
  -> caller district context
  -> receipt
```

Cross-district retrieval never grants cross-district write or execution authority.

## Memory Fabric

```text
WikiVault = canonical evidence and provenance substrate
Obsidian  = durable human-editable knowledge surface
llm-wiki = searchable compiled knowledge/index layer
gBRAIN    = derived/rebuildable attributed graph and ontology index
J-SPACE   = derived deliberation surface
HERMES    = orchestration, routing, and reasoning surface
Models    = replaceable inference resources
```

All of these layers MUST preserve district namespace and provenance boundaries.

## Context Thermodynamics

The federation exists partly to control context pressure.

Agents SHOULD receive the smallest authoritative context surface that satisfies the task. Index-first retrieval, graph traversal, delta loading, and evidence pointers are preferred over dumping a full vault into model context.

This reduces cost, entropy, coordination friction, hallucination surface, and cross-domain contamination while preserving traceability.

## Write-Back

Reusable knowledge produced during work writes back to the narrowest authoritative namespace first.

```text
task result
  -> agent memory when ephemeral
  -> district knowledge when domain-reusable
  -> city graph only when cross-district or constitutional
```

Promotion from district to city state requires provenance, authority, and review appropriate to the record type.

## Anti-Flattening Invariants

The system MUST NOT:

- merge all district vaults into one undifferentiated text heap
- treat a global index as ownership of district knowledge
- give every agent citywide context by default
- infer authority from retrieval access
- let one district taxonomy become universal without explicit canon
- silently promote provisional district claims into city canon
- lose source, namespace, evidence state, or content hash during roll-up

## Compatibility

This doctrine is implemented by the Root City OS District Intelligence Capsule protocol and should be enforced by HERMES, Agent MCP, Mission Control, WikiVault exports, Obsidian node-vault layout, llm-wiki indexes, and gBRAIN namespace resolution.

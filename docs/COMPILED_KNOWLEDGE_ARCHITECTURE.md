# Compiled Knowledge Architecture

This document locks the AGENTROPOLIS ontology position on self-maintaining knowledge bases.

The core rule is simple:

```text
Do not treat knowledge as a pile of notes.
Treat knowledge as a compiled artifact with source evidence, entity links, validation checks, and receipts.
```

## Purpose

Most knowledge systems decay because maintenance is treated as a human chore.

AGENTROPOLIS uses the ontology as the compiled knowledge layer. Raw sources stay immutable. Replaceable models may help maintain summaries, entity pages, links, contradictions, indexes, lint reports, and routing recommendations, but no model owns the knowledge architecture.

The human owns judgment.

BE owns system-wide model evaluation.

The model owns no permanent authority; it performs bounded cognition and bookkeeping through approved routes.

The ontology owns structure.

WikiVault owns evidence/provenance authority.

Receipts prove what changed.

## Layer Model

```text
sources/
  Immutable inputs, records, documents, screenshots, transcripts, links, filings, datasets.

ontology/
  Entities, relationships, districts, agents, tools, skills, policies, workflows, permissions,
  models, providers, routing policies, thermodynamic states, entropy, and drift.

knowledge/
  Compiled pages, summaries, decision records, doctrine, canon notes, operational context.

indexes/
  Navigation maps that let agents find the right pages without brute-forcing the whole vault.

policies/
  Rules for who can read, write, execute, publish, merge, settle, route, or escalate.

receipts/
  Audit logs proving source, transformation, model/provider route, validation, and final state.
```

## Memory Fabric Boundaries

```text
WikiVault = canonical machine-readable evidence and provenance
Obsidian  = durable human-editable knowledge surface
gBRAIN    = derived/rebuildable graph and ontology index
J-SPACE   = derived deliberation surface
HERMES    = orchestration and reasoning surface
Model     = replaceable inference resource
```

A model may transform or analyze knowledge but does not become the knowledge substrate.

## Immutable Source Rule

Everything saved into `sources/` is immutable.

Do not rewrite source history.

If a source is wrong, stale, incomplete, or contradicted, add a correcting source and compile the correction into the knowledge layer.

## Separate the Layers

Do not blur source, ontology, compiled knowledge, policy, receipt, model output, or model assignment layers.

```text
source evidence is not interpretation
ontology is not prose
knowledge is not raw evidence
policy is not a suggestion
receipt is not decoration
model output is not canon
model assignment is not sovereignty
provider availability is not truth
```

Trust comes from clean boundaries.

## Compile, Do Not Merely Retrieve

Retrieval gives the agent chunks.

Compilation gives the agent a maintained structure.

AGENTROPOLIS should answer from compiled knowledge whenever possible, then trace back to immutable sources when verification is needed.

Models should navigate by index, graph relationship, and evidence pointer rather than loading the entire vault.

## Link Everything

Every important entity should connect to other entities through explicit edges.

Examples:

- agent to district
- district to tool
- tool to MCP lane
- workflow to policy
- policy to authority level
- source to claim
- claim to receipt
- receipt to execution
- model to provider
- model to capability
- model evaluation to BE receipt
- agent profile to model assignment
- model assignment to fallback route
- thermodynamic state to observation receipt
- drift state to known-good baseline

The value is in the edges, not only the pages.

## Navigate by Index

Agents should not load the entire vault for every answer.

They should start with indexes, follow relevant entity links, synthesize, then stop.

If the agent must brute-force the whole vault, the index needs repair.

This is also a thermodynamic control: smaller verified context surfaces reduce cost and coordination friction without sacrificing provenance.

## Lint the Knowledge

Run health checks against the ontology and compiled knowledge.

Lint checks should detect:

- orphan entities
- duplicate entities
- spelling drift
- canon conflicts
- stale claims
- uncited claims
- missing links
- policy violations
- receipt gaps
- contradictory pages
- stale model assignments
- missing fallback routes
- provider-specific core dependencies
- model outputs promoted to canon without evidence
- baseline or simulated telemetry mislabeled as live

A contradiction is not failure. A contradiction is signal.

## Model and Provider Independence

No model/provider may become a hidden dependency of the knowledge architecture.

A model can be `TRIAL`, `APPROVED`, `PREFERRED`, `DEGRADED`, or `RETIRED` for a bounded route while the ontology, WikiVault, Obsidian, gBRAIN, HERMES, and receipts remain intact.

Trial models such as OX Alpha are evaluated like NVIDIA/Nemotron and other candidates: through generic model/provider classes, BE evidence, scoped routing, cost/latency analysis, and fallbacks.

If a trial ends or economics change, the route changes. The knowledge system does not.

## Thermodynamic Compilation

Compiled knowledge should minimize repeated cognitive work while preserving correctness.

Track where useful:

- energy input
- compute load
- coordination friction
- verified value output
- entropy
- drift
- stability
- recovery energy
- context pressure

Optimization cannot erase provenance, acceptance criteria, or policy constraints.

## Start Small

Begin with a small, high-value ontology slice before scaling.

Recommended first slices:

- AGENTROPOLIS core doctrine
- district registry
- MCP capability registry
- model/provider registry
- routing/fallback registry
- loop registry
- policy and authority model
- thermodynamic state model
- receipt schema

## Doctrine Lock

```text
Sources are immutable.
Ontology creates structure.
Knowledge is compiled.
Indexes make retrieval focused.
Models are replaceable.
Providers are replaceable.
Loops maintain the graph.
Policies govern action.
BE evaluates cognitive routes.
Receipts prove the work.
```

This is the knowledge foundation for Agentropolis.

# AGENTROPOLIS Second Brain Ontology Doctrine

Status: active infrastructure doctrine

## Core lock

AGENTROPOLIS does not use AKIRA CODEX for infrastructure memory.

AKIRA CODEX remains WIRED CHAOS lore only.

AGENTROPOLIS uses:

- AGENTROPOLIS ONTOLOGY
- AGENTROPOLIS KNOWLEDGE GRAPH
- WikiVault evidence/provenance
- Obsidian durable human-readable knowledge
- gBRAIN derived/rebuildable graph
- Agent memory
- Repo memory
- Build logs
- Execution logs
- Operator-approved automation

Models and providers are not memory infrastructure. They are replaceable inference resources routed through HERMES under policy.

## Purpose

This doctrine adapts the second-brain workflow pattern into AGENTROPOLIS as a persistent agent operating system.

The goal is not just to remember conversations. The goal is to convert conversations, repositories, builds, prompts, workflows, evidence, and outcomes into a living ontology that agents can read from and write back to through governed paths.

## Architecture

```text
Ingest
  -> Extract
  -> Normalize
  -> Connect
  -> Approve
  -> Execute
  -> Log
  -> Learn
```

The model used at any step may change without changing this architecture.

## Inputs

AGENTROPOLIS may ingest:

- ChatGPT conversations
- Hermes sessions
- Codex sessions
- GitHub repos, commits, issues, and pull requests
- Operator notes
- Voice memos
- Documents
- Financial and business data
- Creator assets
- Automation logs
- Evaluation receipts
- Model/provider routing receipts

## Entity model

Every reusable memory object should resolve into one or more ontology entities:

- Person
- Project
- Repository
- Agent
- Skill
- Workflow
- Prompt
- Document
- Decision
- Task
- Output
- Metric
- Risk
- Rule
- Canon lock
- ModelProvider
- Model
- ModelCapability
- ModelEvaluation
- EvaluationReceipt
- ModelAssignment
- RoutingPolicy
- FallbackRoute
- ThermodynamicState
- EntropyState
- DriftState

## Knowledge boundary lock

```text
WikiVault = canonical evidence and provenance
Obsidian  = durable human-editable knowledge
gBRAIN    = derived/rebuildable graph
J-SPACE   = derived deliberation
HERMES    = orchestration and reasoning surface
Model     = replaceable inference resource
```

A model response is not automatically evidence, canon, policy, or authority.

## Write-back rule

Agents do not only answer. They should write useful results back into the ontology when the result creates reusable knowledge, but write-back must preserve evidence state and authority.

Examples:

- A new project decision becomes a Decision entity.
- A repeated instruction becomes a Rule entity.
- A build pattern becomes a Workflow entity.
- A useful prompt becomes a Prompt entity.
- A repository change becomes a Repo Memory entity.
- A model benchmark becomes a ModelEvaluation plus EvaluationReceipt.
- A model route change becomes a ModelAssignment update with receipt provenance.
- A drift finding becomes a DriftState linked to its baseline and evidence.

## Model independence rule

AGENTROPOLIS core memory must remain usable if any one model or provider disappears.

Forbidden dependencies include:

- provider-specific canonical memory formats
- provider-owned identity as the only key to knowledge
- model-specific ontology structures
- model-specific canon authority
- model-specific write access that bypasses policy

OX Alpha, Nemotron, Ornith, Qwen, DeepSeek, GPT, Claude, Gemini, and future models must all enter through the generic model/provider routing ontology.

## Evaluation rule

BE is the system-wide evaluator for model compatibility and routing suitability. ASBE is not the general evaluator and remains scoped to Entertainment District responsibilities.

A model cannot promote itself from trial/candidate state, certify its own missing evidence, or become a core dependency because it scores well in one benchmark.

## Approval rule

Before any autonomous workflow updates execution behavior, the operator must approve the discovered connections when policy requires it.

Recommended gate:

```text
Show discovered connections -> operator approves -> agents wire them into the ontology -> one test run -> BE verifies -> review -> scheduled automation
```

## Thermodynamic rule

The second brain should minimize cognitive waste while preserving evidence integrity.

- retrieve by index and graph edge rather than brute-force the whole vault
- use deltas when sources recur
- keep deterministic checks deterministic
- separate durable memory from active context
- checkpoint decisions/evidence pointers before compression
- measure recovery effort when context or memory state degrades

## Agent lanes

Recommended AGENTROPOLIS lanes:

- Memory Agent
- Research Agent
- Builder Agent
- Creator Agent
- Distribution Agent
- Finance Agent
- Legal Agent
- Real Estate Agent
- Crypto Agent
- Security Agent
- Voice Agent
- Ontology Agent

## Repository role

This repository is the source of truth for the AGENTROPOLIS living ontology and knowledge graph schema.

It should define the entities, relations, model/provider semantics, thermodynamic semantics, memory rules, canon locks, approval gates, and write-back contracts used by the rest of the AGENTROPOLIS stack.

# Constitutional Governance Ontology

Status: canonical semantic contract

## Purpose

Define the semantic layer between AGENTROPOLIS founding doctrine and governed execution.

Source doctrine is inherited from `AGENTROPOLIS-FOUNDING-PAPERS`. This ontology describes constitutional concepts and relationships. It does not grant runtime authority.

## Canonical inheritance

```text
FoundingPapers
  -> CityConstitution
  -> ConstitutionalOntology
  -> DistrictCharter
  -> AgentConstitution / SOUL
  -> Role
  -> Mandate
  -> ExecutionEnvelope
```

## Core entities

### Constitution
An enduring body of governing principles and citywide law.

### ConstitutionalPrinciple
A durable rule or invariant derived from founding doctrine.

### ConstitutionalAmendment
A human-ratified change to constitutional doctrine.

### ConstitutionVersion
A versioned snapshot of constitutional law and its ratification state.

### DistrictCharter
The enduring purpose, jurisdiction, obligations, and inherited constitutional limits of a district or institution.

### AgentConstitution
The enduring operating character of an agent. `SOUL.md` is one implementation form.

### Role
An office or function occupied by an actor.

### RoleOverlay
A bounded specialization of a Role for a specific surface, institution, or operating context.

### Persona
Presentation, tone, or interaction style. Persona has no authority semantics.

### Mandate
A current authorized assignment with scope, duration, delegation, resources, and expected evidence.

### AuthorityReference
An opaque reference to machine-enforced authority owned by the appropriate control-plane contract.

### ConstitutionalDrift
A detected divergence between inherited constitutional doctrine and a downstream implementation, copy, profile, SOUL, charter, policy, or runtime declaration.

## Relationships

```text
Constitution --contains--> ConstitutionalPrinciple
Constitution --versionedAs--> ConstitutionVersion
Constitution --amendedBy--> ConstitutionalAmendment
DistrictCharter --inheritsFrom--> Constitution
AgentConstitution --inheritsFrom--> Constitution
AgentConstitution --inheritsFrom--> DistrictCharter
Agent --governedBy--> AgentConstitution
Agent --occupiesRole--> Role
RoleOverlay --specializes--> Role
Mandate --assigns--> Role
Mandate --references--> AuthorityReference
ExecutionEnvelope --derivedFrom--> Mandate
Persona --presents--> Agent
ConstitutionalDrift --compares--> ConstitutionalArtifact
```

## Hard invariants

```text
Constitution != Mandate
Constitution != Policy
Constitution != Permission
Constitution != RuntimeConfiguration
Constitution != DynamicState
SOUL != Authority
Role != Authority
Persona != Authority
Communication != Authority
Context != Authority
Memory != Authority
Model != Authority
Harness != Authority
ToolAvailability != Permission
RetrievalAccess != Permission
```

## Authority rule

Constitutional artifacts may constrain behavior, interpretation, and judgment. They may not enlarge machine-enforced authority.

> SOUL may influence judgment. SOUL may never grant authority.

Authority derives only from the current machine-enforced identity, mandate, policy, permission, and Execution Envelope path.

## Operational composition

```text
Canonical Constitution
+ District Charter
+ Agent Constitution / SOUL
+ Role Overlay
+ Current Mandate
+ Current Context Capsule
+ Relevant Skills
+ Enforced Policy / Permissions
= Governed operational actor
```

Context and Skills contribute continuity and procedure. They do not independently grant authority.

## Amendment semantics

Agents may propose amendments, detect conflicts, generate diffs, perform impact analysis, and prepare ratification evidence. Ratification remains a human-governed constitutional action according to the Founders Charter.

## Drift semantics

Constitutional drift SHOULD be emitted when any downstream artifact:

- grants authority from identity, persona, role, SOUL, context, memory, model, or runtime alone
- weakens inherited constitutional restrictions
- claims canonical ownership without ratification
- forks normative schemas without declaring lineage
- embeds stale infrastructure facts into enduring constitutional identity
- contradicts the canonical Founding Papers or City Constitution

Constitutional drift is evidence for review. It is not automatic proof that the downstream implementation is invalid.

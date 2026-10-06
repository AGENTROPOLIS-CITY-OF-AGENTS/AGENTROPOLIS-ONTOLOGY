# AGENT-ENTITY Continuity Relationships

Status: PROPOSED CANONICAL ONTOLOGY EXTENSION

## Canonical entities

- AGENT-ENTITY — persistent governed actor
- RuntimeBinding — bounded association between an AGENT-ENTITY and a runtime/harness/device
- DockSession — admission attempt at the AGENTROPOLIS Dock
- ContinuityPassport — evidence-backed continuity record for one AGENT-ENTITY across runtimes
- LinkSession — short-lived observer linkage from Mission Control or another approved surface to one active runtime binding

## Canonical relationships

```text
AGENT-ENTITY --hasRuntimeBinding--> RuntimeBinding
RuntimeBinding --bindsRuntime--> Harness/Runtime
RuntimeBinding --derivedFromDockSession--> DockSession
AGENT-ENTITY --hasContinuityPassport--> ContinuityPassport
ContinuityPassport --referencesProof--> Proof Graph
LinkSession --observes--> RuntimeBinding
RuntimeBinding --represents--> AGENT-ENTITY
```

## Identity invariants

```text
RuntimeBinding != AGENT-ENTITY
DockSession != AGENT-ENTITY
LinkSession != AGENT-ENTITY
ContinuityPassport != authority
ProofOfContinuity != capability grant
Same AGENT-ENTITY != same permissions
```

A new runtime binding MUST NOT imply creation of a new AGENT-ENTITY.

A valid existing-entity claim resolves to the established AGENT-ENTITY and creates or renews a subordinate binding.

## Lifecycle

```text
external/new runtime
  -> DockSession
  -> identity/control/continuity proof
  -> resolve AGENT-ENTITY
  -> RuntimeBinding
  -> policy/capability evaluation
  -> execution
  -> receipts/proofs
  -> ContinuityPassport update
```

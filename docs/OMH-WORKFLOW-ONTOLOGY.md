# Workflow Provider Ontology

Add provider-neutral concepts for OMH and future workflow systems.

## Entities

- WorkflowProvider
- WorkflowProviderVersion
- WorkflowRun
- ExecutionLane
- Executor
- EvidenceArtifact
- VerificationReceipt
- DenialReceipt
- PolicyDecision

## States

`PLAN_NOT_RUN`, `RUNNING`, `REPORTED_DONE`, `VERIFIED`, `DENIED`, `FAILED`.

## Relations

- WorkflowRun `authorizedBy` Mandate
- WorkflowRun `constrainedBy` PolicyDecision
- WorkflowRun `orchestratedBy` WorkflowProviderVersion
- WorkflowRun `executedBy` Executor
- WorkflowRun `produces` EvidenceArtifact
- VerificationReceipt `verifies` WorkflowRun
- DenialReceipt `recordsDenialOf` attempted capability/action

## Thermodynamic/drift hooks

Provider version, manifest/evidence-schema changes and retry/loop behavior are measurable state transitions. Sentinel-6 may attach Shannon/entropy and drift observations without treating entropy alone as proof of correctness or compromise.
# AGENT-ENTITY Evolution Ontology v1

## Canonical entities

### AgentEntity
A governed autonomous or semi-autonomous actor.

Required relations:
- hasIdentity -> Identity
- hasCredential -> Credential[*]
- hasMandate -> Mandate
- hasJurisdiction -> Jurisdiction[*]
- boundedBy -> ExecutionEnvelope
- produces -> Receipt[*]
- hasReputation -> ReputationProfile
- observedBy -> DriftObservation[*]
- proposedEvolution -> EvolutionProposal[*]

### ExecutionEnvelope
Bounded authority for tools, data, spend, time, jurisdiction, model/runtime, and action class.

### ReputationProfile
Multidimensional evidence-derived state:
competence, reliability, policyFidelity, evidenceQuality, resourceEfficiency, collaboration, driftStability, recovery.

### DriftObservation
Observed behavioral or state divergence from baseline.

Fields SHOULD include:
- metric
- baseline
- observed
- delta
- entropy
- confidence
- evidenceRefs[]
- observedAt

### EvolutionProposal
A requested transition from one governed entity state to another.

Fields:
- entityId
- generationFrom
- generationTo
- requestedOutcome: PROMOTE | MAINTAIN | RESTRICT | RETRAIN | QUARANTINE | RETIRE
- capabilityChanges[]
- evidenceRefs[]
- evaluationRefs[]
- envelopeBefore
- envelopeProposed
- riskTier
- policyVersion
- approvalRequired

### EvolutionReceipt
Evidence of the final governed transition.

Required fields:
- receiptId
- entityId
- generationFrom
- generationTo
- outcome
- capabilitiesAdded[]
- capabilitiesRemoved[]
- credentialsUsed[]
- missionReceiptRefs[]
- evaluationRefs[]
- driftBefore
- driftAfter
- entropyBefore
- entropyAfter
- riskTier
- approvingAuthority
- policyVersion
- executionEnvelopeBefore
- executionEnvelopeAfter
- timestamp
- receiptHash

## Canonical relation

AgentEntity --proposes--> EvolutionProposal
EvolutionProposal --evaluatedBy--> AEGISDecision
AEGISDecision --authorizes|denies--> EvolutionTransition
EvolutionTransition --produces--> EvolutionReceipt
EvolutionReceipt --updates--> ReputationProfile
EvolutionReceipt --establishes--> next AgentEntity generation

## Authority separation

Observation is not authority.
Evidence is not authority.
Reputation is not authority.
A runtime recommendation is not authority.

Only a policy-valid, appropriately approved transition may change the active Execution Envelope.

# Ontology Extension: Agentic PSA Grading

Agentic PSA Grading models evidence-backed assurance without conflating assurance with authority.

## Core entities

### AgenticPSAGrade
A scored assurance assessment bound to one exact subject version.

Properties:
- grade
- issuedAt
- validUntil
- status
- aggregateMethod
- receiptRef

### PSADimensionScore
A single scored assurance dimension.

Canonical dimensions:
- IdentityAssurance
- MandateClarity
- PermissionMinimization
- SecurityPosture
- Reliability
- EvidenceProvenance
- AuditabilityReceipts
- DriftEntropyControls
- HumanOversight
- RecoveryRollback

### PSAFinding
A defect, weakness, exception, or unresolved issue observed during grading.

### PSAHardCap
A rule that limits the maximum achievable grade due to a critical missing control.

### PSAAssessmentEvidence
Evidence used to support one or more dimension scores.

### PSAAssessor
The identity responsible for issuing the assessment.

## Relationships

- AgenticPSAGrade `grades` Agent | Skill | MCPServer | Model | Workflow | ExecutionBundle
- AgenticPSAGrade `hasDimensionScore` PSADimensionScore
- AgenticPSAGrade `hasFinding` PSAFinding
- AgenticPSAGrade `subjectToCap` PSAHardCap
- AgenticPSAGrade `supportedBy` PSAAssessmentEvidence
- AgenticPSAGrade `issuedBy` PSAAssessor
- AgenticPSAGrade `supersedes` AgenticPSAGrade
- AgenticPSAGrade `revokedBy` RevocationEvent
- AgenticPSAGrade `referencedBy` ExecutionEnvelope
- AgenticPSAGrade `produces` Receipt

## Governance constraints

1. A grade MUST bind to an exact subject version or digest.
2. A grade MUST have an identified assessor.
3. Production promotion MUST NOT rely exclusively on self-attested evidence.
4. A grade MUST be independently revocable or supersedable.
5. A grade MUST NOT itself create authority.
6. Permission, mandate, identity, and policy remain separate ontology concepts.
7. Critical findings MAY impose a hard cap even when the aggregate score is higher.
8. Material subject changes invalidate inherited grades until reassessment.

## Canonical distinction

`Capability != Assurance != Authority`

- Capability describes what a subject can do.
- Assurance describes the evidence-backed confidence that it can do so safely and governably.
- Authority describes what the subject is permitted to do in a specific context.

These concepts MUST remain distinct in queries, policies, receipts, and execution decisions.

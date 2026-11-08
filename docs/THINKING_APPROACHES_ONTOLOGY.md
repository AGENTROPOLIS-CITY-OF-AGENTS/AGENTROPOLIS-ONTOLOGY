# Contextual Thinking Approaches Ontology

Status: version 1.0.0 vocabulary and record contract. Runtime adoption requires explicit integration and verification.

## Placement and purpose

Cognition → Thinking approaches. This is an operational vocabulary for task planning, accessible interfaces, task routing, and complementary review. It is not a validated psychological assessment, intelligence test, gender model, or diagnosis.

The motivating advertisement supplies no verified scoring method. Its colors, numeric scores, gender claims, and “cognitive utilization” terminology are not adopted as evidence. The vocabulary below is a design decision authorized in the project conversation on 2026-10-26.

## Approach vocabulary

| ID | Meaning | Example |
|---|---|---|
| holistic | Examine the whole and its relationships | Map district dependencies and downstream effects |
| analytical | Examine evidence, causes, and alternatives | Compare explanations for a failed execution |
| detail-oriented | Inspect individual elements and discrepancies | Check permissions, configuration, and receipts |
| sequential | Organize dependencies and ordered steps | Build an execution plan with prerequisites |
| focused | Direct attention toward a bounded target | Complete one scoped investigation |

Approaches may overlap and change within a task. Focus is an attention dimension; sequence is an ordering dimension; neither implies intelligence or competence.

## Classes and relationships

| Relationship | Domain | Range |
|---|---|---|
| performedBy | ThinkingApproachRecord | Actor |
| scopedTo | ThinkingApproachRecord | Task |
| usesApproach | ThinkingApproachRecord | ThinkingApproach |
| supportedBy | ThinkingApproachRecord | EvidenceArtifact |
| requestsSupport | ThinkingApproachRecord | SupportPreference |
| hasOutcome | ThinkingApproachRecord | TaskOutcome |
| informs | ThinkingApproachRecord | RoutingDecision or CognitiveAssessment |

A record contains actor, task, context, record kind, one or more approaches, provenance, time, outcome, and support preferences. Preference, observed behavior, assessed ability, and planned approach are separate record kinds. A plan is not evidence of execution. An observed use is not a permanent trait.

The contract is [contextual-thinking-approach-v1.schema.json](../schemas/contextual-thinking-approach-v1.schema.json). The vocabulary is [thinking-approaches.yaml](../ontology/thinking-approaches.yaml).

## Evidence and governance

- Preference requires an attributable self-report. Do not infer personal preferences from identity, diagnosis, gender, or one interaction.
- Observed behavior requires an attributable artifact and observation context.
- Assessed ability requires an identified assessment method and scope. A structurally valid record does not validate that method.
- Planned approach requires a plan reference and remains declared until execution evidence exists.
- Evaluated outcomes require evidence references. Missing evidence remains unknown, not zero.
- Numeric intelligence, brain-utilization percentages, and invented radar scores are outside this contract.
- Human preference records stay in an appropriately access-controlled namespace. Public examples must be synthetic. Allow correction, withdrawal, and deletion under governing retention policy.
- No approach label grants tools, authority, access, or exemption from review.
- Approach declarations do not replace independent quality evaluation.

## Routing and review

1. Determine the task's required approaches from its dependencies and acceptance criteria.
2. Check mandate, policy, permission, capability evidence, privacy, and cost before selecting an eligible executor.
3. Use volunteered preferences to adapt presentation and support. Offer diagrams, checklists, examples, short steps, or fewer interruptions without inferring limitations.
4. Use demonstrated task-relevant performance as capability evidence. Do not substitute a thinking label for it.
5. Request complementary review where useful: holistic coverage plus detail inspection, or analytical comparison plus sequential execution checks.
6. Record actual outcome evidence and permit revision. No automatic reduction in human review is justified by an approach declaration.

## Existing ontology connections

[Cognitive governance](COGNITIVE_GOVERNANCE_ONTOLOGY.md) continues to describe reasoning coverage and authority boundaries. Thinking approaches describe how work is approached; no equivalence to its NI/NE/TI/TE/FI/FE/SI/SE labels is asserted.

Dispatch may consume these records as advisory context. BE evaluates task outcomes; AEGIS enforces policy boundaries; 54-T verifies effective capability and containment. WikiVault retains provenance; Obsidian can hold editable preferences; gBRAIN indexes authorized records; J-SPACE supports deliberation; HERMES consumes approved task context. These are integration contracts, not claims of installed adapters.

## Synthetic example

```json
{
  "id": "thinking:example-001",
  "actor_ref": "agent:example-reviewer",
  "actor_kind": "agent",
  "task_ref": "task:example-permission-review",
  "context": "Inspect a staging permission configuration",
  "record_kind": "planned_approach",
  "approaches": ["analytical", "detail-oriented"],
  "evidence": {
    "basis": "declared_plan",
    "source_refs": ["plan:example-review-001"]
  },
  "recorded_at": "2026-10-26T20:00:00Z",
  "outcome": {"status": "not_evaluated", "evidence_refs": []},
  "support_preferences": []
}
```

## Acceptance checks

All five IDs resolve in the vocabulary and schema. Unsupported approach values and mismatched evidence bases are rejected. Assessed ability requires method and scope. Evaluated outcomes require evidence. Synthetic examples must not assert an assessment of a real person.

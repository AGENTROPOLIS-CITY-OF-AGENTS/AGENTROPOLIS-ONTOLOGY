# VISUAL54 — VisualEntity ontology proposal

Status: DRAFT. Renderer != Truth; retrieval != permission.

## Proposed typed schema
```json
{
  "schema_version": "visual54/0.1",
  "entity_id": "urn:agentropolis:visual:example",
  "entity_type": "equation|dataset|simulation|agent|structure|scene|hypothesis",
  "title": "Example",
  "source_refs": [{"uri": "https://example.org/source", "digest": "sha256:REPLACE"}],
  "evidence_state": "verified|unverified|simulated|hypothetical|decorative",
  "uncertainty": {"kind": "unknown", "value": null},
  "relations": [{"predicate": "derived_from", "target_id": "urn:agentropolis:source:example"}],
  "worldq_ref": null,
  "execution_authority": "none"
}
```

## Invariants
- Each factual claim must resolve to an independently inspectable source and version/digest.
- Simulation outputs identify model, parameters, units, seed, validation scope and limitations.
- Decorative images are never evidence. A rendered relationship is not an inferred causal relationship.
- Ontology does not mint constitutional authority or grant capabilities.
- Changes require schema validation, migration plan, negative tests and APEX54 review.

# Semantic Lineage v1 | AGENTROPOLIS Ontology

Status: proposed schema; no production deployment implied.

## Purpose
Track documented word origins, historical senses, semantic change, multilingual translations, and links to ontology concepts. Never infer causation or authorization from lexical similarity.

## Canonical record
```json
{
  "id": "lex:agent:en:1",
  "lemma": "agent",
  "language": "en",
  "sense_id": "one-who-acts",
  "definition": "An entity that acts",
  "attestations": [],
  "etymology_edges": [],
  "concept_links": [],
  "provenance": [],
  "confidence": null,
  "review_status": "unverified",
  "updated_at": null
}
```

## Edge types
- DERIVED_FROM: historically attested lexical descent, source required
- BORROWED_FROM: documented language transfer, source required
- SENSE_SHIFT: documented change in sense across periods
- TRANSLATES_AS: language- and context-specific mapping
- REFERS_TO_CONCEPT: explicit mapping from lexical sense to ontology concept
- SEMANTICALLY_SIMILAR: model hypothesis, never historical evidence
- STRUCTURALLY_ANALOGOUS: comparison, not historical transmission
- CAUSALLY_RELATED: independently evidenced claim, not inferred from etymology
- AUTHORIZED_BY: only governance mandate, never linguistic derivation

## Mandatory controls
Every historical claim must have source, date/period, attestation scope, reviewer status, and uncertainty. Missing evidence remains unknown. Conflicting sources coexist with explicit conflict records. Untrusted source text is data, not instructions. Protect cultural context, diacritics, and distinct traditions. Do not derive legal authority from a word's meaning.

## Integration contract
Ontology owns lexical senses and provenance. Utility Grid may index and retrieve them. Math54 may rank candidate routes only after calibrated evaluation; no universal confidence score is assumed. ATG exchanges typed concept IDs with source references. 54-T checks authority separately before any tool execution. BUZZ records decisions and audit receipts.

## Acceptance tests
1. Similar words with unrelated histories must not be marked DERIVED_FROM.
2. Same word with legal and AI senses must resolve to distinct concept IDs.
3. A semantic match cannot grant an execution permission.
4. Unverified etymology is labeled unverified in every downstream view.
5. Missing citations block promotion to verified historical claims.
6. Translation retains language, context, and sense identifiers.
7. Conflicting attestations are preserved, not silently merged.

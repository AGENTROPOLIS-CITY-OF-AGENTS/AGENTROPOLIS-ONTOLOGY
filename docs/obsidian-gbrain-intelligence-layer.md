<!--
Reference copy. Canonical edition (PROPOSED, NEURO decision 2026-10):
  AGENTROPOLIS-CITY-OF-AGENTS/PUBLIC-PORT-DISTRIBUTION-MEMBRANE:docs/obsidian-gbrain-intelligence-layer.md
Provenance: this file previously held a tailored full copy (blob f866146b, commit 77e85842, 2026-07-05 PT; never edited
since). Core sections that conflicted with current ontology law ("Obsidian ... Source-of-truth", "Obsidian is the writable
brain") are replaced by the reference below; ONTOLOGY-specific content is preserved verbatim in the overlay, with the
claim shape extended for provenance. Prior text is recoverable from git history (no history rewrite).
Prepared by Grok Bot (bounded implementation). Not independently verified by VERITY.
-->

# Obsidian + gBRAIN Intelligence Layer (AGENTROPOLIS-ONTOLOGY reference)

The canonical edition of this document lives in
`AGENTROPOLIS-CITY-OF-AGENTS/PUBLIC-PORT-DISTRIBUTION-MEMBRANE` at `docs/obsidian-gbrain-intelligence-layer.md`.
AGENTROPOLIS-ONTOLOGY keeps this reference plus the ontology overlay below. Overlays may add detail; they may not
contradict the canonical Layer Roles or the Governed Write Contract.

Summary of the canonical semantics:

| Layer | Role |
| --- | --- |
| WikiVault | Owns governed evidence and canon (promotion-gated). |
| Obsidian | Human-readable / human-editable knowledge; not canon until promoted. |
| gBRAIN | Derived, rebuildable claims graph; written only by the projection job. |
| J-Space | Contextual reasoning; derived and read-only. |

There is no direct gBRAIN write surface. Claims are staged, reviewed by a non-producing reviewer, promoted to
WikiVault/Obsidian, and then projected into gBRAIN.

## AGENTROPOLIS-ONTOLOGY overlay

### Claim Ontology holders (ontology additions)

In addition to the canonical holders, the ontology recognizes:

- `characters/<slug>`
- `districts/<slug>`

Every claim must preserve attribution and provenance.

### Minimum Claim Shape

```json
{
  "id": "claim_<slug>",
  "kind": "fact | take | doctrine | decision | bet | hunch | relationship | evidence",
  "holder": "people/<slug> | companies/<slug> | projects/<slug> | agents/<slug> | brain | world | self",
  "subject": "entity/<slug>",
  "claim": "Plain-language claim text.",
  "source": "wikivault://<id> | obsidian://note/path | https://source.url",
  "source_hash": "sha256:<hex>",
  "projected_from": "<source id>@<hash> (set by the projection job, not by agents)",
  "confidence": 0.0,
  "status": "active | superseded | disputed | resolved",
  "created_at": "YYYY-MM-DD",
  "updated_at": "YYYY-MM-DD"
}
```

### Bet Extension

Bets must include a resolution path.

```json
{
  "resolution_criteria": "What must happen for this bet to resolve true or false.",
  "resolution_status": "open | true | false | ambiguous",
  "resolved_at": null
}
```


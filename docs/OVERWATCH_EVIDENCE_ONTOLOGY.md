# Overwatch Evidence Ontology

## Purpose

Normalize public-source observations from Omarchy Overwatch into AGENTROPOLIS without allowing a dashboard, feed, model, or visualization to become authority.

## Core entities

### EvidenceEnvelope
A transport-neutral observation record.

### Source
The public feed, provider, registry, API, or operator-imported source.

### Observation
What the source actually supplied.

### Provenance
Where, when, and how the observation was retrieved.

### DerivedAssertion
A model-, rule-, or human-derived interpretation of one or more observations.

### Verification
A VERITY or other governed validation result.

## Relationship law

```text
Source
  -> emitted
Observation
  -> wrapped_as
EvidenceEnvelope
  -> may_support
DerivedAssertion
  -> may_receive
Verification
```

An Observation is not a Mandate.
A DerivedAssertion is not SourceFact.
A Verification is not ExecutionAuthority.
A visualization is not truth.

## State semantics

The adapter preserves source-health state exactly:

- LIVE
- STALE
- ERR
- OFF

UNKNOWN remains valid when the source does not support a field.

## Model-generated brief

Overwatch BRIEF output is a `DerivedAssertion` with model provenance.

It MUST NOT be stored as an original source observation.

## Geography

When supplied, spatial evidence may carry:

- latitude/longitude
- H3 cell
- GeoJSON geometry
- named AOI reference

Spatial overlap or proximity is a relationship candidate, not causal proof.

## Authority invariant

Every Overwatch-derived EvidenceEnvelope begins with:

```json
{
  "authority": {
    "class": "OBSERVATION",
    "executable": false
  }
}
```

Only downstream mandate, policy, execution-envelope, and assurance systems can authorize consequential action.

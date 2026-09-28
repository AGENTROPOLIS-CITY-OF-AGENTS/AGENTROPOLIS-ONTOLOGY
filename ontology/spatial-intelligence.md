# Spatial Intelligence Ontology

## Core entities

- `SpatialEntity` — a non-person asset, event, place, system, infrastructure element, or jurisdiction with spatial state.
- `SpatialObservation` — one source-backed observation of a SpatialEntity at a time and location.
- `SpatialProvenance` — source, timestamp, state, confidence, attribution, and license context for an observation.
- `Jurisdiction` — a governed geographic scope that may affect policy compilation.
- `SceneCapsule` — a serialized WORLD GRID view state. A SceneCapsule is presentation/context state, not evidence by itself.

## Canonical relationships

`SpatialEntity <- OBSERVES - SpatialObservation`

`SpatialObservation - SOURCED_FROM -> SpatialProvenance`

`SpatialObservation - LOCATED_IN -> Jurisdiction`

`SpatialObservation - MAY_INFORM -> Thesis | Plan | Brief | Scene`

`SpatialObservation - DOES_NOT_AUTHORIZE -> Execution`

## Authority separation

A spatial observation can increase or decrease confidence in a thesis, update a scene, trigger a request for additional evidence, or cause ATG to recompile a plan. It cannot itself create tool permission, capital authority, identity authority, or execution authority.

Any consequential action must continue through:

`Identity -> Mandate -> Plan -> ATG compile -> Execution Envelope -> AEGIS gate -> Execute -> Receipt -> Audit`

## Quantization

WORLD GRID may render the same entity differently at Q0 through Q5. Quantization changes presentation density and context, not ontology identity or provenance.

## Person boundary

This ontology does not define named-person search, biometric identity, face recognition, or individual-person tracking entities for the Spatial Intelligence Plane.

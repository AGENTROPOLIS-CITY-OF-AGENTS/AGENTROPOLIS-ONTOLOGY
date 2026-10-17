# Universal Interoperability Ontology — Proposal

Status: PROPOSED; semantic definitions only, never execution authority.

## Reuse existing canon
Extend MODEL_PROVIDER_ONTOLOGY.md and HARNESS_RUNTIME_ONTOLOGY.md rather than redefining Model, Provider, or Runtime. Preserve BE evaluation authority and the existing constitutional inheritance chain.

## Additional classes
AgentIdentity, AgentEndpoint, CapabilityManifest, CapabilityClaim, VerifiedCapability, ProtocolAdapter, ProtocolBinding, TransportEndpoint, InteroperabilitySession, TaskEnvelope, ContextProjection, TrustBoundary, PermissionGrant, RevocationEvent, ConformanceEvaluation, ConformanceReceipt, ArtifactProvenance.

## Relations
- AgentIdentity --exposes--> AgentEndpoint
- AgentEndpoint --speaks--> ProtocolBinding
- ProtocolBinding --implementedBy--> ProtocolAdapter
- CapabilityManifest --claims--> CapabilityClaim
- ConformanceEvaluation --verifies--> VerifiedCapability
- TaskEnvelope --authorizedBy--> Mandate
- ContextProjection --scopedBy--> TrustBoundary
- InteroperabilitySession --uses--> ProtocolAdapter
- InteroperabilitySession --produces--> ArtifactProvenance
- PermissionGrant --revokedBy--> RevocationEvent

## Semantic invariants
Provider != Model != Runtime != AgentIdentity != ProtocolAdapter != Tool. Claim != VerifiedCapability. EndpointReachability != Authorization. Authentication != Mandate. Transport != Trust. Ontology != Enforcement. ModelOutput != Evidence.

## Interchange envelope (illustrative, not ratified schema)
Required: schema_version, task_id, principal_ref, mandate_ref, capability_ref, target_runtime_ref, protocol_binding_ref, policy_decision_ref, context_projection_ref, budget_ref, expected_evidence, receipt_ref, cancellation_ref, expiry. Secrets MUST be referenced, never embedded. Unknown authority fields fail closed.

## Validation
BE evaluates conformance; AEGIS policy gates enforce authorization; Dock owns external harness admission. Require schema checks, negative tests, migration/version tests, revocation, and receipts. Never claim implementation from documentation alone.

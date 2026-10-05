# AGENTROPOLIS Protocol Standards Charter

## Purpose

The AGENTROPOLIS Protocol Standards program turns proven system protocols into public, implementation-neutral specifications that can be implemented outside AGENTROPOLIS.

## Core distinction

A protocol describes how AGENTROPOLIS currently performs an operation.

A standard defines interoperable behavior independent of any single repository, vendor, chain, runtime, model or deployment.

## Non-negotiable rules

1. **Implementation before assertion.** A standard must be grounded in real protocol behavior or a working reference implementation.
2. **No standards theater.** Internal architecture diagrams, product names and marketing claims are not standards.
3. **Authority separation.** Identity, authentication, authorization, mandate, execution and evidence must remain distinguishable when the domain requires it.
4. **Evidence over claims.** Conformance must be testable.
5. **Chain neutrality by default.** Blockchain-specific requirements must be isolated to blockchain profiles or external ERC/EIP candidates.
6. **No silent privilege expansion.** Adapters, agents, models and providers may not infer authority beyond explicit grants.
7. **Portable semantics.** A standard should state what an independent implementer must do, not how AGENTROPOLIS happens to store it.
8. **Backward compatibility is explicit.** Breaking changes require a new version and migration notes.
9. **Security and privacy are normative concerns.** They are not optional appendices.
10. **Independent implementation is the graduation test.** APS Final requires evidence that another implementation can conform without depending on private AGENTROPOLIS internals.

## Required APS sections

Every APS draft SHOULD contain:

- Title
- Status
- Authors / Editors
- Abstract
- Motivation
- Terminology
- Specification
- Data Model
- Interfaces
- State Machine, when applicable
- Normative Requirements
- Security Considerations
- Privacy Considerations
- Failure Modes
- Threat Model
- Reference Implementation
- Test Vectors
- Conformance Requirements
- Backward Compatibility
- Examples
- Rationale
- Versioning
- Governance
- External Standards Mapping

## Normative language

APS specifications SHOULD use RFC-style normative terms:

- MUST
- MUST NOT
- REQUIRED
- SHOULD
- SHOULD NOT
- MAY

## Candidate review questions

A public repository is reviewed with these questions:

1. What reusable primitive exists here?
2. Can the primitive be described without the product UI or repository-specific implementation?
3. Does another subsystem implement the same primitive differently?
4. Which implementation owns the strongest existing source of truth?
5. Are there existing schemas, contracts, receipts or test vectors?
6. Does the primitive overlap an existing external standard?
7. Should it become a core APS, a domain profile, a reference implementation, or remain product-specific?
8. Can conformance be independently verified?

## External submission rule

No proposal is described as an ERC, EIP, W3C Recommendation, IETF RFC or other external standard until the relevant external process has actually assigned or accepted that status.

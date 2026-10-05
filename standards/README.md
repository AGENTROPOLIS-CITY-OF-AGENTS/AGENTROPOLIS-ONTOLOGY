# AGENTROPOLIS Protocol Standards (APS) Bootstrap

> Staging home for the AGENTROPOLIS standards program until the dedicated public `AGENTROPOLIS-STANDARDS` repository is created.

## Canonical rule

**PUBLIC REPOSITORY != STANDARD**

**PUBLIC REPOSITORY = STANDARDIZATION CANDIDATE**

Every active public repository in the installed AGENTROPOLIS-CITY-OF-AGENTS and wiredchaos spaces is entered into the candidate registry and reviewed for reusable, implementation-neutral interoperability rules.

A candidate only graduates when the reusable primitive is isolated and specified.

## Standards lifecycle

```text
Research
  -> Protocol
  -> APS Candidate
  -> APS Draft
  -> Reference Implementation
  -> Conformance + Test Vectors
  -> Independent Implementation
  -> APS Final
  -> External Standards Submission
```

Possible external destinations include ERC/EIP, W3C, IETF, OpenID and other domain-appropriate standards bodies. Not every APS is blockchain-specific and not every APS should become an ERC.

## Maturity levels

- **C0 DISCOVERY** - public repository is in scope; reusable primitive not yet isolated.
- **C1 CANDIDATE** - reusable protocol behavior identified.
- **C2 DRAFTABLE** - data model and normative behavior are sufficiently clear to draft.
- **C3 STANDARDS READY** - specification, implementation, security and conformance material substantially exist.
- **C4 EXTERNAL CANDIDATE** - stable enough for external standards submission.

## Bootstrap inventory

This bootstrap captures **42 active public repositories** from the currently installed GitHub spaces:

- 35 from `AGENTROPOLIS-CITY-OF-AGENTS`
- 7 from `wiredchaos`

See `registry/candidates.yaml`.

## Initial extraction priorities

1. Governed agent payments and economic authority
2. Agent identity, DID, delegation and mandate
3. MCP capability and tool authorization
4. ATG semantic interoperability
5. Agentropolis ontology and evidence semantics
6. GTM / UGC distribution, attribution and campaign receipts
7. Hermes runtime spawn / handoff / coordination
8. Intellectual-property rights, licensing and provenance
9. Evidence-derived reputation
10. Runtime telemetry and assurance

## Migration

When `AGENTROPOLIS-STANDARDS` is created, this directory should be migrated without renumbering finalized APS documents. Candidate IDs are provisional and are not APS numbers.

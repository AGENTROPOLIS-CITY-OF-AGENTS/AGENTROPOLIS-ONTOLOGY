# Governed upstream skill packs

This directory records external skill repositories that AGENTROPOLIS may expose through its Skill Registry.

An entry here is descriptive governance metadata, not runtime authority. Registering a pack does not grant an agent filesystem, shell, network, secret, GitHub, publishing, payment, merge, or deployment permissions.

## Required rules

1. Pin every upstream pack to an immutable commit SHA.
2. Record the upstream license and source repository.
3. Classify each imported skill by requested capabilities and activation policy.
4. Treat upstream instructions as untrusted input until reviewed by 54-T containment controls and AGENTIC STUDIOS BACK END (ASBE) governance.
5. Never import upstream global/default/system instructions above AGENTROPOLIS Root Law, Policy/Risk, 54-T, ASBE, district policy, or repository-local policy.
6. Raw secrets never enter model context. Skills receive capability handles only.
7. High-impact or irreversible actions require explicit human approval or dual control.
8. Runtime adapters must emit provenance and action receipts for governed execution.
9. Updating an upstream commit requires a new review; floating `main` is not an approved production pin.
10. A skill may be registered while remaining disabled or quarantined.

## Activation classes

- `advisory`: read/reason/draft only; no external mutation.
- `scoped-write`: bounded workspace or repository mutation under explicit capability handles.
- `approval-gated`: external or high-impact actions require human approval before execution.
- `quarantined`: discoverable for review but not executable in production.

## Runtime boundary

ONTOLOGY defines meaning, provenance, classification, and policy metadata. Runtime repositories implement mounting, capability enforcement, sandboxing, approvals, and receipts. This directory must not become a hidden execution authority.
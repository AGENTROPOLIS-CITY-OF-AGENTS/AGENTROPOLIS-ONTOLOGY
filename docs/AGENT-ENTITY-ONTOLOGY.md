# AGENT-ENTITY Ontology

Status: CANONICAL ENTITY MODEL DIRECTION

**AGENT-ENTITY** is the persistent entity abstraction for AGENTROPOLIS.

It is not a runtime, model, wallet, device, avatar, card, chain address, application session, or harness process.

## Core principle

```text
Runtime != AGENT-ENTITY
Model != AGENT-ENTITY
Wallet != AGENT-ENTITY
Device != AGENT-ENTITY
Representation != AGENT-ENTITY
Harness Session != AGENT-ENTITY
```

An AGENT-ENTITY persists across changes in runtime, device, model, representation, network, settlement rail, and execution environment.

## Canonical domains

An AGENT-ENTITY may carry references to:

- stable identity;
- lineage and provenance;
- controller / owner;
- mandates and roles;
- rights and permissions;
- relationships and collectives;
- capabilities and skill assertions;
- reputation and verified history;
- assets and representations;
- economic permissions and limits;
- receipts and state-transition history;
- continuity pointers;
- world-state bindings.

Claims do not become truth merely because an entity self-reports them. Verified state requires the applicable evidence and governance path.

## Representations

A single AGENT-ENTITY may appear as multiple representations:

- software agent;
- TCG card;
- game character / NPC;
- 3D avatar;
- BotBae or messaging agent;
- AR / XR resident;
- NFC / physical collectible;
- robot or embodied system;
- service endpoint.

Representations may change without creating a new entity unless the governing ontology explicitly defines a new entity creation event.

## AGENT-ENTITY and ATG

ATG is the Atralith agentic language and semantic expression layer. ATG may reference AGENT-ENTITY identity, mandate, rights, state, and economic constraints, but ATG is not the entity store and does not mint entity truth by itself.

## AGENT-ENTITY and settlement

Arc, Base, XRPL, bank rails, stablecoin rails, and future settlement providers are not identity authorities.

An economic request may result in an AGENT-ENTITY ownership or control transition only after the governing settlement condition is verified and the required receipt is accepted.

Canonical pattern:

```text
AGENT-ENTITY A
  -> ATG economic intent
  -> Execution Envelope
  -> Economic Fabric / PAYRAIL
  -> selected settlement adapter
  -> verified finality
  -> signed receipt
  -> AGENT-ENTITY state transition
```

## TCG and world-state rule

A TCG card is a representation of an AGENT-ENTITY, not the AGENT-ENTITY itself.

Battle outcomes may update progression, reputation, rank, relationship, or game-history state without economic settlement.

Trading, purchase, or transfer may create economic intent and therefore cross into PAYRAIL and the Economic Fabric before authoritative ownership/control state is changed.

## Anti-lock-in invariant

AGENT-ENTITY identity must survive replacement of any current:

- model;
- runtime;
- device;
- operating system;
- wallet implementation;
- chain;
- settlement provider;
- application;
- tool protocol.

The persistent entity record belongs to AGENTROPOLIS governance, not to any replaceable adapter.

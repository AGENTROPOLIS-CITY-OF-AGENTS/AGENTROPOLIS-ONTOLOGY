# Living Game Ontology v0.1

## Purpose

Register the semantics of the project-, franchise-, chain-, device-, platform-, model-, and rules-engine-agnostic Living Game Protocol so every district, runtime, and adapter means the same thing by "Living Game Object", "quest trigger", "live reality session", or "Human Signal Entity".

This ontology names classes and relations. It does **not**:

- define runtime schemas (canonical schemas are owned by [AGENTROPOLIS-GAMING-DISTRICT](https://github.com/AGENTROPOLIS-CITY-OF-AGENTS/AGENTROPOLIS-GAMING-DISTRICT/blob/main/docs/LIVING-GAME-PROTOCOL.md));
- define or mirror an Execution Envelope (the single canonical envelope is owned by AGENTROPOLIS-ATG);
- hold game state, mandates, credentials, or any runtime authority.

Machine-readable: `ontology/living-game-classes.yaml`, `governance/living-game-invariants.yaml`.

## Canonical references

| Concept | Owner | Reference |
|---|---|---|
| Living Game Object v1 | Gaming District | `https://agentropolis.dev/schemas/living-game-object-v1.schema.json` |
| Live Reality Session v1 | Gaming District | `https://agentropolis.dev/schemas/live-reality-session-v1.schema.json` |
| Execution Envelope | ATG | `https://agentropolis.dev/atg/contracts/core/execution-envelope.schema.json` |
| ATG:LIVING-GAME extension | ATG | `https://agentropolis.dev/atg/contracts/profiles/living-game-extension.schema.json` |

## Classes

### LivingGameObject
A physical or digital TCG/tabletop object (card, deck, character, item, miniature, token, terrain, book, location, artifact) with verified identity, gameplay traits, permissions, and explicit interoperability adapters. Registered in the Gaming District registry. May be adapted as a card, RPG character, NPC, quest giver, companion, inventory item, location key, AR summon, tournament credential, or collectible — only through an InteroperabilityAdapter.

### PhysicalAuthenticator
NFC tag, QR code, or managed installation producing *evidence* at one of four assurance tiers: `discovery`, `verified`, `high_assurance`, `managed_installation`. Payloads carry signed public routes or opaque identifiers only. Never transfers value, access, or ownership. Owned by Utility Grid.

### QuestTrigger
A condition (NFC, QR, location, image, object, gesture, audio, card play, game result, social event, broadcast event, agent interaction, wallet proof, AR anchor, VR location) that **proposes** a transition. The authoritative rules engine verifies it. Physical/spatial/gesture/audio/wallet triggers must declare accessibility alternatives. Consequential effects require an Execution Envelope.

### DeviceCapability
Abstract, brand-neutral capability (`photo`, `video_stream`, `microphone`, `display_spatial`, `hand_tracking`, `nfc`, `qr_scan`, ...) offered by a device class (`ar_glasses`, `vr_headset`, `phone`, `tablet`, `browser`, `webcam`, `capture_card`, `mock`, `other`). Connectivity grants nothing.

### LiveRealitySession
AR/VR/phone/browser capture session with modes `private_vision`, `preview`, `party`, `public`, `director`, `evidence`, `replay` and states `draft` → `preview` → `awaiting_approval` → `live` / `paused` / `ended` / `sealed` / `denied`. Privacy defaults: ephemeral frames, hidden location, `faceRecognition: false` (never true), not publicly authorized. Public egress needs authorization, an Execution Envelope, and a BroadcastLease.

### BroadcastDestination
OBS-compatible egress target (`rtmps`, `srt`, `webrtc`, `whip`, `whep`, `hls`, `ndi`, `virtual_camera`, `local_recording`) referencing credentials by secret reference only.

### BroadcastLease
Renewable, time-boxed, metered broadcast permission bound to one Execution Envelope. No "stream forever" authority. Owned by Utility Grid.

### HumanSignalEntity / SignalMagnet
A real-world influencer who docked approved accounts through AGENTROPOLIS Dock with proven ownership and explicit import/publishing scopes. Docking never implies platform-data ownership. Qualified entities may become Signal Magnets; reach never expands authority.

### InteroperabilityAdapter
Explicit, target-game-owned translation with `targetSystem`, `balancePolicy`, `permittedTraits`, `prohibitedEffects`. No implicit interoperability. Output is non-authoritative until the target rules engine accepts it.

### Evidence
Any observation. `grants_authority: false`, always.

### ExecutionEnvelope (external)
Reference only. Owned by ATG. Not defined here.

## Relations

```text
PhysicalAuthenticator --produces--> Evidence --motivates--> Mandate (ATG) --compiles--> ExecutionEnvelope
QuestTrigger --proposes--> Transition --verified_by--> RulesEngine (game)
LivingGameObject --adapted_through--> InteroperabilityAdapter --> target game (authoritative)
LiveRealitySession --uses--> DeviceCapability
LiveRealitySession --routes_to--> BroadcastDestination
LiveRealitySession --leased_under--> BroadcastLease --bound_to--> ExecutionEnvelope
HumanSignalEntity --publishes_under--> ExecutionEnvelope (publish.social / publish.clip)
```

## Ownership boundaries

- **Gaming District:** protocol, canonical schemas, games, campaigns, tournaments, quests, registry.
- **Utility Grid:** NFC registry, device routing, metering, broadcast leases, receipts.
- **ATG:** mandates, risk, approval, the one Execution Envelope.
- **Creator Core:** runtime interfaces, authoring, publishing pipelines.
- **BOTBAE:** least-privilege conversational operations; no camera, credential, treasury, Recognition, or policy authority.
- **NEURO:** observation and advisory only.
- **Ontology:** semantics only.

## Conformance

`tests/test_living_game_ontology.py` checks that the class registry references the canonical schema `$id`s, defines no envelope, keeps every evidence-like class at `grants_authority: false`, and—when `LIVING_GAME_SCHEMA_DIR` points at a Gaming District checkout—that all enumerations match the canonical schemas.

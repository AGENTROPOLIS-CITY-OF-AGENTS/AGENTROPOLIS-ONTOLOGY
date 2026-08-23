# AGENTROPOLIS Spatial Runtime City Ontology

Status: canonical platform contract
Version: 1.0

## Doctrine

The Agentropolis 3D city is not decorative visualization. It is the spatial observability and control surface of the Intelligence Grid.

Runtime systems are tenants. The city is sovereign.

Munder Difflin, HERMES, Codex, Claude Code, Grok, Qwen, local models, DGX nodes, Cloudflare/Claw nodes, and future runtimes may emit events into Agentropolis, but none of them owns city state, authority, district law, memory canon, or world semantics.

```text
Runtime != City
Runtime != Authority
Runtime != Canon
Renderer != Truth
World State != Provider State
```

## Position in the three-layer architecture

### Layer 1 — Infrastructure

The spatial runtime depends on canonical infrastructure services:

- Identity and Mandate
- Agent Runtime
- Dispatch Protocol
- Memory Layer
- Skill Registry
- AEGIS policy/risk controls
- BE evaluation
- Utility Grid telemetry
- Audit Ledger
- Spatial World-State Bus

### Layer 2 — Districts / Institutions

Districts own domain meaning and map governed activity into spatial entities:

- district
- facility/building
- utility corridor
- transit path
- agent presence
- memory endpoint
- tool/MCP endpoint
- evaluation endpoint
- quarantine boundary

### Layer 3 — Applications / Surfaces

The same world state can be consumed by multiple surfaces:

- full 3D City Mode
- District Mode
- Diorama Mode
- Mission Mode
- cinematic scroll-scrub storytelling
- Mission Control dashboards
- mobile/2D fallback surfaces
- accessibility and text telemetry views

No application surface is allowed to become the source of truth for runtime state.

## Canonical data flow

```text
External / Local Runtimes
        |
        v
Runtime Event Adapters
        |
        v
AGENTROPOLIS EVENT BUS
        |
        v
World-State Resolver
        |
        +------------------+------------------+
        |                  |                  |
        v                  v                  v
   3D City/Diorama    Mission Control     Audit Ledger
        |
        v
Camera + Interaction Layer
```

The adapter normalizes provider/runtime-specific events. The World-State Resolver applies Agentropolis identity, mandate, district, policy, evaluation, thermodynamic, and governance semantics before the renderer receives state.

## Runtime adapter contract

A runtime adapter MAY report:

- agent/session spawned
- agent/session stopped
- task assigned
- task state changed
- tool invoked
- MCP invoked
- message sent/received
- memory read/write
- repo/worktree operation
- token/compute usage
- spend/cost usage
- error/retry
- repeated action loop
- no-progress condition
- breaker state
- human approval request
- completion/result

A runtime adapter MUST NOT:

- assign canonical district authority
- expand a mandate
- bypass AEGIS
- write canonical evidence directly into WikiVault
- promote its own memory to canon
- redefine BE evaluation state
- control the renderer directly
- make the city dependent on that runtime's continued availability

## Spatial entity model

Every visible object SHOULD resolve from canonical entity identifiers rather than provider names.

Minimum spatial entities:

- `city`
- `district`
- `facility`
- `agent_presence`
- `mission`
- `utility_link`
- `dispatch_link`
- `memory_link`
- `tool_endpoint`
- `mcp_endpoint`
- `evaluation_gate`
- `audit_endpoint`
- `quarantine_zone`
- `runtime_node`

A provider/runtime may change without changing the stable city entity ID.

## Runtime event -> city behavior

| Runtime / Grid event | Canonical spatial expression |
| --- | --- |
| Agent spawned | assigned facility/presence comes online |
| Task assigned | mission beacon activates |
| Agent working | facility/interior enters active state |
| Tool call | associated utility/tool route pulses |
| MCP call | Docking District route activates |
| Agent-to-agent message | dispatch packet traverses governed path |
| Memory read/write | memory conduit activates |
| WikiVault query | provenance/knowledge conduit activates |
| Git/worktree operation | repo workspace branches/activates |
| Compute/token load rises | thermodynamic load increases |
| Drift detected | controlled instability visualization begins |
| Breaker steering | amber corrective state |
| Constrained | access/utility routes narrow or close |
| Quarantined | visible containment boundary activates |
| Halted | facility/presence powers down |
| Human approval required | escalation route terminates at Mission Control |
| BE evaluation | evaluation gate activates |
| Receipt produced | receipt routes to Audit Ledger |

Visual effects are representations of resolved state, never the source of resolved state.

## Thermodynamic spatial semantics

The 3D city SHALL visualize the existing thermodynamic ontology without inventing a parallel health model.

Recommended state progression:

```text
NORMAL
  -> DRIFT
  -> ENTROPY_RISING
  -> CONSTRAINED
  -> QUARANTINED
  -> HALTED
```

Possible visual channels:

- luminosity = activity/energy
- pulse frequency = event velocity
- traffic density = dispatch/tool usage
- heat/distortion = compute or entropy pressure
- geometry instability = drift
- perimeter state = policy/containment
- route width = available authority/capacity

Visual intensity MUST be bounded and interpretable; cinematic spectacle cannot obscure operational meaning.

## Diorama contract

Diorama Mode is a scoped camera and scene-composition mode over canonical world state.

It MAY isolate:

- one mission
- one district
- one agent team
- one repo/worktree operation
- one incident
- one tool/MCP chain

It MUST NOT fork or fabricate a second simulation state.

A diorama is a lens over the city, not another city.

## Camera modes

### City Mode
Global procedural city view with district-level telemetry and navigation.

### District Mode
Focuses the camera and interaction budget on one institution while preserving links to shared infrastructure.

### Diorama Mode
Creates a cutaway/miniature composition around a selected mission or operational cluster.

### Mission Mode
Follows a governed corridor such as:

```text
Identity -> Mandate -> Plan -> Execute -> BE -> Receipt -> Audit
```

### Cinematic Scroll-Scrub Mode
Uses panoramic/cinematic source media and procedural 3D composition to bind page scroll to camera motion, scene state, depth, district transitions, and narrative reveals.

Scroll-scrub is a presentation controller over the same world-state graph; it is not a separate runtime.

## Munder Difflin integration position

Munder Difflin is classified as an optional governed runtime adapter/reference implementation.

Useful patterns to adapt:

- real PTY/CLI agent sessions
- mailbox / actor-style coordination
- per-agent worktree isolation
- hook-derived event telemetry
- task ledger signals
- cost/token telemetry
- steer -> constrain -> stop circuit breaker

Patterns that do NOT become Agentropolis law:

- a privileged `GOD` agent as sovereign authority
- prompt-defined authority as the primary control surface
- its office-floor visual metaphor
- its memory system as canonical Agentropolis memory

Its orchestrator maps to a scoped Chief of Staff role beneath Mission Control and AEGIS. Authority remains a runtime constraint, never merely a prompt instruction.

## Provider/runtime independence

The city MUST remain operational when:

- Munder Difflin is absent
- HERMES is absent
- OX Alpha trial ends
- a model/provider changes price
- a local node disappears
- a CLI changes event format
- a better runtime replaces the current one

Adapters are replaceable. Canonical world state is not.

## Operational invariant

> The city does not depict agents working. The city depicts governed state transitions produced by agents working.

This distinction is load-bearing.

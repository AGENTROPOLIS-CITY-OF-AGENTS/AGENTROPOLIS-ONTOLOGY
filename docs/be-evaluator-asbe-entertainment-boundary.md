# BE Evaluator and ASBE Entertainment Boundary

## Canonical rule

The following separation is permanent across Agentropolis:

```text
BE = citywide evaluator / verification layer
ASBE = Agentic Studio Build Engine, scoped to the Entertainment District
```

ASBE must never be used as the name or implementation of the generic citywide evaluator, assurance plane, policy plane, or verification layer.

## BE ontology

BE is a Layer 1 infrastructure capability responsible for evaluating evidence produced by governed execution.

BE may perform:

- objective tests
- executable verifier checks
- schema validation
- contract validation
- quality threshold checks
- evidence comparison
- pass / fail decisions
- retry / repair recommendations
- escalation when machine verification is insufficient
- evaluation receipt generation

BE does not:

- grant authority
- replace identity or mandate checks
- replace AEGIS policy
- replace Agent Seatbelts controls
- replace human approval
- replace Mission Control

Canonical execution position:

```text
Identity
→ Mandate
→ Policy / authority checks
→ HERMES or district execution
→ MCP / tool execution
→ BE evaluation
   ├─ FAIL → repair / retry / escalate
   └─ PASS → receipt
→ Audit
```

## ASBE ontology

ASBE means **Agentic Studio Build Engine**.

ASBE is an Entertainment District application and orchestration engine.

Owning institution:

```text
Entertainment District
```

Primary responsibilities:

- studio orchestration
- scene and shot workflows
- production-agent handoffs
- PBX / Production Broadcast Exchange routing
- creator workflow coordination
- media asset routing
- entertainment publication and distribution lane coordination

ASBE may consume BE after production execution. It does not replace BE.

Canonical entertainment flow:

```text
Entertainment mandate
→ ASBE production workflow
→ governed models / tools / MCP
→ BE evaluation
→ human approval when required
→ production receipt
→ entertainment distribution
```

## Cross-repository enforcement rule

Any Agentropolis repository, registry, diagram, schema, Skill, workflow, README, or generated documentation that places ASBE in the generic citywide evaluator or assurance position is architecturally invalid.

The correction rule is:

```text
If role == generic evaluator or verification layer:
    canonical_system = BE

If role == entertainment studio production orchestration:
    canonical_system = ASBE
```

## Model-provider independence

BE and ASBE are architectural systems, not model identities.

Kimi, Ornith, Nemotron, DeepSeek, Qwen, Ox Alpha, NVIDIA-hosted models, local models, or future providers may be routed behind governed execution lanes without redefining BE or ASBE.

The model is replaceable. The system boundary is not.

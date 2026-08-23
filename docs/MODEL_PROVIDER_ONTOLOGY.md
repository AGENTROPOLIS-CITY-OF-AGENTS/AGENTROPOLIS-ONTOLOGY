# Model Provider and Routing Ontology

Status: active infrastructure doctrine

## Core law

AGENTROPOLIS owns the intelligence architecture. Models compete for bounded routing assignments inside it.

A model is a replaceable cognitive resource. A provider is a replaceable source of that resource. Neither a model nor a provider owns AGENTROPOLIS memory, canon, ontology, policy, receipts, identity, or runtime authority.

```text
Model != Memory
Model != Canon
Model != Evidence Authority
Model != Runtime Authority
Model != Ontology
Provider != Infrastructure Sovereignty
```

## Purpose

This ontology prevents model lock-in and provider capture while allowing AGENTROPOLIS to evaluate, route, compare, promote, degrade, and retire models as the AI stack evolves.

It applies equally to commercial, subscription, hosted, local, open-weight, trial, and experimental models. NVIDIA/Nemotron, Ornith, Qwen, DeepSeek, OpenAI, Anthropic, Gemini, and trial models such as OX Alpha are all modeled through the same generic contracts.

## Classes

- `ModelProvider`
- `Model`
- `ModelEndpoint`
- `ModelCapability`
- `ModelEvaluation`
- `EvaluationReceipt`
- `ModelAssignment`
- `AgentProfile`
- `RoutingPolicy`
- `FallbackRoute`
- `CostProfile`
- `AvailabilityState`
- `ThermodynamicProfile`
- `Runtime`
- `PolicyAuthority`
- `EvaluationAuthority`

## Relationships

| Relationship | Domain | Range | Meaning |
| --- | --- | --- | --- |
| `providedBy` | `Model` | `ModelProvider` | Provider currently serving the model. |
| `servedAt` | `Model` | `ModelEndpoint` | Endpoint through which inference is available. |
| `exposesCapability` | `Model` | `ModelCapability` | Verified or declared capability. |
| `evaluatedBy` | `ModelEvaluation` | `EvaluationAuthority` | Authority responsible for evaluation. |
| `evaluatesModel` | `ModelEvaluation` | `Model` | Model under test. |
| `producesReceipt` | `ModelEvaluation` | `EvaluationReceipt` | Evidence artifact produced by evaluation. |
| `eligibleFor` | `Model` | `AgentProfile` | Profile may route to the model after evaluation. |
| `routesTo` | `ModelAssignment` | `Model` | Active model selection. |
| `fallbackTo` | `FallbackRoute` | `Model` | Alternate model if the primary route is unavailable or uneconomic. |
| `constrainedBy` | `ModelAssignment` | `RoutingPolicy` | Policy controlling assignment. |
| `hasCostProfile` | `Model` | `CostProfile` | Price and quota information used by routing. |
| `hasAvailability` | `Model` | `AvailabilityState` | Current service state. |
| `hasThermodynamicProfile` | `Model` | `ThermodynamicProfile` | Observed energy/compute/value/friction characteristics. |
| `operatedBy` | `Runtime` | `ModelAssignment` | Runtime consumes a route; it is not owned by the model. |

## Evaluation authority

`BE` is the system-wide evaluator for model compatibility, capability, routing suitability, and production evidence.

`ASBE` is not the general model-evaluation authority. ASBE remains scoped to Entertainment District responsibilities.

AEGIS governs policy and authority boundaries. 54-T verifies containment and effective capability. HERMES is the operator/reasoning surface that consumes approved routes.

## Model lifecycle

```text
DISCOVERED
  -> CANDIDATE
  -> TRIAL
  -> EVALUATED
      -> APPROVED
      -> REJECTED
  -> PREFERRED
  -> DEGRADED
  -> RETIRED
```

Lifecycle state does not imply permanence.

- `DISCOVERED`: known to the registry but not yet tested.
- `CANDIDATE`: selected for evaluation.
- `TRIAL`: temporarily available for bounded use.
- `EVALUATED`: BE has produced evidence.
- `APPROVED`: eligible for one or more bounded routes.
- `REJECTED`: not eligible for the evaluated route.
- `PREFERRED`: currently favored for a bounded role, not globally sovereign.
- `DEGRADED`: still usable but reduced due to cost, reliability, latency, drift, or availability.
- `RETIRED`: removed from active routing while historical receipts remain valid.

## Assignment law

A `ModelAssignment` is always narrower than the model itself.

Assignments should identify:

- task or profile scope
- primary model
- provider
- required capabilities
- fallback chain
- BE evaluation receipt
- cost ceiling
- latency ceiling when applicable
- authority ceiling
- start time
- optional expiry/review time

No model becomes a system-wide dependency merely because it performs well in one evaluation.

## Fallback law

Every non-local or economically variable production route should have a fallback policy unless the operator explicitly accepts fail-closed unavailability.

Fallbacks must preserve the task's required capability and authority constraints. A fallback may be cheaper, local, or less capable only if the acceptance criteria remain satisfied.

## Trial model law

Trial models are first-class but temporary candidates.

Example:

```yaml
type: Model
id: ox-alpha
provider: nous
provider_model_id: stealth/ox-alpha
lifecycle: TRIAL
required_by_core: false
replaceable: true
fallback_required: true
evaluation_authority: BE
post_trial_cost_status: unresolved
```

This example does not elevate OX Alpha into AGENTROPOLIS infrastructure. If trial access ends or cost becomes unfavorable, routing changes; the city does not.

## Runtime separation

```text
AGENTROPOLIS ontology / memory / policy / receipts
                |
                v
          HERMES runtime
                |
                v
          routing policy
          /      |      \
     Nemotron  OX Alpha  Ornith
          \      |      /
            fallback pool
```

The runtime contract must remain provider-agnostic. Provider-specific request formats belong in adapters.

## Knowledge separation

Model outputs are proposals, transformations, analyses, or actions. They are not automatically evidence or canon.

- WikiVault remains the canonical evidence/provenance substrate.
- Obsidian remains the human-editable durable knowledge surface.
- gBRAIN remains the derived/rebuildable graph and ontology index.
- J-SPACE remains a derived deliberation surface.
- HERMES remains the orchestration and reasoning surface.
- Models remain replaceable inference resources.

## Economic routing

Routing should compare useful verified outcome against total cognitive and operational cost.

Representative objective:

```text
routing value = verified useful work / (inference cost + latency + retries + context cost + coordination friction)
```

A higher benchmark score does not automatically justify a route if a cheaper model satisfies the same acceptance criteria with materially better thermodynamic efficiency.

## Invariants

1. No provider or model is required for AGENTROPOLIS core ontology, memory, governance, or evidence integrity.
2. No model may self-promote its lifecycle state.
3. No model may self-certify a missing BE evaluation receipt.
4. Model assignments are scoped, reviewable, and replaceable.
5. Fallback routes preserve capability and authority constraints.
6. Cost, quota, latency, reliability, entropy, and drift may demote a model even when quality remains high.
7. Historical receipts remain attributable to the exact model/provider route used at execution time.
8. A provider outage changes routing state, not canon state.
9. A model response cannot write directly to canon without the appropriate evidence and review path.
10. OX Alpha, Nemotron, and every future model are instances of this generic ontology, never privileged architecture classes.

# Fleet Execution Ontology

**Relationship:** semantic extension  
**Canonical semantic owner:** AGENTROPOLIS-ONTOLOGY  
**Execution semantics:** ATG:FLEET

This ontology gives AGENTROPOLIS a shared vocabulary for governed multi-agent execution without confusing workers, harnesses, branches, context, or concurrency with authority.

## Entities

### FleetRun
A bounded coordinated execution episode compiled from one governed task contract.

### ExecutionCell
A unit of work with an explicit owner, baseline, scope, route, budget, state, and verification requirement.

### OwnershipLease
A temporary exclusive write claim over a mutable scope. It prevents simultaneous uncoordinated mutation. It does not confer permission outside the governing Execution Envelope.

### WorkspaceIsolation
The observable isolation boundary for a mutating cell. Git worktrees are one implementation; disposable checkouts, containers, VMs, remote workspaces, or equivalent sandboxes may satisfy the relation.

### BaselineSnapshot
An immutable reference to the accepted pre-execution state used for regression attribution and integration comparison.

### IntegrationCandidate
A set of verified cell outputs proposed for combination into a higher-level artifact or branch.

### IntegrationEdge
A typed dependency between cells or integration candidates.

### SharedDeveloperService
Read-mostly or safely namespaced infrastructure shared by multiple isolated cells, such as a language-server pool, symbol index, package cache, compiler cache, dependency graph, or static-analysis service.

### ContextEntropyObservation
A diagnostic observation about how much context, duplication, rehydration, irrelevant traversal, or integration rework a task consumed. It is not a truth score and cannot grant authority.

### FleetPressureObservation
Telemetry for concurrency, CPU, memory, storage, process count, provider limits, queueing, cost, or other resource pressure.

## Relationships

```text
FleetRun
  COMPILED_FROM -> TaskContract
  GOVERNED_BY -> ExecutionEnvelope
  CONTAINS -> ExecutionCell
  HAS_BASELINE -> BaselineSnapshot
  HAS_EDGE -> IntegrationEdge
  EMITS -> Receipt
  PRODUCES -> IntegrationCandidate

ExecutionCell
  EXECUTED_BY -> HarnessRuntime
  ROUTES_TO -> ModelProviderRoute
  ISOLATED_BY -> WorkspaceIsolation
  HOLDS -> OwnershipLease
  RESUMES_FROM -> ContextCapsule
  USES -> SharedDeveloperService
  EMITS -> Receipt
  OBSERVED_BY -> ContextEntropyObservation
  OBSERVED_BY -> FleetPressureObservation

IntegrationCandidate
  COMPOSED_OF -> ExecutionCell
  VERIFIED_BY -> IndependentVerifier
```

## Non-equivalences

```text
FleetRun != Authority
AgentCount != Capability Quality
Concurrency != Permission
Worktree != Mandate
Branch != Authority
Commit != Correctness
ContextCapsule != Memory Sovereignty
ContextCapsule != Permission
ModelRoute != Authority
RuntimeRoute != Identity
CacheHit != Evidence
PassingTests != FullCompatibility
Receipt != AutomaticTruth
```

## Invariants

1. A mutating cell has exactly one active ownership lease for each write scope it controls.
2. Concurrent mutating cells may not have unresolved overlapping write scopes.
3. Every child cell inherits an attenuated subset of the parent's authority and lifetime.
4. Baseline identity remains immutable for the life of a cell; a rebase or baseline change creates a new execution epoch or explicit transition record.
5. Context transfer cannot broaden permissions.
6. Shared developer services cannot become ungoverned communication or credential channels.
7. Integration and verification are distinct semantic roles even when implemented by the same product surface.
8. A builder cannot be the sole source of verification for its own acceptance criteria.
9. Context Entropy and thermodynamic observations are diagnostics, not authorization signals.
10. A FleetRun that cannot be stopped independently of worker cooperation is non-conforming.

## Context Entropy

Context Entropy extends the existing thermodynamic vocabulary with execution-context observations. It is intended to expose waste and cognitive load, not to reward artificial brevity.

Useful observations include:
- tokens loaded vs. tokens materially used;
- duplicated context ratio;
- repeated repository traversal;
- symbol-lookup cost;
- context rehydration cost;
- integration rework;
- number of cross-boundary dependencies required to complete a cell;
- verified artifact output per unit of context/compute.

High context entropy may indicate poor decomposition, excessive coupling, stale context, oversized files, weak indexing, or a task that should not have been parallelized.

Low context entropy does not prove correctness.

## Thermodynamic relationship

Fleet execution contributes to the Grid's thermodynamic state:

```text
compute energy + context energy + coordination energy
        -> execution work
        -> verified value output + friction + entropy + drift
```

The ontology may correlate fleet pressure and context entropy with defect rate, integration rework, cost, or recovery time. Correlation is evidence for routing and architecture review, not a basis for silently expanding or shrinking authority.

## Canonical rule

> Agent swarms are execution topology. Governance remains a separate source of authority.

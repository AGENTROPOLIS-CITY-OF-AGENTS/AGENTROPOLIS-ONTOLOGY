# Spatial Interface Ontology v1

## Purpose

Define the canonical semantic contract for Agentropolis spatial interfaces so district visual builds remain interoperable, hardware-independent, and semantically grounded.

## Core classes

### SpatialSurface
A user-facing Agentropolis interface whose navigation or status model is represented spatially.

### CameraMode
A declared camera behavior used by a SpatialSurface.

Allowed canonical modes:

- `overview-orthographic`
- `explore-free`
- `cinematic-perspective`
- `detail`
- `reduced-motion-static`
- `no-webgl-html`

### SpatialEntity
A rendered object mapped to an Agentropolis semantic entity.

Examples include district, building, room, rail, citizen, utility conduit, checkpoint, and application surface.

### VisualStateBinding
A mapping from a real or explicitly simulated system state to a visual property.

A VisualStateBinding must declare provenance class:

- `instrumented`
- `simulated`
- `unknown`

Unknown telemetry must not be represented as a fabricated numeric state.

## Canonical camera invariant

Every new or materially updated Agentropolis spatial build SHOULD expose `overview-orthographic` as its default orientation surface unless a documented accessibility, product, or technical constraint makes that inappropriate.

Perspective camera paths remain canonical for cinematic transitions and scroll-scrubbed storytelling.

The orthographic rule does not invalidate or replace existing authored perspective paths.

## Hardware independence invariant

SpatialSurface core functionality MUST NOT depend on dedicated local graphics hardware, CUDA, local AI accelerators, Blender runtime rendering, Unity, or Unreal Engine.

Canonical browser baseline:

`Three.js / compatible browser renderer -> WebGL`

WebGPU is an optional enhancement.

## Fallback invariant

Every spatial build MUST define:

- a reduced-motion mode, and
- a no-WebGL HTML path for core navigation/information.

## Progressive rendering tiers

- Tier 1: core orientation, navigation, semantic objects, low-cost lighting, HTML fallback.
- Tier 2: procedural animation, particles, richer materials, scroll choreography, agent motion.
- Tier 3: advanced shaders, splats, heavy post-processing, volumetric-style effects, large media.

Tier 2 and Tier 3 capabilities MUST NOT be required for basic usability.

## Thermodynamic visualization contract

Entropy, drift, load, policy state, or thermodynamic conditions MAY be visualized only when the source state is instrumented or explicitly marked simulated.

Recommended semantic mappings:

- entropy -> turbulence or noise intensity
- drift -> path deviation or spatial offset
- load -> density or pulse rate
- utility health -> conduit activity or emissive intensity
- policy boundary -> gate, zone, or checkpoint
- verification -> BE receipt or confirmation state

BE remains the system evaluator for spatial scene verification where evaluation is required. ASBE remains Entertainment District scoped and is not a system-wide evaluator.

## Reference implementation

AGENTROPOLIS-AQUADUCT is the current reference implementation for the spatial scene grammar, including procedural Three.js generation, authored camera paths, scroll-timeline bindings, reduced-motion fallback, no-WebGL fallback, and BE verification receipts.

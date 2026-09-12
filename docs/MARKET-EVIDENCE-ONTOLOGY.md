# Market Evidence Ontology

## Purpose

Normalize technical, market-structure, liquidity, macro, on-chain, and other financial observations so Agentropolis agents can reason over evidence without confusing evidence with authority.

## Core Entities

- `Instrument` — asset, pair, security, contract, pool, or market symbol.
- `Venue` — exchange, DEX, pool, broker, chain, or data venue.
- `MarketObservation` — timestamped statement derived from source data.
- `MarketFeature` — computed scalar or vector such as RSI, ATR, volume, momentum, or volatility.
- `MarketTransform` — transformed representation such as Heikin Ashi or Renko.
- `MarketPattern` — detected structure such as breakout, FVG, harmonic, candlestick, or reversal.
- `MarketRegime` — trend, range, volatility, liquidity, or other state classification.
- `MarketEvidence` — provenance-backed evidence bundle suitable for downstream reasoning.
- `Invalidation` — explicit condition that weakens or invalidates evidence.
- `Thesis` — synthesized interpretation across one or more evidence objects.
- `ExecutionEnvelope` — separate governance artifact that may authorize bounded action.

## Relationships

```text
Instrument -> observed_on -> Venue
MarketObservation -> describes -> Instrument
MarketFeature -> derived_from -> MarketObservation
MarketTransform -> derived_from -> MarketObservation
MarketPattern -> supported_by -> MarketFeature | MarketTransform | MarketObservation
MarketEvidence -> contains -> MarketPattern | MarketFeature | MarketObservation
MarketEvidence -> has_invalidation -> Invalidation
Thesis -> supported_by -> MarketEvidence
ExecutionEnvelope -> MAY_REFERENCE -> Thesis | MarketEvidence
ExecutionEnvelope -> DOES_NOT_INHERIT_AUTHORITY_FROM -> MarketEvidence
```

## Evidence Classes

### Deterministic / Reproducible
Examples: moving averages, ATR, RSI, OBV, PSAR, explicit breakout boundaries.

### Heuristic / Model-Based
Examples: reversal scoring, divergence, support/resistance clustering, harmonics.

### Subjective / Experimental
Examples: Elliott labels, Gann interpretations, lunar-cycle correlations.

Subjective and experimental evidence MUST carry lower default trust and explicit provenance/invalidation metadata. It MUST NOT silently increase execution authority.

## Correlation Semantics

Evidence can be related or derived from the same underlying price series. Downstream confluence engines SHOULD track feature families and dependency relationships so correlated indicators are not counted as independent confirmation.

## Authority Separation

Ontology describes what evidence *means*. It does not grant permission to trade, spend, settle, custody, withdraw, or change risk limits.

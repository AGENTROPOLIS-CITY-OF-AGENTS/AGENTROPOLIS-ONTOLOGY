# Institutional Onchain Movement Ontology Extension

## Purpose
Add canonical entities and relationships for institutional asset migration, settlement, interoperability, and benchmark state.

## Entities
- Institution
- AssetClass
- RegulatedLiability
- TokenizedDeposit
- TokenizedTreasury
- TokenizedBond
- TokenizedFund
- TokenizedSecurity
- Stablecoin
- SettlementRail
- Ledger
- Jurisdiction
- Counterparty
- MarketEvidence
- BenchmarkSnapshot
- InstitutionalRegime
- ExecutionEnvelope
- EvidenceReceipt

## Relationships
- Institution ISSUES Asset
- Institution HOLDS Asset
- Institution SETTLES_ON Rail
- Asset REPRESENTED_ON Ledger
- Asset GOVERNED_BY Jurisdiction
- Counterparty TRANSFERS_TO Counterparty
- MarketEvidence OBSERVES Event
- BenchmarkSnapshot AGGREGATES MarketEvidence
- BenchmarkSnapshot CLASSIFIES InstitutionalRegime
- InstitutionalRegime INFORMS ExecutionEnvelope
- ExecutionEnvelope REQUIRES AssuranceGate
- Action PRODUCES EvidenceReceipt

## Authority separation
Observation != causation
Signal != order
Benchmark != mandate
Presentation != authentication != authority
Configured != reachable
Execution != evidence

## Required semantics
Institutional movement can alter posture only through an explicit governed policy transition. Ontology relationships MUST NOT imply execution authority merely from observed volume, institutional identity, asset class, or regime score.

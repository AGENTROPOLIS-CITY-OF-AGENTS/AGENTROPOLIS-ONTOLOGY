# Intelligence claim and trial relationships (candidate ontology extension)
Status: semantic design, not schema deployment.

## Evidence classes
`PromotionalClaim` (original exact assertion), `ClaimArithmetic` (calculation only), `TransactionProof` (authenticated transaction and quantity), `RealizedPnLAssessment` (complete cost basis plus fees), `MarketCapObservation` (asset-wide measure), `SocialManipulationIndicator` (hypothesis, not verdict), `ImageExposureAssessment` (consented privacy test), `BillPeriod`, `PaymentEvidence`, `ModelTrial`, `EvaluationReceipt`.

## Required edge semantics
- `ClaimArithmetic derivedFrom PromotionalClaim` **does not entail** `verifiedBy TransactionProof`.
- `MarketCapObservation` cannot substitute for wallet-level fill or proceeds.
- `RealizedPnLAssessment verifiedBy TransactionProof` requires completeness evidence, fees and timeline.
- `PaymentEvidence confirms BillPeriod` only for matching payee and period, never by inherited prior-month state.
- `ImageExposureAssessment derivedFrom ConsentedImage` must carry authority, disclosure limitations and confidence.
- `ModelTrial evaluatedBy BE` and `produces EvaluationReceipt`; trial status does not imply approved or preferred model.
- All new evidence must specify source ID/hash, observed_at, confidence or explicit unknown, and `authority: none` unless a separately approved mandate supplies authority.

Canonical model evaluation ontology remains `docs/MODEL_PROVIDER_ONTOLOGY.md`; market ontology remains `docs/MARKET-EVIDENCE-ONTOLOGY.md`.

# System Watch Ontology Delta — 2026-09-27

## New/strengthened entities
AuthenticatedPrincipal
PresentationIdentity
RelayReservation
ObservedReachability
ConvergenceEpoch
LoadedCapability
CapabilityInventory
ComplianceReceipt
ProviderTermsVersion

## Required distinctions
PresentationIdentity != AuthenticatedPrincipal
ConfiguredRouter != ObservedReachability
InstalledCapability != LoadedCapability
LoadedCapability != AuthorizedEffect
Enrollment != Compliance
ReleaseTag != PromotionEvidence
Timeout != ProviderCancellation

## Relations
Citizen BINDS AuthenticatedPrincipal
Member ADMITTED_TO RouterSet
Member HOLDS RelayReservation
Runtime EXPOSES CapabilityInventory
Repo PRODUCES ComplianceReceipt
CreatorExecution GOVERNED_BY ProviderTermsVersion

These distinctions are canonical across Dispatch, AEGIS, Continuity, Creator and APCP migration.

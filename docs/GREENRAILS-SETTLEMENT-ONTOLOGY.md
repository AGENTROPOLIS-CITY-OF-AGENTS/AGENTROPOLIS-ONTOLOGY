# GREENRAILS Settlement Ontology v1

## Status

Draft canonical vocabulary for GREENRAILS × $XENTS × HOOD TERPS settlement. Mock-only.
Every conforming record carries `mock: true` and the display notice
`MOCK SETTLEMENT · NO FUNDS WILL MOVE`. This document authorizes no custody, swap, transfer,
payout, or live settlement.

Version identifier: `agentropolis.greenrails-settlement.v1`
Schema: `schemas/greenrails-settlement-v1.schema.json`
Invariants: `governance/greenrails-settlement-invariants.yaml`
Wire-level objects: AGENTROPOLIS-PAY-PROTOCOL `schemas/settlement-{quote,state,receipt}.schema.json`
and `specification/greenrails-settlement.md`.

## Relationship to Regulated Digital Money v1

This ontology specializes [regulated-digital-money-ontology-v1](./regulated-digital-money-ontology-v1.md):

- `InputLeg.assetClass` uses the RDM `AssetClass` values (`fiat_bank_deposit`,
  `regulated_stablecoin`, `cryptoasset`).
- `InputLeg.rail` extends RDM `SettlementRail` (`card`, `ach`, `wire`, `base_usdc`,
  `xrpl_xrp`, `xrpl_rlusd`, plus `base_eth`, `ethereum_eth`, `solana_sol`).
- USDC on Base is a `regulated_stablecoin`; $XENTS is a `cryptoasset` / closed-loop
  participation asset. Neither is a bank deposit.
- A GREENRAILS settlement is one `PaymentIntent` lifecycle under RDM; the RDM capability
  state for v1 is `sandbox` at most (`disabled` by default).

## Tier placement

```text
T0 Governance/Risk        SOVEREIGNTY, AEGIS-ASSURANCE, 54T, SENTINEL-6   -> MANUAL_REVIEW owner, audit
T1 Monetary authority     XENTS-CAPITAL-GRID                              -> $XENTS supply/route policy
T2 Protocol/Execution     PAY-PROTOCOL, PAYRAIL, GREENRAILS               -> quote, reserve, route, settle, sign
T3 Ledger/Treasury        54-FISCAL-CMD                                   -> receipts, reconciliation
T4 Commerce consumers     HOOD-TERPS, MAIN-STREET, CREATOR, GAMING-DISTRICT, DOCK -> listings, buyers, sellers
T5 Observability/Ops      MISSION-CONTROL, DEPLOY, HUB, AQUADUCT          -> status surfaces
```

## Entities

| Entity | Definition | Owner tier |
|---|---|---|
| Buyer | Party acquiring a HOOD TERPS item; supplies fiat or crypto input. | T4 |
| Seller | Current owner of the Legacy NFT; receives USDC on Base. Never required to accept $XENTS. | T4 |
| LegacyNft | Token on its native chain. `burnForbidden: true`, `bridgeForbidden: true`. | T4 (asset), T2 (transfer) |
| Quote | Immutable exact-output offer: input max, `$XENTS` exact output, USDC payout, fees, timeouts, thresholds. | T2 |
| Reservation | Hold of the full USDC payout from a liquidity source before any buyer input is accepted. | T2 / T3 |
| InputAuthorization | Buyer fiat/crypto authorization (not capture) on a rail. | T2 |
| XentsRoute | Conversion of input into exact `$XENTS` for participation/settlement. | T2 under T1 policy |
| NftTransfer | Transfer on the native chain to the buyer wallet. | T2 |
| UsdcPayout | Release of the reservation to the seller payout wallet on Base. | T2 |
| Receipt | Signed terminal record; links to a PAY receipt when a mandate applies. | T2 issues, T3 records |
| Refund | Compensating return of buyer input; only before the NFT has moved. | T2 |

## Fee vocabulary

`Fee { code, payer, asset, amount }` with `code ∈ {network, routing, processing, platform,
escrow}` and `payer ∈ {buyer, seller}`. Fees are disclosed amounts. No record may express a
price target, appreciation, yield, profit share, redemption right, or peg.

## State vocabulary

Success path:

```text
QUOTED -> USDC_RESERVED -> INPUT_AUTHORIZED -> XENTS_ROUTED -> NFT_TRANSFER_PENDING
  -> NFT_TRANSFER_CONFIRMED -> USDC_RELEASED -> RECEIPT_FINALIZED
```

Failure states: `QUOTE_EXPIRED`, `INPUT_FAILED`, `INSUFFICIENT_LIQUIDITY`,
`NFT_OWNERSHIP_CHANGED`, `NFT_TRANSFER_FAILED`, `CHAIN_CONFIRMATION_TIMEOUT`,
`USDC_PAYOUT_FAILED`, `REFUND_PENDING`, `REFUNDED`, `MANUAL_REVIEW`.

Terminal: `RECEIPT_FINALIZED`, `QUOTE_EXPIRED`, `INPUT_FAILED`, `INSUFFICIENT_LIQUIDITY`,
`REFUNDED`, `MANUAL_REVIEW`.

Routing rule: failures before input capture end directly; failures after capture but before
NFT movement compensate via `REFUND_PENDING -> REFUNDED`; failures after NFT movement never
auto-refund and escalate to `MANUAL_REVIEW` (T0). The full transition table is normative in
PAY-PROTOCOL `specification/greenrails-settlement.md`.

## Required fields

Every settlement record carries `timeouts` (`quoteTtlSeconds`, `inputAuthorizationSeconds`,
`nftTransferSeconds`, `usdcPayoutSeconds`) and `confirmationThresholds`
(`nftChainConfirmations`, `baseConfirmations`, optional `inputChainConfirmations`), plus an
`idempotencyKey`. Cross-chain settlement is not atomic; these fields make the governed
escrow explicit.

## Receipt

`Receipt { id, finalState, nftTransferVerified, usdcPayoutVerified, evidenceDigest,
signature }`. `finalState = RECEIPT_FINALIZED` requires both verified flags true. Signature
envelope: `alg ∈ {ed25519, es256, es256k, mock-none}`, `canonicalization: rfc8785-jcs`,
`payloadDigest` over the receipt without `signature`. `mock-none` is valid only while
`mock: true`.

## Invariants

Machine-readable list: `governance/greenrails-settlement-invariants.yaml`. Core set:

1. `reserve-before-accept`
2. `dual-verify-before-complete`
3. `no-burn-legacy-nft`
4. `xents-mandatory-participation-not-payout`
5. `usdc-base-payout`

## Validation rules

A component MUST reject or flag any record that:

- lacks `mock: true` or the exact display notice
- reaches `INPUT_AUTHORIZED` without a held reservation for the full USDC amount
- reaches `RECEIPT_FINALIZED` without both verification flags and tx references
- names a payout asset other than USDC on Base, or requires the seller to accept $XENTS
- moves the Legacy NFT off its native chain or to a burn address
- uses a state name outside the canonical list
- omits timeouts, confirmation thresholds, or an idempotency key
- contains price, yield, redemption, or peg language

## Cross-repo ownership

| Repository | Ownership |
|---|---|
| AGENTROPOLIS-ONTOLOGY | This vocabulary, invariants, tier mapping |
| AGENTROPOLIS-PAY-PROTOCOL | Wire schemas, transition table, validator, examples |
| AGENTROPOLIS-PAYRAIL / GREENRAILS | Execution adapters (mock), receipts, replay protection |
| AGENTROPOLIS-XENTS-CAPITAL-GRID | $XENTS route/supply policy |
| 54-FISCAL-CMD | Ledger and reconciliation of receipts |
| HOOD-TERPS | Listings and commerce surfaces; must render the display notice |
| AGENTROPOLIS-HUB | Registry and status |

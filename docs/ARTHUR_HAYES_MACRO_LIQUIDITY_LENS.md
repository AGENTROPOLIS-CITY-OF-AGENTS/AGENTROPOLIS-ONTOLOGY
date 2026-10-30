# Arthur Hayes Macro Liquidity Lens — Ontology Mapping (DRAFT)

**Status:** DRAFT_REVIEW_REQUIRED — proposed integration, not an active/canonical mind profile
**Version:** 0.1.0 (2026-10-08)
**Mind identity:** `people/arthur-hayes`
**Owning domain:** Treasury / Finance Intelligence
**Cognitive home:** J-SPACE ∞ / Mind Vault (reference profile, not impersonation)
**Source profile:** `AGENTROPOLIS-AGENT-MCP/mind-vault/candidates/arthur-hayes.json`
**Authority:** READ_ONLY_ANALYSIS_ONLY

## Existing ontology fit

No new trading authority, district, runtime, or executor is created.

| Existing construct | Arthur Hayes candidate lens usage |
| --- | --- |
| `MarketObservation` | Timestamped TGA, RRP, reserve balances, credit, FX, cross-asset, liquidity and crypto derivatives inputs; include provider and observation time |
| `MarketFeature` | Reproducible deltas, spreads, basis, open interest, futures funding, liquidation concentrations, estimated bank-credit impulses |
| `MarketRegime` | Hypotheses about liquidity expansion/contraction, credit disruption, capital allocation and leverage conditions |
| `MarketEvidence` | Provenance-backed bundle of independent observations and their calculations |
| `Thesis` | A Hayes-attributed narrative/hypothesis compared with countertheses and separately derived AGENTROPOLIS interpretation |
| `Invalidation` | Forecast falsifiers, horizon limits, absent expected flows or competing-cause evidence |
| `ExecutionEnvelope` | Separate bounded permission object, NEVER issued by the lens or inferred from `Thesis` |

Mind Vault identity is the existing J-SPACE `people/<slug>` holder convention. The proposed `CognitiveLens`, `AuthorThesis`, and `LensEvaluation` labels in downstream projections are *candidate vocabulary*, not currently asserted as canonical classes.

## Proposed graph edges (review-only)

```text
people/arthur-hayes
  -> AUTHORS -> AuthorEssay (primary URL, publication date)
  -> PROPOSES -> AuthorThesis
AuthorThesis
  -> ABOUT -> MarketRegime | Instrument | MarketObservation
  -> EVALUATED_AGAINST -> MarketEvidence
  -> CHALLENGED_BY -> CounterThesis
  -> INVALIDATED_BY -> Invalidation
CognitiveLens(arthur-hayes-macro-liquidity)
  -> ATTRIBUTED_TO -> people/arthur-hayes
  -> USES -> SourceBackedReasoningMethods
  -> PRODUCES -> DeliberationProposal
DeliberationProposal
  -> MAY_INFORM -> Thesis
  -> CANNOT_AUTHORIZE -> ExecutionEnvelope
```

`AUTHORS` is attribution, not correctness. `PROPOSES` is authorship, not verified causality. `EVALUATED_AGAINST` must reference independent observations when available.

## Candidate lens: six checkpoints

1. **Policy impulse.** Fed balance sheet, RMP/QE/QT, Treasury financing, TGA, ON RRP, money and credit aggregates, FX coordination. Separate monetary-base changes from Treasury debt swaps and mere account movements.
2. **Transmission.** Who obtains the funding and through which reserve, lending, currency or collateral channels? Do not assume liquidity reaches crypto.
3. **Capital allocation.** Compare demand for dollars in AI infrastructure, sovereign bonds, equities, stablecoins, and crypto markets. Include the possibility of investment crowding-out.
4. **Market structure.** Analyze basis, derivatives funding, leverage, open interest, exchange exposures, liquidations, liquidity and volatility.
5. **Conditional thesis.** Define directional scenario, mechanism, time horizon, confidence, data as-of dates and explicit invalidation. Never convert an author's predicted price into a market fact.
6. **Opposition and audit.** Require independent empirical counterthesis, historical/base-rate comparison, J-SPACE Heretic slot and Meta-J audit of correlated sources.

## Five candidate diagnostic questions

- Is liquidity actually growing, or is the same stock of dollars moving between holders?
- If credit expands, what institutions and asset classes absorb the marginal dollar?
- What observable link exists between the liquidity channel and BTC/ETH price behavior?
- Is there derivatives positioning that can overwhelm or reverse the macro impulse in the relevant horizon?
- What independent evidence, competing explanation, or expiration date would falsify the thesis?

## Read-only evidence packet shape (illustrative, not a new canonical schema)

```json
{
  "lens_id": "arthur-hayes-macro-liquidity",
  "person_id": "people/arthur-hayes",
  "status": "DRAFT_REVIEW_REQUIRED",
  "authority": "READ_ONLY",
  "task": "Evaluate a documented dollar-liquidity hypothesis",
  "source_claims": [
    {
      "classification": "AUTHOR_THESIS_NOT_VERIFIED_FACT",
      "source_url": "https://cryptohayes.substack.com/p/reality-test",
      "published_at": "2026-06-08"
    }
  ],
  "observations": [],
  "theses": [],
  "countertheses": [],
  "invalidations": [],
  "unknowns": [],
  "requires_human_review": true,
  "execution_authority": "NONE"
}
```

## Sources and caution

Authored primary essays:
- Arthur Hayes, [Reality Test](https://cryptohayes.substack.com/p/reality-test), 2026-06-08 — he revisits a failed simplified liquidity-to-Bitcoin inference and proposes capital allocation to AI investment as one explanation.
- Arthur Hayes, [Situationship](https://cryptohayes.substack.com/p/situationship), 2026-08-04 — proposes a speculative AI credit-misallocation / later intervention scenario.
- Arthur Hayes, [Same Same But Different](https://cryptohayes.substack.com/p/same-same-but-different), 2026-08-24 — speculates about US Treasury/Fed market-support mechanisms.
- Arthur Hayes, [Atención](https://cryptohayes.substack.com/p/atencion), 2026-09-02 — develops a EURJPY-centered observation and liquidity scenario.

These are **attributed public arguments**, not independent verification of projected outcomes. The system must not infer a reliable forecast record, real-time performance, or causal identification merely because a thesis is published. Preserve author investment exposures/conflicts when materially relevant.

## Boundaries, review and activation

- Keep the Mind Vault profile `DRAFT_REVIEW_REQUIRED` and `NOT_ACTIVE` pending human/evidence review.
- Preserve source URL, date, captured-at, content hash when independently captured, reviewer and review receipt.
- Verify raw macro and market data separately (e.g. actual Treasury/Fed releases and market venue history), especially before presenting quantitative insights.
- Mark `OBSERVED` author content separately from `VERIFIED` economic causal claims.
- Do not copy an author into a personality/avatar, impersonate him, fabricate quotes, or imply an endorsement.
- Preserve disagreement map, counterfactuals, liquidity/asset-allocation distinctions, source correlations and scenario expiry.
- J-SPACE, FIN54 and this ontology may produce evidence, hypotheses and drafts only. AEGIS / 54T / Mandate / ExecutionEnvelope govern any separately approved execution.
- No source branch/protection bypass, merge, production deployment, wallet interaction or trade is included here.

**Canonical invariant:** The person is a source-backed reasoning reference; the lens is a derived analytical tool; evidence is not an order.

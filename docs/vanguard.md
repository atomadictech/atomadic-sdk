# Vanguard -- SDK reference

> Entitlement `vanguard` - 5 tools - one MCP at `mcp.atomadic.tech`

```python
from atomadic import Atomadic, vanguard
ato = Atomadic(api_key='ato_...')
```

## `assess_mev_exposure_pure`

**In plain English** - Checks and scores mev exposure.

**Technical** - Heuristic MEV-exposure assessment of an order (size/public mempool/slippage) â†’ exposure tier + mitigations. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `order` | object | yes |  |

```python
vanguard.assess_mev_exposure_pure(ato, order=...)
```

## `assess_transaction_risk_pure`

**In plain English** - Checks and scores transaction risk.

**Technical** - Risk-score a proposed transaction (amount/recipient/contract/slippage) â†’ 0-1 risk + tier + hold/allow. Analysis only, no execution. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `transaction` | object | yes |  |

```python
vanguard.assess_transaction_risk_pure(ato, transaction=...)
```

## `compose_settlement_terms_pure`

**In plain English** - Builds settlement terms.

**Technical** - Compose advisory escrow/settlement terms for an A2A deal (release/refund conditions, dispute window). No funds move. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `amount_usd` | number | yes |  |
| `parties` | array | yes |  |
| `release_condition` | string | no |  |

```python
vanguard.compose_settlement_terms_pure(ato, amount_usd=..., parties=...)
```

## `compute_slippage_guard_pure`

**In plain English** - Calculates slippage guard.

**Technical** - Compute the minimum acceptable output (slippage guard) for a swap from expected out + tolerance bps. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `expected_out` | number | yes |  |
| `tolerance_bps` | number | no |  |

```python
vanguard.compute_slippage_guard_pure(ato, expected_out=...)
```

## `validate_spend_policy_pure`

**In plain English** - Checks whether it is valid spend policy.

**Technical** - Validate a transaction against a bounded spend policy (per_tx_max/daily_max/allowlist) â†’ allow/deny + remaining budget. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `transaction` | object | yes |  |
| `budget` | object | yes |  |

```python
vanguard.validate_spend_policy_pure(ato, transaction=..., budget=...)
```

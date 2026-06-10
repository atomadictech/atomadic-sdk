# Catalyst -- SDK reference

> Entitlement `catalyst` - 5 tools - one MCP at `mcp.atomadic.tech`

```python
from atomadic import Atomadic, catalyst
ato = Atomadic(api_key='ato_...')
```

## `compose_paywall_policy_pure`

**In plain English** - Builds paywall policy.

**Technical** - Compose an HTTP 402 paywall policy (x402 challenge spec) for a resource. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `resource` | string | yes |  |
| `price_usd` | number | yes |  |
| `currency` | string | no |  |

```python
catalyst.compose_paywall_policy_pure(ato, resource=..., price_usd=...)
```

## `compute_settlement_split_pure`

**In plain English** - Calculates settlement split.

**Technical** - Split a payment across parties by basis points (sum 10000) with exact largest-remainder cent rounding. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `amount` | number | yes |  |
| `splits` | array | yes |  |

```python
catalyst.compute_settlement_split_pure(ato, amount=..., splits=...)
```

## `compute_usage_meter_pure`

**In plain English** - Calculates usage meter.

**Technical** - Aggregate usage events into a billable total at a per-unit rate, with per-sku breakdown. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `events` | array | yes |  |
| `rate_per_unit` | number | yes |  |

```python
catalyst.compute_usage_meter_pure(ato, events=..., rate_per_unit=...)
```

## `compute_x402_quote_pure`

**In plain English** - Calculates x402 quote.

**Technical** - Compute an x402 metered quote â€” bill overage above plan-included units. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `units` | number | yes |  |
| `rate_per_unit` | number | yes |  |
| `included_units` | number | no |  |

```python
catalyst.compute_x402_quote_pure(ato, units=..., rate_per_unit=...)
```

## `validate_quota_tree_pure`

**In plain English** - Checks whether it is valid quota tree.

**Technical** - Validate a hierarchical quota tree (children sum â‰¤ parent limit, no negatives) â†’ valid + violations. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `tree` | object | yes |  |

```python
catalyst.validate_quota_tree_pure(ato, tree=...)
```

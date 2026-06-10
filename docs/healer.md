# Healer -- SDK reference

> Entitlement `healer` - 5 tools - one MCP at `mcp.atomadic.tech`

```python
from atomadic import Atomadic, healer
ato = Atomadic(api_key='ato_...')
```

## `assess_artifact_health_pure`

**In plain English** - Checks and scores artifact health.

**Technical** - Composite code-health diagnosis of a provided artifact: parses + logic density + single-callable + stub signals, graded A-F with issues. Read-only. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `module_name` | string | no |  |
| `source_text` | string | yes |  |

```python
healer.assess_artifact_health_pure(ato, source_text=...)
```

## `classify_failure_mode_pure`

**In plain English** - Sorts into categories failure mode.

**Technical** - Classify an error/traceback into a failure-mode taxonomy (import/type/value/io/network/auth/syntax/assertion/recursion/memory) with likely cause + first step. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `error_message` | string | yes |  |

```python
healer.classify_failure_mode_pure(ato, error_message=...)
```

## `compose_rollback_plan_pure`

**In plain English** - Builds rollback plan.

**Technical** - Compose an ordered, advisory rollback plan from an error context + change summary: contain â†’ revert â†’ verify â†’ guard â†’ post-mortem. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `error_message` | string | yes |  |
| `change_summary` | string | no |  |

```python
healer.compose_rollback_plan_pure(ato, error_message=...)
```

## `compute_blast_radius_pure`

**In plain English** - Calculates blast radius.

**Technical** - Estimate the blast radius of changing a symbol in a source: total references, using-functions, public-surface flag â†’ low/medium/high radius. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `source_text` | string | yes |  |
| `symbol` | string | yes |  |

```python
healer.compute_blast_radius_pure(ato, source_text=..., symbol=...)
```

## `compute_repair_plan_pure`

**In plain English** - Calculates repair plan.

**Technical** - Compute an advisory repair plan for a provided broken artifact + its error: category, severity, concrete steps, confidence. Read-only â€” application stays with the customer/operator. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `error_message` | string | yes |  |
| `source_text` | string | no |  |

```python
healer.compute_repair_plan_pure(ato, error_message=...)
```

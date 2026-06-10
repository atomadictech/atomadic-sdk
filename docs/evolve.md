# Evolve -- SDK reference

> Entitlement `evolve` - 5 tools - one MCP at `mcp.atomadic.tech`

```python
from atomadic import Atomadic, evolve
ato = Atomadic(api_key='ato_...')
```

## `assess_improvement_candidates_pure`

**In plain English** - Checks and scores improvement candidates.

**Technical** - Propose bounded, simulated improvement candidates for your source â€” missing docstrings/type-hints/guards, bare excepts, stub signals â€” each risk-graded with a simulated gain and a promotion verdict. Read-only/advisory; operates only on the source you provide. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `source_text` | string | yes |  |
| `module_name` | string | yes |  |

```python
evolve.assess_improvement_candidates_pure(ato, source_text=..., module_name=...)
```

## `assess_regression_risk_pure`

**In plain English** - Checks and scores regression risk.

**Technical** - Assess regression risk of a change: public symbols in scope, control-flow complexity, I/O/side-effects, risk keywords â†’ low/medium/high tier + drivers. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `source_text` | string | yes |  |
| `change_summary` | string | no |  |

```python
evolve.assess_regression_risk_pure(ato, source_text=...)
```

## `compose_mutation_plan_pure`

**In plain English** - Builds mutation plan.

**Technical** - Propose a bounded, ordered mutation plan for a source toward a goal â€” safe risk-tiered transforms. Advisory. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `source_text` | string | yes |  |
| `goal` | string | no |  |

```python
evolve.compose_mutation_plan_pure(ato, source_text=...)
```

## `rank_evolution_candidates_pure`

**In plain English** - Orders by importance evolution candidates.

**Technical** - Rank candidate improvements by value (simulated_gain weighted by risk) â†’ ordered list with scores. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `candidates` | array | yes |  |

```python
evolve.rank_evolution_candidates_pure(ato, candidates=...)
```

## `score_evolution_fitness_pure`

**In plain English** - Scores evolution fitness.

**Technical** - Compare a before/after source pair on fitness dimensions (parse health, functions, docs, LOC, stubs) â†’ per-dimension deltas + improved/neutral/regressed verdict. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `before_source` | string | yes |  |
| `after_source` | string | yes |  |

```python
evolve.score_evolution_fitness_pure(ato, before_source=..., after_source=...)
```

# Research -- SDK reference

> Entitlement `research` - 5 tools - one MCP at `mcp.atomadic.tech`

```python
from atomadic import Atomadic, research
ato = Atomadic(api_key='ato_...')
```

## `compose_experiment_design_pure`

**In plain English** - Builds experiment design.

**Technical** - Turn a hypothesis into an experiment design: variables, method, control, sample, success criterion, threats to validity, falsifier. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `hypothesis` | string | yes |  |

```python
research.compose_experiment_design_pure(ato, hypothesis=...)
```

## `compose_literature_query_pure`

**In plain English** - Builds literature query.

**Technical** - Turn a topic into structured search queries across angles + source types to weight. Composes queries; fetches nothing. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `topic` | string | yes |  |

```python
research.compose_literature_query_pure(ato, topic=...)
```

## `compose_problem_decomposition_pure`

**In plain English** - Builds problem decomposition.

**Technical** - Decompose an open problem into dependency-ordered sub-problems (defineâ†’constraintsâ†’exploreâ†’designâ†’buildâ†’verify) + critical path. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `problem` | string | yes |  |

```python
research.compose_problem_decomposition_pure(ato, problem=...)
```

## `compose_research_panel_pure`

**In plain English** - Builds research panel.

**Technical** - Turn an open question into a structured cross-domain research scaffold: per-lens (correctness/performance/security/usability/data/cost) testable hypotheses, the evidence that would confirm each, and a falsifier, plus a synthesis. Pure, deterministic. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `question` | string | yes |  |
| `context` | string | no |  |

```python
research.compose_research_panel_pure(ato, question=...)
```

## `rank_hypotheses_pure`

**In plain English** - Orders by importance hypotheses.

**Technical** - Rank hypotheses by priority = impact Ã— tractability Ã· (uncertainty+1) â†’ ordered list. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `hypotheses` | array | yes |  |

```python
research.rank_hypotheses_pure(ato, hypotheses=...)
```

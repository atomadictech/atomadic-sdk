# Proving Ground -- SDK reference

> Entitlement `proving` - 5 tools - one MCP at `mcp.atomadic.tech`

```python
from atomadic import Atomadic, proving
ato = Atomadic(api_key='ato_...')
```

## `assess_proof_readiness_pure`

**In plain English** - Checks and scores proof readiness.

**Technical** - Assess ship/proof-readiness of provided source: docstring, returns-value, guards/asserts, type-hints, stub-free â†’ score + ready verdict. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `source_text` | string | yes |  |

```python
proving.assess_proof_readiness_pure(ato, source_text=...)
```

## `assess_test_quality_pure`

**In plain English** - Checks and scores test quality.

**Technical** - Assess test-suite quality: test count, assertions, edge-case + error-path coverage, mocks/fixtures, parametrization â†’ 0-1 quality score + findings. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `test_source` | string | yes |  |

```python
proving.assess_test_quality_pure(ato, test_source=...)
```

## `compute_proof_obligations_pure`

**In plain English** - Calculates proof obligations.

**Technical** - Extract per-function proof obligations: preconditions, return paths, error contracts, and a plain-language obligation statement. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `source_text` | string | yes |  |

```python
proving.compute_proof_obligations_pure(ato, source_text=...)
```

## `score_documentation_coverage_pure`

**In plain English** - Scores documentation coverage.

**Technical** - Score docstring coverage (module + every function/class) â†’ documented fraction, undocumented names, good/partial/poor verdict. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `source_text` | string | yes |  |

```python
proving.score_documentation_coverage_pure(ato, source_text=...)
```

## `score_test_coverage_pure`

**In plain English** - Scores test coverage.

**Technical** - Estimate test coverage: which top-level functions in the source are referenced by the test source; returns covered/uncovered + coverage ratio. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `source_text` | string | yes |  |
| `test_source` | string | yes |  |

```python
proving.score_test_coverage_pure(ato, source_text=..., test_source=...)
```

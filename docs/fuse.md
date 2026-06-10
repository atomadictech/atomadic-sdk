# Fuse -- SDK reference

> Entitlement `fuse` - 7 tools - one MCP at `mcp.atomadic.tech`

```python
from atomadic import Atomadic, fuse
ato = Atomadic(api_key='ato_...')
```

## `assess_architecture_pure`

**In plain English** - Checks and scores architecture.

**Technical** - Analyze a provided Python source's architecture vs the Atomadic 5-tier / single-callable discipline: callables, single-callable, imports + tier directions, logic density, tier hint, findings, verdict. Operates only on the provided source. _(plan: free)_

| arg | type | required | description |
|---|---|---|---|
| `module_name` | string | yes |  |
| `source_text` | string | yes |  |

```python
fuse.assess_architecture_pure(ato, module_name=..., source_text=...)
```

## `assess_import_direction_pure`

**In plain English** - Checks and scores import direction.

**Technical** - Tier-law check: verify a source's atomadic imports respect the 5-tier downward-only law (tier-N imports tier-&lt;N only); reports same-tier and upward violations. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `source_text` | string | yes |  |
| `tier` | integer | yes |  |

```python
fuse.assess_import_direction_pure(ato, source_text=..., tier=...)
```

## `assess_naming_clarity_pure`

**In plain English** - Checks and scores naming clarity.

**Technical** - Naming clarity: verb-led function names, length bounds, no single-char variables â†’ clarity score + findings. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `source_text` | string | yes |  |

```python
fuse.assess_naming_clarity_pure(ato, source_text=...)
```

## `compute_complexity_metrics_pure`

**In plain English** - Calculates complexity metrics.

**Technical** - Per-function complexity: cyclomatic complexity, max nesting depth, params, line span â†’ module verdict (ok/refactor). _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `source_text` | string | yes |  |

```python
fuse.compute_complexity_metrics_pure(ato, source_text=...)
```

## `extract_call_graph_pure`

**In plain English** - Pulls out call graph.

**Technical** - Intra-module call graph: per-function callees, entrypoints, and leaves. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `source_text` | string | yes |  |

```python
fuse.extract_call_graph_pure(ato, source_text=...)
```

## `orchestrate_s2s_temporal`

**In plain English** - Runs the full flow for s2s.

**Technical** - Spaghetti-to-shippable: turn a single repo + an intent into a gated, shippable product package. Public profile is BOUNDED â€” single-repo harvest, tier-5-max emission, redaction (enforce_public_s2s_constraints). Dry-run by default. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `intent` | string | yes | What to build from the source |
| `target_source` | string | no | Path/ref to the single source repo to transform |
| `dry_run` | boolean | no | Plan only (default true) |

```python
fuse.orchestrate_s2s_temporal(ato, intent=...)
```

## `scan_code_stubs_pure`

**In plain English** - Scans for code stubs.

**Technical** - Stub-hunter: scan provided source for stub/scaffold/placeholder patterns (NotImplementedError, TODO/FIXME, ellipsis/pass-only bodies, empty-shell returns). Returns REAL or STUB + findings. _(plan: free)_

| arg | type | required | description |
|---|---|---|---|
| `source_text` | string | yes |  |

```python
fuse.scan_code_stubs_pure(ato, source_text=...)
```

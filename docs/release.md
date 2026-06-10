# Release -- SDK reference

> Entitlement `release` - 9 tools - one MCP at `mcp.atomadic.tech`

```python
from atomadic import Atomadic, release
ato = Atomadic(api_key='ato_...')
```

## `compose_changelog_pure`

**In plain English** - Builds changelog.

**Technical** - Compose a grouped changelog (Breaking/Features/Fixes/Other) from change entries â†’ structured groups + markdown. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `entries` | array | yes |  |
| `version` | string | no |  |

```python
release.compose_changelog_pure(ato, entries=...)
```

## `compute_semver_bump_pure`

**In plain English** - Calculates semver bump.

**Technical** - Decide the semver bump (major/minor/patch) from change descriptions and compute the next version. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `change_descriptions` | array | yes |  |
| `current_version` | string | no |  |

```python
release.compute_semver_bump_pure(ato, change_descriptions=...)
```

## `record_release_template_stateful`

**In plain English** - Records release template.

**Technical** - Register a release template (ours or customer BYO) into the template registry ledger. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `brand` | object | no |  |
| `kind` | string | yes |  |
| `registry_path` | string | yes |  |
| `source_kind` | string | yes |  |
| `source_ref` | string | yes |  |
| `template_id` | string | yes |  |
| `tokens` | array | no |  |

```python
release.record_release_template_stateful(ato, kind=..., registry_path=..., source_kind=..., source_ref=...)
```

## `render_from_template_pure`

**In plain English** - Produces from template.

**Technical** - Deterministically render a {{token}} text template from a context mapping. Ours or customer templates, one code path. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `context` | object | yes |  |
| `missing` | string | no |  |
| `template` | string | yes |  |

```python
release.render_from_template_pure(ato, context=..., template=...)
```

## `render_website_stateful`

**In plain English** - Produces website.

**Technical** - Render a static website from a template directory (ours or customer's) into an output dir; {{token}} substitution + assets. Ready for Cloudflare Pages. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `context` | object | yes |  |
| `include_ext` | array | no |  |
| `output_dir` | string | yes |  |
| `template_dir` | string | yes |  |

```python
release.render_website_stateful(ato, context=..., output_dir=..., template_dir=...)
```

## `scan_release_templates_stateful`

**In plain English** - Scans for release templates.

**Technical** - List registered release templates (latest per id), optional kind filter. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `kind` | string | no |  |
| `registry_path` | string | yes |  |

```python
release.scan_release_templates_stateful(ato, registry_path=...)
```

## `serve_cloudflare_pages_stateful`

**In plain English** - Serves cloudflare pages.

**Technical** - Deploy a built site to Cloudflare Pages via wrangler. Dry-run by default; live ONLY with operator_authorized=true. _(plan: teams)_

| arg | type | required | description |
|---|---|---|---|
| `branch` | string | no |  |
| `directory` | string | yes |  |
| `operator_authorized` | boolean | no |  |
| `project_name` | string | yes |  |
| `vault_path` | string | no |  |

```python
release.serve_cloudflare_pages_stateful(ato, directory=..., project_name=...)
```

## `serve_cloudflare_worker_stateful`

**In plain English** - Serves cloudflare worker.

**Technical** - Deploy a Cloudflare Worker (e.g. the MCP edge) via wrangler. Dry-run by default; live ONLY with operator_authorized=true. _(plan: teams)_

| arg | type | required | description |
|---|---|---|---|
| `operator_authorized` | boolean | no |  |
| `vault_path` | string | no |  |
| `worker_dir` | string | yes |  |
| `worker_name` | string | no |  |

```python
release.serve_cloudflare_worker_stateful(ato, worker_dir=...)
```

## `validate_release_readiness_pure`

**In plain English** - Checks whether it is valid release readiness.

**Technical** - Validate release readiness from a checklist (tests/no-stubs/version/changelog/secrets/docs) â†’ go/no-go + blockers. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `checklist` | object | yes |  |

```python
release.validate_release_readiness_pure(ato, checklist=...)
```

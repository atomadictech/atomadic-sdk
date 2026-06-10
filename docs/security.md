# Security -- SDK reference

> Entitlement `security` - 9 tools - one MCP at `mcp.atomadic.tech`

```python
from atomadic import Atomadic, security
ato = Atomadic(api_key='ato_...')
```

## `assess_security_bubble_pure`

**In plain English** - Checks and scores security bubble.

**Technical** - Bubble check: sandbox-scan a content snippet for adversarial / prompt-injection / exfiltration / jailbreak patterns; returns PROCEED / REVIEW / BLOCK with the threats detected. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `content` | string | yes |  |
| `strict` | boolean | no |  |

```python
security.assess_security_bubble_pure(ato, content=...)
```

## `classify_error_fold_pure`

**In plain English** - Sorts into categories error fold.

**Technical** - Classify an error-fold entry with severity, category, and a suggested repair path before Healer ingests it. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `action_kind` | string | no |  |
| `error_message` | string | yes |  |

```python
security.classify_error_fold_pure(ato, error_message=...)
```

## `compute_hardening_posture_pure`

**In plain English** - Calculates hardening posture.

**Technical** - Compute the recommended hardening posture (cumulative directives) for a target product at a level (info/low/medium/high/critical); critical requires operator co-sign. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `hardening_level` | string | yes |  |
| `target_product_id` | string | yes |  |

```python
security.compute_hardening_posture_pure(ato, hardening_level=..., target_product_id=...)
```

## `compute_redacted_args_pure`

**In plain English** - Calculates redacted args.

**Technical** - Redact a tool-args object: replaces secret-pattern values and secret-named fields with safe placeholders (nested-aware). _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `args` | object | yes |  |

```python
security.compute_redacted_args_pure(ato, args=...)
```

## `compute_redacted_text_pure`

**In plain English** - Calculates redacted text.

**Technical** - Redact secrets from free-form text; replaces each match with a verify-without-reveal placeholder [REDACTED:kind:sha8]. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `text` | string | yes |  |

```python
security.compute_redacted_text_pure(ato, text=...)
```

## `compute_threat_model_pure`

**In plain English** - Calculates threat model.

**Technical** - STRIDE threat model for a component (sample threat + mitigation per category), prioritized by exposure. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `component` | string | yes |  |
| `exposure` | string | no |  |

```python
security.compute_threat_model_pure(ato, component=...)
```

## `define_security_constants_pure`

**In plain English** - Returns the canonical security constants.

**Technical** - Canonical Security constants: bubble verdicts, hardening levels + cumulative directives, error-fold categories, redaction kinds, PQC standard (FIPS-203). _(plan: free)_

```python
security.define_security_constants_pure(ato)
```

## `scan_dependency_risk_pure`

**In plain English** - Scans for dependency risk.

**Technical** - Scan a requirements list for supply-chain risk (unpinned, wildcard, VCS/URL install, insecure scheme) â†’ findings + verdict. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `requirements_text` | string | yes |  |

```python
security.scan_dependency_risk_pure(ato, requirements_text=...)
```

## `validate_secret_hygiene_pure`

**In plain English** - Checks whether it is valid secret hygiene.

**Technical** - Scan source for hardcoded secrets (AWS keys, private keys, API tokens, passwords, connection strings) â†’ redacted findings + hygiene verdict. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `source_text` | string | yes |  |

```python
security.validate_secret_hygiene_pure(ato, source_text=...)
```

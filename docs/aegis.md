# Aegis -- SDK reference

> Entitlement `aegis` - 5 tools - one MCP at `mcp.atomadic.tech`

```python
from atomadic import Atomadic, aegis
ato = Atomadic(api_key='ato_...')
```

## `assess_compliance_posture_pure`

**In plain English** - Checks and scores compliance posture.

**Technical** - Score declared controls vs a framework checklist (EU AI Act / NIST RMF / ISO 27001) â†’ coverage + gaps. Self-assessment scaffold, not a legal cert. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `controls` | array | yes |  |
| `framework` | string | no |  |

```python
aegis.assess_compliance_posture_pure(ato, controls=...)
```

## `classify_data_sensitivity_pure`

**In plain English** - Sorts into categories data sensitivity.

**Technical** - Classify data sensitivity of a text sample (PII/PHI/financial/secret/gov-id) â†’ tier + categories. Detection only. _(plan: dev)_

| arg | type | required | description |
|---|---|---|---|
| `text` | string | yes |  |

```python
aegis.classify_data_sensitivity_pure(ato, text=...)
```

## `compose_governance_report_pure`

**In plain English** - Builds governance report.

**Technical** - Compose a governance report (compliance coverage + incidents + policies) â†’ governance score, A-D grade, recommendations. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `system_name` | string | yes |  |
| `compliance_coverage` | number | no |  |
| `open_incidents` | integer | no |  |
| `policies_enforced` | integer | no |  |

```python
aegis.compose_governance_report_pure(ato, system_name=...)
```

## `compute_audit_trail_digest_pure`

**In plain English** - Calculates audit trail digest.

**Technical** - Build a tamper-evident hash-chained digest over audit events (sha256(prev+event)); any change alters the head. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `events` | array | yes |  |

```python
aegis.compute_audit_trail_digest_pure(ato, events=...)
```

## `enforce_action_policy_pure`

**In plain English** - Applies the rules to action policy.

**Technical** - Deterministic action-policy engine: evaluate an action against allow/deny rules â†’ permit/deny + matched rule. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `action` | object | yes |  |
| `policy` | object | yes |  |

```python
aegis.enforce_action_policy_pure(ato, action=..., policy=...)
```

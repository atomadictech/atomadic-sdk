# Nexus -- SDK reference

> Entitlement `nexus` - 13 tools - one MCP at `mcp.atomadic.tech`

```python
from atomadic import Atomadic, nexus
ato = Atomadic(api_key='ato_...')
```

## `assess_nexus_trust_phase_stateful`

**In plain English** - Checks and scores nexus trust phase.

**Technical** - Compute an actor's current trust phase (genesis/building/attested/sovereign/escalated) by reading their attestation history from the ledger. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `actor` | string | no |  |
| `has_federated_key` | boolean | no |  |
| `ledger_path` | string | yes |  |

```python
nexus.assess_nexus_trust_phase_stateful(ato, ledger_path=...)
```

## `assess_sybil_risk_pure`

**In plain English** - Checks and scores sybil risk.

**Technical** - Topological Identity: score Sybil/identity risk from signals (age, attestations, peers, shared fingerprints) â†’ 0-1 risk + tier. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `signals` | object | yes |  |

```python
nexus.assess_sybil_risk_pure(ato, signals=...)
```

## `classify_action_severity_pure`

**In plain English** - Sorts into categories action severity.

**Technical** - Classify action severity (low/medium/high/critical) â†’ trust-phase floor, operator-cosign requirement, hallucination-bound enforcement. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `action_kind` | string | yes |  |
| `context` | string | no |  |

```python
nexus.classify_action_severity_pure(ato, action_kind=...)
```

## `compute_reputation_score_pure`

**In plain English** - Calculates reputation score.

**Technical** - Reputation Ledger: 0-1 reputation from recency-decayed peer-rating events. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `events` | array | yes |  |

```python
nexus.compute_reputation_score_pure(ato, events=...)
```

## `compute_trust_score_pure`

**In plain English** - Calculates trust score.

**Technical** - Compute a 0-1 trust score + phase from attestation count, recent escalations, account age, and federation. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `attestation_count` | integer | yes |  |
| `recent_escalations` | integer | yes |  |
| `account_age_days` | integer | yes |  |
| `has_federated_key` | boolean | no |  |

```python
nexus.compute_trust_score_pure(ato, attestation_count=..., recent_escalations=..., account_age_days=...)
```

## `compute_verified_randomness_pure`

**In plain English** - Calculates verified randomness.

**Technical** - VeriRand: deterministic verifiable randomness from a seed (sha256 hash-chain + commitment); re-derivable and verifiable. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `seed` | string | yes |  |
| `count` | integer | no |  |

```python
nexus.compute_verified_randomness_pure(ato, seed=...)
```

## `define_nexus_constants_pure`

**In plain English** - Returns the canonical nexus constants.

**Technical** - The canonical Nexus trust constants: 5 trust phases + thresholds, 4 severities with phase floor + co-signers, signer modes, the 0.95 hallucination-bound floor, attestation schema, and 5 refusal codes. _(plan: free)_

```python
nexus.define_nexus_constants_pure(ato)
```

## `enforce_nexus_gate_stateful`

**In plain English** - Applies the rules to nexus gate.

**Technical** - Gate-2 two-gate enforcement: resolve trust phase, check severity ceiling, enforce the 0.95 hallucination bound for high/critical, require Gate-1 entitlement; on PASS issue + ledger an attestation. Returns PASS/BLOCKED/ESCALATE + refusal code. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `action_kind` | string | yes |  |
| `attestation_count` | integer | no |  |
| `bound_score` | number/null | no |  |
| `entitlement_ok` | boolean | no |  |
| `has_federated_key` | boolean | no |  |
| `ledger_path` | string | no |  |
| `payload` | object | no |  |
| `recent_escalations` | integer | no |  |
| `severity` | string | yes |  |

```python
nexus.enforce_nexus_gate_stateful(ato, action_kind=..., severity=...)
```

## `match_agent_capability_pure`

**In plain English** - Finds the best match for agent capability.

**Technical** - Agent Discovery: match a required capability set against candidate agents, ranked by coverage. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `need` | array | yes |  |
| `candidates` | array | yes |  |

```python
nexus.match_agent_capability_pure(ato, need=..., candidates=...)
```

## `record_nexus_attestation_stateful`

**In plain English** - Records nexus attestation.

**Technical** - Issue a Nexus attestation envelope (atomadic.nexus_attestation.v1) and append it to the hash-chained attestation ledger. Deterministic envelope + attest:&lt;12-hex&gt; id. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `action_kind` | string | yes |  |
| `bound_score` | number/null | no |  |
| `ledger_path` | string | yes |  |
| `payload` | object | no |  |
| `severity` | string | yes |  |
| `signer_mode` | string | no |  |
| `trust_phase` | string | no |  |

```python
nexus.record_nexus_attestation_stateful(ato, action_kind=..., ledger_path=..., severity=...)
```

## `record_nexus_escalation_stateful`

**In plain English** - Records nexus escalation.

**Technical** - Emit a Nexus escalation envelope to the Operator surface when an action is at the trust-phase boundary (ESCALATION_REQUIRED). _(plan: enterprise)_

| arg | type | required | description |
|---|---|---|---|
| `action_kind` | string | yes |  |
| `actor` | string | no |  |
| `escalation_path` | string | yes |  |
| `reason` | string | no |  |
| `severity` | string | no |  |

```python
nexus.record_nexus_escalation_stateful(ato, action_kind=..., escalation_path=...)
```

## `scan_nexus_attestation_history_stateful`

**In plain English** - Scans for nexus attestation history.

**Technical** - Query the attestation ledger by action kind, signer mode, and/or trust phase; returns recent matching attestations. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `action_kind` | string | no |  |
| `ledger_path` | string | yes |  |
| `limit` | integer | no |  |
| `phase` | string | no |  |
| `signer_mode` | string | no |  |

```python
nexus.scan_nexus_attestation_history_stateful(ato, ledger_path=...)
```

## `validate_delegation_chain_pure`

**In plain English** - Checks whether it is valid delegation chain.

**Technical** - VeriDelegate: validate a UCAN-style capability delegation chain â€” attenuation, audienceâ†’issuer continuity, expiry monotonicity. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `chain` | array | yes |  |

```python
nexus.validate_delegation_chain_pure(ato, chain=...)
```

# Atomadic Python SDK

[![PyPI](https://img.shields.io/pypi/v/atomadic.svg)](https://pypi.org/project/atomadic/)  [![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

**One MCP. One key. Every tool-set you are entitled to.**

Atomadic is sovereign infrastructure for the agent economy. Mount one MCP at
`mcp.atomadic.tech`; your **entitlement key** decides which product tool-sets you
can call. Every call passes Gate-1 (entitlement) then Gate-2 (trust).

- **Docs:** https://atomadic.tech/docs.html
- **Architecture:** https://atomadic.tech/docs.html?d=architecture
- **Support:** support@atomadic.tech

## Install

```bash
pip install atomadic
```

## Quickstart

```python
from atomadic import Atomadic, fuse

ato = Atomadic(api_key='ato_...')  # or set ATOMADIC_KEY env var

# Call any tool your plan unlocks:
result = fuse.assess_architecture_pure(
    ato,
    source_text='def f(x):\n    return x + 1',
    module_name='f_pure',
)
print(result['verdict'], result['density'])

# Or browse the surface your key unlocks:
for t in ato.list_tools():
    print(t['name'])
```

## Authentication

Get an entitlement key from [atomadic.tech](https://atomadic.tech). The key is decoded
and verified at the edge on every call; minting is internal-only. Keep keys
server-side -- the gate refuses out-of-plan calls, but secrets belong in your env.

```python
ato = Atomadic(api_key='ato_<blob>_<sig>')
# or:  export ATOMADIC_KEY=ato_<blob>_<sig>
```

## Products & tool-sets

Each product is an entitlement-gated tool-set; hold the entitlement, call the tool.
Reserved products (Vanguard, Aegis, Catalyst) and roadmap (Evolve, Research, Mind-Lab)
are not yet in the SDK.

### Murmuration [live]

`entitlement: murmuration` &middot; `from atomadic import murmuration`

> _The whole lattice in one entitlement._

Umbrella entitlement: every public product's tool-set under one key.

| Tool | Required args |
|---|---|
| **`omega_agent_heartbeat`** | `agent_id`, `ledger_path` |
| **`omega_attention_marker`** | `agent_id`, `ledger_path`, `focus` |
| **`omega_handoff_capsule`** | `from_agent_id`, `ledger_path`, `next_step` |
| **`omega_lane`** | (none) |
| **`omega_propose_mwo`** | `intent`, `ledger_path` |

```python
from atomadic import Atomadic, murmuration
ato = Atomadic(api_key='ato_...')
murmuration.omega_agent_heartbeat(ato, agent_id=..., ledger_path=...)
```

See per-tool docstrings for full arg schemas: `help(murmuration.omega_agent_heartbeat)`

### Fuse [live]

`entitlement: fuse` &middot; `from atomadic import fuse`

> _Architecture compiler -- AI writes code, we give it architecture._

Analyze your code against the 5-tier, single-callable discipline.

| Tool | Required args |
|---|---|
| **`assess_architecture_pure`** | `source_text`, `module_name` |
| **`assess_import_direction_pure`** | `source_text`, `tier` |
| **`scan_code_stubs_pure`** | `source_text` |

```python
from atomadic import Atomadic, fuse
ato = Atomadic(api_key='ato_...')
fuse.assess_architecture_pure(ato, source_text=..., module_name=...)
```

See per-tool docstrings for full arg schemas: `help(fuse.assess_architecture_pure)`

### Nexus [live]

`entitlement: nexus` &middot; `from atomadic import nexus`

> _The trust gate every action passes._

Gate-2 sovereign trust: trust phases, hallucination bound, signed attestations.

| Tool | Required args |
|---|---|
| **`assess_nexus_trust_phase_stateful`** | `ledger_path` |
| **`define_nexus_constants_pure`** | (none) |
| **`enforce_nexus_gate_stateful`** | `action_kind`, `severity` |
| **`record_nexus_attestation_stateful`** | `action_kind`, `severity`, `ledger_path` |
| **`record_nexus_escalation_stateful`** | `action_kind`, `escalation_path` |
| **`scan_nexus_attestation_history_stateful`** | `ledger_path` |

```python
from atomadic import Atomadic, nexus
ato = Atomadic(api_key='ato_...')
nexus.assess_nexus_trust_phase_stateful(ato, ledger_path=...)
```

See per-tool docstrings for full arg schemas: `help(nexus.assess_nexus_trust_phase_stateful)`

### Security [live]

`entitlement: security` &middot; `from atomadic import security`

> _A bubble of protection around every agent._

Bubble check, redaction, error-fold, hardening posture (PQC/FIPS-203).

| Tool | Required args |
|---|---|
| **`assess_security_bubble_pure`** | `content` |
| **`classify_error_fold_pure`** | `error_message` |
| **`compute_hardening_posture_pure`** | `target_product_id`, `hardening_level` |
| **`compute_redacted_args_pure`** | `args` |
| **`compute_redacted_text_pure`** | `text` |
| **`define_security_constants_pure`** | (none) |

```python
from atomadic import Atomadic, security
ato = Atomadic(api_key='ato_...')
security.assess_security_bubble_pure(ato, content=...)
```

See per-tool docstrings for full arg schemas: `help(security.assess_security_bubble_pure)`

### Proving Ground [live]

`entitlement: proving` &middot; `from atomadic import proving`

> _Nothing ships unproven._

Ship-gate, proof-readiness signals, and test-coverage estimation.

| Tool | Required args |
|---|---|
| **`assess_proof_readiness_pure`** | `source_text` |
| **`score_test_coverage_pure`** | `source_text`, `test_source` |

```python
from atomadic import Atomadic, proving
ato = Atomadic(api_key='ato_...')
proving.assess_proof_readiness_pure(ato, source_text=...)
```

See per-tool docstrings for full arg schemas: `help(proving.assess_proof_readiness_pure)`

### Release [live]

`entitlement: release` &middot; `from atomadic import release`

> _Template -> render -> deploy._

Template registry, website render, Cloudflare deploy. Dry-run by default.

| Tool | Required args |
|---|---|
| **`record_release_template_stateful`** | `template_id`, `kind`, `source_kind`, `source_ref`, `registry_path` |
| **`scan_release_templates_stateful`** | `registry_path` |

```python
from atomadic import Atomadic, release
ato = Atomadic(api_key='ato_...')
release.record_release_template_stateful(ato, template_id=..., kind=..., source_kind=...)
```

See per-tool docstrings for full arg schemas: `help(release.record_release_template_stateful)`

### Healer [beta]

`entitlement: healer` &middot; `from atomadic import healer`

> _Diagnose, grade, and plan the repair._

Read-only diagnosis: code-health grade + advisory repair plan.

| Tool | Required args |
|---|---|
| **`assess_artifact_health_pure`** | `source_text` |
| **`compute_repair_plan_pure`** | `error_message` |
| **`omega_repair_closure`** | `forge_root`, `target_root` |
| **`omega_repair_missing_imports`** | (none) |
| **`omega_scan_ast`** | (none) |
| **`omega_scan_missing_imports`** | (none) |
| **`omega_scan_mistier`** | (none) |
| **`omega_self_heal`** | (none) |
| **`omega_sweep_orphans`** | `src_root` |
| **`omega_verify_imports`** | (none) |

```python
from atomadic import Atomadic, healer
ato = Atomadic(api_key='ato_...')
healer.assess_artifact_health_pure(ato, source_text=...)
```

See per-tool docstrings for full arg schemas: `help(healer.assess_artifact_health_pure)`

### Evolve 

`entitlement: evolve` &middot; `from atomadic import evolve`

| Tool | Required args |
|---|---|
| **`omega_agent_games_register`** | `agent_id`, `ledger_path`, `display_name` |
| **`omega_agent_games_score`** | `agent_id`, `ledgers_dir` |
| **`omega_gratitude_imprint`** | `from_agent_id`, `to_agent_id`, `ledger_path`, `reason` |
| **`omega_pro_tip`** | `author_agent_id`, `ledger_path`, `title`, `body`, `topic` |
| **`omega_signal_boost`** | `author_agent_id`, `ledger_path`, `title` |
| **`omega_wisdom_flywheel`** | (none) |

```python
from atomadic import Atomadic, evolve
ato = Atomadic(api_key='ato_...')
evolve.omega_agent_games_register(ato, agent_id=..., ledger_path=..., display_name=...)
```

See per-tool docstrings for full arg schemas: `help(evolve.omega_agent_games_register)`

### Forge 

`entitlement: forge` &middot; `from atomadic import forge`

| Tool | Required args |
|---|---|
| **`omega_chain_autowire`** | `target_name`, `chain` |
| **`omega_context_packet`** | `query` |
| **`omega_emit_lang`** | `atom` |
| **`omega_emit_polyglot`** | `product`, `output_root` |
| **`omega_govern_actions`** | `additions` |
| **`omega_govern_scopes`** | `additions` |
| **`omega_harvest_permissive`** | `corpus_path` |
| **`omega_intent`** | `intent` |
| **`omega_intent_shippable`** | `intent` |
| **`omega_register_tool`** | `name`, `atom`, `tier`, `description` |
| **`omega_synthesize`** | `raw_name`, `source` |
| **`orchestrate_corpus_harvest_temporal`** | `corpus_path` |
| **`orchestrate_pipeline_truthstate_temporal`** | (none) |
| **`render_from_template_pure`** | `template`, `context` |
| **`render_website_stateful`** | `template_dir`, `context`, `output_dir` |

```python
from atomadic import Atomadic, forge
ato = Atomadic(api_key='ato_...')
forge.omega_chain_autowire(ato, target_name=..., chain=...)
```

See per-tool docstrings for full arg schemas: `help(forge.omega_chain_autowire)`

### Gateway 

`entitlement: gateway` &middot; `from atomadic import gateway`

| Tool | Required args |
|---|---|
| **`filter_entitled_tools_stateful`** | (none) |
| **`serve_cloudflare_pages_stateful`** | `directory`, `project_name` |
| **`serve_cloudflare_worker_stateful`** | `worker_dir` |

```python
from atomadic import Atomadic, gateway
ato = Atomadic(api_key='ato_...')
gateway.filter_entitled_tools_stateful(ato)
```

See per-tool docstrings for full arg schemas: `help(gateway.filter_entitled_tools_stateful)`

### Mind_Lab 

`entitlement: mind_lab` &middot; `from atomadic import mind_lab`

| Tool | Required args |
|---|---|
| **`omega_brainstorm`** | `topic`, `host`, `contributors` |
| **`omega_emergent_chains`** | (none) |

```python
from atomadic import Atomadic, mind_lab
ato = Atomadic(api_key='ato_...')
mind_lab.omega_brainstorm(ato, topic=..., host=..., contributors=...)
```

See per-tool docstrings for full arg schemas: `help(mind_lab.omega_brainstorm)`

## Two-gate dispatch

Every call is filtered then verified:

1. **Gate-1 (entitlement):** `tools/list` shows only the tools your plan unlocks; out-of-plan `tools/call` is refused.
2. **Gate-2 (trust, Nexus):** trust phase + severity ceiling + hallucination bound. Governed actions return a signed `attest:<id>` receipt.

See [the architecture docs](https://atomadic.tech/docs.html?d=two-gate) for the full model.

## Plans

Free / Basic / Dev / Pro / Teams / Enterprise -- per product, or whole-line via
Murmuration Complete. Subscription is the product; x402 meters only overage + agent-
to-agent calls. Pricing: https://atomadic.tech/docs.html?d=pricing.

## Determinism

Pure-tier tools have no side effects and no hidden state: same inputs, same output,
same content hash, every time. Re-running a pure tool is a verification.

## Contributing

This SDK is **auto-emitted from the live Atomadic MCP registry** -- changes here
should flow through the engine, not be hand-patched. For issues, requests, or
feedback: support@atomadic.tech.

## License

Apache-2.0 -- see [LICENSE](LICENSE).

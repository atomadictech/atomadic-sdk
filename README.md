<div align="center">

# Atomadic Python SDK

**One MCP. One key. Every tool-set you are entitled to.**

[![PyPI](https://img.shields.io/pypi/v/atomadic.svg)](https://pypi.org/project/atomadic/) [![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://pypi.org/project/atomadic/) [![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE) [![Docs](https://img.shields.io/badge/docs-atomadic.tech-7c3aed)](https://atomadic.tech/docs.html)

[Website](https://atomadic.tech) · [Docs](https://atomadic.tech/docs.html) · [Architecture](https://atomadic.tech/docs.html?d=architecture) · [Support](mailto:support@atomadic.tech)

</div>

---

Atomadic is sovereign infrastructure for the agent economy. You mount **one** MCP server at `mcp.atomadic.tech`, attach your **entitlement key**, and your client immediately sees the tool-sets your plan unlocks. Every call passes **Gate-1 (entitlement)** then **Gate-2 (trust)** before it runs. Pure-tier tools are deterministic — same inputs, same output, every time. Governed actions return a signed `attest:<id>` proof receipt you can audit.

This SDK is **auto-emitted from the live MCP registry**. When tools change, the package regenerates — every product module, every function signature, every docstring stays in lockstep with the live surface.

## Install

```bash
pip install atomadic
```

Python 3.9+. Zero runtime dependencies (the client uses stdlib `urllib`).

## Quickstart

```python
from atomadic import Atomadic, fuse

ato = Atomadic(api_key="ato_...")   # or: export ATOMADIC_KEY=ato_...

result = fuse.assess_architecture_pure(
    ato,
    source_text="def add(a, b):\n    return a + b",
    module_name="add_pure",
)
print(result["verdict"], result["density"])
# PASS 0.18
```

Browse the surface your key actually unlocks:

```python
for t in ato.list_tools():
    print(t["name"], "—", t["description"][:80])
```

## Authentication

Get an entitlement key from [atomadic.tech](https://atomadic.tech). The key (`ato_<blob>_<sig>`) is signed and **verified at the edge on every call** — no server-side lookup. Minting is internal-only.

```python
# Explicit:
ato = Atomadic(api_key="ato_<blob>_<sig>")

# Or via environment:
#   export ATOMADIC_KEY=ato_<blob>_<sig>
ato = Atomadic()
```

Keep keys server-side. The gate refuses out-of-plan calls, but secrets still belong in your environment, never in client code.

## Products & tool-sets

Each product is an entitlement-gated tool-set. Hold the entitlement, call the tool. The reserved products (Vanguard, Aegis, Catalyst) and roadmap products (Evolve, Research, Mind-Lab) are not yet part of the SDK.

| Product | Status | Entitlement | Module | Tools |
|---|---|---|---|---|
| **Murmuration** | live (all-access) | `murmuration_complete` | _(see all below)_ | 26 |
| **Fuse** | live | `fuse` | `atomadic.fuse` | 3 |
| **Nexus** | live | `nexus` | `atomadic.nexus` | 6 |
| **Security** | live | `security` | `atomadic.security` | 6 |
| **Proving** | live | `proving` | `atomadic.proving` | 3 |
| **Release** | live | `release` | `atomadic.release` | 6 |
| **Healer** | beta | `healer` | `atomadic.healer` | 2 |

### Fuse — architecture compiler

> _AI writes code. We give it architecture._

Analyze your source against the 5-tier, single-callable discipline. Pure and deterministic — nothing about your code leaves the call.

```python
from atomadic import Atomadic, fuse
ato = Atomadic()

fuse.assess_architecture_pure(ato, source_text=src, module_name="x_pure")
fuse.assess_import_direction_pure(ato, source_text=src, tier=3)
fuse.scan_code_stubs_pure(ato, source_text=src)
```

### Nexus — Gate-2 trust authority

> _The trust gate every action passes._

Resolve trust phase, enforce severity ceiling and the 0.95 hallucination bound, and emit signed, hash-chained attestations.

```python
from atomadic import Atomadic, nexus
ato = Atomadic()

nexus.enforce_nexus_gate_stateful(ato, action_kind="emit", severity="medium",
                                  attestation_count=12, recent_escalations=0,
                                  has_federated_key=False, entitlement_ok=True,
                                  bound_score=None, payload={"x": 1},
                                  ledger_path="./trust.jsonl")
```

### Security — the agent bubble

> _A bubble of protection around every agent._

Adversarial bubble-check (PROCEED / REVIEW / BLOCK), verify-without-reveal secret redaction, error-fold classification, cumulative hardening directives.

```python
from atomadic import Atomadic, security
ato = Atomadic()

security.assess_security_bubble_pure(ato, content="…", strict=False)
security.compute_redacted_text_pure(ato, text="token: sk-…")
security.compute_hardening_posture_pure(ato, target_product_id="fuse",
                                        hardening_level="high")
```

### Proving — the gauntlet

> _Nothing ships unproven._

Run the same ship-gate the platform uses against your code: judges logic density, single-callable, echo, imports, sovereignty, stubs.

```python
from atomadic import Atomadic, proving
ato = Atomadic()

proving.validate_logic_block_composite(ato, source_text=src, module_name="x_pure")
proving.assess_proof_readiness_pure(ato, source_text=src)
proving.score_test_coverage_pure(ato, source_text=src, test_source=tests)
```

### Release — template → render → deploy

> _Bring our templates, or your own._

Register and render templates, then deploy to Cloudflare. Dry-run by default; live deploys require explicit `operator_authorized=True`.

```python
from atomadic import Atomadic, release
ato = Atomadic()

release.record_release_template_stateful(ato, template_id="site.v1",
                                         kind="website", source_kind="path",
                                         source_ref="./site",
                                         registry_path="./reg.jsonl")
release.render_website_stateful(ato, template_dir="./site",
                                context={"title": "Acme"}, output_dir="./out")
release.serve_cloudflare_pages_stateful(ato, directory="./out",
                                        project_name="acme-site")
```

### Healer — diagnosis & repair plans _(beta)_

> _Diagnose, grade, and plan the repair._

Read-only diagnosis: an A–F health grade for a code artifact, and a step-by-step advisory repair plan from its error.

```python
from atomadic import Atomadic, healer
ato = Atomadic()

healer.assess_artifact_health_pure(ato, source_text=src, module_name="x_pure")
healer.compute_repair_plan_pure(ato, error_message="ModuleNotFoundError: …",
                                source_text=src)
```

## The two-gate dispatch

Every call is filtered then verified:

```
   call → [ Gate 1: Entitlement ] → [ Gate 2: Trust ] → tool → result + receipt
            commercial rights         sovereign integrity
            (Murmuration)             (Nexus / Aletheia)
```

- **Gate-1** filters `tools/list` to your plan and refuses out-of-plan `tools/call`. Internal tools never surface at any tier.
- **Gate-2** checks trust phase + severity + hallucination bound, and emits a signed attestation on PASS. Refusals return a typed code (`MISSING_ENTITLEMENT`, `INSUFFICIENT_TRUST_PHASE`, `HALLUCINATION_BOUND_VIOLATED`, `SCHEMA_VALIDATION_FAILED`, `ESCALATION_REQUIRED`) — never silent.

Full model: <https://atomadic.tech/docs.html?d=two-gate>.

## Plans

One ladder, per product or whole-line via Murmuration Complete:

**Free** · **Basic** · **Dev** · **Pro** · **Teams** · **Enterprise**

Cards (Stripe) for subscriptions; x402 / USDC meters only overage above plan and agent-to-agent calls; invoice for Enterprise. Subscription is the product; x402 is the meter, not the product. Pricing is being finalized — see <https://atomadic.tech/docs.html?d=pricing>.

## Determinism

Pure-tier tools have no side effects and no hidden state: the same inputs produce the same output and the same content hash, every time, on any machine. Re-running a pure tool is a verification, not a gamble.

Effectful tools (deploys, ledger writes, network) are isolated to where they are contracted and are explicit about it. External-IO release tools dry-run by default and require explicit operator authorization to go live.

## API surface

The SDK is a thin, faithful wrapper:

- `atomadic.Atomadic(api_key=None, url=None)` — client. Reads `ATOMADIC_KEY` and `ATOMADIC_MCP_URL` from env if not passed.
- `Atomadic.call(tool, arguments=None)` — raw `tools/call`. Parses the JSON-text content automatically.
- `Atomadic.list_tools()` — `tools/list`, filtered to your entitlement.
- `atomadic.<product>.<tool>(client, …)` — typed wrapper for every public tool, with arg schemas in the docstrings.

```python
help(atomadic.fuse.assess_architecture_pure)
```

## How this SDK is built

This package is **auto-emitted from the live MCP tool registry** by an engine atom (`build_atomadic_sdk_stateful`). Patching this repo by hand is the wrong layer — module bodies, function signatures, and docstrings are generated. To change behavior, change the tool contract upstream and re-emit.

For issues, feedback, or partner / sovereign / on-prem inquiries: **support@atomadic.tech**.

## License

Apache-2.0 — see [LICENSE](LICENSE).

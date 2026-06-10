# Mind-Lab -- SDK reference

> Entitlement `mind_lab` - 5 tools - one MCP at `mcp.atomadic.tech`

```python
from atomadic import Atomadic, mind_lab
ato = Atomadic(api_key='ato_...')
```

## `assess_falsifiability_pure`

**In plain English** - Checks and scores falsifiability.

**Technical** - Score how falsifiable a claim is (measurable predicate, scope, quantifier vs hedges) â†’ 0-1 score, grade, how to falsify. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `claim` | string | yes |  |

```python
mind_lab.assess_falsifiability_pure(ato, claim=...)
```

## `assess_proposal_verdict_pure`

**In plain English** - Checks and scores proposal verdict.

**Technical** - Multi-layer pre-emission verdict on a proposal (admission, specificity, testability, risk, adversarial dissent) â†’ admit / revise / reject with per-layer notes. Pure, deterministic, advisory. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `proposal_text` | string | yes |  |
| `source_text` | string | no |  |

```python
mind_lab.assess_proposal_verdict_pure(ato, proposal_text=...)
```

## `classify_cognitive_bias_pure`

**In plain English** - Sorts into categories cognitive bias.

**Technical** - Scan reasoning for cognitive-bias signals (confirmation/anchoring/survivorship/sunk-cost/bandwagon/overconfidence/recency) + debiasing prompts. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `reasoning_text` | string | yes |  |

```python
mind_lab.classify_cognitive_bias_pure(ato, reasoning_text=...)
```

## `compose_adversarial_critique_pure`

**In plain English** - Builds adversarial critique.

**Technical** - Structured adversarial critique of a proposal: load-bearing assumption, strongest counter-case, failure modes, disconfirming evidence, steelman-opposite. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `proposal` | string | yes |  |

```python
mind_lab.compose_adversarial_critique_pure(ato, proposal=...)
```

## `score_idea_readiness_pure`

**In plain English** - Scores idea readiness.

**Technical** - Score an idea's readiness-to-emit (clarity/specificity/feasibility/risk-awareness) â†’ 0-1 readiness + ship/refine/rethink. _(plan: pro)_

| arg | type | required | description |
|---|---|---|---|
| `idea_text` | string | yes |  |

```python
mind_lab.score_idea_readiness_pure(ato, idea_text=...)
```

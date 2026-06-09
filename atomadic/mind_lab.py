"""atomadic.mind_lab -- Mind_Lab.




Entitlement: mind_lab (Gate-1 unlocks these tools).
Status: live.
Auto-emitted from the live MCP registry.
"""

def assess_falsifiability_pure(client, claim, **kwargs):
    """[Mind-Lab product Â· entitlement: mind_lab] Score how falsifiable a claim is (measurable predicate, scope, quantifier vs hedges) â†’ 0-1 score, grade, how to falsify.

    Args:
        claim (string, required): see MCP schema

    Example:
        from atomadic import Atomadic, mind_lab
        ato = Atomadic(api_key='ato_...')
        result = mind_lab.assess_falsifiability_pure(ato, claim=...)
    """
    args = {'claim': claim}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('assess_falsifiability_pure', args)

def assess_proposal_verdict_pure(client, proposal_text, source_text=None, **kwargs):
    """[Mind-Lab product Â· entitlement: mind_lab] Multi-layer pre-emission verdict on a proposal (admission, specificity, testability, risk, adversarial dissent) â†’ admit / revise / reject with per-layer notes. Pure, deterministic, advisory.

    Args:
        proposal_text (string, required): see MCP schema
        source_text (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, mind_lab
        ato = Atomadic(api_key='ato_...')
        result = mind_lab.assess_proposal_verdict_pure(ato, proposal_text=...)
    """
    args = {'proposal_text': proposal_text, 'source_text': source_text}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('assess_proposal_verdict_pure', args)

def compose_adversarial_critique_pure(client, proposal, **kwargs):
    """[Mind-Lab product Â· entitlement: mind_lab] Structured adversarial critique of a proposal: load-bearing assumption, strongest counter-case, failure modes, disconfirming evidence, steelman-opposite.

    Args:
        proposal (string, required): see MCP schema

    Example:
        from atomadic import Atomadic, mind_lab
        ato = Atomadic(api_key='ato_...')
        result = mind_lab.compose_adversarial_critique_pure(ato, proposal=...)
    """
    args = {'proposal': proposal}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compose_adversarial_critique_pure', args)

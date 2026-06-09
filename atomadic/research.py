"""atomadic.research -- Research.




Entitlement: research (Gate-1 unlocks these tools).
Status: live.
Auto-emitted from the live MCP registry.
"""

def compose_research_panel_pure(client, question, context=None, **kwargs):
    """[Research product Â· entitlement: research] Turn an open question into a structured cross-domain research scaffold: per-lens (correctness/performance/security/usability/data/cost) testable hypotheses, the evidence that would confirm each, and a falsifier, plus a synthesis. Pure, deterministic.

    Args:
        question (string, required): see MCP schema
        context (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, research
        ato = Atomadic(api_key='ato_...')
        result = research.compose_research_panel_pure(ato, question=...)
    """
    args = {'question': question, 'context': context}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compose_research_panel_pure', args)

"""atomadic.evolve -- Evolve.




Entitlement: evolve (Gate-1 unlocks these tools).
Status: live.
Auto-emitted from the live MCP registry.
"""

def assess_improvement_candidates_pure(client, source_text, module_name, **kwargs):
    """[Evolve product Â· entitlement: evolve] Propose bounded, simulated improvement candidates for your source â€” missing docstrings/type-hints/guards, bare excepts, stub signals â€” each risk-graded with a simulated gain and a promotion verdict. Read-only/advisory; operates only on the source you provide.

    Args:
        source_text (string, required): see MCP schema
        module_name (string, required): see MCP schema

    Example:
        from atomadic import Atomadic, evolve
        ato = Atomadic(api_key='ato_...')
        result = evolve.assess_improvement_candidates_pure(ato, source_text=..., module_name=...)
    """
    args = {'source_text': source_text, 'module_name': module_name}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('assess_improvement_candidates_pure', args)

def assess_regression_risk_pure(client, source_text, change_summary=None, **kwargs):
    """[Evolve product Â· entitlement: evolve] Assess regression risk of a change: public symbols in scope, control-flow complexity, I/O/side-effects, risk keywords â†’ low/medium/high tier + drivers.

    Args:
        source_text (string, required): see MCP schema
        change_summary (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, evolve
        ato = Atomadic(api_key='ato_...')
        result = evolve.assess_regression_risk_pure(ato, source_text=...)
    """
    args = {'source_text': source_text, 'change_summary': change_summary}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('assess_regression_risk_pure', args)

def score_evolution_fitness_pure(client, before_source, after_source, **kwargs):
    """[Evolve product Â· entitlement: evolve] Compare a before/after source pair on fitness dimensions (parse health, functions, docs, LOC, stubs) â†’ per-dimension deltas + improved/neutral/regressed verdict.

    Args:
        before_source (string, required): see MCP schema
        after_source (string, required): see MCP schema

    Example:
        from atomadic import Atomadic, evolve
        ato = Atomadic(api_key='ato_...')
        result = evolve.score_evolution_fitness_pure(ato, before_source=..., after_source=...)
    """
    args = {'before_source': before_source, 'after_source': after_source}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('score_evolution_fitness_pure', args)

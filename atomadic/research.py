"""atomadic.research -- Research.




Entitlement: research (Gate-1 unlocks these tools).
Status: live.
Auto-emitted from the live MCP registry.
"""

def compose_experiment_design_pure(client, hypothesis, **kwargs):
    """[Research product Â· entitlement: research] Turn a hypothesis into an experiment design: variables, method, control, sample, success criterion, threats to validity, falsifier.

    Args:
        hypothesis (string, required): see MCP schema

    Example:
        from atomadic import Atomadic, research
        ato = Atomadic(api_key='ato_...')
        result = research.compose_experiment_design_pure(ato, hypothesis=...)
    """
    args = {'hypothesis': hypothesis}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compose_experiment_design_pure', args)

def compose_literature_query_pure(client, topic, **kwargs):
    """[Research product Â· entitlement: research] Turn a topic into structured search queries across angles + source types to weight. Composes queries; fetches nothing.

    Args:
        topic (string, required): see MCP schema

    Example:
        from atomadic import Atomadic, research
        ato = Atomadic(api_key='ato_...')
        result = research.compose_literature_query_pure(ato, topic=...)
    """
    args = {'topic': topic}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compose_literature_query_pure', args)

def compose_problem_decomposition_pure(client, problem, **kwargs):
    """[Research product Â· entitlement: research] Decompose an open problem into dependency-ordered sub-problems (defineâ†’constraintsâ†’exploreâ†’designâ†’buildâ†’verify) + critical path.

    Args:
        problem (string, required): see MCP schema

    Example:
        from atomadic import Atomadic, research
        ato = Atomadic(api_key='ato_...')
        result = research.compose_problem_decomposition_pure(ato, problem=...)
    """
    args = {'problem': problem}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compose_problem_decomposition_pure', args)

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

def rank_hypotheses_pure(client, hypotheses, **kwargs):
    """[Research product Â· entitlement: research] Rank hypotheses by priority = impact Ã— tractability Ã· (uncertainty+1) â†’ ordered list.

    Args:
        hypotheses (array, required): see MCP schema

    Example:
        from atomadic import Atomadic, research
        ato = Atomadic(api_key='ato_...')
        result = research.rank_hypotheses_pure(ato, hypotheses=...)
    """
    args = {'hypotheses': hypotheses}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('rank_hypotheses_pure', args)

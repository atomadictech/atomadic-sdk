"""atomadic.proving -- Proving Ground.

Nothing ships unproven.
Ship-gate, proof-readiness signals, and test-coverage estimation.

Entitlement: proving (Gate-1 unlocks these tools).
Status: live.
Auto-emitted from the live MCP registry.
"""

def assess_proof_readiness_pure(client, source_text, **kwargs):
    """[Proving product Â· entitlement: proving] Assess ship/proof-readiness of provided source: docstring, returns-value, guards/asserts, type-hints, stub-free â†’ score + ready verdict.

    Args:
        source_text (string, required): see MCP schema

    Example:
        from atomadic import Atomadic, proving
        ato = Atomadic(api_key='ato_...')
        result = proving.assess_proof_readiness_pure(ato, source_text=...)
    """
    args = {'source_text': source_text}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('assess_proof_readiness_pure', args)

def assess_test_quality_pure(client, test_source, **kwargs):
    """[Proving product Â· entitlement: proving] Assess test-suite quality: test count, assertions, edge-case + error-path coverage, mocks/fixtures, parametrization â†’ 0-1 quality score + findings.

    Args:
        test_source (string, required): see MCP schema

    Example:
        from atomadic import Atomadic, proving
        ato = Atomadic(api_key='ato_...')
        result = proving.assess_test_quality_pure(ato, test_source=...)
    """
    args = {'test_source': test_source}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('assess_test_quality_pure', args)

def compute_proof_obligations_pure(client, source_text, **kwargs):
    """[Proving product Â· entitlement: proving] Extract per-function proof obligations: preconditions, return paths, error contracts, and a plain-language obligation statement.

    Args:
        source_text (string, required): see MCP schema

    Example:
        from atomadic import Atomadic, proving
        ato = Atomadic(api_key='ato_...')
        result = proving.compute_proof_obligations_pure(ato, source_text=...)
    """
    args = {'source_text': source_text}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compute_proof_obligations_pure', args)

def score_documentation_coverage_pure(client, source_text, **kwargs):
    """[Proving product Â· entitlement: proving] Score docstring coverage (module + every function/class) â†’ documented fraction, undocumented names, good/partial/poor verdict.

    Args:
        source_text (string, required): see MCP schema

    Example:
        from atomadic import Atomadic, proving
        ato = Atomadic(api_key='ato_...')
        result = proving.score_documentation_coverage_pure(ato, source_text=...)
    """
    args = {'source_text': source_text}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('score_documentation_coverage_pure', args)

def score_test_coverage_pure(client, source_text, test_source, **kwargs):
    """[Proving product Â· entitlement: proving] Estimate test coverage: which top-level functions in the source are referenced by the test source; returns covered/uncovered + coverage ratio.

    Args:
        source_text (string, required): see MCP schema
        test_source (string, required): see MCP schema

    Example:
        from atomadic import Atomadic, proving
        ato = Atomadic(api_key='ato_...')
        result = proving.score_test_coverage_pure(ato, source_text=..., test_source=...)
    """
    args = {'source_text': source_text, 'test_source': test_source}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('score_test_coverage_pure', args)

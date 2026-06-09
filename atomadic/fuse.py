"""atomadic.fuse -- Fuse.

Architecture compiler -- AI writes code, we give it architecture.
Analyze your code against the 5-tier, single-callable discipline.

Entitlement: fuse (Gate-1 unlocks these tools).
Status: live.
Auto-emitted from the live MCP registry.
"""

def assess_architecture_pure(client, source_text, module_name, **kwargs):
    """[Fuse product Â· entitlement: fuse] Analyze a provided Python source's architecture vs the Atomadic 5-tier / single-callable discipline: callables, single-callable, imports + tier directions, logic density, tier hint, findings, verdict. Operates only on the provided source.

    Args:
        source_text (string, required): see MCP schema
        module_name (string, required): see MCP schema

    Example:
        from atomadic import Atomadic, fuse
        ato = Atomadic(api_key='ato_...')
        result = fuse.assess_architecture_pure(ato, source_text=..., module_name=...)
    """
    args = {'source_text': source_text, 'module_name': module_name}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('assess_architecture_pure', args)

def assess_import_direction_pure(client, source_text, tier, **kwargs):
    """[Fuse product Â· entitlement: fuse] Tier-law check: verify a source's atomadic imports respect the 5-tier downward-only law (tier-N imports tier-&lt;N only); reports same-tier and upward violations.

    Args:
        source_text (string, required): see MCP schema
        tier (integer, required): see MCP schema

    Example:
        from atomadic import Atomadic, fuse
        ato = Atomadic(api_key='ato_...')
        result = fuse.assess_import_direction_pure(ato, source_text=..., tier=...)
    """
    args = {'source_text': source_text, 'tier': tier}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('assess_import_direction_pure', args)

def orchestrate_s2s_temporal(client, intent, target_source=None, dry_run=None, **kwargs):
    """[Fuse product Â· entitlement: fuse] Spaghetti-to-shippable: turn a single repo + an intent into a gated, shippable product package. Public profile is BOUNDED â€” single-repo harvest, tier-5-max emission, redaction (enforce_public_s2s_constraints). Dry-run by default.

    Args:
        intent (string, required): What to build from the source
        target_source (string, optional): Path/ref to the single source repo to transform
        dry_run (boolean, optional): Plan only (default true)

    Example:
        from atomadic import Atomadic, fuse
        ato = Atomadic(api_key='ato_...')
        result = fuse.orchestrate_s2s_temporal(ato, intent=...)
    """
    args = {'intent': intent, 'target_source': target_source, 'dry_run': dry_run}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('orchestrate_s2s_temporal', args)

def scan_code_stubs_pure(client, source_text, **kwargs):
    """[Fuse product Â· entitlement: fuse] Stub-hunter: scan provided source for stub/scaffold/placeholder patterns (NotImplementedError, TODO/FIXME, ellipsis/pass-only bodies, empty-shell returns). Returns REAL or STUB + findings.

    Args:
        source_text (string, required): see MCP schema

    Example:
        from atomadic import Atomadic, fuse
        ato = Atomadic(api_key='ato_...')
        result = fuse.scan_code_stubs_pure(ato, source_text=...)
    """
    args = {'source_text': source_text}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('scan_code_stubs_pure', args)

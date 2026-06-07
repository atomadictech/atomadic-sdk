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

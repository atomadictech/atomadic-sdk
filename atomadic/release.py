"""atomadic.release -- Release.

Template -> render -> deploy.
Template registry, website render, Cloudflare deploy. Dry-run by default.

Entitlement: release (Gate-1 unlocks these tools).
Status: live.
Auto-emitted from the live MCP registry.
"""

def record_release_template_stateful(client, template_id, kind, source_kind, source_ref, registry_path, brand=None, tokens=None, **kwargs):
    """[Release product Â· entitlement: release] Register a release template (ours or customer BYO) into the template registry ledger.

    Args:
        template_id (string, required): see MCP schema
        kind (string, required): see MCP schema
        source_kind (string, required): see MCP schema
        source_ref (string, required): see MCP schema
        registry_path (string, required): see MCP schema
        brand (object, optional): see MCP schema
        tokens (array, optional): see MCP schema

    Example:
        from atomadic import Atomadic, release
        ato = Atomadic(api_key='ato_...')
        result = release.record_release_template_stateful(ato, template_id=..., kind=..., source_kind=...)
    """
    args = {'template_id': template_id, 'kind': kind, 'source_kind': source_kind, 'source_ref': source_ref, 'registry_path': registry_path, 'brand': brand, 'tokens': tokens}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('record_release_template_stateful', args)

def scan_release_templates_stateful(client, registry_path, kind=None, **kwargs):
    """[Release product Â· entitlement: release] List registered release templates (latest per id), optional kind filter.

    Args:
        registry_path (string, required): see MCP schema
        kind (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, release
        ato = Atomadic(api_key='ato_...')
        result = release.scan_release_templates_stateful(ato, registry_path=...)
    """
    args = {'registry_path': registry_path, 'kind': kind}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('scan_release_templates_stateful', args)

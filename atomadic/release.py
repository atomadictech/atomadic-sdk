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

def render_from_template_pure(client, template, context, missing=None, **kwargs):
    """[Release product Â· entitlement: release] Deterministically render a {{token}} text template from a context mapping. Ours or customer templates, one code path.

    Args:
        template (string, required): see MCP schema
        context (object, required): see MCP schema
        missing (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, release
        ato = Atomadic(api_key='ato_...')
        result = release.render_from_template_pure(ato, template=..., context=...)
    """
    args = {'template': template, 'context': context, 'missing': missing}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('render_from_template_pure', args)

def render_website_stateful(client, template_dir, context, output_dir, include_ext=None, **kwargs):
    """[Release product Â· entitlement: release] Render a static website from a template directory (ours or customer's) into an output dir; {{token}} substitution + assets. Ready for Cloudflare Pages.

    Args:
        template_dir (string, required): see MCP schema
        context (object, required): see MCP schema
        output_dir (string, required): see MCP schema
        include_ext (array, optional): see MCP schema

    Example:
        from atomadic import Atomadic, release
        ato = Atomadic(api_key='ato_...')
        result = release.render_website_stateful(ato, template_dir=..., context=..., output_dir=...)
    """
    args = {'template_dir': template_dir, 'context': context, 'output_dir': output_dir, 'include_ext': include_ext}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('render_website_stateful', args)

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

def serve_cloudflare_pages_stateful(client, directory, project_name, branch=None, operator_authorized=None, vault_path=None, **kwargs):
    """[Release product Â· entitlement: release] Deploy a built site to Cloudflare Pages via wrangler. Dry-run by default; live ONLY with operator_authorized=true.

    Args:
        directory (string, required): see MCP schema
        project_name (string, required): see MCP schema
        branch (string, optional): see MCP schema
        operator_authorized (boolean, optional): see MCP schema
        vault_path (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, release
        ato = Atomadic(api_key='ato_...')
        result = release.serve_cloudflare_pages_stateful(ato, directory=..., project_name=...)
    """
    args = {'directory': directory, 'project_name': project_name, 'branch': branch, 'operator_authorized': operator_authorized, 'vault_path': vault_path}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('serve_cloudflare_pages_stateful', args)

def serve_cloudflare_worker_stateful(client, worker_dir, operator_authorized=None, vault_path=None, worker_name=None, **kwargs):
    """[Release product Â· entitlement: release] Deploy a Cloudflare Worker (e.g. the MCP edge) via wrangler. Dry-run by default; live ONLY with operator_authorized=true.

    Args:
        worker_dir (string, required): see MCP schema
        operator_authorized (boolean, optional): see MCP schema
        vault_path (string, optional): see MCP schema
        worker_name (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, release
        ato = Atomadic(api_key='ato_...')
        result = release.serve_cloudflare_worker_stateful(ato, worker_dir=...)
    """
    args = {'worker_dir': worker_dir, 'operator_authorized': operator_authorized, 'vault_path': vault_path, 'worker_name': worker_name}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('serve_cloudflare_worker_stateful', args)

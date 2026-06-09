"""atomadic.gateway -- Gateway.




Entitlement: gateway (Gate-1 unlocks these tools).
Status: live.
Auto-emitted from the live MCP registry.
"""

def filter_entitled_tools_stateful(client, entitlements=None, index_path=None, **kwargs):
    """Gate public MCP tools by Atomadic package entitlements using the complete product tool entitlement index plus canonical Gift/Bomb plan resolver.

    Args:
        entitlements (any, optional): see MCP schema
        index_path (any, optional): see MCP schema

    Example:
        from atomadic import Atomadic, gateway
        ato = Atomadic(api_key='ato_...')
        result = gateway.filter_entitled_tools_stateful(ato)
    """
    args = {'entitlements': entitlements, 'index_path': index_path}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('filter_entitled_tools_stateful', args)

def serve_cloudflare_pages_stateful(client, directory, project_name, branch=None, operator_authorized=None, vault_path=None, **kwargs):
    """[Release product Â· entitlement: release] Deploy a built site to Cloudflare Pages via wrangler. Dry-run by default; live ONLY with operator_authorized=true.

    Args:
        directory (string, required): see MCP schema
        project_name (string, required): see MCP schema
        branch (string, optional): see MCP schema
        operator_authorized (boolean, optional): see MCP schema
        vault_path (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, gateway
        ato = Atomadic(api_key='ato_...')
        result = gateway.serve_cloudflare_pages_stateful(ato, directory=..., project_name=...)
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
        from atomadic import Atomadic, gateway
        ato = Atomadic(api_key='ato_...')
        result = gateway.serve_cloudflare_worker_stateful(ato, worker_dir=...)
    """
    args = {'worker_dir': worker_dir, 'operator_authorized': operator_authorized, 'vault_path': vault_path, 'worker_name': worker_name}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('serve_cloudflare_worker_stateful', args)

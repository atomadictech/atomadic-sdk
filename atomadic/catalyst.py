"""atomadic.catalyst -- Catalyst.




Entitlement: catalyst (Gate-1 unlocks these tools).
Status: live.
Auto-emitted from the live MCP registry.
"""

def compose_paywall_policy_pure(client, resource, price_usd, currency=None, **kwargs):
    """[Catalyst product Â· entitlement: catalyst] Compose an HTTP 402 paywall policy (x402 challenge spec) for a resource.

    Args:
        resource (string, required): see MCP schema
        price_usd (number, required): see MCP schema
        currency (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, catalyst
        ato = Atomadic(api_key='ato_...')
        result = catalyst.compose_paywall_policy_pure(ato, resource=..., price_usd=...)
    """
    args = {'resource': resource, 'price_usd': price_usd, 'currency': currency}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compose_paywall_policy_pure', args)

def compute_settlement_split_pure(client, amount, splits, **kwargs):
    """[Catalyst product Â· entitlement: catalyst] Split a payment across parties by basis points (sum 10000) with exact largest-remainder cent rounding.

    Args:
        amount (number, required): see MCP schema
        splits (array, required): see MCP schema

    Example:
        from atomadic import Atomadic, catalyst
        ato = Atomadic(api_key='ato_...')
        result = catalyst.compute_settlement_split_pure(ato, amount=..., splits=...)
    """
    args = {'amount': amount, 'splits': splits}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compute_settlement_split_pure', args)

def compute_usage_meter_pure(client, events, rate_per_unit, **kwargs):
    """[Catalyst product Â· entitlement: catalyst] Aggregate usage events into a billable total at a per-unit rate, with per-sku breakdown.

    Args:
        events (array, required): see MCP schema
        rate_per_unit (number, required): see MCP schema

    Example:
        from atomadic import Atomadic, catalyst
        ato = Atomadic(api_key='ato_...')
        result = catalyst.compute_usage_meter_pure(ato, events=..., rate_per_unit=...)
    """
    args = {'events': events, 'rate_per_unit': rate_per_unit}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compute_usage_meter_pure', args)

def compute_x402_quote_pure(client, units, rate_per_unit, included_units=None, **kwargs):
    """[Catalyst product Â· entitlement: catalyst] Compute an x402 metered quote â€” bill overage above plan-included units.

    Args:
        units (number, required): see MCP schema
        rate_per_unit (number, required): see MCP schema
        included_units (number, optional): see MCP schema

    Example:
        from atomadic import Atomadic, catalyst
        ato = Atomadic(api_key='ato_...')
        result = catalyst.compute_x402_quote_pure(ato, units=..., rate_per_unit=...)
    """
    args = {'units': units, 'rate_per_unit': rate_per_unit, 'included_units': included_units}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compute_x402_quote_pure', args)

def validate_quota_tree_pure(client, tree, **kwargs):
    """[Catalyst product Â· entitlement: catalyst] Validate a hierarchical quota tree (children sum â‰¤ parent limit, no negatives) â†’ valid + violations.

    Args:
        tree (object, required): see MCP schema

    Example:
        from atomadic import Atomadic, catalyst
        ato = Atomadic(api_key='ato_...')
        result = catalyst.validate_quota_tree_pure(ato, tree=...)
    """
    args = {'tree': tree}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('validate_quota_tree_pure', args)

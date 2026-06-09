"""atomadic.vanguard -- Vanguard.




Entitlement: vanguard (Gate-1 unlocks these tools).
Status: live.
Auto-emitted from the live MCP registry.
"""

def assess_mev_exposure_pure(client, order, **kwargs):
    """[Vanguard product Â· entitlement: vanguard] Heuristic MEV-exposure assessment of an order (size/public mempool/slippage) â†’ exposure tier + mitigations.

    Args:
        order (object, required): see MCP schema

    Example:
        from atomadic import Atomadic, vanguard
        ato = Atomadic(api_key='ato_...')
        result = vanguard.assess_mev_exposure_pure(ato, order=...)
    """
    args = {'order': order}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('assess_mev_exposure_pure', args)

def assess_transaction_risk_pure(client, transaction, **kwargs):
    """[Vanguard product Â· entitlement: vanguard] Risk-score a proposed transaction (amount/recipient/contract/slippage) â†’ 0-1 risk + tier + hold/allow. Analysis only, no execution.

    Args:
        transaction (object, required): see MCP schema

    Example:
        from atomadic import Atomadic, vanguard
        ato = Atomadic(api_key='ato_...')
        result = vanguard.assess_transaction_risk_pure(ato, transaction=...)
    """
    args = {'transaction': transaction}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('assess_transaction_risk_pure', args)

def compose_settlement_terms_pure(client, amount_usd, parties, release_condition=None, **kwargs):
    """[Vanguard product Â· entitlement: vanguard] Compose advisory escrow/settlement terms for an A2A deal (release/refund conditions, dispute window). No funds move.

    Args:
        amount_usd (number, required): see MCP schema
        parties (array, required): see MCP schema
        release_condition (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, vanguard
        ato = Atomadic(api_key='ato_...')
        result = vanguard.compose_settlement_terms_pure(ato, amount_usd=..., parties=...)
    """
    args = {'amount_usd': amount_usd, 'parties': parties, 'release_condition': release_condition}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compose_settlement_terms_pure', args)

def compute_slippage_guard_pure(client, expected_out, tolerance_bps=None, **kwargs):
    """[Vanguard product Â· entitlement: vanguard] Compute the minimum acceptable output (slippage guard) for a swap from expected out + tolerance bps.

    Args:
        expected_out (number, required): see MCP schema
        tolerance_bps (number, optional): see MCP schema

    Example:
        from atomadic import Atomadic, vanguard
        ato = Atomadic(api_key='ato_...')
        result = vanguard.compute_slippage_guard_pure(ato, expected_out=...)
    """
    args = {'expected_out': expected_out, 'tolerance_bps': tolerance_bps}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compute_slippage_guard_pure', args)

def validate_spend_policy_pure(client, transaction, budget, **kwargs):
    """[Vanguard product Â· entitlement: vanguard] Validate a transaction against a bounded spend policy (per_tx_max/daily_max/allowlist) â†’ allow/deny + remaining budget.

    Args:
        transaction (object, required): see MCP schema
        budget (object, required): see MCP schema

    Example:
        from atomadic import Atomadic, vanguard
        ato = Atomadic(api_key='ato_...')
        result = vanguard.validate_spend_policy_pure(ato, transaction=..., budget=...)
    """
    args = {'transaction': transaction, 'budget': budget}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('validate_spend_policy_pure', args)

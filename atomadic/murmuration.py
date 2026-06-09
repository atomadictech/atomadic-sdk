"""atomadic.murmuration -- Murmuration.

The whole lattice in one entitlement.
Umbrella entitlement: every public product's tool-set under one key.

Entitlement: murmuration (Gate-1 unlocks these tools).
Status: live.
Auto-emitted from the live MCP registry.
"""

def omega_agent_heartbeat(client, agent_id, ledger_path, current_intent=None, lane=None, performance_card=None, phase=None, product_identity=None, **kwargs):
    """Register a Murmuration agent heartbeat (swarm presence) - hash-chain appends an agent_heartbeat.v1 record to ledger_path. Returns {ok, agent_id, ts, chain_hash}.

    Args:
        agent_id (string, required): see MCP schema
        ledger_path (string, required): see MCP schema
        current_intent (string, optional): see MCP schema
        lane (string, optional): see MCP schema
        performance_card (string, optional): see MCP schema
        phase (string, optional): see MCP schema
        product_identity (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, murmuration
        ato = Atomadic(api_key='ato_...')
        result = murmuration.omega_agent_heartbeat(ato, agent_id=..., ledger_path=...)
    """
    args = {'agent_id': agent_id, 'ledger_path': ledger_path, 'current_intent': current_intent, 'lane': lane, 'performance_card': performance_card, 'phase': phase, 'product_identity': product_identity}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_agent_heartbeat', args)

def omega_attention_marker(client, agent_id, ledger_path, focus, intent_summary=None, ttl_seconds=None, **kwargs):
    """Stake a Murmuration attention marker ('working here, give space') with a TTL - hash-chain appends an attention_marker.v1 record. ttl clamped [60,14400]. Returns {ok, marker_id, expires_at, chain_hash}.

    Args:
        agent_id (string, required): see MCP schema
        ledger_path (string, required): see MCP schema
        focus (object, required): see MCP schema
        intent_summary (string, optional): see MCP schema
        ttl_seconds (integer, optional): see MCP schema

    Example:
        from atomadic import Atomadic, murmuration
        ato = Atomadic(api_key='ato_...')
        result = murmuration.omega_attention_marker(ato, agent_id=..., ledger_path=..., focus=...)
    """
    args = {'agent_id': agent_id, 'ledger_path': ledger_path, 'focus': focus, 'intent_summary': intent_summary, 'ttl_seconds': ttl_seconds}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_attention_marker', args)

def omega_handoff_capsule(client, from_agent_id, ledger_path, next_step, blocked=None, done=None, lane=None, open_questions=None, to_agent_id=None, **kwargs):
    """Post a Murmuration handoff capsule (done/next/blocked/open-questions) - hash-chain appends a handoff_capsule.v1 record. Returns {ok, capsule_id, chain_hash}.

    Args:
        from_agent_id (string, required): see MCP schema
        ledger_path (string, required): see MCP schema
        next_step (string, required): see MCP schema
        blocked (string, optional): see MCP schema
        done (string, optional): see MCP schema
        lane (string, optional): see MCP schema
        open_questions (array, optional): see MCP schema
        to_agent_id (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, murmuration
        ato = Atomadic(api_key='ato_...')
        result = murmuration.omega_handoff_capsule(ato, from_agent_id=..., ledger_path=..., next_step=...)
    """
    args = {'from_agent_id': from_agent_id, 'ledger_path': ledger_path, 'next_step': next_step, 'blocked': blocked, 'done': done, 'lane': lane, 'open_questions': open_questions, 'to_agent_id': to_agent_id}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_handoff_capsule', args)

def omega_lane(client, lane=None, **kwargs):
    """Curate the registered tool surface into six user-facing lanes (murmuration lane aligned): recon (look), governance (decide/attest), emit (make), hive (swarm coherence), intent (find a tool), other. Pass `lane` for that bucket's tools; omit for an all-lanes summary. registry_path engine-bound.

    Args:
        lane (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, murmuration
        ato = Atomadic(api_key='ato_...')
        result = murmuration.omega_lane(ato)
    """
    args = {'lane': lane}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_lane', args)

def omega_propose_mwo(client, intent, ledger_path, preferred_lane=None, preferred_tier=None, requested_by=None, **kwargs):
    """Generate a Murmuration MWO (Mission Work Order) proposal from a free-text intent: CNAE-token-parse it into a proposed tool name + tool_contract.v1 + mission_work_order.v1 (pending_operator_authorization), hash-chain appended. Returns {ok, proposed_tool_name, proposed_contract, proposed_mwo, mwo_id, chain_hash}.

    Args:
        intent (string, required): see MCP schema
        ledger_path (string, required): see MCP schema
        preferred_lane (string, optional): see MCP schema
        preferred_tier (integer, optional): see MCP schema
        requested_by (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, murmuration
        ato = Atomadic(api_key='ato_...')
        result = murmuration.omega_propose_mwo(ato, intent=..., ledger_path=...)
    """
    args = {'intent': intent, 'ledger_path': ledger_path, 'preferred_lane': preferred_lane, 'preferred_tier': preferred_tier, 'requested_by': requested_by}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_propose_mwo', args)

"""atomadic.healer -- Healer.

Diagnose, grade, and plan the repair.
Read-only diagnosis: code-health grade + advisory repair plan.

Entitlement: healer (Gate-1 unlocks these tools).
Status: beta.
Auto-emitted from the live MCP registry.
"""

def assess_artifact_health_pure(client, source_text, module_name=None, **kwargs):
    """[Healer product Â· entitlement: healer] Composite code-health diagnosis of a provided artifact: parses + logic density + single-callable + stub signals, graded A-F with issues. Read-only.

    Args:
        source_text (string, required): see MCP schema
        module_name (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, healer
        ato = Atomadic(api_key='ato_...')
        result = healer.assess_artifact_health_pure(ato, source_text=...)
    """
    args = {'source_text': source_text, 'module_name': module_name}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('assess_artifact_health_pure', args)

def compute_repair_plan_pure(client, error_message, source_text=None, **kwargs):
    """[Healer product Â· entitlement: healer] Compute an advisory repair plan for a provided broken artifact + its error: category, severity, concrete steps, confidence. Read-only â€” application stays with the customer/operator.

    Args:
        error_message (string, required): see MCP schema
        source_text (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, healer
        ato = Atomadic(api_key='ato_...')
        result = healer.compute_repair_plan_pure(ato, error_message=...)
    """
    args = {'error_message': error_message, 'source_text': source_text}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compute_repair_plan_pure', args)

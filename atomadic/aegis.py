"""atomadic.aegis -- Aegis.




Entitlement: aegis (Gate-1 unlocks these tools).
Status: live.
Auto-emitted from the live MCP registry.
"""

def assess_compliance_posture_pure(client, controls, framework=None, **kwargs):
    """[Aegis product Â· entitlement: aegis] Score declared controls vs a framework checklist (EU AI Act / NIST RMF / ISO 27001) â†’ coverage + gaps. Self-assessment scaffold, not a legal cert.

    Args:
        controls (array, required): see MCP schema
        framework (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, aegis
        ato = Atomadic(api_key='ato_...')
        result = aegis.assess_compliance_posture_pure(ato, controls=...)
    """
    args = {'controls': controls, 'framework': framework}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('assess_compliance_posture_pure', args)

def classify_data_sensitivity_pure(client, text, **kwargs):
    """[Aegis product Â· entitlement: aegis] Classify data sensitivity of a text sample (PII/PHI/financial/secret/gov-id) â†’ tier + categories. Detection only.

    Args:
        text (string, required): see MCP schema

    Example:
        from atomadic import Atomadic, aegis
        ato = Atomadic(api_key='ato_...')
        result = aegis.classify_data_sensitivity_pure(ato, text=...)
    """
    args = {'text': text}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('classify_data_sensitivity_pure', args)

def compose_governance_report_pure(client, system_name, compliance_coverage=None, open_incidents=None, policies_enforced=None, **kwargs):
    """[Aegis product Â· entitlement: aegis] Compose a governance report (compliance coverage + incidents + policies) â†’ governance score, A-D grade, recommendations.

    Args:
        system_name (string, required): see MCP schema
        compliance_coverage (number, optional): see MCP schema
        open_incidents (integer, optional): see MCP schema
        policies_enforced (integer, optional): see MCP schema

    Example:
        from atomadic import Atomadic, aegis
        ato = Atomadic(api_key='ato_...')
        result = aegis.compose_governance_report_pure(ato, system_name=...)
    """
    args = {'system_name': system_name, 'compliance_coverage': compliance_coverage, 'open_incidents': open_incidents, 'policies_enforced': policies_enforced}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compose_governance_report_pure', args)

def compute_audit_trail_digest_pure(client, events, **kwargs):
    """[Aegis product Â· entitlement: aegis] Build a tamper-evident hash-chained digest over audit events (sha256(prev+event)); any change alters the head.

    Args:
        events (array, required): see MCP schema

    Example:
        from atomadic import Atomadic, aegis
        ato = Atomadic(api_key='ato_...')
        result = aegis.compute_audit_trail_digest_pure(ato, events=...)
    """
    args = {'events': events}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compute_audit_trail_digest_pure', args)

def enforce_action_policy_pure(client, action, policy, **kwargs):
    """[Aegis product Â· entitlement: aegis] Deterministic action-policy engine: evaluate an action against allow/deny rules â†’ permit/deny + matched rule.

    Args:
        action (object, required): see MCP schema
        policy (object, required): see MCP schema

    Example:
        from atomadic import Atomadic, aegis
        ato = Atomadic(api_key='ato_...')
        result = aegis.enforce_action_policy_pure(ato, action=..., policy=...)
    """
    args = {'action': action, 'policy': policy}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('enforce_action_policy_pure', args)

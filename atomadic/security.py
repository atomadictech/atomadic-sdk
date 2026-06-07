"""atomadic.security -- Security.

A bubble of protection around every agent.
Bubble check, redaction, error-fold, hardening posture (PQC/FIPS-203).

Entitlement: security (Gate-1 unlocks these tools).
Status: live.
Auto-emitted from the live MCP registry.
"""

def assess_security_bubble_pure(client, content, strict=None, **kwargs):
    """[Security product Â· entitlement: security] Bubble check: sandbox-scan a content snippet for adversarial / prompt-injection / exfiltration / jailbreak patterns; returns PROCEED / REVIEW / BLOCK with the threats detected.

    Args:
        content (string, required): see MCP schema
        strict (boolean, optional): see MCP schema

    Example:
        from atomadic import Atomadic, security
        ato = Atomadic(api_key='ato_...')
        result = security.assess_security_bubble_pure(ato, content=...)
    """
    args = {'content': content, 'strict': strict}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('assess_security_bubble_pure', args)

def classify_error_fold_pure(client, error_message, action_kind=None, **kwargs):
    """[Security product Â· entitlement: security] Classify an error-fold entry with severity, category, and a suggested repair path before Healer ingests it.

    Args:
        error_message (string, required): see MCP schema
        action_kind (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, security
        ato = Atomadic(api_key='ato_...')
        result = security.classify_error_fold_pure(ato, error_message=...)
    """
    args = {'error_message': error_message, 'action_kind': action_kind}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('classify_error_fold_pure', args)

def compute_hardening_posture_pure(client, target_product_id, hardening_level, **kwargs):
    """[Security product Â· entitlement: security] Compute the recommended hardening posture (cumulative directives) for a target product at a level (info/low/medium/high/critical); critical requires operator co-sign.

    Args:
        target_product_id (string, required): see MCP schema
        hardening_level (string, required): see MCP schema

    Example:
        from atomadic import Atomadic, security
        ato = Atomadic(api_key='ato_...')
        result = security.compute_hardening_posture_pure(ato, target_product_id=..., hardening_level=...)
    """
    args = {'target_product_id': target_product_id, 'hardening_level': hardening_level}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compute_hardening_posture_pure', args)

def compute_redacted_args_pure(client, args, **kwargs):
    """[Security product Â· entitlement: security] Redact a tool-args object: replaces secret-pattern values and secret-named fields with safe placeholders (nested-aware).

    Args:
        args (object, required): see MCP schema

    Example:
        from atomadic import Atomadic, security
        ato = Atomadic(api_key='ato_...')
        result = security.compute_redacted_args_pure(ato, args=...)
    """
    args = {'args': args}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compute_redacted_args_pure', args)

def compute_redacted_text_pure(client, text, **kwargs):
    """[Security product Â· entitlement: security] Redact secrets from free-form text; replaces each match with a verify-without-reveal placeholder [REDACTED:kind:sha8].

    Args:
        text (string, required): see MCP schema

    Example:
        from atomadic import Atomadic, security
        ato = Atomadic(api_key='ato_...')
        result = security.compute_redacted_text_pure(ato, text=...)
    """
    args = {'text': text}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('compute_redacted_text_pure', args)

def define_security_constants_pure(client, **kwargs):
    """[Security product Â· entitlement: security] Canonical Security constants: bubble verdicts, hardening levels + cumulative directives, error-fold categories, redaction kinds, PQC standard (FIPS-203).

    Example:
        from atomadic import Atomadic, security
        ato = Atomadic(api_key='ato_...')
        result = security.define_security_constants_pure(ato)
    """
    args = {}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('define_security_constants_pure', args)

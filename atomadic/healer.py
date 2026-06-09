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

def omega_repair_closure(client, forge_root, target_root, max_iter=None, **kwargs):
    """LOSSLESS store-closure repair: iteratively quarantine atoms whose body cannot wire in the flat sovereign layout (relative import, missing-dep import, or upward/same-tier import) until import-closure is GREEN. Quarantine appends the DNA to logic-base/quarantine and removes the shard line + emitted .py (re-promotable once imports resolve). Symmetric across forge+target. Returns {iterations, quarantined, remaining}. Pass forge_root/target_root explicitly to scope it (point both at a shadow for a no-canonical-write dry validation).

    Args:
        forge_root (string, required): Root whose logic-base/shards are repaired (quarantine sink #1).
        target_root (string, required): Root whose shards + src/atomadic are repaired (quarantine sink #2; .py removed here).
        max_iter (integer, optional): Max fixpoint iterations (default 30).

    Example:
        from atomadic import Atomadic, healer
        ato = Atomadic(api_key='ato_...')
        result = healer.omega_repair_closure(ato, forge_root=..., target_root=...)
    """
    args = {'forge_root': forge_root, 'target_root': target_root, 'max_iter': max_iter}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_repair_closure', args)

def omega_repair_missing_imports(client, apply=None, max_apply=None, **kwargs):
    """Definitive systemic repair for the stripped-import bug: injects stdlib module imports (underscore-guarded), stdlib from-imports (Path/timezone/defaultdict/dataclass/lru_cache/dedent/...), and downward atom imports into fully-fixable atoms; re-emits via emit_atom_stateful on the existing record (preserves identity, gates each write). Skips atoms with same/upper-tier refs. apply=False dry run; max_apply caps batch.

    Args:
        apply (boolean, optional): False (default) = dry run. True = repair.
        max_apply (integer, optional): Cap atoms repaired this run (0 = all).

    Example:
        from atomadic import Atomadic, healer
        ato = Atomadic(api_key='ato_...')
        result = healer.omega_repair_missing_imports(ato)
    """
    args = {'apply': apply, 'max_apply': max_apply}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_repair_missing_imports', args)

def omega_scan_ast(client, large_dir_threshold=None, skip_dirs=None, **kwargs):
    """Live AST scan of the engine's emitted code: returns a structured map (per-module functions/classes/imports/assigns + per-tier/action/scope rollups + parse errors) for emergent discovery, healing, and drift pipelines. root engine-bound to $OMEGA; optional skip_dirs, large_dir_threshold.

    Args:
        large_dir_threshold (integer, optional): see MCP schema
        skip_dirs (array, optional): see MCP schema

    Example:
        from atomadic import Atomadic, healer
        ato = Atomadic(api_key='ato_...')
        result = healer.omega_scan_ast(ato)
    """
    args = {'large_dir_threshold': large_dir_threshold, 'skip_dirs': skip_dirs}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_scan_ast', args)

def omega_scan_missing_imports(client, max_samples=None, **kwargs):
    """Read-only blast-radius scan for the systemic stripped-helper-import bug: finds atoms that call sibling-helper atoms as bare undefined names, split into fixable (lower-tier, injectable downward) vs unfixable (upper/same-tier). Mutates nothing. Returns counts + samples.

    Args:
        max_samples (integer, optional): Max sample atoms to include in the report (default 40).

    Example:
        from atomadic import Atomadic, healer
        ato = Atomadic(api_key='ato_...')
        result = healer.omega_scan_missing_imports(ato)
    """
    args = {'max_samples': max_samples}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_scan_missing_imports', args)

def omega_scan_mistier(client, max_samples=None, **kwargs):
    """Read-only diagnostic for mis-tiered atoms (Map==Terrain): finds atoms named for a higher tier than their body warrants (pure body named composite/stateful; composing body named stateful). These cause same/upper-tier import violations and block polyglot emit. Highlights polyglot codegen helpers. Returns counts + samples + proposed corrected tier.

    Args:
        max_samples (integer, optional): Max sample atoms in report (default 40).

    Example:
        from atomadic import Atomadic, healer
        ato = Atomadic(api_key='ato_...')
        result = healer.omega_scan_mistier(ato)
    """
    args = {'max_samples': max_samples}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_scan_mistier', args)

def omega_self_heal(client, max_rounds=None, fill_gaps=None, **kwargs):
    """Closed-loop non-destructive engine self-heal: repair imports, re-tier pure atoms, fill DNA gaps. Runs up to 5 rounds until fixpoint. Returns {ok, rounds, broken_final}. This IS the flywheel.

    Args:
        max_rounds (integer, optional): Max heal rounds (default 3)
        fill_gaps (boolean, optional): Auto-emit missing-reference gaps (default true)

    Example:
        from atomadic import Atomadic, healer
        ato = Atomadic(api_key='ato_...')
        result = healer.omega_self_heal(ato)
    """
    args = {'max_rounds': max_rounds, 'fill_gaps': fill_gaps}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_self_heal', args)

def omega_sweep_orphans(client, src_root, apply=None, **kwargs):
    """Sweep orphaned emitted .py files (no backing DNA atom) from a src tree, deriving valid names from the store's shards. Dry-run unless apply=true. Restores DNA->src purity (part of byte-parity).

    Args:
        src_root (string, required): Emitted src dir to sweep, e.g. C:\Omega\src\atomadic
        apply (boolean, optional): Delete orphans when true; dry-run (list only) when false/default.

    Example:
        from atomadic import Atomadic, healer
        ato = Atomadic(api_key='ato_...')
        result = healer.omega_sweep_orphans(ato, src_root=...)
    """
    args = {'src_root': src_root, 'apply': apply}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_sweep_orphans', args)

def omega_verify_imports(client, **kwargs):
    """Engine self-diagnosis: verify every emitted atom's imports actually resolve. Reports atoms with missing-import / unresolved-symbol failures the static gate didn't catch. Use to spot the engine's own gaps so it can heal them.

    Example:
        from atomadic import Atomadic, healer
        ato = Atomadic(api_key='ato_...')
        result = healer.omega_verify_imports(ato)
    """
    args = {}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_verify_imports', args)

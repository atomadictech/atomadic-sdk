"""atomadic.forge -- Forge.




Entitlement: forge (Gate-1 unlocks these tools).
Status: live.
Auto-emitted from the live MCP registry.
"""

def omega_chain_autowire(client, target_name, chain, **kwargs):
    """Emergent-composite synthesis: given a target CNAE name and an ordered chain of EXISTING verified atom names, autowire them into a NEW composite (linear pipe; result feeds next atom's first arg). Grounded composition only, no fabrication. Returns {ok, id, tier, source, violations}. forge/target engine-bound.

    Args:
        target_name (string, required): CNAE name for the new composite (action_entity_scope).
        chain (array, required): Ordered list of existing atom names to compose.

    Example:
        from atomadic import Atomadic, forge
        ato = Atomadic(api_key='ato_...')
        result = forge.omega_chain_autowire(ato, target_name=..., chain=...)
    """
    args = {'target_name': target_name, 'chain': chain}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_chain_autowire', args)

def omega_context_packet(client, query, max_artifacts=None, radius=None, snippet_chars=None, **kwargs):
    """Token-efficient proximity context retrieval (murmuration context_packet aligned): given a query (CNAE name, 12-hex locator48, or free text), return the nearest atoms in the DNA store - Golay-locator Hamming distance when the query resolves to a coordinate, else CNAE token overlap - as a compact packet (name, tier, distance, file_path, docstring snippet). Use instead of Read+Glob+Grep for recon. logic_base/src_root engine-bound.

    Args:
        query (string, required): see MCP schema
        max_artifacts (integer, optional): see MCP schema
        radius (integer, optional): see MCP schema
        snippet_chars (integer, optional): see MCP schema

    Example:
        from atomadic import Atomadic, forge
        ato = Atomadic(api_key='ato_...')
        result = forge.omega_context_packet(ato, query=...)
    """
    args = {'query': query, 'max_artifacts': max_artifacts, 'radius': radius, 'snippet_chars': snippet_chars}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_context_packet', args)

def omega_emit_lang(client, atom, language=None, **kwargs):
    """DEH per-atom polyglot language selector: emit one atom in any target language by routing to the decoupled emit_<language>_atom emitter (dynamic dispatch over ~80 languages; aliases ts/rs/py/cs/cpp). Default python. Returns {ok, language, emitter, code}. This is the DEH choosing the output language via the `language` kwarg.

    Args:
        atom (object, required): Atom dict (name, cnae{action,entity,scope}, tier, intent) to emit.
        language (string, optional): Target language (default python; e.g. rust, typescript, go, csharp, haskell).

    Example:
        from atomadic import Atomadic, forge
        ato = Atomadic(api_key='ato_...')
        result = forge.omega_emit_lang(ato, atom=...)
    """
    args = {'atom': atom, 'language': language}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_emit_lang', args)

def omega_emit_polyglot(client, product, output_root, languages=None, **kwargs):
    """Polyglot emit head: emit a product's atoms as native source packages in any of ~80 target languages (Python/Rust/TypeScript/Go/C#/Java/Haskell/Lean/...). DEH chooses language via the `languages` kwarg (default python+rust+typescript); each language gets CNAE source files + .tocc-contracts + lineage + native scaffold (Cargo.toml/pyproject/package.json). Returns {ok, product_id, languages_emitted, packages}.

    Args:
        product (object, required): Product dict with product_id + atoms (the logic to emit).
        output_root (string, required): Directory to write the per-language packages into.
        languages (array, optional): Target languages (default ['python','rust','typescript']).

    Example:
        from atomadic import Atomadic, forge
        ato = Atomadic(api_key='ato_...')
        result = forge.omega_emit_polyglot(ato, product=..., output_root=...)
    """
    args = {'product': product, 'output_root': output_root, 'languages': languages}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_emit_polyglot', args)

def omega_govern_actions(client, additions, **kwargs):
    """Additively amend the action collapse map in the frozen actions glossary â€” the action-vocab analog of omega_govern_scopes (which extended scopes for tiers 5-8 on 2026-06-07). Adds synonym tokens to existing canonical actions' collapse lists so omega_synthesize accepts harvested names that aren't on the frozen 54. Idempotent. Records an amendment. Server-internal write via the engine's own emit path; the glossary stays hook-protected. additions=[{canonical, synonyms:[...], intent}].

    Args:
        additions (array, required): see MCP schema

    Example:
        from atomadic import Atomadic, forge
        ato = Atomadic(api_key='ato_...')
        result = forge.omega_govern_actions(ato, additions=...)
    """
    args = {'additions': additions}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_govern_actions', args)

def omega_govern_scopes(client, additions, **kwargs):
    """Additively amend the frozen scope glossary with new scope->tier tokens (preserves all existing scopes; idempotent; records an amendment). Returns {ok, added, skipped_existing, total_scopes, tier_scope, path}. target_root engine-bound to $OMEGA. Pass additions=[{name,tier,intent},...].

    Args:
        additions (array, required): see MCP schema

    Example:
        from atomadic import Atomadic, forge
        ato = Atomadic(api_key='ato_...')
        result = forge.omega_govern_scopes(ato, additions=...)
    """
    args = {'additions': additions}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_govern_scopes', args)

def omega_harvest_permissive(client, corpus_path, exclude=None, **kwargs):
    """Permissive harvest (spaghetti-to-shippable): absorb good logic from a corpus even when its names are NOT CNAE-compliant, by reclassifying each atom from its docstring/source onto a compliant CNAE address, then immune-gating the body. Permissive on name, strict on logic. Pass corpus_path; forge/target engine-bound.

    Args:
        corpus_path (string, required): see MCP schema
        exclude (array, optional): see MCP schema

    Example:
        from atomadic import Atomadic, forge
        ato = Atomadic(api_key='ato_...')
        result = forge.omega_harvest_permissive(ato, corpus_path=...)
    """
    args = {'corpus_path': corpus_path, 'exclude': exclude}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_harvest_permissive', args)

def omega_intent(client, intent, args=None, **kwargs):
    """One-call intent router: take an intent, resolve it to the proper engine atom (or create one by autowiring existing atoms), run it, and return the result.

    Args:
        intent (string, required): see MCP schema
        args (object, optional): see MCP schema

    Example:
        from atomadic import Atomadic, forge
        ato = Atomadic(api_key='ato_...')
        result = forge.omega_intent(ato, intent=...)
    """
    args = {'intent': intent, 'args': args}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_intent', args)

def omega_intent_shippable(client, intent, target_tier=None, top_n=None, **kwargs):
    """Intent â†’ shippable tool router (MVP of the intent enhance loop). Tokenizes a natural-language intent, classifies tokens against the frozen vocab to derive candidate CNAE names, probes the DNA store for direct matches, and returns either (a) the matched atom as a shippable (path + tier + signature + suggested MCP tool name) or (b) the inferred CNAE scaffold + top-N semantic-neighbor atoms by token overlap + a synthesize-ready next-step hint. Foundational entry point; the full flywheel (loop_intent_temporal et al.) is gated by broken harvest atoms still pending corpus-level repair.

    Args:
        intent (string, required): Natural-language description of the tool to ship.
        target_tier (integer, optional): Optional tier hint (0..7); narrows scope candidates.
        top_n (integer, optional): Number of semantic neighbors to return when no direct match.

    Example:
        from atomadic import Atomadic, forge
        ato = Atomadic(api_key='ato_...')
        result = forge.omega_intent_shippable(ato, intent=...)
    """
    args = {'intent': intent, 'target_tier': target_tier, 'top_n': top_n}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_intent_shippable', args)

def omega_register_tool(client, name, atom, tier, description, bind=None, input_schema=None, **kwargs):
    """Engine self-registration: register or update an MCP tool entry in mcp_tools.jsonl so a newly-emitted atom becomes a live tool after omega_reload (idempotent by name).

    Args:
        name (string, required): see MCP schema
        atom (string, required): see MCP schema
        tier (integer, required): see MCP schema
        description (string, required): see MCP schema
        bind (object, optional): see MCP schema
        input_schema (object, optional): see MCP schema

    Example:
        from atomadic import Atomadic, forge
        ato = Atomadic(api_key='ato_...')
        result = forge.omega_register_tool(ato, name=..., atom=..., tier=...)
    """
    args = {'name': name, 'atom': atom, 'tier': tier, 'description': description, 'bind': bind, 'input_schema': input_schema}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_register_tool', args)

def omega_synthesize(client, raw_name, source, inputs=None, intent=None, outputs=None, **kwargs):
    """The engine's native authoring entry point: synthesize one atom from {raw_name, source, intent} â€” load frozen vocab, compose the canonical logic_block, persist DNA to forge+target, render+gate+write the atom into $OMEGA/src. Returns {ok,id,tier,cnae,written,path,violations} or a reject verdict. forge_root/target_root are engine-bound to $FORGE/$OMEGA.

    Args:
        raw_name (string, required): Source function name (may be non-CNAE; will be reclassified).
        source (string, required): Full Python source of the single callable to absorb.
        inputs (array, optional): see MCP schema
        intent (string, optional): Optional human intent describing the capability.
        outputs (array, optional): see MCP schema

    Example:
        from atomadic import Atomadic, forge
        ato = Atomadic(api_key='ato_...')
        result = forge.omega_synthesize(ato, raw_name=..., source=...)
    """
    args = {'raw_name': raw_name, 'source': source, 'inputs': inputs, 'intent': intent, 'outputs': outputs}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('omega_synthesize', args)

def orchestrate_corpus_harvest_temporal(client, corpus_path, limit=None, product=None, **kwargs):
    """Absorb a corpus of Python into canonical DNA end-to-end: walk -> shatter into one-callable atoms -> classify onto CNAE -> immune-gate -> dedup (by typed address + content hash) -> synthesize -> emit. Returns a harvest manifest {scanned,candidates,gated,authored,deduped,emitted,blocked,ids}.

    Args:
        corpus_path (string, required): see MCP schema
        limit (integer, optional): see MCP schema
        product (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, forge
        ato = Atomadic(api_key='ato_...')
        result = forge.orchestrate_corpus_harvest_temporal(ato, corpus_path=...)
    """
    args = {'corpus_path': corpus_path, 'limit': limit, 'product': product}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('orchestrate_corpus_harvest_temporal', args)

def orchestrate_pipeline_truthstate_temporal(client, min_tier=None, **kwargs):
    """Regenerate logic-base/pipelines as the state-of-truth of Omega's real composition chains (the function-calling index for the GUI/leech brain).

    Args:
        min_tier (integer, optional): see MCP schema

    Example:
        from atomadic import Atomadic, forge
        ato = Atomadic(api_key='ato_...')
        result = forge.orchestrate_pipeline_truthstate_temporal(ato)
    """
    args = {'min_tier': min_tier}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('orchestrate_pipeline_truthstate_temporal', args)

def render_from_template_pure(client, template, context, missing=None, **kwargs):
    """[Release product Â· entitlement: release] Deterministically render a {{token}} text template from a context mapping. Ours or customer templates, one code path.

    Args:
        template (string, required): see MCP schema
        context (object, required): see MCP schema
        missing (string, optional): see MCP schema

    Example:
        from atomadic import Atomadic, forge
        ato = Atomadic(api_key='ato_...')
        result = forge.render_from_template_pure(ato, template=..., context=...)
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
        from atomadic import Atomadic, forge
        ato = Atomadic(api_key='ato_...')
        result = forge.render_website_stateful(ato, template_dir=..., context=..., output_dir=...)
    """
    args = {'template_dir': template_dir, 'context': context, 'output_dir': output_dir, 'include_ext': include_ext}
    args = {k: v for k, v in args.items() if v is not None}
    args.update(kwargs)
    return client.call('render_website_stateful', args)

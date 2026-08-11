# Brooklyn Skills integration

AGENTROPOLIS adopts `OutThisLife/brooklyn-skills` as a governed upstream skill pack, not as a root instruction set or autonomous runtime.

Pinned upstream commit:

`f60ab3b43f422309c74dff5ed7dc53af042c2908`

Registry policy:

`governance/upstream-skills/brooklyn-skills.yaml`

## Why this pack

The upstream repository contains portable `SKILL.md` packages with no required harness-specific setup scripts. The initial curated set strengthens coding-agent operations in four areas:

- evidence-first research and audit-only investigation
- isolated worktree execution for parallel agents
- PR triage/readiness/update discipline
- UI-system discipline and visual verification

## Governance boundary

The upstream repository's `defaults.md` is not imported as an AGENTROPOLIS global prompt. Upstream defaults remain reference material only.

Execution precedence remains:

1. AGENTROPOLIS Root Law
2. Policy/Risk Layer
3. 54-T containment
4. AGENTIC STUDIOS BACK END (ASBE) governance
5. district policy
6. repository-local policy
7. imported skill instructions

A skill registration grants no authority by itself.

## Hermes target

Hermes supports external skill directories. A runtime adapter may clone the pinned commit into a governed cache and expose only approved paths from the registry manifest.

Conceptual configuration after adapter enforcement:

```yaml
skills:
  external_dirs:
    - ~/.agentropolis/skill-cache/brooklyn-skills/f60ab3b43f422309c74dff5ed7dc53af042c2908/skills
```

Do not point production Hermes directly at a floating upstream checkout. The cache must correspond to the reviewed commit and must not silently update with `git pull`.

## Codex / Claude Code / Cursor / OpenCode targets

Provider adapters should map common AGENTROPOLIS skill identifiers to approved skill entrypoints. Do not paste upstream `defaults.md` wholesale into root `AGENTS.md` or equivalent system-level instruction files.

The adapter should preserve:

- source repository and commit SHA
- selected skill path
- capability grant used for the run
- policy decision
- execution receipt or advisory-only result

## Recommended first activation wave

Advisory by default:

- `research`
- `audit-only`
- `ui-system`
- `visual-verify`

Scoped repository execution:

- `work`
- `clean`
- `ui-only`
- `runtime-debug`

Approval-gated Git/GitHub execution:

- `pr-triage`
- `pr-ready`
- `pr-update`
- `cpr`

## Deferred upstream skills

Machine-state cleanup, macOS notarization, social drafting, ticket shipping, and other higher-impact workflows remain deferred until their domain-specific capability policies are reviewed.

## Update procedure

1. Fetch the new upstream commit without activating it.
2. Diff every curated `SKILL.md` and referenced resource against the current pin.
3. Re-run 54-T capability/risk review.
4. Record ASBE provenance and policy result.
5. Update the manifest pin in a reviewed PR.
6. Refresh runtime caches only after approval.

No automatic floating upstream updates.
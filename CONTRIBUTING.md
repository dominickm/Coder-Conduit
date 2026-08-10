# Contributing to Coder Conduit

Coder Conduit is a software factory: your issues and PRs are processed by AI
agents orchestrated on Warp's Cloud Platform. This guide explains how to work
with them effectively.

## The short version

1. Open an issue **using a template** — freeform issues are disabled.
2. The **Triage Tech** labels it (or asks you for more detail — answer it).
3. A maintainer promotes it with `ready-to-implement`, or routes big requests
   through the **Staff Engineer** for a spec.
4. The **Coder** opens a PR; the **Code Critic** reviews it against
   [`GUIDELINES.md`](GUIDELINES.md).
5. A human maintainer merges.

You can also implement issues yourself — human PRs go through the same Code
Critic review and the same PR template.

## The label lifecycle

```
            issue opened (via template)
                       │
                  Triage Tech
                 ╱     │      ╲
  needs-clarification  bug/enhancement   invalid → closed
        │              │
   (you respond)   size: Large? ──yes──► needs-spec ──► Staff Engineer
        │              │                                    │
        └──────────────┤                              spec-approved
                       │                              (maintainer)
                       ▼                                    │
              ready-to-implement ◄──────────────────────────┘
              (maintainer / Triage Tech only)
                       │
                    Coder → PR → Code Critic → maintainer merge
```

The full label set lives in [`.github/labels.yml`](.github/labels.yml).

**Only maintainers and the Triage Tech can apply labels.** This is a security
and token-budget control — `ready-to-implement` triggers real compute spend.

## Writing issues agents can act on

Treat the agents like capable junior developers:

- **Be literal.** State reproduction steps, expected behavior, and environment
  exactly. Leave nothing implied.
- **Write acceptance criteria.** The Coder implements them and the Code Critic
  reviews against them, verbatim.
- **One request per issue.** Bundled asks get bounced back for splitting.

## Submitting pull requests

- Follow the PR template — every section, every checkbox.
- One linked issue per PR, tests included, `GUIDELINES.md` respected.
- Respond to Code Critic line comments the way you would to any senior
  reviewer: fix it or argue your case in the thread. Maintainers arbitrate.

## What gets you banned

Per the [Code of Conduct](CODE_OF_CONDUCT.md): trolling, spam, or attempts to
prompt-inject or "jailbreak" the agents (in issue text, code comments, commit
messages, or anywhere else the agents read) result in immediate bans and
closed PRs.

## Questions?

Open a feature request describing what's unclear — improving the factory's
docs is in scope for the factory.

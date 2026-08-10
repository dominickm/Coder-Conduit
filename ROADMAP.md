# Coder Conduit — Road to Alpha

This document lays out the concrete path from the current state (README + LICENSE)
to a functioning Alpha of the Coder Conduit software factory.

## What "Alpha" means here

Coder Conduit's product is the **factory itself**: a repository where community
submissions flow through AI agents that triage, plan, implement, and review.
Alpha is reached when:

1. A community member can open an issue using a template, and the **Triage Tech**
   labels it without human intervention.
2. A maintainer can apply `ready-to-implement`, and the **Coder** produces a PR.
3. The **Code Critic** reviews that PR against written, checked-in guidelines.
4. At least one small, community-chosen application lives in this repo and has
   been built end-to-end through that loop.

## Phase 0 — Repository scaffolding (this branch)

The agents can't operate on a repo that has nothing for them to parse. This
phase adds every artifact the README already promises:

- [x] `ROADMAP.md` — this document
- [ ] Structured issue templates (`.github/ISSUE_TEMPLATE/`) — YAML issue forms,
      so agent parsing is deterministic rather than best-effort
- [ ] Pull request template (`.github/PULL_REQUEST_TEMPLATE.md`)
- [ ] `CONTRIBUTING.md` — the human-facing workflow, including the label lifecycle
- [ ] `GUIDELINES.md` — the code standards the Code Critic reviews against
- [ ] `CODE_OF_CONDUCT.md` — backs the enforcement policy stated in the README
- [ ] `.github/labels.yml` — declarative source of truth for the label set

## Phase 1 — Agent enablement

Wire the five Warp agents to the scaffolding and verify each in isolation:

1. **Triage Tech** — point it at the issue forms; verify it applies labels from
   `.github/labels.yml` only, and asks for clarification on incomplete forms.
2. **Code Critic** — point it at `GUIDELINES.md`; open a deliberately
   non-conforming test PR and confirm it requests changes with line comments.
3. **Coder** — seed one small, well-specified `ready-to-implement` issue and
   confirm it ships a passing PR.
4. **Staff Engineer** — file one larger feature request and review the spec it
   produces (specs land in `specs/`).
5. **Architect** — enable the CRON job last, once the repo has real code to scan.

Each agent gets a dry run before the repo opens to general submissions.

## Phase 2 — Pick the Alpha application

The factory needs raw material. Open a pinned discussion/issue where the
community proposes and votes on the first project. Constraints for a good pick:

- Small enough that a single agent PR can deliver a meaningful slice
- Testable, so the Code Critic and CI have something objective to check
- Fun enough to keep Coder Radio listeners filing issues

Once chosen, the Staff Engineer produces the initial spec, a maintainer approves
it, and the skeleton (build tooling, CI workflow, test harness) is committed.

## Phase 3 — Alpha exit checklist

- [ ] CI runs on every PR (lint + tests) and the Code Critic treats a red build
      as an automatic change request
- [ ] Five or more community issues have flowed through triage → implementation
      → review → merge with no manual code written by maintainers
- [ ] The Architect has filed at least one issue that was subsequently shipped
- [ ] `README.md` badges/status reflect a live, working factory

## Out of scope for Alpha

- Multi-project support (one community app only)
- Automated label application by anyone other than Triage Tech + maintainers
- Token-budget dashboards / cost reporting (track manually for now)

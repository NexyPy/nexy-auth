# Nexy Auth - Agent Guide

## Scope

nexy-auth is the native authentication module for Nexy. It stays a module of Nexy, not an
independent framework. The API is designed in the issues before any implementation. The first
version covers email and password, sessions, OAuth and OpenID Connect, passwordless sign-in,
second factor and organizations.

## Order of work

1. Research the question before changing anything. Read the issue, the README and the official
   documentation of every tool or protocol involved. Check current versions and advisories with
   the registries, not from memory. Write the source and the date in the issue or the pull request.
2. Verify the research by running a command that answers the question: `uv pip index versions`,
   `npm view`, `curl` on a registry, `gh api`, or a small program. A claim without a command is
   not a fact.
3. Write the test that fails (red). One behaviour, one assertion, named
   `test_<thing>_<scenario>`.
4. Write the least code that passes (green).
5. Refactor while the tests stay green.
6. Run every gate and quote what it printed. A gate that was not run does not exist.

## Research and verification

- Use primary sources first: official documentation, package registries, CVE databases, the
  source of the action or library pinned in this repository.
- Record the exact version you checked. Versions in this file are a snapshot, not a promise.
- Reproduce a security advisory with a test that sends the hostile input before you fix it.
- Reproduce a performance claim with a measurement before and after, then keep it in a budget test.
- Verify a tool setting by breaking it on purpose in a scratch file, then restoring it. A setting
  that was never red cannot be trusted when it is green.
- Never guess a commit SHA, a version or a configuration key. Resolve them with a command.

## Done means tested, measured and checked

- Every added line of `src/server/nexy_auth/` runs in a test, and every branch it opens is taken. Total
  coverage is not enough, because it hides the new lines no test runs.
- Security has its own tests. Every value a person or another site controls gets a hostile test:
  a path that climbs out of its folder, a body over the limit, a redirect to another site, a call
  from another origin, a session cookie without HttpOnly.
- A hot path has a number before and after, and a budget test keeps it there. The budget compares
  with a baseline measured in the same run.
- Each test sets up its own data, leaves nothing behind and never sleeps.
- The code has one job, a name that says it, and no copy of code that already exists.
- `python scripts/verify.py` prints only successes.

## Code

- KISS. The simplest code that works wins. No abstraction for a case that does not exist yet, no
  clever one-liner, no option nobody asked for.
- One function, one treatment. A function does one thing and its name is a verb that says which.
  Aim for fewer than 20 lines.
- One class, one intention. Aim for fewer than 10 methods. Depend on a `Protocol`, not on a
  concrete class, and pass collaborators in rather than creating them inside.
- Dependency injection is constructor injection. Define the port as a `Protocol` in `ports.py`,
  accept it in `__init__`, and let the composition root build the graph. No global mutable
  singleton, no service locator, no import-time side effect. A class that needs a database or a
  clock takes it as an argument.
- One folder, one set of intentions. Never `utils/`, `misc/` or `common/`. A folder that mixes two
  intentions is split.
- Names are English, complete words, no abbreviation a newcomer would have to guess. A comment
  says why, never what.
- SOLID in practice: one reason to change per unit, small interfaces, extend by adding rather
  than by editing a switch.
- No duplication. The second copy is a signal, the third is a bug. Extract after the second.

## Characters and language

- All code, comments, names, docs, issues, pull requests, commit messages and replies are in
  English. French accented letters are allowed only where French text is quoted.
- Use only characters typed on an English or French keyboard. Never write an em dash, an en dash,
  an arrow, an ellipsis character, a curly quote, a bullet, a middle dot, an almost equal sign, a
  multiplication sign, a check mark, a warning sign, a star used as a mark, box drawing, a
  no-break space or a zero-width space. Use a comma, a colon, parentheses or two sentences. A
  Markdown list uses a hyphen. An icon is an SVG with an accessible name, never a symbol used as
  a picture.
- No emoji anywhere: code, comments, UI text, terminal output, logs, docs or commits.
- `scripts/check_human_characters.py` enforces the character rule on tracked files, staged files
  and commit messages. It is a gate, not a suggestion.

## Branches

- `main` is the release branch. It receives reviewed changes from `develop` and release commits.
- `develop` is the integration branch. Every change lands there first. Open a pull request against
  `develop` and link the issue it resolves.
- Work branches use `feature/*`, `fix/*`, `docs/*` and `perf/*`, named after the issue. A work branch
  starts from `develop` and targets `develop`.
- Diff coverage compares with `origin/develop`, so a change is measured against the code it will
  merge into.
- Only the maintainer merges into `main` and `develop`. A contributor works on a branch and waits
  for the review.
- GitHub branch protection enforces this on both branches: a pull request, one code owner approval,
  an approval after the last push, up-to-date branches and every CI check are required. Force pushes
  and branch deletion are refused. The maintainer can bypass the rule when the repository needs it.

## Commits and attribution

- Conventional Commits: `feat:`, `fix:`, `docs:`, `refactor:`, `perf:`, `test:`, `chore:`. The
  message says why.
- One commit, one unit: a function with its test and its doc line, one behaviour with the test
  that proves it, or one structure change with no behaviour change. A refactor and a feature
  never share a commit. One file written by hand per commit, with only what that file implies.
- No attribution to an AI tool or an AI account. No `Co-authored-by` with a tool or an agent, no
  `Generated with` footer, no agent account as author or committer. This applies to Codex,
  Freebuff, Claude Code, OpenCode and every other tool. GitHub counts a trailer as a contributor
  forever, so the check runs on every commit.
- `scripts/check_attribution.py` runs in `.githooks/commit-msg` and in CI. Never bypass a hook
  with `--no-verify`. A failed gate is fixed, not skipped.
- `.githooks/pre-commit` checks staged files. Enable the hooks once per clone with
  `git config core.hooksPath .githooks`.

## Toolchain

- Python 3.13, uv and the Astral tools: ruff for lint and format, mypy in strict mode, pytest
  with branch coverage, bandit for the security scan, pip-audit for advisories.
- TypeScript uses pnpm, Vitest for unit tests and `tsc --noEmit` for the full project typecheck.
  Node and every package must be on a supported LTS or current stable line. Lockfiles are
  committed and installed frozen.
- A job fails on an error or a warning. No rule is disabled to make a gate green. A deliberate
  exception needs a one-line justification next to it and an entry in the accepted risk register.
- Dependencies are updated by Dependabot on a weekly schedule. A version is upgraded after its
  gates pass, not before.

## Bot identities

- Every bot account that acts for Nexy uses the Nexy logo as its avatar. A GitHub App owned by Nexy
  uploads `docs/assets/nexy-bot-avatar.png` as its badge, with the dark background `#0a0a0a`.
- GitHub-owned bots (Dependabot, github-actions) keep their own avatar. A repository cannot change
  it, and no bot is created to impersonate them.
- Third-party apps keep their own identity. A bot with write access is reviewed like any other
  collaborator and is never named after an AI tool.

## Pull requests and releases

- A pull request has one purpose, an English description, the gate output and no generated text.
  The PR template is the checklist. Do not merge with a red gate.
- A contributor never approves or merges their own pull request. The maintainer reviews the work
  and merges it. A pull request from a contributor needs the maintainer approval before it can
  merge. The maintainer owns every file through .github/CODEOWNERS.
- Releases are tag driven and published with PyPI Trusted Publishing. The build job and the
  publish job are separate, the publish job has only `id-token: write`, and the distributions are
  smoke tested before upload.
- The tag must match the version in the package. A release is created from the tag only after
  PyPI accepted the files.

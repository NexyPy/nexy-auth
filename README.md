# nexy-auth

Authentication for Nexy apps, in the spirit of better-auth: sign-in, sessions and permissions that
work the day the module is added, stored in the database the project already has.

## Why

Every app rewrites the same parts: password hashing, session cookies, OAuth callbacks, email
verification, password reset, rate limits on sign-in. Each rewrite is a new chance to get security
wrong. nexy-auth ships them once, tested, with safe defaults.

## What it covers

| Area | First version |
|---|---|
| Email and password | sign-up, sign-in, verification email, reset, Argon2id hashing |
| Sessions | database sessions, HttpOnly cookies, rotation, revocation, list of active devices |
| OAuth | GitHub, Google, Apple, Microsoft, Discord, plus any OpenID Connect provider |
| Passwordless | magic links, one-time codes, passkeys (WebAuthn) |
| Second factor | TOTP apps, backup codes |
| Teams | organizations, members, invitations, roles |
| Protection | rate limits on sign-in and reset, CSRF on forms, account lockout |

## How it fits in Nexy

- Configured in `nexyconfig.py`, tables created by `nx migrate` from the existing `DATABASE_URL`.
- Server side: a dependency for handlers and actions, and a guard for routes and layouts.
- Client side: the same hooks for React, Vue, Svelte, Solid and Preact islands.
- Plugins add a provider or a feature without forking the module.
- Emails go through [nexy-mail](https://github.com/NexyPy/nexy-mail) when it is installed.

## Status

Design phase. The API is being written in the issues before any code. Nothing is published yet.

## Documentation

The module docs live in [docs/](docs/README.md). The planned install is two commands:

```bash
nx add nexy-auth
nx migrate --upgrade
```

`nx add` currently handles UI components, so module support is being designed in
[issue 9](https://github.com/NexyPy/nexy-auth/issues/9). The docs show the planned API and how it will
be used in a project, and every page says what is still a decision.

## Repository layout

- `src/server/nexy_auth/` is the Python package, imported as `nexy_auth`.
- `client/` is the TypeScript contract harness, installed with pnpm.
- `docs/` is the module documentation.

## Development

Python uses uv and the Astral tools. TypeScript uses pnpm and Vitest. Node 26 and Python 3.13
are the reference runtimes.

```bash
uv sync --frozen --group dev
git config core.hooksPath .githooks
uv run python scripts/verify.py
pnpm --dir client run verify
```

Read AGENTS.md before a change. Every gate must pass, every identifier and sentence is in English,
and no AI tool is named as an author or a co-author.

## License

MIT

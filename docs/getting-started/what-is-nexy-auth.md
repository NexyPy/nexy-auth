# What is nexy-auth?

nexy-auth is the authentication module of Nexy. It provides sign-in, sessions and permissions that
work the day the module is added, stored in the database the project already has.

The module is in design phase. Its API is being written in the issues of this repository before any
code. Nothing is published, and no page here shows an install command.

## What problem does it solve?

Every app rewrites the same security code: password hashing, session cookies, OAuth callbacks, email
verification, password reset and rate limits on sign-in. Each rewrite is a new chance to get security
wrong. nexy-auth ships these parts once, with safe defaults and hostile input tests.

## What is in the first version?

The first version covers email and password, sessions, OAuth and OpenID Connect, passwordless
sign-in, second factor and organizations. See
[Which features come first?](which-features-come-first.md) for the list and the issues behind it.

## How does it fit in Nexy?

- Configured in `nexyconfig.py`, with tables created by `nx migrate` from the existing `DATABASE_URL`.
- Server side, a typed dependency for handlers and actions, and a guard for routes and layouts.
- Client side, the same hooks for React, Vue, Svelte, Solid and Preact islands.
- Plugins add a provider or a feature without forking the module.
- Email goes through [nexy-mail](https://github.com/NexyPy/nexy-mail) when it is installed.

These names describe the planned API tracked in issue 1. Read
[What will the nexy-auth API look like?](../reference/planned-api.md) for the current outline.

## What is not decided?

Native mobile clients are deferred until a concrete app needs them. Issue 7 records what a decision
requires. Native mobile clients are not part of the first version.

# Which features come first?

The first version of nexy-auth covers email and password, sessions, OAuth and OpenID Connect,
passwordless sign-in, second factor and organizations. Native mobile clients are deferred.

Each row names the issue that decides the feature. The module is in design phase, so a row is a
decision about scope, not a shipped interface.

| Area | What it covers | Issue |
|---|---|---|
| Email and password | Sign-up, sign-in, verification, reset, Argon2id hashing | 2 |
| Sessions | Database sessions, HttpOnly cookies, rotation, revocation, rate limits | 2 |
| OAuth and OpenID Connect | GitHub, Google, Apple, Microsoft, Discord, any OpenID Connect provider | 3 |
| Passwordless | Magic links, one-time codes, passkeys with WebAuthn | 4 |
| Second factor | TOTP apps and backup codes | 4 |
| Organizations | Organizations, members, invitations, roles and a permission check | 5 |
| HTTP contract | Endpoints, shapes and headers for clients outside a Nexy app | 6 |
| Native mobile clients | Deferred until a concrete app requires them | 7 |

## What decides the order?

Issue 1 writes the API of the module before any code. An area is designed in its own issue, then
implemented with a test that proves the behaviour. A feature is not written as working in these docs
until its code exists.

## Where is the detail?

Read [How do sessions work?](../concepts/sessions.md),
[How do organizations and roles work?](../concepts/organizations-and-roles.md), and
[What will the nexy-auth API look like?](../reference/planned-api.md).

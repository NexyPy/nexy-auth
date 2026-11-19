# How can an external client call nexy-auth?

Issue 6 defines a reusable HTTP contract so a client outside a Nexy app can use nexy-auth without
depending on Nexy or on a particular frontend framework. No endpoint is agreed yet, so this page
lists the scope and constraints and does not invent a URL.

## What must the contract cover?

- Sign-up, sign-in, verification and reset.
- Session cookies, rotation and revocation.
- Second-factor challenge and completion.
- Provider callback handoff for OAuth and OpenID Connect.
- Error shapes and status codes.

## What are the constraints?

- Nexy apps keep the native path: typed dependency, route guard and hooks. The HTTP contract is for
  external clients, not a replacement for that path.
- One shared domain core. Nexy itself does not go through the HTTP boundary.
- No frontend dependency in nexy-auth. Each framework gets a thin adapter.
- The five web frameworks in the first version are React, Vue, Svelte, Solid and Preact.

## What threat model must be written?

The contract document must cover CSRF, cookie flags, session fixation, rate limits and token replay.

## What is deferred?

Native mobile clients are tracked in issue 7. A decision needs a concrete app, the storage of tokens
or cookies on each platform, the callback return path, the scope of passkeys and TOTP, and the parts
of this contract that can be reused. No spec is written before that decision.

For the native path in a Nexy app, read
[How do I use the nexy-auth API in a project?](../getting-started/use-the-api-in-a-project.md).

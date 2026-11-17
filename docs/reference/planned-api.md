# What will the nexy-auth API look like?

The nexy-auth API is being written in issue 1 before any code. The outline below lists the surfaces
that issue has to define. Every name here is planned, not available.

| Surface | What issue 1 has to define | Where a Nexy app uses it |
|---|---|---|
| Configuration | Fields in `nexyconfig.py` and their defaults | Project configuration |
| Server dependency | A typed dependency for handlers and actions | Python code |
| Route guard | A guard for routes and layouts | Routing |
| Client hooks | The same hooks for React, Vue, Svelte, Solid and Preact | Client islands |
| Plugin interface | Add a provider or a feature without forking the module | Extension |
| Tables | Tables created by `nx migrate` from `DATABASE_URL` | Database |

## What is the native path?

A Nexy app keeps the native path: configure the module, take the dependency in a handler, guard a
route and call the hooks in a client island. The HTTP contract in issue 6 is for clients outside a
Nexy app. It does not replace the native path.

## What must not happen?

- No global mutable singleton. A class that needs a database or a clock takes it in its constructor.
- No Nexy dependency in the domain core, and no frontend dependency in the module.
- No import-time side effect.
- No planned name written as if it worked.

## When does this page change?

When the first version ships, this page is rewritten against the real names and the planned label is
removed. Until then, a change here points at the issue that decides it.

For a walk through the surfaces in a project, read
[How do I use the nexy-auth API in a project?](../getting-started/use-the-api-in-a-project.md).

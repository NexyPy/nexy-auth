# How do I add nexy-auth to a Nexy project?

The planned install is `nx add nexy-auth`, then `nx migrate --upgrade` to create the tables. nexy-auth
is in design phase and `nx add` currently handles UI components, so module support is being designed
in issue 9. Nothing in this page has shipped yet.

## What you will run

```bash
nx add nexy-auth
nx migrate --upgrade
```

## What each step will do

| Step | Effect |
|---|---|
| `nx add nexy-auth` | Install the package in the project environment |
| `nx add nexy-auth` | Add auth fields with their defaults to `nexyconfig.py` |
| `nx add nexy-auth` | Register the auth tables with the project ORM |
| `nx migrate --upgrade` | Apply the pending migration to the database at `DATABASE_URL` |

The command must be idempotent: running it twice changes nothing the second time. It must not
overwrite a file it does not own. Both rules are part of issue 9 and need a test each.

## What you need before you start

- A Nexy project with `nexyconfig.py` and a `DATABASE_URL` that `nx migrate` can reach.
- An ORM selected in `useORM`, so `nx migrate` knows whether to use Alembic or Aerich.
- A committed lockfile, so the added package is pinned.

## What happens next

Read [How do I use the nexy-auth API in a project?](use-the-api-in-a-project.md) for the planned
configuration, dependency, guard and hooks. Read
[What will the nexy-auth API look like?](../reference/planned-api.md) for the list of surfaces.

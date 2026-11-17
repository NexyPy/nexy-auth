# How do I use the nexy-auth API in a project?

In the planned API you configure nexy-auth in `nexyconfig.py`, take a typed dependency in a handler,
guard a route or layout with a dependency, and call the same hooks from a client island. Every name
below is a proposal from issue 1, not a working interface. The first version has not shipped.

## 1. Configure the module

After [adding the module](add-to-a-project.md), the generated configuration has the auth fields next
to the Nexy fields:

```python filename="nexyconfig.py"
from nexy.core.models import NexyConfigModel
from nexy.frontend import react
from nexy_auth import auth


class NexyConfig(NexyConfigModel):
    useFF = react()
    useORM = "SQLAlchemy"
    useAuth = auth(providers=["github", "google"], require_verified_email=True)
```

The exact field names and defaults are part of issue 1. `nx migrate` uses `useORM` to pick Alembic or
Aerich.

## 2. Read the session in a handler

A handler takes the session through `Depends`, like any other FastAPI dependency. The server keeps
the session in the database and the browser sends its identifier in an HttpOnly cookie.

```python filename="src/routes/api/me.py"
from nexy.http import Depends
from nexy_auth import current_session


async def GET(session=Depends(current_session)):
    return {"user_id": session.user_id, "email": session.email}
```

## 3. Guard a directory

A `dependencies.py` applies to every handler and page in its directory and below. Put the session
guard there to protect a whole section of the site.

```python filename="src/routes/admin/dependencies.py"
from nexy_auth import require_session

dependencies = [require_session]
```

## 4. Check a role

A permission check is a dependency too, so it works on a handler, an action or a page. A role that
does not exist is refused, and there is a test for that case.

```python filename="src/routes/admin/users/index.py"
from nexy.decorators import UseGuard
from nexy_auth import require_role


@UseGuard(require_role("admin"))
async def GET():
    return {"ok": True}
```

## 5. Read the session in a client island

The same hooks are planned for React, Vue, Svelte, Solid and Preact. nexy-auth has no frontend
dependency; each framework gets a thin adapter.

```tsx filename="src/components/UserMenu.tsx"
import { useSession } from "nexy-auth/react";

export function UserMenu() {
  const { user, signOut } = useSession();

  if (!user) {
    return <a href="/sign-in">Sign in</a>;
  }

  return (
    <div>
      <span>{user.email}</span>
      <button onClick={() => void signOut()}>Sign out</button>
    </div>
  );
}
```

The import path and hook name are proposed, not available. External clients use the
[HTTP contract](../reference/http-contract.md) instead; that contract does not replace the native
path shown here.

## What is hostile input here?

The implementation tests must cover a cookie without HttpOnly, a revoked session, a role the member
does not have, a body over the limit and a redirect to another site. Each case gets a test that
asserts the refusal before the behaviour is called done.

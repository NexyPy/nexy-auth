## What changed

One sentence. Name the behaviour, not the files.

## Why

Link the issue. Say what problem this solves for a person using Nexy.

## Verification

Paste the output of these two commands:

```text
uv run python scripts/verify.py
pnpm --dir client run verify
```

If a gate was skipped, say which one and why. A skipped gate is not a pass.

## Checklist

- [ ] The test was written before the code.
- [ ] Every added line of `src/nexy_auth/` runs in a test and every branch is taken.
- [ ] Hostile inputs have their own security tests.
- [ ] No character a person does not type appears in code, docs or this description.
- [ ] No AI tool or agent is named as an author, a co-author or a generator.
- [ ] Every identifier, comment and sentence is in English.
- [ ] The commit is one unit and its message says why.
- [ ] The maintainer, not the author, will review and merge this pull request.

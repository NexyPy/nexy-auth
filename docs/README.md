# nexy-auth documentation

**Authentication for Nexy apps, designed before any code is written.**

nexy-auth is in design phase. These docs describe the API being written in the issues of this
repository and name the decision that is still open. Nothing is published yet, so no page here shows
an install command or a running example.

Start with [What is nexy-auth?](getting-started/what-is-nexy-auth.md), then read the
[planned API](reference/planned-api.md) and the
[HTTP contract for external clients](reference/http-contract.md).

## Getting started

| Page | What you will learn |
|---|---|
| [What is nexy-auth?](getting-started/what-is-nexy-auth.md) | What the module covers and why Nexy needs it |
| [How do I add nexy-auth to a Nexy project?](getting-started/add-to-a-project.md) | The planned `nx add` and `nx migrate` commands |
| [How do I use the nexy-auth API in a project?](getting-started/use-the-api-in-a-project.md) | Configuration, handler dependency, guard and client hooks |
| [Which features come first?](getting-started/which-features-come-first.md) | The first version and the issues behind it |

## Concepts

| Page | What you will learn |
|---|---|
| [How do sessions work?](concepts/sessions.md) | Database sessions, cookies, rotation and revocation |
| [How do organizations and roles work?](concepts/organizations-and-roles.md) | Members, invitations and the permission check |

## Reference

| Page | What you will learn |
|---|---|
| [What will the nexy-auth API look like?](reference/planned-api.md) | Configuration, dependency, guard, hooks, plugins and tables |
| [How can an external client call nexy-auth?](reference/http-contract.md) | The HTTP contract being defined in issue 6 |

## Contributing

| Page | What you will do |
|---|---|
| [How do I write a page in these docs?](contributing/writing-docs.md) | Follow the search, language and character rules |
| [Which bot accounts act for Nexy?](contributing/bot-identities.md) | Give every Nexy-owned bot the Nexy logo avatar |

## Layout

```text
docs/
- README.md                  this index
- getting-started/           what the module is, how to add it, how to use it, what comes first
- concepts/                  sessions, organizations and roles
- reference/                 planned API and HTTP contract
- contributing/              rules for writing a page and bot identities
- assets/                    the Nexy logo for a GitHub App badge
```

## Status of a page

Every page either describes a decision already written in an issue or names the issue that has to
decide it. A page never presents a planned name as a working one. When the first version ships, the
planned pages are rewritten against the code and this note is removed.

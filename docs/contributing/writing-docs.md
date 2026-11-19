# How do I write a page in these docs?

Write plain Markdown in `docs/`, one question per page, in English, with only characters a person
types. This repository has no docs site generator and no translation step.

## What makes a good page?

- The title is the question a person types in a search.
- The first paragraph answers that question in one sentence. A reader looking for one answer gets it
  before any heading.
- The headings and the file name reuse the words of the title.
- A page answers one question. A second page on the same words would compete with the first.
- A table in `docs/README.md` lists the page with the question and what the reader will do.

## What language and characters are allowed?

Every identifier, comment and sentence is in English. Use only characters typed on an English or
French keyboard. No emoji, no em dash, no arrow, no curly quote and no box drawing. A Markdown list
uses a hyphen. `scripts/check_human_characters.py` checks tracked files, staged files and commit
messages.

## What about a plan?

The module is in design phase. A page names the issue that decides a point and never writes a planned
name as a working one. When code ships, the page is rewritten against the code in its own commit.

## What is the workflow?

1. Research with primary sources and verify with a command.
2. Write the page in English and link it from `docs/README.md`.
3. Run `python scripts/check_human_characters.py` and `uv run python scripts/verify.py`.
4. Open one pull request per page. The maintainer reviews and merges it.

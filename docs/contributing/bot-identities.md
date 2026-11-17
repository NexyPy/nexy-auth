# Which bot accounts act for Nexy?

Every bot account that acts for Nexy uses the Nexy logo as its avatar. An owner of a GitHub App can
upload the logo as the app badge. GitHub-owned bots such as Dependabot and github-actions keep their
own avatar because GitHub does not let a repository change it.

## What the rule covers

| Bot | Who owns it | Avatar |
|---|---|---|
| A Nexy GitHub App | Nexy | Nexy logo, uploaded as the app badge |
| Dependabot | GitHub | GitHub avatar, not configurable from a repository |
| github-actions | GitHub | GitHub avatar, not configurable from a repository |
| Vercel, Netlify and other installed apps | Third party | Their own avatar, not ours to change |

## How to set the badge on a Nexy GitHub App

The asset is [nexy-bot-avatar.png](../assets/nexy-bot-avatar.png), a 200 by 200 PNG made from the
Nexy favicon at `sites/vanilla/assets/favicon.svg` in the main repository. GitHub recommends 200 by
200 pixels for an app badge.

1. Open the organization settings, then Developer settings, then GitHub Apps.
2. Edit the app and open Display information.
3. Upload the PNG as the logo and crop it if needed.
4. Set the badge background color to the Nexy dark color, `#0a0a0a`.
5. Save the change and check the avatar in a pull request or a comment.

## What must not happen

- Do not create a bot account to impersonate Dependabot or github-actions. They are GitHub identities.
- Do not upload a different logo to a Nexy bot, and do not leave the generated identicon in place.
- Do not commit a GitHub App private key or an installation token to this repository.

## Where the rule is enforced

AGENTS.md in this repository and in the main Nexy repository states the rule. A review checks that a
new bot owned by Nexy uses the logo before the app is added to a workflow.

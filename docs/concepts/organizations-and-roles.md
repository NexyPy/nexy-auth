# How do organizations and roles work?

nexy-auth plans to group users in organizations, invite members and check their roles before a
protected action runs. The scope is defined in issue 5. This page describes the decision, not a
shipped API.

## What is an organization?

An organization is the boundary for members and roles. A user can belong to more than one
organization, with a different role in each.

## What is a role check?

A role check is a permission test callable from a handler, an action and a layout. It answers one
question: does this member have the role this action requires? The plugin interface in issue 1 must
allow a new role without editing a switch.

## What is an invitation?

An invitation records who was invited, to which organization and with which role. The first version
covers invitations as part of issue 5.

## What is hostile input here?

A check must refuse a user who is not a member, a role that does not exist and an invitation used by
a different account. Each case needs a test that asserts the refusal.

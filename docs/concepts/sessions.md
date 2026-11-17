# How do sessions work?

nexy-auth plans to keep sessions in the database and send their identifier in an HttpOnly cookie,
with rotation and revocation. This is a design decision in issue 2, not a shipped interface.

## Why database sessions?

A database session can be revoked from the server, listed as an active device, and invalidated when a
password changes. A stateless token cannot be revoked without extra state, so it does not meet the
same requirement.

## What happens at sign-in?

The plan, as written in issue 2, is:

1. Verify the email and password with Argon2id hashing.
2. Create a session row in the database the project already uses.
3. Set the session identifier in an HttpOnly cookie.
4. Apply the sign-in rate limit.

## What does rotation mean?

Rotation replaces the session identifier on a privileged action. The old identifier stops working.
The aim is to limit the time a stolen cookie can be used.

## What does revocation mean?

Revocation removes a session from the database. A revoked session fails on the next request, and the
person sees it in the list of active devices.

## What is hostile input here?

The implementation tests must send a cookie without HttpOnly, a session identifier that was revoked,
a body over the limit, a redirect to another site and a call from another origin. Each one gets its
own test that asserts the refusal.

# AzerothCore Merge process

### PRs merge rate

At AzerothCore, we merge only a few PRs daily, picking them from the [[To Be Merged]](https://github.com/azerothcore/azerothcore-wotlk/pulls?q=is%3Apr+is%3Aopen+label%3A%22To+Be+Merged%22) list.

Everyday we pick the oldest PRs to merge, unless there are more urgent PRs that need to be merged first for any reason.

Users can request the AC Staff to give a PR a higher priority if they really need to have it merged soon, we are quite flexible with that (ex: a hook).

This process might appear "slow", however there are reasons for that:

- Everyone has the possibility to review PRs before they get merged into master, stability is important for us.

- Testers and developers can still have a chance to say "no guys, don't merge this yet! I've just found an unexpected bug with this PR" before it gets finally merged.

- We have a very strict process of accepting PR (we require at least 1 code review approval and 1 manual tester approval), but it can always happen that bugs get to master branch. 
If we merge too many PRs at once, it's hard to understand which one of them was faulty. 
Merging a low amount of PRs per day enables us to quickly identify faulty commits and fix/revert them as soon as possible.

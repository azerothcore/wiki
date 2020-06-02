# AzerothCore Merge process

### PRs merge rate

At AzerothCore we merge only a few PRs daily (usually 1 or 2 per day), picking them from the [[To Be Merged]](https://github.com/azerothcore/azerothcore-wotlk/pulls?q=is%3Apr+is%3Aopen+label%3A%22To+Be+Merged%22) list.

Everyday we pick the oldest PRs to merge, unless there are more urgent PRs that need to be merged first for any reasons.

Users can request to the AC Staff to give a PR a higher priority if they really need to have it merged soon, we are quite flexible with that.

This process might appear too "slow" to someone, however there are several reasons for that:

- Provides a constant activity on the master branch, so people can regularly plan to update their servers knowing that the amount of changes in a certain window of time it's going to be always more or less the same.

- Everyone has the possibility to review PRs before they get merged into master, stability is important for us.

- Despite we have a very strict process of accepting PR (we require at least 1 code review approval and 1 manual tester approval), 
it can always happen that bugs get to master branch. 
If we merge too many PRs at once, it's hard to understand which one of them was faulty. 
Merging a low amount of PRs per day enables us to quickly identify faulty commits and fix/revert them asap.

---
redirect_from: "/Live-e2e"
---

# Live e2e tests

AzerothCore can run **live end-to-end tests** on a real 3.3.5a realm. They are protocol clients, not a stub of the core and not a dry-run of worldserver.

The bots come from [AzerothGhost](https://github.com/azerothcore/AzerothGhost). They log in through auth, enter the world, and drive the same opcodes a retail client uses (login, teleports, casts, combat, quests, loot, and so on). Assertions look at the protocol, the object cache, and sometimes the character DB.

This does **not** replace [testing a PR in game](how-to-test-a-pr). It is extra coverage on the live stack, mainly so a PR cannot merge while a player-visible path is already broken.

## What CI does

On a pull request against `azerothcore/azerothcore-wotlk` (not forks, not drafts):

1. The usual `nopch-build` job compiles real `authserver` and `worldserver` (ubuntu-24.04, clang-18, no PCH) and uploads those binaries.
2. The `e2e full` job starts MySQL and applies the normal AC database and client-data setup.
3. It boots **those same binaries**. `worldserver` listens on 8085, `authserver` on 3724. The job waits until both ports accept connections.
4. It runs `go test -tags=e2e` from `e2e/` against that realm.

So the pipeline runs a **full** AC stack from the PR's binaries, then talks to it as a client. There is no partial worldserver and no mocked combat.

A comment in the workflow about "dry-run" is only about the CMake/compile path. The tests themselves always hit a live process.

Merge to `master` keeps the clang-18 build and does **not** run the suite again. Official CI already ran it on the PR.

You can also start the suite by hand with `workflow_dispatch` (`scope=full` or `scope=smoke`).

## What the tests are

They live in the AzerothCore repo under `e2e/` (`smoke/` and `suites/`). They import the harness from [AzerothGhost](https://github.com/azerothcore/AzerothGhost) (`e2e/e2eharness`).

Typical flow:

1. Create a GM test account and a character.
2. Log in and wait until the session is in the world.
3. Place the bot (named tele, pad, or `.go creature`).
4. Optionally prepare combat (`.gm off`, cheats, PvP flag).
5. Drive a real client action (cast, pull, trade, relog, …).
6. Assert something a player would see (aura gone, HP dropped, still on the bridge, next wave not early, world still alive).

Setup may use GM commands. The oracle should be the player-visible result, not "the GM command returned".

Open core bugs stay commented out with `OPEN(e2e)` and an issue link. They are not compiled, so they cannot soft-pass.

## How to run them locally

You need a running authserver, worldserver, and MySQL, plus Go 1.26+.

```bash
cd e2e
cp .env.example .env   # edit auth addr + DSNs
set -a; source .env; set +a
go test -tags=e2e ./... -count=1 -v -timeout 120m -parallel 1 -p 1
```

Without `-tags=e2e`, `go test ./...` skips these packages.

Keep `-parallel 1 -p 1` unless you know each concurrent package has its own isolation pad. Sharing a pad makes bots thrash each other.

Authoring details: `e2e/README.md` in the core repo, plus AzerothGhost [`LLM_GUIDE.md`](https://github.com/azerothcore/AzerothGhost/blob/main/e2e/LLM_GUIDE.md) and [`EXAMPLES.md`](https://github.com/azerothcore/AzerothGhost/blob/main/e2e/EXAMPLES.md).

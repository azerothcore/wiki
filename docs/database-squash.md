---
redirect_from: "/Database-squash"
---

# Database Squash

## Introduction

### What is the Database squash

The DB-squash is a procedure where we merge all the DB updates into the base files.

So, all files from:

- [data/sql/updates](https://github.com/azerothcore/azerothcore-wotlk/tree/master/data/sql/updates)

Will be squashed into:

- [data/sql/base](https://github.com/azerothcore/azerothcore-wotlk/tree/master/data/sql/base)

And also a copy of them will be kept inside:

- [data/sql/archive](https://github.com/azerothcore/azerothcore-wotlk/tree/master/data/sql/archive)

During this process we also issue a new project release (e.g. `1.0.0`, `2.0.0`, etc...).

### Why we need it

The files in [data/sql/updates](https://github.com/azerothcore/azerothcore-wotlk/tree/master/data/sql/updates) (mostly in `db_world`) can easily grow and become unhandy to have a huge list of updates.
Having a list of updates that is too long, or having some update files that are too big, can lead to issues or simply slowness when installing or updating the AzerothCore Database.

As a result of the DB squash:

- it will be faster to install and update an AzerothCore Database
- we prevent some common issues (e.g. `MySQL server has gone away...` while importing)

### When we do it

There is no fixed timetable. We typically do it once every 1 or 2 years, however we might do it sooner in case we need it.

## How to do it (for project maintainers)

1) **Commit** a new release by modifying the version in `acore.json` and in the `version` table of the DB world, removing `dev` [(example)](https://github.com/azerothcore/azerothcore-wotlk/commit/2742a2ed37bec33544ca496b883ed50d6a50693e)

2) Wait that the pending update file fromt the previous commit is been processed by the bot [(example)](https://github.com/azerothcore/azerothcore-wotlk/commit/1fc22a74088e235e78fa02decbaf0864899477d7).
   Now draft a new release on GitHub. **NOTE**: this will be the "release commit".

3) Now pull and update your local DB to the latest version. **IMPORTANT: Make sure your DB is perfectly clean.**
  It's better to destroy it and install a fresh one at this point. Do **NOT** commit anything until specified.

4) Do the actual squash action, by using the script located at `bin/acore-db-export`. This will basically backup your DBs into the base files.

5) Move the ` data/sql/updates/db_*` folders under a new folder inside `data/sql/archive` having the name of the release (e.g. 6.x)

6) Start a new development version by modifying the version in `acore.json` and in the `version` table of the DB world, adding the `dev` suffix to the next version

7) Commit the changes from steps 4-6 together [(example)](https://github.com/azerothcore/azerothcore-wotlk/commit/0858526c9a678e90ffa830182c25434b36fee2c5)

8) Add new pending files [(example)](https://github.com/azerothcore/azerothcore-wotlk/pull/10292/commits/71f7023e1917ab7123118d4d65933dadcbe66d19)

9) Announce to the users that a new release is available so they have to update their DBs following a special procedure (see below)

## How to update an existing server from a previous release

The existing servers will have to:

- `git pull`
- Startup `authserver` and `worldserver` with config options
```ini
###################################################################################################
# UPDATE SETTINGS
#
#    Updates.EnableDatabases
#        Description: A mask that describes which databases shall be updated.
#
#        Following flags are available
#           DATABASE_LOGIN     = 1, // Auth database
#           DATABASE_CHARACTER = 2, // Character database
#           DATABASE_WORLD     = 4, // World database
#
#        Default:     7  - (All enabled)
#                     4  - (Enable world only)
#                     0  - (All disabled)

Updates.EnableDatabases = 7

#
#    Updates.AutoSetup
#        Description: Auto populate empty databases.
#        Default:     1 - (Enabled)
#                     0 - (Disabled)

Updates.AutoSetup   = 1

#
#    Updates.Redundancy
#        Description: Perform data redundancy checks through hashing
#                     to detect changes on sql updates and reapply it.
#        Default:     1 - (Enabled)
#                     0 - (Disabled)

Updates.Redundancy  = 1

#
#    Updates.ArchivedRedundancy
#        Description: Check hashes of archived updates (slows down startup).
#        Default:     0 - (Disabled)
#                     1 - (Enabled)

Updates.ArchivedRedundancy = 0

#
#    Updates.AllowRehash
#        Description: Inserts the current file hash in the database if it is left empty.
#                     Useful if you want to mark a file as applied but you don't know its hash.
#        Default:     1 - (Enabled)
#                     0 - (Disabled)

Updates.AllowRehash = 1

#
#    Updates.CleanDeadRefMaxCount
#        Description: Cleans dead/ orphaned references that occur if an update was removed or renamed and edited in one step.
#                     It only starts the clean up if the count of the missing updates is below or equal the Updates.CleanDeadRefMaxCount value.
#                     This way prevents erasing of the update history due to wrong source directory state (maybe wrong branch or bad revision).
#                     Disable this if you want to know if the database is in a possible "dirty state".
#        Default:     3 - (Enabled)
#                     0 - (Disabled)
#                    -1 - (Enabled - unlimited)

Updates.CleanDeadRefMaxCount = 3

#
###################################################################################################
```

Example: [Upgrade-from-pre-2.0.0-to-latest-master](https://www.azerothcore.org/wiki/Upgrade-from-pre-2.0.0-to-latest-master)


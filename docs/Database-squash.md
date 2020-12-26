## Database squash Introduction

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

The only drawback of this procedure is that, every time the DB gets squashed, existing servers will have to follow a (little) special procedure to update their database (see below).

### When we do it

There is no fixed timetable. We typically do it once every 1 or 2 years, however we might do it sooner in case we need it.

## How to do it (for project maintainers)

During this process NO ONE should push anything to the master branch.

1) **Commit** a new release by modifying the version in `acore.json` and in the `version` table of the DB world, removing `dev` [(example)](https://github.com/azerothcore/azerothcore-wotlk/commit/2742a2ed37bec33544ca496b883ed50d6a50693e)

2) Wait that the pending update file fromt the previous commit is been processed by the bot [(example)](https://github.com/azerothcore/azerothcore-wotlk/commit/1fc22a74088e235e78fa02decbaf0864899477d7).
   Now draft a new release on GitHub. **NOTE**: this will be the "release commit".

3) Now pull and update your local DB to the latest version. **IMPORTANT: Make sure your DB is perfectly clean.**
  It's better to destroy it and install a fresh one at this point. Do **NOT** commit anything until specified.

4) Do the actual squash action, by using the script located at `bin/acore-db-export`. This will basically backup your DBs into the base files.

5) Move the ` data/sql/updates/db_*` folders under a new folder inside `data/sql/archive` having the name of the release (e.g. 2.x)

6) Start a new development version by modifying the version in `acore.json` and in the `version` table of the DB world, adding the `dev` suffix to the next version

7) Commit the changes from steps 4-6 together [(example)](https://github.com/azerothcore/azerothcore-wotlk/commit/0858526c9a678e90ffa830182c25434b36fee2c5)

8) Announce to the users that a new release is available so they have to update their DBs following a special procedure (see below)

## How to update an existing server from a previous release

The existing servers will have to:

- `git pull`
- Checkout the release commit (`git checkout COMMIT_HASH`)
- Update their DB following the standard procedure
- Checkout the latest master version (`git pull` again)
- Update their DB following the standard procedure (yes, again)

Example: [Upgrade-from-pre-2.0.0-to-latest-master](https://www.azerothcore.org/wiki/Upgrade-from-pre-2.0.0-to-latest-master)


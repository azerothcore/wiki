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

The only drawback of this procedure is that, every time the DB gets squashed, existing servers will have to follow a (little) special procedure to update their database (see below).

### When we do it

There is no fixed timetable. We typically do it once every 1 or 2 years, however we might do it sooner in case we need it.

## How to do it (for project maintainers)

1) Wait that the any existing pending update file is been processed by the bot [(example)](https://github.com/azerothcore/azerothcore-wotlk/commit/d9449c7a9954c3b973153dc5bf06a441c9036cb4).
   Now draft a new release on GitHub. **NOTE**: this will be the "release commit".

2) Now pull and update your local DB to the latest version. **IMPORTANT: Make sure your DB is perfectly clean.**
  It's better to destroy it and install a fresh one at this point. Do **NOT** commit anything until specified.

3) Do the actual squash action, by using the script located at `bin/acore-db-export`. This will basically backup your DBs into the base files.

4) Move the `data/sql/updates/db_*` folders under a new folder inside `data/sql/archive/db_*` having the name of the release (e.g. 2.x)

5) Start a new development version by modifying the version in `acore.json` and in the `version` table of the DB world, adding the `dev` suffix to the next version

6) Need set all updates state to `ARCHIVED`. Create new `.sql` file (**WITH** pending system) in `./data/sql/updates/pending_db_*`. For `db_world` need update `db_version` and `cache_id`.

Example for `auth`:
```sql
-- ACDB 335.5-dev auth
UPDATE `updates` SET `state`='ARCHIVED';
```

Example for `characters`:
```sql
-- ACDB 335.5-dev characters
UPDATE `updates` SET `state`='ARCHIVED';
```

Example for `world`:
```sql
-- ACDB 335.5-dev world
UPDATE `version` SET `db_version`='ACDB 335.5-dev', `cache_id`=5 LIMIT 1;
UPDATE `updates` SET `state`='ARCHIVED';
```

## How to update an existing server from a previous release

The existing servers will have to:

- `git pull`
- In config files (`authserver.conf` and `worldserver.conf`) just set `Updates.EnableDatabases` for all DB.
- These options are already enabled by default, you do not need to do anything if you have not touched them 
- For `worldserver.conf` - `Updates.EnableDatabases = 7`
- For `authserver.conf` - `Updates.EnableDatabases = 1`

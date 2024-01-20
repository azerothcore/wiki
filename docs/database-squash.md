---
redirect_from: "/Database-squash"
---

# Database Squash

## Introduction

We do this to update the base files so that a clean install of the server is done quicker and all update files are not needed to be run, as they will already exist in the base files.

## How to

{% include caution.html content="These steps are only for project maintainers who intend to update base files." %}

{% include important.html content="No SQL changes should be merged during the Base Squash." %}

We ONLY squash into BASE files. We never move files.
ARCHIVE dir is UNUSED.
All update files ALWAYS exist in the updates dir.

as the `updates` table in base files always will contain the entries from the updates dir they will never be run again on a clean setup. 

How to do the squash.

{% include important.html content="A squash needs to be done on a clean database. Drop all tables in Auth, Characters and World." %}

1. Update the acore.json file. Increment version by one
2. Create a new file in the updates/db_world/ dir, the file should be incremented containing

{% include note.html content="It should NOT be placed as a pending update and should only be done on world db. This is because we want the updated DB version to follow into the base files" %}

```sql
UPDATE `version` SET `db_version`='ACDB 335.11-dev', `cache_id`=11 LIMIT 1;
```
{% include note.html content="Remember to increment the db_version and cache_id the same as acore.json" %}

4. Drop all your databases, and run Worldserver to populate a clean database.
5. Export the databases using i.e HeidiSQL

{% include important.html content="Set the following values
</br>> Tables -> DROP + CREATE
</br>> Data -> Delete + insert (truncate existing data)
</br>> Max INSERT size -> 1024
</br>This is so that no unexpected issues occur." %}

6. Move the exported table files into the base directory to update the existing files.
7. Make a PR

{% include important.html content="See https://github.com/azerothcore/azerothcore-wotlk/pull/18197 as a reference how to squash into Base files." %}

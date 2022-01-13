---
redirect_from: "/Update"
---

# How to update AzerothCore to the latest stable version

## Verify that you're on the latest release

1. Type `.server debug` in your console.
  
    1. If it outputs `Using World DB: ACDB 335.4-dev` then you can proceed to [Update your local source](#update-your-local-source).
  
    1. If it outputs anything else for `Using World DB:` then you first need to follow [this guide on updating to latest master](upgrade-from-pre-3.0.0-to-latest-master.md).

We'd also highly recommend following the #announcements channel on the AzerothCore discord so you'll know about any other important changes to AzerothCore.

## Update your local source

Move to your AzerothCore sources directory.

- If you have your own fork of AzerothCore, you need to update from latest master branch.

- Otherwise, if you cloned AzerothCore directly from the main repo, you have to `git pull` to update it.

## Recompile

Compile again your sources, this step is the same as the [Compilation step during Installation](Installation#3-compiling), but generally you can skip the CMake part unless you're adding new modules.

For example, in Linux/Mac you just have to `cd build;` and run `make -j 8; make install`. Of course you can change the value of the `-j` paramether according to your CPU.

## Update the Database

**If you are updating your production environment, BACKUP your databases BEFORE updating them!**

You need to import the **new** sql update files (located at https://github.com/azerothcore/azerothcore-wotlk/tree/master/data/sql/updates) to each database.

To automate this process you can use the db-assembler bash script `bash apps/db_assembler/db_assembler.sh`.

If this is the first time you are using it [READ THIS FIRST](database-installation.md) and properly configure your `conf/config.sh` file.

![](https://user-images.githubusercontent.com/75517/50738699-6912ee80-11d7-11e9-95ea-667baa0bda70.png)

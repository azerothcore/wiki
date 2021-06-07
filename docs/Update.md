# How to update AzerothCore to the latest stable version

## 1) Verify that you're on the latest release
Check the [releases](https://github.com/azerothcore/azerothcore-wotlk/releases) page on the azerothcore-wotlk github page to see if there has been a new release since you last upgraded. If there has been a new release, follow the upgrade instructions to update to the latest release. **The next steps will not work properly unless you are on the latest release.**

We'd also highly recommend following the #announcements channel on the AzerothCore discord so you'll know about any other important changes to AzerothCore.

## 2) Update your local sources

Move to your AzerothCore sources directory.

- If you have your own fork of AzerothCore, you need to [sync it](Syncing-your-fork).

- Otherwise, if you cloned AzerothCore directly from the main repo, you have to `git pull` to update it.

## 3) Recompile

Compile again your sources, this step is the same as the [Compilation step during Installation](Installation#3-compiling), but generally you can skip the CMake part unless you're adding new modules.

For example, in Linux/Mac you just have to `cd build;` and run `make -j 8; make install`. Of course you can change the value of the `-j` paramether according to your CPU.

## 4) Update the Database

**If you are updating your production environment, BACKUP your databases BEFORE updating them!**

You need to import the **new** sql update files (located at https://github.com/azerothcore/azerothcore-wotlk/tree/master/data/sql/updates) to each database.

To automate this process you can use the db-assembler bash script `bash apps/db_assembler/db_assembler.sh`.

If this is the first time you are using it [READ THIS FIRST](https://www.azerothcore.org/wiki/database-installation) and properly configure your `conf/config.sh` file.

![](https://user-images.githubusercontent.com/75517/50738699-6912ee80-11d7-11e9-95ea-667baa0bda70.png)

---
redirect_from: "/Update"
---

# How to update AzerothCore to the latest stable version


**NOTE: THIS IS NOT UP TO DATE. SEE DISCORD ANNOUNCEMENT CHANNEL ON WHICH COMMIT TO CHECKOUT!**


## Verify that you're on the latest release

1. Type `.server debug` in your console.
  
    1. If it outputs `Using World DB: ACDB 335.7-dev` then you can proceed to [Update your local source](#update-your-local-source).
  
    1. If it outputs anything else for `Using World DB:` then you first need to follow [this guide on updating to latest master](upgrade-from-pre-3.0.0-to-latest-master.md).

We'd also highly recommend following the #announcements channel on the AzerothCore discord so you'll know about any other important changes to AzerothCore.

## Update your local source

Move to your AzerothCore sources directory.

- If you have your own fork of AzerothCore, you need to update from latest master branch.

- Otherwise, if you cloned AzerothCore directly from the main repo, you have to `git pull` to update it.

## Recompile

Compile your source again, this step is the same as the [compilation step during installation](Installation#3-compiling), but generally you can skip the CMake part unless you're adding new modules.

For example, in Linux/Mac you just have to `cd build;` and run `make -j 8; make install`. Of course you can change the value of the `-j` parameter according to your CPU.

## Update the Database

**If you are updating your production environment, BACKUP your databases BEFORE updating them!**

You need to import the **new** sql update files (located at https://github.com/azerothcore/azerothcore-wotlk/tree/master/data/sql/updates) to each database.

To automate this process, both the authserver and worldserver have database updaters inside of them as described [here](https://www.azerothcore.org/wiki/database-installation). This means that once you recompile your source, all you'd need to do is launch the authserver and worldserver as you would normally.

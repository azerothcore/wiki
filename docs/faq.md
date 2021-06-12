---
redirect_from: "/FAQ"
---

# Frequently Asked Questions

If you have trouble installing or compiling AzerothCore read [Common Errors](common-errors.md).

| Did this FAQ not answer your questions? Read [How to ask for help](how-to-ask-for-help.md) on how to proceed with your question in the best way. |
| --- |

## General-related FAQ

- What operating systems/platforms are supported?
  - Currently, Windows, macOS, Linux and Docker are supported.

- When should I update my source?
  - We recommend updating your core frequently, at least once a week, in order to benefit of latest core fixes and security patches.

- How much RAM do I need for AzerothCore?
  - You can find all RAM information [here](Memory-Usage.md).

- What is "Blizzlike"?
  - AzerothCore is trying to replicate the Blizzard state for World of Warcraft. The term "Blizzlike" means that it is close enough to being a replication of what was on the Blizzard servers.

- Why does AzerothCore not mimic "blizzlike" bugs or exploits?
  - Although we strive to provide blizzlike content we also value user experience. This means that we sometimes fix bugs or exploits which existed during retail at the time to provide a better overall experience for the players.

- How can I contribute?
  - You can help fixing issues by submitting Pull Requests, read more [here](contribute.md).
  - You can help us by testing our [Pull Requests](contribute#how-to-test-a-pull-request) and participating on the [github issues' discussions](https://github.com/azerothcore/azerothcore-wotlk/issues).
  - You can put bounties (money) on issues or suggestions that you want fixed using bountysource. Learn more here: [Bountysource](bountysource.md)
  - You can help improve the wiki by submitting a [Pull Request](https://github.com/azerothcore/wiki).

- Why do you not merge my fix?
  - All fixes must be reviewed by a dev. All devs don't know everything, so you need to wait until someone reviews it.
  - Some fixes requires testing and not all devs can test so you need to wait on someone else to test it.
  - They get merged eventually after getting the To Be Merged label.
  - Maybe you are not following the [SQL/C++ standards](https://www.azerothcore.org/wiki/standard-operating-procedure).
  - Read more in [Merge Process](merge-process.md).

- How do I report a crash?
  - By pasting your crashlog into a PasteBin or Gist.
  - The crashlog **needs to come from a RelWithDebInfo or Debug compilation**. If it is from Release it is useless.
  - [How to Restart and Debug](how-to-restart-and-debug.md).

- Do you support Repacks based on AzerothCore?
  - No. Compile the code yourself if you want support.

## Database-related FAQ

- How often do you update the database?
  - The database is updated nearly every day.

- How do I update the database?
  - You can find everything you need to keep the database up-to-date in this guide on [Database Keeping the Server Up-to-Date](database-keeping-the-server-up-to-date.md).

## Core-related FAQ

- When will the source be stable?
  - Soon...™
  - We do our best to keep the master branch stable and playable. We never push code directly into the master branch, but rather we first require everyone (including AC admins and staff) to first open a PR so everyone is able check them before they got merged into master.
  - Please help us by [testing PRs](https://www.azerothcore.org/wiki/How-to-test-a-PR) and reporting any bugs you may find.

- I can't run the extractors on Windows-platforms, it just disappears when I click on it?
  - Understand that it is a **commandline** tool, not a GUI-tool. This means you need to use the commandline in Windows (for example "Command prompt") instead of just doubleclicking on it. 

- Why can't I run my older MAP/DBC extractors?
  - They are updated for a reason, and will give you errors when you start the Worldserver if you do not extract with the latest version.
  - You will always get the latest version if you compile with "TOOLS".

- What are Maps, VMaps, MMaps and DBCs?
  - **Note that AzerothCore does not support and does not condone any form of modification to client files or private / public servers! AzerothCore in itself is meant for theory-crafting and learning.**
  - Beside the core as binaries which give a fundamental and the individual client interpreting functions, definitions and commands, the core can be described as 'a body' with the following data forming it's 'anatomy':
    - **Maps**: Maps are **required to run AzerothCore**. Maps provide the physical values and data for the core to interpret. Based on these, the core has a layout that can be compared with each client. This includes area definitions.
    - **VMaps**: VMaps are **optional, but highly recommended**. VMaps ("Virtual Maps") calculate the possibility of line-of-sight, as an example. Based on their content, the server can (for example) calculate if spell casts are possible (e.g. if a wall is in between the target and caster or not).
    - **MMaps**: MMaps are optional, but recommended. To further physical boundaries, MMaps ("Movement Maps") enforce physical boundaries on non-player characters, e.g. NPCs, as their collision is not handled by the client. They also improve path generation.
    - **DBC**: DBCs are **required to run AzerothCore**. The DBCs ("Data Base Client [Files]") give essential values that the World of Warcraft client interprets. They define races, textures, local models and more. AzerothCore interprets these and loads them up.
  - Compiling AzerothCore with "TOOLS" will always create the necessary tools to extract and create these files.

- I have issues with extracting Maps, VMaps, MMaps, DBCs (and I've tried using older versions of the extractors) - what is wrong?
  - The older tools are deprecated and will not work.
  - You are required to use a commandline to be able to run the tools.

- I am missing the libraries for MySQL and can't seem to find them in the repository?
  - The library is called "mysql.lib" and is not provided by AzerothCore.
  - Make sure you installed your MySQL-Server with DEVELOPMENT HEADERS.
  - You can follow the [Core Installation](core-intallation.md) guide to find the libraries.

- I am missing the libraries for OpenSSL and can't seem to find them in the repository?
  - For OpenSSL versions prior to 1.1.0 they will be named "libeay32.dll" and "ssleay32.dll".
  - For OpenSSL versions 1.1.0 and more recent they are called:
    - For 32bit installs: "libssl-1_1.dll" and "libcrypto-1_1.dll".
    - for 64bit installs: "libssl-1_1-x64.dll" and "libcrypto-1_1-x64.dll"
  - You can follow the [Core Installation](core-intallation.md) guide to find the libraries.

## Debug-related FAQ

- How can I get a good crashlog on Windows?
  - Compile your core in RelWithDebInfo or Debug. A crashlog from Release will be useless.
  - You can debug it yourself if you [Run worldserver and autherserver in Visual Studio](run-worldserver-and-authserver-in-visual-studio.md)

## Module-related FAQ

- I need a new hook for my custom module, what can I do?
  - You can add the hook to your own fork (cf: [Create a new Hook](create-a-new-hook.md)) and create a new Pull Request to the official repository so we can validate it and merge it.

- Is it possible to turn a core patch into a module?
  - Yes. [Is it possible to turn a core patch into a module for AzerothCore? - StackOverflow](https://stackoverflow.com/questions/66340549/is-it-possible-to-turn-a-core-patch-into-a-module-for-azerothcore/66340683#66340683)

## Feature-related FAQ

- What instances/arenas/battlegrounds are working?
  - Most of them are working perfectly, some are working worse.
  - The Core is always being worked on, the most accurate data will come from you trying them yourself.

- Does Warden work?
  - Yes it does, but not with 100% sucess rate. Warden does not detect all hacks, not even on Retail.

- How do I close an instance or battleground? How can I disable a spell?
  - All disabling is handled in the [disables table](https://www.azerothcore.org/wiki/disables).

| Did this FAQ not answer your questions? Read [How to ask for help](how-to-ask-for-help.md) on how to proceed with your question in the best way. |
| --- |

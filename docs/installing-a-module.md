# Installing a Module

| Installation Guide |
| :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 8: Client Setup](client-setup.md) |

By default AzerothCore delivers a Blizzlike experience. This can however be altered in different ways by adding Modules.

## Installing the Module

1. Find a module of your needs in the [AzerothCore Catalogue](https://www.azerothcore.org/catalogue#/).
2. Clone the repository
    - Clone the repositroy using Git the same way AzerothCore was first cloned in the [Core Installation](core-installation.md). The repository should be cloned into the \modules\ directory. i.e E:\AzerothCore\modules\
    - Download the ZIP file from the catalogue and extract it in the \modules\ directory. i.e E:\AzerothCore\modules\mod-anticheat

**Note: If your module has a suffix i.e "-master". This needs to be removed in order for the module to work!**

## Recompiling

In order for your module to work you need to recompile the source. For an indepth guide how to recompile, read over [Core Installation](core-installation.md) again.

1. Reconfigure and regenerate CMake.
    - To make sure the module was correctly installed you can check if it can be found in the CMake logs under **\* Modules configuration (static)**

2. Rebuild the core.

Your Worldserver will automatically run any SQL Queries provided by the Modules.

You should always check the README file of the module to see if any manual steps are needed for the module to function properly.

## Common Errors

- During compiling I get the error "error LINK2019: unresolved external symbol "void __cdcel Addmod_module_masterScripts(void)"
    - Remove **-master** from the modules directory name.

- The module is for some reason not working in-game.
    - You can always use the **.server debug** command to see all loaded modules.
    - Always fall back to the README file from the module for exact installation steps for that module.

<br>

## Help

If you are still having problems, check:

* [FAQ](faq.md)

* [Common Errors](common-errors.md)

* [How to ask for help](how-to-ask-for-help.md)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide |
| :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 8: Client Setup](client-setup.md) |
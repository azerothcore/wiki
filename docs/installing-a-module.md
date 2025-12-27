# Installing a Module

| Installation Guide                                                                                                                   |
| :----------------------------------------------------------------------------------------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 8: Client Setup](client-setup)                                                                                              |

Adding a module is an optional step to alter the blizzlike gameplay offered by AzerothCore by default.

## Installing the Module

1. Find a module of your needs in the [AzerothCore Catalogue](https://www.azerothcore.org/catalogue#/).
2. Clone the repository
    - Clone the repository using Git the same way AzerothCore was first cloned in the [Core Installation](core-installation). The repository should be cloned into the \modules\ directory. i.e E:\AzerothCore\modules\
    - Download the ZIP file from the catalog and extract it in the \modules\ directory. i.e E:\AzerothCore\modules\mod-anticheat

{% include note.html content="If your module has a suffix i.e. -master. This needs to be removed in order for the module to work!" %}

## Recompiling

In order for your module to work you need to recompile the source. For an in-depth guide on how to recompile, read over [Core Installation](core-installation) again.

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
    - Always fall back to the README file from the module for the exact installation steps for that module.

<br>

## Help

{% include help.html %}

| Installation Guide                                                                                                                   |
| :----------------------------------------------------------------------------------------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 8: Client Setup](client-setup)                                                                                              |

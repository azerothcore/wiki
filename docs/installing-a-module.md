# Installing a Module

| Installation Guide                                                                                                                   |
| :----------------------------------------------------------------------------------------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 8: Client Setup](client-setup)                                                                                              |

AzerothCore offers a modular setup, which allows you to alter your experience in your needs, being by your own creation or others.

The advantange about this modular setup? Allows you to do changes to your core without actually changing the base core, which is one of many issues with "changes" to the core in other emulators, which may require you to it's own branch or even fork to operate.

Note that in cases that the core needs to be modified to suit a module, this is the same as it would be for other emulators, but this isn't the most commun example for AzerothCore, is the exception.

## Installing the Module

1. To find and choose a module you wish to use you can use [AzerothCore Catalogue](https://www.azerothcore.org/catalogue#/) or in [GitHub](https://github.com/search?q=&type=repositories) search function for AzerothCore or the [respective tags](https://www.azerothcore.org/catalogue#/how-to).

Be sure to read the instructions or readme files that come with the module.

2. Clone or download from the repository.
    - If you clone using Git, it would be the same as you did for [Core Installation](core-installation), but into your module's folder as example: `C:\azerothcore-wotlk\modules`

    - If you decide to manually download, for the case of Github, you click on the green button `<> Code` and `Download ZIP`, when you do this way, you will not be able to easily update it without maunully doing this everytime it has an update, you extract the contents into your module's folder as example: `C:\azerothcore-wotlk\modules`

{% include note.html content="If your module has a suffix i.e. -master. This needs to be removed in order for the module to work!" %}

## Recompiling

In order for your module to work you need to recompile the source. For an in-depth guide on how to recompile, read over [Core Installation](core-installation) again.

1. Reconfigure and regenerate CMake.

    - To make sure the module was correctly installed you can check if it can be found in the CMake logs under **\* Modules configuration (static)**

2. Rebuild the core.

    - If you face errors here can be many things, can 
    - If you get `error LINK2019: unresolved external symbol "void __cdcel Addmod_module_masterScripts(void)` you missed removing the branch name in the suffix e.g `-master` from the module folder.
    - The module is not up to date (core has changes that module hasn't updated to).
    - Your core is not up to date (the module has been updated but your current core hasn't).
    - You missed an insturction from the module.

3. Copying and renaming the module configuration files

Similiar how is done in [Server Setup](server-setup) phase, example below is for windows.

You will need to go in the `Build` folder you created, under `\bin\RelWithDebInfo\configs\modules` and make a copy and rename the copy to the following:
`ModuleName.conf.dist - Copy` to `ModuleName.conf`

And any changes you want to do the module (if any), you know change `ModuleName.conf` not the `ModuleName.conf.dist`.

4. SQL Requirements

    - If the module you're using has the same strucuture for example: `data\sql\db-DatabaseName` as [skeleton-module](https://github.com/azerothcore/skeleton-module/tree/master/data) it should apply automatically any SQL upon running `worldserver`.

    - In the case the module doesn't follow that strucuture for example `data\sql\world` you will have to run those queries manually into their respectives databases.

After that, if you still having issues with the module, running `.server debug` and it can display how many modules are in the server (doesn't mean they are active or running, only that they were enabled in CMake and were compiled.)

```
List of enabled modules:
|- mod-1v1-arena
```

If the module appears up there, check the config file of the module, the place where you renamed previously `ModuleName.conf.dist - Copy` to `ModuleName.conf` some modules come "disabled" by default.

<br>

## Help

{% include help.html %}

| Installation Guide                                                                                                                   |
| :----------------------------------------------------------------------------------------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 8: Client Setup](client-setup)                                                                                              |

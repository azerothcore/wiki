# Optional Additions

| Installation Guide                                                                                                                   |                                         |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. | Optional                                |
| [<< Step 8: Client Setup](client-setup)                                                                                              |                                         |

At this point you have a working AzerothCore server. Everything below is **optional** - pick whatever fits your server, or skip this step entirely.

## Installing a Module

Modules let you alter or extend the blizzlike gameplay AzerothCore offers by default, without touching the core itself. They are the most common way to customise a server, and hundreds of them are available in the [AzerothCore Catalogue](https://www.azerothcore.org/catalogue#/).

Pick this if you want to add features such as anticheat, transmogrification, solo dungeon scaling, or player bots.

- [Installing a Module](installing-a-module)

## Cluster Mode

Cluster mode lets several worldservers serve a **single realm**, splitting players and maps between them. It relies on the external [ToCloud9](https://github.com/walkline/ToCloud9) project for the distributed logic.

Pick this only if you are experimenting with a large, horizontally scaled setup.

{% include warning.html content="Cluster mode is <b>experimental</b> and still under development. It is not needed for a normal server." %}

- [Cluster Mode](cluster-mode)

<br>

## Help

{% include help.html %}

| Installation Guide                                                                                                                   |                                         |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |                                         |
| [<< Step 8: Client Setup](client-setup)                                                                                              |                                         |

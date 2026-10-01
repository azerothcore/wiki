# Database Keeping the Server Up-to-Date

| Installation Guide                                                                                                                   |                                         |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 6: Final Server Steps](final-server-steps)                                                                                  | [Step 8: Client Setup >>](client-setup) |

1. First make sure that your core is [up-to-date](keeping-the-server-up-to-date).

If you want to know how the SQL directory works or plan to have custom changes we recommend you read [this](sql-directory).

## Automatic Database Updater

By default, the Worldserver and Authserver will check for, and execute all new files into the database you specified in the config.

1. Start worldserver.exe

To edit the automatic database updater you will find the necessary settings in authserver.conf and worldserver.conf under **UPDATE SETTINGS**.

## Database Updater tool (dbimport)

AzerothCore also ships a standalone tool called **dbimport**. It runs the exact same updater as the Authserver and Worldserver, but without starting a server: it connects to the three databases, creates and populates them if they are empty, applies all pending SQL updates and then exits.

This is useful when you want to:

- update your databases while the server is offline, or from a script (deployments, cron jobs, CI)
- keep a machine that only manages the database, without compiling the servers
- run the updater on a database that isn't attached to a running server

### Compiling only the Database Updater

The tool is part of the **tools** build list, so it can be compiled on its own:

- `-DTOOLS_BUILD=db-only` builds `dbimport` and none of the other tools (the map/vmap/mmap extractors)
- `-DAPPS_BUILD=none` skips the Authserver and Worldserver

{% include tip.html content="TOOLS_BUILD defaults to `none`, so if you want the updater you have to ask for it explicitly. The full list of accepted values is `none`, `all`, `db-only` and `maps-only` for TOOLS_BUILD, and `none`, `all`, `auth-only` and `world-only` for APPS_BUILD." %}

{% include important.html content="Module SQL files are only applied if the modules are present in the `modules/` folder when you run cmake, and are not disabled. Use the same MODULES value you use for your server build, otherwise the updater will not know about your modules." %}

### Using the Database Updater

The tool is installed next to the other binaries (for example `env/dist/bin/dbimport` on Linux, or `dbimport.exe` in your build output folder on Windows) and reads its own configuration file, **dbimport.conf**, which is created from `dbimport.conf.dist` in the same way as the other config files.

`dbimport.conf` contains the same **UPDATE SETTINGS** as authserver.conf and worldserver.conf (`Updates.EnableDatabases`, `Updates.AutoSetup`, `Updates.Redundancy`, `Updates.AllowedModules`, ...) plus the MySQL connection settings, so make sure those match your server configuration.

<br>

## Help

{% include help.html %}

| Installation Guide                                                                                                                   |                                         |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 6: Final Server Steps](final-server-steps)                                                                                  | [Step 8: Client Setup >>](client-setup) |

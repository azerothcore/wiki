# Database Installation

| Installation Guide                                                                                                                   |                                     |
| :----------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 3: Server Setup](server-setup)                                                                                              | [Step 5: Networking >>](networking) |

## Creating the Database in MySQL

### Creating the Databases and User

First of all, you need to create the acore user. You need to run the script below within a MySQL client or with the MySQL command-line interface (CLI).
You need to run the script as the **root** user of MySQL within a MySQL client or the MySQL cli.

https://github.com/azerothcore/azerothcore-wotlk/blob/master/data/sql/create/create_mysql.sql

{% include important.html content="Use the MySQL root user ONLY to run the script above, never run the core as root or administrator!" %}

{% include tip.html content="You can change the password of the user you are creating for increased security." %}

## Populating the database

If you want to know how the SQL directory works or plan to have custom changes we recommend you read [this](sql-directory).

#### Automatic Database Updater

The Authorization and Worldserver checks and applies all needed database files at startup.

To edit the automatic database updater you will find the necessary settings in authserver.conf and worldserver.conf under **UPDATE SETTINGS**.

1. Start Authserver.exe, in the Build folder you created, under \bin\RelWithDebInfo or \bin\Debug folder.
2. Start Worldserver.exe, in the same location.

If you get the following message in your console press enter to create and populate the databases.

```
Database "acore_auth" does not exist
Do you want to create it? [yes (default) / no]:
```

<br>

## Help

{% include help.html %}

| Installation Guide                                                                                                                   |                                     |
| :----------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 3: Server Setup](server-setup)                                                                                              | [Step 5: Networking >>](networking) |

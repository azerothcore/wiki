# Database Installation

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 3: Server Setup](server-setup.md) | [Step 5: Networking >>](networking.md) |

## Creating the Database in MySQL

### Creating the Databases and User

First of all, you need to create the acore user. You need to run the script below within a MySQL client or with the MySQL command-line interface (CLI). 
You need to run the script as the **root** user of MySQL within a MySQL client or the MySQL cli.

https://github.com/azerothcore/azerothcore-wotlk/blob/master/data/sql/create/create_mysql.sql

*Note: Use the MySQL root user ONLY to run the script above, never run the core as root or administrator!*

*Tip: You can change the password of the user you are creating for increased security.*

## Populating the database

If you want to know how the SQL directory works or plan to have custom changes we recommend you read [this](sql-directory).

#### Automatic Database Updater

The Auth- and Worldserver checks and applies all needed database files at startup.

To edit the automatic database updater you will find the necessary settings in authserver.conf and worldserver.conf under **UPDATE SETTINGS**.

1. Start Authserver.
2. Start Worldserver.

If you get the following message in your console press enter to create and populate the databases.

```
Database "acore_auth" does not exist
Do you want to create it? [yes (default) / no]:
```

<br>

## Help

If you are still having problems, check:

* [FAQ](faq.md)

* [Common Errors](common-errors.md)

* [How to ask for help](how-to-ask-for-help.md)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 3: Server Setup](server-setup.md) | [Step 5: Networking >>](networking.md) |

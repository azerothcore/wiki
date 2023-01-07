# Database Installation

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 3: Server Setup](server-setup.md) | [Step 5: Networking >>](networking.md) |

## Creating the Database in MySQL

### Creating the Databases and User

First of all you need to create the acore user using the script below.

https://github.com/azerothcore/azerothcore-wotlk/blob/master/data/sql/create/create_mysql.sql

You can perform this with a MySQL client or with the MySQL command-line interface (CLI).

You would need to use one MySQL root account with your MySQL client or with MySQL CLI before starting core to run one of those files (use MySQL root only to import one of those files, never run core as root or administrator).

*Tip: You can change the password of the user you are creating for increased security.*

## Populating the database

If you want to know how the SQL directory works or plan to have custom changes we recommend you read [this](sql-directory).

#### Automatic Database Updater

By default the Worldserver and Authserver will check for, and import all new files into the database you specified in the config.

This is the easiest and recommended way to make sure you are always up-to-date with the core.

To edit the automatic database updater you will find the necessary settings in authserver.conf and worldserver.conf under **UPDATE SETTINGS**.

1. Start Authserver.
2. Start Worldserver.

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

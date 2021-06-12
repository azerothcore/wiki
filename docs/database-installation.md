# Database Installation

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 3: Server Setup](server-setup.md) | [Step 5: Networking >>](networking.md) |

## Creating and Populating the Database in MySQL with automated script

### Creating the Databases and User

First of all you need to create the acore user using the script below.

https://github.com/azerothcore/azerothcore-wotlk/blob/master/data/sql/create/create_mysql.sql

You can perform this with a MySQL client or with the MySQL command-line interface (CLI).

You would need to use one MySQL root account with your MySQL client or with MySQL CLI before starting core to run one of those files (use MySQL root only to import one of those files, never run core as root or administrator).

*Tip: You can change the password of the user you are creating for increased security.*

### Importing the Database

*Note: if you're using MySQL 5.7, first run*

```
mysql -e "SET GLOBAL sql_mode = '';" -u root -p first
```

(replace root with your mysql user).

*Note: If you are using Windows you will need to run the .sh files with git*

1. Open **C:\AzerothCore\apps\db_assambler**

1. Run db_assambler.sh `bash apps/db_assembler/db_assembler.sh`

1. Select **import-all: Assemble & Import all**

### Changing user or password

If you want to change the user or password you will need to edit the script config.

1. Copy the file **conf/dist/config.sh** to **conf/config.sh**.

1. Open **conf/config.sh** with a text editor.

1. Go to the secion **DB EXPORTER/IMPORTER CONFIGURATIONS**.

1. Edit the variables accordingly, e.g. you most likely need to edit **MYSQL_USER** and **MYSQL_PASS** variables putting your mysql server settings.

<br>

## Help

If you are still having problems, check:

* [How to ask for help](how-to-ask-for-help.md)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 3: Server Setup](server-setup.md) | [Step 5: Networking >>](networking.md) |

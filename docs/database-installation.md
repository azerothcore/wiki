# Database Installation

| Installation Guide                                                                                                                   |                                     |
| :----------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 3: Server Setup](server-setup)                                                                                              | [Step 5: Networking >>](networking) |

## Creating the Database in MySQL

You will download or copy the contents of [create_mysql.sql](https://github.com/azerothcore/azerothcore-wotlk/blob/master/data/sql/create/create_mysql.sql).

Using the created super-user (by default is `root`) you will open any of database client refered in the requirements page (HeidiSQL, MySQL command-line interface [CLI], etc... or others your choice).

Now you will either drag/run or copy-paste the content of the file [create_mysql.sql](https://github.com/azerothcore/azerothcore-wotlk/blob/master/data/sql/create/create_mysql.sql).

### HeidiSQL (most popular for newer users of MySQL).
- Into your `Query` tab and press the blue "play" button or pressing `F9` (by default) to run the query.


### MySQL CLI (most popular for linux users.)
- In your terminal of choice (example given for `CMD` of Windows, which is recommended to be ran as `Administrator`) 
`mysql -u YourSuperUsername -h 127.0.0.1 -p < "YourPath/create_mysql.sql"` 

(This will prompt your password after being executed, in the safe side make sure the path is between "" and using / in the case is giving you `Access is denied` or `The system cannont find the file specified` check your path and file.extension in the case you do have the permissions or that you've executed as `Administrator`)


{% include important.html content="The file above file is a Query or SQL file, is not a SQL script, for the case of DBeaver users that may get that confusion." %}

{% include tip.html content="You can change the password of the user you are creating for increased security, either in the query file, execution or after in your Database client of choice." %}

## Populating the database

### Automatic Database Updater (Recommended, specially for newer users.)

The `authserver` and `worldserver` checks and applies all needed database files at startup.

To edit the automatic database updater you can find it in `authserver.conf` and `worldserver.conf` under **AUTOUPDATER** OR **UPDATE SETTINGS**.

1. Start `authserver`, in the `Build` folder you created, under `\bin\RelWithDebInfo` (for Windows) or `env/dist/bin` (for Linux).
2. Start `worldserver` in the same location.

If you get the following message in your console press ENTER to create and populate the databases (for: `acore_auth`, `acore_characters` or `acore_world`).

Example:
```
Database "acore_auth" does not exist
Do you want to create it? [yes (default) / no]:
```

If you want to know how the SQL directory works or plan to have custom changes we recommend you read [this](sql-directory), for manual or automatic execution.

{% include tip.html content="If you wish ever to start any of the databases from scratch, you always drop their databases and let them re-create and re-populate, keep in mind if you drop a database you WILL LOOSE everything in it, highly recommend if you have any custom changes SQL or Modules changes, backup your database before executing the queries and/or adding the modules, any SQL changes you should save the queries outside of the database in the case you wish to use them again in the future." %}


<br>

## Help

{% include help.html %}

| Installation Guide                                                                                                                   |                                     |
| :----------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 3: Server Setup](server-setup)                                                                                              | [Step 5: Networking >>](networking) |

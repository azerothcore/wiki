You can setup the database manually or using the automated script.

## How to setup the AzerothCore DB using the automated script

### Use the default configurations:

The `db_assembler` script and the `acore.sh` dashboard both use by default the **acore** db user for the database connection. Running for the first time the assembler command should create the user for you, however, if you're having permissions error or any other issue with that user, please run the following queries in your database with the root user:

```SQL
CREATE USER 'acore'@'localhost' IDENTIFIED BY 'acore';
CREATE USER 'acore'@'127.0.0.1' IDENTIFIED BY 'acore';
GRANT ALL PRIVILEGES ON * . * TO 'acore'@'localhost';
GRANT ALL PRIVILEGES ON * . * TO 'acore'@'127.0.0.1';
FLUSH PRIVILEGES;
exit;
```

It will setup the acore user properly to be used by the db_assembler script


### [ALTERNATIVE] Edit script configuration

If you don't want to use the default acore user, then you can change the configuration of the script with the following steps:

- Copy the file `conf/dist/config.sh` to `conf/config.sh`
- Open the `conf/config.sh` with any text editor
- Go to the secion `DB EXPORTER/IMPORTER CONFIGURATIONS`
- Edit the variables accordingly, e.g. you most likely need to edit `MYSQL_USER` and `MYSQL_PASS` variables putting your mysql server settings.

### Run the script

**Note**: if you're using MySQL 5.7, first run `mysql -e "SET GLOBAL sql_mode = '';" -u root -p` first (replace `root` with your mysql user).

**Note**: if you're using Windows you must set-up MySQL as an Environment Variable using [this tutorial](http://www.azerothcore.org/wiki/Environment-Variable) and run the commands using **git bash**

- Make sure you are currently located in the `azerothcore-wotlk` directory
- Run `bash apps/db_assembler/db_assembler.sh`
- Select `import-all: Assemble & Import all`
- Once the process is finished, you can exit the script.

-----------

Alternatively, you could also [set up your DB manually](Database-Manual-Setup.md) but this process is harder and not recommended for beginners.

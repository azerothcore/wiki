# SQL Directory

$ is relative to the source directory.

## Create and drop files

All create and drop files are found in $\data\sql\create\ directory.

create_mysql.sql contains the queries to create the acore user and the databases.

drop_mysql.sql revokes all permissions and drops the acore user and drops all databases. This is used for MySQL 5.7.

drop_mysql_8.sql drops the acore user and drops all databases. This is used for MySQL 8.0 or newer.

## Base files

All base files are found in the $\data\sql\base\ directory.

These files contain the all the data from the latest squashed update files.

Files from this directory are automatically imported with the [Automatic Database Updater](database-installation#automatic-database-updater-default-recommended).

## Update files

All update files are found in the $\data\sql\updates\ directory.

These files contain all the new updates to the database since the last squash.

Files from this directory are automatically imported with the [Automatic Database Updater](database-installation#automatic-database-updater-default-recommended).

## Pending update files

All pending update files are found in the $\data\sql\updates\pending_db_*\ directory.

All SQL changes you make to fix an issue on AzerothCore go in here.

You create the pending update file by running create_sql.sh script.

## Custom files

All custom files are found in the $\data\sql\custom\ directory.

All custom updates you make to the database should be stored in SQL files within this directory to make sure that they are not lost when updating your server.

Files from this directory are automatically imported with the [Automatic Database Updater](database-installation#automatic-database-updater-default-recommended).

## Archived files

All archived files are found in $\data\sql\archive\ directory.

All archived files are update files from previous database squashes.

These files serve no real purpose.

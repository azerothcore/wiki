# AC Database-only quick setup

This tutorial explains how to quickly setup an instance of the AC Database.


### Introduction

Sometimes you need an AzerothCore DB up and running without having to setup the whole server,
for example to use applications like [Keira3](https://github.com/azerothcore/Keira3) or similar.

With this setup, you do **not** have to install MySQL server in your system.

### Requirements

The only requirements are git and Docker (including `docker-compose`).
You can find the links to setup Docker for your operating system in the "Software requirements" category of 
[this page](http://www.azerothcore.org/wiki/Install-with-Docker#setup).

### Clone the AC sources

You need to clone the AC sources somewhere in your machine and cd into it:

```
git clone https://github.com/azerothcore/azerothcore-wotlk.git;
cd azerothcore-wotlk;
```

### How to quickly spin up an AzerothCore Database instance

You can easily create an instance of MySQL server containing the AC database using:

```
docker compose up -d ac-database
```

The default password will be `password` and the default port will be `3306`.

If you want to change those values, run the following instead:

```
DOCKER_DB_EXTERNAL_PORT=9000 DOCKER_DB_ROOT_PASSWORD=root docker compose up -d ac-database
```

After the db service is up and running, use the following command to import the database

`docker compose run --rm ac-dev-server ./acore.sh db-assembler import-all`

This will import all the sql files needed to setup your database 

**NOTE:** The same command can be used to keep the database updated with latest changes when you update the repository

### Destroy the docker instance of the AC Database

You can destroy the containers created with docker-compose using:

```
docker compose down
```


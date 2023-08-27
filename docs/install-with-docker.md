---
tableofcontents: 1
redirect_from: "/Install-with-Docker"
---

# Install with Docker

Welcome to the AzerothCore Docker guide!

The example docker configurations for AzerothCore may seem non-idiomatic at times, and this document can help users get started with running an AzerothCore server in a container-based environment.

## Setup

### Software requirements

The only requirements are [git](https://git-scm.com/download/) and Docker.

- For GNU/Linux install [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu)
- For macOS 10.12+ Sierra and newer version install [Docker Desktop for Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac)
- For Windows 10 install [Docker Desktop for Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

You'll also need the `compose` plugin for docker. Installation instructions are available [at this link](https://docs.docker.com/compose/install/#scenario-one-install-docker-desktop). If you're using a machine with docker desktop, you do not need to do this step.

Before going further, make sure you have `docker` and `docker compose` installed in your system by typing in a terminal:

```
docker --version
```
```
docker compose version
```

You should see a similar output:

```
Docker version 20.10.5, build 55c4c88
Docker Compose version 2.10.2
```

**Note for Windows users**: you can use **git-bash** (the shell included in git) as a terminal.

### Clone the AzerothCore repository

You need to clone the AzerothCore repository (or use your own fork):

```
git clone https://github.com/azerothcore/azerothcore-wotlk.git --depth 1
```

Now go into the main directory using `cd azerothcore-wotlk`. **All commands will have to be run inside this folder**.

### Installation

Inside your terminal (if you use Windows, use git bash), run the following commands inside the azerothcore-wotlk folder

**IMPORTANT**: the following procedure uses our acore.sh dashboard, however, these commands are a shortcut of the docker compose ones.
      you can check the docker compose commands used in background by running `./acore.sh docker --help` and read the description of each command

**1) Compile AzerothCore:**
```
./acore.sh docker build
```
It will build docker images and compile the core automatically! This may take a while.  

**For Windows:** if the build fails to complete with a message similar to the following:
```
unable to start container process: exec: "C:/Program Files/Git/usr/bin/bash": stat C:/Program Files/Git/usr/bin/bash: no such file or directory: unknown
```

You may have an issue with Unix > Windows path conversion. Setting the `MSYS_NO_PATHCONV=1` environment variable may fix this:

```
MSYS_NO_PATHCONV=1 ./acore.sh docker build
```

**2) Run the containers**

```
./acore.sh docker start:app
```

**Congratulations! Now you have an up and running azerothcore server! Continue to the next step to create an account**

If you need to run this in background, you can use the following command to run the docker compose detached mode:

```
./acore.sh docker start:app:d
```

**4) Access the worldserver console**

Open a new terminal and run the following command

```
docker compose ps
```

find the name of worldserver

```
azerothcore-wotlk_ac-authserver_1    ./acore.sh run-authserver     Up             0.0.0.0:3724->3724/tcp,:::3724->3724/tcp
azerothcore-wotlk_ac-database_1      docker-entrypoint.sh mysqld   Up (healthy)   0.0.0.0:3306->3306/tcp,:::3306->3306/tcp, 33060/tcp
azerothcore-wotlk_ac-worldserver_1   ./acore.sh run-worldserver    Up             0.0.0.0:7878->7878/tcp,:::7878->7878/tcp, 0.0.0.0:8085->8085/tcp,:::8085->8085/tcp
```

and then attach the worldserver. E.g.

```
docker attach azerothcore-wotlk_ac-worldserver_1
```

If you got error message `the input device is not a TTY.  If you are using mintty, try prefixing the command with 'winpty'` 

This command will automatically attach your terminal to the worldserver console. 
Now you can run the `account create <user> <password>` command to [create your first in-game account.](creating-accounts.md)

**IMPORTANT**:  **To detach**: press `ctr+p` and `ctrl+q`. Do **NOT** try to detach using `ctrl+c` or you will kill your worldserver process!

**5) Access database and update realmlist**

To access your MySQL database we recommend clients like [HeidiSQL](https://www.heidisql.com/) (for Windows/Linux+Wine) or [SequelPro](https://www.sequelpro.com/) (for macOS). Use `root` as user and `127.0.0.1` as default host.
The default password of the root DB user will be `password`.

Unless your server installation is on the same machine as your client, you might want to update the `realmlist` address in the `acore_auth` database with your server's public or private IP address :
```sql
USE acore_auth;
SELECT * FROM realmlist;
UPDATE realmlist SET address='<SERVER PUBLIC IP ADDRESS>';
```

## Procedures

### Configuring AzerothCore in Containers

Similar to most applications running in containers, AzerothCore can be configured with environment variables. You can find the valid configuration parameters and their description from the default configuration files for [the worldserver](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/apps/worldserver/worldserver.conf.dist) and the [authserver](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/apps/authserver/authserver.conf.dist). Locally, these files can be found in the `env/dist/etc` directory after a build (as in, `./acore.sh docker build`) by default.

After you've found a parameter you'd like to change, you can insert the new value to the `environment` section of that service in the `docker-compose.yml`. For example, environment variables to configure the worldserver would go under [this line](https://github.com/azerothcore/azerothcore-wotlk/blob/3eb2463c69e55f6e76683cca37811e8a8ca29605/docker-compose.yml#L183) (see code block below). Do note that there's a few environment variables predefined. These are required for the operation of the various components of AzerothCore in a container-based environment. Removal of them will make it difficult to ensure that your AzerothCore Server is functioning as intended.

```yaml
services:
  ...
  ac-worldserver:
    ...
    environment:
      AC_DATA_DIR: "/azerothcore/env/dist/data" # DataDir
      AC_LOGS_DIR: "/azerothcore/env/dist/logs" # LogsDir
      AC_LOGIN_DATABASE_INFO: "ac-database;3306;root;${DOCKER_DB_ROOT_PASSWORD:-password};acore_auth" # LoginDatabaseInfo
      AC_WORLD_DATABASE_INFO: "ac-database;3306;root;${DOCKER_DB_ROOT_PASSWORD:-password};acore_world" # WorldDatabaseInfo
      AC_CHARACTER_DATABASE_INFO: "ac-database;3306;root;${DOCKER_DB_ROOT_PASSWORD:-password};acore_characters" # CharacterDatabaseInfo
      AC_CLOSE_IDLE_CONNECTIONS: "0" # CloseIdleConnections
      # [ CUSTOM PARAMETERS BELOW THIS LINE ]
      AC_ALLOW_TWO_SIDE_INTERACTION_CALENDAR: "1" # AllowTwoSide.Interaction.Calendar
```

Figuring out the environment variable name of a configuration parameter can be a bit difficult. The general rules for this:

- The entire parameter is prefixed with `AC_`
- Periods (`.`) become underscores (`_`)
- A sequence with a lowercase letter and then an uppercase letter inserts an underscore (`_`) between them
- The entire parameter is uppercased (so `foo` becomes `FOO`)

A few examples:

- `foo.bar_baz` => `AC_FOO_BAR_BAZ`
- `MaxPrimaryTradeSkill` => `AC_MAX_PRIMARY_TRADE_SKILL`
- `AllowTwoSide.Interaction.Calendar` => `AC_ALLOW_TWO_SIDE_INTERACTION_CALENDAR`

Directly inserting the environment variables into the `docker-compose.yml` keeps all of the configuration in one place; it's easy to see the full configuration of the server (including things like port forwards) without having to jump through multiple files. At times though, it may be more practical to have all env vars defined in the `env_file` or in a [`compose.override.yml`](https://docs.docker.com/compose/multiple-compose-files/merge/) file. While the inclusion of separate files may add to the complexity of your setup, separate files may make it easier to manage a subset of the containers' configuration that's changed often.  

### How to keep your AzerothCore updated with the latest changes

First of all, you just need to use the `git` tool to update your repository by running the following command:

`git pull origin master` : this will download latest commits from the azerothcore repository

Then you can just run the following command:

`./acore.sh docker build`: to rebuild the images and generate new binaries.

NOTE:  We do not update so often the client data, but when it happens you can run the following command:

`./acore.sh docker client-data`: it will download the new version of the client data if there's a new version available

### How to run the worldserver with GDB

Running the server with GDB allows you to generate a crashdump if the server crashes. The crashdump file is useful for developers to understand which lines are failing and possibly fix it.

**Keep in mind that you should compile your code with one of the following compilation types: Debug or RelWithDebInfo, otherwise GDB won't work properly**

To enable GDB the steps are the following:

1. Create a `config.sh` file under the `/conf/` directory of the azerothcore-wotlk repository
2. Add this configuration inside: `AC_RESTARTER_WITHGDB=true`. It will configure the restarter used by our docker services to use GDB instead of the binaries directly
3. Restart your containers and that's it!

If the server crashes, you will find the crashdump file (`gdb.txt`) within the `/env/docker` folder

### .devcontainer support

In `docker-compose.yml`, we define the `ac-dev-server` service
This service is used for our build and db operations, but it can also be used
by you to develop with the [VSCode Remote Docker extension](https://code.visualstudio.com/docs/remote/containers)

A dev-container lets you use a Docker container as a full-featured development environment. The **.devcontainer** folder in our project contains files to tell VS Code how to access (or create) a development container with all the needed tools. This container will run the AzerothCore with all the software and the configurations needed for working with our codebase and debugging the server.

Inside the azerothcore repo there's a pre-configured `devcontainer.json` that can be opened by using the VSCode command palette.
To setup the Dev-Container follow these steps:

1. [install and open VSCode](https://code.visualstudio.com/)
2. install the [remote-container](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension
3. Open the azerothcore folder inside VSCode
4. Open the VSCode [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) (Ctrl+Shift+P) and run: `>Remote-Containers: Reopen in Container` 

**IMPORTANT**: The dev-container also contains a pre-configured debugger action that allows you to use breakpoints and debug your worldserver. 

Do not forget that you need to [Remote Container extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 
installed in your [Visual Studio Code](https://code.visualstudio.com/) IDE

#### How to debug your code with the dev-container

NOTE: **Keep in mind that you should compile your code with the Debug mode, otherwise the debugger won't work properly**

Once inside the VSCode dev-container you can go to the debug session and use the `Linux/Docker debug` action as you can see in this image:

![image](https://user-images.githubusercontent.com/147092/115712693-5a837d80-a375-11eb-98aa-b415e1919125.png)

It will run a worldserver in debug mode and then you can start placing breakpoints in your code to debug it.

![image](https://user-images.githubusercontent.com/147092/115712867-9cacbf00-a375-11eb-9cab-890e4f68d98b.png)

For more info about how to debug in vscode you can refer to the [official guide](https://code.visualstudio.com/docs/editor/debugging)

### How to create a second realm with docker compose

<!-- TODO: flesh this out. This can be included here. -->

To create a second realm we suggest you to take a look at the example available within the http://github.com/azerothcore/acore-docker repository.


## More info

### Adding Modules

To add a module simply place the module directory inside of the `/azerothcore-wotlk/modules` directory.

After adding a module you'll have to rebuild azerothcore:
```
./acore.sh docker build
```

If the added module makes use of configurations files you'll have to place them in the `azerothcore-wotlk/env/dist/etc/modules` directory.  If this modules directory doesn't exist, you'll have to manually create it yourself.

After rebuilding you can [(re)start the containers](#how-can-i-start-stop-create-and-destroy-my-containers) again.

## FAQ

### Where are the etc and logs folders of my server?

With docker, it's common that applications log to the console. You can view these with the `docker compose --profile app logs` command,

Additionally, they are located in `env/dist/logs` and `env/dist/logs`, though this may be removed in the future. 

### How can I start, stop, create and destroy my containers?

- The `docker compose start --profile app start` will start your existing app containers in detached mode.

- The `docker compose stop` will stop your containers, but it won't remove them.

- The `docker compose --profile app up` builds, (re)creates, and starts your app services.

- The `docker compose down --remove-orphans` command will stop your containers, but it also removes the stopped containers as well as any networks that were created.

- ⚠️ The `docker compose down --rmi all -v --remove-orphans` : command will stop, remove, and delete EVERYTHING. Including the volumes with the associated database ⚠️ 

### How to deal with the permission issues

#### [Linux] You must run docker without sudo

It's very important to run Docker without using sudo or the root user when possible. To do that you must setup your current user to be part of the docker group.
Please, follow the official guide to configure it: [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)

#### [Linux] the containers are running as root

For simplicity, we run all the containers of the `azerothcore-wotlk` repo as root user to avoid permission issues while running them.
However, it means that you need to reset the user permissions of the files created by the containers on your host, you can easily do it by running this command 

```sudo chown -R $(id -u):$(id -g) .```

If you want to run your containers with a different user instead, you need to create an `.env` file in the root directory and set the following variables:

```
DOCKER_USER=acore
DOCKER_USER_ID=1000
DOCKER_GROUP_ID=1000
```

The USER_ID and the GROUP_ID must be aligned with the user of your host

### How can I delete my database files?

**Warning** Once you've deleted your database files they are unrecoverable unless you have a backup.

To remove your database files you firstly want to make sure that your containers have been stopped and removed by typing: `docker compose down`.

After stopping and removing your containers you can proceed to remove the volume by typing: `docker volume rm azerothcore-wotlk_ac-database`

**Note** If you've changed your folder name from the default `azerothcore-wotlk` the volume name will be slightly different. To find the new volume name you can use the command `docker volume ls`. The volume should be labelled something along the lines of `xxxx_ac-database`.

### Performance optimizations (for dev server)

NOTE: If you are not experimenting any particular issues with I/O performance, we suggest to **NOT** use this configuration

The **osxfs** and the NTFS are well known to have [performance limitations](https://github.com/docker/for-mac/issues/1592) with docker binded volumes, we optimized the docker compose by using volumes and the "delegated/cached" strategy when possible, but that's not enough for some configurations.

* **Windows users:** we suggest to use the [WSL2](https://docs.docker.com/desktop/windows/wsl/) to clone our repo and work with docker. It has similar performance to a native linux environment

* **Mac users:** unfortunately there is not something similar to WSL2 on Mac, however, only the `ac-dev-server` uses binded src volumes that can cause such slowness.
  If you still want to use the `ac-dev-server` under Mac, consider to try the [acore-docker one](https://www.azerothcore.org/acore-docker/#dev-server). It uses named volumes
  that are way faster than the binded ones.

### Docker reference & support requests

For server administrators, we recommend to read the [Docker documentation](https://docs.docker.com/) as well as the [Docker Compose reference](https://docs.docker.com/compose/reference/overview/).

If you want to be an administrator of an AzerothCore production server, it helps if you are familiar and comfortable with Docker and using a command line.

Feel free to ask questions on [StackOverflow](https://stackoverflow.com/) and link them in the **#support-docker** channel of our [Discord chat](https://stackoverflow.com/questions/tagged/azerothcore). We will be happy to help you!

## Introduction

The AzerothCore bash dashboard is a collection of scripts that help with the installation and maintenance of an AzerothCore server.
It allows to easily install, update and execute AzerothCore on your machine in a tremendously small amount of steps.

Installing a development or production private server has never been so easy before.

### NOTE: not for all platforms yet

These scripts are supposed to be cross-platform, however we are not quite there yet.
It's not currently recommended to use the installation process described in this page on Windows or macOS.
You can of course try them anyway and [let us know](https://github.com/azerothcore/azerothcore-wotlk/issues/new/choose) in case you encounter any issue.

That does not mean that you cannot use this in production.
We tested this procedure on a dedicated server machine running Ubuntu 20.04 and it worked quite nicely,
we'll include here some extra tips for production environments as well.


### Tips for dedicated servers

You can easily install AzerothCore in a linux server without any kind of GUI,
simply connecting remotely via ssh using [Visual Studio Code](https://code.visualstudio.com/) 
and the [SSH](https://code.visualstudio.com/docs/remote/ssh) 
and the [SSH: Editing Configuration Files](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh-edit) extensions so you'll feel just like at home.

If you need any help just [ask a question](https://www.azerothcore.org/wiki/How-to-ask-for-help).

More tips for dedicated servers below.

## Setup

### Get the AC sources

Install [git](https://git-scm.com/) and clone the AC repository:

```
apt update && apt install git
```

```
git clone https://github.com/azerothcore/azerothcore-wotlk.git; cd azerothcore-wotlk`
```

### Configuration

There is a [conf/dist/config.sh](https://github.com/azerothcore/azerothcore-wotlk/blob/master/conf/dist/config.sh) 
file containing a default configuration. Have a look at it. 
Most of the configuration defaults will probably work for your case, 
but you can copy it under `conf/config.sh` and change values as you please.


### Install all AC dependencies

```
./acore.sh install-deps
```

### Build everything from scratch

```
./acore.sh compiler all
```

### Set-up the database

- Either connect to your MySQL database and manually create the `acore` MySQL user:

```
DROP USER IF EXISTS 'acore'@'localhost';
DROP USER IF EXISTS 'acore'@'127.0.0.1';
CREATE USER 'acore'@'localhost' IDENTIFIED BY 'acore';
CREATE USER 'acore'@'127.0.0.1' IDENTIFIED BY 'acore';
GRANT ALL PRIVILEGES ON * . * TO 'acore'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON * . * TO 'acore'@'127.0.0.1' WITH GRANT OPTION;
FLUSH PRIVILEGES;
exit;
```

- Or change the `config.sh` to use another MySQL user.

Then run:

```
./acore.sh db-assembler import-all
```

this will install a full AzerothCore Database. No need to import any DB update at this point.

### Download the latest client data

Get the latest client data:

```
./acore.sh client-data
```

### Server config files

```
cp env/dist/etc/authserver.conf.dist env/dist/etc/authserver.conf
```
```
cp env/dist/etc/worldserver.conf.dist env/dist/etc/worldserver.conf
```

### Result

If you followed the above, you'll get your server inside the `env/dist` directory.

The `worldserver` and `authserver` binaries are located in `azerothcore-wotlk/env/dist/bin`.

You can either run them directly or use the restarter (see below).

### Restarter

The AzerothCore dashboard comes with a bundled restarter suite:

```
./acore.sh run-worldserver
```

```
./acore.sh run-authserver
```

For dedicated servers, 
you may want to run them inside terminal multiplexer sessions using tools like `tmux` (see below).

## How to update your server

Update the sources:

```
git pull
```

Rebuild:
```
./acore.sh compiler build
```

Update the database:

```
./acore.sh db-assembler import-updates
```

That's it.

## Tips for dedicated (production) servers

### Run AzerothCore inside Tmux sessions

You can use [tmux](https://github.com/tmux/tmux) as terminal multiplexer, 
it will allow you to easily manage your processes inside a server with no GUI.

You can create 2 sessions for the `worldserver` and `authserver` processes:

- `tmux new -s world-session`
- `tmux new -s auth-session`

For example you can attach to the `world-session` session using:

- `tmux attach -t world-session`

Then you can push `CTRL+B+D` to exit the session without killing the process.
If connected using VSCode SSH, you can just close the terminal session.

Other useful commands:

- create a new session: `tmux new -s my_session`
- list all sessions: `tmux ls`
- kill a session: `tmux kill my_session` (or just attach to it and type `exit`)
- ...more details available at the [tmux wiki](https://github.com/tmux/tmux/wiki)


### Automatically start the tmux sessions at system startup

TODO

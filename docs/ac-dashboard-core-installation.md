## Introduction

The AzerothCore bash dashboard is a collection of scripts that help with the installation and maintenance of an AzerothCore server.
It allows to easily install, update and execute AzerothCore on your machine in a tremendously small amount of steps.

Installing a development or production private server has never been so easy before. 
If you need any help just [ask a question](How-to-ask-for-help).


## Requirements

You need to have [git](https://git-scm.com/), [curl](https://curl.se/), [unzip](https://github.com/madler/unzip), [sudo](https://www.sudo.ws/) installed in your machine. 
No other software is required to be installed manually.


- debian/ubuntu-based: `apt update && apt install git curl unzip sudo`
- macOS: `brew install git`
- Windows: download and install [Git for Windows](https://gitforwindows.org/)

### Notes
- For macOS users: install and use the latest version of bash to run the commands of the dashboard (`brew install bash`)
- For Windows users: the commands need to be executed within the "git bash" shell or a bash-compatible shell such as WSL, cygwin etc..
  However, git bash is suggested because is preinstalled with git for windows (one of our requirements)
  

## Setup

### Get the AC sources

```
git clone https://github.com/azerothcore/azerothcore-wotlk.git; cd azerothcore-wotlk
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

NOTE: on Windows it must be executed as an administrator

### Build everything from scratch

```
./acore.sh compiler all
```

### Set-up the database

- Connect to your MySQL database (with `sudo mysql -u root`) and manually create the `acore` MySQL user by running:

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

*Note:  even though the `acore` user is only accessible from localhost, 
it is a good practice to change its password to something more secure.*

### Download the latest client data

Get the latest client data:

```
./acore.sh client-data
```

### Server config files

create these 2 files. They contain the default configuration for the worldserver and authserver, if you don't wish to modify simply copying them is enough.

#### Linux and Mac

```
cp env/dist/etc/authserver.conf.dist env/dist/etc/authserver.conf
cp env/dist/etc/worldserver.conf.dist env/dist/etc/worldserver.conf
```

#### Windows and Mac

```
cp env/dist/configs/authserver.conf.dist env/dist/configs/authserver.conf
cp env/dist/configs/worldserver.conf.dist env/dist/configs/worldserver.conf
```

### Result

If you followed the above, you'll get your server inside the `env/dist` directory.

The `worldserver` and `authserver` binaries are located in `azerothcore-wotlk/env/dist/bin`.

You can either run them directly or use the restarter (see below).
The first startup of the `worldserver` will install a full AzerothCore Database. No need to import any DB update at this point.

Please also see [Networking](networking) and [Final Server Steps](final-server-steps).

### Restarter

The AzerothCore dashboard comes with a bundled restarter suite:

```
./acore.sh run-worldserver
```

Wait until the process is completed then run: 

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

[database-keeping-the-server-up-to-date](database-keeping-the-server-up-to-date)

That's it.


## Tips for dedicated (production) servers

### Daily backups of your databases via Telegram

Getting daily backups of your private server databases directly to your phone/computer 
via [Telegram](https://telegram.org/) messages?

Yes, that's possible. Just use: [azerothcore/telegram-automated-db-backup](https://github.com/azerothcore/telegram-automated-db-backup)

### Visual Studio Code SSH

You can easily install AzerothCore in a linux server without any kind of GUI,
simply connecting remotely via ssh using [Visual Studio Code](https://code.visualstudio.com/)
and the [SSH](https://code.visualstudio.com/docs/remote/ssh)
and the [SSH: Editing Configuration Files](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh-edit) extensions so you'll feel just like at home.

### Run AzerothCore inside Tmux sessions

You can use [tmux](https://github.com/tmux/tmux) as terminal multiplexer, 
it will allow you to easily manage your processes inside a server with no GUI.

You can create 2 sessions and run the `worldserver` and `authserver` processes inside them:

- `tmux new -s world-session`
- now run the `./acore.sh run-worldserver` inside it, then detach from it


- `tmux new -s auth-session`
- now run the `./acore.sh run-authserver` inside it, then detach from it

You can detach using `CTRL+B+D` to exit the session without killing the process.
If connected using VSCode SSH, you can just close the terminal session.

You can attach again to the `world-session` session using:

- `tmux attach -t world-session`

Other useful commands:

- create a new session: `tmux new -s my_session`
- list all sessions: `tmux ls`
- kill a session: `tmux kill my_session` (or just attach to it and type `exit`)
- kill ALL sessions: `tmux kill-server`
- ...more details available at the [tmux wiki](https://github.com/tmux/tmux/wiki)


### Automatically start the tmux sessions at system startup

You can automatically create the tmux sessions and execute the `authserver` and `worldserver` using this simple script:

```sh
#!/usr/bin/env bash

# CHANGE THESE WITH THE CORRECT PATHS
authserver="/path/to/azerothcore-wotlk/acore.sh run-authserver"
worldserver="/path/to/azerothcore-wotlk/acore.sh run-worldserver"

authserver_session="auth-session"
worldserver_session="world-session"

if tmux new-session -d -s $authserver_session; then
    echo "Created authserver session: $authserver_session"
else
    echo "Error when trying to create authserver session: $authserver_session"
fi

if tmux new-session -d -s $worldserver_session; then
    echo "Created worldserver session: $worldserver_session"
else
    echo "Error when trying to create worldserver session: $worldserver_session"
fi

if tmux send-keys -t $authserver_session "$authserver" C-m; then
    echo "Executed \"$authserver\" inside $authserver_session"
    echo "You can attach to $authserver_session and check the result using \"tmux attach -t $authserver_session\""
else
    echo "Error when executing \"$authserver\" inside $authserver_session"
fi

if tmux send-keys -t $worldserver_session "$worldserver" C-m; then
    echo "Executed \"$worldserver\" inside $worldserver_session"
    echo "You can attach to $worldserver_session and check the result using \"tmux attach -t $worldserver_session\""
else
    echo "Error when executing \"$worldserver\" inside $worldserver_session"
fi
```

On unix systems, you can then use [crontab](https://en.wikipedia.org/wiki/Cron) 
to run the script automatically at system startup:

```
crontab -e
```

then add this line (replace `/path/to/startup.sh` with the path of where you placed the above script):

```
@reboot /bin/bash /path/to/startup.sh
```

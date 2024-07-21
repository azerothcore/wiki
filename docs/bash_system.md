# BASH system

AzerothCore uses an advanced bash system that allows us to automate processes such as the sources **compilation, module installation, database setup etc.**

For now we are using bash instead of Python to reduce external dependencies since BASH is a crossplatform scripting language that is already included 
with **OSX, Linux and Windows** (via GIT BASH that we ask you to install in our requirements).

You can read the official bash documentation here: https://tldp.org/LDP/abs/html/index.html

## ACORE DASHBOARD

Our azerothcore related bash scripts can be found inside the /app folder, but we also created a script called **acore.sh** within the root folder. 
This script runs a dashboard that contains the commands to run all scripts related to the /app folder.

run `./acore.sh --help` for the entire list of the available commands. 

### Configuration

The /conf folder available in our project root directory is used to give you the possibility to change configurations for all our bash scripts

### Interactive mode

run `./acore.sh` and you can use the dashboard in interactive mode: you can navigate within the dashboard menu and sub-menu and run the command you need

### Command arguments

You can use the commands of the dashboard as arguments of the ./acore.sh script. For instance:

`./acore.sh compiler configure` will run the configuration process of our c++ compiler

All commands come with a shorter alias. For example `./acore.sh c configure` will run the compiler configuration, but also `./acore.sh 5 3` will do it.


## DEPS

Our bash system uses external bash libraries that are generic and not related to the azerothcore itself, those libraries have been created by us and 
have been placed under /deps folder


## HOOKS:

Internal [Hook system for bash](hooks-bash)

## Other resources

- Single bash command to install azerothcore: [Video + script in description](https://www.youtube.com/watch?v=j1HI6pLZZvM)

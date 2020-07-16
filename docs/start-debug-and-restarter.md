# How to start the server

## introduction
AzerothCore is composed by 2 services: authserver and worldserver.
Authserver only acts as an authenticator and a router for your realms redirecting your authorized client connections to the selected realm address.
the Worldserver instead handles all connections related to the game mechanics and it's the single source of truth for everything related to a single realm.

Authserver and Worldservers can be placed to different environment, however, in the following guide we will explain you how to run them together on same environment.

## how to start

both authserver and worldserver can be started by simply run the compiled binaries after [completing the installation](https://www.azerothcore.org/wiki/Installation).


### How to Debug

[WIP]

## Acore Restarter

**based on**: bash
**operating systems**: Linux, MacOS, Windows (with WSL)

If you compile azerothcore using the [acore.sh](https://www.azerothcore.org/wiki/bash_system), you will notice that ...

[WIP]

### Run at system startup

[WIP]

### Enable GDB

[WIP]


## As Windows service

**based on**: windows services
**operating systems**: Windows

[WIP]

## PM2 Process Manager

**based on**: nodejs
**operating systems**: [All OS supported by NodeJS](https://en.wikipedia.org/wiki/Node.js)

[WIP]

## Docker

**based on**: docker
**operating systems**: [All OS supported by docker](https://en.wikipedia.org/wiki/Docker_(software))

[WIP]


### With Manual compilation

[WIP]

### With Prebuilt images

Available Soon™

---
tableofcontents: 1
---

# How to restart and debug

AzerothCore is composed of two services: authserver and worldserver.
Authserver only acts as an authenticator and a router for your realms redirecting your authorized client connections to the selected realm address.
The worldserver instead handles all connections related to the game mechanics and it is the single source of truth for everything related to a single realm.

Authserver and worldservers can be placed on different environments. However, in the following guide we will explain how to run them together on the same environment.

## The `startup-scripts` Engine

We have introduced a new set of startup scripts that provide a powerful and unified way to run, manage, and debug your servers. This is now the recommended way to handle the `authserver` and `worldserver` processes for all non-Docker installations.

These scripts offer advanced features like automatic restarts via systemd or PM2, session management (using `tmux` or `screen`), and integrated GDB debugging for crash analysis.

For a complete guide on how to use and configure the new startup scripts, please refer to the official **[README.md located in the startup-scripts directory](https://github.com/azerothcore/azerothcore-wotlk/blob/master/apps/startup-scripts/README.md)**.

### Basic Usage

The easiest way to use the new system is through the acore.sh dashboard:

```bash
# To run the worldserver with the new engine
./acore.sh run-worldserver

# To run the authserver with the new engine
./acore.sh run-authserver
```

### Configuration and Debugging

To enable the GNU Debugger (GDB) and generate crash reports, you need to edit the configuration file for your service. For example, for a service named `ac-world-1`, you would edit a file similar to ac-world-1-run-engine.conf and set `GDB_ENABLED=1`.

```properties
// ...existing code...
# Enable/disable GDB execution
export GDB_ENABLED=1
// ...existing code...
```

If the server crashes after enabling GDB, you will find the crashdump file (e.g., `gdb-YYYY-MM-DD-HH-MM-SS.txt`) inside the `apps/startup-scripts/logs/crashes/` directory. <b>Keep in mind that you must compile your code with one of the following compilation types: `Debug` or `RelWithDebInfo`, otherwise GDB will not produce meaningful reports.</b>

## Using Docker (cross-platform)

Our Docker setup integrates the `startup-scripts` engine. This means that enabling GDB and managing restarts works seamlessly within the Docker environment as well. Moreover, our docker-compose.yml uses the [restart-policy feature](https://docs.docker.com/config/containers/start-containers-automatically/) to automatically keep the containers up and running after a crash or a system reboot.

For more information, please refer to the [Install with Docker](https://www.azerothcore.org/wiki/Install-with-Docker) documentation. You will also find a guide on how to debug your code by using VSCode combined with its Remote Docker extension.


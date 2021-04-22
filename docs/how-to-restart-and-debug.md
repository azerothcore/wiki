---
tableofcontents: 1
---

### Restarter using acore dashboard

You can use `./acore.sh run-worldserver` and `./acore.sh run-authserver`

They both work out of the box when you compile with the dashboard.

**NOTE**: To enable GDB you can use `AC_RESTARTER_WITHGDB=true` as an environment variable or by adding this to your `/conf/config.sh` file

### USING DOCKER

Our docker system integrates the scripts above within the docker-compose. It means that enabling the GDB works exactly in the same way in docker too.
Moreover our docker-compose uses the [restart-policy feature](https://docs.docker.com/config/containers/start-containers-automatically/) to keep the containers up and running.

For more information please refer to the [Install-with-Docker](Install-with-Docker.md) documentation

### Advanced restarter

For more advanced restarters that include several other useful configurations, you can try our "run-engine" system written in bash.

Here you can find the restarters for linux/bash environments: https://github.com/azerothcore/azerothcore-wotlk/tree/master/apps/startup-scripts

Those scripts are automatically copied after the compilation to the `/dist` directory if you're using our `./acore.sh` dashboard

You can copy the `conf.sh.dist` and create a `conf-world.sh` file to customize those documented configurations (do the same for the `conf-auth.sh`). In this way, you have both restarter and gdb pre-configured to create a `gdb.txt` (crashdump) file when the core crashes. Make sure to use `RelWithDebInfo` or `Debug` compilation (in your CMake command) in order to get meaningful crash reports.

Then copy the `restarter-world.sh` and the `restarter-auth.sh` from the "examples" beside your conf file and in the same folder of the "run-engine" file.

Eventually you will have something like this:

[![example][1]][1]

Run those 2 restarter script to have both authserver and worldserver restarters with gdb support.


### Manual way

Always make sure to use **RelWithDebInfo** or **Debug** compilation (in your CMake command) in order to get meaningful crash reports.

Create a file called `gdb.conf` with this inside:

    set logging on
    set debug timestamp
    run -c ../etc/worldserver.conf
    bt

Then, to debug or create a crashdump you can just use the gdb command as described in its documentation:

```
gdb -x gdb.conf --batch ./worldserver
```

This command should be enough to both attach your IDE to debug your code and also generate a crashdump when the server crashes

For an "universal" and more advanced restarter, Personally I'm using [PM2][2]

```
pm2 start "gdb -x gdb.conf --batch ./worldserver"
```

It should be enough to automatically restart, monitoring and gdb your server


  [1]: https://i.stack.imgur.com/EyIi7.png
  [2]: https://pm2.keymetrics.io/
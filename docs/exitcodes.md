# Exit Codes

AzerothCore has 3 default exit codes that are called if you shutdown, restart or crash the server.

```cpp
enum ShutdownExitCode
{
    SHUTDOWN_EXIT_CODE = 0,
    ERROR_EXIT_CODE    = 1,
    RESTART_EXIT_CODE  = 2,
};
```

SHUTDOWN_EXIT_CODE is called when you use the commands **.server shutdown**, **.server idleshutdown**, **.server exit** or if the [m_serviceStatus == 0](https://github.com/azerothcore/azerothcore-wotlk/blob/a594bf5b290e5476c61bab29809a079e93c5daa2/src/server/worldserver/Main.cpp#L575-L581) for Windows.

RESTART_EXIT_CODE is called when you use the commands **..server restart** and **.server idlerestart**.

ERROR_EXIT_CODE is called when the server crashes. This can be due to due to guid/id/entry overflow, [Network.Threads](https://github.com/azerothcore/azerothcore-wotlk/blob/a594bf5b290e5476c61bab29809a079e93c5daa2/src/server/worldserver/worldserver.conf.dist#L2909-L2913) being <= 0 or if the server cannot initialize network.

The best way to know where all the exit codes are called is by finding them in the source code.

## Commands

```
.server idleshutdown #delay [#exit_code]
.server idlerestart #delay [#exit_code]
.server shutdown #delay [#exit_code]
.server restart #delay [#exit_code]
```

The `.server shutdown/restart`, `.server idleshutdown/restart` commands all have an argument for **[#exit_code]**.

The default exit code for shutdown is always 0 and the default exit code for restart is always 2 if the argument is left blank.

The argument can take a value between 0 - 125 which lets you output a custom exit code other than the defaults.

## Scripts including exit codes

Having the Worldserver sending exit codes let's you create an external script that can act when it reads a specific exit code being displayed.

For example it's possible to write a script to automatically restart if the Worldserver sends RESTART_EXIT_CODE.

You can view [this](https://github.com/Kitzunu/azerothcore-exitcode-script) batch script for Windows how exit codes can be used.

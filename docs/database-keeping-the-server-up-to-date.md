# Database Keeping the Server Up-to-Date

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 6: Final Server Steps](final-server-steps.md) | [Step 8: Client Setup >>](client-setup.md) |

1. First make sure that your core is [up-to-date](keeping-the-server-up-to-date.md).

## Automatic Database Updater (default, recommended)

By default the Worldserver and Authserver will check for, and import all new files into the database you specified in the config.

This is the easiest and recommended way to make sure you are always up-to-date with the core.

To edit the automatic database updater you will find the neccessary settings in authserver.conf and worldserver.conf under [UPDATE SETTINGS](https://github.com/azerothcore/azerothcore-wotlk/commit/2d2857ce81db5297eb63d388d2e2f252ef52412d#diff-56b141374cf0384a2887c9fd490c6a79a3d2f31fb020ee0e423a5685344b59d3R30).

## DB Assambler

1. Run db_assambler.sh and select **import-updates: Assamble & Import only updates**.
    
    1. For Linux and macOS users run this command:
    
    ```
    bash apps/db_assembler/db_assembler.sh
    ```

Tip: how to [make sure your DB is up to date](https://stackoverflow.com/questions/55282167/how-to-make-sure-that-the-db-is-up-to-date)

<br>

## Help

If you are still having problems, check:

* [FAQ](faq.md)

* [Common Errors](common-errors.md)

* [How to ask for help](how-to-ask-for-help.md)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 6: Final Server Steps](final-server-steps.md) | [Step 8: Client Setup >>](client-setup.md) |

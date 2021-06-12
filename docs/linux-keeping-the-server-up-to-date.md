# Linux Keeping the Server Up-to-Date

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 6: Final Server Steps](final-server-steps.md) | [Step 8: Client Setup >>](client-setup.md) |

## Keeping the source Up-to-Date

```sh
cd ~/azerothcore/
git pull origin master
```

```sh
cd build
make -j 8; make install
```

Sometimes we add or remove files from the repositiory. At that point it is neccessary to recompile the server, the same way as it was installed the first time [in the Linux Core Installation](linux-core-installation.md#configuring-for-compiling).

## Keeping the Database Up-to-Date

Read [Database Keeping the Server Up-to-Date](database-keeping-the-server-up-to-date.md)

<br>

## Help

If you are still having problems, check:

* [How to ask for help](how-to-ask-for-help.md)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 6: Final Server Steps](final-server-steps.md) | [Step 8: Client Setup >>](client-setup.md) |

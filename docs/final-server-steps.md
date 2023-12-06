# Final Server Steps

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 5: Networking](networking.md) | [Step 7: Keeping the Server Up-to-Date >>](keeping-the-server-up-to-date.md) |

## Starting the server

- Run authserver and worldserver in your build folder.

For detailed information on how to configure a restarter and a debugger go to [how-to-restart-and-debug](how-to-restart-and-debug.md) page

{% include important.html content="NEVER create an account directly into your database unless you are ABSOLUTELY SURE that you know what to do and how to do it!" %}

- Next, create your Login Account by typing directly into the **worldserver** window the GM Command **account create**. Syntax: (see examples below)

- If you wish to set the account as a GM then type into the worldserver window: **account set gmlevel $account #level #realmid** where **$account** is the account name to change, **#level** can be 0-4 and **#realmid** is the realm ID. Setting a **#level** of "3" is GM account level (higher numbers = more access), and the "-1" is the realm ID that stands for "all realms".

{% include tip.html content="Open your **acore_world** database and find the **command** table. This shows a full list of GM Commands, descriptions, and security levels.<br/>This will always be the most up-to-date list you can find, assuming you keep your DB and Core updated." %}

- Minimize your servers and run **WoW** (never run WoW using the Launcher unless you edited the realmlist.wtf's patchlist option above).

- Log in using the user/pass you just created.

- The AzerothCore realm should be selectable. Log in, create a character, and you're all done!

## Creating an Account

Read [creating accounts](creating-accounts.md).

## Setting up Remote Access
For development purposes, this step is not necessary. However, for increased security when you want other people to make accounts you should set up a registration form, so you don't have to paste their passwords. Check out [Remote Access](remote-access.md) on how to send commands into the server.

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
| [<< Step 5: Networking](networking.md) | [Step 7: Keeping the Server Up-to-Date >>](keeping-the-server-up-to-date.md) |

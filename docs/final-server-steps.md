# Final Server Steps

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 5: Networking](networking.md) | [Step 7: Keeping the Server Up-to-Date >>](keeping-the-server-up-to-date.md) |

## Starting the server

- Run authserver and worldserver in your build folder.

**NEVER create an account directly into your database unless you are ABSOLUTELY SURE that you know what to do and how to do it!**

- Next create your Login Account by typing directly into the **worldserver** window the GM Command **account create**. Syntax: (see examples below)

- If you wish to set the account as a GM then type into the worldserver window: **account set gmlevel $account #level #realmid** where **$account** is the account name to change, **#level** can be 0-4 and **#realmid** is the realm ID. Setting a **#level** of "3" is GM account level (higher numbers = more access), and the "-1" is the realm ID that stands for "all realms".

*Tip: Open your **acore_world** database and find the **command** table. This shows a full list of GM Commands, descriptions and security level.*
*This will always be the most up-to-date list you can find, assuming you keep your DB and Core updated.*

- Minimize your servers and run **WoW** (never run WoW using the Launcher unless you edited the realmlist.wtf's patchlist option above).

- Log in using the user/pass you just created.

- The AzerothCore realm should be selectable. Log in, create a character, and you're all done!

## Account Creation

**To create an account**

```
account create <user> <pass>
```

**To set your account security level**

```
account set gmlevel <user> 3 -1
```

**Changing password**

```
account set password <user> <password> <password>
```

<br>

## Help

If you are still having problems, check:

* [How to ask for help](How-to-ask-for-help.md)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 5: Networking](networking.md) | [Step 7: Client Setup >>](client-setup.md) |

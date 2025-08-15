# Final Server Steps

| Installation Guide                                                                                                                   |                                                                           |
| :----------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------ |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 5: Networking](networking)                                                                                                  | [Step 7: Keeping the Server Up-to-Date >>](keeping-the-server-up-to-date) |

## Starting the server

1. Start `authserver`, in the `Build` folder you created, under `\bin\RelWithDebInfo` (for Windows) or `env/dist/bin` (for Linux).
2. Start `worldserver` in the same location.

For detailed information on how to configure a restarter and a debugger go to [how-to-restart-and-debug](how-to-restart-and-debug) page (For linux environments).


## Creating an Account

Read [creating accounts](creating-accounts).

{% include warning.html content="NEVER create an account directly into your database unless you are ABSOLUTELY SURE that you know what to do and how to do it!" %}

- Inside of the World of Warcraft Folder (`3.3.5` not `3.4.x` "modern" version), you will see a `Data` folder and a locale folder inside of `Data` example `enUS` or `enGB`, inside of that folder **should exist** a `realmlist.wtf` (in the case it doesn't exist, create it).

{% include tip.html content="In the case you created realmlist.wtf file and doesn't work, make sure you've -Hide extensions for known file types- unchecked in your windows folder options." %}

- Open `realmlist.wtf` and `set realmlist 127.0.0.1` (or you can change the IP or use a DNS).

- Open your `wow.exe` not any launcher of any sort.

- Login into your account by using your `username` and `password` the e-mail functionality doesn't work (as a login into client) for AzerothCore.

- The AzerothCore realm should be selectable. Log in, create a character, and you're all done!

{% include tip.html content="In the case you're connecting to the server in the same machine as the client, and the realm gets stuck (as you can't do anything after logging in) trying pressing ENTER in the worldserver.exe (this for windows issue), we recommend disabling Windows Terminal -QuickEdit Mode- which tends to hang the CLI applications for Windows 10 and foward." %}


If you want to see the `GM Commands` in your server, you can check your `acore_world` database and find the `command` table. This shows a full list of GM Commands, descriptions, and security levels.<br/>This will always be the most up-to-date list you can find, assuming you keep your DB and Core updated.

You also may also refer to the wiki [GM Commands](gm-commands).

Highely recommend also if you want to have a similiar expeirence of wowhead [wowgaming](https://wowgaming.github.io/) provides us with an similiar but focused on Azerothcore, wowgaming's [aowow](https://wowgaming.altervista.org/aowow/) version.

This similiar version of wowhead, doesn't update with your changes, they use their own `Data` they provided previously in the server setup steps and they keep their website updated every week based on azerothcore's updates to the core.


## Setting up Remote Access
For development purposes, this step is not necessary. However, for increased security when you want other people to make accounts you should set up a registration form, so you don't have to paste their passwords. Check out [Remote Access](remote-access) on how to send commands into the server.

Also refer to [account](account) which provides some `php` examples how do Calculate, Get and Verify `SRP6` protocol, in the addition of trying to make a way to create or access account information related to Azerothcore.

In addition to it we provide a [catologue](https://www.azerothcore.org/catalogue.html) mainly focused in modules created by the community, but you may find others like a Registration page.

## Help

{% include help.html %}

| Installation Guide                                                                                                                   |                                                                           |
| :----------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------ |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 5: Networking](networking)                                                                                                  | [Step 7: Keeping the Server Up-to-Date >>](keeping-the-server-up-to-date) |

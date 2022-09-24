# Networking

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click on the previous link to easily move between the steps. |
| [<< Step 4: Database Installation](database-installation.md) | [Step 6: Final Server Steps >>](final-server-steps.md) |

This guide is intended for advanced setups or just to provide more details in setting up your realm for local or internet use. In general the default setup explained in your particular OS specific guide should be fine for simple setups.

## Worldserver and Authserver configurations

For almost all basic setup scenarios the default localhost (127.0.0.1) IP settings should be left alone. The default bindip (0.0.0.0) should be left alone as well.

### Setting the auth database realmlist for internet connections

This is where you have to use your internet IP so clients from the internet can find your server. You have to have the ports 3724 (authserver) and 8085 (worldserver) forwarded or open from your router / firewall.

**Realmlist Table**

You need to make sure that your **authserver** application directs incoming connections to your realm.

- Run your chosen database management tool (ex. SQLYog or HeidiSQL) or with the MySQL command-line interface (CLI).

- If you need to connect to your database from one external machine, read https://www.enovision.net/mysql-ssh-tunnel-heidisql instead open ports to mysql server.

- Open the **acore_auth** database and find the **realmlist** table. You need to edit the **address field** according to your needs:

    - LAN IP (192.168.x.x) - If you are installing AzerothCore on a different computer from where you run WoW, but all the computers involved are on the same network (router) use that computer's Local Area Network IP.

    - 127.0.0.1 - Also known as "localhost". Leave this setting alone here and in your configs if you've installed AzerothCore on the same computer you run WoW on, and only you are connecting to it.

    - External IP – If you want other people to connect to your server, use your external IP. Visit http://www.whatismyip.com/ to find your external IP address.

 - MySQL CLI Commands (This step is not needed if you used a MySQL Manager like HeidiSQL)
    - `$ sudo mysql`
    - You should see a prompt change to mysql>
    - use acore_world;
    - **Replace your IP with the one you've chosen to use from above**
    - `UPDATE realmlist SET address = '[your_ip]' WHERE id = 1;`
    - exit
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
| [<< Step 4: Database Installation](database-installation.md) | [Step 6: Final Server Steps >>](final-server-steps.md) |

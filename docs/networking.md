# Networking

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 4: Database Installation](database-installation) | [Step 6: Final Server Steps >>](final-server-steps) |

This guide is intended for advanced setups or just to provide more details in setting up your realm for local or internet use. In general, the default setup explained in your particular OS-specific guide should be fine for simple setups.

## Worldserver and Authserver configurations

For almost all basic setup scenarios the default localhost (127.0.0.1) IP settings should be left alone. The default bindip (0.0.0.0) should be left alone as well.

### Setting the auth database realmlist for internet connections

This is where you have to use your internet IP so clients from the internet can find your server. You have to have the ports 3724 (authserver) and 8085 (worldserver) forwarded or open from your router/firewall. Using TCP protocol.

**Realmlist Table**

You need to make sure that your **authserver** application directs incoming connections to your realm.

- Run your chosen database management tool (ex. SQLYog or HeidiSQL) or with the MySQL command-line interface (CLI).

- If you need to connect to your database from one external machine, read https://www.enovision.net/mysql-ssh-tunnel-heidisql instead open ports to the MySQL server.

- Open the **acore_auth** database and find the **realmlist** table. You need to edit the **address field** according to your needs:

    - LAN IP (192.168.x.x) - If you are installing AzerothCore on a different computer from where you run WoW, but all the computers involved are on the same network (router) use that computer's Local Area Network IP.

    - 127.0.0.1 - Also known as "localhost". Leave this setting alone here and in your configs, if you've installed AzerothCore on the same computer you run WoW on, and only you are connecting to it.

    - Public IP address – If you want other people to connect to your server, use your external IP. Visit http://www.whatismyip.com/ to find your external IP address. 
        -  If you're hosting it from a home network you'll likely need to set up the proper port forwards, which isn't covered within the scope of this guide. https://portforward.com has guides for most routers, and your Internet Service Provider should be able to assist with this. 
    
    - Fully qualified domain name - (mydomain.com or warcraft.mydomain.com) Similar to an external IP address, this would be used if you want other people to connect to your server with the added benefit of not needing to track a potentially dynamic IP address. 
        - Similar to the Public IP address, it's likely that you'll need to set up port forwards if you're hosting from a home network.
        - Additionally, you'll need to configure DNS to point to the server's public IP address. Setting up DNS is out of the scope of this guide, though your domain registrar or dynamic DNS provider should have this documentation available.

{% include note.html content="If you are using HeidiSQL, make sure you are in the Data tab when you edit values." %}

 - MySQL CLI Commands (This step is not needed if you used a MySQL Manager like HeidiSQL)
    - `$ sudo mysql`
    - You should see a prompt change to mysql>
    - `use acore_auth`;
    - **Replace your IP with the one you've chosen to use from above**
    - `UPDATE realmlist SET address = '[your_ip]' WHERE id = 1;`
    - exit
<br>

## Help

If you are still having problems, check:

* [FAQ](faq)

* [Common Errors](common-errors)

* [How to ask for help](how-to-ask-for-help)

* [Join our Discord Server](https://discord.gg/gkt4y2x), but it is not a 24/7 support channel. A staff member will answer you whenever they have time.

| Installation Guide | |
| :- | :- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 4: Database Installation](database-installation) | [Step 6: Final Server Steps >>](final-server-steps) |

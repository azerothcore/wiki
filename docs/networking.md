# Networking

| Installation Guide                                                                                                                   |                                                     |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 4: Database Installation](database-installation)                                                                            | [Step 6: Final Server Steps >>](final-server-steps) |

This guide is intended for advanced setups or just to provide more details in setting up your realm for local or internet use. In general, the default setup explained in your particular OS-specific guide should be fine for simple setups.

## Authserver and Worldserver configurations

For the majority of the cases the default configuration values for `LoginDatabaseInfo`, `CharacterDatabaseInfo` and `WorldDatabaseInfo` should be left alone as `127.0.0.1` (also known as `localhost`, the current machine hosting/running the `authserver` and `worldserver`), the same goes for `BindIP` should be left alone as well as `0.0.0.0`.

If you need to connect to your database from one external machine, read [this](https://www.enovision.net/mysql-ssh-tunnel-heidisql) instead of opening ports to the MySQL server.

### Port Forwarding (Incoming / Inbound)

| DST Port | Protocol | Destination | Comment     |
| -------- | -------- | ----------- | ----------- |
| 3724     | TCP      | any         | authserver  |
| 8085     | TCP      | any         | worldserver |

This are the ports used by the `authserver` and `worldserver` which you will be required to port foward / open the ports in your router and/or firewall to allow external connections to your server.

How to [port foward](https://portforward.com), this is for majority of routers, not all.

You need to make sure that your **authserver** application directs incoming connections to your server, normally is windows issue under the `UAC` (User Account Control), which will prompt after being executed once, normally.

{% include warning.html content="NEVER open your MYSQL Ports (normally 8085) unless you are ABSOLUTELY SURE that you know what to do, no one but the machine hosting the service should have access to it." %}


### Realmlist

Open the `acore_auth` database and find the `realmlist` table. 

`acore_auth.realmlist`
| id | name | address | localAddress | localSubnetMask | port |
| ---: | --- | --- | --- | --- | ---: |
| 1 | AzerothCore | 127.0.0.1| 127.0.0.1| 255.255.255.0 | 8085 |

The table above is snippet how `realmlist` under `acore_auth` database looks.

- `id` - Is a primary key (unique number per row), auto-incrementing (increases automatically when a new entry).
- `name` - Is a unique key (unique column name), this refers to `Realm` name that appears in-game and `authserver`.
- `address` - Referes to the machine hosting's [Public IP](http://www.whatismyip.com/), which is the IP people use to connect to your server (outside / externally of your network), for some cases is the **DNS** ("domain name").
- `localAddress` - Referes to the machine hosting's **Local** / **LAN IP**, which is the IP you and other people use to connect to your server (within / inside of your network), for some cases where you're using **DNS** as your `address` field, you may use the machine hosting's [Public IP](http://www.whatismyip.com/) in `localAddress` field.
- `localSubnetMask` - This only should be changed by people who know what they are doing, beginners shoudln't have to care about the correct usage SubnetMask for their IP category, so leave as it is.
- `port` - This refers to `mysql` service port being used, by default is `8085` which is the default one in `mysql` also.

If you leave the default values of `127.0.0.1` only the client in the same machine as that's hosting the server will be able to connect, for this cases where you wish to join from another computer in the same network make sure you change `localAddress` to match the **Local IP** of the machine that's hosting the server.

Same applies for `address` but machine as that's hosting the server's [Public IP](http://www.whatismyip.com/) which is can be used to connect from a computer outside of the network, some routers have `hairpinning` which allow you to use machine's [Public IP](http://www.whatismyip.com/) to connect within the same network.

`DNS` technical:
- Fully qualified domain name - (mydomain.com or warcraft.mydomain.com) Similar to an external IP address, this would be used if you want other people to connect to your server with the added benefit of not needing to track a potentially dynamic IP address.
- Similar to the Public IP address, it's likely that you'll need to set up port forwards if you're hosting from a home network.
- Additionally, you'll need to configure DNS to point to the server's public IP address. Setting up DNS is out of the scope of this guide, though your domain registrar or dynamic DNS provider should have this documentation available.


Using any of database client refered in the requirements page (HeidiSQL, MySQL command-line interface [CLI], etc... or others your choice) you may change any of column's values by a simple SQL query.

### HeidiSQL (most popular for newer users of MySQL).
- Click once in `acore_auth` within that database click once in `realmlist` and in the `Query` tab run the query below.

Alternative you may use the UI by going to `Data` (not `Table: realmlist`) tab and change the values manually (by double clicking in them).

### MySQL CLI (most popular for linux users.)
- In your terminal of choice (example given for `CMD` of Windows, which is recommended to be ran as `Administrator`) 

`mysql -u acore -p -h 127.0.0.1 acore_auth`

(This will prompt your password after being executed)

Example:

```
UPDATE `realmlist` SET `address` = "21.0.1.59", `localAddress` = "192.168.1.50"  WHERE `id` = 1;
```

This will change the [Public IP](http://www.whatismyip.com/) to `21.0.1.59` and the **Local IP** to `192.168.1.50` where the `Realm ID` is `1` (by default is `AzerothCore`).

## Help

{% include help.html %}

| Installation Guide                                                                                                                   |                                                     |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 4: Database Installation](database-installation)                                                                            | [Step 6: Final Server Steps >>](final-server-steps) |

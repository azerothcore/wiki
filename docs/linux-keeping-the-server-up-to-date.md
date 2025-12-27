# Linux Keeping the Server Up-to-Date

| Installation Guide                                                                                                                   |                                         |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 6: Final Server Steps](final-server-steps)                                                                                  | [Step 8: Client Setup >>](client-setup) |

## Keeping the source Up-to-Date

```sh
cd ~/azerothcore/
git pull origin master
```

Rebuild the changes you pulled.

```sh
cd build
make -j 8; make install
```

Sometimes we add or remove files from the repository. At that point it is necessary to recompile the server, the same way as it was installed the first time [in the Linux Core Installation](linux-core-installation#configuring-for-compiling).

## Using automation server
If you would like to update AzerothCore using Jenkins, Teamcity or similar tool, following steps might help you.

Add required commands to sudoers file. Services bellow were created [in the Linux Core Installation](linux-core-installation#services)
```sh
sudo visudo

%sudo ALL=NOPASSWD: /usr/sbin/service worldserver start
%sudo ALL=NOPASSWD: /usr/sbin/service authserver start
%sudo ALL=NOPASSWD: /usr/sbin/service worldserver stop
%sudo ALL=NOPASSWD: /usr/sbin/service authserver stop
%sudo ALL=NOPASSWD: /srv/azerothcore-wotlk/acore.sh compiler all
```

Run commands in Jenkins/Teamcity
```sh
sudo service worldserver stop
sudo service authserver stop

cd /srv/azerothcore-wotlk
git pull origin master

sudo /srv/azerothcore-wotlk//acore.sh compiler all

sudo service worldserver start
sudo service authserver start
```


## Keeping the Database Up-to-Date

Read [Database Keeping the Server Up-to-Date](database-keeping-the-server-up-to-date)

<br>

## Help

{% include help.html %}

| Installation Guide                                                                                                                   |                                         |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------- |
| This article is a part of the Installation Guide. You can read it alone or click the previous link to easily move between the steps. |
| [<< Step 6: Final Server Steps](final-server-steps)                                                                                  | [Step 8: Client Setup >>](client-setup) |

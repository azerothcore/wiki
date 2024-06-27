# AzerothCore Debian 12 Quick Install Guide

This is a streamlined guide for installing AzerothCore to a Debian 12 server, securing it, and enabling one-command maintenance from your Windows PC.
## Table of Contents

1. [Requirements](#requirements)
2. [Debian Setup](#debian-setup)
    1. [First Login](#first-login)
    2. [Change Default Password](#change-default-password)
    3. [Change Default SSH Port](#change-default-ssh-port)
    4. [Setup Firewall](#setup-firewall)
    5. [Get Dependencies](#get-dependencies)
    6. [Install SQL Database](#install-sql-database)
3. [SSH Setup](#ssh-setup)
    1. [Key Generation](#key-generation)
    2. [Key-Based Login Setup](#key-based-login-setup)
    3. [Disable Password Logins](#disable-password-logins)
4. [AzerothCore Installation](#azerothcore-installation)
    1. [Clone Repository](#clone-repository)
    2. [Get Data Files](#get-data-files)
    3. [Add Anticheat Module](#add-anticheat-module)
    4. [Build Core](#build-core)
    5. [Edit Configs](#edit-configs)
    6. [Set Realm IP](#set-realm-ip)
    7. [Launch Server](#launch-server)
    8. [Create GM Account](#create-gm-account)
5. [Maintenance](#maintenance)
    1. [Create Alias Command](#create-alias-command)
    2. [Update AzerothCore](#update-azerothcore)

## Requirements

##### [PuTTY](https://www.putty.org/)
- A Windows program for sending commands to the server.
##### [FileZilla](https://filezilla-project.org/download.php)
- A Windows program for transferring files to/from the server.
##### [HeidiSQL](https://www.heidisql.com/)
- A Windows program for connecting to the servers SQL database.
##### [Debian 12](https://www.ovhcloud.com/en-ca/vps/)
- A server with Debian 12 installed. (ex: 4gb/4core VPS from OVH)

---
## Debian Setup
### First Login

- Use **PuTTY** to connect to your Debian server using the IP address and login credentials supplied by the hosting provider.
- Copy the following code blocks and paste them into the PuTTY terminal with right click, then hit enter.
### Change Default Password
```bash
passwd
```
### Change Default SSH Port
```bash
sudo sed -i 's/^#Port 22\+$/Port 55022/' /etc/ssh/sshd_config
sudo systemctl restart sshd
```
### Setup Firewall
```bash
sudo apt install ufw
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 55022
sudo ufw allow 3724
sudo ufw allow 8085
sudo ufw enable
```
### Get Dependencies
```bash
sudo apt update && sudo apt full-upgrade -y
sudo apt install git cmake make gcc g++ clang libssl-dev libbz2-dev libreadline-dev libncurses-dev libboost-all-dev mariadb-server mariadb-client libmariadb-dev libmariadb-dev-compat build-essential p7zip-full screen fail2ban -y
```
### Install SQL Database
```bash
sudo mysql_secure_installation
```
- **-/N/Y/Y/Y/Y/Y**
```bash
sudo mysql -u root -p
```
- Enter the root password you just set up.
```bash
DROP USER IF EXISTS 'acore'@'localhost';
CREATE USER 'acore'@'%' IDENTIFIED BY 'NEWPASSWORD';
GRANT ALL PRIVILEGES ON * . * TO 'acore'@'%';
GRANT ALL PRIVILEGES ON `acore_world` . * TO 'acore'@'%';
GRANT ALL PRIVILEGES ON `acore_characters` . * TO 'acore'@'%';
GRANT ALL PRIVILEGES ON `acore_auth` . * TO 'acore'@'%';
exit
```
- Change **NEWPASSWORD** to something more secure.
---
## SSH Setup

### Key Generation
#### Debian Public Key
```bash
ssh-keygen -t ed25519 -C "Debian12"
cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
```
#### Windows Private Key
- Use **Filezilla** to connect to the server and navigate to `home/debian/ssh/`
- Copy the `id_ed25519` file to your PC and load it into **puttygen.exe** (located in the PuTTY folder) 
- Generate a private key `.ppk` file. Store this file somewhere safe and make a backup.
### Key-based Login Setup
#### PuTTY
![PuTTY1](https://github.com/aradep/wiki/assets/61268368/1ccb09ec-2df2-4798-874b-6346bf237487)
![PuTTY2](https://github.com/aradep/wiki/assets/61268368/6e5ebe8b-7416-4e69-a030-a88d13fde26e)
#### FileZilla
![FileZilla](https://github.com/aradep/wiki/assets/61268368/83e35326-db88-4aed-828c-e29fa0cd167e)
#### HeidiSQL
![HeidiSQL1](https://github.com/aradep/wiki/assets/61268368/f3b927dc-94f1-491e-a000-1125a0c1544f)
![HeidiSQL2](https://github.com/aradep/wiki/assets/61268368/689de88e-8bf8-4171-af7c-710f296e793d)
### Disable Password Logins
- **After confirming that key-based login works**, disable password logins to enhance SSH security.
```bash
sudo sed -i -E 's/#?PasswordAuthentication yes/PasswordAuthentication no/' ~/etc/ssh/sshd_config
sudo rm /etc/ssh/sshd_config.d/*
sudo service ssh restart
```

---

## AzerothCore Installation

### Clone Repository
```bash
git -C ~/ clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore
```
### Add Anticheat Module
```bash
git -C ~/azerothcore/modules clone https://github.com/azerothcore/mod-anticheat
cp -n ~/azerothcore/modules/mod-anticheat/conf/Anticheat.conf.dist ~/server/etc/Anticheat.conf 
```
### Get Data Files
```bash
mkdir -p ~/server/data && cd ~/server/data
wget https://github.com/wowgaming/client-data/releases/download/v16/data.zip
7z x data.zip && rm data.zip
```
### Build Core
```bash
mkdir -p ~/azerothcore/build && cd ~/azerothcore/build
cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS_BUILD=db-only -DSCRIPTS=static -DMODULES=static
make -j $(nproc) install
```
### Edit Configs
```bash
cp -n ~/server/etc/authserver.conf.dist ~/server/etc/authserver.conf
cp -n ~/server/etc/worldserver.conf.dist ~/server/etc/worldserver.conf
sudo sed -i -E 's|^DataDir = .*|DataDir = "/home/USERNAME/server/data"|' ~/server/etc/worldserver.conf
sudo sed -i -E 's/= "127.0.0.1;3306;acore;acore;/= "127.0.0.1;3306;acore;NEWPASSWORD;/' ~/server/etc/*.conf
```
- Change **USERNAME** to your Debian user.
- Change **NEWPASSWORD** to the password you used earlier during the [SQL database setup](#install-sql-database).
### Set Realm IP
```bash
sudo mysql -u root -p
```

```sql
UPDATE acore_auth.realmlist SET address = '0.0.0.0' WHERE id = 1;
```
- Change **0.0.0.0** to the public IP address of your Debian12 server.
### Launch Server
```bash
screen -AmdS auth ~/server/bin/authserver
screen -AmdS world ~/server/bin/worldserver
screen -r world
```

### Create GM account
```bash
account create USERNAME PASSWORD
account set gmlevel USERNAME 3 -1
```

- **To exit screen:** Ctrl+A -> Ctrl+D
- **To kill process:** Ctrl+C

---
## Maintenance
### Create Alias Command
```bash
touch ~/.bash_aliases
echo "alias acoreupdate='
screen -S world -p 0 -X stuff "saveall^m";
screen -X -S "world" quit;
git -C ~/azerothcore/modules/mod-anticheat pull;
git -C ~/azerothcore pull;
cd ~/azerothcore/build;
cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS_BUILD=db-only -DSCRIPTS=static -DMODULES=static;
make -j $(nproc) install;
screen -AmdS world ~/server/bin/worldserver;
screen -r world;'" > ~/.bash_aliases
source ~/.bashrc
```

- Now we can **save/exit** the worldserver, **pull** the latest changes from GitHub, **build** the updated core, and **restart** the worldserver all with one command.
### Update AzerothCore
```
acoreupdate
```

## Finish!

- You should now be able to connect to the AzerothCore server by setting your realmlist to the public IP address of the Debian12 server. ex: `set realmlist 0.0.0.0`

---
## Common Problems

#### Auth/Worldserver wont even start.
- Make sure you [created the .conf files](#edit-configs) and matched the password of the [SQL user](#install-sql-database).
#### Successful login but cant enter the realm.
- Double check the [realm address.](#set-realm-ip)

---
##### Good things to know that this guide does not cover.
- Domain name and DNS setup for *"set realmlist logon.server.com"*
- Wordpress registration site & acore-cms plugin SOAP connection.
- Automated database backups to Google Drive using cron and rclone.

## Other Resources
- [Official AzerothCore Installation Guide](https://www.azerothcore.org/wiki/installation)
- [heyaapl's Debian Tutorial](https://www.azerothcore.org/wiki/digital-ocean-video-tutorial)
- [Digital Scriptorium's Video](https://www.youtube.com/watch?v=k4i4za1Scgg)

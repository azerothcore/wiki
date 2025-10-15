# AzerothCore Debian 12 Install Guide

This is a quickstart guide for installing AzerothCore to a Debian 12 server from your Windows PC. For a more in-depth tutorial, see the [official AzerothCore Installation Guide](installation).


## Table of Contents
  - [Requirements](#requirements)
  - [Debian Setup](#debian-setup)
  - [SSH Setup](#ssh-setup)
  - [AzerothCore Installation](#azerothcore-installation)
  - [Maintenance](#maintenance)
  - [Common Problems](#common-problems)
  - [Other Resources](#other-resources)

## Requirements
##### [PuTTY](https://www.putty.org/)
- A Windows program for sending commands to the server.
##### [Debian 12](https://www.ovhcloud.com/en-ca/vps/)
- A server with Debian 12 installed. (ex: 4gb/4core VPS from OVH)

#### Optional
  ##### [HeidiSQL](https://www.heidisql.com/)
  - A Windows program for connecting to the servers SQL database. Not used in this guide. If you want to connect to your database using HeidiSQL, [read this](https://www.enovision.net/mysql-ssh-tunnel-heidisql)

---
## Debian Setup
### First Login

- Use **PuTTY** to connect to your Debian server using the IP address and login credentials supplied by the hosting provider.
- For each step copy the entire code block and paste it into the PuTTY terminal with right click, then hit enter.
  <details><summary>If you're logged in as root...</summary>
    
    #### Create a new user with sudo privileges and switch to it.
    ```bash
    read -p "New username: " USERNAME
    adduser "$USERNAME"
    usermod -aG sudo "$USERNAME"
    su - "$USERNAME"
    ```
    #### Disable remote root login
    ```bash
    sudo sed -i 's/^#\?PermitRootLogin .*/PermitRootLogin no/' /etc/ssh/sshd_config
    sudo systemctl reload ssh
    ```
  </details>

### Change Default SSH Port
```bash
sudo sed -i 's/^#Port 22\+$/Port 55022/' /etc/ssh/sshd_config
sudo systemctl restart sshd
```
*(Remember to use 55022 as the SSH port from now on)*
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
sudo apt update && sudo apt install git cmake make gcc g++ clang libssl-dev libbz2-dev libreadline-dev libncurses-dev libboost-all-dev lsb-release gnupg wget p7zip-full nodejs npm fail2ban -y && sudo npm install pm2 -g
```
### Get MySQL
- Visit the [MySQL APT repository](https://dev.mysql.com/downloads/repo/apt/) to verify the latest version.
```bash
# Version
MYSQL_APT_CONFIG_VERSION=0.8.34-1
# # # # #
mkdir -p ~/mysqlpackages && cd ~/mysqlpackages
# Download
wget "https://dev.mysql.com/get/mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb"
wget "https://dev.mysql.com/downloads/gpg/?file=mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb&p=37" -O mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb.asc
# Verify
gpg --keyserver keyserver.ubuntu.com --recv-keys A8D3785C
gpg --verify mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb.asc mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
# Install
sudo DEBIAN_FRONTEND="noninteractive" dpkg -i ./mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
sudo apt update
sudo DEBIAN_FRONTEND="noninteractive" apt install -y mysql-server libmysqlclient-dev
# Cleanup
rm -v mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all* && unset MYSQL_APT_CONFIG_VERSION
```

### Setup SQL Database
```bash
sudo mysql <<'EOF'
DROP USER IF EXISTS 'acore'@'localhost';
CREATE USER 'acore'@'localhost' IDENTIFIED BY 'acore' WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0;
CREATE DATABASE IF NOT EXISTS `acore_world` DEFAULT CHARACTER SET UTF8MB4 COLLATE utf8mb4_unicode_ci;
CREATE DATABASE IF NOT EXISTS `acore_characters` DEFAULT CHARACTER SET UTF8MB4 COLLATE utf8mb4_unicode_ci;
CREATE DATABASE IF NOT EXISTS `acore_auth` DEFAULT CHARACTER SET UTF8MB4 COLLATE utf8mb4_unicode_ci;
GRANT ALL PRIVILEGES ON `acore_world`.* TO 'acore'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON `acore_characters`.* TO 'acore'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON `acore_auth`.* TO 'acore'@'localhost' WITH GRANT OPTION;
EOF
```
---

## SSH Setup
This is an **optional** step that involves creating a key file and disabling password-based SSH logins to increase security of the Debian server and SQL database.

<details><summary>▫️▫️▫️</summary>
  
### FileZilla
  - This step requires [FileZilla](https://filezilla-project.org/download.php), a Windows program for transferring files to/from the server.

### Key Generation
#### Debian Public Key
```bash
ssh-keygen -t ed25519 -C "Debian12"
cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
```
#### Windows Private Key
- Use **Filezilla** to connect to the server and navigate to `home/USERNAME/ssh/`
- Copy the `id_ed25519` file to your PC and load it into **puttygen.exe** (located in the PuTTY folder) 
- Generate a private key `.ppk` file. Store this file somewhere safe and make a backup.
### Key-based Login Setup

<details>
<summary>PuTTY</summary>
  
![PuTTY1](https://github.com/azerothcore/wiki/assets/61268368/6210d43d-a7c4-4444-b896-4f23a2ee415f)
![PuTTY2](https://github.com/azerothcore/wiki/assets/61268368/e39e5a4f-f93f-4a69-9d9c-785bd98afdbd)
</details>

<details>
<summary>FileZilla</summary>
  
#### FileZilla
![FileZilla](https://github.com/azerothcore/wiki/assets/61268368/d45e952a-4f3b-4c38-9cdb-b72f5bc76651)
</details>

<details>
<summary>HeidiSQL</summary>

![HeidiSQL12](https://github.com/user-attachments/assets/b23a37d2-774e-4a47-b5b5-2bb2ba73c690)
![HeidiSQL2](https://github.com/azerothcore/wiki/assets/61268368/4043857a-2d1e-4c5b-bb61-2d76ed8a5514)
</details>

### Disable Password Logins
- **After confirming that key-based login works**, disable password logins.
```bash
sudo sed -i -E 's/#?PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo rm /etc/ssh/sshd_config.d/*
sudo service ssh restart
```
</details>

---
## AzerothCore Installation
### Clone Repository
```bash
git -C ~/ clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore
```
### Add Anticheat Module
```bash
git -C ~/azerothcore/modules clone https://github.com/azerothcore/mod-anticheat
```
### Get Data Files
```bash
rm -rf ~/server/data &&
mkdir -p ~/server/data && cd ~/server/data &&
wget https://github.com/wowgaming/client-data/releases/download/v17/data.zip &&
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
# Copy .dist
cp -n ~/server/etc/authserver.conf.dist ~/server/etc/authserver.conf
cp -n ~/server/etc/worldserver.conf.dist ~/server/etc/worldserver.conf
cp -n ~/server/etc/modules/Anticheat.conf.dist ~/server/etc/modules/Anticheat.conf
# Data Directory
sudo sed -i -E "s|^DataDir = .*|DataDir = \"/home/$USER/server/data\"|" ~/server/etc/worldserver.conf
# Logs Directory
sudo sed -i -E "s|^LogsDir = .*|LogsDir = \"/home/$USER/server/logs\"|" ~/server/etc/*.conf
mkdir -p ~/server/logs
```
### Launch Server
```bash
pm2 start $HOME/server/bin/authserver --name authserver -- -c $HOME/server/etc/authserver.conf
pm2 start $HOME/server/bin/worldserver --name worldserver -- -c $HOME/server/etc/worldserver.conf
eval "$(pm2 startup | grep sudo)"
pm2 save
pm2 attach $(pm2 id worldserver | tr -d '[][:space:]')
```
### Create GM account
```bash
account create USERNAME PASSWORD
```
```bash
account set gmlevel USERNAME 3 -1
```
- Detach from the worldserver with Ctrl+C.

### Set Realm IP
```bash
sudo mysql <<'EOF'
UPDATE `acore_auth`.`realmlist` SET `address` = 'x.x.x.x' WHERE `id` = 1;
EOF
```
- Change **x.x.x.x** to the public IP address of your Debian12 server.
## Finish!

- You should now be able to log into AzerothCore by setting your WoW clients realmlist.wtf to the public IP address of the Debian12 server. ex: `set realmlist 12.345.67.890`

</details>

---

## Maintenance

### Change SQL Password
- This changes the password for the acore database user. The guide uses default "acore/acore" SQL credentials.
```bash
# Prompt for new password
while true; do read -s -p "Set a new SQL password: " MYSQL_PASSWORD && echo; read -s -p "Retype SQL password: " MYSQL_PASSWORD_CONFIRM && echo; [ "$MYSQL_PASSWORD" = "$MYSQL_PASSWORD_CONFIRM" ] && break || echo "Passwords did not match."; done; unset MYSQL_PASSWORD_CONFIRM
# Update SQL user
sudo mysql <<EOF
ALTER USER 'acore'@'localhost' IDENTIFIED BY '${MYSQL_PASSWORD}';
FLUSH PRIVILEGES;
EOF
# Update configs
sudo sed -i -E "s|= \"127.0.0.1;3306;acore;[^;]*;|= \"127.0.0.1;3306;acore;${MYSQL_PASSWORD};|" ~/server/etc/*.conf
# Cleanup
unset MYSQL_PASSWORD
```
### Modify Config Files
- This script can be extended to include all your preferred config settings. Running it will **delete the .conf files** and remake them from the .dist before applying changes.
```bash
#!/bin/bash
# Helper: Reset and update configs
update_config() {
    local config_file="$1"
    declare -n settings="$2"
    cp -f "${config_file}.dist" "$config_file"
    for key in "${!settings[@]}"; do
        sudo sed -i -E "s|^($key\s*=\s*).*|\1${settings[$key]}|" "$config_file"
    done
}
# Authserver.conf
declare -A auth_settings=(
    ["LogsDir"]="\"$HOME/server/logs\""
)
# Worldserver.conf
declare -A world_settings=(
    ["DataDir"]="\"$HOME/server/data\""
    ["LogsDir"]="\"$HOME/server/logs\""
    ["StartPlayerLevel"]="1"
)
# Anticheat.conf
declare -A anticheat_settings=(
    ["LogsDir"]="\"$HOME/server/logs\""
)
#### Add your modules here ####

# Apply updates
update_config "$HOME/server/etc/authserver.conf" auth_settings
update_config "$HOME/server/etc/worldserver.conf" world_settings
update_config "$HOME/server/etc/modules/Anticheat.conf" anticheat_settings
#### Add your modules here ####
```
### Core Update Command
- This creates a shortcut command to automate the core update process. 
```bash
cat <<'EOF' >> ~/.bash_aliases
alias acoreupdate='
WORLD_ID="$(pm2 id worldserver | tr -d "[][:space:]")"
CORE_UPDATED=0

# Helper: Check for updates
update_repo() {
    local REPO_PATH="$1"
    git -C "$REPO_PATH" fetch origin
    LOCAL_HASH=$(git -C "$REPO_PATH" rev-parse HEAD)
    REMOTE_HASH=$(git -C "$REPO_PATH" rev-parse "@{upstream}")
    if [ "$LOCAL_HASH" != "$REMOTE_HASH" ]; then
        git -C "$REPO_PATH" pull
        CORE_UPDATED=1
    fi
}

# Helper: Build and restart
update_core() {
    cd "$HOME/azerothcore/build" &&
    cmake ../ -DCMAKE_INSTALL_PREFIX="$HOME/server/" -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS_BUILD=db-only -DSCRIPTS=static -DMODULES=static &&
    make -j "$(nproc)" install &&
    pm2 send "$WORLD_ID" "saveall" &&
    pm2 send "$WORLD_ID" "server restart 10" &&
    echo "Restarting worldserver in 10 seconds..." &&
    sleep 12 &&
    pm2 restart "$WORLD_ID" &&
    pm2 attach "$WORLD_ID"
}

# Check for updates
update_repo "$HOME/azerothcore"
update_repo "$HOME/azerothcore/modules/mod-anticheat"
##### Add your modules here #####

# Build and restart
if [ "$CORE_UPDATED" -eq 1 ]; then update_core; else echo "AzerothCore is up-to-date."; fi
'
EOF
source ~/.bash_aliases
```

- Now you can pull the latest changes from GitHub, build the updated core, and restart the worldserver all with one command:
### Update AzerothCore
```bash
acoreupdate
```
---
### Common Problems

#### Successful login but cant enter the realm.
- Double check the [realm address.](#set-realm-ip)
#### Crash loop causing incomplete error logs.
- Stop worldserver with `pm2 stop` and start it with `pm2 start --no-autorestart` to get a full error log.
---
##### Good things to know that this guide does not cover.
- Domain name and DNS setup for *"set realmlist logon.server.com"*
- Wordpress registration site & acore-cms plugin SOAP connection.
- Automated database backups to Google Drive using cron and rclone.

### Other Resources
- [Official AzerothCore Installation Guide](installation)
- [heyaapl's Debian Tutorial](digital-ocean-video-tutorial)
- [Digital Scriptorium's Video](https://www.youtube.com/watch?v=k4i4za1Scgg)

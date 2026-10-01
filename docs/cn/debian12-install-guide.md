# AzerothCore Debian 12 安装指南

{% include note.html content="本指南由社区编写。它可能不是最新的，也不受官方支持。" %}

这是一份从 Windows 电脑将 AzerothCore 安装到 Debian 12 服务器的快速入门指南。如需更深入的教程，请参阅[官方 AzerothCore 安装指南](installation)。


## 目录
  - [环境要求](#requirements)
  - [Debian 设置](#debian-setup)
  - [SSH 设置](#ssh-setup)
  - [AzerothCore 安装](#azerothcore-installation)
  - [维护](#maintenance)
  - [常见问题](#common-problems)
  - [其他资源](#other-resources)

## 环境要求 {#requirements}
##### [PuTTY](https://www.putty.org/)
- 一个用于向服务器发送命令的 Windows 程序。
##### [Debian 12](https://www.ovhcloud.com/en-ca/vps/)
- 一台安装了 Debian 12 的服务器。（例如 OVH 的 4gb/4core VPS）

#### 可选
  ##### [HeidiSQL](https://www.heidisql.com/)
  - 一个用于连接服务器 SQL 数据库的 Windows 程序。本指南不涉及。如果你想使用 HeidiSQL 连接数据库，请[阅读这篇](https://www.enovision.net/mysql-ssh-tunnel-heidisql)

---
## Debian 设置 {#debian-setup}
### 首次登录

- 使用 **PuTTY** 通过主机提供商提供的 IP 地址和登录凭据连接到你的 Debian 服务器。
- 对于每个步骤，请复制整个代码块，然后右键粘贴到 PuTTY 终端中，再按回车。
  <details><summary>如果你以 root 身份登录...</summary>
    
    #### 创建一个具有 sudo 权限的新用户并切换过去。
    ```bash
    read -p "New username: " USERNAME
    adduser "$USERNAME"
    usermod -aG sudo "$USERNAME"
    su - "$USERNAME"
    ```
    #### 禁用远程 root 登录
    ```bash
    sudo sed -i 's/^#\?PermitRootLogin .*/PermitRootLogin no/' /etc/ssh/sshd_config
    sudo systemctl reload ssh
    ```
  </details>

### 更改默认 SSH 端口
```bash
sudo sed -i 's/^#Port 22\+$/Port 55022/' /etc/ssh/sshd_config
sudo systemctl restart sshd
```
*（从现在起请记住使用 55022 作为 SSH 端口）*
### 设置防火墙
```bash
sudo apt install ufw
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 55022
sudo ufw allow 3724
sudo ufw allow 8085
sudo ufw enable
```
### 获取依赖
```bash
sudo apt update && sudo apt install git cmake make gcc g++ clang libssl-dev libbz2-dev libreadline-dev libncurses-dev libboost-all-dev lsb-release gnupg wget p7zip-full nodejs npm fail2ban -y && sudo npm install pm2 -g
```
### 获取 MySQL
- 访问 [MySQL APT 软件仓库](https://dev.mysql.com/downloads/repo/apt/) 以验证最新版本。
```bash
# Version
MYSQL_APT_CONFIG_VERSION=0.8.36-1
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

### 设置 SQL 数据库
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

## SSH 设置 {#ssh-setup}
这是一个**可选的**步骤，涉及创建密钥文件并禁用基于密码的 SSH 登录，以提高 Debian 服务器和 SQL 数据库的安全性。

<details><summary>▫️▫️▫️</summary>
  
### FileZilla
  - 此步骤需要 [FileZilla](https://filezilla-project.org/download.php)，这是一个用于在服务器间传输文件的 Windows 程序。

### 密钥生成
#### Debian 公钥
```bash
ssh-keygen -t ed25519 -C "Debian12"
cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
```
#### Windows 私钥
- 使用 **Filezilla** 连接到服务器并导航到 `home/USERNAME/ssh/`
- 将 `id_ed25519` 文件复制到你的电脑，并加载到 **puttygen.exe** 中（位于 PuTTY 文件夹内）
- 生成一个私钥 `.ppk` 文件。将此文件存放在安全的地方并做好备份。
### 基于密钥的登录设置

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

### 禁用密码登录
- **在确认基于密钥的登录可以正常工作之后**，禁用密码登录。
```bash
sudo sed -i -E 's/#?PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo rm /etc/ssh/sshd_config.d/*
sudo service ssh restart
```
</details>

---
## AzerothCore 安装 {#azerothcore-installation}
### 克隆仓库
```bash
git -C ~/ clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore
```
### 添加反作弊模块
```bash
git -C ~/azerothcore/modules clone https://github.com/azerothcore/mod-anticheat
```
### 获取数据文件
```bash
rm -rf ~/server/data &&
mkdir -p ~/server/data && cd ~/server/data &&
wget https://github.com/wowgaming/client-data/releases/download/v19/data.zip &&
7z x data.zip && rm data.zip
```
### 构建核心
```bash
mkdir -p ~/azerothcore/build && cd ~/azerothcore/build
cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS_BUILD=db-only -DSCRIPTS=static -DMODULES=static
make -j $(nproc) install
```
### 编辑配置
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
### 启动服务器
```bash
pm2 start $HOME/server/bin/authserver --name authserver -- -c $HOME/server/etc/authserver.conf
pm2 start $HOME/server/bin/worldserver --name worldserver -- -c $HOME/server/etc/worldserver.conf
eval "$(pm2 startup | grep sudo)"
pm2 save
pm2 attach $(pm2 id worldserver | tr -d '[][:space:]')
```
### 创建 GM 账号
```bash
account create USERNAME PASSWORD
```
```bash
account set gmlevel USERNAME 3 -1
```
- 使用 Ctrl+C 从 worldserver 分离。

### 设置 Realm IP {#set-realm-ip}
```bash
sudo mysql <<'EOF'
UPDATE `acore_auth`.`realmlist` SET `address` = 'x.x.x.x' WHERE `id` = 1;
EOF
```
- 将 **x.x.x.x** 改为你的 Debian12 服务器的公网 IP 地址。
## 完成！

- 现在你应该可以通过将 WoW 客户端的 realmlist.wtf 设置为 Debian12 服务器的公网 IP 地址来登录 AzerothCore 了。例如：`set realmlist 12.345.67.890`

</details>

---

## 维护 {#maintenance}

### 更改 SQL 密码
- 这会更改 acore 数据库用户的密码。本指南使用默认的 "acore/acore" SQL 凭据。
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
### 修改配置文件
- 此脚本可以扩展以包含你所有偏好的配置设置。运行它会**删除 .conf 文件**，并在应用更改之前从 .dist 重新创建它们。
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
### 核心更新命令
- 这会创建一个快捷命令来自动化核心更新过程。
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

- 现在你可以用一条命令从 GitHub 拉取最新更改、构建更新后的核心并重启 worldserver：
### 更新 AzerothCore
```bash
acoreupdate
```
---
### 常见问题 {#common-problems}

#### 登录成功但无法进入 realm。
- 请再次检查 [realm 地址](#set-realm-ip)。
#### 崩溃循环导致错误日志不完整。
- 使用 `pm2 stop` 停止 worldserver，然后使用 `pm2 start --no-autorestart` 启动它，以获得完整的错误日志。
---
##### 本指南未涵盖但值得了解的内容。
- 域名和 DNS 设置，用于 *"set realmlist logon.server.com"*
- Wordpress 注册站点和 acore-cms 插件的 SOAP 连接。
- 使用 cron 和 rclone 自动备份数据库到 Google Drive。

### 其他资源 {#other-resources}
- [官方 AzerothCore 安装指南](installation)
- [Digital Scriptorium 的视频](https://www.youtube.com/watch?v=k4i4za1Scgg)

# Guía de instalación de AzerothCore en Debian 12

Esta es una guía de inicio rápido para instalar AzerothCore en un servidor Debian 12 desde tu PC con Windows. Para un tutorial más detallado, consulta la [Guía de instalación oficial de AzerothCore](es/installation).


## Tabla de contenidos
  - [Requisitos](#requirements)
  - [Configuración de Debian](#debian-setup)
  - [Configuración de SSH](#ssh-setup)
  - [Instalación de AzerothCore](#azerothcore-installation)
  - [Mantenimiento](#maintenance)
  - [Problemas comunes](#common-problems)
  - [Otros recursos](#other-resources)

## Requisitos {#requirements}
##### [PuTTY](https://www.putty.org/)
- Un programa de Windows para enviar comandos al servidor.
##### [Debian 12](https://www.ovhcloud.com/en-ca/vps/)
- Un servidor con Debian 12 instalado. (ej.: VPS de 4gb/4core de OVH)

#### Opcional
  ##### [HeidiSQL](https://www.heidisql.com/)
  - Un programa de Windows para conectarse a la base de datos SQL del servidor. No se usa en esta guía. Si quieres conectarte a tu base de datos usando HeidiSQL, [lee esto](https://www.enovision.net/mysql-ssh-tunnel-heidisql)

---
## Configuración de Debian {#debian-setup}
### Primer inicio de sesión

- Usa **PuTTY** para conectarte a tu servidor Debian usando la dirección IP y las credenciales de acceso proporcionadas por el proveedor de hosting.
- Para cada paso, copia el bloque de código completo y pégalo en la terminal de PuTTY con click derecho, luego presiona enter.
  <details><summary>Si has iniciado sesión como root...</summary>

    #### Crea un nuevo usuario con privilegios sudo y cámbiate a él.
    ```bash
    read -p "New username: " USERNAME
    adduser "$USERNAME"
    usermod -aG sudo "$USERNAME"
    su - "$USERNAME"
    ```
    #### Deshabilita el inicio de sesión remoto de root
    ```bash
    sudo sed -i 's/^#\?PermitRootLogin .*/PermitRootLogin no/' /etc/ssh/sshd_config
    sudo systemctl reload ssh
    ```
  </details>

### Cambiar el puerto SSH por defecto
```bash
sudo sed -i 's/^#Port 22\+$/Port 55022/' /etc/ssh/sshd_config
sudo systemctl restart sshd
```
*(Recuerda usar 55022 como puerto SSH de ahora en adelante)*
### Configurar el firewall
```bash
sudo apt install ufw
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 55022
sudo ufw allow 3724
sudo ufw allow 8085
sudo ufw enable
```
### Obtener las dependencias
```bash
sudo apt update && sudo apt install git cmake make gcc g++ clang libssl-dev libbz2-dev libreadline-dev libncurses-dev libboost-all-dev lsb-release gnupg wget p7zip-full nodejs npm fail2ban -y && sudo npm install pm2 -g
```
### Obtener MySQL
- Visita el [repositorio APT de MySQL](https://dev.mysql.com/downloads/repo/apt/) para verificar la última versión.
```bash
# Versión
MYSQL_APT_CONFIG_VERSION=0.8.36-1
# # # # #
mkdir -p ~/mysqlpackages && cd ~/mysqlpackages
# Descargar
wget "https://dev.mysql.com/get/mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb"
wget "https://dev.mysql.com/downloads/gpg/?file=mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb&p=37" -O mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb.asc
# Verificar
gpg --keyserver keyserver.ubuntu.com --recv-keys A8D3785C
gpg --verify mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb.asc mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
# Instalar
sudo DEBIAN_FRONTEND="noninteractive" dpkg -i ./mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
sudo apt update
sudo DEBIAN_FRONTEND="noninteractive" apt install -y mysql-server libmysqlclient-dev
# Limpieza
rm -v mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all* && unset MYSQL_APT_CONFIG_VERSION
```

### Configurar la base de datos SQL
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

## Configuración de SSH {#ssh-setup}
Este es un paso **opcional** que consiste en crear un archivo de clave y deshabilitar los inicios de sesión SSH basados en contraseña para aumentar la seguridad del servidor Debian y de la base de datos SQL.

<details><summary>▫️▫️▫️</summary>

### FileZilla
  - Este paso requiere [FileZilla](https://filezilla-project.org/download.php), un programa de Windows para transferir archivos hacia/desde el servidor.

### Generación de claves
#### Clave pública de Debian
```bash
ssh-keygen -t ed25519 -C "Debian12"
cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
```
#### Clave privada de Windows
- Usa **Filezilla** para conectarte al servidor y navega a `home/USERNAME/ssh/`
- Copia el archivo `id_ed25519` a tu PC y cárgalo en **puttygen.exe** (ubicado en la carpeta de PuTTY)
- Genera un archivo de clave privada `.ppk`. Guarda este archivo en un lugar seguro y haz un backup.
### Configuración del inicio de sesión basado en clave

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

### Deshabilitar los inicios de sesión con contraseña
- **Después de confirmar que el inicio de sesión basado en clave funciona**, deshabilita los inicios de sesión con contraseña.
```bash
sudo sed -i -E 's/#?PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo rm /etc/ssh/sshd_config.d/*
sudo service ssh restart
```
</details>

---
## Instalación de AzerothCore {#azerothcore-installation}
### Clonar el repositorio
```bash
git -C ~/ clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore
```
### Añadir el módulo Anticheat
```bash
git -C ~/azerothcore/modules clone https://github.com/azerothcore/mod-anticheat
```
### Obtener los archivos de datos
```bash
rm -rf ~/server/data &&
mkdir -p ~/server/data && cd ~/server/data &&
wget https://github.com/wowgaming/client-data/releases/download/v19/data.zip &&
7z x data.zip && rm data.zip
```
### Compilar el core
```bash
mkdir -p ~/azerothcore/build && cd ~/azerothcore/build
cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS_BUILD=db-only -DSCRIPTS=static -DMODULES=static
make -j $(nproc) install
```
### Editar las configuraciones
```bash
# Copiar .dist
cp -n ~/server/etc/authserver.conf.dist ~/server/etc/authserver.conf
cp -n ~/server/etc/worldserver.conf.dist ~/server/etc/worldserver.conf
cp -n ~/server/etc/modules/Anticheat.conf.dist ~/server/etc/modules/Anticheat.conf
# Directorio de datos
sudo sed -i -E "s|^DataDir = .*|DataDir = \"/home/$USER/server/data\"|" ~/server/etc/worldserver.conf
# Directorio de logs
sudo sed -i -E "s|^LogsDir = .*|LogsDir = \"/home/$USER/server/logs\"|" ~/server/etc/*.conf
mkdir -p ~/server/logs
```
### Iniciar el servidor
```bash
pm2 start $HOME/server/bin/authserver --name authserver -- -c $HOME/server/etc/authserver.conf
pm2 start $HOME/server/bin/worldserver --name worldserver -- -c $HOME/server/etc/worldserver.conf
eval "$(pm2 startup | grep sudo)"
pm2 save
pm2 attach $(pm2 id worldserver | tr -d '[][:space:]')
```
### Crear una cuenta GM
```bash
account create USERNAME PASSWORD
```
```bash
account set gmlevel USERNAME 3 -1
```
- Sepárate del worldserver con Ctrl+C.

### Establecer la IP del reino {#set-realm-ip}
```bash
sudo mysql <<'EOF'
UPDATE `acore_auth`.`realmlist` SET `address` = 'x.x.x.x' WHERE `id` = 1;
EOF
```
- Cambia **x.x.x.x** por la dirección IP pública de tu servidor Debian12.
## ¡Listo!

- Ahora deberías poder iniciar sesión en AzerothCore configurando el realmlist.wtf de tu cliente de WoW con la dirección IP pública del servidor Debian12. ej.: `set realmlist 12.345.67.890`

</details>

---

## Mantenimiento {#maintenance}

### Cambiar la contraseña de SQL
- Esto cambia la contraseña del usuario acore de la base de datos. La guía usa las credenciales SQL por defecto "acore/acore".
```bash
# Pedir la nueva contraseña
while true; do read -s -p "Set a new SQL password: " MYSQL_PASSWORD && echo; read -s -p "Retype SQL password: " MYSQL_PASSWORD_CONFIRM && echo; [ "$MYSQL_PASSWORD" = "$MYSQL_PASSWORD_CONFIRM" ] && break || echo "Passwords did not match."; done; unset MYSQL_PASSWORD_CONFIRM
# Actualizar el usuario SQL
sudo mysql <<EOF
ALTER USER 'acore'@'localhost' IDENTIFIED BY '${MYSQL_PASSWORD}';
FLUSH PRIVILEGES;
EOF
# Actualizar las configuraciones
sudo sed -i -E "s|= \"127.0.0.1;3306;acore;[^;]*;|= \"127.0.0.1;3306;acore;${MYSQL_PASSWORD};|" ~/server/etc/*.conf
# Limpieza
unset MYSQL_PASSWORD
```
### Modificar los archivos de configuración
- Este script puede extenderse para incluir todos tus ajustes de configuración preferidos. Ejecutarlo **eliminará los archivos .conf** y los recreará desde los .dist antes de aplicar los cambios.
```bash
#!/bin/bash
# Auxiliar: reiniciar y actualizar configuraciones
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
#### Añade tus módulos aquí ####

# Aplicar los cambios
update_config "$HOME/server/etc/authserver.conf" auth_settings
update_config "$HOME/server/etc/worldserver.conf" world_settings
update_config "$HOME/server/etc/modules/Anticheat.conf" anticheat_settings
#### Añade tus módulos aquí ####
```
### Comando de actualización del core
- Esto crea un comando de atajo para automatizar el proceso de actualización del core.
```bash
cat <<'EOF' >> ~/.bash_aliases
alias acoreupdate='
WORLD_ID="$(pm2 id worldserver | tr -d "[][:space:]")"
CORE_UPDATED=0

# Auxiliar: comprobar actualizaciones
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

# Auxiliar: compilar y reiniciar
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

# Comprobar actualizaciones
update_repo "$HOME/azerothcore"
update_repo "$HOME/azerothcore/modules/mod-anticheat"
##### Añade tus módulos aquí #####

# Compilar y reiniciar
if [ "$CORE_UPDATED" -eq 1 ]; then update_core; else echo "AzerothCore is up-to-date."; fi
'
EOF
source ~/.bash_aliases
```

- Ahora puedes descargar los últimos cambios de GitHub, compilar el core actualizado y reiniciar el worldserver, todo con un solo comando:
### Actualizar AzerothCore
```bash
acoreupdate
```
---
### Problemas comunes {#common-problems}

#### Inicio de sesión exitoso pero no puedo entrar al reino.
- Verifica bien la [dirección del reino.](#set-realm-ip)
#### Bucle de crashes que causa logs de error incompletos.
- Detén el worldserver con `pm2 stop` e inícialo con `pm2 start --no-autorestart` para obtener un log de error completo.
---
##### Cosas buenas que conviene saber y que esta guía no cubre.
- Configuración de nombre de dominio y DNS para *"set realmlist logon.server.com"*
- Sitio de registro con Wordpress y conexión SOAP del plugin acore-cms.
- Backups automáticos de la base de datos a Google Drive usando cron y rclone.

### Otros recursos {#other-resources}
- [Guía de instalación oficial de AzerothCore](es/installation)
- [Tutorial de Debian de heyaapl](es/digital-ocean-video-tutorial)
- [Video de Digital Scriptorium](https://www.youtube.com/watch?v=k4i4za1Scgg)

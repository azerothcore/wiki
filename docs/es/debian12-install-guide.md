# Guía de instalación de AzerothCore Debian 12

Esta es una guía de inicio rápido para instalar AzerothCore en un servidor Debian 12, protegerlo y habilitar el mantenimiento con un solo comando desde su PC con Windows.

## Table of Contents
  - [Requisitos](#requisitos)
  - [Configuración de Debian](#configuración-de-debian)
    - [Primer inicio de sesión](#primer-inicio-de-sesión)
    - [Cambiar el puerto SSH predeterminado](#cambiar-el-puerto-ssh-predeterminado)
    - [Configurar el firewall](#configurar-el-firewall)
    - [Obtener dependencias](#obtener-dependencias)
    - [Obtener MySQL](#obtener-mysql)
    - [Configurar la base de datos SQL](#configurar-la-base-de-datos-sql)
  - [Configuración de SSH](#configuración-de-ssh)
    - [Generación de claves](#generación-de-claves)
    - [Configuración de inicio de sesión basada en clave](#configuración-de-inicio-de-sesión-basada-en-clave)
    - [Deshabilitar inicios de sesión con contraseña](#deshabilitar-inicios-de-sesión-con-contraseña)
  - [Instalación de AzerothCore](#instalación-de-azerothcore)
    - [Repositorio de clones](#repositorio-de-clones)
    - [Añadir módulo antitrampas](#añadir-módulo-antitrampas)
    - [Obtener archivos de datos](#obtener-archivos-de-datos)
    - [Construir núcleo](#construir-núcleo)
    - [Editar configuraciones](#editar-configuraciones)
    - [Establecer IP del reino](#establecer-ip-del-reino)
    - [Servidor de lanzamiento](#servidor-de-lanzamiento)
    - [Crear una cuenta GM](#crear-una-cuenta-gm)
  - [Mantenimiento](#mantenimiento)
  - [Problemas comunes](#problemas-comunes)
  - [Otros recursos](#otros-recursos)

## Requisitos
##### [PuTTY](https://www.putty.org/)
- Un programa de Windows para enviar comandos al servidor.
##### [Debian 12](https://www.ovhcloud.com/en-ca/vps/)
- Un servidor con Debian 12 instalado. (ej: VPS de 4gb/4core de OVH)
### Opcional
##### [FileZilla](https://filezilla-project.org/download.php)
- Un programa de Windows para transferir archivos hacia/desde el servidor. Se utiliza durante la [Configuración SSH](#ssh-setup) para copiar el archivo de clave generado a su PC.
##### [HeidiSQL](https://www.heidisql.com/)
- Un programa de Windows para conectarse a la base de datos SQL del servidor. No se utiliza en esta guía. Si desea conectarse a su base de datos mediante HeidiSQL, [lea esto](https://www.enovision.net/mysql-ssh-tunnel-heidisql)


---
## Configuración de Debian
### Primer inicio de sesión

- Usa **PuTTY** para conectarte a tu servidor Debian usando la dirección IP y las credenciales de inicio de sesión proporcionadas por el proveedor de alojamiento. (Si inicias sesión como root, primero crea un nuevo usuario con privilegios de sudo y cámbiate a él).
- Copia los siguientes bloques de código y pégalos en la terminal de PuTTY haciendo clic derecho y pulsando Intro.
### Cambiar el puerto SSH predeterminado
```bash
sudo sed -i 's/^#Port 22\+$/Port 55022/' /etc/ssh/sshd_config
sudo systemctl restart sshd
```
- Recuerde utilizar 55022 como puerto SSH de ahora en adelante.
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
### Obtener dependencias
```bash
sudo apt update && sudo apt install git cmake make gcc g++ clang libssl-dev libbz2-dev libreadline-dev libncurses-dev libboost-all-dev lsb-release gnupg wget p7zip-full screen fail2ban -y
```
### Obtener MySQL
- Visit the [MySQL APT repository](https://dev.mysql.com/downloads/repo/apt/) to verify the latest version.
```bash
export MYSQL_APT_CONFIG_VERSION=0.8.33-1
```
```bash
mkdir -p ~/mysqlpackages && cd ~/mysqlpackages
wget "https://dev.mysql.com/get/mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb"
wget "https://dev.mysql.com/downloads/gpg/?file=mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb&p=37" -O mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb.asc
gpg --keyserver keyserver.ubuntu.com --recv-keys A8D3785C
gpg --verify mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb.asc mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
sudo DEBIAN_FRONTEND="noninteractive" dpkg -i ./mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
sudo apt update
sudo DEBIAN_FRONTEND="noninteractive" apt install -y mysql-server libmysqlclient-dev
rm -v mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all* && unset MYSQL_APT_CONFIG_VERSION
```

### Configurar la base de datos SQL
```bash
sudo mysql <<EOF
DROP USER IF EXISTS 'acore'@'localhost';
CREATE USER 'acore'@'localhost' IDENTIFIED BY 'SQLPASSWORD';
GRANT ALL PRIVILEGES ON *.* TO 'acore'@'localhost';
CREATE DATABASE \`acore_world\` DEFAULT CHARACTER SET UTF8MB4 COLLATE utf8mb4_unicode_ci;
CREATE DATABASE \`acore_characters\` DEFAULT CHARACTER SET UTF8MB4 COLLATE utf8mb4_unicode_ci;
CREATE DATABASE \`acore_auth\` DEFAULT CHARACTER SET UTF8MB4 COLLATE utf8mb4_unicode_ci;
EOF
```
- Cambie **SQLPASSWORD** por algo más seguro.
---
## Configuración de SSH
Este es un paso opcional que implica crear un archivo de clave y deshabilitar los inicios de sesión SSH basados ​​en contraseña para aumentar la seguridad del servidor Debian y la base de datos SQL.

### Generación de claves
#### Debian Public Key
```bash
ssh-keygen -t ed25519 -C "Debian12"
cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
```
#### Windows Private Key
- Utilice **Filezilla** para conectarse al servidor y navegue a `home/USERNAME/ssh/`
- Copie el archivo `id_ed25519` a su PC y cárguelo en **puttygen.exe** (ubicado en la carpeta PuTTY)
- Genere un archivo de clave privada `.ppk`. Guárdelo en un lugar seguro y haga una copia de seguridad.
### Configuración de inicio de sesión basada en clave

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

### Deshabilitar inicios de sesión con contraseña
- **Después de confirmar que el inicio de sesión basado en clave funciona**, desactive los inicios de sesión con contraseña.
```bash
sudo sed -i -E 's/#?PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo rm /etc/ssh/sshd_config.d/*
sudo service ssh restart
```

---

## Instalación de AzerothCore

### Repositorio de clones
```bash
git -C ~/ clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore
```
### Añadir módulo antitrampas
```bash
git -C ~/azerothcore/modules clone https://github.com/azerothcore/mod-anticheat
```
### Obtener archivos de datos
```bash
mkdir -p ~/server/data && cd ~/server/data
wget https://github.com/wowgaming/client-data/releases/download/v16/data.zip
7z x data.zip && rm data.zip
```
### Construir núcleo
```bash
mkdir -p ~/azerothcore/build && cd ~/azerothcore/build
cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS_BUILD=db-only -DSCRIPTS=static -DMODULES=static
make -j $(nproc) install
```
### Editar configuraciones
```bash
cp -n ~/server/etc/authserver.conf.dist ~/server/etc/authserver.conf
cp -n ~/server/etc/worldserver.conf.dist ~/server/etc/worldserver.conf
cp -n ~/azerothcore/modules/mod-anticheat/conf/Anticheat.conf.dist ~/server/etc/Anticheat.conf 
sudo sed -i -E 's|^DataDir = .*|DataDir = "/home/USERNAME/server/data"|' ~/server/etc/worldserver.conf
sudo sed -i -E 's|^LogsDir = .*|LogsDir = "/home/USERNAME/server/logs"|' ~/server/etc/*.conf
sudo sed -i -E 's/= "127.0.0.1;3306;acore;[^;]*;/= "127.0.0.1;3306;acore;SQLPASSWORD;/' ~/server/etc/*.conf
```
- Cambie **NOMBREDEUSUARIO** por su usuario Debian.
- Cambie **CONTRASEÑA SQL** por la contraseña del usuario de la base de datos de puntuación.
### Servidor de lanzamiento
```bash
mkdir -p ~/server/logs
screen -AmdS auth ~/server/bin/authserver
screen -AmdS world ~/server/bin/worldserver
screen -r world
```

### Crear una cuenta GM
```bash
account create USERNAME PASSWORD
```
```bash
account set gmlevel USERNAME 3 -1
```
- Desconectarse de la pantalla del servidor mundial con Ctrl+A -> Ctrl+D

### Establecer IP del reino
```bash
sudo mysql <<EOF
UPDATE acore_auth.realmlist SET address = '0.0.0.0' WHERE id = 1;
EOF
```
- Change **0.0.0.0** to the public IP address of your Debian12 server.
## ¡Finalizar!

- Ahora debería poder iniciar sesión en AzerothCore configurando su lista de reinos en la dirección IP pública del servidor Debian12. ej: `set realmlist 0.0.0.0`
---
## Mantenimiento
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

- Ahora podemos **guardar/salir** del servidor mundial, **extraer** los últimos cambios de GitHub, **construir** el núcleo actualizado y **reiniciar** el servidor mundial, todo con un solo comando.
### Actualizar AzerothCore
```
acoreupdate
```
---
## Problemas comunes

#### Auth/Worldserver ni siquiera se inicia.
- Asegúrese de que la contraseña del usuario acore [SQL](#setup-sql-database) coincida con la de [las configuraciones](#edit-configs)
#### Inicio de sesión exitoso pero no puedo ingresar al reino.
- Verifique nuevamente la [dirección del reino](#set-realm-ip)

---
##### Cosas buenas que es bueno saber que esta guía no cubre.
- Nombre de dominio y configuración de DNS para *"set realmlist logon.server.com"*
- Sitio de registro de Wordpress y conexión SOAP del complemento acore-cms.
- Copias de seguridad automatizadas de bases de datos en Google Drive mediante cron y rclone.

## Otros recursos
- [Guía oficial de instalación de AzerothCore](installation)
- [Tutorial de Debian de heyaapl](digital-ocean-video-tutorial)
- [Vídeo del Scriptorium Digital](https://www.youtube.com/watch?v=k4i4za1Scgg)

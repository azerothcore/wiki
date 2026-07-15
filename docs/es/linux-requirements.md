# Requisitos de Linux

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Inicio: Guía de instalación](classic-installation) | [Paso 2: Instalación del Core >>](linux-core-installation) |

| |
| :- |
| [MySQL](https://github.com/azerothcore/azerothcore-wotlk/security/policy) |
| Boost ≥ 1.74 |
| OpenSSL ≥ 3.0.x |
| CMake ≥ 3.16 |
| [OS](https://github.com/azerothcore/azerothcore-wotlk/security/policy) |
| [GCC / CLang](https://github.com/azerothcore/azerothcore-wotlk/security/policy) |

#### Ubuntu con MySQL 8.x

```sh
sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libboost-all-dev
```

Recuerda que si usas el usuario `root`, no es necesario usar `sudo`.

Para configurar MySQL en Ubuntu y similares (establecer la contraseña de `root` y otros ajustes), lee [esta guía](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04).

---

#### Debian 12 y 13

```sh
apt-get update && apt-get install -y git cmake make gcc g++ clang libssl-dev libbz2-dev libreadline-dev libncurses-dev libboost-all-dev lsb-release gnupg wget screen
```

Recuerda que si usas el usuario `root`, no es necesario usar `sudo`.

**Nota:** Al usar la opción `-y`, comenzará la instalación sin necesidad de que confirmes.

---

##### Instalar MySQL

1. Visita la página del [repositorio APT de MySQL](https://dev.mysql.com/downloads/repo/apt/) para verificar y descargar la última versión del script.
```sh
export MYSQL_APT_CONFIG_VERSION=0.8.36-1
```

1. Descarga el último paquete de información del repositorio de MySQL.

```sh
wget https://dev.mysql.com/get/mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
```

1. (Recomendado) Verifica la autenticidad de la configuración. Si tienes algún problema con este paso, consulta: https://dev.mysql.com/doc/refman/8.4/en/checking-gpg-signature.html
```sh
wget "https://dev.mysql.com/downloads/gpg/?file=mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb&p=37" -O mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb.asc
gpg --keyserver pgp.mit.edu --recv-keys A8D3785C
gpg --verify mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb.asc mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
rm -v mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb.asc
```

1. Instalación no interactiva usando `DEBIAN_FRONTEND="noninteractive"` para instalar la última versión MYSQL-LTS, p. ej. `mysql-8.4-lts`, sin que aparezca ningún prompt al usuario.

```sh
sudo DEBIAN_FRONTEND="noninteractive" dpkg -i ./mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
rm -v ./mysql-apt-config_${MYSQL_APT_CONFIG_VERSION}_all.deb
unset MYSQL_APT_CONFIG_VERSION
sudo apt-get update
sudo DEBIAN_FRONTEND="noninteractive" apt-get install -y mysql-server libmysqlclient-dev
```

---

#### Comprueba tu versión de clang

```sh
clang --version
```

Tu versión de `clang` **DEBE** ser igual o superior a la versión requerida que aparece al inicio de esta página.

---

#### Comprueba tu versión de cmake

```sh
cmake --version
```

Tu versión de `cmake` **DEBE** ser igual o superior a la versión requerida que aparece al inicio de esta página.

---

#### Comprueba tu versión de openssl

```sh
openssl version
```

Tu versión de `openssl` **DEBE** ser igual o superior a la versión requerida que aparece al inicio de esta página.

---

## Ayuda

Si sigues teniendo problemas, comprueba:

- [Preguntas frecuentes](faq)
- [Errores comunes](common-errors)
- [Cómo pedir ayuda](how-to-ask-for-help)
- [Únete a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del staff te responderá cuando tenga tiempo.

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Inicio: Guía de instalación](classic-installation) | [Paso 2: Instalación del Core >>](linux-core-installation) |

# Requisitos de Linux

| Guía de instalación | |
| :- | :- |
| Este articulo es una parte de la guía de instalación. Puedes leerlo o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Inicio: Guía de instalación](classic-installation.md) | [Paso 2: Instalación del núcleo >>](linux-core-installation.md) |

| |
| :- |
| MySQL ≥ 5.7.0 |
| Boost ≥ 1.67 |
| CMake ≥ 3.16 |
| Clang ≥ [10](https://github.com/azerothcore/azerothcore-wotlk/actions?query=workflow%3Acore-build) |

#### Ubuntu con MariaDB 10.x

AzerothCore no soporta las versiones 10.6 y 10.5 de MariaDB.
```

```sh
sudo apt update && sudo apt full-upgrade -y && sudo apt install git cmake make gcc g++ clang libssl-dev libbz2-dev libreadline-dev libncurses-dev libboost-all-dev mariadb-server mariadb-client libmariadb-dev libmariadb-dev-compat
```

#### Ubuntu con MySQL 8.x

```sh
sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libboost-all-dev
```

Recuerda que si eres el usuario `root` no es necesario usar `sudo`.

Para configurar MySQL en Ubuntu 18.04 y similares (establecer la contraseña `root` y otros ajustes) lea [esta guía](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04).

**Nota**: en versiones antiguas de Ubuntu como la **18.04** necesitas instalar `gcc-10` y `libboost1.74-dev`:

```
sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test
sudo add-apt-repository -y ppa:mhier/libboost-latest
sudo apt-get update
sudo apt install -y gcc-10 g++-10
sudo apt install -y install libboost1.74-dev
```

---

#### Debian 10 / Debian 12

```sh
sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang default-libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mariadb-server libboost-all-dev
```

Recuerda que si eres el usuario `root` no es necesario usar `sudo`.

**Nota:** Si añades la opción `-y` al final de la lista de comandos, comenzará a instalarlos sin necesidad de que confirmes.

**Ejemplo:**

```sh
apt-get update && apt-get install git cmake make gcc g++ clang default-libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mariadb-server libboost-all-dev -y
```

---

#### Verificar la versión de clang

```sh
clang --version
```

La versión de `clang` **DEBE** ser `10` o superior ([aquí](https://github.com/azerothcore/azerothcore-wotlk/actions?query=workflow%3Acore-build) puedes comprobar las versiones que se ejecutan en nuestro canal de acciones de Github, te recomendamos que utilices una de esas versiones).

Por ejemplo, si estás usando una versión antigua de Ubuntu como la 18.04, necesitas instalar clang usando:

```sh
sudo apt-get install clang-10.0
```

Si usas otra distro o versión, busca en google cómo instalar la versión de clang adecuada para tu sistema.

Actualmente el proyecto requiere clang10 o superior.

Esta es una forma de actualizar e instalar la versión 11.

La respuesta se detalla aquí:

[Cómo instalar clang 11 en Debian](https://stackoverflow.com/questions/66223241/how-to-install-clang-11-on-debian)

#### Verificar la versión de cmake

```sh
cmake --version
```

La versión de `cmake` **DEBE** ser `3.16` o superior.

En una versión más antigua de Ubuntu (ejemplo: 16.04), puede seguir las instrucciones aquí para instalar la última versión de cmake. En Debian necesitarás usar las fuentes de backports o construir Cmake manualmente.

Recuerde que es posible actualizar cmake usando Python.

Instalar:

```sh
python -m pip install cmake
```

Actualizar:

```sh
python -m pip install --upgrade cmake
```

#### Asegúrese de que las cabeceras de gcc-8 están instaladas

Esto es un problema si, por ejemplo, se utiliza una versión antigua de Ubuntu como la 16.04. Ahí tienes que añadir el PPA "Toolchain test builds":
https://launchpad.net/~ubuntu-toolchain-r/+archive/ubuntu/test

Después

```sh
sudo apt-get update
```

puedes instalar gcc-8: 

```sh
sudo apt-get install g++-8 gcc-8
```

## Ayuda

Si todavía tiene problemas, compruebe:

* [FAQ - Preguntas frecuentes](faq.md)

* [Errores comunes](common-errors.md)

* [Cómo pedir ayuda](how-to-ask-for-help.md)

* [Únase a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del staff le responderá siempre que tenga tiempo.

| Guía de instalación | |
| :- | :- |
| Este articulo es una parte de la guía de instalación. Puedes leerlo o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Inicio: Guía de instalación](classic-installation.md) | [Paso 2: Instalación del núcleo >>](linux-core-installation.md) |

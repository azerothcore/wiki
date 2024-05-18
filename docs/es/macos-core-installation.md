# Instalación del Core en macOS

| Guía de Instalación | |
| :- | :- |
| Este artículo forma parte de la Guía de Instalación. Puedes leerlo por separado o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 1: Requisitos](macos-requirements.md) | [Paso 3: Configuración del Servidor >>](server-setup.md) |

## Software necesario

Consulta [Requisitos](macos-requirements.md) antes de continuar.

### Descarga del código

Elija **UNO** del siguiente método, ejecute uno de los siguientes comandos `git ...` en su terminal.


1. Clonar solo la rama maestra + historial completo (tamaño más pequeño - recomendado):

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore
    ```

1. Clonar solo la rama maestra + sin historial previo (tamaño más pequeño):

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore --depth 1
    ```

    Nota: Si desea recuperar el historial completo, utilice `git fetch --unshallow`.

1. Clona todas las ramas y todo el historial:

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git azerothcore
    ```

Esto creará un directorio `azerothcore-wotlk` que contiene los archivos fuente de AC.

## Compilando el código fuente

### Creando el directorio de compilación

Para evitar problemas con las actualizaciones y compilaciones de fuentes en conflicto, creamos un directorio de compilación específico, de modo que evitamos cualquier posible problema debido a eso (si es que puede ocurrir alguno).

```sh
cd azerothcore
mkdir build
cd build
```

### Configurando para compilar


Los directorios que utiliza Homebrew para instalar paquetes difieren entre las Mac que tienen CPU Apple Silicon y aquellas que tienen CPU Intel. Asegúrese de ejecutar el comando CMake correcto para su máquina. Puede ver su tipo de CPU en `Acerca de esta Mac`. Los comandos siguientes están etiquetados para el tipo de CPU correspondiente.


Antes de ejecutar el comando CMake, reemplace `$HOME/azeroth-server/` con la ruta de instalación del servidor (donde desea colocar los archivos binarios compilados).

Explicación de parámetros para usuarios avanzados [Opciones de CMake](cmake-options.md).


En este punto, debes estar en tu directorio "build/".

**Nota**: en el siguiente comando, la variable `$HOME` es la ruta del **usuario actual**, por lo que si ha iniciado sesión como root, $HOME será "/root".

Para CPU APPLE SILICON::
```sh
export OPENSSL_ROOT_DIR=$(brew --prefix openssl@3)
cmake ../ \
-DCMAKE_INSTALL_PREFIX=$HOME/azeroth-server/  \
-DTOOLS_BUILD=all \
-DSCRIPTS=static \
-DMYSQL_ADD_INCLUDE_PATH=/opt/homebrew/include/mysql \
-DMYSQL_LIBRARY=/opt/homebrew/lib/libmysqlclient.dylib \
-DREADLINE_INCLUDE_DIR=/opt/homebrew/opt/readline/include \
-DREADLINE_LIBRARY=/opt/homebrew/opt/readline/lib/libreadline.dylib \
-DOPENSSL_INCLUDE_DIR="$OPENSSL_ROOT_DIR/include" \
-DOPENSSL_SSL_LIBRARIES="$OPENSSL_ROOT_DIR/lib/libssl.dylib" \
-DOPENSSL_CRYPTO_LIBRARIES="$OPENSSL_ROOT_DIR/lib/libcrypto.dylib"
```

Para CPU INTEL:
```sh
export OPENSSL_ROOT_DIR=$(brew --prefix openssl@3)
cmake ../ \
-DCMAKE_INSTALL_PREFIX=$HOME/azeroth-server/  \
-DTOOLS_BUILD=all \
-DSCRIPTS=static \
-DMYSQL_ADD_INCLUDE_PATH=/usr/local/include/mysql \
-DMYSQL_LIBRARY=/usr/local/opt/mysql/lib/libmysqlclient.dylib \
-DREADLINE_INCLUDE_DIR=/usr/local/opt/readline/include \
-DREADLINE_LIBRARY=/usr/local/opt/readline/lib/libreadline.dylib \
-DOPENSSL_INCLUDE_DIR="$OPENSSL_ROOT_DIR/include" \
-DOPENSSL_SSL_LIBRARIES="$OPENSSL_ROOT_DIR/lib/libssl.dylib" \
-DOPENSSL_CRYPTO_LIBRARIES="$OPENSSL_ROOT_DIR/lib/libcrypto.dylib"
```
Luego, para construir e instalar:

```sh
make -j `nproc`
make install
```

<br>

## Ayuda

Si todavía tiene problemas, compruebe:

* [FAQ - Preguntas frecuentes](faq.md)

* [Errores comunes](common-errors.md)

* [Cómo pedir ayuda](how-to-ask-for-help.md)

* [Únase a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del staff le responderá siempre que tenga tiempo.

| Guía de Instalación | |
| :- | :- |
| Este artículo forma parte de la Guía de Instalación. Puedes leerlo por separado o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 1: Requisitos](macos-requirements.md) | [Paso 3: Configuración del Servidor >>](server-setup.md) |

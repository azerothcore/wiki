# Instalación del Core en macOS

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 1: Requisitos](macos-requirements) | [Paso 3: Configuración del servidor >>](macos-server-setup) |

## Software necesario

Consulta [Requisitos](macos-requirements) antes de continuar.

## Obtener el código fuente

Elige **UNO** de los siguientes métodos; ejecuta uno de los comandos `git ...` de abajo en tu terminal.


1. Clonar solo la rama master + historial completo (menor tamaño - recomendado):

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore
    ```

1. Clonar solo la rama master + sin historial previo (el menor tamaño):

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore --depth 1
    ```

    Nota: Si quieres recuperar el historial completo, usa `git fetch --unshallow`.

1. Clonar todas las ramas y todo el historial:

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git azerothcore
    ```

Esto creará un directorio `azerothcore-wotlk` que contiene los archivos fuente de AC.

## Compilación del código fuente

### Crear el directorio de build

Para evitar problemas con las actualizaciones y builds de código que colisionen, creamos un directorio de build específico, así evitamos cualquier posible problema por eso (si llegara a ocurrir alguno)

```sh
cd azerothcore
mkdir build
cd build
```

### Configurar para compilar {#configuring-for-compiling}

Los directorios que Homebrew usa para instalar paquetes difieren entre las Mac con CPU Apple Silicon y las que tienen CPU Intel. Asegúrate de ejecutar el comando CMake correcto para tu máquina. Puedes ver tu tipo de CPU en `Acerca de este Mac`. Los comandos de abajo están etiquetados según el tipo de CPU correspondiente.

Antes de ejecutar el comando CMake, reemplaza `$HOME/azeroth-server/` con la ruta de instalación del servidor (donde quieras colocar los binarios compilados).

Explicación de los parámetros para usuarios avanzados: [Opciones de CMake](cmake-options).

En este punto, debes estar en tu directorio "build/".

**Nota**: en el siguiente comando la variable `$HOME` es la ruta del **usuario actual**, así que si has iniciado sesión como root, $HOME será "/root".

Para CPU APPLE SILICON:
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

## Ayuda

Si sigues teniendo problemas, comprueba:

- [Preguntas frecuentes](faq)
- [Errores comunes](common-errors)
- [Cómo pedir ayuda](how-to-ask-for-help)
- [Únete a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del staff te responderá cuando tenga tiempo.

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 1: Requisitos](macos-requirements) | [Paso 3: Configuración del servidor >>](macos-server-setup) |

# Instalación del Core en Linux

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 1: Requisitos](es/linux-requirements) | [Paso 3: Configuración del servidor >>](es/linux-server-setup) |

## Directorios de instalación

Los siguientes pasos instalarán AzerothCore en `$AC_CODE_DIR`. Por defecto será `$HOME/azerothcore`. Esta ruta puede cambiarse a cualquier otra ubicación a la que el usuario tenga acceso, si se desea.

El usuario `azerothuser` también se usará en algunos ejemplos. De nuevo, puede cambiarse por lo que se desee.

**Nota**: en el siguiente comando la variable `$HOME` es la ruta del **usuario actual**, así que si has iniciado sesión como root, $HOME será "/root". Puedes comprobar el estado de la variable de entorno así:

```sh
echo $HOME
```

Configura el directorio de instalación así:

```sh
export AC_CODE_DIR=$HOME/azerothcore
```

## Software necesario

Consulta [Requisitos](es/linux-requirements) antes de continuar.

## Obtener el código fuente

Elige **UNO** de los siguientes métodos; ejecuta uno de los comandos `git ...` de abajo en tu terminal.


1. Clonar solo la rama master + historial completo (menor tamaño - recomendado):

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch $AC_CODE_DIR
    ```

1. Clonar solo la rama master + sin historial previo (el menor tamaño):

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch $AC_CODE_DIR --depth 1
    ```

    Nota: Si quieres recuperar el historial completo, usa `git fetch --unshallow`.

1. Clonar todas las ramas y todo el historial:

    ```sh
    git clone https://github.com/azerothcore/azerothcore-wotlk.git $AC_CODE_DIR
    ```

Esto creará un directorio `azerothcore` en tu carpeta home que contiene los archivos fuente de AC.

## Compilación del código fuente

> [!WARNING]
> Cuando uses versiones recientes de Debian o Ubuntu, ¡existe una comprobación e instalación automática de actualizaciones que puede romper el funcionamiento del servidor!
> De hecho, MySQL por ejemplo puede actualizarse automáticamente (¡mientras el servidor está en ejecución!), por lo que `authserver` y `worldserver` se cierran al instante y esta situación puede causar pérdida de tiempo de juego.
>
> Así que, para evitarlo, simplemente haz esto:
> 1. edita el archivo `sudo nano /etc/apt/apt.conf.d/20auto-upgrades`
> 2. comenta todas las líneas
> 3. reinicia
>
> Esto evitará que el sistema actualice algunos programas útiles y cierre tu servidor de juego
>
> enlaces:
> https://discord.com/channels/217589275766685707/1255602330431127753/1369358673465442405
> https://discord.com/channels/217589275766685707/555424966137479180/1445387284768620554

### Crear el directorio de build

Para evitar problemas con las actualizaciones y builds de código que colisionen, creamos un directorio de build específico, así evitamos cualquier posible problema por eso (si llegara a ocurrir alguno)

```sh
cd $AC_CODE_DIR
mkdir build
cd build
```

### Configurar para compilar {#configuring-for-compiling}

Explicación de los parámetros para usuarios avanzados: [Opciones de CMake](es/cmake-options).

En este punto, debes estar en tu directorio `$AC_CODE_DIR/build`.


**Nota**: en caso de que uses un paquete no predeterminado para `clang`, necesitas reemplazarlo en consecuencia. Por ejemplo, si instalaste `clang-6.0`, tienes que reemplazar `clang` por `clang-6.0` y `clang++` por `clang++-6.0`

```sh
cmake ../ -DCMAKE_INSTALL_PREFIX=$AC_CODE_DIR/env/dist/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS_BUILD=all -DSCRIPTS=static -DMODULES=static
```

Para saber la cantidad de cores disponibles,
puedes usar el siguiente comando

```sh
nproc --all
```

Establece el número de cores con los que compilar, reemplazando el comando con el número de hilos que quieras ejecutar, si aplica:

```sh
export BUILD_CORES=`nproc | awk '{print $1 - 1}'`
```

Luego, escribe:

```sh
make -j$BUILD_CORES
make install
```

Puede ser útil conservar estos comandos en un script o anotarlos para más adelante. Necesitarás volver a ejecutar los tres comandos cada vez que actualices AzerothCore o añadas nuevos módulos. Por ejemplo:

```sh
#!/bin/bash

BUILD_CORES=`nproc | awk '{print $1 - 1}'`
cmake ../ -DCMAKE_INSTALL_PREFIX=$AC_CODE_DIR/env/dist/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS_BUILD=all -DSCRIPTS=static -DMODULES=static &&
make -j$BUILD_CORES &&
make install
```

## (Opcional) Servicios de Systemd {#optional-systemd-services}

Los servicios de systemd pueden ayudarte a gestionar tu servidor de AzerothCore. Los archivos de servicio que se muestran abajo deben instalarse como `root` en la mayoría de las distros. La ubicación apropiada en la mayoría de las distros es `/etc/systemd/system`.

Dado que estos comandos no se ejecutarán con acceso a las variables del usuario, el directorio de instalación `$AC_CODE_DIR` debe expandirse completamente a, por ejemplo, `/home/azerothuser/azerothcore`. Ejecuta `echo $AC_CODE_DIR` como tu usuario si no estás seguro de cuál debería ser.

Establece el usuario con el que se ejecutarán las units. El nombre de usuario usado aquí es `azerothuser`, y debe sustituirse por tu nombre de usuario.
```sh
export AC_UNIT_USER=azerothuser
```

### ac-authserver.service

```sh
sudo tee /etc/systemd/system/ac-authserver.service << EOF
[Unit]
Description=AzerothCore Authserver
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=$AC_UNIT_USER
WorkingDirectory=$AC_CODE_DIR
ExecStart=$AC_CODE_DIR/acore.sh run-authserver

[Install]
WantedBy=multi-user.target
EOF
```

### ac-worldserver.service

```sh
sudo tee /etc/systemd/system/ac-worldserver.service << EOF
[Unit]
Description=AzerothCore Worldserver
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=$AC_UNIT_USER
WorkingDirectory=$AC_CODE_DIR
ExecStart=/bin/screen -S worldserver -D -m $AC_CODE_DIR/acore.sh run-worldserver

[Install]
WantedBy=multi-user.target
EOF
```

systemd toma conocimiento de estos nuevos archivos de servicio con `systemctl daemon-reload`. Puedes iniciar AzerothCore así:

```sh
sudo service ac-worldserver start
sudo service ac-authserver start
```

O detenerlo:

```sh
sudo service ac-worldserver stop
sudo service ac-authserver stop
```

Los servidores pueden configurarse para que se inicien automáticamente cuando el sistema arranca con:

```sh
sudo systemctl enable ac-authserver
sudo systemctl enable ac-worldserver
```

Puedes revisar si los servicios se iniciaron correctamente inspeccionando las entradas de log del journal de systemd así:

```sh
sudo journalctl ac-authserver.service
sudo journalctl ac-worldserver.service
```

## Ayuda

Si sigues teniendo problemas, comprueba:

- [Preguntas frecuentes](es/faq)
- [Errores comunes](es/common-errors)
- [Cómo pedir ayuda](es/how-to-ask-for-help)
- [Únete a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del staff te responderá cuando tenga tiempo.

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 1: Requisitos](es/linux-requirements) | [Paso 3: Configuración del servidor >>](es/linux-server-setup) |

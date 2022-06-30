## Introducción

Este tutorial le guiará a través de la creación de un script para reiniciar AzerothCore después de un apagado, reinicio o caída cuando se utiliza un servidor Linux.

La forma más fácil de configurar un reiniciador es utilizando nuestros [scripts integrados o docker](how-to-restart-and-debug.md)

Sin embargo, el siguiente tipo le mostrará cómo crear su propio reiniciador desde cero.

## Creación de los scripts

#### Requisitos previos

- Compruebe que su servidor Linux tiene instalados `screen` y `nano`.

```sh
sudo apt-get update && sudo apt-get install screen nano
```

- Una vez que hayas instalado `screen` y `nano`, continúa con el siguiente paso.

#### Creación del script

- Navega al directorio bin de tu servidor `~/azeroth-server/bin` y escribe `nano auth.sh`
- En la nueva pantalla de nano, introduzca el siguiente script:

```sh
#!/bin/sh
while :; do
./authserver
sleep 20
done
```

- Una vez introducido, pulse `ctrl + o`, presione Enter, y luego `ctrl + x`. Eso guardará el nuevo script y le devolverá a la terminal. Acabamos de crear el script de reinicio de `authserver`. Ahora vamos a crear el script de `worldserver`.
- Escribe `nano world.sh`
- En la nueva pantalla de nano, introduzca el siguiente script:

```sh
while :; do
./worldserver
sleep 20
done
```

- Una vez introducido, pulsa `ctrl + o`, pulsa Enter, y luego `ctrl + x`. Eso guardará el nuevo script y te devolverá a la terminal. Acabamos de crear el script de reinicio de Worldserver. A continuación vamos a crear un script que lanzará los scripts de reinicio de Authserver y Worldserver.
- Escribe `nano restarter.sh`

```sh
#!/bin/bash
screen -AmdS auth ./auth.sh
screen -AmdS world ./world.sh
```

- Una vez introducido, pulsamos `ctrl + o`, pulsamos Enter y luego `ctrl + x`. Por último, vamos a crear nuestro script de apagado del servidor.
- Escribe `nano shutdown.sh`

```sh
#!/bin/bash
screen -X -S "world" quit
screen -X -S "auth" quit
```

- Una vez introducido, pulsamos `ctrl + o`, pulsamos Enter, y luego `ctrl + x`. A continuación, vamos a iniciar nuestro servidor.

## Gestión de servidores

#### Puesta en marcha del servidor

- Para iniciar tu servidor con los scripts, asegúrate de estar en el directorio bin de tu servidor `~/azeroth-server/bin`.
- Iniciaremos los scripts de reinicio escribiendo el siguiente comando `./restarter.sh`.
- Nota adicional: Si deseas iniciar el servidor y ver la consola de worldserver, utiliza el siguiente comando `./restarter.sh; screen -r world`.

#### Monitorización de servidores

- Para acceder y ver las consolas Authserver o Worldserver:
        - authserver: `screen -r auth`
        - worldserver: `screen -r world`
- Cuando quieras salir del screen y volver a tu terminal, escribe `ctrl + a`, seguido de `d` (ctrl + a + d)

#### Apagado del servidor

- Para terminar el reiniciador y apagar tu servidor, asegúrate de que estás en el directorio bin de tu servidor `~/azeroth-server/bin`.
- Escribe `./shutdown.sh` y los scripts se apagarán y tu servidor terminará.

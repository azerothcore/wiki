## Introducción

El panel de bash de AzerothCore es una colección de scripts que ayudan con la instalación y el mantenimiento de un servidor AzerothCore.
Permite instalar, actualizar y ejecutar fácilmente AzerothCore en su máquina en una cantidad tremendamente pequeña de pasos.

Instalar un servidor privado de desarrollo o producción nunca ha sido tan fácil.
Si necesitas ayuda simplemente [haz una pregunta](How-to-ask-for-help).


## Requisitos

Necesita tener [git](https://git-scm.com/), [curl](https://curl.se/), [unzip](https://github.com/madler/unzip), [sudo](https://www.sudo.ws/) instalados en su máquina.
No es necesario instalar manualmente ningún otro software.


- basado en Debian/Ubuntu: `apt update && apt install git`
- macOS: `brew install git`
- Windows: descargar e instalar [Git para Windows](https://gitforwindows.org/)

### Notas
- Para usuarios de macOS: instale y use la última versión de bash para ejecutar los comandos del panel de control (`brew install bash`)
- Para usuarios de Windows: los comandos deben ejecutarse dentro del shell "git bash" o un shell compatible con bash como WSL, cygwin, etc.
  Sin embargo, se sugiere git bash porque está preinstalado con git para Windows (uno de nuestros requisitos).


## Configuración

### Obtenga las fuentes de AzerothCore

```
git clone https://github.com/azerothcore/azerothcore-wotlk.git; cd azerothcore-wotlk
```

### Configuración

Hay un archivo [conf/dist/config.sh](https://github.com/azerothcore/azerothcore-wotlk/blob/master/conf/dist/config.sh) que contiene la configuración predeterminada. Échale un vistazo. 
La mayor parte de las configuraciones predefinidas le servirán. Sin embargo, puede copiarlas bajo `conf/config.sh` y cambiarlas como le parezca o lo requiera.


### Instalar todas las dependencias de AzerothCore

```
./acore.sh install-deps
```

NOTA: en Windows debe ejecutarse como administrador

### Construye todo desde cero

```
./acore.sh compiler all
```

### Configurar la base de datos

- - Conéctese a su base de datos MySQL (con `sudo mysql -u root`) y cree manualmente el usuario MySQL `acore` ejecutando:

```
DROP USER IF EXISTS 'acore'@'localhost';
DROP USER IF EXISTS 'acore'@'127.0.0.1';
CREATE USER 'acore'@'localhost' IDENTIFIED BY 'acore';
CREATE USER 'acore'@'127.0.0.1' IDENTIFIED BY 'acore';
GRANT ALL PRIVILEGES ON * . * TO 'acore'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON * . * TO 'acore'@'127.0.0.1' WITH GRANT OPTION;
FLUSH PRIVILEGES;
exit;
```

*Nota: aunque el usuario `acore` solo es accesible desde localhost, es una buena práctica cambiar su contraseña a algo más seguro.*

### Descargue los últimos datos del cliente

Obtenga los últimos datos de sus clientes:

```
./acore.sh client-data
```

### Archivos de configuración del servidor

Cree los dos archivos con los siguientes comandos. Contienen la configuración predeterminada para el servidor mundial y el servidor de autenticación. Si no desea modificarlos, basta con copiarlos.

```
cp env/dist/etc/authserver.conf.dist env/dist/etc/authserver.conf
cp env/dist/etc/worldserver.conf.dist env/dist/etc/worldserver.conf
```

### Resultado

Si siguió lo anterior, obtendrá su servidor dentro del directorio `env/dist`.

Los binarios `worldserver` y `authserver` se encuentran en `azerothcore-wotlk/env/dist/bin`.

Puede ejecutarlos directamente o utilizar el reiniciador (ver a continuación).
El primer inicio del servidor mundial instalará una base de datos completa de AzerothCore. No es necesario importar ninguna actualización de la base de datos en este momento.

Consulte también [Redes](networking) y [Pasos finales del servidor](final-server-steps)

### Reiniciador

El panel de control de AzerothCore viene con un paquete de reinicio incluido:

```
./acore.sh run-worldserver
```

Espere hasta que se complete el proceso y luego ejecute:

```
./acore.sh run-authserver
```

Para servidores dedicados, es posible que desees ejecutarlos dentro de sesiones de multiplexor de terminal usando herramientas como `tmux` (ver a continuación).


## Cómo actualizar su servidor

Actualizar las fuentes:

```
git pull
```

Reconstruir:
```
./acore.sh compiler build
```

Actualizar la base de datos:

[base de datos-manteniendo-el-servidor-actualizado](database-keeping-the-server-up-to-date)

Eso es todo.


## Consejos para servidores dedicados (de producción)

### Copias de seguridad diarias de tus bases de datos a través de Telegram

¿Quieres recibir copias de seguridad diarias de las bases de datos de tu servidor privado directamente en tu teléfono o computadora a través de mensajes de [Telegram](https://telegram.org/)?

Sí, es posible. Solo usa: [azerothcore/telegram-automated-db-backup](https://github.com/azerothcore/telegram-automated-db-backup)

### Visual Studio Code SSH

Puedes instalar AzerothCore fácilmente en un servidor Linux sin interfaz gráfica. Simplemente conéctate remotamente por SSH con [Visual Studio Code](https://code.visualstudio.com/) y las extensiones [SSH](https://code.visualstudio.com/docs/remote/ssh) y [SSH: Editar archivos de configuración](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh-edit) para que parezca que se ejecuta localmente.

### Ejecutar AzerothCore dentro de las sesiones de Tmux

Puede utilizar [tmux](https://github.com/tmux/tmux) como multiplexor de terminal, lo que le permitirá administrar fácilmente sus procesos dentro de un servidor sin GUI.

Puede crear 2 sesiones y ejecutar los procesos `worldserver` y `authserver` dentro de ellas:

- `tmux new -s world-session`
- Ahora ejecute `./acore.sh run-worldserver` dentro de él y luego sepárese de él.


- `tmux new -s auth-session`
- Ahora ejecute `./acore.sh run-authserver` dentro de él y luego sepárese de él.

Puedes desconectarte usando `CTRL+B+D` para salir de la sesión sin terminar el proceso.
Si te conectas mediante VSCode SSH, puedes simplemente cerrar la sesión de terminal.

Puedes conectarte nuevamente a la sesión `world-session` usando:

- `tmux attach -t world-session`

Otros comandos útiles:

- crear una nueva sesión: `tmux new -s my_session`
- finalizar todas las sesiones: `tmux ls`
- matar una sesión: `tmux kill my_session` (o simplemente adjuntarlo y escribir `exit`)
- finalizar TODAS las sesiones: `tmux kill-server`
- ...más detalles disponibles en la [wiki de tmux](https://github.com/tmux/tmux/wiki)


### Iniciar automáticamente las sesiones de tmux al iniciar el sistema

Puede crear automáticamente las sesiones tmux y ejecutar `authserver` y `worldserver` usando este sencillo script:

```sh
#!/usr/bin/env bash

# PERMITIR QUE TMUX ESPERE A QUE MYSQL ESTÉ LISTO
# DEBES CAMBIAR EL USUARIO Y CONTRASEÑA PARA QUE CORRESPONDA A TU INSTALACIÓN
    mysql_ready() {
        mysqladmin ping --host=127.0.0.1 --user=YOURUSER --password=YOURPASSWORD > /dev/null 2>&1
    }

    while !(mysql_ready)
    do
       sleep 3
       echo "esperando mysql..."
    done

# CAMBIE ESTOS CON LOS CAMINOS CORRECTOS
authserver="/path/to/azerothcore-wotlk/acore.sh run-authserver"
worldserver="/path/to/azerothcore-wotlk/acore.sh run-worldserver"

authserver_session="auth-session"
worldserver_session="world-session"

if tmux new-session -d -s $authserver_session; then
    echo "Sesión de servidor de autenticación creada: $authserver_session"
else
    echo "Error al intentar crear una sesión de servidor de autenticación: $authserver_session"
fi

if tmux new-session -d -s $worldserver_session; then
    echo "Sesión de servidor mundial creada: $worldserver_session"
else
    echo "Error al intentar crear una sesión de servidor mundial: $worldserver_session"
fi

if tmux send-keys -t $authserver_session "$authserver" C-m; then
    echo "Se ejecutó "$authserver" dentro de $authserver_session"
    echo "Puede conectarse a la sesión del servidor $auth y verificar el resultado usando \"tmux attached -t $authserver_session\""
else
    echo "Error al ejecutar "$authserver" dentro de $authserver_session"
fi

if tmux send-keys -t $worldserver_session "$worldserver" C-m; then
    echo "Se ejecutó "$worldserver" dentro de $worldserver_session"
    echo "Puede conectarse a $worldserver_session y verificar el resultado usando \"tmux attached -t $worldserver_session\""
else
    echo "Error al ejecutar "$worldserver" dentro de $worldserver_session"
fi
```

En sistemas Unix, puedes usar [crontab](https://es.wikipedia.org/wiki/Cron_(Unix))
para ejecutar el script automáticamente al iniciar el sistema:

```
crontab -e
```

luego agrega esta línea (reemplaza `/path/to/startup.sh` con la ruta donde colocaste el script anterior):

```
@reboot /bin/bash /path/to/startup.sh
```

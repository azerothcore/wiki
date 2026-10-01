## Introducción

El dashboard Bash de AzerothCore es una colección de scripts que ayudan con la instalación y el mantenimiento de un servidor AzerothCore.
Permite instalar, actualizar y ejecutar AzerothCore fácilmente en tu máquina en una cantidad de pasos tremendamente pequeña.

Instalar un servidor privado de desarrollo o producción nunca había sido tan fácil.
Si necesitas cualquier ayuda, simplemente [haz una pregunta](how-to-ask-for-help).


## Requisitos

Necesitas tener instalados [git](https://git-scm.com/), [curl](https://curl.se/), [unzip](https://github.com/madler/unzip) y [sudo](https://www.sudo.ws/) en tu máquina.
Ningún otro software necesita instalarse manualmente.


- basados en debian/ubuntu: `apt update && apt install git curl unzip sudo`
- macOS: `brew install git`
- Windows: descarga e instala [Git for Windows](https://gitforwindows.org/)

### Notas
- Para usuarios de macOS: instala y usa la última versión de bash para ejecutar los comandos del dashboard (`brew install bash`)
- Para usuarios de Windows: los comandos necesitan ejecutarse dentro de la shell "git bash" o una shell compatible con bash como WSL, cygwin, etc..
  Sin embargo, se sugiere git bash porque viene preinstalada con git for windows (uno de nuestros requisitos)


## Instalación

### Obtener las fuentes de AC

```
git clone https://github.com/azerothcore/azerothcore-wotlk.git; cd azerothcore-wotlk
```

### Configuración

Hay un archivo [conf/dist/config.sh](https://github.com/azerothcore/azerothcore-wotlk/blob/master/conf/dist/config.sh) que contiene una configuración por defecto. Échale un vistazo.
La mayoría de los valores por defecto de la configuración probablemente funcionarán para tu caso,
pero puedes copiarlo bajo `conf/config.sh` y cambiar los valores como quieras.


### Instalar todas las dependencias de AC

```
./acore.sh install-deps
```

NOTA: en Windows debe ejecutarse como administrador

### Construir todo desde cero

```
./acore.sh compiler all
```

### Configurar la base de datos

- Conéctate a tu base de datos MySQL (con `sudo mysql -u root`) y crea manualmente el usuario `acore` de MySQL ejecutando:

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

*Nota: aunque el usuario `acore` solo es accesible desde localhost, es una buena práctica cambiar su contraseña por algo más seguro.*

### Descargar los datos del cliente más recientes

Obtén los datos del cliente más recientes:

```
./acore.sh client-data
```

### Archivos de configuración del servidor

crea estos 2 archivos. Contienen la configuración por defecto para el worldserver y el authserver; si no deseas modificarla, simplemente copiarlos es suficiente.

#### Linux y Mac

```
cp env/dist/etc/authserver.conf.dist env/dist/etc/authserver.conf
cp env/dist/etc/worldserver.conf.dist env/dist/etc/worldserver.conf
```

#### Windows y Mac

```
cp env/dist/configs/authserver.conf.dist env/dist/configs/authserver.conf
cp env/dist/configs/worldserver.conf.dist env/dist/configs/worldserver.conf
```

### Resultado

Si seguiste lo anterior, obtendrás tu servidor dentro del directorio `env/dist`.

Los binarios `worldserver` y `authserver` están ubicados en `azerothcore-wotlk/env/dist/bin`.

Puedes ejecutarlos directamente o usar el reiniciador (ver abajo).
El primer arranque del `worldserver` instalará una base de datos completa de AzerothCore. No es necesario importar ninguna actualización de la base de datos en este punto.

Consulta también [Red](networking) y [Pasos finales del servidor](final-server-steps).

### Reiniciador

El dashboard de AzerothCore viene con una suite de reinicio incorporada:

```
./acore.sh run-worldserver
```

Espera hasta que el proceso se complete y luego ejecuta:

```
./acore.sh run-authserver
```

Para servidores dedicados,
quizás quieras ejecutarlos dentro de sesiones de multiplexor de terminal usando herramientas como `tmux` (ver abajo).


## Cómo actualizar tu servidor

Actualiza las fuentes:

```
git pull
```

Reconstruye:
```
./acore.sh compiler build
```

Actualiza la base de datos:

[database-keeping-the-server-up-to-date](database-keeping-the-server-up-to-date)

Eso es todo.


## Consejos para servidores dedicados (de producción)

### Copias de respaldo diarias de tus bases de datos vía Telegram

¿Quieres obtener copias de respaldo diarias de las bases de datos de tu servidor privado directamente en tu teléfono/computadora vía mensajes de [Telegram](https://telegram.org/)?

Sí, es posible. Solo usa: [azerothcore/telegram-automated-db-backup](https://github.com/azerothcore/telegram-automated-db-backup)

### Visual Studio Code SSH

Puedes instalar AzerothCore fácilmente en un servidor linux sin ningún tipo de GUI,
simplemente conectándote de forma remota vía ssh usando [Visual Studio Code](https://code.visualstudio.com/)
y las extensiones [SSH](https://code.visualstudio.com/docs/remote/ssh)
y [SSH: Editing Configuration Files](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh-edit) para que te sientas como en casa.

### Ejecutar AzerothCore dentro de sesiones de Tmux

Puedes usar [tmux](https://github.com/tmux/tmux) como multiplexor de terminal;
te permitirá gestionar fácilmente tus procesos dentro de un servidor sin GUI.

Puedes crear 2 sesiones y ejecutar los procesos `worldserver` y `authserver` dentro de ellas:

- `tmux new -s world-session`
- ahora ejecuta `./acore.sh run-worldserver` dentro de ella, luego sepárate (detach)


- `tmux new -s auth-session`
- ahora ejecuta `./acore.sh run-authserver` dentro de ella, luego sepárate (detach)

Puedes separarte usando `CTRL+B+D` para salir de la sesión sin matar el proceso.
Si estás conectado usando VSCode SSH, puedes simplemente cerrar la sesión de la terminal.

Puedes volver a adjuntarte a la sesión `world-session` usando:

- `tmux attach -t world-session`

Otros comandos útiles:

- crear una nueva sesión: `tmux new -s my_session`
- listar todas las sesiones: `tmux ls`
- matar una sesión: `tmux kill my_session` (o simplemente adjúntate a ella y escribe `exit`)
- matar TODAS las sesiones: `tmux kill-server`
- ...más detalles disponibles en la [wiki de tmux](https://github.com/tmux/tmux/wiki)


### Iniciar automáticamente las sesiones de tmux en el arranque del sistema

Puedes crear automáticamente las sesiones de tmux y ejecutar el `authserver` y el `worldserver` usando este sencillo script:

```sh
#!/usr/bin/env bash

# PERMITIR QUE TMUX ESPERE A QUE MYSQL ESTÉ LISTO
# DEBES CAMBIAR EL USUARIO Y LA CONTRASEÑA PARA QUE CORRESPONDAN CON TU INSTALACIÓN
    mysql_ready() {
        mysqladmin ping --host=127.0.0.1 --user=YOURUSER --password=YOURPASSWORD > /dev/null 2>&1
    }

    while !(mysql_ready)
    do
       sleep 3
       echo "waiting for mysql ..."
    done

# CAMBIA ESTAS RUTAS POR LAS CORRECTAS
authserver="/path/to/azerothcore-wotlk/acore.sh run-authserver"
worldserver="/path/to/azerothcore-wotlk/acore.sh run-worldserver"

authserver_session="auth-session"
worldserver_session="world-session"

if tmux new-session -d -s $authserver_session; then
    echo "Created authserver session: $authserver_session"
else
    echo "Error when trying to create authserver session: $authserver_session"
fi

if tmux new-session -d -s $worldserver_session; then
    echo "Created worldserver session: $worldserver_session"
else
    echo "Error when trying to create worldserver session: $worldserver_session"
fi

if tmux send-keys -t $authserver_session "$authserver" C-m; then
    echo "Executed \"$authserver\" inside $authserver_session"
    echo "You can attach to $authserver_session and check the result using \"tmux attach -t $authserver_session\""
else
    echo "Error when executing \"$authserver\" inside $authserver_session"
fi

if tmux send-keys -t $worldserver_session "$worldserver" C-m; then
    echo "Executed \"$worldserver\" inside $worldserver_session"
    echo "You can attach to $worldserver_session and check the result using \"tmux attach -t $worldserver_session\""
else
    echo "Error when executing \"$worldserver\" inside $worldserver_session"
fi
```

En sistemas unix, puedes usar [crontab](https://en.wikipedia.org/wiki/Cron)
para ejecutar el script automáticamente en el arranque del sistema:

```
crontab -e
```

luego añade esta línea (reemplaza `/path/to/startup.sh` con la ruta donde colocaste el script anterior):

```
@reboot /bin/bash /path/to/startup.sh
```

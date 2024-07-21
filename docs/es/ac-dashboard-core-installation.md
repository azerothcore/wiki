## Introducción

El panel de control Bash de Azeroth Core es una colección de scripts que ayudan durante la instalación y mantenimiento del servidor basado en AC. Permiten facilidad en al instalación, actualización y ejecución de AzerothCore mediante una realmente baja cantidad de pasos.

Installar un servidor para desarrollo o producción nunca había sido tan fácil.

Si necesita algún tipo de ayuda: [haga una pregunta](How-to-ask-for-help).


## Requisitos

Necesita tener [git](https://git-scm.com/) instalado en su máquina. 
Ningún otro software require ser instalado manualmente.

- debian/ubuntu-based: `apt update && apt install git`
- macOS: `brew install git`

### Notas
- Para usuarios de macOS: instale y use la ultima verisón de bash para ejecutar los comandos del panel de control (`brew install bash`)
- Para usuarios de Windows: Los comandos deben ser ejecutados dentro de la consola de "git bash" o una compatible por ejemplo: WSL, cywin, etc...
  Sin embargo, se sugiere usar git bash ya que viene preinstalada con git para Windows (uno de nuestros requisitos).

## Instalación

### Obténga las fuentes de AzerothCore

```
git clone https://github.com/azerothcore/azerothcore-wotlk.git; cd azerothcore-wotlk
```

### Configuración

Existe un archivo [conf/dist/config.sh](https://github.com/azerothcore/azerothcore-wotlk/blob/master/conf/dist/config.sh) que contiene una configuración predeterminada. Échele un vistazo. La mayor parte de las configuraciones predefinidas le servirán. Sin embargo, puede copiarlas bajo `conf/config.sh` y cambiarlas como le parezca o lo requiera.


### Instalar todas las dependecias de AzerothCore

```
./acore.sh install-deps
```

### Construya todo desde cero

```
./acore.sh compiler all
```

### Configurar la base de datos

- Bien puede conectarse a su base de datos MySQL (con `sudo mysql -u root`) y crear manualmente el usuario de MySQL `acore` ejecutando:

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

*Nota:  aún cuando el usuario `acore` solo es accesible desde la conexión local, cambiar su contraseña por algo más seguro es una buena práctica.*

- O cambiar el `config.sh` para usar otro usuario de MySQL.

Luegoe ejecute:

```
./acore.sh db-assembler import-all
```

Esto va a instalar toda la base de datos de AzerothCore. No se necesita importar alguna actualización de la base de datos en este punto.

### Descargar los archivos del cliente más recientes

Ejecute:

```
./acore.sh client-data
```

### Archivos de configuración del Servidor

```
cp env/dist/etc/authserver.conf.dist env/dist/etc/authserver.conf
```
```
cp env/dist/etc/worldserver.conf.dist env/dist/etc/worldserver.conf
```

### Resultado

Si siguió los pasos anteriores, tendrá el servidor dentro del directorio `env/dist`.

Los binarios `worldserver` y `authserver` están ubicados en `azerothcore-wotlk/env/dist/bin`.

Bien puedes ejecutralos directamente, o usar el reiniciador (ver abajo).

### Reiniciador

El panel de control de  AzerothCore viene con un sistema de reinicio incorporado:

```
./acore.sh run-worldserver
```

```
./acore.sh run-authserver
```

Para servidores de dedicados, tal vez usted quiera ejecutarlos dentro de sesiones multiplexer de la terminal, usando herrambientas como `tmux` (ver abajo).


## Como actualizar su servidor

Actualice las fuentes:

```
git pull
```

Reconstruya:
```
./acore.sh compiler build
```

Actualice la base de datos:

```
./acore.sh db-assembler import-updates
```

Eso es todo.


## Consejos para servidores dedicados (de producción)

### Copias de respaldo diarias via Telegram

Obtener copias de respaldo diarias de las bases de datos de su servidor directamente en su celular o computador
via mensajes de[Telegram](https://telegram.org/)?

Sí, es posible. Solamente use: [azerothcore/telegram-automated-db-backup](https://github.com/azerothcore/telegram-automated-db-backup)

### Visual Studio Code SSH

Puede instalar AzerothCore en un servidor de linux, con facilidad, sin usar ningún tipo de GUI (Interfáz gráfica de usuario). Simplemente conectese de forma remota via SSH, usando [Visual Studio Code](https://code.visualstudio.com/)
y las extensiones [SSH](https://code.visualstudio.com/docs/remote/ssh)
y [SSH: Editing Configuration Files](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh-edit) de manera que se va a sentir como en casa.

### Ejecutar AzerothCore dentro de sesiones Tmux Run AzerothCore inside Tmux sessions

Usted puede usar [tmux](https://github.com/tmux/tmux) como terminal multiplexer, 
esto le permitirá administrar con facilidad los procesos dentro de un servidor sin GUI.

Puede crear 2 sesiones y ejecutrar `worldserver` y `authserver` dentro de estas:

- `tmux new -s world-session`
- luego ejecute `./acore.sh run-worldserver` dentro de esta, luego salga.


- `tmux new -s auth-session`
- luego ejecute `./acore.sh run-authserver` dentro de esta,  luego salga.

Puede salir usando `CTRL+B+D`. De esta manera no finalizará el/los proceso.
Si está conectado usando VsCode SSH, puede simplemente serrar la sesión de la terminal.

Puede volver de nuevo a la sesión `world-session` usando:

- `tmux attach -t world-session`

Otros comandos útiles:

- crear nueva sesión: `tmux new -s my_session`
- listar todas las sesiones: `tmux ls`
- finalizar una sesión: `tmux kill my_session` (or just attach to it and type `exit`)
- finalizar TODAS las sesiones: `tmux kill-server`
- ...más detalles disponibles en la [wiki de tmux](https://github.com/tmux/tmux/wiki)


### Iniciar automáticamente las sesiones tmux en el arranque del sistema

Puede crear automáticamente las sesiones y ejecutar `authserver` y `worldserver` usando este sencillo script:

```sh
#!/usr/bin/env bash

# CHANGE THESE WITH THE CORRECT PATHS
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

En sistemas unix, puede usar [crontab](https://en.wikipedia.org/wiki/Cron) 
para ejecutrar el script automáticamente en el arranque del sistema:

```
crontab -e
```

luego, añada esta linea (remplace `/path/to/startup.sh` con la ruta de donde está ubicado el script script):

```
@reboot /bin/bash /path/to/startup.sh
```

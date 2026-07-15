---
tableofcontents: 1
redirect_from: "/es/Install-with-Docker"
---

# Instalación con Docker

¡Bienvenido a la guía de Docker de AzerothCore!

Las configuraciones de docker de ejemplo para AzerothCore pueden parecer poco idiomáticas a veces, y este documento puede ayudar a los usuarios a empezar a ejecutar un servidor AzerothCore en un entorno basado en contenedores.

## Configuración inicial

### Requisitos de software

Los únicos requisitos son [git](https://git-scm.com/download/) y Docker.

- Para GNU/Linux instala [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu)
- Para macOS 10.12+ Sierra y versiones posteriores instala [Docker Desktop for Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac)
- Para Windows 10 instala [Docker Desktop for Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

También necesitarás el plugin `compose` de docker. Las instrucciones de instalación están disponibles [en este enlace](https://docs.docker.com/compose/install/#scenario-one-install-docker-desktop). Si usas una máquina con docker desktop, no necesitas hacer este paso.

Antes de continuar, asegúrate de tener `docker` y `docker compose` instalados en tu sistema escribiendo en una terminal:

```
docker --version
```
```
docker compose version
```

Deberías ver una salida similar:

```
Docker version 20.10.5, build 55c4c88
Docker Compose version 2.10.2
```

**Nota para usuarios de Windows**: puedes usar **git-bash** (la shell incluida con git) como terminal.

### Clonar el repositorio de AzerothCore

Necesitas clonar el repositorio de AzerothCore (o usar tu propio fork):

```
git clone https://github.com/azerothcore/azerothcore-wotlk.git --depth 1
```

Ahora entra en el directorio principal usando `cd azerothcore-wotlk`. **Todos los comandos deberán ejecutarse dentro de esta carpeta**.

### Instalación {#installation}

Para construir los contenedores, ejecuta `docker compose build`. Y luego, para iniciar los contenedores, ejecuta `docker compose up -d`

Estos comandos pueden combinarse en uno solo, con `docker compose up -d --build`

El contenedor `ac-client-data` descargará automáticamente los datos del cliente a un volumen, y el dbimport ejecutará las migraciones de la base de datos. Ambas operaciones pueden tardar de 10 a 15 minutos en la primera ejecución.

Una vez que el db-import se complete, el authserver y el worldserver deberían iniciarse, y puedes continuar con [crear una cuenta](#creating-an-account)

Los contenedores se pueden detener con `docker compose down`, o reiniciar con `docker compose restart`.

Todos los comandos indicados en esta sección admiten recibir el nombre de un contenedor como argumento. Por ejemplo, puedes reconstruir y reiniciar solo el worldserver con `docker compose up -d --build ac-worldserver`.

Puedes encontrar más comandos de `docker compose` [en su documentación](https://docs.docker.com/compose/reference/)

### (Alternativa) Instalación usando el Dashboard

Dentro de tu terminal (si usas Windows, usa git bash), ejecuta los siguientes comandos dentro de la carpeta azerothcore-wotlk

El siguiente procedimiento usa nuestro dashboard acore.sh; sin embargo, estos comandos son una envoltura ligera sobre la CLI estándar de `docker compose`.

#### 1) Compilar AzerothCore
```
./acore.sh docker build
```
¡Construirá las imágenes de docker y compilará el core automáticamente! Esto puede tardar un rato.

**Para Windows:** si el build no se completa y muestra un mensaje similar al siguiente:
```
unable to start container process: exec: "C:/Program Files/Git/usr/bin/bash": stat C:/Program Files/Git/usr/bin/bash: no such file or directory: unknown
```

Puede que tengas un problema con la conversión de rutas Unix > Windows. Establecer la variable de entorno `MSYS_NO_PATHCONV=1` puede solucionarlo:

```
MSYS_NO_PATHCONV=1 ./acore.sh docker build
```

#### 2) Ejecutar los contenedores

```
./acore.sh docker start:app
```

**¡Felicidades! ¡Ahora tienes un servidor azerothcore en funcionamiento! Continúa con el siguiente paso para crear una cuenta**

Si necesitas ejecutar esto en segundo plano, puedes usar el siguiente comando para ejecutar docker compose en modo detached:

```
./acore.sh docker start:app:d
```

### Crear una cuenta {#creating-an-account}

#### 1) Acceder a la consola del worldserver

Abre una nueva terminal y ejecuta el siguiente comando para adjuntarte (attach) al worldserver:

```
docker attach ac-worldserver
```

Para separarte (detach), presiona `ctrl+p` y `ctrl+q`. **NO** intentes separarte usando `ctrl+c` ¡o matarás el proceso de tu worldserver!

Si obtienes el mensaje de error `the input device is not a TTY.  If you are using mintty, try prefixing the command with 'winpty'`

Este comando adjuntará automáticamente tu terminal a la consola del worldserver.
Ahora puedes ejecutar el comando `account create <user> <password>` para crear tu primera cuenta dentro del juego. Hay [más información en la página de Creación de cuentas](es/creating-accounts).

### Acceder a la base de datos y actualizar el realmlist

Para acceder a tu base de datos MySQL recomendamos clientes como [HeidiSQL](https://www.heidisql.com/) (para Windows/Linux+Wine) o [SequelPro](https://www.sequelpro.com/) (para macOS). Usa `root` como usuario y `127.0.0.1` como host por defecto.
La contraseña por defecto del usuario root de la base de datos será `password`.

A menos que la instalación de tu servidor esté en la misma máquina que tu cliente, quizás quieras actualizar la dirección `realmlist` en la base de datos `acore_auth` con la IP pública o privada de tu servidor:
```sql
USE acore_auth;
SELECT * FROM realmlist;
UPDATE realmlist SET address='$SERVER PUBLIC IP ADDRESS';
```

## Procedimientos

### Hacer backups

Cuando ejecutas cualquier tipo de servidor del que dependen otras personas, es importante hacer backups. Para AzerothCore, hacer backups es sencillo, ya que es lo mismo que hacer un backup estándar de MySQL.

Para cada base de datos (normalmente `acore_auth`, `acore_characters` y `acore_world`), deberías ejecutar este comando:

```console
$ mysqldump -h 127.0.0.1 -P3306 -u$DATABASE_USERNAME -p$PASSWORD DATABASE_NAME > ./DATABASE_NAME-$(date +%F).sql
```

Usando la configuración por defecto de cada base de datos, los comandos deberían verse así:

```console
$ mysqldump -h127.0.0.1 -P3306 -uroot -ppassword acore_auth > acore_auth-$(date +%F).sql
$ mysqldump -h127.0.0.1 -P3306 -uroot -ppassword acore_characters > acore_characters-$(date +%F).sql
$ mysqldump -h127.0.0.1 -P3306 -uroot -ppassword acore_world > acore_world-$(date +%F).sql
```

Algunas notas sobre estos comandos:

- Normalmente es mejor automatizar este comando con un cron job (Linux/MacOS) o un evento programado (en Windows).
- El comando `$(date +%F)` imprime la fecha en formato "yyyy-mm-dd". Esto es útil para que puedas ejecutar el comando una y otra vez.
- Los valores por defecto están diseñados para ayudar a alguien a empezar lo más rápido posible. Si ejecutas un sistema del que dependen otras personas, **no deberías usar el usuario root** (y la contraseña del usuario root debería ser distinta) y, en su lugar, debería haber un usuario específico para los backups.
- Para más información, recomendamos encarecidamente leer [la documentación de MySQL sobre Backup and Recovery](https://dev.mysql.com/doc/refman/8.0/en/backup-and-recovery.html).

### Configurar AzerothCore en contenedores

Al igual que la mayoría de las aplicaciones que se ejecutan en contenedores, AzerothCore puede configurarse con variables de entorno. Puedes encontrar los parámetros de configuración válidos y su descripción en los archivos de configuración por defecto del [worldserver](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/apps/worldserver/worldserver.conf.dist) y del [authserver](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/apps/authserver/authserver.conf.dist). Localmente, estos archivos se encuentran en el directorio `env/dist/etc` después de un build.

En Docker, la mejor forma de establecer configuraciones para AzerothCore es usar un archivo [`docker-compose.override.yml`](https://docs.docker.com/compose/multiple-compose-files/merge/). Esto crea un archivo adicional que no se sobrescribirá al actualizar el repo de git, pero que mantiene todos tus cambios personalizados correctamente configurados.

Una vez que hayas encontrado un parámetro que quieras cambiar (quizás `AllowTwoside.Interaction.Calendar`), puedes crear un archivo override así:

```yaml
# docker-compose.override.yml
services:
  ac-worldserver:
    environment:
      AC_ALLOW_TWO_SIDE_INTERACTION_CALENDAR: "1" # AllowTwoSide.Interaction.Calendar
```

Averiguar el nombre de la variable de entorno de un parámetro de configuración puede ser un poco difícil. Las reglas generales para esto:

- Todo el parámetro se prefija con `AC_`
- Los puntos (`.`) se convierten en guiones bajos (`_`)
- Una secuencia con una letra minúscula seguida de una mayúscula inserta un guion bajo (`_`) entre ellas
- Todo el parámetro se pasa a mayúsculas (así `foo` se convierte en `FOO`)

Algunos ejemplos:

- `foo.bar_baz` => `AC_FOO_BAR_BAZ`
- `MaxPrimaryTradeSkill` => `AC_MAX_PRIMARY_TRADE_SKILL`
- `AllowTwoSide.Interaction.Calendar` => `AC_ALLOW_TWO_SIDE_INTERACTION_CALENDAR`

### Cómo mantener tu AzerothCore actualizado con los últimos cambios

Primero, solo necesitas usar la herramienta `git` para actualizar tu repositorio ejecutando el siguiente comando:

`git pull origin master` : esto descargará los últimos commits del repositorio de azerothcore

[Reconstruye y reinicia](#installation) los contenedores como de costumbre

### Cómo ejecutar el worldserver con gdb

Ejecutar el servidor con GDB te permite generar un crashdump si el servidor falla. El archivo crashdump es útil para que los desarrolladores entiendan qué líneas están fallando y posiblemente lo corrijan.

En iteraciones anteriores de los contenedores docker de AzerothCore, gdb se incluía por defecto. Eso se ha cambiado para mantener contenedores más pequeños. Para muchos problemas en los que se necesita gdb, a menudo no es un problema específico de Docker, y se pueden usar herramientas como el [devcontainer](#devcontainer-support) para depurar más a fondo el problema.

Ten en cuenta que deberías compilar tu código con los tipos de compilación Debug o RelWithDebInfo; de lo contrario, gdb no funcionará correctamente.

Para usar gdb en los contenedores docker:

1. Edita el target "runtime" del Dockerfile
    1. Para saber qué sección es "runtime", deberían ser las ~15 líneas aproximadamente bajo la sección "FROM skeleton as runtime"
2. Busca el comando "apt-get install" en esta sección runtime
3. Edita el comando para que también instale GDB, y copia también el archivo `gdb.conf`
    1. Debería verse así:

    ```
    RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      libmysqlclient21 libreadline8 \
      gettext-base default-mysql-client \
      gdb gdbserver && \
    rm -rf /var/lib/apt/lists/*

    COPY apps/startup-scripts/gdb.conf /azerothcore/gdb.conf
    ```
4. Edita tu `docker-compose.override.yml` para que el `command` del `ac-worldserver` sea `gdb -x /azerothcore/gdb.conf --batch /azerothcore/env/dist/bin/worldserver`
    1. Debería verse así:

    ```yaml
    services:
      ac-worldserver:
        command: gdb -x /azerothcore/gdb.conf --batch /azerothcore/env/dist/bin/worldserver
    ```

5. Reinicia y reconstruye tus contenedores, y el worldserver debería estar ejecutándose ahora con gdb

Si el servidor falla, encontrarás el archivo crashdump (`gdb.txt`) dentro de la carpeta `/azerothcore`. Se puede copiar hacia afuera con el comando `docker cp ac-worldserver:/azerothcore/gdb.txt ./gdb.txt`.

### Soporte de .devcontainer {#devcontainer-support}

En `docker-compose.yml` definimos el servicio `ac-dev-server`.
Este servicio se usa para nuestras operaciones de build y base de datos, pero también puedes usarlo tú para desarrollar con la [extensión Remote Docker de VSCode](https://code.visualstudio.com/docs/remote/containers)

Un dev-container te permite usar un contenedor Docker como un entorno de desarrollo completo. La carpeta **.devcontainer** de nuestro proyecto contiene archivos que le indican a VS Code cómo acceder a (o crear) un contenedor de desarrollo con todas las herramientas necesarias. Este contenedor ejecutará AzerothCore con todo el software y las configuraciones necesarias para trabajar con nuestra base de código y depurar el servidor.

Dentro del repo de azerothcore hay un `devcontainer.json` preconfigurado que puede abrirse usando la paleta de comandos de VSCode.
Para configurar el Dev-Container sigue estos pasos:

1. [Instala y abre VSCode](https://code.visualstudio.com/)
2. instala la extensión [remote-container](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
3. Abre la carpeta de azerothcore dentro de VSCode
4. Abre la [paleta de comandos](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) de VSCode (Ctrl+Shift+P) y ejecuta: `>Remote-Containers: Reopen in Container`

**IMPORTANTE**: el dev-container también contiene una acción de debugger preconfigurada que te permite usar breakpoints y depurar tu worldserver.

No olvides que necesitas tener instalada la [extensión Remote Container](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) en tu IDE [Visual Studio Code](https://code.visualstudio.com/)

#### Cómo depurar tu código con el dev-container

NOTA: **Ten en cuenta que deberías compilar tu código en modo Debug; de lo contrario, el debugger no funcionará correctamente**

Una vez dentro del dev-container de VSCode, puedes ir a la sesión de depuración y usar la acción `Linux/Docker debug` como puedes ver en esta imagen:

![image](https://user-images.githubusercontent.com/147092/115712693-5a837d80-a375-11eb-98aa-b415e1919125.png)

Ejecutará un worldserver en modo debug y luego puedes empezar a colocar breakpoints en tu código para depurarlo.

![image](https://user-images.githubusercontent.com/147092/115712867-9cacbf00-a375-11eb-9cab-890e4f68d98b.png)

Para más información sobre cómo depurar en vscode, puedes consultar la [guía oficial](https://code.visualstudio.com/docs/editor/debugging)

### Cómo crear un segundo reino con docker compose

TODO

La idea general es editar el `docker-compose.yml` (o crear un override) para añadir servicios `ac-worldserver` y `ac-db-import` adicionales. Se pueden copiar de las secciones principales, pero deben renombrarse para que no haya colisión.


## Preguntas frecuentes

### ¿Cómo instalo módulos?

Instalar módulos para docker es igual que instalar módulos para la instalación clásica: clona el módulo en `./modules` y vuelve a ejecutar el build. La diferencia es que el comando para docker no es el mismo que el clásico.

Para añadir un módulo, coloca el directorio del módulo dentro del directorio `/azerothcore-wotlk/modules`.

Después de añadir un módulo, tendrás que [reconstruir el servidor](#installation) y reiniciar los contenedores.

Por ejemplo, para instalar `mod-solocraft`:

```console
# Clona el módulo en modules con el nombre del repositorio
$ git clone https://github.com/azerothcore/mod-solocraft.git modules/mod-solocraft
# Instala los archivos SQL (OPCIONAL)
$ cp modules/mod-solocraft/data/sql/db-characters/mod_solo_craft.sql data/sql/custom/db_characters
# Reconstruye Azerothcore
$ docker compose up -d --build
```

Las configuraciones mediante variables de entorno funcionan con los módulos; sin embargo, si prefieres archivos de configuración, tendrás que colocarlos en el directorio `azerothcore-wotlk/env/dist/etc/modules`. Si este directorio modules no existe, tendrás que crearlo manualmente.

Ten en cuenta que el SQL también necesita instalarse manualmente; esto puede semi-automatizarse moviendo los archivos SQL al directorio correspondiente bajo `data/sql/custom`, o puedes ejecutar el archivo SQL contra la base de datos correcta.

### ¿Dónde están los logs del servidor?

Con docker, es común que las aplicaciones registren logs en la consola. Al registrar en la consola, docker se encarga de la rotación y persistencia de los logs. Puedes verlos con el comando `docker compose logs`.

Además, se encuentran en `env/dist/logs`, aunque esto puede eliminarse en el futuro.

### Cómo lidiar con los problemas de permisos

#### [Linux] Debes ejecutar docker sin sudo

Es importante ejecutar Docker sin usar sudo ni el usuario root. Para ello debes configurar tu usuario actual para que forme parte del grupo docker.

Esto se indica en la documentación de docker: [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)

### ¿Cómo puedo eliminar mis archivos de base de datos?

**Advertencia**: una vez que hayas eliminado tus archivos de base de datos, son irrecuperables a menos que tengas un backup.

Para eliminar tus archivos de base de datos, primero asegúrate de que tus contenedores se hayan detenido y eliminado escribiendo: `docker compose down`.

Después de detener y eliminar tus contenedores, puedes proceder a eliminar el volumen escribiendo: `docker volume rm azerothcore-wotlk_ac-database`

**Nota**: si cambiaste el nombre de tu carpeta respecto al `azerothcore-wotlk` por defecto, el nombre del volumen será ligeramente distinto. Para encontrar el nuevo nombre del volumen puedes usar el comando `docker volume ls`. El volumen debería estar etiquetado con algo parecido a `xxxx_ac-database`.

### Construir los contenedores con el bridge por defecto de docker deshabilitado

Si tienes `{"bridge":"none"}` en tu archivo de configuración del daemon de docker (en `/etc/docker/daemon.json`), hay 2 formas de construir correctamente los contenedores.

Esto a veces puede venir acompañado de este mensaje de error:

```
WARN[0000] buildx: failed to read current commit information with git rev-parse --is-inside-work-tree
network mode "ac-network" not supported by buildkit - you can define a custom network for your builder using the network driver-opt in
buildx create
```

Para arreglar los builds en este caso, se puede crear un `docker-compose.override.yml` que establezca el modo de red del build en `host`, permitiendo que los contenedores se construyan correctamente:

```yaml
# docker-compose.override.yml
services:
  ac-worldserver:
    build:
      network: host
  ac-authserver:
    build:
      network: host
  ac-db-import:
    build:
      network: host
  ac-client-data-init:
    build:
      network: host
```

Ten en cuenta que esto no funciona en Windows ni MacOS

Una sintaxis donde `network` se establece al nombre de la red (o sea `ac-network` en lugar de `host` en el ejemplo de arriba) debería funcionar correctamente, pero desafortunadamente esto parece no estar funcionando o no estar soportado por docker, como se evidencia en el [issue de Github](https://github.com/docker/buildx/issues/175)

### Optimizaciones de rendimiento (para servidor de desarrollo)

NOTA: si no estás experimentando ningún problema particular con el rendimiento de I/O, sugerimos **NO** usar esta configuración

Es bien sabido que **osxfs** y NTFS tienen [limitaciones de rendimiento](https://github.com/docker/for-mac/issues/1592) con los volúmenes montados (binded) de docker; optimizamos el docker compose usando volúmenes y la estrategia "delegated/cached" cuando es posible, pero eso no es suficiente para algunas configuraciones.

* **Usuarios de Windows:** sugerimos usar [WSL2](https://docs.docker.com/desktop/windows/wsl/) para clonar nuestro repo y trabajar con docker. Tiene un rendimiento similar al de un entorno linux nativo

* **Usuarios de Mac:** desafortunadamente no hay algo similar a WSL2 en Mac; sin embargo, solo el `ac-dev-server` usa volúmenes de src montados (binded) que pueden causar esa lentitud.
  Si aún quieres usar el `ac-dev-server` en Mac, considera probar el [de acore-docker](https://www.azerothcore.org/acore-docker/#dev-server). Usa volúmenes con nombre (named) que son mucho más rápidos que los montados.

### Referencia de Docker y solicitudes de soporte

Para administradores de servidores, recomendamos leer la [documentación de Docker](https://docs.docker.com/) así como la [referencia de Docker Compose](https://docs.docker.com/compose/reference/overview/).

Si quieres ser administrador de un servidor de producción de AzerothCore, ayuda estar familiarizado y cómodo con Docker y con el uso de la línea de comandos.

No dudes en hacer preguntas en [StackOverflow](https://stackoverflow.com/) y enlazarlas en el canal **#support-docker** de nuestro [chat de Discord](https://stackoverflow.com/questions/tagged/azerothcore). ¡Estaremos encantados de ayudarte!

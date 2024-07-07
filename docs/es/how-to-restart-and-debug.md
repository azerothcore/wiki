# Cómo reiniciar y depurar

AzerothCore está compuesto por 2 servicios: `authserver` y `worldserver`.

- Authserver sólo actúa como un autentificador y un router para sus reinos redirigiendo las conexiones de sus clientes autorizados a la dirección del reino seleccionado.
- En cambio, el servidor de mundos (worldserver) se encarga de todas las conexiones relacionadas con la mecánica del juego y es la única fuente de verdad para todo lo relacionado con un solo reino.

`authserver` y `worldserver` pueden ser colocados en diferentes entornos, sin embargo, en la siguiente guía le explicaremos cómo ejecutarlos juntos en el mismo entorno.

## Cómo iniciar los servicios

Tanto authserver como worldserver pueden iniciarse simplemente ejecutando los binarios compilados después de [completar la instalación](Installation).

## Cómo configurar un reinicio

El reinicio y la depuración de una aplicación funcionan de manera muy diferente dependiendo de su sistema operativo. Por eso siempre sugerimos utilizar nuestra solución docker que es totalmente compatible con todas las plataformas.

Sin embargo, si necesitas mantener tu servidor en funcionamiento después de una caída y comprobar qué ocurre con tu código, puedes hacerlo utilizando un reiniciador y un depurador.

A continuación vamos a explicar cómo utilizar nuestros scripts de reinicio integrados y la utilidad de depuración [GDB](https://www.gnu.org/software/gdb/) también para generar `crash-dumps`.

### Restarter usando acore dashboard (sólo para bash)

Puedes utilizar `./acore.sh run-worldserver` y `./acore.sh run-authserver`.

Ambos funcionan de forma inmediata cuando se compila con el dashboard.

**NOTA:** Para habilitar GDB puede utilizar `AC_RESTARTER_WITHGDB=true` como variable de entorno o añadiendo esto a su archivo `/conf/config.sh`.

Después de habilitar GDB, si el servidor se bloquea, encontrarás el archivo crashdump (gdb.txt) dentro de la carpeta `/env/`. **Tenga en cuenta que debe compilar su código con uno de los siguientes tipos de compilación: Debug o RelWithDebInfo, de lo contrario GDB no funcionará correctamente**.

### Uso de docker (multiplataforma)

Nuestro sistema docker integra los scripts anteriores dentro de `docker-compose`. Esto significa que habilitar el `GDB` funciona exactamente de la misma manera en docker también.

Además, nuestro `docker-compose` utiliza la función [política de reinicio](https://docs.docker.com/config/containers/start-containers-automatically/) para mantener los contenedores en funcionamiento.

Para más información, consulte la documentación [Instalación con Docker](install-with-docker).

También encontrarás una guía sobre cómo depurar tu código utilizando VSCode combinado con su extensión Remote Docker.

### Reiniciador avanzado (sólo para bash)

Si desea un reinicio más avanzado que incluya otras configuraciones útiles, puede probar nuestro sistema `run-engine` escrito en bash.

[Aquí](https://github.com/azerothcore/azerothcore-wotlk/tree/master/apps/startup-scripts) puedes encontrar los reinicios para entornos linux/bash.

Estos scripts se copian automáticamente después de la compilación en el directorio `/dist` si estás usando nuestro dashboard `./acore.sh`.

Puede copiar el archivo `conf.sh.dist` y crear un archivo `conf-world.sh` para personalizar esas configuraciones documentadas (haga lo mismo con el archivo `conf-auth.sh`). De esta manera, tienes tanto el restarter como el gdb preconfigurados para crear un archivo `gdb.txt` (crashdump) cuando el núcleo se bloquea. Asegúrese de utilizar la compilación `RelWithDebInfo` o `Debug` (en su comando CMake) para obtener informes de fallos significativos.

Luego copia el `restarter-world.sh` y el `restarter-auth.sh` de los "ejemplos" al lado de tu archivo conf y en la misma carpeta del archivo "run-engine".

Al final tendrás algo así:

[![example][1]][1]

Ejecuta esos 2 script de reinicio para tener tanto el reinicio de authserver como el de worldserver con soporte gdb.

### De forma manual (multiplataforma)

Asegúrese siempre de utilizar la compilación **RelWithDebInfo** o **Debug** (en su comando CMake) para obtener informes de fallos significativos.

Crea un archivo llamado `gdb.conf` con esto dentro:

```bash
set logging on
set debug timestamp
run -c ../etc/worldserver.conf
bt
bt full
info thread
thread apply all backtrace full
```

Luego, para depurar o crear un crashdump sólo tienes que usar el comando gdb como se describe en su documentación:

```bash
gdb -x gdb.conf --batch ./worldserver
```

Este comando debería ser suficiente tanto para conectar su IDE para depurar su código como para generar un crashdump cuando el servidor se bloquea

Para un reinicio "universal" y más avanzado, personalmente estoy usando [PM2][2]

```bash
pm2 start "gdb -x gdb.conf --batch ./worldserver"
```

Debería ser suficiente para reiniciar automáticamente, monitorear y gdb su servidor

[1]: https://i.stack.imgur.com/EyIi7.png
[2]: https://pm2.keymetrics.io/

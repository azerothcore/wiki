---
tableofcontents: 1
---

# Cómo reiniciar y depurar

AzerothCore está compuesto por dos servicios: authserver y worldserver.
El authserver solo actúa como autenticador y router para tus reinos, redirigiendo las conexiones autorizadas de tus clientes a la dirección del reino seleccionado.
El worldserver, en cambio, se encarga de todas las conexiones relacionadas con la mecánica del juego y es la única fuente de verdad para todo lo relacionado con un reino concreto.

El authserver y los worldservers pueden colocarse en entornos diferentes. Sin embargo, en la siguiente guía explicaremos cómo ejecutarlos juntos en el mismo entorno.

## El motor `startup-scripts`

Hemos introducido un nuevo conjunto de startup scripts que ofrecen una forma potente y unificada de ejecutar, gestionar y depurar tus servidores. Esta es ahora la forma recomendada de manejar los procesos `authserver` y `worldserver` para todas las instalaciones que no usen Docker.

Estos scripts ofrecen funcionalidades avanzadas como reinicios automáticos mediante systemd o PM2, gestión de sesiones (usando `tmux` o `screen`) y depuración con GDB integrada para el análisis de fallos.

Para una guía completa sobre cómo usar y configurar los nuevos startup scripts, consulta el **[README.md ubicado en el directorio startup-scripts](https://github.com/azerothcore/azerothcore-wotlk/blob/master/apps/startup-scripts/README.md)** oficial.

### Uso básico

La forma más sencilla de usar el nuevo sistema es a través del dashboard acore.sh:

```bash
# Para ejecutar el worldserver con el nuevo motor
./acore.sh run-worldserver

# Para ejecutar el authserver con el nuevo motor
./acore.sh run-authserver
```

### Configuración y depuración

Para habilitar el GNU Debugger (GDB) y generar reportes de fallos, necesitas editar el archivo de configuración de tu servicio. Por ejemplo, para un servicio llamado `ac-world-1`, editarías un archivo similar a ac-world-1-run-engine.conf y establecerías `GDB_ENABLED=1`.

```properties
// ...existing code...
# Habilitar/deshabilitar la ejecución de GDB
export GDB_ENABLED=1
// ...existing code...
```

Si el servidor falla después de habilitar GDB, encontrarás el archivo crashdump (p. ej. `gdb-YYYY-MM-DD-HH-MM-SS.txt`) dentro del directorio `apps/startup-scripts/logs/crashes/`. **Ten en cuenta que debes compilar tu código con uno de los siguientes tipos de compilación: `Debug` o `RelWithDebInfo`; de lo contrario, GDB no producirá reportes útiles.**

## Uso de Docker (multiplataforma)

Nuestra configuración de Docker integra el motor `startup-scripts`. Esto significa que habilitar GDB y gestionar los reinicios también funciona sin problemas dentro del entorno de Docker. Además, nuestro docker-compose.yml usa la [funcionalidad de restart-policy](https://docs.docker.com/config/containers/start-containers-automatically/) para mantener automáticamente los contenedores en funcionamiento tras un fallo o un reinicio del sistema.

Para más información, consulta la documentación de [Instalación con Docker](install-with-docker). También encontrarás una guía sobre cómo depurar tu código usando VSCode combinado con su extensión Remote Docker.

# Configuración del registro (tipo log4j)

## Configuración del registro en el núcleo

```cpp
LOG_TYPE("appender", "LOG MESSAGE {}", var);

// Example
LOG_ERROR("sql.sql", "Unable to load creature entry {} and spawnId {}", entry, guid);
```

Para pasar cualquier argumento al MENSAJE DE REGISTRO utilice las llaves, que utilizan el formato FMT para tomar cualquier argumento y pasarlo al REGISTRO.

## Tipo

- FATAL
- ERROR
- WARN
- INFO
- DEBUG
- TRACE

## Registradores y anexos

El sistema de registro tiene dos componentes: los registradores y los anexos. Estos tipos de componentes permiten a los usuarios registrar los mensajes según el tipo y el nivel de los mismos y controlar en tiempo de ejecución dónde se reportan.

### Registradores

La primera y principal ventaja de este sistema residía en la posibilidad de deshabilitar ciertas declaraciones de registro mientras se permitía que otras se imprimieran sin problemas.

Esta capacidad supone que los registradores se clasifican de acuerdo con algunos criterios elegidos por el desarrollador.

Los registradores son entidades con nombre. Los nombres de los registradores distinguen entre mayúsculas y minúsculas y siguen la regla de nomenclatura jerárquica:

Se dice que un registrador es antecesor de otro registrador si su nombre seguido de un punto es un prefijo del nombre del registrador descendiente. Se dice que un registrador es padre de un registrador hijo si no hay ancestros entre él mismo y el registrador descendiente.

Por ejemplo, el registrador llamado `entities.player` es un padre del registrador llamado `entities.player.character`. Del mismo modo, `entities` es un padre de `entities.player` y un ancestro de `entities.player.character`.

Se pueden asignar niveles a los registradores. El conjunto de niveles posibles son TRACE, DEBUG, INFO, WARN, ERROR y FATAL, o bien desactivarse mediante el nivel DISABLED.

Por definición, el método de impresión determina el nivel de una solicitud de registro. Por ejemplo, LOG_INFO(...) es una solicitud de registro de nivel INFO.

Se dice que una solicitud de registro está habilitada si su nivel es mayor o igual que el nivel de su registrador. En caso contrario, se dice que la solicitud está deshabilitada. Un registrador sin nivel asignado heredará uno de la jerarquía.

Ejemplo:

| Logger Name | Assigned Level | Inherited Level |
| :---------- | :------------- | :-------------- |
| root        | Proot          | Proot           |
| server      | None           | Proot           |

Como "servidor" no está definido, utiliza el registrador raíz y su nivel de registro.

FATAL < ERROR < WARN < INFO < DEBUG < TRACE.

### Apuntadores

La capacidad de habilitar o deshabilitar selectivamente las solicitudes de registro en función de sus registradores es sólo una parte del panorama. Este sistema permite que las solicitudes de registro se impriman en múltiples destinos. Un destino de salida se llama appender.

El sistema actual define appenders para la consola, los archivos y la base de datos, pero puede extenderse fácilmente al servidor de socket remoto, a los registradores de eventos de NT, a los demonios de syslog o a cualquier otro sistema.

Se puede adjuntar más de un appender a un registrador. Cada solicitud de registro habilitada para un determinado registrador se enviará a todos los anexos de ese registrador.

### Configuración

El sistema leerá todos los elementos de configuración con el prefijo "Logger." y "Appender." y configurará el sistema de registro. Si el "root" no puede ser configurado correctamente el núcleo eliminará todos los loggers y appenders y creará un conjunto por defecto:

- Logger `root` con nivel de log Error
- Logger `server` con nivel de registro Info
- Appender `Console` para registrar en la consola

La línea de configuración de la aplicación sigue el formato:

> Type,LogLevel,Flags,optional1,optional2

Es una lista de elementos separados por comas donde cada elemento tiene su propio significado

```
Tipo: Tipo del anexos

1 - (Console)
2 - (File)
3 - (DB)

LogLevel: Log level

0 - (Disabled)
1 - (Fatal)
2 - (Error)
3 - (Warning)
4 - (Info)
5 - (Debug)
6 - (Trace)

flags: Definir algunas modificaciones adicionales para hacer a los mensajes de registro

1 - Prefix Timestamp to the text
2 - Prefix Log Level to the text
4 - Prefix Log Filter type to the text
8 - Append timestamp to the log file name. Format: YYYY-MM-DD_HH-MM-SS (Only used with Type = 2)
16 - Make a backup of existing file before overwrite (Only used with Mode = w)
```

Dependiendo del tipo, los elementos optional1 y optional2 tomarán diferentes

```
Colors (read as optiona11 if Type = Console)

Format: "fatal error warn info debug trace"
0 - BLACK
1 - RED
2 - GREEN
3 - BROWN
4 - BLUE
5 - MAGENTA
6 - CYAN
7 - GREY
8 - YELLOW
9 - LRED
10 - LGREEN
11 - LBLUE
12 - LMAGENTA
13 - LCYAN
14 - WHITE
Example: "1 9 3 6 5 8"

File: Nombre del archivo (leído como opcional1 si Tipo = Archivo)
Permite utilizar un "%u" para crear archivos dinámicos

Mode: Modo para abrir el archivo (leído como opcional2 si Type = File)

a - (Append)
w - (Overwrite)
```

Ejemplo:

```
Appender.Console1=1,5,6
```

Crea un nuevo appender para registrar en la consola cualquier mensaje con nivel de registro DEBUG o superior y antepone el tipo y nivel de registro al mensaje.

```
Appender.Console2=1,2,1,"1 9 3 6 5 8"
```

Crea un nuevo appender para registrar en la consola cualquier mensaje con nivel de registro ERROR o superior y antepone la marca de tiempo al mensaje usando texto coloreado.

```
Appender.File=2,5,7,Auth.log,w
```

Crea un nuevo appender para registrar en el archivo "Auth.log" cualquier mensaje con nivel de registro DEBUG o superior y antepone la marca de tiempo, el tipo y el nivel al mensaje

En el ejemplo, tener dos loggers diferentes para registrar en la consola es perfectamente legal pero redundante.

Una vez que tenemos la lista de loggers para leer, el sistema intentará configurar un nuevo logger desde su línea de configuración. La línea de configuración del logger sigue el formato

> LogLevel,AppenderList

Es una lista de elementos separados por comas donde cada elemento tiene su propio significado

```
LogLevel

0 - (Disabled)
1 - (Fatal)
2 - (Error)
3 - (Warning)
4 - (Info)
5 - (Debug)
6 - (Trace)

AppenderList: List of appenders linked to logger
(Using spaces as separator).
```

## Ejemplos

### Ejemplo 1

Registrar los errores en la consola y en un archivo llamado server.log que sólo contenga los registros de esta ejecución del servidor. El archivo debe tener un prefijo de marca de tiempo, tipo y nivel de registro en los mensajes. La consola debe poner el prefijo de tipo y nivel de registro.

```
Appender.Console=1,2,6
Appender.Server=2,2,7,Server.log,w
Logger.root=2,Console Server
```

Vamos a rastrear cómo el sistema registrará dos mensajes diferentes:

1. LOG_ERROR("guild", "Guild 1 created");

El sistema intentará encontrar un registrador de tipo GUILD, pero como no hay ningún registrador configurado para GUILD, utilizará el registrador raíz. Como el nivel de registro del mensaje es igual o mayor que el nivel de registro del logger, el mensaje se envía a los Appenders configurados en el Logger. "Consola" y "Servidor".

La consola escribirá: "ERROR [GUILD] Guild 1 created"

El servidor escribirá en el archivo "2012-08-15 ERROR [GUILD] Guild 1 created"

2. LOG_INFO("entities.player.character", "Player Name Logged in");

El sistema intentará encontrar un logger de tipo "character", como no hay ningún logger configurado para "character" utilizará el logger Root. Como el nivel de registro del mensaje no es igual o mayor que el nivel de registro del registrador, el mensaje se descarta.

### Ejemplo 2

El mismo ejemplo que el anterior, pero ahora quiero ver todos los mensajes de nivel INFO en el archivo y el archivo del servidor debe añadir la marca de tiempo en la creación.

```
Appender.Console=1,2,6
Appender.Server=2,4,15,Server.log
Logger.root=3,Console Server
```

Vamos a rastrear cómo el sistema registrará dos mensajes diferentes:

1. LOG_ERROR("guild", "Guild 1 created");

Realiza exactamente lo mismo que el ejemplo 1.

2. LOG_INFO("entities.player.character", "Nombre del jugador registrado");

El sistema intentará encontrar un logger de tipo "personaje", como no hay ningún logger configurado para "personaje" utilizará el logger Root. Como el nivel de registro del mensaje es igual o mayor que el nivel de registro del logger, el mensaje se envía a los Appenders configurados en el Logger. "Consola" y "Servidor".

La consola descartará el mensaje ya que el nivel de registro no es mayor o igual al de este appender.

El servidor escribirá en el archivo "2012-08-15 INFO [CHARACTER] Nombre del jugador conectado"

### Ejemplo 3

Como dev, puedo estar interesado en registrar sólo una parte particular del núcleo mientras trato de arreglar algo. Así que... quiero depurar "guild" al máximo y también algunos eventos de "personaje" hasta cierto punto. También estoy comprobando algunos Waypoints así que quiero que "sql.dev" se registre en un archivo sin prefijos. Todos los demás mensajes deben ser registrados en la consola, "guild" en TRACE y "character" en INFO.

```
Appender.Console=1,6
Appender.SQLDev=2,5,0,SQLDev.log
Logger.guild=6,Console
Logger.entities.player.character=4,Console
Logger.sql.dev=4,SQLDev
```

Con esta configuración, cualquier logger de mensajes con un tipo de log diferente a "guild", "character" o "sql.dev" será ignorado, ya que no definimos un logger Root y el sistema creó un Root deshabilitado por defecto. Consola del Appender, el nivel de log debe ser definido para permitir todos los posibles mensajes de sus loggers, en este caso "guild" usa TRACE (6), por lo que el Appender debe permitirlo. Logger Characters limitará sus propios mensajes a INFO (4).

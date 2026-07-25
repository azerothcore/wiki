# game_event

[<-Volver a:World](database-world)

**Tabla \`game_event\`**

**Estructura**

Esta tabla contiene las definiciones de todos los eventos de juego que el sistema de eventos (Game Event System) del core activa o desactiva automáticamente.

| Field                        | Type         | Attributes | Key | Null | Default | Extra  | Comment                                                                                                                              |
| ---------------------------- | ------------ | ---------- | --- | ---- | ------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| [eventEntry](#evententry)    | TINYINT      | UNSIGNED   | PRI | NO   |         | Unique | Entry del evento de juego                                                                                                            |
| [start_time](#starttime)     | TIMESTAMP    |            |     | YES  | NULL    |        | Fecha de inicio absoluta; el evento nunca empezará antes de esta                                                                      |
| [end_time](#endtime)         | TIMESTAMP    |            |     | YES  | NULL    |        | Fecha de fin absoluta; el evento nunca empezará después de esta; si es NULL se fija implícitamente a 2 años en el futuro en cada arranque del servidor |
| [occurrence](#occurrence)    | BIGINT       | UNSIGNED   |     | NO   |         |        | Retardo en minutos entre repeticiones del evento                                                                                     |
| [length](#length)            | BIGINT       | UNSIGNED   |     | NO   |         |        | Duración en minutos del evento                                                                                                        |
| [holiday](#holiday)          | MEDIUMINT    | UNSIGNED   |     | NO   |         |        | Id de festividad del lado del cliente (del dbc)                                                                                       |
| [holidayStage](holidaystage) | TINYINT      | UNSIGNED   |     | NO   |         |        |                                                                                                                                      |
| [description](#description)  | VARCHAR(255) | SIGNED     |     | YES  | NULL    |        | Descripción del evento mostrada en consola                                                                                            |
| [world_event](#worldevent)   | TINYINT      | UNSIGNED   |     | NO   |         |        | 0 si es un evento normal, 1 si es un evento mundial                                                                                   |
| [announce](#announce)        | TINYINT      | UNSIGNED   |     | YES  | 2       |        | 0 no anunciar, 1 anunciar, 2 valor de la configuración                                                                               |

**Descripción de los campos**

### eventEntry

Entry del evento. Mantenlo tan bajo como sea posible y evita dejar huecos en la lista. Cuanto mayor sea el id máximo, más memoria se usará para almacenar los datos del evento.

### start_time

Fecha de inicio absoluta del evento. El evento solo empezará a ocurrir si la hora local del servidor es posterior a la fijada aquí.

{% include note.html content="Para los eventos ligados a festividades con cálculo de fecha dinámico (Pascua, Año Nuevo Lunar, Acción de Gracias, etc.), start_time se calcula automáticamente al arrancar el servidor y sobrescribe cualquier valor fijado en la base de datos. Consulta la sección Sistema de festividades dinámicas más abajo." %}

### end_time

Fecha de fin absoluta del evento. El evento dejará de ocurrir si la hora local del servidor es posterior a la fijada aquí.

{% include note.html content="Para los eventos ligados a festividades con cálculo de fecha dinámico, end_time se calcula automáticamente a partir de la duración del evento y de start_time." %}

### occurrence

Número de minutos entre 2 repeticiones del evento. (2880 = 2 días, 1440 = 1 día, etc.)

{% include warning.html content="El valor no puede ser 0 o el servidor se colgará." %}

### length

Número de minutos que durará el evento tras el inicio de la repetición. (2880 = 2 días, 1440 = 1 día, etc.)
Este valor debe ser menor que el de occurrence o el evento nunca terminará.


### holiday

Id de festividad del [archivo DBC Holidays](holidays). Se envía al cliente para actualizar el calendario.

### description

Cadena que contiene el nombre del evento mostrado en consola cada vez que empieza o termina.

### world_event

Este es un campo booleano que determina si este evento de juego es un evento mundial o no. 0 = evento normal, 1 = evento mundial. Para que el evento mundial funcione necesitas, como mínimo, poblar [game_event_condition](game_event_condition) y [game_event_quest_condition](game_event_quest_condition).

### announce

| Value | Description                                          |
| ----- | ---------------------------------------------------- |
| 0     | No anunciar el evento                                |
| 1     | Anunciar la descripción del evento al mundo          |
| 2     | Usar la configuración `event.announce` del config    |

## Sistema de festividades dinámicas

Algunas festividades ocurren en fechas que varían de un año a otro. Para estas festividades, el servidor calcula automáticamente las fechas correctas al arrancar mediante algoritmos astronómicos y reglas de calendario.

### Festividades calculadas dinámicamente

| Holiday ID | Holiday Name | Método de cálculo |
| ---------- | ------------ | ------------------ |
| 141 | Feast of Winter Veil | 6 días antes del solsticio de invierno (15-16 dic) |
| 181 | Noblegarden | El día después del Domingo de Pascua |
| 201 | Children's Week | Primer lunes en o después del 25 de abril |
| 283 | Harvest Festival | 2 días antes del equinoccio de otoño |
| 301 | Hallow's End | Fijo el 18 oct |
| 321 | Lunar Festival | El día antes del Año Nuevo Chino (cálculo lunar astronómico) |
| 324 | Midsummer Fire Festival | Fijo el 21 jun |
| 327 | Brewfest | Primer sábado en o después del 15 sep, menos 7 días |
| 335 | Love is in the Air | Primer lunes en o después del 3 feb |
| 341 | Day of the Dead | Fijo el 1 nov |
| 372 | Pilgrim's Bounty | 4.º jueves de noviembre menos 4 días |
| 374 | Darkmoon Faire (Elwynn) | Primer domingo de mar/jun/sep/dic menos 2 días |
| 375 | Darkmoon Faire (Mulgore) | Primer domingo de ene/abr/jul/oct menos 2 días |
| 376 | Darkmoon Faire (Terokkar) | Primer domingo de feb/may/ago/nov menos 2 días |

### Cómo funciona

1. Al arrancar el servidor, `GameEventMgr::LoadHolidayDates()` recorre todas las reglas de festividades
2. Para cada festividad se calculan las fechas de varios años (año actual ± varios años)
3. Las fechas calculadas se escriben en el array Date[] de `Holidays.dbc` para mostrarlas en el calendario
4. El `start_time` y `end_time` del game_event correspondiente se actualizan para coincidir con la siguiente repetición
5. Los eventos se reprograman automáticamente tras completarse cada repetición

### Notas

- La tabla de base de datos `holiday_dates` ha sido **eliminada**: ahora todas las fechas se calculan dinámicamente
- Las fechas del calendario se pueblan para ~4 años para asegurar que el calendario del juego se muestre correctamente
- Darkmoon Faire tiene varias repeticiones al año, rotando mensualmente entre Mulgore (ene), Terokkar (feb), Elwynn (mar), y repitiendo

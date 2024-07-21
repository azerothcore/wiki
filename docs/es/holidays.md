# Holidays

## holidays.dbc

[`Volver a:DBC`](dbc-index)

## Estructura

| Columna | Campo                         | Tipo    | Notas                                                                                      | Info Extra                                                                                           |
|---------|-------------------------------|---------|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| 0       | [eventID][1]                  | Integer | ID del Evento de Festividad                                                                |                                                                                                      |
| 1       | [eventStage1Duration][2]      | Integer | Duración del evento (en la fase 1)                                                         | Ya sea como evento de preparación o evento principal. Véase eventSchedulerType para más información) |
| 2       | [eventStage2Duration][3]      | Integer | Duración del evento (en la fase 2)                                                         | Ya sea como evento principal o de reinicio. Véase eventSchedulerType para más información)           |
| 11      | [eventDate][4]                | Integer | Packed blizzdate - Epochdate=01.01.2000-00:00 - El año se descarta si la columna12 es 0    |                                                                                                      |
| 37      | [Region][5]                   | integer | ??? (necesita ser investigado)                                                             |                                                                                                      |
| 38      | [Looping][6]                  | integer | ??? (necesita ser investigado - se utiliza sólo en los eventos de Llamamiento a las armas) | 283 - Llamamiento a las armas: Valle de Alterac                                                      |
|         |                               |         |                                                                                            | 284 - Llamamiento a las armas: Garganta Grito de Guerra                                              |
|         |                               |         |                                                                                            | 285 - Llamamiento a las armas: Cuenca de Arathi                                                      |
|         |                               |         |                                                                                            | 353 - Llamamiento a las armas: Ojo de la tormenta                                                    |
|         |                               |         |                                                                                            | 400 - Llamamiento a las armas: Playa de los Ancestros                                                |
|         |                               |         |                                                                                            | 420 - Llamamiento a las armas: Isla de la Conquista                                                  |
| 39      | [calendarFlags][7]            | integer | ??? (necesita ser investigado)                                                             |                                                                                                      |
| 49      | [eventCalendarName][8]        | iRefID  | Referencia al Loc(idioma) en HolidayNames.dbc                                              |                                                                                                      |
| 50      | [eventCalendarDescription][9] | iRefID  | Referencia al Loc(idioma) en HolidayNames.dbc                                              |                                                                                                      |
| 51      | [eventCalendarOverlay][10]    | String  | Textura superpuesta utilizada para la decoración de eventos del calendario del juego       |                                                                                                      |
| 52      | [priority][11]                | Integer | ??? (necesita ser investigado)                                                             |                                                                                                      |
| 53      | [eventSchedulerType][12]      | Integer | Definición sobre qué tipo de temporizador se utiliza, véase eventSchedulerType             | -1: repetición, anualmente                                                                           |
|         |                               |         |                                                                                            | 0: repetición, semanalmente                                                                          |
|         |                               |         |                                                                                            | 1: repetición, usado en fechas definidas                                                             |
|         |                               |         |                                                                                            | 2: repetición, por hora                                                                              |
| 54      | [eventFlags][13]              | Integer | ??? (necesita ser investigado)                                                             |                                                                                                      |
 
[1]: #eventid
[2]: #eventstage1duration
[3]: #eventstage2duration
[4]: #eventdate
[5]: #region
[6]: #looping
[7]: #calendarflags
[8]: #eventcalendarname
[9]: #eventcalendardescription
[10]: #eventcalendaroverlay
[11]: #priority
[12]: #eventschedulertype
[13]: #eventflags

### eventID

### eventStage1Duration

### eventStage2Duration

### eventDate

### Region

### Looping

### calendarFlags

### eventCalendarName

### eventCalendarDescription

### eventCalendarOverlay

### priority

## eventSchedulerType
```
eventSchedulerType define qué tipo de temporizador se usa para que el evento se detenga o inicie, etc. - y en caso también de que utilice diferentes etapas durante su fase de "acumulación" (2 etapas disponibles)
-1: el evento se repite anualmente basado en las fechas de la columna11, columna12, etc. - la duración y las posibles fases del evento se toman de la información dada en la columna1 y la columna2 (fijada en DBC para mantenerla en línea con los cambios **anuales**) - En caso de que la columna12 equivalga al valor 0 usaría sólo la FECHA del campo11
0: el evento se repite cada 7 días, con una duración de un tiempo de tipo <eventStage1Duration> (duración de primera fase) (fecha de inicio codificada en el servidor dependiendo del tipo de ID del evento)
1: el evento se repite en base a los valores de la columna11, columna12, etc. (ver -1) - En caso de que <eventStage2Duration> (duración de segunda fase) exista, se utiliza primero <eventStage1Duration> (duración de primera fase) como duración de la fase previa al evento
2: el evento se repite cada X horas (siendo <eventStage2Duration> el temporizador eventPause/eventWait)
```

### eventFlags

# achievement\_dbc

[<-Volver a: World](database-world)

**La tabla \`achievement\_dbc\`**

Almacena la información de los logrso que falta en in [Achievement.dbc](achievement)

**Estructura**

| Field                | Type | Attributes | Key | Null | Default | Extra | Comment                                                                          |
| -------------------- | ---- | ---------- | --- | ---- | ------- | ----- | -------------------------------------------------------------------------------- |
| [ID][1]              | INT  | UNSIGNED   | PRI | NO   |         |       |                                                                                  |
| [requiredFaction][2] | INT  | SIGNED     |     | NO   | -1      |       |                                                                                  |
| [mapID][3]           | INT  | SIGNED     |     | NO   | -1      |       |                                                                                  |
| [points][4]          | INT  | UNSIGNED   |     | NO   | 0       |       | Achievement points awarded for completing the achievement, has no use serverside |
| [flags][5]           | INT  | UNSIGNED   |     | NO   | 0       |       |                                                                                  |
| [count][6]           | INT  | UNSIGNED   |     | NO   | 0       |       |                                                                                  |
| [refAchievement][7]  | INT  | UNSIGNED   |     | NO   | 0       |       |                                                                                  |

[1]: #id
[2]: #requiredfaction
[3]: #mapid
[4]: #points
[5]: #flags
[6]: #count
[7]: #refachievement

**Descripción de los campos**

### ID

Esta es la ID del logro de [Achievement\_Criteria.dbc](Achievement+Criteria) (2da columna)

### requiredFaction

| Condition | Faction |
| --------- | ------- |
| Both      | -1      |
| Horde     | 0       |
| Alliance  | 1       |

### mapID

Condición: El jugador debe estar en ese mapa para que se permitan las actualizaciones de los criterios. (-1 si no está configurado)

### points

Puntos de logro adquiridios al completar el logro. No tiene uso del lado del servidor.

### flags

| Name                               | Value      | Comment                                                                                              |
| ---------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------- |
| ACHIEVEMENT_FLAG_COUNTER           | 0x00000001 | Cuenta estadística, (nunca para y completa)                                                       |
| ACHIEVEMENT_FLAG_HIDDEN            | 0x00000002 | No enviado al cliente - solo para uso interno                                                               |
| ACHIEVEMENT_FLAG_STORE_MAX_VALUE   | 0x00000004 | Guarda solo el máximo valor? Usado solo en "Reach level xx"                                                  |
| ACHIEVEMENT_FLAG_SUMM              | 0x00000008 | Usa la suma de los valores de los criterios para todos los requisitos (y calcula el valor máximo)                               |
| ACHIEVEMENT_FLAG_MAX_USED          | 0x00000010 | Muestra el máximo de criterios (y calcula el valor máximo??)                                                       |
| ACHIEVEMENT_FLAG_REQ_COUNT         | 0x00000020 | Usa una cuenta de requisitos mayor a cero (y calcula el valor máximo)                                                     |
| ACHIEVEMENT_FLAG_AVERAGE           | 0x00000040 | Mostrado como valor promedio (valor / tiempo en días) depende de otra flag (por defecto usa el valor del ultimo criterio) |
| ACHIEVEMENT_FLAG_BAR               | 0x00000080 | Mostrado como barra de progreso (valor / valor máximo) depende de otra flag (por defecto usa el valor del ultimo criterio)      |
| ACHIEVEMENT_FLAG_REALM_FIRST_REACH | 0x00000100 |                                                                                                      |
| ACHIEVEMENT_FLAG_REALM_FIRST_KILL  | 0x00000200 |                                                                                                      |

### count

Debería ser siempre 1.

### refAchievement

Debería ser siempre 0.

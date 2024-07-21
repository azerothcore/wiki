# instance

[<-Volver a:Characters](database-characters)

**Tabla \`instance\`**

La tabla contiene información estática acerca de todas las instancias actuales que aún no han sido reiniciadas.

**Estructura**

| Field                    | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------ | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]                  | INT      | UNSIGNED   | PRI | NO   | 0       |       |         |
| [map][2]                 | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [resettime][3]           | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [difficulty][4]          | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [completedEncounters][5] | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [data][6]                | TINYTEXT | SIGNED     |     | NO   |         |       |         |

[1]: #id
[2]: #map
[3]: #resettime
[4]: #difficulty
[5]: #completedencounters
[6]: #data

**Descripción de los Campos**

### id

La ID de la instancia. El número debe de ser único para cada instancia.

### map

EL ID del mapa de la instancia respectiva. Ver [Map.dbc](map).

### resettime

La hora en la que se reiniciará la instancia en tiempo Unix. Este campo posee el valor cero para las instancias de tipo Raid y Heróicas.
El tiempo de reinicio de las instancias tipo Raid y Heróicas para cada grupo en específico se almacena en la tabla [instance_reset](instance_reset).

### difficulty

La dificultad de la instancia actual.

| Value | Description   |
| ----- | ------------- |
| 0     | 10 Normal     |
| 1     | 25 Normal     |
| 2     | 10 Heroico    |
| 3     | 25 Heroico    |

### completedEncounters

Número de encuentros completados de la instancia.

### data

Datos específicos de cada instancia (en texto).

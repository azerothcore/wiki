# pvpstats\_battlegrounds

[<-Volver a:Characters](database-characters.md)

**Tabla \`pvpstats\_battlegrounds\`**

La tabla contiene datos acerca de las puntuaciones en Campos de Batalla. Para habilitar el almacenamiento de este tipo de información, establezca **Battleground.StoreStatistics.Enable = 1** en el archivo **worldserver.config.dist** o **worldserver.config**.

**Estructura**

| Field               | Type     | Attributes | Key | Null | Default | Extra          | Comment |
| ------------------- | -------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [id][1]             | BIGINT   | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [winner_faction][2] | TINYINT  | SIGNED     |     | NO   |         |                |         |
| [bracket_id][3]     | TINYINT  | UNSIGNED   |     | NO   |         |                |         |
| [type][4]           | TINYINT  | UNSIGNED   |     | NO   |         |                |         |
| [date][5]           | DATETIME | SIGNED     |     | NO   |         |                |         |

[1]: #id
[2]: #winnerfaction
[3]: #bracketid
[4]: #type
[5]: #date

**Descripción de los Campos**

### id

Valor único que identifica el Campo de Batalla.

### winner\_faction

La facción que ganó en el Campo de Batalla:

| Valor | Descripción |
| ----- | ----------- |
| 0     | HORDA       |
| 1     | ALIANZA     |
| 2     | NINGUNO     |

### bracket\_id

Identificador del rango por niveles.

| Value | Level range |
| ----- | ----------- |
| 1     | 10-19       |
| 2     | 20-29       |
| 3     | 30-39       |
| 4     | 40-49       |
| 5     | 50-59       |
| 6     | 60-69       |
| 7     | 70-79       |
| 8     | 80          |

### type

Tipo de Campo de Batalla.

| Value | Description                       |
| ----- | --------------------------------- |
| 1     | Valle de Alterac                  |
| 2     | Garganta Grito de Guerra          |
| 3     | Cuenca de Arathi                  |
| 7     | Ojo de la Tormenta                |
| 9     | Playa de los Ancestros            |
| 30    | Isla de la Conquista              |

### date

Fecha y hora de finalización del Campo de Batalla.

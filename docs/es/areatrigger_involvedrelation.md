# areatrigger\_involvedrelation

[<-Volver a:World](database-world)

**Tabla \`areatrigger\_involvedrelation\`**

Permite que un trigger complete una condición de una quest (explorar)

Si hay un registro en la tabla para una quest, entonces la quest no se completará hasta que el jugador active este areatrigger. La quest no queda necesariamente terminada tras eso, pero sí queda satisfecha esa condición de la quest. Si la única condición de la quest es explorar un área, entonces la quest se completará.

**Estructura**

| Field      | Type      | Attributes | Key | Null | Default | Extra | Comments         |
| ---------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------------- |
| [id][1]    | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Identifier       |
| [quest][2] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       | Quest Identifier |

[1]: #id
[2]: #quest

**Descripción de los campos**

### id

Este es el ID del trigger de [AreaTrigger.dbc](DBC-AreaTrigger)

### quest

Este es el id de la quest a la que está ligado el trigger.

### Example

| id  | quest |
| --- | ----- |
| 78  | 155   |
| 87  | 76    |
| 88  | 62    |
| 98  | 201   |
| 169 | 287   |

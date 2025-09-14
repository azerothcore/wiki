# areatrigger\_involvedrelation

[<-Voler a:World](database-world)

**La \`areatrigger\_involvedrelation\` tabla**

Habilitar un disparador para finalizar una condición de una misión (explorar).

Si hay un registro en la tabla para una misión, esta no se completará hasta que el jugador active este disparador de área. La misión no termina necesariamente después de eso, pero se cumple esa condición. Si la única condición de la misión es explorar un área, se completará.

**Estructura**

| Campo      | Tipo      | Atributos | Llave | Nulo | Por defecto | Extra | Comentarios             |
| ---------- | --------- | --------- | ----- | ---- | ----------- | ----- | ----------------------- |
| [id][1]    | MEDIUMINT | UNSIGNED  | PRI   | NO   | 0           |       | Identificador           |
| [quest][2] | MEDIUMINT | UNSIGNED  |       | NO   | 0           |       | Identificador de misión |

[1]: #id
[2]: #quest

**Descripción de los campos**

### id

Este es el ID del activador de [AreaTrigger.dbc](DBC-AreaTrigger)

### quest

Este es el ID de la misión a la que está vinculado el disparador.

### Ejemplo

| id  | búsqueda |
| --- | -------- |
| 78  | 155      |
| 87  | 76       |
| 88  | 62       |
| 98  | 201      |
| 169 | 287      |

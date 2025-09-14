# areatrigger\_tavern

[<-Voler a:World](database-world)

**La \`areatrigger\_tavern\` tabla**

Activa un disparador cuando el jugador entra en una ciudad o taberna. Esto provoca que el jugador entre en estado de reposo.

**Estructura**

| Campo     | Tipo      | Atributos | Llave | Nulo | Por defecto | Extra | Comentario    |
| --------- | --------- | --------- | ----- | ---- | ----------- | ----- | ------------- |
| [id][1]   | MEDIUMINT | UNSIGNED  | PRI   | NO   | 0           |       | Identificador |
| [name][2] | text      |           |       | YES  |             |       |               |

[1]: #id
[2]: #name

**Descripción de los campos**

### id

Este es el identificador del disparador, consulte [AreaTrigger.dbc](DBC-AreaTrigger)

### name

Nombre de la ciudad o taberna. Esto es puramente descriptivo.

### Ejemplo

| id  | nombre                                         |
| --- | -------------------------------------------- |
| 71  | Westfall - Sentinel Hill Inn                 |
| 98  | Nesingwary's Expedition                      |
| 178 | Strahnbrad                                   |
| 562 | Elwynn Forest - Goldshire - Lion's Pride Inn |
| 682 | Redridge Mountains - Lakeshire Inn           |

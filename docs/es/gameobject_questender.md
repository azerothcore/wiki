# gameobject\_questender

[<-Volver a: World](database-world)

**Tabla \`gameobject\_questender\`**

Contiene las relaciones de objetos de juego que reciben misiones. Los objetos de juego de esta tabla deberían ser todos de tipo QUESTGIVER (2).

**Estructura**

| Field      | Type      | Attributes | Key | Null | Default | Extra | Comment          |
| ---------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------------- |
| [id][1]    | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |                  |
| [quest][2] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Quest Identifier |

[1]: #id
[2]: #quest

**Descripción de los campos**

### id

El ID de plantilla del objeto de juego. Ver [gameobject\_template.entry](http://www.azerothcore.org/wiki/gameobject_template#entry)

### quest

El ID de la misión que este objeto de juego finaliza. Ver [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id)

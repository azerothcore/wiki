# gameobject\_queststarter

[<-Volver a: World](database-world)

**Tabla \`gameobject\_queststarter\`**

Contiene las relaciones de objetos de juego que otorgan misiones. Los objetos de juego de esta tabla deberían ser todos de tipo QUESTGIVER (2).

**Estructura**

| Field      | Type      | Attributes | Key | Null | Default | Extra | Comment          |
| ---------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------------- |
| [id][1]    | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |                  |
| [quest][2] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Quest Identifier |

[1]: #id
[2]: #quest

**Descripción de los campos**

### id

El ID de plantilla del objeto de juego. Ver [gameobject\_template.entry](gameobject_template#entry)

### quest

El ID de la misión que este objeto de juego inicia. Ver [quest\_template.id](quest_template#id)

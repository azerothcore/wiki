# creature\_queststarter

[<-Volver a:World](database-world)

**Tabla \`creature\_queststarter\`**

Contiene las relaciones entre los NPC que otorgan misiones y qué NPC inician determinadas misiones.

**Estructura**

| Campo      | Tipo      | Atributos | Llave | Nulo | Por defecto | Extra | Comentario              |
| ---------- | --------- | --------- | ----- | ---- | ----------- | ----- | ----------------------- |
| [id][1]    | MEDIUMINT | UNSIGNED  | PRI   | NO   | 0           |       | Identificador           |
| [quest][2] | MEDIUMINT | UNSIGNED  | PRI   | NO   | 0           |       | Identificador de misión |

[1]: #id
[2]: #quest

**Descripción de los campos**

### id

El ID de la criatura. Ver [creature\_template.entry](http://www.azerothcore.org/wiki/creature_template#creature_template-entry)

### quest

El ID de la misión que inicia la criatura. Ver [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id)

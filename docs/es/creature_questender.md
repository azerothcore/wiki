# creature\_questender

[<-Volver a:World](database-world)

**Tabla \`creature\_questender\`**

Holds NPC quest ender relations on which NPCs finishes which quests.

**Table Structure**

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

El ID de la misión que la criatura completa. Ver [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id)

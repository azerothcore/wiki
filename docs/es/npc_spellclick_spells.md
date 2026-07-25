# npc\_spellclick\_spells

[<-Volver a: World](database-world)

**Tabla \`npc\_spellclick\_spells\`**

Esta tabla contiene información sobre los hechizos a lanzar al recibir CMSG\_SPELLCLICK.

Ese opcode se envía para misiones en las que tienes que saquear criaturas que ya están muertas al aparecer. Ejemplos son [Planning for the Future](http://www.wowhead.com/quest=11960) y [Rifle the bodies](http://www.wowhead.com/quest=11999).

**Estructura**

| Field           | Type     | Attributes | Key | Null | Default | Extra | Comment                                                                 |
| --------------- | -------- | ---------- | --- | ---- | ------- | ----- | ----------------------------------------------------------------------- |
| [npc_entry][1]  | INT      | UNSIGNED   | PRI | NO   | NULL    |       | Reference to the creature_template table                                |
| [spell_id][2]   | INT      | UNSIGNED   | PRI | NO   | NULL    |       | The ID of the spell to be cast                                          |
| [cast_flags][3] | TINYINT  | UNSIGNED   |     | NO   | NULL    |       | Who casts the spell on who, creature <=> player (values: 0-3)           |
| [user_type][4]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       | Relation with summoner: 0-no 1-friendly 2-raid 3-party player can click |

[1]: #npc_entry
[2]: #spell_id
[3]: #cast_flags
[4]: #user_type

**Descripción de los campos**

### npc\_entry

Referencia a creature\_template.entry

### spell\_id

El hechizo que debe lanzarse.

Ten en cuenta que para varias misiones hay más de un hechizo por click.

[Planing for the Future](http://www.wowhead.com/quest=11960) por ejemplo tiene [Planning for the Future: Create Snowfall Glade Pup](http://www.wowhead.com/spell=46773) que creará el objeto en el inventario del jugador
y [Planning for the Future: Create Snowfall Glade Pup Cover](http://www.wowhead.com/spell=46167) que hace desaparecer a la criatura.

Esto crea la ilusión de que la criatura ha sido saqueada.

### cast\_flags

En cada evento de spellclick, "participan" un jugador y una criatura. Este campo define quién lanza el hechizo sobre quién.
El bit inferior define al lanzador: 1=el que hace click (Clicker), 0=sobre el que se hace click (Clickee); el bit superior define el objetivo, con el mismo mapeo que el bit del lanzador.
Puedes usar esta tabla para el valor real:

| Caster   | Target  | cast\_flags value |
| -------- | ------- | ----------------- |
| Creature | Clickee | 0                 |
| Clicker  | Clickee | 1                 |
| Clickee  | Clicker | 2                 |
| Clicker  | Clicker | 3                 |

### user\_type

Relación con el invocador: define quién puede usar este spellclick.

| Value | Description |
| ----- | ----------- |
| 0     | Only self   |
| 1     | Friendly    |
| 2     | Raid        |
| 3     | Party       |

# spell\_group

[<-Volver a: World](database-world)

**Tabla \`spell\_group\`**

Tabla usada para agrupar hechizos para varias comprobaciones en el core. Un hechizo puede añadirse a muchos grupos, pero solo puede aparecer una vez en cada grupo.

| Field             | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]           | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [spell_id][2]     | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [special_flag][3] | INT  | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #id
[2]: #spell_id
[3]: #special_flag

**Descripción de los campos**

### id

Identificador de grupo
Reglas de asignación de id:

-   si el grupo se va a usar en el código del core, usa la primera entrada disponible por debajo de 1000 y añade el valor enum al enum SpellGroup en SpellMgr.h
-   si el grupo no se va a usar en el código del core, usa la entrada disponible más baja superior a 1000

### spell\_id

SpellId de Spell.dbc o id de spell\_group prefijado con "-". Si el hechizo se añade a spell\_ranks, spell\_id tiene que ser el primer rango de ese hechizo.

### special\_flag

Enum SpellGroupSpecialFlags en el core:

| Flag | Hex    | Name                                                     | Comment                                                                                   |
| ---- | ------ | -------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 0    | 0x000  | SPELL\_GROUP\_SPECIAL\_FLAG\_NONE                        |                                                                                           |
| 1    | 0x001  | SPELL\_GROUP\_SPECIAL\_FLAG\_ELIXIR\_BATTLE              |                                                                                           |
| 2    | 0x002  | SPELL\_GROUP\_SPECIAL\_FLAG\_ELIXIR\_GUARDIAN            |                                                                                           |
| 3    | 0x003  | SPELL\_GROUP\_SPECIAL\_FLAG\_FLASK                       | SPELL\_GROUP\_SPECIAL\_FLAG\_ELIXIR\_BATTLE SPELL\_GROUP\_SPECIAL\_FLAG\_ELIXIR\_GUARDIAN |
| 4    | 0x004  | SPELL\_GROUP\_SPECIAL\_FLAG\_ELIXIR\_UNSTABLE            |                                                                                           |
| 8    | 0x008  | SPELL\_GROUP\_SPECIAL\_FLAG\_ELIXIR\_SHATTRATH           |                                                                                           |
| 15   | 0x00F  | SPELL\_GROUP\_SPECIAL\_FLAG\_STACK\_EXCLUSIVE\_MAX       |                                                                                           |
| 16   | 0x010  | SPELL\_GROUP\_SPECIAL\_FLAG\_FORCED\_STRONGEST           | Flag útil si algunos hechizos tienen auras diferentes, pero solo una debe estar presente  |
| 32   | 0x020  | SPELL\_GROUP\_SPECIAL\_FLAG\_SKIP\_STRONGER\_CHECK       |                                                                                           |
| 64   | 0x040  | SPELL\_GROUP\_SPECIAL\_FLAG\_BASE\_AMOUNT\_CHECK         |                                                                                           |
| 256  | 0x100  | SPELL\_GROUP\_SPECIAL\_FLAG\_PRIORITY1                   |                                                                                           |
| 512  | 0x200  | SPELL\_GROUP\_SPECIAL\_FLAG\_PRIORITY2                   |                                                                                           |
| 1024 | 0x400  | SPELL\_GROUP\_SPECIAL\_FLAG\_PRIORITY3                   |                                                                                           |
| 2048 | 0x800  | SPELL\_GROUP\_SPECIAL\_FLAG\_PRIORITY4                   |                                                                                           |
| 4096 | 0x1000 | SPELL\_GROUP\_SPECIAL\_FLAG\_SAME\_SPELL\_CHECK          |                                                                                           |
| 8192 | 0x2000 | SPELL\_GROUP\_SPECIAL\_FLAG\_SKIP\_STRONGER\_SAME\_SPELL |                                                                                           |

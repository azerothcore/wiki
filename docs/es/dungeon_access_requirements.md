# dungeon\_access\_requirements

[<-Volver a:World](database-world)

**Tabla \`dungeon\_access\_requirements\`**

**Estructura**

| Field                  | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [dungeon_access_id][1] | TINYINT      | UNSIGNED   | PRI | NO   |         |       |         |
| [requirement_type][2]  | TINYINT      | UNSIGNED   | PRI | NO   |         |       |         |
| [requirement_id][3]    | MEDIUMINT    | UNSIGNED   | PRI | NO   |         |       |         |
| [requirement_note][4]  | VARCHAR(255) |            |     | YES  | NULL    |       |         |
| [faction][5]           | TINYINT      | UNSIGNED   |     | NO   | 2       |       |         |
| [priority][6]          | TINYINT      | UNSIGNED   |     | YES  | NULL    |       |         |
| [leader_only][7]       | TINYINT      | SIGNED     |     | NO   | 0       |       |         |
| [comment][8]           | VARCHAR(255) |            |     | YES  | NULL    |       |         |

[1]: #dungeon_access_id
[2]: #requirement_type
[3]: #requirement_id
[4]: #requirement_note
[5]: #faction
[6]: #priority
[7]: #leader_only
[8]: #comment

**Descripción de los campos**

### dungeon_access_id

ID de [dungeon_access_template.id](dungeon_access_template#id).

### requirement_type

| Value | Type        | Comment                         |
| :---- | :---------- | :------------------------------ |
| 0     | Achievement |                                 |
| 1     | Quest       |                                 |
| 2     | Item        | El item no puede estar en el banco. |

### requirement_id

ID del logro (Achievement), quest o item según el [requirement_type][2] elegido.

### requirement_note

El texto que se muestra si intentas entrar en la instancia sin cumplir los requisitos.

### faction

| Value | Comment  |
| :---- | :------- |
| 0     | Alliance |
| 1     | Horde    |
| 2     | Both     |

### priority

Orden de prioridad del requisito, ordenado por tipo. 0 es la prioridad más alta.

### leader_only

0 = Comprobar el requisito para cada jugador que intente entrar.

1 = Comprobar el requisito solo para el líder del grupo.

### comment

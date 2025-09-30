# dungeon\_access\_requirements

[<-Volver a:World](database-world)

**Tabla \`dungeon\_access\_requirements\`**

**Estructura**

| Campo                  | Tipo         | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| ---------------------- | ------------ | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [dungeon_access_id][1] | TINYINT      | UNSIGNED  | PRI   | NO   |             |       |            |
| [requirement_type][2]  | TINYINT      | UNSIGNED  | PRI   | NO   |             |       |            |
| [requirement_id][3]    | MEDIUMINT    | UNSIGNED  | PRI   | NO   |             |       |            |
| [requirement_note][4]  | VARCHAR(255) |           |       | Si   | NULL        |       |            |
| [faction][5]           | TINYINT      | UNSIGNED  |       | NO   | 2           |       |            |
| [priority][6]          | TINYINT      | UNSIGNED  |       | Si   | NULL        |       |            |
| [leader_only][7]       | TINYINT      | SIGNED    |       | NO   | 0           |       |            |
| [comment][8]           | VARCHAR(255) |           |       | Si   | NULL        |       |            |

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

Identificación de [dungeon_access_template.id](dungeon_access_template#id).

### requirement_type

| Valor | Tipo        | Comentario                              |
| ----- | ----------- | --------------------------------------- |
| 0     | Logro       |                                         |
| 1     | Búsqueda    |                                         |
| 2     | Artículo    | El artículo no puede estar en el banco. |

### requirement_id

ID para logro, misión o artículo según el [requirement_type] elegido [2].

### requirement_note

El texto que se muestra si intenta ingresar a la instancia sin cumplir con los requisitos.

### faction

| Valor | Comment  |
| ----- | -------- |
| 0     | Alliance |
| 1     | Horde    |
| 2     | Both     |

### priority

Orden de prioridad del requisito, ordenado por tipo. 0 es la prioridad más alta.

### leader_only

0 = Consulte los requisitos para cada jugador que intente ingresar.

1 = Solo verifique el requisito para el líder del grupo.

### comment

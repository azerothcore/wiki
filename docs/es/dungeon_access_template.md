# dungeon\_access\_template

[<-Volver a:World](database-world)

**Tabla \`dungeon\_access\_template\`**

**Estructura**

| Field                   | Type         | Attributes | Key | Null | Default        | Extra                                         | Comment |
| ----------------------- | ------------ | ---------- | --- | ---- | -------------- | --------------------------------------------- | ------- |
| [id][1]                 | TINYINT      | UNSIGNED   | PRI | NO   | AUTO_INCREMENT |                                               |         |
| [map_id][2]             | MEDIUMINT    | UNSIGNED   | KEY | NO   |                | FK_dungeon_access_template__instance_template |         |
| [difficulty][3]         | TINYINT      | UNSIGNED   |     | NO   | 0              |                                               |         |
| [min_level][4]          | TINYINT      | UNSIGNED   |     | YES  | NULL           |                                               |         |
| [max_level][5]          | TINYINT      | UNSIGNED   |     | YES  | NULL           |                                               |         |
| [min_avg_item_level][6] | SMALLINT     | UNSIGNED   |     | YES  | NULL           |                                               |         |
| [comment][7]            | VARCHAR(255) |            |     | YES  | NULL           |                                               |         |

[1]: #id
[2]: #map_id
[3]: #difficulty
[4]: #min_level
[5]: #max_level
[6]: #min_avg_item_level
[7]: #comment

**Descripción de los campos**

### id

El ID de la plantilla de mazmorra

### map_id

ID del mapa de [instance_template.map](instance_template#map).

### difficulty

- 5 jugadores: 0 = normal, 1 = heroico, 2 = épico (Mítico, no implementado en 3.3.5) 

- 10 jugadores: 0 = normal, 2 = heroico 

- 25 jugadores: 1 = normal, 3 = heroico

### min_level

El nivel mínimo que debes tener para entrar en la instancia.

### max_level

El nivel máximo que puedes tener para entrar en la instancia.

### min_avg_item_level

El ilvl medio mínimo requerido para entrar en la instancia.

- Todas las heroicas de WotLK requieren al menos un nivel de objeto medio de 180.

- La Prueba del Campeón, el Foso de Saron y la Fragua de las Almas requieren un nivel de objeto medio de 200.

- Las Cámaras del Reflejo requieren un nivel de objeto medio de 219.

**Nota:** este requisito solo se aplica al Buscador de Mazmorras y al Explorador de Bandas, no a un portal de mazmorra/banda (y es blizzlike). Esto también significa que una hermandad podría intentar limpiar una banda estando mal equipada :)

### comment

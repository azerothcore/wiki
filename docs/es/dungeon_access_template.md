# dungeon\_access\_template

[<-Volver a:World](database-world)

**Tabla \`dungeon\_access\_template\`**

**Estructura**

| Campo                   | Tipo         | Atributos | Llave | Nulo | Por defecto    | Extra                                         | Comentario |
| ----------------------- | ------------ | --------- | ----- | ---- | -------------- | --------------------------------------------- | ---------- |
| [id][1]                 | TINYINT      | UNSIGNED  | PRI   | NO   | AUTO_INCREMENT |                                               |            |
| [map_id][2]             | MEDIUMINT    | UNSIGNED  | KEY   | NO   |                | FK_dungeon_access_template__instance_template |            |
| [difficulty][3]         | TINYINT      | UNSIGNED  |       | NO   | 0              |                                               |            |
| [min_level][4]          | TINYINT      | UNSIGNED  |       | Si   | NULL           |                                               |            |
| [max_level][5]          | TINYINT      | UNSIGNED  |       | Si   | NULL           |                                               |            |
| [min_avg_item_level][6] | SMALLINT     | UNSIGNED  |       | Si   | NULL           |                                               |            |
| [comment][7]            | VARCHAR(255) |           |       | Si   | NULL           |                                               |            |

[1]: #id
[2]: #map_id
[3]: #difficulty
[4]: #min_level
[5]: #max_level
[6]: #min_avg_item_level
[7]: #comment

**Descripción de los campos**

### id

ID de la plantilla de mazmorra

### map_id

ID del mapa de [instance_template.map](instance_template#map).

### difficulty

- 5 man: 0 = normal, 1 = heroic, 2 = epic (Mythic, no implementado en 3.3.5) 

- 10 man: 0 = normal, 2 = heroic 

- 25 man: 1 = normal, 3 = heroic

### min_level

El nivel mínimo que debes tener para ingresar a la instancia.

### max_level

El nivel máximo que puedes tener para ingresar a la instancia.

### min_avg_item_level

Nivel de objeto promedio mínimo requerido para ingresar a la instancia.

- Todas las heroicas de WotLK requieren al menos un nivel de objeto promedio de 180.

- La Prueba del Campeón, el Pozo de Saron y la Forja de Almas requieren un nivel de objeto promedio de 200.

- Salones de reflexión requiere un nivel de objeto promedio de 219.

**Nota:** Este requisito solo aplica al Buscador de Mazmorras y al Navegador de Bandas, no a un portal de mazmorras/bandas (y es similar a Blizzard). Esto también significa que una hermandad podría intentar completar una banda con equipo insuficiente. :)

### comment

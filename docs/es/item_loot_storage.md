# item\_loot_\storage

[<-Volver a: Characters](database-characters)

**Tabla \`item\_loot_\storage\`**

**Estructura**

| Field                   | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [containerGUID][1]      | INT     | UNSIGNED   |     | NO   |         |       |         |
| [itemid][2]             | INT     | UNSIGNED   |     | NO   |         |       |         |
| [count][3]              | INT     | UNSIGNED   |     | NO   |         |       |         |
| [randomPropertyId][4]   | INT     | SIGNED     |     | NO   |         |       |         |
| [randomSuffix][5]       | INT     | UNSIGNED   |     | NO   |         |       |         |
| [follow_loot_rules][6]  | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [freeforall][7]         | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [is_blocked][8]         | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [is_counted][9]         | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [is_underthreshold][10] | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [needs_quest][11]       | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [conditionLootId][12]   | INT     | SIGNED     |     | NO   | 0       |       |         |

[1]: #containerguid
[2]: #itemid
[3]: #count
[4]: #randompropertyid
[5]: #randomsuffix
[6]: #followlootrules
[7]: #freeforall
[8]: #isblocked
[9]: #iscounted
[10]: #isunderthreshold
[11]: #needsquest
[12]: #conditionlootid

**Descripción de los Campos**

### containerGUID

`campo-sin-descripción|1` (GUID o Identificador Global Único del contenedor en cuestión)

### itemid

`campo-sin-descripción|2` (¿ID del Item? Se desconoce si la ID se extrae de item_instance o item_template (posiblemente de item_instance))

### count

`campo-sin-descripción|3` (Posiblemente la cantidad de los mismos)

### randomPropertyId

`campo-sin-descripción|4` (¿Aquella ID de alguna propiedad aleatoria para Item?)

### randomSuffix

`campo-sin-descripción|5` (¿Sufijo aleatorio?)

### follow\_loot\_rules

`campo-sin-descripción|6` (Posiblemente ligado a las reglas de loot para despojar el Item)

### freeforall

`campo-sin-descripción|7` (¿Despojo libre del Item?)

### is\_blocked

`campo-sin-descripción|8` (¿Está bloqueado?)

### is\_counted

`campo-sin-descripción|9` (¿Está contado?)

### is\_underthreshold

`campo-sin-descripción|10` (¿Se encuentra bajo un límite o umbral?)

### needs\_quest

`campo-sin-descripción|11` (¿Necesita una misión para ser despojado?)

### conditionLootId

`campo-sin-descripción|12` (¿ID de las condiciones de despojo?)

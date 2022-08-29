# item\_loot_\storage

[<-Volver a:Characters](database-characters.md)

**Tabla \`item\_loot_\storage\`**

Aparentemente esta tabla "almacena el botín de Items" que serán despojados.

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

`field-no-description|1` (GUID o Identificador Global Único del contenedor en cuestión)

### itemid

`field-no-description|2` (¿ID del Item? Se desconoce si la ID se extrae de item_instance o item_template (posiblemente de item_instance))

### count

`field-no-description|3` (Posiblemente la cantidad de los mismos)

### randomPropertyId

`field-no-description|4` (¿Aquella ID de alguna propiedad aleatoria para Item?)

### randomSuffix

`field-no-description|5` (¿Sufijo aleatorio?)

### follow\_loot\_rules

`field-no-description|6` (Posiblemente ligado a las reglas de loot para despojar el Item)

### freeforall

`field-no-description|7` (¿Despojo libre del Item?)

### is\_blocked

`field-no-description|8` (¿Está bloqueado?)

### is\_counted

`field-no-description|9` (¿Está contado?)

### is\_underthreshold

`field-no-description|10` (¿Se encuentra bajo un límite o umbral?)

### needs\_quest

`field-no-description|11` (¿Necesita una misión para ser despojado?)

### conditionLootId

`field-no-description|12` (¿ID de las condiciones de despojo?)

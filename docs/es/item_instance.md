# item\_instance

[<-Volver a:Characters](database-characters.md)

**Tabla \`item\_instance\`**

La tabla alberga información de instancias de Items individuales para todos los objetos actualmente equipados en algún tipo de bolsa o banco de personaje, en casas de subastas, en bancos de gremio o en correos.

**Estructura**

| Field                  | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]              | INT       | UNSIGNED   | PRI | NO   | 0       |       |         |
| [itemEntry][2]         | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [owner_guid][3]        | INT       | UNSIGNED   |     | NO   | 0       |       |         |
| [creatorGuid][4]       | INT       | UNSIGNED   |     | NO   | 0       |       |         |
| [giftCreatorGuid][5]   | INT       | UNSIGNED   |     | NO   | 0       |       |         |
| [count][6]             | INT       | UNSIGNED   |     | NO   | 1       |       |         |
| [duration][7]          | INT       | SIGNED     |     | NO   | 0       |       |         |
| [charges][8]           | TINYTEXT  | SIGNED     |     | YES  |         |       |         |
| [flags][9]             | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [enchantments][10]     | TEXT      | SIGNED     |     | NO   |         |       |         |
| [randomPropertyId][11] | SMALLINT  | SIGNED     |     | NO   | 0       |       |         |
| [durability][12]       | SMALLINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [playedTime][13]       | INT       | UNSIGNED   |     | NO   | 0       |       |         |
| [text][14]             | TEXT      | SIGNED     |     | YES  |         |       |         |

[1]: #guid
[2]: #itementry
[3]: #ownerguid
[4]: #creatorguid
[5]: #giftcreatorguid
[6]: #count
[7]: #duration
[8]: #charges
[9]: #flags
[10]: #enchantments
[11]: #randompropertyid
[12]: #durability
[13]: #playedtime
[14]: #text

**Descripción de los Campos**

### guid

GUID del Item. Éste número es único para cada instancia del Item.

### itemEntry

[Item_template.entry](item_template#entry).

### owner\_guid

GUID del personaje quien posée este Item. Véase [characters.guid](characters#guid).

### creatorGuid

[Characters.guid](characters#guid) del personaje que creó el item.

### giftCreatorGuid

[Characters.guid](characters#guid) del personaje quien creó el [item](character_gifts#item_guid).

### count

Número actual de copias del Item en la casilla.

### duration

`field-no-description|6` (¿Duración del Item?(si tiene))

### charges

El número de cargas para cada una de las cinco posibles cargas del hechizo en un Item, especificado a través de cinco enteros separados por espacios.

### flags

`field-no-description|8` (¿Marcadores del Item?(si tiene))

### enchantments

Encantamientos desde SpellItemEnchantment.dbc. Véase [item_instance_enchantments](item_instance_enchantments.md)

### randomPropertyId

`field-no-description|10` (propiedad aleatoria(si está encantado))

### durability

Durabilidad actual del item.

### playedTime

Tiempo medido en segundos.

### text

El texto contenido en este Item.

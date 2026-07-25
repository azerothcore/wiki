# loot_template

[<-Volver a: World](database-world)

**Las tablas \*_loot_template**

**Estructura**

| Field                           | Type         | Attributes | Key | Null | Default | Extra | Comment                       |
| ------------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ----------------------------- |
| [Entry](#entry)                 | INT          | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [Item](#item)                   | INT          | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [Reference](#reference)         | INT          |            |     | NO   | 0       |       |                               |
| [Chance](#chance)               | FLOAT        |            |     | NO   | 0       |       |                               |
| [QuestRequired](#questrequired) | TINYINT      |            |     | NO   | 0       |       |                               |
| [LootMode](#lootmode)           | SMALLINT     | UNSIGNED   |     | NO   | 1       |       |                               |
| [GroupId](#groupid)             | TINYINT      | UNSIGNED   |     | NO   | 0       |       | PRI in creature_loot_template |
| [MinCount](#mincount)           | TINYINT      | UNSIGNED   |     | NO   | 1       |       |                               |
| [MaxCount](#maxcount)           | TINYINT      | UNSIGNED   |     | NO   | 1       |       |                               |
| [Comment](#comment)             | VARCHAR(255) |            |     | YES  | NULL    |       | TEXT in player_loot_template  |

**Descripción de los campos**

### Entry

| Table                     | Entry                                                                | Comment                                                                                   |
| ------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| creature_loot_template    | [creature_template.lootid](creature_template#lootid)                 | Usually the same as [creature_template.entry](creature_template#entry)                    |
| disenchant_loot_template  | [item_template.DisenchantID](item_template#disenchantid)             |                                                                                           |
| fishing_loot_template     | area id                                                              |                                                                                           |
| gameobject_loot_template  | [gameobject_template.data1](gameobject_template#data023)             | Need to have gamobject type GAMEOBJECT_TYPE_CHEST (3) or GAMEOBJECT_TYPE_FISHINGHOLE (25) |
| item_loot_template        | [item_template.entry](item_template#entry)                           |                                                                                           |
| mail_loot_template        | mail template id                                                     |                                                                                           |
| milling_loot_template     | [item_template.entry](item_template#entry)                           |                                                                                           |
| pickpocket_loot_template  | [creature_template.pickpocketloot](creature_template#pickpocketloot) |                                                                                           |
| player_loot_template      | TeamID (0 Horde/1 Alliance)                                          | Only drops in BGs as insignia removal.                                                    |
| prospecting_loot_template | [item_template.entry](item_template#entry)                           |                                                                                           |
| reference_loot_template   | [\*_loot_template.reference](loot_template#reference)                |                                                                                           |
| skinning_loot_template    | [creature_template.skinloot](creature_template#skinloot)             | Also includes minable/herbable loot from creatures                                        |
| spell_loot_template       | SpellID                                                              |                                                                                           |

### Item

[item_template.entry](item_template#entry)

### Reference

[reference_loot_template.entry](loot_template#entry).

Usa las entradas de la plantilla referenciada en la plantilla actual.

**Nota: nunca se permite la autorreferencia. Esto provocará un crash.**

### Chance

Probabilidad de que caiga el loot. La probabilidad nunca puede superar un total de 100 para todas las entradas con el mismo [GroupID](#groupid).

Si el campo se deja en 0, la probabilidad será uniforme entre todas las entradas con el mismo [GroupID](#groupid) y chance = 0.

### QuestRequired

0 - El loot siempre está disponible.

1 - El loot solo puede caer si el jugador tiene una quest con el item id especificado en [quest_template.RequiredItemId1-6](quest_template#requireditemid1).

### LootMode

Máscara de bits.

Se usa para separar el loot condicional. Como el loot del Hardmode en Ulduar. El core puede cambiar el/los lootmode(s) activo(s) en cualquier momento.

En la mayoría de los casos este campo se deja en 1.

### GroupId

Se usa para agrupar items dentro de la misma plantilla de loot.

- Solo puede caer un item del grupo.
- Si la [chance](#chance) total del grupo es 100, entonces siempre caerá un item.
- Si la [chance](#chance) total del grupo es menor que 100, entonces existe el riesgo de un loot vacío.

El loot referenciado puede formar parte de un grupo, igual que los items. Cuando una referencia está agrupada, compite con las demás entradas de ese grupo, y solo se seleccionará una entrada (item o referencia). Si la referencia gana la tirada, se procesa toda la plantilla referenciada.

**Nota: el cliente solo puede mostrar 16 items en las ventanas de loot, incluido el oro. Por tanto, no se recomienda usar más de 16 grupos.**

### MinCount

Cantidad mínima de un item que puede caer en un solo loot. No puede ser 0.

### MaxCount

| Table                    | Comment                                                                                                                                                                                                                                 |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \*_loot_template         | Maximum amount of an item to drop in a single loot.                                                                                                                                                                                     |
| referenced_loot_template | How many times a referenced loot template should be processed. **Note: The core only rolls chance per loot definition once. If the initial reference roll was lost, it will skip the current loot completely, regardless of MaxCount.** |

### Comment

Comentario

# disables

[<-Volver a: World](database-world)

**Tabla \`disables\`**

Esta tabla se usa para deshabilitar dungeons/bgs/hechizos/etc.

**Estructura**

| Field           | Type         | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [sourceType][1] | INT          | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [entry][2]      | INT          | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [flags][3]      | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [params_0][4]   | VARCHAR(255) |            |     | NO   |         |       |         |
| [params_1][5]   | VARCHAR(255) |            |     | NO   |         |       |         |
| [comment][6]    | VARCHAR(255) |            |     | NO   |         |       |         |

[1]: #sourcetype
[2]: #entry
[3]: #flags
[4]: #params_0
[5]: #params_1
[6]: #comment

**Descripción de los campos**

### sourceType

| Value | Type                              |
| ----- | --------------------------------- |
| 0     | DISABLE_TYPE_SPELL                |
| 1     | DISABLE_TYPE_QUEST                |
| 2     | DISABLE_TYPE_MAP                  |
| 3     | DISABLE_TYPE_BATTLEGROUND         |
| 4     | DISABLE_TYPE_ACHIEVEMENT_CRITERIA |
| 5     | DISABLE_TYPE_OUTDOORPVP           |
| 6     | DISABLE_TYPE_VMAP                 |
| 7     | DISABLE_TYPE_MMAP                 |
| 8     | DISABLE_TYPE_LFG_MAP              |
| 9     | DISABLE_TYPE_GAME_EVENT           |
| 10    | DISABLE_TYPE_LOOT                 |

### entry

Entry de Spell/Quest/Map/BG/Achievement/Map/GameEvent/Item.

***Si sourceType = DISABLE_TYPE_SPELL:***

Entry de Spell

***Si sourceType = DISABLE_TYPE_QUEST:***

[quest_template.id](quest_template#id)

***Si sourceType = DISABLE_TYPE_MAP:***

***Si sourceType = DISABLE_TYPE_VMAP:***

***Si sourceType = DISABLE_TYPE_MMAP:***

***Si sourceType = DISABLE_TYPE_OUTDOORPVP:***

***Si sourceType = DISABLE_TYPE_LFG_MAP:***

Entry de Map

***Si sourceType = DISABLE_TYPE_ACHIEVEMENT_CRITERIA:***

Entry de Achievement

***Si sourceType = DISABLE_TYPE_GAME_EVENT:***

[game_event.eventEntry](game_event#evententry)

***Si sourceType = DISABLE_TYPE_LOOT:***

[item_template.entry](item_template#entry)

### flags

Si sourceType = DISABLE_TYPE_SPELL: especifica para quién está deshabilitado el hechizo.

| Value | Type                                                                                          |
| ----- | --------------------------------------------------------------------------------------------- |
| 0     | Spell enabled                                                                                 |
| 1     | Spell disabled for players                                                                    |
| 2     | Spell disabled for creatures                                                                  |
| 4     | Spell disabled for pets                                                                       |
| 8     | Spell completely disabled (used for no logner existing spells in DBCs)                        |
| 16    | Spell disabled for MapId                                                                      |
| 32    | Spell disabled for AreaId                                                                     |
| 64    | Line of Sight (LOS) is disabled for this spell (replaces "vmap.ignoreSpellIds" config option) |

Ejemplo: INSERT INTO \`disables\` VALUES (0, 8921, (1+16+32), "571,1", "1519", "Moonfire Example");

Esto deshabilitará el hechizo Moonfire (8921) para los jugadores en los mapas 571,1 y el área 1519.

***Si sourceType = DISABLE_TYPE_MAP:***

Especifica qué tipo de mapa está deshabilitado (5man/10man/heroic/etc).

| Value | Type                                                        |
| ----- | ----------------------------------------------------------- |
| 1     | DUNGEON_STATUS_FLAG_NORMAL OR RAID_STATUS_FLAG_10MAN_NORMAL |
| 2     | DUNGEON_STATUS_FLAG_HEROIC OR RAID_STATUS_FLAG_25MAN_NORMAL |
| 4     | RAID_STATUS_FLAG_10MAN_HEROIC                               |
| 8     | RAID_STATUS_FLAG_25MAN_HEROIC                               |

El valor es una máscara de bits de los modos VÁLIDOS para el mapa específico; 15 NO es, por tanto, una máscara válida en ciertos mapas, solo aquellos realmente posibles para el mapa respectivo.

***Si sourceType = DISABLE_TYPE_VMAP:***

Especifica en qué mapa debe deshabilitarse el vMap

| Value | Type                  |
| ----- | --------------------- |
| 1     | VMAP_DISABLE_AREAFLAG |
| 2     | VMAP_DISABLE_HEIGHT   |
| 4     | VMAP_DISABLE_LOS      |
| 8     | VMAP_LIQUIDSTATUS     |

Ejemplo: INSERT INTO \`disables\` VALUES (6, 1, (2 + 4), 0, 0, "Disable Kalimdor vMaps");

Esto deshabilitará los vMaps en todo Kalimdor.

***Si sourceType = DISABLE_TYPE_QUEST:***

***Si sourceType = DISABLE_TYPE_ACHIEVEMENT_CRITERIA:***

***Si sourceType = DISABLE_TYPE_OUTDOORPVP:***

***Si sourceType = DISABLE_TYPE_MMAP:***

***Si sourceType = DISABLE_TYPE_LFG_MAP:***

***Si sourceType = DISABLE_TYPE_GAME_EVENT:***

***Si sourceType = DISABLE_TYPE_LOOT:***

No se necesitan flags, solo añade el entry a la tabla con \`flags\`=0.

### params_0

MapId si se usa DISABLE_TYPE_SPELL, 0 para todos los mapas.

### params_1

AreaId si se usa DISABLE_TYPE_SPELL, 0 para todas las áreas.

### comment

Un comentario sobre por qué se deshabilitó algo, o cualquier otro texto que quieras.

# disables

[<-Back-to:World](database-world)

**The \`disables\` table**

This table is used to disable dungeons/bgs/spells/etc.

**Table: disables's Structure**

| Field                     | Type         |          | Null | Key | Default | Extra | Comment |
| :------------------------ | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [sourceType](#sourcetype) | INT          | UNSIGNED | NO   | PRI |         |       |         |
| [entry](#entry)           | INT          | UNSIGNED | NO   | PRI |         |       |         |
| [flags](#flags)           | TINYINT      | UNSIGNED | NO   |     | 0       |       |         |
| [params_0](#params0)      | VARCHAR(255) |          | NO   |     | ''      |       |         |
| [params_1](#params1)      | VARCHAR(255) |          | NO   |     | ''      |       |         |
| [comment](#comment)       | VARCHAR(255) |          | NO   |     | ''      |       |         |

**Description of the table's fields**

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

Entry of Spell/Quest/Map/BG/Achievement/Map/GameEvent/Item.

***If sourceType = DISABLE_TYPE_SPELL:***

Entry of Spell

***If sourceType = DISABLE_TYPE_QUEST:***

[quest_template.id](quest_template#id)

***If sourceType = DISABLE_TYPE_MAP:***

***If sourceType = DISABLE_TYPE_VMAP:***

***If sourceType = DISABLE_TYPE_MMAP:***

***If sourceType = DISABLE_TYPE_OUTDOORPVP:***

***If sourceType = DISABLE_TYPE_LFG_MAP:***

Entry of Map

***If sourceType = DISABLE_TYPE_ACHIEVEMENT_CRITERIA:***

Entry of Achievement

***If sourceType = DISABLE_TYPE_GAME_EVENT:***

[game_event.eventEntry](game_event#evententry)

***If sourceType = DISABLE_TYPE_LOOT:***

[item_template.entry](item_template#entry)

### flags

If sourceType = DISABLE_TYPE_SPELL: Specifies who the spell is disabled for.

| Value | Hex    | Flag | Comment                                                                                       |
| :---- | :----: | :--- | :-------------------------------------------------------------------------------------------- |
| 0     | `0x00` |      | Spell enabled                                                                                 |
| 1     | `0x01` |      | Spell disabled for players                                                                    |
| 2     | `0x02` |      | Spell disabled for creatures                                                                  |
| 4     | `0x04` |      | Spell disabled for pets                                                                       |
| 8     | `0x08` |      | Spell completely disabled (used for no logner existing spells in DBCs)                        |
| 16    | `0x10` |      | Spell disabled for MapId                                                                      |
| 32    | `0x20` |      | Spell disabled for AreaId                                                                     |
| 64    | `0x40` |      | Line of Sight (LOS) is disabled for this spell (replaces "vmap.ignoreSpellIds" config option) |

Example: INSERT INTO \`disables\` VALUES (0, 8921, (1+16+32), "571,1", "1519", "Moonfire Example");

This will disable spell Moonfire (8921) for players in maps 571,1 and area 1519.

***If sourceType = DISABLE_TYPE_MAP:***

Specifies what type of map is disabled (5man/10man/heroic/etc).

| Value | Hex    | Flag | Comment                                                     |
| :---- | :----: | :--- | :---------------------------------------------------------- |
| 1     | `0x01` |      | DUNGEON_STATUS_FLAG_NORMAL OR RAID_STATUS_FLAG_10MAN_NORMAL |
| 2     | `0x02` |      | DUNGEON_STATUS_FLAG_HEROIC OR RAID_STATUS_FLAG_25MAN_NORMAL |
| 4     | `0x04` |      | RAID_STATUS_FLAG_10MAN_HEROIC                               |
| 8     | `0x08` |      | RAID_STATUS_FLAG_25MAN_HEROIC                               |

The value is a bitmask of VALID modes for the specific map, 15 is as such NOT a valid mask on certain maps, only those actually found possible for the respective map.

***If sourceType = DISABLE_TYPE_VMAP:***

Specifies on which map should be vMap disabled

| Value | Hex    | Flag                      | Comment                              |
| :---- | :----: | :------------------------ | :----------------------------------- |
| 1     | `0x01` | VMAP_DISABLE_AREAFLAG     | Area flags from vmaps are not used   |
| 2     | `0x02` | VMAP_DISABLE_HEIGHT       | Height from vmaps is not used        |
| 4     | `0x04` | VMAP_DISABLE_LOS          | Line of sight from vmaps is not used |
| 8     | `0x08` | VMAP_DISABLE_LIQUIDSTATUS | Liquid status from vmaps is not used |

Example: INSERT INTO \`disables\` VALUES (6, 1, (2 + 4), 0, 0, "Disable Kalimdor vMaps");

This will disable vMaps on whole Kalimdor.

***If sourceType = DISABLE_TYPE_QUEST:***

***If sourceType = DISABLE_TYPE_ACHIEVEMENT_CRITERIA:***

***If sourceType = DISABLE_TYPE_OUTDOORPVP:***

***If sourceType = DISABLE_TYPE_MMAP:***

***If sourceType = DISABLE_TYPE_LFG_MAP:***

***If sourceType = DISABLE_TYPE_GAME_EVENT:***

***If sourceType = DISABLE_TYPE_LOOT:***

No flags needed just add the entry to the table with \`flags\`=0.

### params_0

MapId if DISABLE_TYPE_SPELL used, 0 for all maps.

### params_1

AreaId if DISABLE_TYPE_SPELL used, 0 for all areas.

### comment

A comment as to why the something was disabled, or any other text that you want.

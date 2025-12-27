# disables

[<-Back-to:World](database-world)

**The \`disables\` table**

This table is used to disable dungeons/bgs/spells/etc.

**Table Structure**

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

**Description of the fields**

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

Example: INSERT INTO \`disables\` VALUES (0, 8921, (1+16+32), "571,1", "1519", "Moonfire Example");

This will disable spell Moonfire (8921) for players in maps 571,1 and area 1519.

***If sourceType = DISABLE_TYPE_MAP:***

Specifies what type of map is disabled (5man/10man/heroic/etc).

| Value | Type                                                        |
| ----- | ----------------------------------------------------------- |
| 1     | DUNGEON_STATUS_FLAG_NORMAL OR RAID_STATUS_FLAG_10MAN_NORMAL |
| 2     | DUNGEON_STATUS_FLAG_HEROIC OR RAID_STATUS_FLAG_25MAN_NORMAL |
| 4     | RAID_STATUS_FLAG_10MAN_HEROIC                               |
| 8     | RAID_STATUS_FLAG_25MAN_HEROIC                               |

The value is a bitmask of VALID modes for the specific map, 15 is as such NOT a valid mask on certain maps, only those actually found possible for the respective map.

***If sourceType = DISABLE_TYPE_VMAP:***

Specifies on which map should be vMap disabled

| Value | Type                  |
| ----- | --------------------- |
| 1     | VMAP_DISABLE_AREAFLAG |
| 2     | VMAP_DISABLE_HEIGHT   |
| 4     | VMAP_DISABLE_LOS      |
| 8     | VMAP_LIQUIDSTATUS     |

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

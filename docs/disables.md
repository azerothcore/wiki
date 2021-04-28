# disables

[<-Back-to:World](database-world.md)

**The \`disables\` table**

This table is used to disable dungeons/bgs/spells/etc.

**Structure**

| Field           | Type         | Attributes | Key | Null | Default | Extra | Comment |
|-----------------|--------------|------------|-----|------|---------|-------|---------|
| [sourceType][1] | int(10)      | unsigned   | PRI | NO   | NULL    |       |         |
| [entry][2]      | int(10)      | unsigned   | PRI | NO   | NULL    |       |         |
| [flags][3]      | tinyint(3)   | unsigned   |     | NO   | 0       |       |         |
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

| Value | Type                                 |
|-------|--------------------------------------|
| 0     | DISABLE\_TYPE\_SPELL                 |
| 1     | DISABLE\_TYPE\_QUEST                 |
| 2     | DISABLE\_TYPE\_MAP                   |
| 3     | DISABLE\_TYPE\_BATTLEGROUND          |
| 4     | DISABLE\_TYPE\_ACHIEVEMENT\_CRITERIA |
| 5     | DISABLE\_TYPE\_OUTDOORPVP            |
| 6     | DISABLE\_TYPE\_VMAP                  |
| 7     | DISABLE\_TYPE\_MMAP                  |
| 8     | DISABLE\_TYPE\_LFG\_MAP              |

### entry

Entry of Spell/Quest/Map/BG/Achievement/Map.

### flags

If sourceType = DISABLE\_TYPE\_SPELL: Specifies who the spell is disabled for.

| Value | Type                                                                                          |
|-------|-----------------------------------------------------------------------------------------------|
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

***If sourceType = DISABLE\_TYPE\_MAP:***

Specifies what type of map is disabled (5man/10man/heroic/etc).

| Value | Type                                                        |
|-------|-------------------------------------------------------------|
| 1     | DUNGEON_STATUS_FLAG_NORMAL OR RAID_STATUS_FLAG_10MAN_NORMAL |
| 2     | DUNGEON_STATUS_FLAG_HEROIC OR RAID_STATUS_FLAG_25MAN_NORMAL |
| 4     | RAID_STATUS_FLAG_10MAN_HEROIC                               |
| 8     | RAID_STATUS_FLAG_25MAN_HEROIC                               |

The value is a bitmask of VALID modes for the specific map, 15 is as such NOT a valid mask on certain maps, only those actually found possible for the respective map.

***If sourceType = DISABLE\_TYPE\_VMAP:***

Specifies on which map should be vMap disabled

| Value | Type                    |
|-------|-------------------------|
| 1     | VMAP\_DISABLE\_AREAFLAG |
| 2     | VMAP\_DISABLE\_HEIGHT   |
| 4     | VMAP\_DISABLE\_LOS      |
| 8     | VMAP\_LIQUIDSTATUS      |

Example: INSERT INTO \`disables\` VALUES (6, 1, (2 + 4), 0, 0, "Disable Kalimdor vMaps");

This will disable vMaps on whole Kalimdor.

***If sourceType = DISABLE\_TYPE\_QUEST:***

***If sourceType = DISABLE\_TYPE\_ACHIEVEMENT\_CRITERIA:***

***If sourceType = DISABLE\_TYPE\_OUTDOORPVP:***

***If sourceType = DISABLE\_TYPE\_MMAP:***

******If sourceType = DISABLE\_TYPE\_LFG\_MAP:***
***

No flags needed just add the entry to the table with \`flags\`=0.

### params\_0

MapId if DISABLE\_TYPE\_SPELL used, 0 for all maps.

### params\_1

AreaId if DISABLE\_TYPE\_SPELL used, 0 for all areas.

### comment

A comment as to why the something was disabled, or any other text that you want.

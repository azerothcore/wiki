# corpse

[<-Back-to:Characters](database-characters)

**The \`corpse\` table**

Holds the corpses of dead player characters that are in the world.

**Table: corpse's Structure**

| Field            | Type     | Attributes | Key | Null | Default | Extra | Comment                            |
| ---------------- | -------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [guid][1]        | INT      | UNSIGNED   | PRI | NO   | 0       |       | Character Global Unique Identifier |
| [posX][2]        | FLOAT    | SIGNED     |     | NO   | 0       |       |                                    |
| [posY][3]        | FLOAT    | SIGNED     |     | NO   | 0       |       |                                    |
| [posZ][4]        | FLOAT    | SIGNED     |     | NO   | 0       |       |                                    |
| [orientation][5] | FLOAT    | SIGNED     |     | NO   | 0       |       |                                    |
| [mapId][6]       | SMALLINT | UNSIGNED   |     | NO   | 0       |       | Map Identifier                     |
| [phaseMask][7]   | INT      | UNSIGNED   |     | NO   | 1       |       |                                    |
| [displayId][8]   | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |
| [itemCache][9]   | TEXT     |            |     | NO   |         |       |                                    |
| [bytes1][10]     | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |
| [bytes2][11]     | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |
| [guildId][12]    | INT      | UNSIGNED   |     | NO   | 0       |       |                                    |
| [flags][13]      | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                    |
| [dynFlags][14]   | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                    |
| [time][15]       | INT      | UNSIGNED   | MUL | NO   | 0       |       |                                    |
| [corpseType][16] | TINYINT  | UNSIGNED   | MUL | NO   | 0       |       |                                    |
| [instanceId][17] | INT      | UNSIGNED   | MUL | NO   | 0       |       | Instance Identifier                |

[1]: #guid
[2]: #posx
[3]: #posy
[4]: #posz
[5]: #orientation
[6]: #mapid
[7]: #phasemask
[8]: #displayid
[9]: #itemcache
[10]: #bytes1
[11]: #bytes2
[12]: #guildid
[13]: #flags
[14]: #dynflags
[15]: #time
[16]: #corpsetype
[17]: #instanceid

**Description of the table's fields**

### guid

The character guid. See [characters.guid](characters#guid).

### posX

X position of the corpse.

### posY

Y position of the corpse.

### posZ

Z position of the corpse.

### orientation

Orientation of the corpse.

### mapId

The map the corpse is on. See [Map.dbc](map).

### phaseMask

The phases the corpse is visible in.

### displayId

The character's native display ID, so the corpse looks like the character.

### itemCache

The items the character was wearing, so the corpse shows them. One value per equipment slot, separated by spaces. Each value is `displayId | (InventoryType << 24)` of the item, or 0 for an empty slot. Bones have no items.

### bytes1

Appearance of the character: `(race << 8) | (gender << 16) | (skin << 24)`.

### bytes2

Appearance of the character: `face | (hairStyle << 8) | (hairColor << 16) | (facialHair << 24)`.

### guildId

The guild of the character. See [guild.guildid](guild#guildid).

### flags

| Flag | Name                   | Description                                   |
| ---- | ---------------------- | --------------------------------------------- |
| 1    | CORPSE_FLAG_BONES      | The corpse is bones.                          |
| 2    | CORPSE_FLAG_UNK1       |                                               |
| 4    | CORPSE_FLAG_UNK2       | Set on every corpse.                          |
| 8    | CORPSE_FLAG_HIDE_HELM  | The character had their helm hidden.          |
| 16   | CORPSE_FLAG_HIDE_CLOAK | The character had their cloak hidden.         |
| 32   | CORPSE_FLAG_LOOTABLE   | Other players can loot the corpse, in battlegrounds and in Wintergrasp during battle. |

### dynFlags

1 (`CORPSE_DYNFLAG_LOOTABLE`) if the corpse can be looted right now, otherwise 0.

### time

The time the corpse was created, in Unix time.

### corpseType

| Value | Type                       | Description                                         |
| ----- | -------------------------- | --------------------------------------------------- |
| 0     | CORPSE_BONES               | Bones left after the character was resurrected.     |
| 1     | CORPSE_RESURRECTABLE_PVE   | Corpse of a character killed in PvE.                |
| 2     | CORPSE_RESURRECTABLE_PVP   | Corpse of a character killed in PvP.                |

### instanceId

The instance the corpse is in, 0 if the map is not an instance.

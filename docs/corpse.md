# corpse

[<-Back-to:Characters](database-characters)

**The \`corpse\` table**

Holds the corpses of dead player characters that are in the world.

**Table: corpse's Structure**

| Field                       | Type     |          | Null | Key | Default | Extra | Comment                            |
| :-------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :--------------------------------- |
| [guid](#guid)               | INT      | UNSIGNED | NO   | PRI | 0       |       | Character Global Unique Identifier |
| [posX](#posx)               | FLOAT    |          | NO   |     | 0       |       |                                    |
| [posY](#posy)               | FLOAT    |          | NO   |     | 0       |       |                                    |
| [posZ](#posz)               | FLOAT    |          | NO   |     | 0       |       |                                    |
| [orientation](#orientation) | FLOAT    |          | NO   |     | 0       |       |                                    |
| [mapId](#mapid)             | SMALLINT | UNSIGNED | NO   |     | 0       |       | Map Identifier                     |
| [phaseMask](#phasemask)     | INT      | UNSIGNED | NO   |     | 1       |       |                                    |
| [displayId](#displayid)     | INT      | UNSIGNED | NO   |     | 0       |       |                                    |
| [itemCache](#itemcache)     | TEXT     |          | NO   |     |         |       |                                    |
| [bytes1](#bytes1)           | INT      | UNSIGNED | NO   |     | 0       |       |                                    |
| [bytes2](#bytes2)           | INT      | UNSIGNED | NO   |     | 0       |       |                                    |
| [guildId](#guildid)         | INT      | UNSIGNED | NO   |     | 0       |       |                                    |
| [flags](#flags)             | TINYINT  | UNSIGNED | NO   |     | 0       |       |                                    |
| [dynFlags](#dynflags)       | TINYINT  | UNSIGNED | NO   |     | 0       |       |                                    |
| [time](#time)               | INT      | UNSIGNED | NO   | MUL | 0       |       |                                    |
| [corpseType](#corpsetype)   | TINYINT  | UNSIGNED | NO   | MUL | 0       |       |                                    |
| [instanceId](#instanceid)   | INT      | UNSIGNED | NO   | MUL | 0       |       | Instance Identifier                |

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

| Value | Hex    | Flag                   | Comment                                                                               |
| :---- | :----: | :--------------------- | :------------------------------------------------------------------------------------ |
| 1     | `0x01` | CORPSE_FLAG_BONES      | The corpse is bones.                                                                  |
| 2     | `0x02` | CORPSE_FLAG_UNK1       | Unknown. It has no description in AzerothCore, TrinityCore, cmangos or mangos         |
| 4     | `0x04` | CORPSE_FLAG_UNK2       | Set on every corpse.                                                                  |
| 8     | `0x08` | CORPSE_FLAG_HIDE_HELM  | The character had their helm hidden.                                                  |
| 16    | `0x10` | CORPSE_FLAG_HIDE_CLOAK | The character had their cloak hidden.                                                 |
| 32    | `0x20` | CORPSE_FLAG_LOOTABLE   | Other players can loot the corpse, in battlegrounds and in Wintergrasp during battle. |

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

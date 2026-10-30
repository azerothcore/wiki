# creature\_addon

[<-Back-to:World](database-world)

**The \`creature\_addon\` table**

The creature\_addon and creature\_template\_addon tables define different things that are applied on creatures when they are loaded. These "different things" can be for example to have the creature be mounted, to have it emote something, to have it display an aura effect, etc. Through the use of the fields in this table, many things can be changed about the outward visual appearance of the creature. The creature\_template\_addon table affects all creatures with that creature template ID while the creature\_addon table affects individually spawned creatures (so that two creatures using the same template can look different).

NOTE: A creature\_addon record will override a creature\_template\_addon record should they overlap on the same creature.

**Table: creature\_addon's Structure**

| Field                                             | Type    |          | Null | Key | Default | Extra | Comment |
| :------------------------------------------------ | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guid/entry](#guidentry)                          | INT     | UNSIGNED | NO   | PRI | 0       |       |         |
| [path_id](#pathid)                                | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [mount](#mount)                                   | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [bytes1](#bytes1)                                 | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [bytes2](#bytes2)                                 | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [emote](#emote)                                   | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [visibilityDistanceType](#visibilitydistancetype) | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [auras](#auras)                                   | TEXT    |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### guid/entry

For creature\_addon, this field signifies a unique creature guid. It will affect just that creature whose GUID matches the one specified here.
For creature\_template\_addon, this field signifies the [creature\_template.entry](creature_template#entry). It will affect all spawned creatures using that template entry.

### path\_id

If a creature has waypoint pathed movement, this field hold the waypoint\_data.id for the path the creature is to follow.

### mount

The model ID of the mount to be used to make the creature appear mounted. The value here overrides the value for the creature's unit field UNIT\_FIELD\_MOUNTDISPLAYID.

### bytes1

The value here overrides the value for the creature's unit field `UNIT_FIELD_BYTES_1`. It packs four
bytes, little-endian:

`bytes1 = standState | (petTalents << 8) | (standFlags << 16) | (animTier << 24)`

- byte 0, `& 0xFF` = stand state: standing, sitting, sleeping, kneeling, submerged
- byte 1, `<< 8` = pet talent points: unused on creatures, always 0
- byte 2, `<< 16` = stand flags: creep, untrackable
- byte 3, `<< 24` = animation tier: 0 Ground, 1 AlwaysStand (`AnimTier` calls it Swim), 2 Hover, 3 Fly, 4 Submerged

Setting a single field is one shift, so an animation tier of Fly is `3 << 24` = 50331648 and Hover is
`2 << 24` = 33554432. Fields combine with OR, for example kneeling while flying is `0x03000008` =
50331656. `0` leaves the creature standing, with no stand flags and the ground tier.

The tier only changes how the client animates the creature; walking, flying and hovering come from
the movement flags, from [creature\_template\_movement](creature_template_movement) or from a script.

Stand states, used in byte 0:

| Value | Stand state      | Notes                                                                                   |
| ----- | ---------------- | --------------------------------------------------------------------------------------- |
| 0     | Stand            |                                                                                         |
| 1     | Sit              |                                                                                         |
| 2     | Sit chair        |                                                                                         |
| 3     | Sleep            |                                                                                         |
| 4     | Sit low chair    |                                                                                         |
| 5     | Sit medium chair |                                                                                         |
| 6     | Sit high chair   |                                                                                         |
| 7     | Dead             | Shows the creature as dead. Combine with the state dead [emote](#emote) to make it look dead. |
| 8     | Kneel            |                                                                                         |
| 9     | Submerged        | Submerges the creature below the ground.                                                |

### bytes2

The value here overrides the value for the creature's unit field UNIT\_FIELD\_BYTES\_2. The core only uses the first byte, which sets how the creature holds its weapons. The other bytes are ignored.

| Value | Sheath state         | Effect                                                         |
| ----- | -------------------- | -------------------------------------------------------------- |
| 0     | SHEATH\_STATE\_UNARMED | Weapons are not drawn, they are shown on the sides or back.  |
| 1     | SHEATH\_STATE\_MELEE   | Melee weapons are drawn and held in the hands.                 |
| 2     | SHEATH\_STATE\_RANGED  | Ranged weapon is drawn, melee weapons are shown on the sides.  |

If bytes2 is 0, the creature keeps its default, which is to have its melee weapons drawn.

### emote

Emote ID that the creature should continually perform.

List of often used emote IDs and what they do can be found [here](emotes).

### visibilityDistanceType

This field controls the visibility distance for creatures:

| Value | Name     | Distance                            |
| ----- | -------- | ----------------------------------- |
| 0     | Normal   | 100 yards, the default on continents |
| 1     | Tiny     | 25 yards                            |
| 2     | Small    | 50 yards                            |
| 3     | Large    | 200 yards                           |
| 4     | Gigantic | 400 yards                           |
| 5     | Infinite | 533 yards                           |

With Normal, the creature uses the visibility distance of the map.

### auras

This field controls any auras to be applied on the creature (both in effect and visually). The value is a list of spell IDs separated by spaces. Spells that do not exist and duplicate spells are skipped, and an error is logged.

List of useful aura entries (examples):

- '16380' - Makes the creature invisible.
- '18950' - Makes the creature detect other invisible units (players or creatures).
- '16380 18950' - Both auras above

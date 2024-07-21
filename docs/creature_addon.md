# creature\_addon

[<-Back-to:World](database-world)

**The \`creature\_addon\` table**

The creature\_addon and creature\_template\_addon tables define different things that are applied on creatures when they are loaded. These "different things" can be for example to have the creature be mounted, to have it emote something, to have it display an aura effect, etc. Through the use of the fields in this table, many things can be changed about the outward visual appearance of the creature. The creature\_template\_addon table affects all creatures with that creature template ID while the creature\_addon table affects individually spawned creatures (so that two creatures using the same template can look different).

NOTE: A creature\_addon record will override a creature\_template\_addon record should they overlap on the same creature.

NOTICE: The data for this table is largely incomplete and is mostly just a regurgitation of what the client receives from the server. This article is a WIP as to what all the possible values are.

**Table Structure**

| Field                        | Type          | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------------- | ------------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid/entry][1]              | INT/MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [path_id][2]                 | INT           | UNSIGNED   |     | NO   |         |       |         |
| [mount][3]                   | MEDIUMINT     | UNSIGNED   |     | NO   |         |       |         |
| [bytes1][4]                  | INT           | UNSIGNED   |     | NO   |         |       |         |
| [bytes2][5]                  | INT           | UNSIGNED   |     | NO   |         |       |         |
| [emote][6]                   | INT           | UNSIGNED   |     | NO   |         |       |         |
| [aiAnimKit][7]               | SMALLINT      | SIGNED     |     | NO   |         |       |         |
| [movementAnimKit][8]         | SMALLINT      | SIGNED     |     | NO   |         |       |         |
| [meleeAnimKit][9]            | SMALLINT      | SIGNED     |     | NO   |         |       |         |
| [visibilityDistanceType][10] | TINYINT       | UNSIGNED   |     | NO   |         |       |         |
| [auras][11]                  | text          |            |     | YES  |         |       |         |

[1]: #guid/entry
[2]: #path_id
[3]: #mount
[4]: #bytes1
[5]: #bytes2
[6]: #emote
[7]: #aianimkit
[8]: #movementanimkit
[9]: #meleeanimkit
[10]: #visibilityDistanceType
[11]: #auras

**Description of the fields**

### guid/entry

For creature\_addon, this field signifies a unique creature guid. It will affect just that creature whose GUID matches the one specified here.
For creature\_template\_addon, this field signifies the [creature\_template.entry](creature_template#creature_template-entry). It will affect all spawned creatures using that template entry.

### path\_id

If a creature has waypoint pathed movement, this field hold the waypoint\_data.id for the path the creature is to follow.

### mount

The model ID of the mount to be used to make the creature appear mounted. The value here overrides the value for the creature's unit field UNIT\_FIELD\_MOUNTDISPLAYID.

### bytes1

The value here overrides the value for the creature's unit field UNIT\_FIELD\_BYTES\_1.

List of known values and what their visual effects on the creature

- 1 = Sitting
- 2 = Sit chair
- 3 = Sleep
- 4 = Sit low chair
- 5 = Sit medium chair
- 6 = Sit high chair
- 7 = Shows health bar as empty (combine with the state dead emote to make a creature look dead)
- 8 = Makes the mob kneel
- 9 = Submerges the creature below the ground
- 54432 = Hover mode
- 50331648 = Hover mode 2

### bytes2

The value here overrides the value for the creature's unit field UNIT\_FIELD\_BYTES\_2.

NOTE: //creatures always have melee weapon ready if any unless specified otherwise

List of few known values and what their visual effects on the creature

- 0 = STATE\_UNARMED (not prepared weapon, weapons on the sides/back)
- 1 = STATE\_MELEE (prepared melee weapon in hands)
- 2 = STATE\_RANGED (prepared ranged weapon in hands, melee weapons on the sides)

### emote

Emote ID that the creature should continually perform.

List of often used emote IDs and what they do can be found [here](Emotes).

### aiAnimKit / movementAnimKit / meleeAnimKit

AnimKit ID from AnimKit.db2 that is applied on creature when spawned.

### visibilityDistanceType

This field controls the visibility distance for creatures:

- Normal = 0,  100.0f  // default visible distance, 100 yards on continents
- Tiny = 1,  25.0f
- Small = 2,  50.0f
- Large = 3, 200.0f
- Gigantic = 4, 400.0f
- Infinite = 5, SIZE_OF_GRIDS // max distance for visible objects)

### auras

This field controls any auras to be applied on the creature (both in effect and visually). To apply multiple auras, you can add more aura entries, separating each entry by a space. Remember that if a spell applies multiple auras.

List of useful aura entries (examples):

- '16380' - Makes the creature invisible.
- '18950' - Makes the creature detect other invisible units (players or creatures).
- '16380 18950' - Both auras above

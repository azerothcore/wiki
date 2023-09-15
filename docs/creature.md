# creature

[<-Back-to:World](database-world.md)

**Table Structure**

Contains individual creature spawn data for each individual spawn of each individual creature in the game world.

| Field                 | Type      | Attributes | Key | Null | Default | Extra          | Comment                                 |
| --------------------- | --------- | ---------- | --- | ---- | ------- | -------------- | --------------------------------------- |
| [guid][1]             | INT       | UNSIGNED   | PRI | NO   | NULL    | Auto Increment | Global Unique Identifier                |
| [id1][2]              | INT       | UNSIGNED   |     | NO   | 0       |                | Creature Identifier                     |
| [id2][3]              | INT       | UNSIGNED   |     | NO   | 0       |                | Creature Identifier                     |
| [id3][4]              | INT       | UNSIGNED   |     | NO   | 0       |                | Creature Identifier                     |
| [map][5]              | SMALLINT  | UNSIGNED   |     | NO   | 0       |                | Map Identifier                          |
| [zoneId][6]           | SMALLINT  | UNSIGNED   |     | NO   | 0       |                | Zone Identifier                         |
| [areaId][7]           | SMALLINT  | UNSIGNED   |     | NO   | 0       |                | Area Identifier                         |
| [spawnMask][8]        | TINYINT   | UNSIGNED   |     | NO   | 1       |                |                                         |
| [phaseMask][9]        | SMALLINT  | UNSIGNED   |     | NO   | 1       |                |                                         |
| [equipment_id][10]    | TINYINT   | UNSIGNED   |     | NO   | 1       |                |                                         |
| [position_x][11]      | FLOAT     | SIGNED     |     | NO   | 0       |                |                                         |
| [position_y][12]      | FLOAT     | SIGNED     |     | NO   | 0       |                |                                         |
| [position_z][13]      | FLOAT     | SIGNED     |     | NO   | 0       |                |                                         |
| [orientation][14]     | FLOAT     | SIGNED     |     | NO   | 0       |                |                                         |
| [spawntimesecs][15]   | INT       | UNSIGNED   |     | NO   | 120     |                |                                         |
| [wander_distance][16] | FLOAT     | SIGNED     |     | NO   | 5       |                | Dist in yards for random movement.      |
| [currentwaypoint][17] | INT       | UNSIGNED   |     | NO   | 0       |                | Storage used by core. "Always set as 0" |
| [curhealth][18]       | INT       | UNSIGNED   |     | NO   | 1       |                | Storage used by core. "Always set as 1" |
| [curmana][19]         | INT       | UNSIGNED   |     | NO   | 0       |                | Storage used by core. "Always set as 0" |
| [MovementType][20]    | TINYINT   | UNSIGNED   |     | NO   | 0       |                | 0 No movement, 1 random, 2 path         |
| [npcflag][21]         | INT       | UNSIGNED   |     | NO   | 0       |                | creature_template override              |
| [unit_flags][22]      | INT       | UNSIGNED   |     | NO   | 0       |                | creature_template override              |
| [dynamicflags][23]    | INT       | UNSIGNED   |     | NO   | 0       |                | creature_template override              |
| [ScriptName][24]      | CHAR      |            |     | YES  | NULL    |                |                                         |
| [VerifiedBuild][25]   | INT       | SIGNED     |     | YES  | NULL    |                | Not used by the core.                   |
| [CreateObject][26]    | TINYINT   | UNSIGNED   |     | NO   | 0       |                | Not used by the core.                   |
| [Comment][27]         | TEXT      |            |     | YES  | NULL    |                | Not used by the core.                   |

[1]: #guid
[2]: #id1
[3]: #id2
[4]: #id3
[5]: #map
[6]: #zoneId
[7]: #areaId
[8]: #spawnmask
[9]: #phasemask
[10]: #equipmentid
[11]: #positionx
[12]: #positiony
[13]: #positionz
[14]: #orientation
[15]: #spawntimesecs
[16]: #wanderdistance
[17]: #currentwaypoint
[18]: #curhealth
[19]: #curmana
[20]: #movementtype
[21]: #npcflag
[22]: #unitflags
[23]: #dynamicflags
[24]: #scriptname
[25]: #verifiedbuild
[26]: #createobject
[27]: #comment

**Field Descriptions**

### guid

A unique identifier given to each creature to distinguish one creature from another. Two creatures can NOT have same GUID.

### id1

The Main ID of the [template](creature_template#creature_template-entry) that is used when instantiating this creature.

### id2

The Secondary ID of the [template](creature_template#creature_template-entry) that is used when instantiating this creature.

### id3

The Third ID of the [template](creature_template#creature_template-entry) that is used when instantiating this creature.

### map

The ID of the [map](Map) that the creature is spawned on.

### zoneId

The ID of the zone that the creature is spawned in. (e.g. The Barrens)

This column is filled in by the worldserver on startup if the `Calculate.Creature.Zone.Area.Data` setting is enabled. It originates from AreaTable.dbc.

### areaId

The ID of the area that the creature is spawned in. You can think of an area as a "subzone" of a zone, e.g. Lushwater Oasis inside The Barrens. 

This column is filled in by the worldserver on startup if the `Calculate.Creature.Zone.Area.Data` setting is enabled. It originates from AreaTable.dbc.

### spawnMask

Controls under which difficulties the creature is spawned. The values are bit-masked, so you can add them together to combine the effects of two or more values.

Example:

4 + 8 = 12

The creature will spawn in only the 10 and 25 man heroic versions of the map that the creature is spawned on.

| Value | Comment                                                                              |
| ----- | ------------------------------------------------------------------------------------ |
| 0     | Not spawned                                                                          |
| 1     | Spawned only in 10-man-normal versions of maps (includes maps without a heroic mode) |
| 2     | Spawned only in 25-man-normal versions of maps (or heroics pre 3.2)                  |
| 4     | Spawned only in 10-man heroic versions of maps                                       |
| 8     | Spawned only in 25-man-heroic versions of maps                                       |
| 15    | Spawned in all versions of maps                                                      |

### phaseMask

This is a bit-mask field that describes all the phases that a creature will appear in. Aura 261 determines the phase you can see. For example, if you had this aura <http://www.wowhead.com/?spell=55782>, you would be able to see creatures in phase 2. If you wanted the creature to be visible in both phase 1 and phase 2, you would set the phase-mask to 3.

### equipment\_id

The ID as defined within [creature\_equip\_template](creature_equip_template) corresponding to the [entry](creature_template). The value essential defines the equip:

-   **-1**: A random equip from the set of equips in [creature\_equip\_template](creature_equip_template) will be chosen.
-   **0**: No equipment defined.
-   **1+**: The individual id within creature\_equip\_template.

If creature spawned with `.npc add`, then this value will be set automatically (0 if nothing in creature_equip_template).

### position\_x

The X position of the creatures spawn point.

### position\_y

The Y position of the creatures spawn point.

### position\_z

The Z position of the creatures spawn point.

### orientation

The orientation of the creatures spawn point. (North = 0.0; South = pi (3.14159))

### spawntimesecs

The respawn time, in seconds, of the creature.

### wander_distance

The maximum distance that the creature may spawn from its spawn point. Also controls how far away the creature can walk from its spawn point if its [MovementType](#creature-MovementType) = 1.

### currentwaypoint

The current [waypoint](waypoint_data#waypoint_data-point) that the creature is on, if any.

### curhealth

The health that the creature will spawn with.

### curmana

The mana that the creature will spawn with.

### MovementType

The movement type associated with the creature. Usually the same as its [MovementType](creature_template#creature_template-MovementType), but it can be different.

### npcflag

Same as [creature\_template.npcflag](creature_template#creature_template-npcflag) .

NOTE: A creature.npcflag record will override a [creature\_template.npcflag](creature_template#creature_template-npcflag) record.

### unit\_flags

Same as creature\_template.unit\_flags.

Note:

A creature.unit\_flags record will override a [creature\_template.unit\_flags](creature_template#creature_template-unit_flags) record.

### dynamicflags

Same as creature\_template.dynamicflags.

Note:

A creature.dynamicflags record will override a [creature\_template.dynamicflags](creature_template#creature_template-dynamicflags) record.

### ScriptName

Same as creature\_template.scriptname.

A creature.scriptname record will override a [creature\_template.scriptname](creature_template#creature_template-scriptname) record.

### VerifiedBuild

This field is used to determine if this creature originates from verified sniffs.

If value is 0 then it has not been parsed yet or it has been inherited from an older DB or another Core.

If value is above 0 then it has been parsed with sniffs from that specific client build.

If value is -Client Build then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.

### CreateObject

This field is specific to creatures and used to determine if the positions are perfected.

Once a creature is sniffed, the packet can be either CreateObject1 or CreateObject2.
A CO1 creature usually has already spawned, has moved, and thus deviates from its real spawn position.
A CO2 creature was sniffed when it has spawned, so it is, in most cases, its real spawn position.

Another 3rd value is used for special cases, which are creatures that do not respawn normally but by scripts. It is functionally the same as CO2 and only used to distinguish these special cases better.

### comment

This field serves to add additional context to this creature, mostly in the context of sniffed or script notes.

For example, if a creature's position needed to be modified, the original positions are kept in the comment field. Or if the creatures in question are part of a larger script, the comment serves for context.

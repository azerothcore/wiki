# creature

[<-Back-to:World](database-world)

**Table: creature's Structure**

Contains individual creature spawn data for each individual spawn of each individual creature in the game world.

| Field                               | Type     |          | Null | Key | Default | Extra          | Comment                                 |
| :---------------------------------- | :------- | :------- | :--: | :-: | :-----: | :------------: | :-------------------------------------- |
| [guid](#guid)                       | INT      | UNSIGNED | NO   | PRI |         | AUTO_INCREMENT | Global Unique Identifier                |
| [id](#id)                           | INT      | UNSIGNED | NO   | MUL | 0       |                | Creature Identifier                     |
| [map](#map)                         | SMALLINT | UNSIGNED | NO   | MUL | 0       |                | Map Identifier                          |
| [zoneId](#zoneid)                   | SMALLINT | UNSIGNED | NO   |     | 0       |                | Zone Identifier                         |
| [areaId](#areaid)                   | SMALLINT | UNSIGNED | NO   |     | 0       |                | Area Identifier                         |
| [spawnMask](#spawnmask)             | TINYINT  | UNSIGNED | NO   |     | 1       |                |                                         |
| [phaseMask](#phasemask)             | INT      | UNSIGNED | NO   |     | 1       |                |                                         |
| [equipment_id](#equipmentid)        | TINYINT  |          | NO   |     | 0       |                |                                         |
| [position_x](#positionx)            | FLOAT    |          | NO   |     | 0       |                |                                         |
| [position_y](#positiony)            | FLOAT    |          | NO   |     | 0       |                |                                         |
| [position_z](#positionz)            | FLOAT    |          | NO   |     | 0       |                |                                         |
| [orientation](#orientation)         | FLOAT    |          | NO   |     | 0       |                |                                         |
| [spawntimesecs](#spawntimesecs)     | INT      | UNSIGNED | NO   |     | 120     |                |                                         |
| [wander_distance](#wanderdistance)  | FLOAT    |          | NO   |     | 0       |                | Dist in yards for random movement.      |
| [currentwaypoint](#currentwaypoint) | INT      | UNSIGNED | NO   |     | 0       |                | Storage used by core. "Always set as 0" |
| [curhealth](#curhealth)             | INT      | UNSIGNED | NO   |     | 1       |                | Storage used by core. "Always set as 1" |
| [curmana](#curmana)                 | INT      | UNSIGNED | NO   |     | 0       |                | Storage used by core. "Always set as 0" |
| [MovementType](#movementtype)       | TINYINT  | UNSIGNED | NO   |     | 0       |                | 0 No movement, 1 random, 2 path         |
| [npcflag](#npcflag)                 | INT      | UNSIGNED | NO   |     | 0       |                | creature_template override              |
| [unit_flags](#unitflags)            | INT      | UNSIGNED | NO   |     | 0       |                | creature_template override              |
| [dynamicflags](#dynamicflags)       | INT      | UNSIGNED | NO   |     | 0       |                | creature_template override              |
| [ScriptName](#scriptname)           | CHAR(64) |          | YES  |     | ''      |                |                                         |
| [VerifiedBuild](#verifiedbuild)     | INT      |          | YES  |     | NULL    |                | Not used by the core.                   |
| [CreateObject](#createobject)       | TINYINT  | UNSIGNED | NO   |     | 0       |                | Not used by the core.                   |
| [Comment](#comment)                 | TEXT     |          | YES  |     | NULL    |                | Not used by the core.                   |

**Description of the table's fields**

### guid

A unique identifier given to each creature to distinguish one creature from another. Two creatures can NOT have same GUID.

### id

The ID of the [template](creature_template#entry) that is used when instantiating this creature.

To let a single spawn point pick from more than one template (the old `id1`/`id2`/`id3` behaviour), add the additional entries in [creature_multispawn](creature_multispawn) keyed by this creature's `guid`.

### map

The ID of the [map](map) that the creature is spawned on.

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

| Value | Hex    | Flag | Comment                                                                              |
| :---- | :----: | :--- | :----------------------------------------------------------------------------------- |
| 0     | `0x00` |      | Not spawned                                                                          |
| 1     | `0x01` |      | Spawned only in 10-man-normal versions of maps (includes maps without a heroic mode) |
| 2     | `0x02` |      | Spawned only in 25-man-normal versions of maps (or heroics pre 3.2)                  |
| 4     | `0x04` |      | Spawned only in 10-man heroic versions of maps                                       |
| 8     | `0x08` |      | Spawned only in 25-man-heroic versions of maps                                       |
| 15    | `0x0F` |      | Spawned in all versions of maps                                                      |

### phaseMask

This is a bit-mask field that describes all the phases that a creature will appear in. Aura 261 determines the phase you can see. For example, if you had this aura <http://www.wowhead.com/?spell=55782>, you would be able to see creatures in phase 2. If you wanted the creature to be visible in both phase 1 and phase 2, you would set the phase-mask to 3.

### equipment_id

The ID as defined within [creature_equip_template](creature_equip_template) corresponding to the [entry](creature_template). The value essential defines the equip:

-   **-1**: A random equip from the set of equips in [creature_equip_template](creature_equip_template) will be chosen.
-   **0**: No equipment defined.
-   **1+**: The individual id within creature_equip_template.

If creature spawned with `.npc add`, then this value will be set automatically (0 if nothing in creature_equip_template).

### position_x

The X position of the creatures spawn point.

### position_y

The Y position of the creatures spawn point.

### position_z

The Z position of the creatures spawn point.

### orientation

The orientation of the creatures spawn point. (North = 0.0; South = pi (3.14159))

### spawntimesecs

The respawn time, in seconds, of the creature.

### wander_distance

The maximum distance that the creature may spawn from its spawn point. Also controls how far away the creature can walk from its spawn point if its [MovementType](#movementtype) = 1.

### currentwaypoint

The current [waypoint](waypoint_data#point) that the creature is on, if any.

### curhealth

The health that the creature will spawn with.

### curmana

The mana that the creature will spawn with.

### MovementType

The movement type associated with the creature. Usually the same as its [MovementType](creature_template#movementtype), but it can be different.

### npcflag

Same as [creature_template.npcflag](creature_template#npcflag) .

NOTE: A creature.npcflag record will override a [creature_template.npcflag](creature_template#npcflag) record.

### unit_flags

Same as creature_template.unit_flags.

Note:

A creature.unit_flags record will override a [creature_template.unit_flags](creature_template#unitflags) record.

### dynamicflags

Same as creature_template.dynamicflags.

Note:

A creature.dynamicflags record will override a [creature_template.dynamicflags](creature_template#dynamicflags) record.

### ScriptName

Same as creature_template.scriptname.

A creature.scriptname record will override a [creature_template.scriptname](creature_template#scriptname) record.

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

This field serves to add additional context to this creature, mostly in the context of sniffed values or script notes.

For example, if a creature's position needed to be modified, the original positions are kept in the comment field. Or if the creatures in question are part of a larger script, the comment serves for context.

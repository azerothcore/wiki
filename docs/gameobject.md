# gameobject

[<-Back-to:World](database-world)

**The \`gameobject\` table**

This table holds the individual object data on each spawned game object in the world. This data along with the object's template data is read and used to instantiate the objects in the world.

**Table: gameobject's Structure**

| Field                           | Type     |          | Null | Key | Default | Extra          | Comment                  |
| :------------------------------ | :------- | :------- | :--: | :-: | :-----: | :------------: | :----------------------- |
| [guid](#guid)                   | INT      | UNSIGNED | NO   | PRI |         | AUTO_INCREMENT | Global Unique Identifier |
| [id](#id)                       | INT      | UNSIGNED | NO   |     | 0       |                | Gameobject Identifier    |
| [map](#map)                     | SMALLINT | UNSIGNED | NO   |     | 0       |                | Map Identifier           |
| [zoneId](#zoneid)               | SMALLINT | UNSIGNED | NO   |     | 0       |                | Zone Identifier          |
| [areaId](#areaid)               | SMALLINT | UNSIGNED | NO   |     | 0       |                | Area Identifier          |
| [spawnMask](#spawnmask)         | TINYINT  | UNSIGNED | NO   |     | 1       |                |                          |
| [phaseMask](#phasemask)         | INT      | UNSIGNED | NO   |     | 1       |                |                          |
| [position_x](#positionx)        | FLOAT    |          | NO   |     | 0       |                |                          |
| [position_y](#positiony)        | FLOAT    |          | NO   |     | 0       |                |                          |
| [position_z](#positionz)        | FLOAT    |          | NO   |     | 0       |                |                          |
| [orientation](#orientation)     | FLOAT    |          | NO   |     | 0       |                |                          |
| [rotation0](#rotation0)         | FLOAT    |          | NO   |     | 0       |                |                          |
| [rotation1](#rotation1)         | FLOAT    |          | NO   |     | 0       |                |                          |
| [rotation2](#rotation2)         | FLOAT    |          | NO   |     | 0       |                |                          |
| [rotation3](#rotation3)         | FLOAT    |          | NO   |     | 0       |                |                          |
| [spawntimesecs](#spawntimesecs) | INT      |          | NO   |     | 0       |                |                          |
| [animprogress](#animprogress)   | TINYINT  | UNSIGNED | NO   |     | 0       |                |                          |
| [state](#state)                 | TINYINT  | UNSIGNED | NO   |     | 0       |                |                          |
| [ScriptName](#scriptname)       | CHAR(64) |          | YES  |     | ''      |                |                          |
| [VerifiedBuild](#verifiedbuild) | INT      |          | YES  |     | NULL    |                | Not used by the core.    |
| [Comment](#comment)             | TEXT     |          | YES  |     | NULL    |                |                          |

**Description of the table's fields**

### guid

The global unique identifier for the game object. This field must be unique among all game objects.

### id

The template ID of the gameobject. See [gameobject_template.entry](http://www.azerothcore.org/wiki/gameobject_template#entry)

### map

The map ID where this object is spawned. See Maps.dbc

### zoneId

The ID of the zone that this object is spawned in. (e.g. The Barrens)

This column is filled in by the worldserver on startup if the `Calculate.Gameoject.Zone.Area.Data` setting is enabled. It originates from AreaTable.dbc.

### areaId

The ID of the area that this object is spawned in. You can think of an area as a "subzone" of a zone, e.g. Lushwater Oasis inside The Barrens. 

This column is filled in by the worldserver on startup if the `Calculate.Gameoject.Zone.Area.Data` setting is enabled. It originates from AreaTable.dbc.

### spawnMask

Controls under which difficulties the object is spawned.

Just like flags you can add them as you wish so 3 would be: Spawned in 10/25 man normal versions of maps (pre 3.2 all maps)

| Value | Hex    | Flag | Comment                                                                              |
| :---- | :----: | :--- | :----------------------------------------------------------------------------------- |
| 0     | `0x00` |      | Not spawned                                                                          |
| 1     | `0x01` |      | Spawned only in 10-man-normal versions of maps (includes maps without a heroic mode) |
| 2     | `0x02` |      | Spawned only in 25-man-normal versions of maps (or heroics pre 3.2)                  |
| 4     | `0x04` |      | Spawned only in 10-man heroic versions of maps                                       |
| 8     | `0x08` |      | Spawned only in 25-man-heroic versions of maps                                       |
| 15    | `0x0F` |      | Spawned in all versions of maps                                                      |

### phaseMask

This is a bitmask field that describes all the phases that this gameobject will appear in. Aura 261 determines the phase you can see. For example, if you had this aura <http://www.wowhead.com/?spell=55782>, you would be able to see gameobjects in phase 2. If you wanted the gameobject to be visible in both phase 1 and phase 2, you would set the phaseMask to 3.

### position_x

The X position.

### position_y

The Y position.

### position_z

The Z position.

### orientation

The orientation. (North = 0, South = 3.14159)

### rotation0

The X value of the quaternion that sets the rotation of the gameobject. rotation0, rotation1, rotation2 and rotation3 together are the X, Y, Z and W values of the quaternion.

Each value must be between -1 and 1, and together they must form a unit quaternion (rotation0² + rotation1² + rotation2² + rotation3² = 1). If they do not, the core ignores them and only rotates the gameobject by its [orientation](#orientation).

For a gameobject that is only turned around the Z axis, which is most of them:

- rotation0 = 0
- rotation1 = 0
- rotation2 = sin([orientation](#orientation) / 2)
- rotation3 = cos([orientation](#orientation) / 2)

The `.gobject turn` command sets the rotation in game.

### rotation1

The Y value of the rotation quaternion. See [rotation0](#rotation0).

### rotation2

The Z value of the rotation quaternion. See [rotation0](#rotation0).

### rotation3

The W value of the rotation quaternion. See [rotation0](#rotation0).

### spawntimesecs

Time in seconds for this object to respawn.

Using 0 will result in the object not despawning on use.

Using a negative value will result in the object starting out by being "despawned" until a script will spawn it. It will then despawn after the amount of time specified here has passed.

### animprogress

Not really known what this is used for at this time. However, always set it to 100 for chests.

### state

For chests or doors.

-   1 = closed
-   0 = open

### ScriptName

Same as gameobject_template.scriptname.

A gameobject.scriptname record will override a [gameobject_template.scriptname](gameobject_template#scriptname) record.

### VerifiedBuild

This field is used to determine if this gameobject originates from verified sniffs.

If value is 0 then it has not been parsed yet or it has been inherited from an older DB or another Core.

If value is above 0 then it has been parsed with sniffs from that specific client build.

If value is -Client Build then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.

### comment

This field serves to add additional context to this gameobject, mostly in the context of sniffed values or script notes.

For example, if a gameobject's position needed to be modified, the original positions are kept in the comment field. Or if the gobs in question are part of a larger script, the comment serves for context.

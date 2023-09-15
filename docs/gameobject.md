# gameobject

[<-Back-to:World](database-world.md)

**The \`gameobject\` table**

This table holds the individual object data on each spawned game object in the world. This data along with the object's template data is read and used to instantiate the objects in the world.

**Structure**

| Field               | Type         | Attributes | Key | Null | Default | Extra          | Comment                  |
|---------------------|--------------|------------|-----|------|---------|----------------|--------------------------|
| [guid][1]           | INT          | UNSIGNED   | PRI | NO   | NULL    | Auto increment | Global Unique Identifier |
| [id][2]             | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |                | Gameobject Identifier    |
| [map][3]            | SMALLINT     | UNSIGNED   |     | NO   | 0       |                | Map Identifier           |
| [zoneId][4]         | SMALLINT     | UNSIGNED   |     | NO   | 0       |                | Zone Identifier          |
| [areaId][5]         | SMALLINT     | UNSIGNED   |     | NO   | 0       |                | Area Identifier          |
| [spawnMask][6]      | TINYINT      | UNSIGNED   |     | NO   | 1       |                |                          |
| [phaseMask][7]      | SMALLINT     | UNSIGNED   |     | NO   | 1       |                |                          |
| [position_x][8]     | FLOAT        | SIGNED     |     | NO   | 0       |                |                          |
| [position_y][9]     | FLOAT        | SIGNED     |     | NO   | 0       |                |                          |
| [position_z][10]    | FLOAT        | SIGNED     |     | NO   | 0       |                |                          |
| [orientation][11]   | FLOAT        | SIGNED     |     | NO   | 0       |                |                          |
| [rotation0][12]     | FLOAT        | SIGNED     |     | NO   | 0       |                |                          |
| [rotation1][13]     | FLOAT        | SIGNED     |     | NO   | 0       |                |                          |
| [rotation2][14]     | FLOAT        | SIGNED     |     | NO   | 0       |                |                          |
| [rotation3][15]     | FLOAT        | SIGNED     |     | NO   | 0       |                |                          |
| [spawntimesecs][16] | INT          | SIGNED     |     | NO   | 0       |                |                          |
| [animprogress][17]  | TINYINT      | UNSIGNED   |     | NO   | 0       |                |                          |
| [state][18]         | TINYINT      | UNSIGNED   |     | NO   | 1       |                |                          |
| [Comment][19]       | TEXT         |            |     | YES  | NULL    |                |                          |

[1]: #guid
[2]: #id
[3]: #map
[4]: #zoneId
[5]: #areaId
[6]: #spawnmask
[7]: #phasemask
[8]: #position_x
[9]: #position_y
[10]: #position_z
[11]: #orientation
[12]: #rotation0
[13]: #rotation1
[14]: #rotation2
[15]: #rotation3
[16]: #spawntimesecs
[17]: #animprogress
[18]: #state
[19]: #comment

**Description of the fields**

### guid

The global unique identifier for the game object. This field must be unique among all game objects.

### id

The template ID of the gameobject. See [gameobject\_template.entry](http://www.azerothcore.org/wiki/gameobject_template#entry)

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

| Value | Comment                                                                              |
|-------|--------------------------------------------------------------------------------------|
| 0     | Not spawned                                                                          |
| 1     | Spawned only in 10-man-normal versions of maps (includes maps without a heroic mode) |
| 2     | Spawned only in 25-man-normal versions of maps (or heroics pre 3.2)                  |
| 4     | Spawned only in 10-man heroic versions of maps                                       |
| 8     | Spawned only in 25-man-heroic versions of maps                                       |
| 15    | Spawned in all versions of maps                                                      |

### phaseMask

This is a bitmask field that describes all the phases that this gameobject will appear in. Aura 261 determines the phase you can see. For example, if you had this aura <http://www.wowhead.com/?spell=55782>, you would be able to see gameobjects in phase 2. If you wanted the gameobject to be visible in both phase 1 and phase 2, you would set the phaseMask to 3.

### position\_x

The X position.

### position\_y

The Y position.

### position\_z

The Z position.

### orientation

The orientation. (North = 0, South = 3.14159)

### rotation0

### rotation1

### rotation2

### rotation3

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

### comment

This field serves to add additional context to this gameobject, mostly in the context of sniffed values or script notes.

For example, if a gameobject's position needed to be modified, the original positions are kept in the comment field. Or if the gobs in question are part of a larger script, the comment serves for context.

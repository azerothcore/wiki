# gameobject

[<-Back-to:World](database-world.md)

**The \`gameobject\` table**

This table holds the individual object data on each spawned game object in the world. This data along with the object's template data is read and used to instantiate the objects in the world.

**Structure**

| Field               | Type         | Attributes | Key | Null | Default | Extra          | Comment                  |
|---------------------|--------------|------------|-----|------|---------|----------------|--------------------------|
| [guid][1]           | INT(10)      | unsigned   | PRI | NO   | NULL    | Auto increment | Global Unique Identifier |
| [id][2]             | MEDIUMINT(8) | unsigned   |     | NO   | 0       |                | Gameobject Identifier    |
| [map][3]            | SMALLINT(5)  | unsigned   |     | NO   | 0       |                | Map Identifier           |
| [spawnMask][4]      | TINYINT(3)   | unsigned   |     | NO   | 1       |                |                          |
| [phaseMask][5]      | SMALLINT(5)  | unsigned   |     | NO   | 1       |                |                          |
| [position_x][6]     | FLOAT        | signed     |     | NO   | 0       |                |                          |
| [position_y][7]     | FLOAT        | signed     |     | NO   | 0       |                |                          |
| [position_z][8]     | FLOAT        | signed     |     | NO   | 0       |                |                          |
| [orientation][9]    | FLOAT        | signed     |     | NO   | 0       |                |                          |
| [rotation0][10]     | FLOAT        | signed     |     | NO   | 0       |                |                          |
| [rotation1][11]     | FLOAT        | signed     |     | NO   | 0       |                |                          |
| [rotation2][12]     | FLOAT        | signed     |     | NO   | 0       |                |                          |
| [rotation3][13]     | FLOAT        | signed     |     | NO   | 0       |                |                          |
| [spawntimesecs][14] | INT(11)      | signed     |     | NO   | 0       |                |                          |
| [animprogress][15]  | TINYINT(3)   | unsigned   |     | NO   | 0       |                |                          |
| [state][16]         | TINYINT(3)   | unsigned   |     | NO   | 1       |                |                          |

[1]: #guid
[2]: #id
[3]: #map
[4]: #spawnmask
[5]: #phasemask
[6]: #position_x
[7]: #position_y
[8]: #position_z
[9]: #orientation
[10]: #rotation0
[11]: #rotation1
[12]: #rotation2
[13]: #rotation3
[14]: #spawntimesecs
[15]: #animprogress
[16]: #state

**Description of the fields**

### guid

The global unique identifier for the game object. This field must be unique among all game objects.

### id

The template ID of the gameobject. See [gameobject\_template.entry](http://www.azerothcore.org/wiki/gameobject_template#entry)

### map

The map ID where this object is spawned. See Maps.dbc

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

Using a negative value will result in the object starting out by being "despawned" until a script will spawn it. It will then despawn after the amount of time specified here has passed.

### animprogress

Not really known what this is used for at this time. However, always set it to 100 for chests.

### state

For chests or doors.

-   1 = closed
-   0 = open

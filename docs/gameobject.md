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
| [position_z][10]     | FLOAT        | SIGNED     |     | NO   | 0       |                |                          |
| [orientation][11]    | FLOAT        | SIGNED     |     | NO   | 0       |                |                          |
| [rotation0][12]     | FLOAT        | SIGNED     |     | NO   | 0       |                |                          |
| [rotation1][13]     | FLOAT        | SIGNED     |     | NO   | 0       |                |                          |
| [rotation2][14]     | FLOAT        | SIGNED     |     | NO   | 0       |                |                          |
| [rotation3][15]     | FLOAT        | SIGNED     |     | NO   | 0       |                |                          |
| [spawntimesecs][16] | INT          | SIGNED     |     | NO   | 0       |                |                          |
| [animprogress][17]  | TINYINT      | UNSIGNED   |     | NO   | 0       |                |                          |
| [state][18]         | TINYINT      | UNSIGNED   |     | NO   | 1       |                |                          |

[1]: #guid
[2]: #id
[3]: #map
[4]: #zoneId
[5]: #areaId
[6]: #spawnMask
[7]: #phaseMask
[8]: #position\_x
[9]: #position\_y
[10]: #position\_z
[11]: #orientation
[12]: #rotation0
[13]: #rotation1
[14]: #rotation2
[15]: #rotation3
[16]: #spawntimesecs
[17]: #animprogress
[18]: #state

## Column's description

### guid

The global unique identifier for the game object. This field must be unique among all game objects.

### id

The template ID of the gameobject. See [gameobject\_template.entry](http://www.azerothcore.org/wiki/gameobject_template#entry)

### map

The map ID where this object is spawned.The most used values are:
Map ID | Map name
--- | ---
0 | Eastern Kingdoms
1 | Kalimdor
530 | Northrend

For more information, use the [DBC Reader](https://github.com/wowgaming/node-dbc-reader) on Maps.dbc for the used data.

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

### position\_y

### position\_z

There are 3 axis for position on the 3D space which are position\_x , y and z.
The coordinates of the gameobject on said map.
There's a command called `.gps` which can be used to know the player's current position which prints on the chat your current position on the map.

If you want to manually add gameobjects you can do so with `.gobject add #entry` and the positions will be automatically added based on the player's current position.

### orientation

The direction to which the gameobject is facing towards. 

Direction | Value
--- | ---
North | 0
south | 3.14159

### rotation0
### rotation1
### rotation2
### rotation3

There are 4 columns for rotation ranging from 0 to 3.

### spawntimesecs

Time in seconds for this object to respawn.

Using a negative value will result in the object starting out by being "despawned" until a script will spawn it. It will then despawn after the amount of time specified here has passed.

### animprogress

This column is still not understood to what its purpose is for however, this is always set to `100` for chests.

According to **ratkosrb**:
> In wotlk and after its the current health percent of destructible gameobjects, like the gates in SOTA. In vanilla and tbc I'm not sure what its used for, but if you set it to 255 it disables animations, like doors snapping open/closed instantly. Also this field was first added to update fields in patch 1.12 (previous vanilla versions didn't have it), so my guess is it was used for the open world PvP objectives in EPL.



### state

This column is used to avoid players to interact at the same time with the same gameobject.
When it is used, by right clicking or interacting with it via command, the state changes, preventing it to be activated more than once.
-   When `State = 1` the gameobject hasn't been used yet, being in a "Closed" state. For example, Chests when shut or locked doors.
-   When `State = 0` the gameobject has been activated, being set to a "Open" or "Active" state. For example, Chests when open, opened doors or nodes when gathered.

It's normal for all gameobjects to jump from state to state and this is usually reset whenever they re-spawn, rarely by scripts but not unlikely.

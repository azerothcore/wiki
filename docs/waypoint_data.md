# waypoint\_data

[<-Back-to:World](database-world)

**The \`waypoint\_data\` table**

This table contains all the path data for creatures that use waypoints and waypoint scripts directly in their creature addon definition. See also [Waypoints-Information](Waypoints-Information) for general information about waypoints.

**Table Structure**

| Field                           | Type      | Attributes | Key | Null | Default |
| ------------------------------- | --------- | ---------- | --- | ---- | ------- |
| [id](#id)                       | INT       | UNSIGNED   | PRI | NO   | 0       |
| [point](#point)                 | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |
| [position\_x](#positionx)       | FLOAT     |            |     | NO   | 0       |
| [position\_y](#positiony)       | FLOAT     |            |     | NO   | 0       |
| [position\_z](#positionz)       | FLOAT     |            |     | NO   | 0       |
| [orientation](#orientation)     | FLOAT     |            |     | YES  | NULL    |
| [delay](#delay)                 | INT       | UNSIGNED   |     | NO   | 0       |
| [move\_type](#movetype)         | INT       |            |     | NO   | 0       |
| [action](#action)               | INT       |            |     | NO   | 0       |
| [action\_chance](#actionchance) | SMALLINT  |            |     | NO   | 100     |
| [wpguid](#wpguid)               | INT       | UNSIGNED   |     | NO   | 0       |

**Description of the fields**

### id

Unique ID for each path.

*The TDB standard way of assigning an ID is to multiply GUID of the creature by 10.*

*So for a creature with a GUID of 1234 the path ID would be 12340. Any waypoints submitted to TDB should follow this standard.*

*However, this is only a suggestion when creating your own waypoints. This ID can be anything you want as long as creature\_addon.path\_id is set to the ID you pick here for the creature you are creating a waypoint for.*

### point

Unique point ID for each point in a path. Starts at 1 and increases with each path.

### position\_x

The X coordinate of the destination waypoint.

### position\_y

The Y coordinate of the destination waypoint.

### position\_z

The Z coordinate of the destination waypoint.

### orientation

The orientation of the creature. (North = 0.0; South = π (3.14159))

### delay

Time to wait (in ms) between each point.

### move\_type

|      |     |
| ---- | --- |
| Walk | 0   |
| Run  | 1   |
| Fly  | 2   |

### action

ID of the action to be performed. See [waypoint\_scripts.id](waypoint_scripts).

### action\_chance

Percentage of action happening (0-100%).

### wpguid

This field is used by the core and is **NOT** to be set by hand.

This field holds the GUID of the waypoint visual when you enable the visual mode for waypoints.

### Example Rows

| Id    | Point | Position\_x | Position\_y | Position\_z | Orientation | Delay | Move\_type | Action | Action\_chance | wpguid |
| ----- | ----- | ----------- | ----------- | ----------- | ----------- | ----- | ---------- | ------ | -------------- | ------ |
| 20160 | 1     | -4998       | -1167       | 501657      | 0           | 10000 | 0          | 0      | 100            | 0      |
| 20160 | 2     | -4958.38    | -1199.34    | 501659      | 0           | 0     | 0          | 0      | 100            | 0      |

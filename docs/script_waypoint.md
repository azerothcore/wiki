# script\_waypoint

[<-Back-to:World](database-world)

**The \`script\_waypoint\` table**

This table contains waypoint paths used by creatures driven by scripted AI (`CreatureAI`). It is the scripted-AI counterpart to [waypoint\_data](waypoint_data) (used by creatures via their [creature\_addon](creature_addon)) and to [waypoints](waypoints) (used by [SmartAI](smart_scripts)). See also [Waypoints-Information](waypoints-information) for general information about waypoints.

**Table Structure**

| Field                             | Type | Attributes | Key | Null | Default |
| --------------------------------- | ---- | ---------- | --- | ---- | ------- |
| [entry](#entry)                   | INT  | UNSIGNED   | PRI | NO   | 0       |
| [pointid](#pointid)               | INT  | UNSIGNED   | PRI | NO   | 0       |
| [location\_x](#locationx)         | FLOAT |           |     | NO   | 0       |
| [location\_y](#locationy)         | FLOAT |           |     | NO   | 0       |
| [location\_z](#locationz)         | FLOAT |           |     | NO   | 0       |
| [waittime](#waittime)             | INT  | UNSIGNED   |     | NO   | 0       |
| [point\_comment](#pointcomment)   | TEXT |            |     | YES  | NULL    |

**Description of the fields**

### entry

The [creature\_template.entry](creature_template#entry) of the creature this path belongs to. Together with `pointid` it forms the primary key.

### pointid

The sequential number of this point within the path, starting at 1. Together with `entry` it forms the primary key.

### location_x

The X coordinate of the waypoint.

### location_y

The Y coordinate of the waypoint.

### location_z

The Z coordinate of the waypoint.

### waittime

How long the creature waits at this waypoint, in milliseconds, before moving to the next point.

### point_comment

An optional free-text comment describing the waypoint.

[Database Structure](Database-Structure) > [World-Database](World-Database) > [waypoint_scripts](waypoint_scripts)

# waypoint\_scripts

###### **Used by [waypoint_data](waypoint_data)**

### Information

Waypoint paths directly attached to a creature via [creature_addon.path_id](creature_addon#path_id) use the tables [waypoint_data](waypoint_data) and [waypoint_scripts](waypoint_scripts). They can be added and manipulated using the GM '.wp' commands. See also [Waypoints-Information](Waypoints-Information) for general information about waypoints.

### Structure

| Field                            | Type         | Attributes   | Key | Null | Default | Comment
|----------------------------------|--------------|--------------|-----|------|---------|--------
| [id](scripts#id)                 | INT      | UNSIGNED     |     | NO   | 0       |
| [delay](scripts#delay)           | INT      | UNSIGNED     |     | NO   | 0       |
| [command](scripts#command)       | INT      | UNSIGNED     |     | NO   | 0       |
| [datalong](scripts#otherfields)  | INT      | UNSIGNED     |     | NO   | 0       |
| [datalong2](scripts#otherfields) | INT      | UNSIGNED     |     | NO   | 0       |
| [dataint](scripts#otherfields)   | INT      | UNSIGNED     |     | NO   | 0       |
| [x](scripts#otherfields)         | FLOAT        |              |     | NO   | 0       |
| [y](scripts#otherfields)         | FLOAT        |              |     | NO   | 0       |
| [z](scripts#otherfields)         | FLOAT        |              |     | NO   | 0       |
| [o](scripts#otherfields)         | FLOAT        |              |     | NO   | 0       |
| [guid](scripts#guid)             | INT      |              | PRI | NO   | 0       | acts as primary key and is set automatically using the [GM command](GM-Commands) 'wp event add'


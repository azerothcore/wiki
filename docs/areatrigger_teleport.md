# areatrigger\_teleport

[<-Back-to:World](database-world.md)

**The \`areatrigger\_teleport\` table**

Contains all the teleport triggers definition. This table is used to complete .dbc file information.

**Structure**

| Field                   | Type         | Attributes | Key | Null | Default | Extra | Comment    |
|-------------------------|--------------|------------|-----|------|---------|-------|------------|
| [id][1]                 | mediumint(8) | unsigned   | PRI | NO   | 0       |       | Identifier |
| [name][2]               | text         | signed     |     | YES  | NULL    |       |            |
| [target_map][3]         | smallint(5)  | unsigned   |     | NO   | 0       |       |            |
| [target_position_x][4]  | float        | signed     |     | NO   | 0       |       |            |
| [target_position_y][5]  | float        | signed     |     | NO   | 0       |       |            |
| [target_position_z][6]  | float        | signed     |     | NO   | 0       |       |            |
| [target_orientation][7] | float        | signed     |     | NO   | 0       |       |            |
| [VerifiedBuild][8]      | smallint(5)  | signed     |     | YES  | 0       |       |            |

[1]: #id
[2]: #name
[3]: #target_map
[4]: #target_position_x
[5]: #target_position_y
[6]: #target_position_z
[7]: #target_orientation
[8]: #verifiedbuild

**Description of the fields**

### id

This is the trigger identifier, it must match with the one from [AreaTrigger.dbc](DBC-AreaTrigger)

### name

Name of the trigger. This can be an arbitrary name, and is for descriptive purposes only.

### target\_map

Target map of the trigger (see Maps.dbc).

### target\_position\_x

X coordinate for the target destination of the trigger

### target\_position\_y

Y coordinate for the target destination of the trigger

### target\_position\_z

Z coordinate for the target destination of the trigger

### target\_orientation

Orientation the player will get when appearing at this location

### VerifiedBuild

This field was used to determine whether a template has been verified from WDB files.

If value is 0 then it has not been parsed yet.

If value is above 0 then it has been parsed with WDB files from that specific client build.

If value is -1 then it is just a place holder until proper data are found on WDBs.

If value is -Client Build then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.

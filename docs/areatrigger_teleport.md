# areatrigger\_teleport

[<-Back-to:World](database-world)

**The \`areatrigger\_teleport\` table**

Contains all the teleport triggers definition. This table is used to complete .dbc file information.

**Table: areatrigger\_teleport's Structure**

| Field                                    | Type     |          | Null | Key | Default | Extra | Comment |
| :--------------------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                | INT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [Name](#name)                            | TEXT     |          | YES  | MUL | NULL    |       |         |
| [target_map](#targetmap)                 | SMALLINT | UNSIGNED | NO   |     | 0       |       |         |
| [target_position_x](#targetpositionx)    | FLOAT    |          | NO   |     | 0       |       |         |
| [target_position_y](#targetpositiony)    | FLOAT    |          | NO   |     | 0       |       |         |
| [target_position_z](#targetpositionz)    | FLOAT    |          | NO   |     | 0       |       |         |
| [target_orientation](#targetorientation) | FLOAT    |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

This is the trigger identifier, it must match with the one from [AreaTrigger.dbc](dbc-areatrigger)

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

### Examples

| ID  | Name                                     | target_map | target_position_x | target_position_y | target_position_z | target_orientation |
| --- | ---------------------------------------- | ---------- | ----------------- | ----------------- | ----------------- | ------------------ |
| 45  | Scarlet Monastery - Graveyard (Entrance) | 189        | 1688.99           | 1053.48           | 18.6775           | 0.00117            |
| 78  | DeadMines Entrance                       | 36         | -16.4             | -383.07           | 61.78             | 1.86               |
| 101 | Stormwind Stockades Entrance             | 34         | 54.23             | 0.28              | -18.34            | 6.26               |
| 107 | Stormwind Vault Entrance                 | 35         | -0.91             | 40.57             | -24.23            | 0                  |
| 109 | Stormwind Vault Instance                 | 0          | -8653.45          | 606.19            | 91.16             | 0                  |

# areatrigger

[<-Back-to:World](database-world.md)

**The \`areatrigger\` table**

This table contains trigger points for events in certain coordinates in the maps.

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db.md)

**Structure**

| Field       | Type  | Attributes | Key | Null | Default | Extra          | Comment                                              |
| ----------- | ----- | ---------- | --- | ---- | ------- | -------------- | ---------------------------------------------------- |
| entry       | INT   | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |                                                      |
| map         | INT   | UNSIGNED   |     | NO   | 0       |                |                                                      |
| x           | FLOAT |            |     | NO   | 0       |                |                                                      |
| y           | FLOAT |            |     | NO   | 0       |                |                                                      |
| z           | FLOAT |            |     | NO   | 0       |                |                                                      |
| radius      | FLOAT |            |     | NO   | 0       |                | Seems to be a box of size yards with center at x,y,z |
| length      | FLOAT |            |     | NO   | 0       |                | Most commonly used when size is 0, but not always    |
| width       | FLOAT |            |     | NO   | 0       |                | Most commonly used when size is 0, but not always    |
| height      | FLOAT |            |     | NO   | 0       |                | Most commonly used when size is 0, but not always    |
| orientation | FLOAT |            |     | NO   | 0       |                | Most commonly used when size is 0, but not always    |

**Description of the fields**

### Entry

This is just a automatic counter that assigns a value to each trigger to list it.

### Map

This field recall a certain map based on the ID (for example, ID 30 recalls Elwynn Forest)

### X, Y and Z

Contains the coordinates of the three 3d dimensions.

### Radius

This contains the radius of activation of the trigger.

### Length, Width, Height and Orientation

these fields contain the values for the physics and behavior of a given trigger.

### Example

| entry | map | x        | y        | z       | radius | length | width | height | orientation |
| ----- | --- | -------- | -------- | ------- | ------ | ------ | ----- | ------ | ----------- |
| 45    | 0   | 2924.38  | -798.429 | 161.611 | 8      | 0      | 0     | 0      | 0           |
| 71    | 0   | -10645.9 | 1179.06  | 48.1781 | 27     | 0      | 0     | 0      | 0           |
| 78    | 0   | -11208.5 | 1685.34  | 25.7612 | 7      | 0      | 0     | 0      | 0           |
| 84    | 0   | 16449.9  | 16393.2  | 69.4444 | 15     | 0      | 0     | 0      | 0           |
| 87    | 0   | -9077.34 | -552.925 | 60.3476 | 30     | 0      | 0     | 0      | 0           |

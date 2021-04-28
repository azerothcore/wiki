# player\_levelstats

[<-Back-to:World](database-world.md)

**The \`player\_levelstats\` table**

This table holds information on what stats are gained by characters when they level up. Each race-class combination has different level stats. All of the values in this table signify only the base stats of the race-class combination at a specific level.

**Structure**

| Field      | Type       | Attributes | Key | Null | Default | Extra | Comment |
|------------|------------|------------|-----|------|---------|-------|---------|
| [race][1]  | TINYINT(3) | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [class][2] | TINYINT(3) | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [level][3] | TINYINT(3) | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [str][4]   | TINYINT(3) | UNSIGNED   |     | NO   | NULL    |       |         |
| [agi][5]   | TINYINT(3) | UNSIGNED   |     | NO   | NULL    |       |         |
| [sta][6]   | TINYINT(3) | UNSIGNED   |     | NO   | NULL    |       |         |
| [inte][7]  | TINYINT(3) | UNSIGNED   |     | NO   | NULL    |       |         |
| [spi][8]   | TINYINT(3) | UNSIGNED   |     | NO   | NULL    |       |         |

[1]: #race
[2]: #class
[3]: #level
[4]: #str
[5]: #agi
[6]: #sta
[7]: #inte
[8]: #spi

**Description of the fields**

### race

The character race. This field along with [class](#player_levelstats-class) defines what stats to be applied on the character.
`ChrRaces.dbc`

### class

The character class. This field along with [race](#player_levelstats-race) defines what stats to be applied on the character.
`ChrClasses.dbc`

### level

The level at which the stats should be applied.

### str

The base strength of the character.

### agi

The base agility of the character.

### sta

The base stamina of the character.

### inte

The base intellect of the character.

### spi

The base spirit of the character.

### Examples

| race | class | level | str | agi | sta | inte | spi |
|------|-------|-------|-----|-----|-----|------|-----|
| 1    | 1     | 1     | 23  | 20  | 22  | 20   | 20  |
| 2    | 1     | 1     | 26  | 17  | 24  | 17   | 23  |
| 3    | 1     | 1     | 25  | 16  | 25  | 19   | 19  |
| 4    | 1     | 1     | 20  | 25  | 21  | 20   | 20  |
| 5    | 1     | 1     | 22  | 18  | 23  | 18   | 25  |
| 6    | 1     | 1     | 28  | 15  | 24  | 15   | 22  |
| 7    | 1     | 1     | 18  | 23  | 21  | 24   | 20  |
| 8    | 1     | 1     | 24  | 22  | 23  | 16   | 21  |
| 11   | 1     | 1     | 24  | 17  | 21  | 21   | 22  |

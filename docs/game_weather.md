# game\_weather

[<-Back-to:World](database-world)

**Table: game\_weather's Structure**

This table holds the percent chances for weather changes to occur in various zones. Not all zones can have their weather changed. For any given zone the percentage of all weather types for each season should total, and not exceed 100%.

| Field                     | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [zone][1]                 | INT      | UNSIGNED   | PRI | NO   | 0       |       |         |
| [spring_rain_chance][2]   | TINYINT  | UNSIGNED   |     | NO   | 25      |       |         |
| [spring_snow_chance][3]   | TINYINT  | UNSIGNED   |     | NO   | 25      |       |         |
| [spring_storm_chance][4]  | TINYINT  | UNSIGNED   |     | NO   | 25      |       |         |
| [summer_rain_chance][5]   | TINYINT  | UNSIGNED   |     | NO   | 25      |       |         |
| [summer_snow_chance][6]   | TINYINT  | UNSIGNED   |     | NO   | 25      |       |         |
| [summer_storm_chance][7]  | TINYINT  | UNSIGNED   |     | NO   | 25      |       |         |
| [fall_rain_chance][8]     | TINYINT  | UNSIGNED   |     | NO   | 25      |       |         |
| [fall_snow_chance][9]     | TINYINT  | UNSIGNED   |     | NO   | 25      |       |         |
| [fall_storm_chance][10]   | TINYINT  | UNSIGNED   |     | NO   | 25      |       |         |
| [winter_rain_chance][11]  | TINYINT  | UNSIGNED   |     | NO   | 25      |       |         |
| [winter_snow_chance][12]  | TINYINT  | UNSIGNED   |     | NO   | 25      |       |         |
| [winter_storm_chance][13] | TINYINT  | UNSIGNED   |     | NO   | 25      |       |         |
| [ScriptName][14]          | CHAR(64) |            |     | NO   | ''      |       |         |

[1]: #zone
[2]: #springrainchance
[3]: #springsnowchance
[4]: #springstormchance
[5]: #summerrainchance
[6]: #summersnowchance
[7]: #summerstormchance
[8]: #fallrainchance
[9]: #fallsnowchance
[10]: #fallstormchance
[11]: #winterrainchance
[12]: #wintersnowchance
[13]: #winterstormchance
[14]: #scriptname

**Description of the table's fields**

### zone

This field contains the zone id from the [AreaTable DBC file](areatable) that you wish to change the weather for.

### spring\_rain\_chance

Percent chance for rain in the Spring

### spring\_snow\_chance

Percentage chance for snow to occur in the Spring

### spring\_storm\_chance

Percent chance for a sand storm to occur in the Spring

### summer\_rain\_chance

Percent chance for rain to occur in the Summer

### summer\_snow\_chance

Percent chance for snow to occur in the Summer

### summer\_storm\_chance

Percent chance for a sand storm to occur in the Summer

### fall\_rain\_chance

Percent chance for rain to occur in the Fall

### fall\_snow\_chance

Percent chance for snow to occur in the Fall

### fall\_storm\_chance

Percent chance for a sand storm to occur in the Fall

### winter\_rain\_chance

Percentage chance for rain to occur in the Winter

### winter\_snow\_chance

Percentage chance for snow to occur in the Winter

### winter\_storm\_chance

Percentage chance for a sand storm to occur in the Winter

### ScriptName

Name of the script associated with this zone's weather, registered in the core to allow custom weather handling.

# game\_weather

[<-Back-to:World](database-world)

**Table Structure**

This table holds the percent chances for weather changes to occur in various zones. Not all zones can have their weather changed. For any given zone the percentage of all weather types for each season should total, and not exceed 100%.

| Field                     | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [zone][1]                 | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [spring_rain_chance][2]   | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [spring_snow_chance][3]   | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [spring_storm_chance][4]  | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [summer_rain_chance][5]   | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [summer_snow_chance][6]   | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [summer_storm_chance][7]  | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [fall_rain_chance][8]     | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [fall_snow_chance][9]     | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [fall_storm_chance][10]   | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [winter_rain_chance][11]  | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [winter_snow_chance][12]  | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [winter_storm_chance][13] | TINYINT   | UNSIGNED   |     | NO   |         |       |         |

[1]: #zone
[2]: #spring_rain_chance
[3]: #spring_snow_chance
[4]: #spring_storm_chance
[5]: #summer_rain_chance
[6]: #summer_snow_chance
[7]: #summer_storm_chance
[8]: #fall_rain_chance
[9]: #fall_snow_chance
[10]: #fall_storm_chance
[11]: #winter_rain_chance
[12]: #winter_snow_chance
[13]: #winter_storm_chance

**Field Descriptions**

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

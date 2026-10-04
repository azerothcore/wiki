# game\_weather

[<-Back-to:World](database-world)

**Table: game\_weather's Structure**

This table holds the percent chances for weather changes to occur in various zones. Not all zones can have their weather changed. For any given zone the percentage of all weather types for each season should total, and not exceed 100%.

| Field                                     | Type     |          | Null | Key | Default | Extra | Comment |
| :---------------------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [zone](#zone)                             | INT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [spring_rain_chance](#springrainchance)   | TINYINT  | UNSIGNED | NO   |     | 25      |       |         |
| [spring_snow_chance](#springsnowchance)   | TINYINT  | UNSIGNED | NO   |     | 25      |       |         |
| [spring_storm_chance](#springstormchance) | TINYINT  | UNSIGNED | NO   |     | 25      |       |         |
| [summer_rain_chance](#summerrainchance)   | TINYINT  | UNSIGNED | NO   |     | 25      |       |         |
| [summer_snow_chance](#summersnowchance)   | TINYINT  | UNSIGNED | NO   |     | 25      |       |         |
| [summer_storm_chance](#summerstormchance) | TINYINT  | UNSIGNED | NO   |     | 25      |       |         |
| [fall_rain_chance](#fallrainchance)       | TINYINT  | UNSIGNED | NO   |     | 25      |       |         |
| [fall_snow_chance](#fallsnowchance)       | TINYINT  | UNSIGNED | NO   |     | 25      |       |         |
| [fall_storm_chance](#fallstormchance)     | TINYINT  | UNSIGNED | NO   |     | 25      |       |         |
| [winter_rain_chance](#winterrainchance)   | TINYINT  | UNSIGNED | NO   |     | 25      |       |         |
| [winter_snow_chance](#wintersnowchance)   | TINYINT  | UNSIGNED | NO   |     | 25      |       |         |
| [winter_storm_chance](#winterstormchance) | TINYINT  | UNSIGNED | NO   |     | 25      |       |         |
| [ScriptName](#scriptname)                 | CHAR(64) |          | NO   |     | ''      |       |         |

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

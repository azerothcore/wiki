# game\_weather

[<-Volver a:World](database-world)

**Estructura**

Esta tabla contiene las probabilidades porcentuales de que ocurran cambios de clima en varias zonas. No todas las zonas pueden cambiar su clima. Para una zona dada, el porcentaje de todos los tipos de clima de cada estación debería sumar, y no exceder, el 100%.

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

**Descripción de los campos**

### zone

Este campo contiene el id de zona del [archivo AreaTable DBC](areatable) para la que quieres cambiar el clima.

### spring\_rain\_chance

Probabilidad porcentual de lluvia en primavera

### spring\_snow\_chance

Probabilidad porcentual de que nieve en primavera

### spring\_storm\_chance

Probabilidad porcentual de que ocurra una tormenta de arena en primavera

### summer\_rain\_chance

Probabilidad porcentual de que llueva en verano

### summer\_snow\_chance

Probabilidad porcentual de que nieve en verano

### summer\_storm\_chance

Probabilidad porcentual de que ocurra una tormenta de arena en verano

### fall\_rain\_chance

Probabilidad porcentual de que llueva en otoño

### fall\_snow\_chance

Probabilidad porcentual de que nieve en otoño

### fall\_storm\_chance

Probabilidad porcentual de que ocurra una tormenta de arena en otoño

### winter\_rain\_chance

Probabilidad porcentual de que llueva en invierno

### winter\_snow\_chance

Probabilidad porcentual de que nieve en invierno

### winter\_storm\_chance

Probabilidad porcentual de que ocurra una tormenta de arena en invierno

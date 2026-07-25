# pet\_name\_generation\_locale

[<-Volver a:World](database-world)

**Tabla \`pet\_name\_generation\_locale\`**

Esta tabla contiene fragmentos de nombres (primera y segunda mitad) que se usan para la generación de nombres de mascotas por localización.

**Estructura**

| Field       | Type      | Attributes | Key | Null | Default | Extra          | Comment |
| ----------- | --------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [ID][1]     | MEDIUMINT | UNSIGNED   | PRI | NO   | NULL    | Auto increment |         |
| [locale][2] | VARCHAR   |            |     | NO   |         |                |         |
| [word][3]   | tinytext  | SIGNED     |     | NO   | NULL    |                |         |
| [entry][4]  | MEDIUMINT | UNSIGNED   |     | NO   | 0       |                |         |
| [half][5]   | TINYINT   | SIGNED     |     | NO   | 0       |                |         |

[1]: #id
[2]: #locale
[3]: #word
[4]: #entry
[5]: #half

**Descripción de los campos**

### ID

El ID de la entrada. Este campo debe coincidir con [pet_name_generation.id](pet_name_generation#id)

### Locale

Este es el idioma del cliente.

| Language |
| -------- |
| koKR     |
| frFR     |
| deDE     |
| zhCN     |
| zhTW     |
| esES     |
| esMX     |
| ruRU     |

### word

La parte del nombre para esta entrada.

### entry

El entry de creature\_template.entry de la creature para la que quieres que se genere esta parte del nombre.

### half

Esto determina si esta es la primera o la segunda mitad del nombre para esta entrada.

-   0 Primera mitad
-   1 Segunda mitad

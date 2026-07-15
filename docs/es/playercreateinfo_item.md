# playercreateinfo\_item

[<-Volver a:World](database-world)

**Tabla \`playercreateinfo\_item\`**

Esta tabla se usa para cualquier item personalizado que quieras dar a los personajes al crearlos. Antes se usaba también para contener los items normales que reciben los personajes, pero ahora esa información se lee de CharStartOutfit.dbc

**Estructura**

| Field       | Type      | Attributes | Key  | Null | Default | Extra | Comment |
| :---------- | :-------- | :--------- | :--- | :--- | :------ | :---- | :------ |
| [race][1]   | TINYINT   | UNSIGNED   | PRI  | NO   | 0       |       |         |
| [class][2]  | TINYINT   | UNSIGNED   | PRI  | NO   | 0       |       |         |
| [itemid][3] | MEDIUMINT | UNSIGNED   | PRI  | NO   | 0       |       |         |
| [amount][4] | SMALLINT  | UNSIGNED   |      | NO   | 1       |       |         |
| [Note][5]   | VARCHAR   |            |      | YES  | NULL    |       |         |

[1]: #race
[2]: #class
[3]: #itemid
[4]: #amount
[5]: #Note

**Descripción de los campos**

### race

La raza del personaje.
`:ChrRaces.dbc_tc2`

### class

La clase del personaje.
`:ChrClasses.dbc_tc2`

### itemid

El ID de plantilla del item. Ver item\_template.entry

### amount

El número de copias de ese item.

### Note

Nota de la entrada

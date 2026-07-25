# pet\_name\_generation

[<-Volver a:World](database-world)

**Tabla \`pet\_name\_generation\`**

Esta tabla contiene fragmentos de nombres (primera y segunda mitad) que se usan para la generación de nombres de mascotas.

**Estructura**

| Field      | Type      | Attributes | Key | Null | Default | Extra          | Comment |
| ---------- | --------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [id][1]    | MEDIUMINT | UNSIGNED   | PRI | NO   | NULL    | Auto increment |         |
| [word][2]  | tinytext  | SIGNED     |     | NO   | NULL    |                |         |
| [entry][3] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |                |         |
| [half][4]  | TINYINT   | SIGNED     |     | NO   | 0       |                |         |

[1]: #id
[2]: #word
[3]: #entry
[4]: #half

**Descripción de los campos**

### id

El ID de la entrada. Este es un campo auto increment y es un número arbitrario. Al añadir entradas es mejor dejar que la base de datos elija el siguiente número de ID disponible.

### word

La parte del nombre para esta entrada.

### entry

El entry de creature\_template.entry de la creature para la que quieres que se genere esta parte del nombre.

### half

Esto determina si esta es la primera o la segunda mitad del nombre para esta entrada.

-   0 Primera mitad
-   1 Segunda mitad

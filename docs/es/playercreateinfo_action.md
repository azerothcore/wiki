# playercreateinfo\_action

[<-Volver a:World](database-world)

**Tabla \`playercreateinfo_action\`**

Esta tabla contiene información sobre qué acciones por defecto debería tener un personaje recién creado al empezar. Cada combinación raza-clase puede tener una configuración inicial por defecto distinta.

**Estructura**

| Field       | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [race][1]   | TINYINT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [class][2]  | TINYINT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [button][3] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [action][4] | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [type][5]   | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #race
[2]: #class
[3]: #button
[4]: #action
[5]: #type

**Descripción de los campos**

### race

La [raza](ChrRaces#content) del personaje.

### class

La [clase](ChrClasses#content) del personaje.

### button

El ID del slot en la barra de acciones donde se colocará el icono de la acción.

Las barras especiales se usan para posturas, auras, mascotas, sigilo y otros modos especiales similares.

| Button IDs | Set (key)                          |
| ---------- | ---------------------------------- |
| 0-11       | 1 (SHIFT + 1)                      |
| 12-23      | 2 (SHIFT + 2)                      |
| 24-35      | 3 (SHIFT + 3) h1. Right Side Bar   |
| 36-47      | 4 (SHIFT + 4) Right Side Bar 2     |
| 48-59      | 5 (SHIFT + 5) h1. Bottom Right Bar |
| 60-71      | 6 (SHIFT + 6) Bottom Left Bar      |
| 72-83      | 1 SpecialA                         |
| 84-95      | 1 SpecialB                         |
| 96-107     | 1 SpecialC                         |
| 108-119    | 1 SpecialD                         |

### action

Dependiendo del valor de type, este puede ser el [ID del spell](Spell#id), el [ID del item](item_template#entry) o el ID de la macro.

### type

El tipo de acción:

| ID  | Type  |
| --- | ----- |
| 0   | Spell |
| 64  | Macro |
| 128 | Item  |

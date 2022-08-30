# character\_equipmentsets

[<-Volver a:Characters](database-characters.md)

**Tabla \`character\_equipmentsets\`**

La tabla alberga información acerca de la configuración del Gestor de Equipamiento del jugador.

**Estructura**

| Field            | Type         | Attributes | Key | Null | Default | Extra          | Comment |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | -------------- | ------- |
| [guid][1]        | INT          | SIGNED     |     | NO   |         | UNIQUE         |         |
| [setguid][2]     | BIGINT       | SIGNED     | PRI | NO   |         | UNIQUE         |         |
| [setindex][3]    | TINYINT      | UNSIGNED   |     | NO   |         | UNIQUE         |         |
| [name][4]        | VARCHAR(31)  | SIGNED     |     | NO   |         |                |         |
| [iconname][5]    | VARCHAR(100) | SIGNED     |     | NO   |         |                |         |
| [ignore_mask][6] | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item0][7]       | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item1][8]       | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item2][9]       | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item3][10]      | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item4][11]      | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item5][12]      | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item6][13]      | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item7][14]      | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item8][15]      | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item9][16]      | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item10][17]     | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item11][18]     | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item12][19]     | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item13][20]     | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item14][21]     | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item15][22]     | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item16][23]     | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item17][24]     | INT          | UNSIGNED   |     | NO   |         |                |         |
| [item18][25]     | INT          | UNSIGNED   |     | NO   |         |                |         |

[1]: #guid
[2]: #setguid
[3]: #setindex
[4]: #name
[5]: #iconname
[6]: #ignoremask
[7]: #item
[8]: #item
[9]: #item
[10]: #item
[11]: #item
[12]: #item
[13]: #item
[14]: #item
[15]: #item
[16]: #item
[17]: #item
[18]: #item
[19]: #item
[20]: #item
[21]: #item
[22]: #item
[23]: #item
[24]: #item
[25]: #item

**Descripción de los Campos**

### guid

GUID o identificador Global Único del jugador. Véase [characters.guid](characters#guid).

### setguid

Primer GUID o identificador Global Único libre del Gestor de Equipamiento.

### setindex

Establece la casilla del Item, para esto son usados los valores del 0 al 9.

### name

El nombre lo asigna el propio jugador.

### iconname

Nombre tomado de [ItemDisplayInfo.dbc](ItemDisplayInfo.dbc), columna número 6.

### ignore\_mask

`field-no-description|6` (¿Máscara de bits acaso?)

### item

Valores tomados de [item\_instance.guid](item_instance#guid).

| ID | Name           |
| -- | -------------- |
| 0  | Cabeza         |
| 1  | Cuello         |
| 2  | Hombros        |
| 3  | Camisa         |
| 4  | Pecho          |
| 5  | Cinturón       |
| 6  | Piernas        |
| 7  | Pies           |
| 8  | Muñecas        |
| 9  | Manos          |
| 10 | Anillo 1       |
| 11 | Anillo 2       |
| 12 | Abalorio 1     |
| 13 | Abalorio 2     |
| 14 | Espalda        |
| 15 | Mano principal |
| 16 | Segunda mano   |
| 17 | Reliquia       |
| 18 | Tabardo        |

Recordemos que son en total 19 columnas con este mismo nombre, en cada una de ellas se asigna el GUID o Identificador Global único del Item extraído desde [item\_instance.guid](item_instance#guid), no de [item_template](item_template#entry).
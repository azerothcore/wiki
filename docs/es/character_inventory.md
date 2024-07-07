# character\_inventory

[<-Volver a:Characters](database-characters)

**Tabla \`character\_inventory\`**

Alberga todos los datos del inventario del personaje, incluyendo los datos del banco.

**Estructura**

| Field     | Type    | Attributes | Key    | Null | Default | Extra | Comment                       |
| --------- | ------- | ---------- | ------ | ---- | ------- | ----- | ----------------------------- |
| [guid][1] | INT     | UNSIGNED   | Unique | NO   | 0       |       | Global Unique Identifier      |
| [bag][2]  | INT     | UNSIGNED   |        | NO   | 0       |       |                               |
| [slot][3] | TINYINT | UNSIGNED   |        | NO   | 0       |       |                               |
| [item][4] | INT     | UNSIGNED   | PRI    | NO   | 0       |       | Item Global Unique Identifier |

[1]: #guid
[2]: #bag
[3]: #slot
[4]: #item

**Descripción de los Campos**

### guid

GUID o Identificador Global Único del personaje. Véase [characters.guid](characters#guid).

### bag

En caso de que éste campo no sea el número '0', entonces el valor vendría a ser el GUID (Identificador Global Único) del Item de la bolsa en cuestión. Véase [item\_instance.guid](item_instance#guid).

### slot

En caso de que el campo de la bolsa sea distinto de '0', la ranura es la misma ranura de la bolsa en donde se encuentra almacenado el Item. El rango puede variar en función del número de ranuras que tenga la bolsa.

Luego, si el campo de la bolsa es el número '0', la ranura tiene un rango del 0 al 130 y el o los valores pueden representar lo siguiente:

| Ranura    | Valor                                       |
| --------- | ------------------------------------------- |
| 0         | Cabeza                                      |
| 1         | Cuello                                      |
| 2         | Hombros                                     |
| 3         | Camisa                                      |
| 4         | Pecho                                       |
| 5         | Cinturón                                    |
| 6         | Piernas                                     |
| 7         | Pies                                        |
| 8         | Muñecas                                     |
| 9         | Manos                                       |
| 10        | Anillo 1                                    |
| 11        | Anillo 2                                    |
| 12        | Abalorio 1                                  |
| 13        | Abalorio 2                                  |
| 14        | Espalda                                     |
| 15        | Mano principal                              |
| 16        | Segunda mano                                |
| 17        | A distancia                                 |
| 18        | Tabardo                                     |
| 19-22     | Bolsas Equipadas                            |
| 23-38     | Mochila principal                           |
| 39-66     | Banco principal                             |
| 67-73     | Bolsas del banco                            |
| 86-117    | Llaves en el llavero                        |
| 118-135   | Monedas (Emblemas, distintivos,marcas etc.) |

### item

GUID o Identificador Global Único del Item. Véase [item\_instance.guid](item_instance#guid).

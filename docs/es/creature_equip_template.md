# creature\_equip\_template

[<-Volver a: World](database-world)

## **Tabla: creature\_equip\_template**

Esta tabla contiene todas las combinaciones de equipamiento que se pueden enviar para cada criatura.

## Estructura

| Field           | Type      | Attributes | Key | Null | Default | Extra | Comment      |
| --------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------------ |
| [CreatureID][1] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Unique entry |
| [ID][2]         | TINYINT   | UNSIGNED   | PRI | NO   | 1       |       | Unique entry |
| [ItemID1][3]    | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |              |
| [ItemID2][4]    | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |              |
| [ItemID3][5]    | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |              |

[1]: #creatureid
[2]: #id
[3]: #itemid1
[4]: #itemid2
[5]: #itemid3

## Descripción de los campos

### CreatureID

El [id](creature#id) directo correspondiente en la tabla [creature](creature) o el [entry](creature_template#entry) en la tabla [creature\_template](creature_template).

### ID

Un identificador adicional para cada registro individual, que permite varios equipamientos para una misma criatura. El contador **debe** empezar en 1 y crecer en consecuencia.

### ItemID1

Este es el número de item del equipamiento usado en la mano derecha, de [Item.dbc](item).

### ItemID2

Este es el número de item del equipamiento usado en la mano izquierda, de [Item.dbc](item).

### ItemID3

Este es el número de item del equipamiento usado en la ranura de distancia, de [Item.dbc](item).

# creature\_equip\_template

[<-Volver a:World](database-world)

## **Tabla creature\_equip\_template**

Esta tabla contiene todas las combinaciones de equipo que se pueden enviar para cada criatura.

**Estructura**

| Campo           | Tipo      | Atributos | Llave | Nulo | Por defecto | Extra | Comentario    |
| --------------- | --------- | --------- | ----- | ---- | ----------- | ----- | ------------- |
| [CreatureID][1] | MEDIUMINT | UNSIGNED  | PRI   | NO   | 0           |       | Entrada única |
| [ID][2]         | TINYINT   | UNSIGNED  | PRI   | NO   | 1           |       | Entrada única |
| [ItemID1][3]    | MEDIUMINT | UNSIGNED  |       | NO   | 0           |       |               |
| [ItemID2][4]    | MEDIUMINT | UNSIGNED  |       | NO   | 0           |       |               |
| [ItemID3][5]    | MEDIUMINT | UNSIGNED  |       | NO   | 0           |       |               |

[1]: #creatureid
[2]: #id
[3]: #itemid1
[4]: #itemid2
[5]: #itemid3

## Descripción de los campos

### CreatureID

El [id](http://www.azerothcore.org/wiki/creature#id) directo correspondiente en la tabla [creature](creature) o la [entrada](http://www.azerothcore.org/wiki/creature_template#creature_template-entry) en la tabla [creature\_template](creature_template).

### ID

Un identificador adicional para cada entrada individual, lo que permite varios equipos para una entrada de criatura. El contador **debe** comenzar con 1 y crecer en consecuencia.

### ItemID1

Este es el número de artículo del equipo utilizado en la mano derecha de [Item.dbc](Item).

### ItemID2

Este es el número de artículo del equipo utilizado en la mano izquierda de [Item.dbc](Item).

### ItemID3

Este es el número de artículo del equipo utilizado en la ranura a distancia de [Item.dbc](Item).

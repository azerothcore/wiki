# npc\_vendor

[<-Volver a: World](database-world)

## Información general

Esta tabla contiene los datos de vendedor de todos los NPC que venden objetos o monedas. Un vendedor solo puede tener hasta 150 objetos (15 páginas); está hardcodeado en el emulador y si lo cambias, el cliente se bloqueará (crash).

### Precios

El precio (en oro) de cada objeto o moneda se define en la entrada relacionada de su item template como [item_template.BuyPrice](item_template#buyprice).
Los costes especiales (honor, tokens, etc...) se definen en esta tabla en la columna [ExtendedCost](#extendedcost).

### Modo GM

Si abres la ventana del vendedor en modo GM, verás todos los objetos que vende el vendedor. Si deshabilitas el modo GM, verás los objetos vendidos como un jugador normal (ej: si no puedes usar un objeto y no puedes comerciar con él, no lo verás listado).


## Estructura

| Field             | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]        | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [slot][2]         | SMALLINT  | SIGNED     |     | NO   | 0       |       |         |
| [item][3]         | MEDIUMINT | SIGNED     | PRI | NO   | 0       |       |         |
| [maxcount][4]     | TINYINT   | UNSIGNED   |     | NO   | 0       |       |         |
| [incrtime][5]     | INT       | UNSIGNED   |     | NO   | 0       |       |         |
| [ExtendedCost][6] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |

[1]: #entry
[2]: #slot
[3]: #item
[4]: #maxcount
[5]: #incrtime
[6]: #extendedcost


## Descripción de los campos

### entry

El ID de la criatura. Ver [creature\_template.entry](creature_template#entry).

### slot

Posición del objeto cuando se abre la ventana del vendedor. Empieza desde 0 hasta x, de arriba abajo y de izquierda a derecha.
*Nota: si tienes una lista de objetos en el slot 0, y editas uno de ellos para que esté en el slot 1 o cualquier número, ese objeto siempre estará al final porque todos los demás objetos están en el slot 0.*

### item

El ID del objeto. Ver [item\_template.entry](item_template#entry).

### maxcount

El número máximo de objetos que lleva el vendedor en cualquier momento. Si quieres que el vendedor lleve un número ilimitado del objeto, entonces pon esto a **0**; si no, ponlo a cualquier número positivo. En la imagen de abajo el valor maxcount está rodeado.

### incrtime

Combinado con [maxcount](#maxcount), este campo indica cada cuánto (en segundos) se refresca la lista del vendedor y se reabastecen las copias limitadas del objeto. Para las copias limitadas del objeto, en cada refresco la cantidad se incrementa en [item\_template.BuyCount](item_template#buycount) .

### ExtendedCost

El valor aquí corresponde al ID en [ItemExtendedCost.dbc](itemextendedcost_dbc#id) y ese ID controla el precio no monetario del objeto, ya sean puntos de honor, puntos de arena, distintos tipos de insignias o cualquier combinación de los anteriores.

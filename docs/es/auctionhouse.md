# auctionhouse

[<-Volver a:Characters](database-characters.md)

**Tabla \`auctionhouse\`**

Alberga toda la información acerca de las subastas en curso dentro del mundo. Controla qué Items son subastados y quién los subasta, quién tiene la mayor puja del mismo, etc.

**Estructura**

| Field               | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]             | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [houseid][2]        | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [itemguid][3]       | INT  | UNSIGNED   | UNI | NO   | 0       |       |         |
| [itemowner][4]      | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [buyoutprice][5]    | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [time][6]           | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [buyguid][7]        | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [lastbid][8]        | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [startbid][9]       | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [deposit][10]       | INT  | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #id
[2]: #houseid
[3]: #itemguid
[4]: #itemowner
[5]: #buyoutprice
[6]: #time
[7]: #buyguid
[8]: #lastbid
[9]: #startbid
[10]: #deposit

**Descripción de los Campos**

### id

Identificador único para cada subasta existente.

### houseid

GUID o Identificador Global Único de aquella criatura a la que se añadió cierto Item dentro de la casa de subastas. Véase [creature.guid](creature#guid).

### itemguid

GUID Identificador Global Único (NO ID o Entry del Item) que fue puesto en venta en la casa de subastas. Véase [item\_instance.guid](item_instance#guid).

### itemowner

GUID del propietario (jugador) del Item subastado. Véase [characters.guid](characters#guid).

### buyoutprice

Precio de compra del Item medido en monedas de cobre. Divide por 100 para obtener plata y por 100 de nuevo para obtener oro.

Ejemplo:

23 de oro (230000 en monedas de cobre).

7 de plata (700 en monedas de cobre)

### time

Hora de finalización de la subasta, medido en [Tiempo Unix](https://es.wikipedia.org/wiki/Tiempo_Unix) (Número de segundos desde las 00:00 del 1 de enero de 1970).

### buyguid

GUID del personaje que posea la mayor puja por el Item en cuestión. Véase [characters.guid](characters#guid).

### lastbid

Cantidad de dinero medido en monedas de cobre de la última puja hecha por el Item.

### startbid

Cantidad de dinero medido en monedas de cobre de la puja inicial por el Item.

### deposit

Cantidad de dinero medido en monedas de cobre gastada en el depósito.

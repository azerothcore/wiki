# character\_homebind

[<-Volver a:Characters](database-characters)

**Tabla \`character\_homebind\`**

Alberga información acerca de la ubicación hacia la que son teletransportados los personajes de los jugadores cuando utilizan su Piedra de Hogar.

**Estructura**

| Campo       | Tipo        | Atributos | Llave | Nulo | Por defecto | Extra | Comentario                 |
| ----------- | ----------- | --------- | ----- | ---- | ----------- | ----- | -------------------------- |
| [guid][1]   | INT         | UNSIGNED  | PRI   | NO   | 0           |       | Identificador único global |
| [mapId][2]  | SMALLINT    | UNSIGNED  |       | NO   | 0           |       | Identificador de mapa      |
| [zoneId][3] | SMALLINT    | UNSIGNED  |       | NO   | 0           |       | Identificador de zona      |
| [posX][4]   | FLOAT       | SIGNED    |       | NO   | 0           |       |                            |
| [posY][5]   | FLOAT       | SIGNED    |       | NO   | 0           |       |                            |
| [posZ][6]   | FLOAT       | SIGNED    |       | NO   | 0           |       |                            |

[1]: #guid
[2]: #mapid
[3]: #zoneid
[4]: #posx
[5]: #posy
[6]: #posz

**Descripción de los Campos**

### guid

GUID o Identificador Global Único del personaje. Véase [characters.guid](characters#guid).

### mapId

ID del mapa hacia el que es teletransportado el personaje. Véase [Map.dbc](map) columna número 1.

### zoneId

ID de la zona hacia la que es teletransportado el personaje. Véase [AreaTable.dbc](areatable) columna número 1.

### posX

Posición cartesiana en X hacia la que es teletransportado el personaje.

### posY

Posición cartesiana en Y hacia la que es teletransportado el personaje.

### posZ

Posición cartesiana en Z hacia la que es teletransportado el personaje.

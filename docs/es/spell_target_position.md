# spell\_target\_position

[<-Volver a: World](database-world)

**Tabla \`spell\_target\_position\`**

Esta tabla contiene la información de coordenadas de a dónde debe teletransportarse el jugador cuando un hechizo tiene el tipo de objetivo: TARGET\_DST\_DB(17).

**Estructura**

| Field                   | Type      | Attributes | Key | Null | Default | Extra | Comment    |
| ----------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------- |
| [id][1]                 | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Identifier |
| [target_map][2]         | SMALLINT  | UNSIGNED   |     | NO   | 0       |       |            |
| [target_position_x][3]  | FLOAT     | SIGNED     |     | NO   | 0       |       |            |
| [target_position_y][4]  | FLOAT     | SIGNED     |     | NO   | 0       |       |            |
| [target_position_z][5]  | FLOAT     | SIGNED     |     | NO   | 0       |       |            |
| [target_orientation][6] | FLOAT     | SIGNED     |     | NO   | 0       |       |            |

[1]: #id
[2]: #targetmap
[3]: #targetpositionx
[4]: #targetpositiony
[5]: #targetpositionz
[6]: #targetorientation

**Descripción de los campos**

### id

El ID del hechizo. Ver [Spell.dbc](spell)

### target\_map

Mapa al que debe teletransportarse el jugador. Ver [Map.dbc](map).

### target\_position\_x

Coordenada X del destino objetivo del hechizo.

### target\_position\_y

Coordenada Y del destino objetivo del hechizo.

### target\_position\_z

Coordenada Z del destino objetivo del hechizo.

### target\_orientation

Orientación que tendrá el jugador al aparecer en esta ubicación

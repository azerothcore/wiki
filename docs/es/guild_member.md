# guild\_member

[<-Volver a:Characters](database-characters.md)

**Tabla \`guild\_member\`**

La tabla alberga información sobre los miembros de todas las hermandades, sus rangos en la hermandad respectiva y cualquier nota creada por ellos o por los oficiales de la hermandad.

**Estructura**

| Field        | Type        | Attributes | Key    | Null | Default | Extra | Comment             |
| ------------ | ----------- | ---------- | ------ | ---- | ------- | ----- | ------------------- |
| [guildid][1] | INT         | UNSIGNED   |        | NO   |         |       | Guild Identificator |
| [guid][2]    | INT         | UNSIGNED   | Unique | NO   |         |       |                     |
| [rank][3]    | TINYINT     | UNSIGNED   |        | NO   |         |       |                     |
| [pnote][4]   | VARCHAR(31) | SIGNED     |        | NO   |         |       |                     |
| [offnote][5] | VARCHAR(31) | SIGNED     |        | NO   |         |       |                     |

[1]: #guildid
[2]: #guid
[3]: #rank
[4]: #pnote
[5]: #offnote

**Descripción de los Campos**

### guildid

ID de la hermandad en la cual es parte el jugador. Véase [guild.guildid](guild#guildid).

### guid

GUID del jugador respectivo. Véase [characters.guid](characters#guid).

### rank

El rango que el jugador posée dentro de la hermandad. Véase [guild\_rank.rid](Guild_rank#rid).

### pnote

La nota creada por el jugador, la cual que puede ser leída por los demás miembros.

### offnote

La nota establecida por los oficiales de hermandad, la cual sólo puede ser leída por otros oficiales de la misma.

# item\_soulbound\_trade\_data

[<-Volver a:Characters](database-characters.md)

**Tabla \`item\_soulbound\_trade\_data**

Esta tabla almacena información sobre qué jugadores pueden intercambiar artículos ligados al alma entre ellos.

**Estructura**

| Field              | Type | Attributes | Key | Null | Default | Extra  | Comment                                                                 |
| ------------------ | ---- | ---------- | --- | ---- | ------- | ------ | ----------------------------------------------------------------------- |
| [itemGuid][1]      | INT  | UNSIGNED   | PRI | NO   |         |        | Item GUID                                                               |
| [alowedPlayers][2] | TEXT | SIGNED     |     | NO   |         |        | Space separated GUID list of players who can receive this item in trade |

[1]: #itemguid
[2]: #alowedplayers

**Descripción de los campos**

### itemGuid

El GUID del artículo que se puede comercializar. Consulte [item\_instance.guid](item_instance#guid).

### alowedPlayers

GUID de jugadores elegibles para el intercambio separados por espacio. Consulte [characters.guid](characters#guid).

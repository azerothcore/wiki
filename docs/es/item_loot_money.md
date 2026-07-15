# item\_loot\_money

[<-Volver a: Characters](database-characters)

**Tabla \`item\_loot\_money\`**

Contiene el dinero asociado a un objeto de inventario saqueable
como una "Fat Sack of Coins".

Esta tabla se rellena la primera vez que el jugador hace click derecho para abrir un objeto. Las filas se eliminan cuando
el jugador retira el dinero o destruye el objeto contenedor.

**Estructura**

| Field             | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [container_id][1] | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [money][2]        | INT  | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #container_id
[2]: #money

**Descripción de los campos**

### container\_id

El GUID del objeto contenedor. Ver item\_instance.guid

### money

La cantidad de dinero saqueado, en cobre.

# petition

[<-Volver a:Characters](database-characters.md)

Leer en: [English :gb:](../petition) [Spanish :es:](petition)

**Tabla \`petition\`**

Esta tabla contiene información sobre todas las peticiones en curso para un hermandad o un equipo de arena.

**Estructura**

| Field             | Type        | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ownerguid][1]    | INT         | UNSIGNED   | PRI | NO   |         |       |         |
| [petitionguid][2] | INT         | UNSIGNED   |     | YES  | 0       |       |         |
| [name][3]         | VARCHAR(24) | SIGNED     |     | NO   |         |       |         |
| [type][4]         | TINYINT     | UNSIGNED   | PRI | NO   | 0       |       |         |

[1]: #ownerguid
[2]: #petitionguid
[3]: #name
[4]: #type

**Descripción de los campos**

### ownerguid

GUID del propietario de la petición. Ver [characters.guid](characters#guid).

### petitionguid

El GUID del elemento de la petición. Ver [item\_instance.guid](item_instance#guid).

### name

El nombre del hermandad o equipo de arena para el que el jugador intenta solicitar las peticiones.

### type

El tipo de petición.

| ID | Type               |
|--- | ------------------ |
| 2  | 2vs2 Arena charter |
| 3  | 3vs3 Arena charter |
| 5  | 5vs5 Arena charter |
| 9  | Guild charter      |

# petition\_sign

[<-Volver a:Characters](database-characters)

Leer en: [English :gb:](../petition_sign) [Spanish :es:](petition_sign)

**Tabla \`petition\_sign\`**

Esta tabla contiene información sobre todas las firmas de una petición para un hermandad o un equipo de arena.

**Estructura**

| Field               | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ownerguid][1]      | INT     | UNSIGNED   |     | NO   |         |       |         |
| [petitionguid][2]   | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [playerguid][3]     | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [player_account][4] | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [type][5]           | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #ownerguid
[2]: #petitionguid
[3]: #playerguid
[4]: #playeraccount
[5]: #type

**Descripción de los campos**

### ownerguid

El GUID del propietario que intenta formar parte del equipo del hermandad/arena. Ver [characters.guid](characters#guid).

### petitionguid

El GUID del artículo de la carta. Ver [item\_template.guid](item_template#guid).

### playerguid

El GUID del jugador que ha firmado la carta. Ver [characters.guid](characters#guid).

### player\_account

El ID de cuenta del jugador que ha firmado la carta. No hay dos jugadores que puedan firmar la misma carta desde la misma cuenta.

### type

El tipo de petición.

| ID | Type               |
|--- | ------------------ |
| 2  | 2vs2 Arena charter |
| 3  | 3vs3 Arena charter |
| 5  | 5vs5 Arena charter |
| 9  | Guild charter      |

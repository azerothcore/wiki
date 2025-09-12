# account\_access

[<- Volver a: Auth](database-auth)

**Tabla \`account\_access\`**

Esta tabla contiene el nivel de acceso de seguridad para cualquier reino en la tabla [realmlist](realmlist).

**Estructura**

| Field        | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------ | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]      | INT          | UNSIGNED   | PRI | NO   |         |       |         |
| [gmlevel][2] | TINYINT      | UNSIGNED   |     | NO   |         |       |         |
| [RealmID][3] | INT          | SIGNED     | PRI | NO   | -1      |       |         |
| [comment][4] | VARCHAR(255) | SIGNED     |     | YES  | ''      |       |         |

[1]: #id
[2]: #gmlevel
[3]: #realmid
[4]: #comment

**Descripción de los campos**

### id

El [ID de la cuenta](account#id).

### gmlevel

El nivel de seguridad de la cuenta. Los diferentes niveles tienen acceso a diferentes comandos. El nivel individual requerido para un comando se define en la tabla [command](command) en cada reino.

### RealmID

El [ID del reino](realmlist#id).

### comment

# rbac\_default\_permissions

[<-Volver a:Auth](database-auth)

**Tabla \`rbac\_default\_permissions\`**

Esta tabla mapea los niveles de seguridad de [account_access.gmlevel](account_access#gmlevel) a roles RBAC predeterminados. Cuando un jugador inicia sesión, su nivel de seguridad determina qué rol recibe automáticamente.

Para una visión general del sistema, consulta [RBAC](rbac).

**Estructura**

| Field             | Type    | Attributes | Key | Null | Default | Extra | Comment                  |
| ----------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [secId](#secid)               | INT     | UNSIGNED   | PRI | NO   |         |       | Security Level id        |
| [permissionId](#permissionid) | INT     | UNSIGNED   | PRI | NO   |         |       | Permission id            |
| [realmId](#realmid)           | INT     | SIGNED     | PRI | NO   | -1      |       | Realm Id, -1 means all   |

El campo `permissionId` tiene una clave foránea a [rbac_permissions.id](rbac_permissions#id).

**Descripción de los campos**

### secId

El nivel de seguridad de [account_access.gmlevel](account_access#gmlevel).

### permissionId

El permiso (rol) RBAC a conceder por defecto para este nivel de seguridad. Las asignaciones predeterminadas son:

| secId | permissionId | Role |
| ----- | ------------ | ---- |
| 0 | 195 | Player |
| 1 | 194 | Moderator |
| 2 | 193 | Gamemaster |
| 3 | 192 | Administrator |

Como los roles se encadenan a través de [rbac_linked_permissions](rbac_linked_permissions), conceder Administrator (192) incluye automáticamente los permisos de Gamemaster, Moderator y Player.

### realmId

El [ID del realm](realmlist#id) al que se aplica este predeterminado. Usa `-1` para aplicarlo a todos los realms.

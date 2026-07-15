# rbac\_account\_permissions

[<-Volver a:Auth](database-auth)

**Tabla \`rbac\_account\_permissions\`**

Esta tabla almacena las sobrescrituras de permisos por cuenta. Úsala para conceder o denegar permisos concretos a cuentas individuales, más allá de lo que proporciona su nivel de seguridad predeterminado.

Para una visión general del sistema, consulta [RBAC](rbac).

**Estructura**

| Field             | Type       | Attributes | Key | Null | Default | Extra | Comment                  |
| ----------------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [accountId](#accountid)       | INT        | UNSIGNED   | PRI | NO   |         |       | Account id               |
| [permissionId](#permissionid) | INT        | UNSIGNED   | PRI | NO   |         |       | Permission id            |
| [granted](#granted)           | TINYINT(1) | SIGNED     |     | NO   | 1       |       | Granted = 1, Denied = 0  |
| [realmId](#realmid)           | INT        | SIGNED     | PRI | NO   | -1      |       | Realm Id, -1 means all   |

El campo `accountId` tiene una clave foránea a [account.id](account#id) con `ON DELETE CASCADE`.
El campo `permissionId` tiene una clave foránea a [rbac_permissions.id](rbac_permissions#id) con `ON DELETE CASCADE`.

**Descripción de los campos**

### accountId

El [ID de la cuenta](account#id).

### permissionId

El ID del permiso de [rbac_permissions](rbac_permissions). Puede ser un permiso individual o un rol. Conceder/denegar un rol afecta a todos los permisos enlazados a él.

### granted

Controla si esta entrada es una concesión o una denegación:

| Value | Significado |
| ----- | ------- |
| 1 | **Grant** — añade este permiso a la cuenta |
| 0 | **Deny** — quita este permiso (y sus permisos enlazados) de la cuenta |

Durante la [resolución de permisos](rbac#permission-resolution), las denegaciones se restan de las concesiones tras la expansión. Esto significa que denegar un rol deniega todo lo que ese rol contiene.

### realmId

El [ID del realm](realmlist#id) al que se aplica esta sobrescritura. Usa `-1` para aplicarla a todos los realms.

Estas sobrescrituras se pueden gestionar dentro del juego con los [comandos .rbac](rbac#commands).

# rbac\_account\_permissions

[<-Back-to:Auth](database-auth)

**The \`rbac\_account\_permissions\` table**

This table stores per-account permission overrides. Use it to grant or deny specific permissions to individual accounts, beyond what their default security level provides.

For a system overview, see [RBAC](rbac).

**Table Structure**

| Field             | Type       | Attributes | Key | Null | Default | Extra | Comment                  |
| ----------------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [accountId](#accountid)       | INT        | UNSIGNED   | PRI | NO   |         |       | Account id               |
| [permissionId](#permissionid) | INT        | UNSIGNED   | PRI | NO   |         |       | Permission id            |
| [granted](#granted)           | TINYINT(1) | SIGNED     |     | NO   | 1       |       | Granted = 1, Denied = 0  |
| [realmId](#realmid)           | INT        | SIGNED     | PRI | NO   | -1      |       | Realm Id, -1 means all   |

The `accountId` field has a foreign key to [account.id](account#id) with `ON DELETE CASCADE`.
The `permissionId` field has a foreign key to [rbac_permissions.id](rbac_permissions#id) with `ON DELETE CASCADE`.

**Description of the fields**

### accountId

The [account ID](account#id).

### permissionId

The permission ID from [rbac_permissions](rbac_permissions). This can be an individual permission or a role. Granting/denying a role affects all permissions linked to it.

### granted

Controls whether this entry is a grant or a deny:

| Value | Meaning |
| ----- | ------- |
| 1 | **Grant** — adds this permission to the account |
| 0 | **Deny** — removes this permission (and its linked permissions) from the account |

During [permission resolution](rbac#permission-resolution), denies are subtracted from grants after expansion. This means denying a role denies everything that role contains.

### realmId

The [realm ID](realmlist#id) this override applies to. Use `-1` to apply to all realms.

These overrides can be managed in-game with the [.rbac commands](rbac#commands).

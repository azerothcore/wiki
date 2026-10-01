# rbac\_default\_permissions

[<-Back-to:Auth](database-auth)

**The \`rbac\_default\_permissions\` table**

This table maps [account_access.gmlevel](account_access#gmlevel) security levels to default RBAC roles. When a player logs in, their security level determines which role they receive automatically.

For a system overview, see [RBAC](rbac).

**Table Structure**

| Field             | Type    | Attributes | Key | Null | Default | Extra | Comment                  |
| ----------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [secId](#secid)               | INT     | UNSIGNED   | PRI | NO   |         |       | Security Level id        |
| [permissionId](#permissionid) | INT     | UNSIGNED   | PRI | NO   |         |       | Permission id            |
| [realmId](#realmid)           | INT     | SIGNED     | PRI | NO   | -1      |       | Realm Id, -1 means all   |

The `permissionId` field has a foreign key to [rbac_permissions.id](rbac_permissions#id).

**Description of the fields**

### secId

The security level from [account_access.gmlevel](account_access#gmlevel).

### permissionId

The RBAC permission (role) to grant by default for this security level. The default assignments are:

| secId | permissionId | Role |
| ----- | ------------ | ---- |
| 0 | 195 | Player |
| 1 | 194 | Moderator |
| 2 | 193 | Gamemaster |
| 3 | 192 | Administrator |

Because roles chain through [rbac_linked_permissions](rbac_linked_permissions), granting Administrator (192) automatically includes Gamemaster, Moderator, and Player permissions.

### realmId

The [realm ID](realmlist#id) this default applies to. Use `-1` to apply to all realms.

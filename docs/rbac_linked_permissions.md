# rbac\_linked\_permissions

[<-Back-to:Auth](database-auth)

**The \`rbac\_linked\_permissions\` table**

This table defines the parent-child relationships between permissions. When a permission (typically a role) is granted, all of its linked permissions are also granted. This is how role inheritance works in the [RBAC](rbac) system.

**Table Structure**

| Field         | Type | Attributes | Key | Null | Default | Extra | Comment              |
| ------------- | ---- | ---------- | --- | ---- | ------- | ----- | -------------------- |
| [id](#id)             | INT  | UNSIGNED   | PRI | NO   |         |       | Permission id        |
| [linkedId](#linkedid) | INT  | UNSIGNED   | PRI | NO   |         |       | Linked Permission id |

Both fields have a foreign key to [rbac_permissions.id](rbac_permissions#id) with `ON DELETE CASCADE`.

**Description of the fields**

### id

The parent permission (role) that contains other permissions. Typically one of the role IDs:

| ID | Role |
| -- | ---- |
| 192 | Administrator |
| 193 | Gamemaster |
| 194 | Moderator |
| 195 | Player |
| 196 | Admin Commands |
| 197 | GM Commands |
| 198 | Mod Commands |
| 199 | Player Commands |

### linkedId

The child permission that is granted when the parent (`id`) is granted. Can be any permission from [rbac_permissions](rbac_permissions), including another role — this is how the hierarchy chains together (e.g. Administrator 192 links to Gamemaster 193, which links to Moderator 194, and so on).

Linked permissions are expanded recursively during [permission resolution](rbac#permission-resolution).

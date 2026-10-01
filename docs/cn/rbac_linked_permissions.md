# rbac\_linked\_permissions

[<-返回至:Auth](database-auth)

**`rbac\_linked\_permissions` 表**

此表定义权限之间的父子关系。当授予某个权限（通常是角色）时，其所有关联权限也会一并授予。这就是 [RBAC](rbac) 系统中角色继承的工作方式。

**表结构**

| Field         | Type | Attributes | Key | Null | Default | Extra | Comment              |
| ------------- | ---- | ---------- | --- | ---- | ------- | ----- | -------------------- |
| [id](#id)             | INT  | UNSIGNED   | PRI | NO   |         |       | 权限 ID              |
| [linkedId](#linkedid) | INT  | UNSIGNED   | PRI | NO   |         |       | 关联权限 ID          |

两个字段都具有指向 [rbac_permissions.id](rbac_permissions#id) 的外键，且带有 `ON DELETE CASCADE`。

**字段说明**

### id

包含其他权限的父权限（角色）。通常为以下角色 ID 之一：

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

授予父权限（`id`）时随之授予的子权限。可以是 [rbac_permissions](rbac_permissions) 中的任意权限，包括另一个角色——这正是层级链式继承的方式（例如 Administrator 192 关联到 Gamemaster 193，Gamemaster 193 又关联到 Moderator 194，依此类推）。

在 [权限解析](rbac#permission-resolution) 过程中，关联权限会被递归展开。

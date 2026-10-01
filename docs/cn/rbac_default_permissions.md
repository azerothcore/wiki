# rbac\_default\_permissions

[<-返回至:Auth](database-auth)

**`rbac\_default\_permissions` 表**

此表将 [account_access.gmlevel](account_access#gmlevel) 安全级别映射到默认的 RBAC 角色。当玩家登录时，其安全级别决定会自动授予哪个角色。

有关系统概述，请参阅 [RBAC](rbac)。

**表结构**

| Field             | Type    | Attributes | Key | Null | Default | Extra | Comment                  |
| ----------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [secId](#secid)               | INT     | UNSIGNED   | PRI | NO   |         |       | 安全级别 ID              |
| [permissionId](#permissionid) | INT     | UNSIGNED   | PRI | NO   |         |       | 权限 ID                  |
| [realmId](#realmid)           | INT     | SIGNED     | PRI | NO   | -1      |       | 服务器 ID，-1 表示全部   |

`permissionId` 字段具有指向 [rbac_permissions.id](rbac_permissions#id) 的外键。

**字段说明**

### secId

来自 [account_access.gmlevel](account_access#gmlevel) 的安全级别。

### permissionId

针对此安全级别默认授予的 RBAC 权限（角色）。默认分配如下：

| secId | permissionId | Role |
| ----- | ------------ | ---- |
| 0 | 195 | Player |
| 1 | 194 | Moderator |
| 2 | 193 | Gamemaster |
| 3 | 192 | Administrator |

由于角色通过 [rbac_linked_permissions](rbac_linked_permissions) 进行链式继承，授予 Administrator（192）会自动包含 Gamemaster、Moderator 和 Player 的权限。

### realmId

此默认设置所适用的 [realm ID](realmlist#id)。使用 `-1` 表示适用于所有服务器。

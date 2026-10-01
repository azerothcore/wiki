# rbac\_account\_permissions

[<-返回至:Auth](database-auth)

**`rbac\_account\_permissions` 表**

此表存储每个账号的权限覆盖。使用它来为单个账号授予或拒绝特定权限，超出其默认安全级别所提供的权限。

有关系统概述，请参阅 [RBAC](rbac)。

**表结构**

| Field             | Type       | Attributes | Key | Null | Default | Extra | Comment                  |
| ----------------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [accountId](#accountid)       | INT        | UNSIGNED   | PRI | NO   |         |       | 账号 ID                  |
| [permissionId](#permissionid) | INT        | UNSIGNED   | PRI | NO   |         |       | 权限 ID                  |
| [granted](#granted)           | TINYINT(1) | SIGNED     |     | NO   | 1       |       | 授予 = 1，拒绝 = 0      |
| [realmId](#realmid)           | INT        | SIGNED     | PRI | NO   | -1      |       | 领域 ID，-1 表示全部    |

`accountId` 字段对 [account.id](account#id) 有一个外键，并带有 `ON DELETE CASCADE`。
`permissionId` 字段对 [rbac_permissions.id](rbac_permissions#id) 有一个外键，并带有 `ON DELETE CASCADE`。

**字段说明**

### accountId

[账号 ID](account#id)。

### permissionId

来自 [rbac_permissions](rbac_permissions) 的权限 ID。这可以是单个权限或角色。授予/拒绝一个角色会影响链接到它的所有权限。

### granted

控制此条目是授予还是拒绝：

| Value | Meaning |
| ----- | ------- |
| 1 | **授予（Grant）** — 将此权限添加到账号 |
| 0 | **拒绝（Deny）** — 从账号中移除该权限（及其链接的权限） |

在[权限解析](rbac#permission-resolution)过程中，拒绝会在扩展后从授予中减去。这意味着拒绝一个角色就会拒绝该角色所包含的一切。

### realmId

此覆盖所适用的[领域 ID](realmlist#id)。使用 `-1` 应用于所有领域。

这些覆盖可以在游戏内使用 [.rbac 命令](rbac#commands) 进行管理。

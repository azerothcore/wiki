# rbac\_permissions

[<-返回至:Auth](database-auth)

**`rbac\_permissions` 表**

此表定义所有可用的 RBAC 权限。每个权限代表一项独立的能力——一种游戏玩法权限、一条命令，或者一个将其他权限捆绑在一起的角色。

有关系统概述，请参阅 [RBAC](rbac)。

**表结构**

| Field    | Type         | Attributes | Key | Null | Default | Extra | Comment       |
| -------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------- |
| [id](#id)     | INT          | UNSIGNED   | PRI | NO   | 0       |       | 权限 ID       |
| [name](#name) | VARCHAR(100) | SIGNED     |     | NO   |         |       | 权限名称      |

**字段说明**

### id

唯一的权限标识符。ID 范围如下：

| Range | Purpose |
| ----- | ------- |
| 1–53 | 游戏玩法权限（立即退出、跳过排队、加入战场等） |
| 192–195 | 安全级别角色（Administrator、Gamemaster、Moderator、Player） |
| 196–199 | 命令角色（Admin Commands、GM Commands、Mod Commands、Player Commands） |
| 200–925 | 单条命令权限（每条 `.command` 对应一个） |
| 100000+ | 模块权限（通过 [module_rbac_permissions](module_rbac_permissions) 自动分配） |

### name

用于描述权限的可读名称。遵循以下约定：

- 游戏玩法权限：描述性名称（例如 `Instant logout`、`Skip Queue`）
- 角色：以 `Role:` 为前缀（例如 `Role: Sec Level Administrator`）
- 命令：以 `Command:` 为前缀（例如 `Command: rbac account list`）

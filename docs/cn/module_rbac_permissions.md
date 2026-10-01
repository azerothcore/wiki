# module\_rbac\_permissions

[<-返回至:Auth](database-auth)

**\`module\_rbac\_permissions\` 表**

此表允许模块注册自己的 RBAC 权限，而不会与核心权限或其他模块的权限产生 ID 冲突。每个模块使用本地 ID（1、2、3...），该表会自动分配从 100000 开始的全局 ID。

有关系统概述，请参阅 [RBAC](rbac)。

**表结构**

| Field       | Type         | Attributes | Key    | Null | Default | Extra          | Comment                    |
| ----------- | ------------ | ---------- | ------ | ---- | ------- | -------------- | -------------------------- |
| [module](#module)     | VARCHAR(255) | SIGNED     | PRI    | NO   |         |                | 模块目录名称，例如 mod-cfbg |
| [id](#id)             | INT          | UNSIGNED   | PRI    | NO   |         |                | 模块本地权限 ID             |
| [global_id](#globalid) | INT         | UNSIGNED   | UNIQUE | NO   |         | AUTO_INCREMENT | 自动分配的全局权限 ID       |
| [name](#name)         | VARCHAR(100) | SIGNED     |        | NO   |         |                | 权限名称                    |

主键是由 `(module, id)` 组成的复合主键，可防止跨模块的 ID 冲突。`global_id` 列具有独立的 `UNIQUE` 索引，并从 100000 开始自动递增。

**字段说明**

### module

模块目录名称（例如 `mod-cfbg`、`mod-eluna`）。该名称必须与 `modules/` 下的模块目录名称一致。

### id

模块本地权限 ID。每个模块自行管理从 1 开始的 ID 序列。由于主键包含模块名称，不同模块可以使用相同的本地 ID 而不会产生冲突。

### global\_id

由核心 RBAC 系统使用的自动分配的全局唯一权限 ID。`AUTO_INCREMENT` 从 100000 开始，以避免与核心权限 ID（1–924）冲突。模块绝不应手动设置此值——它由数据库在插入时分配。

### name

权限的人类可读名称。按照惯例，命令权限使用 `Command: .命令名 子命令` 的格式。

## 模块集成指南

### 第 1 步：在 SQL 中注册权限

在模块的 `data/sql/db-auth/` 目录下创建一个 SQL 文件：

```sql
INSERT IGNORE INTO `module_rbac_permissions` (`module`, `id`, `name`) VALUES
('mod-example', 1, 'Command: .example hello'),
('mod-example', 2, 'Command: .example info');
```

使用 `INSERT IGNORE` 以确保 SQL 可以安全地重复执行。

### 第 2 步：在 C++ 中查询全局 ID

在模块的 C++ 代码中，使用 `AccountMgr` 将本地 ID 转换为全局 ID：

```cpp
#include "AccountMgr.h"

uint32 globalId = sAccountMgr->GetModulePermission("mod-example", 1);
```

如果在数据库中找不到该权限，则返回 0。

### 第 3 步：在 CommandScript 中使用

在定义命令时，将全局 ID 用作每个命令的权限：

```cpp
static uint32 GetPermission(uint32 localId)
{
    return sAccountMgr->GetModulePermission("mod-example", localId);
}

std::vector<ChatCommand> GetCommands() const override
{
    static std::vector<ChatCommand> exampleCommandTable =
    {
        { "hello", GetPermission(1), false, &HandleHelloCommand, "" },
        { "info",  GetPermission(2), false, &HandleInfoCommand,  "" },
    };

    static std::vector<ChatCommand> commandTable =
    {
        { "example", SEC_PLAYER, false, nullptr, "", exampleCommandTable },
    };

    return commandTable;
}
```

### 第 4 步：分配权限

模块权限需要先分配给角色或账号，之后才能被使用。

**分配给角色** —— 通过 [rbac_linked_permissions](rbac_linked_permissions) 将模块权限链接到命令角色。所有继承该角色的玩家都将获得访问权限：

```sql
-- 将 mod-example 的所有命令授予 GM 命令角色 (197)
INSERT IGNORE INTO `rbac_linked_permissions` (`id`, `linkedId`)
SELECT 197, `global_id`
FROM `module_rbac_permissions`
WHERE `module` = 'mod-example';
```

**分配给特定账号** —— 插入到 [rbac_account_permissions](rbac_account_permissions) 中，或在游戏中使用 `.rbac` 命令：

```sql
-- 将 mod-example 的第一个命令授予所有服务器上的账号 5
INSERT INTO `rbac_account_permissions` (`accountId`, `permissionId`, `granted`, `realmId`)
SELECT 5, `global_id`, 1, -1
FROM `module_rbac_permissions`
WHERE `module` = 'mod-example' AND `id` = 1;
```

或者在游戏中，一旦你知道了全局 ID（例如 100001）：

```
.rbac account grant 5 100001
```

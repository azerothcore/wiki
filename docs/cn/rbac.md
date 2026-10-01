# RBAC

[<-返回至:文档索引](documentation-index)

## 概述

基于角色的访问控制（RBAC）是 AzerothCore 的权限系统。它提供了对每个账号可以做什么的细粒度控制——从单个命令到游戏内特权，例如跳过登录队列或加入战场。

使用 RBAC 你可以：

- 单独控制对每个命令的访问
- 创建将相关权限捆绑在一起的角色
- 在无需更改账号整体安全级别的情况下，为每个账号覆盖特定权限
- 让模块注册自己的权限，而不会与核心 ID 冲突

## 架构

RBAC 系统建立在四个概念之上：

1. **权限（Permissions）** — 单项能力（例如"可以使用 `.tele`"、"跳过队列"、"加入战场"）
2. **角色（Roles）** — 链接到其他权限的权限，形成一个组。授予一个角色即授予其所包含的一切
3. **默认值（Defaults）** — 从 `account_access.gmlevel` 到初始 RBAC 角色的映射，使安全级别自动映射到权限集
4. **账号覆盖（Account Overrides）** — 针对每个账号的授予或拒绝，用于在默认值之外微调访问权限

### 数据库表

| Table | Purpose |
| ----- | ------- |
| [rbac_permissions](rbac_permissions) | 定义所有可用的权限 |
| [rbac_linked_permissions](rbac_linked_permissions) | 将角色链接到其子权限 |
| [rbac_default_permissions](rbac_default_permissions) | 将安全级别映射到默认角色 |
| [rbac_account_permissions](rbac_account_permissions) | 针对每个账号的覆盖（授予/拒绝） |
| [module_rbac_permissions](module_rbac_permissions) | 模块注册的权限 |

一个便捷视图 `vw_rbac` 连接了链接表和默认表，以便更轻松地查询。

## 权限 ID 范围

| Range | Purpose | Examples |
| ----- | ------- | ------- |
| 1–53 | 游戏内权限 | 立即退出、跳过队列、加入战场/竞技场/地下城查找器 |
| 192–195 | 安全级别角色 | 管理员 (192)、游戏管理员 (193)、版主 (194)、玩家 (195) |
| 196–199 | 命令角色 | 管理员命令 (196)、GM 命令 (197)、版主命令 (198)、玩家命令 (199) |
| 200–925 | 单个命令权限 | 每个 `.command` 一个 |
| 100000+ | 模块权限 | 通过 [module_rbac_permissions](module_rbac_permissions) 自动分配 |

## 角色层级

角色通过链接权限相互继承。每个较高级别的角色都会链接到其下方的角色，因此管理员会自动获得玩家拥有的每个权限。

```
Administrator (192)
├── Core admin perms (7, 21, 42, 43)
├── Admin Commands (196)
└── Gamemaster (193)
    ├── Core GM perms (45, 48, 52, 53)
    ├── GM Commands (197)
    └── Moderator (194)
        ├── Core mod perms (1, 2, 9, 11, 13–47, 51, ...)
        ├── Mod Commands (198)
        └── Player (195)
            ├── Core player perms (3, 4, 5, 6, 24, 49, 50)
            └── Player Commands (199)
```

### 默认安全级别映射

当玩家登录时，其 `account_access.gmlevel` 决定他们获得哪个角色：

| gmlevel | Role | Permission ID |
| ------- | ---- | ------------- |
| 3 | Administrator（管理员） | 192 |
| 2 | Gamemaster（游戏管理员） | 193 |
| 1 | Moderator（版主） | 194 |
| 0 | Player（玩家） | 195 |

这些默认值存储在 [rbac_default_permissions](rbac_default_permissions) 中。

## 权限解析 {#permission-resolution}

当计算账号的权限时，会执行以下步骤：

1. **收集授予（Collect grants）** — 来自 [rbac_account_permissions](rbac_account_permissions) 的账号特定授予，加上来自 [rbac_default_permissions](rbac_default_permissions) 的默认值
2. **扩展授予（Expand grants）** — 每个已授予的权限都会通过 [rbac_linked_permissions](rbac_linked_permissions) 递归扩展。如果权限 192 链接到 193，而 193 链接到 194，则全部都会包含在内
3. **收集拒绝（Collect denies）** — 来自 [rbac_account_permissions](rbac_account_permissions) 的账号特定拒绝
4. **扩展拒绝（Expand denies）** — 被拒绝的权限也会通过链接权限进行扩展
5. **相减（Subtract）** — 最终权限 = 扩展授予 − 扩展拒绝

这意味着拒绝一个角色就会拒绝该角色所包含的一切。

## 命令 {#commands}

`.rbac` 命令允许无需重启服务器即可实时管理账号权限。

| Command | Permission | Description |
| ------- | ---------- | ----------- |
| `.rbac account list <account>` | 202 | 列出账号已授予、已拒绝和默认的权限 |
| `.rbac account grant <account> <permId> [realmId]` | 203 | 向账号授予权限 |
| `.rbac account deny <account> <permId> [realmId]` | 204 | 拒绝账号的权限 |
| `.rbac account revoke <account> <permId> [realmId]` | 205 | 撤销先前授予或拒绝的权限 |
| `.rbac list [permId]` | 206 | 列出所有权限，或显示特定权限的详细信息 |

更改对在线玩家立即生效。

## 模块集成

模块可以使用 [module_rbac_permissions](module_rbac_permissions) 表注册自己的 RBAC 权限。每个模块使用本地 ID（1、2、3……），这些 ID 会自动映射到从 100000 开始的全局 ID，从而避免与核心权限 ID 以及模块之间产生冲突。

完整的集成指南请参阅 [module_rbac_permissions](module_rbac_permissions)。

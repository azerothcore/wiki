---
redirect_from: "/cn/Creating-Accounts"
---

# 创建账号

要登录你的新服务器，你需要一个账号。

建议为你的账号使用安全级别 3。

在世界服务器（Worldserver）控制台中运行以下命令。

## 创建账号

```
account create <user> <pass>
```

**示例：**

```
account create admin admin
```

## 设置账号的安全级别

| 级别 | 安全级别        |
|------|-----------------|
| 0    | SEC_PLAYER      |
| 1    | SEC_MODERATOR   |
| 2    | SEC_GAMEMASTER  |
| 3    | SEC_ADMINISTRATOR |

```
account set gmlevel <user> <level> <realm>
```

{% include note.html content="如果命令是在账号已登录的情况下运行的，你需要重新登录，安全级别才能正确更新。" %}

**示例：**

```
account set gmlevel admin 3 -1
```

{% include note.html content="使用 -1 来选择所有服务器（realm），或者指定具体的服务器 ID。" %}

## 修改密码

```
account set password <user> <password> <password>
```

**示例：**

```
account set password admin 1234 1234
```

## 更高的安全级别

最高的安全级别是 SEC_CONSOLE (4)，这是你的世界服务器默认拥有的级别。

它拥有账号管理权限，对于不了解相关操作的人，不建议将其用于游戏内账号。

要将账号更新为安全级别 4，你需要手动编辑数据库中的字段，或者运行下面的查询。

```sql
UPDATE `account_access` AS `access`
INNER JOIN `account` AS `account` ON `access`.`id` = `account`.`id`
SET `gmlevel` = 4 WHERE `username` = '<user>';
```

# guild\_bank\_right

[<-返回至:Characters](database-characters)

**\`guild\_bank\_right\` 表**

此表保存了公会成员在公会银行中取出、存入等权限的相关信息。

**表结构**

| Field           | Type    | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guildid][1]    | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [TabId][2]      | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [rid][3]        | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [gbright][4]    | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |
| [SlotPerDay][5] | INT     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guildid
[2]: #tabid
[3]: #rid
[4]: #gbright
[5]: #slotperday

**字段说明**

### guildid

公会的 ID。

### TabId

你正在为其设置权限的标签页 ID。

### rid

你正在为其设置权限的职位（rank）。

### gbright

你想授予该职位玩家在此标签页上的权限。这是一个位掩码（bitmask）。要组合权限，你必须对标志进行 OR 运算求和。

标志（FLAGS）：

| 值   | 描述                                    |
| ---- | --------------------------------------- |
| 1    | 查看物品                                |
| 2    | 存入物品                                |
| 4    | 在浏览标签页时更新显示的物品名称        |
| 8    | 取出物品                                |
| 255  | 拥有全部权限                            |

### SlotPerDay

玩家每天可以取出的物品数量（如果权限允许其取出物品的话）。

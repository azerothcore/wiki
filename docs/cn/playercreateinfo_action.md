# playercreateinfo_action

[<-返回至:World](database-world)

**`playercreateinfo_action` 表**

该表保存了新建角色应拥有的默认动作信息。每种种族-职业组合都可以有不同的默认起始设置。

**表结构**

| Field       | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [race][1]   | TINYINT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [class][2]  | TINYINT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [button][3] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [action][4] | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [type][5]   | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #race
[2]: #class
[3]: #button
[4]: #action
[5]: #type

**字段说明**

### race

角色的[种族](chrraces#content)。

### class

角色的[职业](chrclasses#content)。

### button

动作条上放置动作图标的插槽 ID。

特殊动作条用于姿态、光环、宠物、潜行以及其他类似的特殊模式。

| Button IDs | 动作条（按键）                 |
| ---------- | ------------------------------ |
| 0-11       | 1 (SHIFT + 1)                  |
| 12-23      | 2 (SHIFT + 2)                  |
| 24-35      | 3 (SHIFT + 3) 右侧动作条 1     |
| 36-47      | 4 (SHIFT + 4) 右侧动作条 2     |
| 48-59      | 5 (SHIFT + 5) 右下动作条       |
| 60-71      | 6 (SHIFT + 6) 左下动作条       |
| 72-83      | 1 特殊 A                       |
| 84-95      | 1 特殊 B                       |
| 96-107     | 1 特殊 C                       |
| 108-119    | 1 特殊 D                       |

### action

根据 type 值的不同，它可以是[法术 ID](spell#id)、[物品 ID](item_template#entry) 或宏 ID。

### type

动作类型：

| ID  | Type  |
| --- | ----- |
| 0   | 法术   |
| 64  | 宏    |
| 128 | 物品   |

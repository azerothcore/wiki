# character\_account\_data

[<-返回至:Characters](database-characters)

**\`character\_account\_data\` 表**

包含角色设置的数据。

**表结构**

| Field     | Type    | Attributes | Key | Null | Default | Extra | Comment |
| --------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1] | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [type][2] | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [time][3] | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [data][4] | BLOB    | SIGNED     |     | NO   |         |       |         |

[1]: #guid
[2]: #type
[3]: #time
[4]: #data

**字段说明**

### guid

角色全局唯一标识符。参见 [characters.guid](characters#guid)。

### type

| 值   | 描述                  |
| ---- | --------------------- |
| 1    | 每个角色的配置缓存    |
| 3    | 每个角色的按键绑定缓存 |
| 5    | 每个角色的宏缓存      |
| 6    | 每个角色的布局缓存    |
| 7    | 每个角色的聊天缓存    |

### time

上次修改的时间，以 Unix 时间表示。

### data

无法编写描述。你只需要明白它就是数据。

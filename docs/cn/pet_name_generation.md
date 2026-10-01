# pet\_name\_generation

[<-返回至:World](database-world)

**`pet_name_generation` 表**

该表保存用于宠物名字生成的名称片段（前半部分和后半部分）。

**表结构**

| Field      | Type      | Attributes | Key | Null | Default | Extra          | Comment |
| ---------- | --------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [id][1]    | MEDIUMINT | UNSIGNED   | PRI | NO   | NULL    | Auto increment |         |
| [word][2]  | tinytext  | SIGNED     |     | NO   | NULL    |                |         |
| [entry][3] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |                |         |
| [half][4]  | TINYINT   | SIGNED     |     | NO   | 0       |                |         |

[1]: #id
[2]: #word
[3]: #entry
[4]: #half

## 字段说明

### id

条目 ID。这是一个自增字段，数值是任意的。在添加条目时，最好让数据库自动选取下一个可用的 ID 编号。

### word

此条目的名称片段。

### entry

你想为其生成该名称片段的生物在 creature\_template.entry 中的条目。

### half

该值决定这是此条目名称的前半部分还是后半部分。

-   0 前半部分
-   1 后半部分

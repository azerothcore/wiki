# pet\_name\_generation\_locale

[<-返回至:World](database-world)

**`pet_name_generation_locale` 表**

该表保存用于特定语言区域宠物名字生成的名称片段（前半部分和后半部分）。

**表结构**

| Field       | Type      | Attributes | Key | Null | Default | Extra          | Comment |
| ----------- | --------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [ID][1]     | MEDIUMINT | UNSIGNED   | PRI | NO   | NULL    | Auto increment |         |
| [locale][2] | VARCHAR   |            |     | NO   |         |                |         |
| [word][3]   | tinytext  | SIGNED     |     | NO   | NULL    |                |         |
| [entry][4]  | MEDIUMINT | UNSIGNED   |     | NO   | 0       |                |         |
| [half][5]   | TINYINT   | SIGNED     |     | NO   | 0       |                |         |

[1]: #id
[2]: #locale
[3]: #word
[4]: #entry
[5]: #half

## 字段说明

### ID

条目 ID。该字段必须与 [pet_name_generation.id](pet_name_generation#id) 匹配

### Locale

客户端的语言。

| Language |
| -------- |
| koKR     |
| frFR     |
| deDE     |
| zhCN     |
| zhTW     |
| esES     |
| esMX     |
| ruRU     |

### word

此条目的名称片段。

### entry

你想为其生成该名称片段的生物在 creature\_template.entry 中的条目。

### half

该值决定这是此条目名称的前半部分还是后半部分。

-   0 前半部分
-   1 后半部分

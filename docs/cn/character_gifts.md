# character\_gifts

[<-返回:Characters](database-characters)

**\`character\_gifts\` 表**

该表保存了关于已包装/礼物的物品的数据。

**表结构**

| Field          | Type | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]      | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [item_guid][2] | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [entry][3]     | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [flags][4]     | INT  | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #itemguid
[3]: #entry
[4]: #flags

**字段说明**

### guid

角色的 GUID。参见 [characters.guid](characters#guid)。

### item\_guid

物品的 GUID。参见 [item\_instance.guid](item_instance#guid)。

### entry

物品的 entry（物品模板 ID）。参见 [item\_template.entry](item_template#entry)。

### flags

礼物物品在被打包（wrapped）时的物品原型标志（item proto flags）。

*留待后续研究：最大 flags 为 13369920？ProtoFlags 的 FieldFlags？*

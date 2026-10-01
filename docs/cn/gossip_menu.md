# gossip\_menu

[<-返回至:World](database-world)

**\`gossip\_menu\` 表**

此表用于在玩家与设置了 [npcflag](creature_template#npcflag) 的 NPC 交谈时显示对话（gossip）内容。

**表结构**

| Field       | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [MenuID][1] | SMALLINT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [TextID][2] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |

[1]: #menuid
[2]: #textid

**字段说明**

### MenuID

此值必须与你添加到 [creature\_template.gossip\_menu\_id](creature_template#gossipmenuid) 中的条目（entry）相匹配。它还会对 gossip\_menu\_option 中的选项进行分组，并显示所有与此 ID 相关联的选项。

**注意：** 如果你要添加自己的自定义菜单选项，通常建议从 90,000 或以上的 ID 开始，以确保不会与其他对话菜单 ID 冲突。

### TextID

此字段链接到 [npc\_text.ID](npc_text#id)，用于指定最初要显示的对话内容。同时，它还会决定 NPC 在选项菜单显示时于顶部说出的话语。

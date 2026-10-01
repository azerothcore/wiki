# gossip\_menu\_option

**表：gossip\_menu\_option**

此表保存了对话（gossip）NPC 可以拥有的菜单选项相关信息。选项示例："训练我！"、"我想要遗忘我的天赋"。

## 结构

| Field                      | Type      | Attributes | Key | Null | Default | Extra | Comment |
| -------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [MenuID][1]                | SMALLINT  | UNSIGNED   | PRI | NO   |         |       |         |
| [OptionID][2]              | SMALLINT  | UNSIGNED   | PRI | NO   |         |       |         |
| [OptionIcon][3]            | SMALLINT  | UNSIGNED   | PRI | NO   |         |       |         |
| [OptionText][4]            | text      |            |     | YES  | NULL    |       |         |
| [OptionBroadcastTextID][5] | MEDIUMINT |            |     | NO   |         |       |         |
| [OptionType][6]            | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [OptionNpcFlag][7]         | INT       | UNSIGNED   |     | NO   |         |       |         |
| [ActionMenuID][8]          | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [ActionPoiID][9]           | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [BoxCoded][10]             | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [BoxMoney][11]             | INT       | UNSIGNED   |     | NO   |         |       |         |
| [BoxText][12]              | text      |            |     | YES  | NULL    |       |         |
| [BoxBroadcastTextID][13]   | MEDIUMINT |            |     | NO   |         |       |         |
| [VerifiedBuild][14]        | SMALLINT  |            |     | NO   |         |       |         |

[1]: #menuid
[2]: #optionid
[3]: #optionicon
[4]: #optiontext
[5]: #optionbroadcasttextid
[6]: #optiontype
[7]: #optionnpcflag
[8]: #actionmenuid
[9]: #actionpoiid
[10]: #boxcoded
[11]: #boxmoney
[12]: #boxtext
[13]: #boxbroadcasttextid
[14]: #verifiedbuild

## 字段说明

### MenuID

此选项所关联的 Gossip\_menu.entry 中的对话条目。
如果这是所选 NPC 的默认对话选项，请确认该 NPC 在其 [creature\_template.gossip\_menu\_id](creature_template#gossipmenuid) 中具有此值。

### OptionID

与此 gossip\_menu\_option 相关联的 ID。对于给定的 menu\_id，从 0（零）开始必须是唯一的。
如果同一个 gossip\_menu 中有多个选项，则值每次递增 1。

### OptionIcon

| 名称                        | ID  | 描述                                    |
| --------------------------- | --- | --------------------------------------- |
| GOSSIP\_ICON\_CHAT          | 0   | 白色聊天气泡                            |
| GOSSIP\_ICON\_VENDOR        | 1   | 棕色袋子                                |
| GOSSIP\_ICON\_TAXI          | 2   | 飞行                                    |
| GOSSIP\_ICON\_TRAINER       | 3   | 书本                                    |
| GOSSIP\_ICON\_INTERACT\_1   | 4   | 交互轮盘                                |
| GOSSIP\_ICON\_INTERACT\_2   | 5   | 交互轮盘                                |
| GOSSIP\_ICON\_MONEY\_BAG    | 6   | 带黄点的棕色袋子（金币）                |
| GOSSIP\_ICON\_TALK          | 7   | 带黑点的白色聊天气泡（**...**）          |
| GOSSIP\_ICON\_TABARD        | 8   | 战袍                                    |
| GOSSIP\_ICON\_BATTLE        | 9   | 双剑                                    |
| GOSSIP\_ICON\_DOT           | 10  | 黄点                                    |

### OptionText

这是你想在玩家可选择选项中显示的文本。例如："请训练我。"、"我想浏览一下你的商品。"、"学习双天赋"。
如果 OptionBroadcastTextID 包含有效的 broadcast\_text.ID，则会链接到 broadcast\_text，从而直接显示 broadcast\_text 中的内容，而不是 option\_text 字段中的内容。

### OptionBroadcastTextID

与 broadcast\_text.ID 中相同文本对应的 ID。

### OptionType

| option_id 名称                  | 值   | npcflag 名称（& 注释）                                                | npcflag 值 |
| ------------------------------- | ---- | --------------------------------------------------------------------- | ---------- |
| GOSSIP_OPTION_NONE              | 0    | UNIT_NPC_FLAG_NONE                                                    | 0          |
| GOSSIP_OPTION_GOSSIP            | 1    | UNIT_NPC_FLAG_GOSSIP                                                  | 1          |
| GOSSIP_OPTION_QUESTGIVER        | 2    | UNIT_NPC_FLAG_QUESTGIVER                                              | 2          |
| GOSSIP_OPTION_VENDOR            | 3    | UNIT_NPC_FLAG_VENDOR（确保该生物存在 npc_vendor 数据）                | 128        |
| GOSSIP_OPTION_TAXIVENDOR        | 4    | UNIT_NPC_FLAG_TAXIVENDOR                                              | 8192       |
| GOSSIP_OPTION_TRAINER           | 5    | UNIT_NPC_FLAG_TRAINER（记得在 creature_default_trainer 中设置 (TrainerId, CreatureId)） | 16         |
| GOSSIP_OPTION_SPIRITHEALER      | 6    | UNIT_NPC_FLAG_SPIRITHEALER                                            | 16384      |
| GOSSIP_OPTION_SPIRITGUIDE       | 7    | UNIT_NPC_FLAG_SPIRITGUIDE                                             | 32768      |
| GOSSIP_OPTION_INNKEEPER         | 8    | UNIT_NPC_FLAG_INNKEEPER                                               | 65536      |
| GOSSIP_OPTION_BANKER            | 9    | UNIT_NPC_FLAG_BANKER                                                  | 131072     |
| GOSSIP_OPTION_PETITIONER        | 10   | UNIT_NPC_FLAG_PETITIONER                                              | 262144     |
| GOSSIP_OPTION_TABARDDESIGNER    | 11   | UNIT_NPC_FLAG_TABARDDESIGNER                                          | 524288     |
| GOSSIP_OPTION_BATTLEFIELD       | 12   | UNIT_NPC_FLAG_BATTLEFIELDPERSON                                       | 1048576    |
| GOSSIP_OPTION_AUCTIONEER        | 13   | UNIT_NPC_FLAG_AUCTIONEER                                              | 2097152    |
| GOSSIP_OPTION_STABLEPET         | 14   | UNIT_NPC_FLAG_STABLE                                                  | 4194304    |
| GOSSIP_OPTION_ARMORER           | 15   | UNIT_NPC_FLAG_ARMORER（未使用）                                       | 4096       |
| GOSSIP_OPTION_UNLEARNTALENTS    | 16   | UNIT_NPC_FLAG_TRAINER（GOSSIP_OPTION_TRAINER 的附加选项）             | 16         |
| GOSSIP_OPTION_UNLEARNPETTALENTS | 17   | UNIT_NPC_FLAG_TRAINER（GOSSIP_OPTION_TRAINER 的附加选项）             | 16         |
| GOSSIP_OPTION_LEARNDUALSPEC     | 18   | UNIT_NPC_FLAG_TRAINER（GOSSIP_OPTION_TRAINER 的附加选项）             | 16         |
| GOSSIP_OPTION_OUTDOORPVP        | 19   | 由代码添加（用于户外 PvP 生物的选项）                                  |            |
| GOSSIP_OPTION_MAX               |      |                                                                       |            |

### OptionNpcFlag

这是 NPC 必须拥有的 npcflag（[Creature\_template.npcflag](creature_template#npcflag)），用于让该选项得以显示。请参见上表中（// 之后）的注释。

### ActionMenuID

如果你想创建子菜单，这就是要链接的 ID（[gossip\_menu.entry](gossip_menu#entry) / [gossip\_menu\_option.menu\_id](gossip_menu_option#menuid)），用于创建该子菜单。

### ActionPoiID

如果你想在小地图上显示一个 POI（兴趣点）（就像向城市卫兵问路时卫兵会放置一个标记那样），此字段为 [Points\_of\_interest.entry](points_of_interest#entry) 中的 \`entry\`。

### BoxCoded

如果你想显示一个需要输入代码的输入框，就可以使用此字段。

### BoxMoney

玩家为所选选项需要支付的金额，会以金币、银币、铜币的数量形式显示在确认框中。
你在此处插入的数据库值必须以铜币数量表示，例如 10 金币应填写为 100000（10g 00s 00c）。

### BoxText

这是弹出的窗口的文本，窗口中带有 "Yes"（是）或 "No"（否）的可点击按钮。如果你希望在脚本执行前出现一个是/否确认窗口，这会非常有用。例如："Are you sure you want to teleport to Dalaran?"（你确定要传送到达拉然吗？）。
如果 BoxBroadCastTextID 包含有效的 broadcast\_text.ID，则会链接到 broadcast\_text，从而直接显示 broadcast\_text 中的内容，而不是 box\_text 字段中的内容。

### BoxBroadcastTextID

与 [broadcast\_text.ID](broadcast_text#id) 中相同文本对应的 ID。

### VerifiedBuild

此字段用于确定模板是否已根据 WDB 文件进行验证。

如果值为 0，则表示尚未解析。

如果值大于 0，则表示已使用该特定客户端构建版本的 WDB 文件进行解析。

如果值为 -1，则它只是一个占位符，直到在 WDB 中找到正确的数据为止。

如果值为 [客户端构建版本](realmlist#gamebuild)，则表示已使用该特定客户端构建版本的 WDB 文件进行解析，并出于某些特殊需要而稍后进行了手动编辑。

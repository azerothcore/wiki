# npc\_spellclick\_spells

[<-返回:World](database-world)

**\`npc\_spellclick\_spells\` 表**

此表保存有关在收到 CMSG\_SPELLCLICK 时要施放的法术的信息。

该操作码用于某些任务中，这些任务要求你拾取那些在生成时就已经死亡的生物。例如 [为未来打算](http://www.wowhead.com/quest=11960) 和 [搜刮尸体](http://www.wowhead.com/quest=11999)。

**表结构**

| Field           | Type     | Attributes | Key | Null | Default | Extra | Comment                                                              |
| --------------- | -------- | ---------- | --- | ---- | ------- | ----- | -------------------------------------------------------------------- |
| [npc_entry][1]  | INT      | UNSIGNED   | PRI | NO   | NULL    |       | 引用 creature_template 表                                            |
| [spell_id][2]   | INT      | UNSIGNED   | PRI | NO   | NULL    |       | 要施放的法术的 ID                                                    |
| [cast_flags][3] | TINYINT  | UNSIGNED   |     | NO   | NULL    |       | 谁向谁施放法术，生物 <=> 玩家（值：0-3）                             |
| [user_type][4]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       | 与召唤者的关系：0-否 1-友好 2-团队 3-小队，玩家可以点击              |

[1]: #npcentry
[2]: #spellid
[3]: #castflags
[4]: #usertype

**字段说明**

### npc\_entry

引用 creature\_template.entry

### spell\_id

应当施放的法术。

请注意，某些任务每次点击会施放多个法术。

例如，[为未来打算](http://www.wowhead.com/quest=11960) 有 [为未来打算：制造雪崩小狼崽](http://www.wowhead.com/spell=46773)，它会在玩家的背包中创建物品，
以及 [为未来打算：制造雪崩小狼崽的伪装](http://www.wowhead.com/spell=46167)，它会使生物消失。

这营造出该生物已被拾取的假象。

### cast\_flags

每次法术点击（spellclick）事件中，都有一个玩家和一个生物"参与"。此字段定义了谁向谁施放法术。
低位定义施法者：1=点击者（Clicker），0=被点击者（Clickee）；高位定义目标，映射方式与施法者位相同。
你可以使用该表查询实际值：

| 施法者   | 目标     | cast\_flags 值 |
| -------- | -------- | -------------- |
| 生物     | 被点击者 | 0              |
| 点击者   | 被点击者 | 1              |
| 被点击者 | 点击者   | 2              |
| 点击者   | 点击者   | 3              |

### user\_type

与召唤者的关系：定义谁可以使用此法术点击（spellclick）。

| 值 | 描述   |
| -- | ------ |
| 0  | 仅自己 |
| 1  | 友好   |
| 2  | 团队   |
| 3  | 小队   |

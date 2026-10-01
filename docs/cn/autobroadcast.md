# autobroadcast

[<-返回:Auth](database-auth)

**\`autobroadcast\` 表**

该表包含你各个服务器的自动广播条目。诸如活动、位置和定时（\*.On、\*.Center、\*.Timer）等配置在 [worldserver.conf](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/worldserver/worldserver.conf.dist) 中定义。条目会根据其权重被随机选中。

**表结构**

| Field        | Type     | Attributes | Key | Null | Default | Extra          | Comment |
| ------------ | -------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [realmid][1] | INT      | SIGNED     | PRI | NO   | -1      |                |         |
| [id][2]      | TINYINT  | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [weight][3]  | TINYINT  | UNSIGNED   |     | YES  | 1       |                |         |
| [text][4]    | LONGTEXT | SIGNED     |     | NO   |         |                |         |

[1]: #realmid
[2]: #id
[3]: #weight
[4]: #text

**字段说明**

### realmid

[realmlist.id](realmlist#id)。定义该条目属于哪个服务器。使用 **-1** 表示在所有服务器上加载该条目。

### id

每个服务器的唯一标识键。具有相同 id 的条目会相互覆盖且不会产生警告——这可用于在特定服务器上替换 -1 realmid 条目。

### weight

一个非负整数。权重越高的条目被选中的几率越大。

### text

要广播的文本。可以使用颜色以及物品/法术/任务链接的格式化代码。

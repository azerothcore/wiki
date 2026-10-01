# 客户端缓存 (wdb)

客户端会把服务器发送给它的部分数据缓存在 `.wdb` 文件中，这些文件存储在 WoW 目录内的 `Cache/WDB/<locale>` 中。当这些数据在服务器端发生变化时，客户端会继续显示旧版本，直到相关缓存文件被删除。

规则是：客户端以**查询响应（query response）**形式收到的任何数据都会被写入缓存文件。服务器在正常交互过程中推送的数据不会被缓存。

| 世界表 | 查询响应 | 缓存文件 | 影响 |
|---|---|---|---|
| [item_template](item_template) | `SMSG_ITEM_QUERY_SINGLE_RESPONSE` | `itemcache.wdb` | 物品名称、描述、属性、显示 ID、品质、图标 |
| [creature_template](creature_template) | `SMSG_CREATURE_QUERY_RESPONSE` | `creaturecache.wdb` | 生物名称、副名/称号、显示 ID、类型 |
| [gameobject_template](gameobject_template) | `SMSG_GAMEOBJECT_QUERY_RESPONSE` | `gameobjectcache.wdb` | 游戏对象名称、显示 ID、类型 |
| [quest_template](quest_template) | `SMSG_QUEST_QUERY_RESPONSE` | `questcache.wdb` | 任务标题、描述、目标、完成文本 |
| [page_text](page_text) | `SMSG_PAGE_TEXT_QUERY_RESPONSE` | `pagetextcache.wdb` | 书籍、卷轴和铭牌文字 |
| [npc_text](npc_text) | `SMSG_NPC_TEXT_UPDATE` | `npccache.wdb` | NPC 问候语和对话文本 |

Gossip 是常见的困惑来源。[gossip_menu](gossip_menu) 和 [gossip_menu_option](gossip_menu_option) 会在玩家每次与 NPC 交谈时通过 `SMSG_GOSSIP_MESSAGE` 实时发送，因此对它们的修改会立即生效，无需清除缓存。只有来自 [npc_text](npc_text) 的正文文本会被缓存。

此列表涵盖了最常被编辑的世界表，而非所有被缓存的字段。由于整个查询响应都会被缓存，请将客户端显示的任何字段都视为已缓存，即使上面没有列出。

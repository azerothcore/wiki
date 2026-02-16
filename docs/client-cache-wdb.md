# Client Cache (wdb)

You can see below what's cache by the client and theorically should need to be cleared in the case of changing any content of those databases.

Cache is not exclusive to a `Database Table` but to certain parts of the `Database Table` (equivalent on the Client side).

All `Database Tables` below require in theory cache clearing (of the client) when changing them, could be in their entirety  or just one field.

| Database Tables | Packet | Client Cache File | Description |
|-----------------|-------------------------------|---------------------|-------------------------------------------------------------|
| [item_template](item_template) | `SMSG_ITEM_QUERY_RESPONSE` | itemcache.wdb | Item name, description, stats, display ID, quality, icons |
| [creature_template](creature_template) | `SMSG_CREATURE_QUERY_RESPONSE` | creaturecache.wdb | Creature name, subname/title, display ID, type |
| [gameobject_template](gameobject_template) | `SMSG_GAMEOBJECT_QUERY_RESPONSE` | gameobjectcache.wdb | Gameobject name, display ID, type |
| [quest_template](quest_template) | `SMSG_QUEST_QUERY_RESPONSE` | questcache.wdb | Quest title, description, objectives, completion text |
| [page_text](page_text) | `SMSG_PAGE_TEXT_QUERY_RESPONSE` | pagetextcache.wdb | Book/scroll/plaque text |
| [npc_text](npc_text), [gossip_menu](gossip_menu), [gossip_menu_option](gossip_menu_option) | `SMSG_NPC_TEXT_UPDATE`, `SMSG_GOSSIP_MESSAGE` | npccache.wdb (merged with others) | NPC dialogue, gossip menus, greetings |

The table above doesn't mean it's all `Database Tables` if changed that require a client cache clearing, it's at least something, better than guessing majority of the time, there's no currently much information to what each field may or not be cached and requires the file to be or not deleted.


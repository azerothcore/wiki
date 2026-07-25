# Client Cache (wdb)

The client caches part of the data the server sends it in `.wdb` files, stored in `Cache/WDB/<locale>` inside the WoW folder. When that data changes server-side, the client keeps displaying the old version until the relevant cache file is deleted.

The rule is: anything the client receives as a **query response** gets written to a cache file. Data the server pushes during normal interaction is not cached.

| World table | Query response | Cache file | Affects |
|---|---|---|---|
| [item_template](item_template) | `SMSG_ITEM_QUERY_SINGLE_RESPONSE` | `itemcache.wdb` | Item name, description, stats, display ID, quality, icons |
| [creature_template](creature_template) | `SMSG_CREATURE_QUERY_RESPONSE` | `creaturecache.wdb` | Creature name, subname/title, display ID, type |
| [gameobject_template](gameobject_template) | `SMSG_GAMEOBJECT_QUERY_RESPONSE` | `gameobjectcache.wdb` | Gameobject name, display ID, type |
| [quest_template](quest_template) | `SMSG_QUEST_QUERY_RESPONSE` | `questcache.wdb` | Quest title, description, objectives, completion text |
| [page_text](page_text) | `SMSG_PAGE_TEXT_QUERY_RESPONSE` | `pagetextcache.wdb` | Book, scroll and plaque text |
| [npc_text](npc_text) | `SMSG_NPC_TEXT_UPDATE` | `npccache.wdb` | NPC greeting and dialogue text |

Gossip is a common source of confusion. [gossip_menu](gossip_menu) and [gossip_menu_option](gossip_menu_option) are sent live with `SMSG_GOSSIP_MESSAGE` every time a player talks to an NPC, so edits to them show up immediately and need no cache clearing. Only the text body from [npc_text](npc_text) is cached.

This list covers the world tables that are edited most often, not every cached field. Because the entire query response is cached, treat any field the client displays as cached, even if it is not named above.

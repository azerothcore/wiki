# gossip\_menu

[<-Back-to:World](database-world)

**The \`gossip\_menu\` table**

This table is used for displaying gossip when a player talks to an NPC with [npcflag](creature_template#npcflag) set.

**Table Structure**

| Field       | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [MenuID][1] | SMALLINT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [TextID][2] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |

[1]: #menuid
[2]: #textid

**Description of the fields**

### MenuID

This must match the entry you added to [creature\_template.gossip\_menu\_id](creature_template#gossip_menu_id). This also
groups the options from gossip\_menu\_option and displays all options associated with this ID.

**Note:** If adding your own custom menu options, then it is common practice to start with an ID at or above 90,000 just to be safe that it doesn't conflict with other gossip menu id's.

### TextID

This links to the [npc\_text.ID](npc_text#id) for the gossip you want to be initially displayed. Also this tells the NPC what to say at the top of the options menu when it is displayed.

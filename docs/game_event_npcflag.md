# game\_event\_npcflag

[<-Back-to:World](database-world)

**The \`game\_event\_npcflag\` table**

This table contains npcflags that are to be added to an NPC when the specified event is active for the creature with the given guid.

**Table: game\_event\_npcflag's Structure**

| Field                     | Type    |          | Null | Key | Default | Extra | Comment                 |
| :------------------------ | :------ | :------- | :--: | :-: | :-----: | :---: | :---------------------- |
| [eventEntry](#evententry) | TINYINT | UNSIGNED | NO   | PRI |         |       | Entry of the game event |
| [guid](#guid)             | INT     | UNSIGNED | NO   | PRI | 0       |       |                         |
| [npcflag](#npcflag)       | INT     | UNSIGNED | NO   |     | 0       |       |                         |

**Description of the table's fields**

### eventEntry

The eventEntry that is tied to this npcflag change.

### guid

The guid of the creature that you want to change npcflag for.

### npcflag

The npcflags that you want to set. The value specified here is bitwise added to the npcflag already set on the NPC.

So, if you want the creature to be also a quest giver, just put 2 in this column.

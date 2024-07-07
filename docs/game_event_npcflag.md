# game\_event\_npcflag

[<-Back-to:World](database-world)

**The \`game\_event\_npcflag\` table**

This table contains npcflags that are to be added to an NPC when the specified event is active for the creature with the given guid.

**Table Structure**

| Field           | Type      | Attributes | Key | Null | Default | Extra | Comment                 |
| --------------- | --------- | ---------- | --- | ---- | ------- | ----- | ----------------------- |
| [eventEntry][1] | TINYINT   | UNSIGNED   | PRI | NO   |         |       | Entry of the game event |
| [guid][2]       | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |                         |
| [npcflag][3]    | INT       | UNSIGNED   |     | NO   | 0       |       |                         |

[1]: #evententry
[2]: #guid
[3]: #npcflag

**Description of the fields**

### eventEntry

The eventEntry that is tied to this npcflag change.

### guid

The guid of the creature that you want to change npcflag for.

### npcflag

The npcflags that you want to set. The value specified here is bitwise added to the npcflag already set on the NPC.

So, if you want the creature to be also a quest giver, just put 2 in this column.

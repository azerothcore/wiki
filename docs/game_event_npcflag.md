# game\_event\_npcflag

[<-Back-to:World](database-world.md)

**The \`game\_event\_npcflag\` table**

This table contains npcflags that are to be added to an NPC when the specified event is active for the creature with the given guid.

**Structure**

| Field           | Type         | Attributes | Key | Null | Default | Extra | Comment                 |
|-----------------|--------------|------------|-----|------|---------|-------|-------------------------|
| [eventEntry][1] | TINYINT(3)   | unsigned   | PRI | NO   |         |       | Entry of the game event |
| [guid][2]       | MEDIUMINT(8) | unsigned   | PRI | NO   | 0       |       |                         |
| [npcflag][3]    | int(10)      | unsigned   |     | NO   | 0       |       |                         |

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

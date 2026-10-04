# creature\_sparring

[<-Back-to:World](database-world)

**The \`creature\_sparring\` table**

Stores the sparring health threshold for a creature. While sparring, a creature will not be brought below the configured health percentage by other sparring creatures (used to keep training/duelling NPCs alive). `GUID` references `creature.guid`.

**Table: creature\_sparring's Structure**

| Field                       | Type  |          | Null | Key | Default | Extra | Comment |
| :-------------------------- | :---- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [GUID](#guid)               | INT   | UNSIGNED | NO   | PRI |         |       |         |
| [SparringPCT](#sparringpct) | FLOAT |          | NO   |     |         |       |         |

**Description of the table's fields**

### GUID

References `creature.guid` – the spawned creature this rule applies to.

### SparringPCT

Health percentage below which the creature will not be damaged by other sparring partners.

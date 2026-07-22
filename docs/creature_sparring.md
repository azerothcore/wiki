# creature_sparring

[<-Back-to:World](database-world)

**The `creature_sparring` table**

Stores the sparring health threshold for a creature. While sparring, a creature will not be brought below the configured health percentage by other sparring creatures (used to keep training/duelling NPCs alive). `GUID` references `creature.guid`.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [GUID](#guid) | INT | UNSIGNED | PRI | NO |  |  |  |
| [SparringPCT](#sparringpct) | FLOAT | SIGNED |  | NO |  |  |  |

**Description of the fields**

### GUID

References `creature.guid` – the spawned creature this rule applies to.

### SparringPCT

Health percentage below which the creature will not be damaged by other sparring partners.

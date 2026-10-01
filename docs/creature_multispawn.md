# creature_multispawn

[<-Back-to:World](database-world)

**The `creature_multispawn` table**

Allows a single creature spawn point to be represented by more than one `creature_template` entry. Each row links a spawn (`creature.guid`, stored in `spawnId`) to a `creature_template.entry` that may be used for that spawn, letting the same guid appear as one of several possible creatures.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [spawnId](#spawnid) | INT | UNSIGNED | PRI | NO |  |  | creature.guid |
| [entry](#entry) | INT | UNSIGNED | PRI | NO |  |  | creature_template.entry |

**Description of the fields**

### spawnId

References `creature.guid` – the spawn this entry applies to.

### entry

References `creature_template.entry` – a template that may be spawned for this `spawnId`.

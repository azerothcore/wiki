# creature\_multispawn

[<-Back-to:World](database-world)

**The \`creature\_multispawn\` table**

Allows a single creature spawn point to be represented by more than one `creature_template` entry. Each row links a spawn (`creature.guid`, stored in `spawnId`) to a `creature_template.entry` that may be used for that spawn, letting the same guid appear as one of several possible creatures.

**Table: creature\_multispawn's Structure**

| Field               | Type |          | Null | Key | Default | Extra | Comment                 |
| :------------------ | :--- | :------- | :--: | :-: | :-----: | :---: | :---------------------- |
| [spawnId](#spawnid) | INT  | UNSIGNED | NO   | PRI |         |       | creature.guid           |
| [entry](#entry)     | INT  | UNSIGNED | NO   | PRI |         |       | creature_template.entry |

**Description of the table's fields**

### spawnId

References `creature.guid` – the spawn this entry applies to.

### entry

References `creature_template.entry` – a template that may be spawned for this `spawnId`.

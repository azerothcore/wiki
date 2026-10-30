# pool\_quest

[<-Back-to:World](database-world)

**The \`pool\_quest\` table**

This table contains a list of quests that are tied to a specific pool.

**Table: pool\_quest's Structure**

| Field                       | Type         |          | Null | Key | Default | Extra | Comment |
| :-------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [entry](#entry)             | INT          | UNSIGNED | NO   | PRI | 0       |       |         |
| [pool_entry](#poolentry)    | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [description](#description) | VARCHAR(255) |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### entry

Quest [id](quest_template#id).

### pool\_entry

The [pool](pool_template#entry) that this quest is in. Refers to [pool\_template entry](pool_template#entry).

### description

A human-readable description or comment for this pool quest entry.

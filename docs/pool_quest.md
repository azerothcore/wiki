# pool\_quest

[<-Back-to:World](database-world)

**The \`pool\_quest\` table**

This table contains a list of quests that are tied to a specific pool.

**Table Structure**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]       | INT          | UNSIGNED   | PRI | NO   | 0       |       |         |
| [pool_entry][2]  | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [description][3] | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |

[1]: #entry
[2]: #pool_entry
[3]: #description

**Description of the fields**

### entry

Quest [id](quest_template#id).

### pool\_entry

The [pool](pool_template#entry) that this quest is in. Refers to [pool\_template entry](pool_template#entry).

### description

`field-no-description|3`

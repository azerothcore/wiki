# pool\_quest\_save

[<-Back-to:Characters](database-characters)

**The \`pool\_quest\_save\` table**

Stores which quests of each quest pool are currently active.

**Table: pool\_quest\_save's Structure**

| Field                | Type |          | Null | Key | Default | Extra | Comment |
| :------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [pool_id](#poolid)   | INT  | UNSIGNED | NO   | PRI | 0       |       |         |
| [quest_id](#questid) | INT  | UNSIGNED | NO   | PRI | 0       |       |         |

**Description of the table's fields**

### pool\_id

[pool\_quest.entry](pool_quest#entry).

### quest\_id

[quest\_template.id](quest_template#id).

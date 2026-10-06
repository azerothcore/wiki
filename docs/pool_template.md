# pool\_template

[<-Back-to:World](database-world)

**The \`pool\_template\` table**

Each unique pool is defined in this table.

**Table: pool\_template's Structure**

| Field                       | Type         |          | Null | Key | Default | Extra | Comment                               |
| :-------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------------------------------------ |
| [entry](#entry)             | INT          | UNSIGNED | NO   | PRI | 0       |       | Pool entry                            |
| [max_limit](#maxlimit)      | INT          | UNSIGNED | NO   |     | 0       |       | Max number of objects (0) is no limit |
| [description](#description) | VARCHAR(255) |          | YES  |     | NULL    |       |                                       |

**Description of the table's fields**

### entry

The pool ID. This is an arbitrary number that is only used to link the gameobjects, creatures or quests in this pool.

### max\_limit

This is the maximum number of objects that should be spawned in this pool.
0 is no limit.

### description

Field describes the basic information about what the pool refers to. Example: Snarlflare (14272)

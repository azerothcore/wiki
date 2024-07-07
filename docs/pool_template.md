# pool\_template

[<-Back-to:World](database-world)

**The \`pool\_template\` table**

Each unique pool is defined in this table.

**Table Structure**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment                               |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------------------------------- |
| [entry][1]       | MEDIUMINT    | UNSIGNED   | PRI | NO   | 0       |       | Pool entry                            |
| [max_limit][2]   | INT          | UNSIGNED   |     | NO   | 0       |       | Max number of objects (0) is no limit |
| [description][3] | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |                                       |

[1]: #entry
[2]: #max_limit
[3]: #description

**Description of the fields**

### entry

The pool ID. This is an arbitrary number that is only used to link the gameobjects, creatures or quests in this pool.

### max\_limit

This is the maximum number of objects that should be spawned in this pool.
0 is no limit.

### description

Field describes the basic information about what the pool refers to. Example: Snarlflare (14272)

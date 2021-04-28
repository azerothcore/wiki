# pool\_template

[<-Back-to:World](database-world.md)

**The \`pool\_template\` table**

Each unique pool is defined in this table.

**Structure**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment                               |
|------------------|--------------|------------|-----|------|---------|-------|---------------------------------------|
| [entry][1]       | mediumint(8) | unsigned   | PRI | NO   | 0       |       | Pool entry                            |
| [max_limit][2]   | int(10)      | unsigned   |     | NO   | 0       |       | Max number of objects (0) is no limit |
| [description][3] | VARCHAR(255) | signed     |     | YES  | NULL    |       |                                       |

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

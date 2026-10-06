# pool\_pool

[<-Back-to:World](database-world)

**The \`pool\_pool\` table**

This is the pool of pools table. You can create a pool with a chance of a range of pools in that pool being activated.

**Table: pool\_pool's Structure**

| Field                       | Type         |          | Null | Key | Default | Extra | Comment |
| :-------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [pool_id](#poolid)          | INT          | UNSIGNED | NO   | PRI | 0       |       |         |
| [mother_pool](#motherpool)  | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [chance](#chance)           | FLOAT        |          | NO   |     | 0       |       |         |
| [description](#description) | VARCHAR(255) |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### pool\_id

The ID of the [pool\_template](pool_template)) that you want to include in this "pool of pools" as a child pool.

### mother\_pool

The ID of the [pool\_template](pool_template)) that defines this "pool of pools".

### chance

The explicit percentage chance that this child pool will be spawned.

If the mother pool spawns just one child pool (max\_limit = 1 in the respective mother pool's [pool\_template](pool_template), the core selects the child pool to be spawned in a two-step process: First, only the explicitly-chanced (chance > 0) child pools of the mother pool are rolled. If this roll does not produce any child pool, all the child pools without an explicit chance (chance = 0) are rolled with equal chance.

If the mother pool spawns more than one child pool, the chance is ignored and all the child pools in the mother pool are rolled in one step with equal chance.

In case the mother pool spawns just one child pool and all the child pools have a nonzero chance, the sum of the chances for all the child pools must equal to 100, otherwise the mother pool won't function correctly.

### description

A text field to describe what this pool of pools is for.

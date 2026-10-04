# pool\_gameobject

[<-Back-to:World](database-world)

**The \`pool\_gameobject\` table**

This table contains gameobjects that are tied to a specific pool.
This table can only contain gameobjects that have a type of GAMEOBJECT\_TYPE\_CHEST, GAMEOBJECT\_TYPE\_GOOBER, GAMEOBJECT\_TYPE\_FISHINGHOLE.

**Table: pool\_gameobject's Structure**

| Field                       | Type         |          | Null | Key | Default | Extra | Comment |
| :-------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guid](#guid)               | INT          | UNSIGNED | NO   | PRI | 0       |       |         |
| [pool_entry](#poolentry)    | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [chance](#chance)           | FLOAT        |          | NO   |     | 0       |       |         |
| [description](#description) | VARCHAR(255) |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### guid

[gameobject.guid](gameobject#guid)

### pool\_entry

The pool that this gameobject is in. Refers to [pool\_template.entry](pool_template#entry).

### chance

The explicit percentage chance that this gameobject will be spawned.

If the pool spawns just one gameobject (max\_limit = 1 in the respective [pool\_template](pool_template)), the core selects the gameobject to be spawned in a two-step process: First, only the explicitly-chanced (chance &gt; 0) gameobjects of the pool are rolled. If this roll does not produce any gameobject, all the gameobjects without an explicit chance (chance = 0) are rolled with equal chance.

If the pool spawns more than one gameobject, the chance is ignored and all the gameobjects in the pool are rolled in one step with equal chance.

In case the pool spawns just one gameobject and all the gameobjects have a nonzero chance, the sum of the chances for all the gameobjects must equal to 100, otherwise the pool won't be spawned.

Value must be >=0. If the value does not meet the condition the SQL will fail on `pool_gameobject_chk_1`.

### description

This field usually names the game object corresponding to the guid and mentions which spawn point it is. Example: Spawn Point 4 - Tin Vein

# pool\_creature

[<-Back-to:World](database-world)

**The \`pool\_creature\` table**

This table contains a list of creatures that are tied to a specific pool.

**Table Structure**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]        | INT          | UNSIGNED   | PRI | NO   | 0       |       |         |
| [pool_entry][2]  | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [chance][3]      | FLOAT        | UNSIGNED   |     | NO   | 0       |       |         |
| [description][4] | VARCHAR(255) |            |     | YES  | NULL    |       |         |

[1]: #guid
[2]: #pool_entry
[3]: #chance
[4]: #description

**Description of the fields**

### guid

[creature.guid](creature#guid)

### pool\_entry

The pool that this creature is in. Refers to [pool\_template.entry](pool_template#entry).

### chance

The explicit percentage chance that this creature will be spawned.

If the pool spawns just one creature (max\_limit = 1 in the respective [pool\_template](pool_template)), the core selects the creature to be spawned in a two-step process: First, only the explicitly-chanced (chance &gt; 0) creatures of the pool are rolled. If this roll does not produce any creature, all the creatures without an explicit chance (chance = 0) are rolled with equal chance.

If the pool spawns more than one creature, the chance is ignored and all the creatures in the pool are rolled in one step with equal chance.

In case the pool spawns just one creature and all the creatures have a nonzero chance, the sum of the chances for all the creatures must equal to 100, otherwise the pool won't be spawned.

Value must be >=0. If the value does not meet the condition the SQL will fail on `pool_creature_chk_1`.

### description

This field usually names the creature corresponding to the guid and mentions which spawn point it is. Example: Snarlflare (14272) - Spawn 1

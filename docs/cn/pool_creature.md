# pool\_creature

[<-返回至:World](database-world)

**\`pool\_creature\` 表**

此表包含关联到特定刷新池（pool）的生物列表。

**表结构**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]        | INT          | UNSIGNED   | PRI | NO   | 0       |       |         |
| [pool_entry][2]  | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [chance][3]      | FLOAT        | UNSIGNED   |     | NO   | 0       |       |         |
| [description][4] | VARCHAR(255) |            |     | YES  | NULL    |       |         |

[1]: #guid
[2]: #poolentry
[3]: #chance
[4]: #description

**字段说明**

### guid

[creature.guid](creature#guid)

### pool\_entry

该生物所属的刷新池。指向 [pool\_template.entry](pool_template#entry)。

### chance

该生物被刷新的明确百分比几率。

如果刷新池只刷出一个生物（对应 [pool\_template](pool_template) 中 max\_limit = 1），核心会通过两步流程选择要刷新的生物：首先，只对池中具有明确几率（chance &gt; 0）的生物进行抽取。如果这次抽取没有产生任何生物，则所有没有明确几率（chance = 0）的生物将以相同几率被抽取。

如果刷新池刷出多个生物，则几率会被忽略，池中所有生物将一步到位地以相同几率被抽取。

如果刷新池只刷出一个生物，且所有生物都具有非零几率，那么所有生物的几率之和必须等于 100，否则该刷新池将不会被刷新。

值必须 >=0。如果该值不满足条件，SQL 将在 `pool_creature_chk_1` 上失败。

### description

此字段通常标明与 guid 对应的生物名称，并指出它是哪个刷新点。示例：Snarlflare (14272) - Spawn 1

# pool\_pool

[<-返回至:World](database-world)

**\`pool\_pool\` 表**

这是"池中池"（pool of pools）表。你可以创建一个刷新池，并让该池中的一系列子池按一定几率被激活。

**表结构**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [pool_id][1]     | MEDIUMINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [mother_pool][2] | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [chance][3]      | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [description][4] | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |

[1]: #poolid
[2]: #motherpool
[3]: #chance
[4]: #description

**字段说明**

### pool\_id

你想要作为子池包含进此"池中池"的 [pool\_template](pool_template)) 的 ID。

### mother\_pool

定义此"池中池"的 [pool\_template](pool_template)) 的 ID。

### chance

此子池被刷新的明确百分比几率。

如果母池只刷出一个子池（对应母池的 [pool\_template](pool_template) 中 max\_limit = 1），核心会通过两步流程选择要刷新的子池：首先，只对母池中具有明确几率（chance > 0）的子池进行抽取。如果这次抽取没有产生任何子池，则所有没有明确几率（chance = 0）的子池将以相同几率被抽取。

如果母池刷出多个子池，则几率会被忽略，母池中的所有子池将一步到位地以相同几率被抽取。

如果母池只刷出一个子池，且所有子池都具有非零几率，那么所有子池的几率之和必须等于 100，否则母池将无法正常工作。

### description

用于描述此"池中池"用途的文本字段。

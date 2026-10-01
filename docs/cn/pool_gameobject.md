# pool\_gameobject

[<-返回至:World](database-world)

**\`pool\_gameobject\` 表**

此表包含关联到特定刷新池（pool）的游戏对象。
此表只能包含类型为 GAMEOBJECT\_TYPE\_CHEST、GAMEOBJECT\_TYPE\_GOOBER、GAMEOBJECT\_TYPE\_FISHINGHOLE 的游戏对象。

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

[gameobject.guid](gameobject#guid)

### pool\_entry

该游戏对象所属的刷新池。指向 [pool\_template.entry](pool_template#entry)。

### chance

该游戏对象被刷新的明确百分比几率。

如果刷新池只刷出一个游戏对象（对应 [pool\_template](pool_template) 中 max\_limit = 1），核心会通过两步流程选择要刷新的游戏对象：首先，只对池中具有明确几率（chance &gt; 0）的游戏对象进行抽取。如果这次抽取没有产生任何游戏对象，则所有没有明确几率（chance = 0）的游戏对象将以相同几率被抽取。

如果刷新池刷出多个游戏对象，则几率会被忽略，池中所有游戏对象将一步到位地以相同几率被抽取。

如果刷新池只刷出一个游戏对象，且所有游戏对象都具有非零几率，那么所有游戏对象的几率之和必须等于 100，否则该刷新池将不会被刷新。

值必须 >=0。如果该值不满足条件，SQL 将在 `pool_gameobject_chk_1` 上失败。

### description

此字段通常标明与 guid 对应的游戏对象名称，并指出它是哪个刷新点。示例：Spawn Point 4 - Tin Vein

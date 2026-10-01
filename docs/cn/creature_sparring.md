# creature_sparring

[<-返回：世界](database-world)

**`creature_sparring` 表**

存储生物的切磋（sparring）生命值阈值。在切磋期间，生物不会因其他切磋生物的攻击而低于所配置的生命值百分比（用于保持训练/决斗 NPC 存活）。`GUID` 引用 `creature.guid`。

**表结构**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [GUID](#guid) | INT | UNSIGNED | PRI | NO |  |  |  |
| [SparringPCT](#sparringpct) | FLOAT | SIGNED |  | NO |  |  |  |

**字段说明**

### GUID

引用 `creature.guid` —— 此规则所适用的已刷新生灵。

### SparringPCT

生命值百分比，低于该百分比时，生物将不会受到其他切磋伙伴的伤害。

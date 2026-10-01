# creature_multispawn

[<-返回：世界](database-world)

**`creature_multispawn` 表**

允许单个生物刷新点由多个 `creature_template` 条目来表示。每一行都将一个刷新点（`creature.guid`，存储在 `spawnId` 中）与可用于该刷新点的 `creature_template.entry` 关联起来，使同一个 guid 可以表现为多种可能的生物之一。

**表结构**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [spawnId](#spawnid) | INT | UNSIGNED | PRI | NO |  |  | creature.guid |
| [entry](#entry) | INT | UNSIGNED | PRI | NO |  |  | creature_template.entry |

**字段说明**

### spawnId

引用 `creature.guid` —— 该条目所适用的刷新点。

### entry

引用 `creature_template.entry` —— 可能为该 `spawnId` 刷新的模板。

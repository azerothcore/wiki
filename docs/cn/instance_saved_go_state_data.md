# instance_saved_go_state_data

[<-返回至:Characters](database-characters)

**`instance_saved_go_state_data` 表**

持久化已绑定副本内游戏对象（例如保持打开的门或拉杆）的已保存状态，以便在副本重新加载时恢复该状态。以副本 `id` 和游戏对象 `guid` 作为键。

**表结构**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id](#id) | INT | UNSIGNED | PRI | NO |  |  | instance.id |
| [guid](#guid) | INT | UNSIGNED | PRI | NO |  |  | gameobject.guid |
| [state](#state) | TINYINT | UNSIGNED |  | YES | 0 |  | gameobject.state |

**字段说明**

### id

引用 `instance.id` —— 已保存的副本。

### guid

引用 `gameobject.guid` —— 其状态被保存的游戏对象。

### state

游戏对象已保存的 `GOState`（例如 active/ready）。

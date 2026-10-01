# trainer

[<-返回:世界数据库](database-world)

**\`trainer\` 表**

该表包含唯一的训练师模板（trainer template）。

**表结构**

| Field                           | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Id](#id)                       | INT        | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Type](#type)                   | TINYINT    | UNSIGNED   |     | NO   | 2       |       |         |
| [Requirement](#requirement)     | MEDIUMINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [Greeting](#greeting)           | MEDIUMTEXT |            |     | NO   |         |       |         |
| [VerifiedBuild](#verifiedbuild) | INT        |            |     | YES  | 0       |       |         |

**字段说明**

### ID

唯一的训练师 ID

### Type

| Type | Description |
| ---- | ----------- |
| 0    | Class       |
| 1    | Mount       |
| 2    | Tradeskill  |
| 3    | Pet         |

### Requirement

没有要求时保持为 0。

| Type       | Requirement                              | Description                                             |
| ---------- | ---------------------------------------- | ------------------------------------------------------- |
| Class      | [ChrClasses.Content](chrclasses#content) | 玩家必须是该职业才能在此训练师处学习。 |
| Mount      | [ChrRaces](chrraces#content)             | 玩家必须是该种族才能在此训练师处学习。  |
| TradeSkill | Spell ID                                 | 玩家必须掌握该法术才能在此训练师处学习。 |
| Pet        | [ChrClasses.Content](chrclasses#content) | 玩家必须是该职业才能在此训练师处学习。 |

### Greeting

打开训练师窗口时显示的文本。

这不是闲聊（gossip）文本。

### VerifiedBuild

该字段用于确定此游戏物体是否来源于经过验证的嗅探（sniff）数据。

如果值为 0，则表示它尚未被解析，或者继承自旧的数据库或其他核心。

如果值大于 0，则表示它是使用该特定客户端构建版本的嗅探数据解析的。

如果值为 -Client Build，则表示它是使用该特定客户端构建版本的 WDB 文件解析的，后来因某些特殊需要而被手动编辑。

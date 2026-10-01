# quest\_greeting

[<-返回至:World](database-world)

**\`quest_greeting\` 表**

此表为 NPC 或游戏对象添加问候行为。

**表结构**

| Field                | Type      | Attributes | Key | NULL | Default | Comment |
| -------------------- | --------- | ---------- | --- | ---- | ------- | ------- |
| [ID][1]              | MEDIUMINT | UNSIGNED   | Yes | NO   | 0       |         |
| [Type][2]            | TINYINT   | UNSIGNED   | Yes | NO   | 0       |         |
| [GreetEmoteType][3]  | SMALLINT  | UNSIGNED   | NO  | NO   | 0       |         |
| [GreetEmoteDelay][4] | INT       | UNSIGNED   | NO  | NO   | 0       |         |
| [Greeting][5]        | TEXT      |            | NO  | YES  | NULL    |         |
| [VerifiedBuild][6]   | SMALLINT  | SIGNED     | NO  | NO   | 0       |         |

[1]: #id
[2]: #type
[3]: #greetemotetype
[4]: #greetemotedelay
[5]: #greeting
[6]: #verifiedbuild

**字段说明：**

### ID

唯一 ID（[creature_template.entry](creature_template#entry) 或 [gameobject\_template.entry](gameobject_template#entry)）

### Type

-   0=生物（Creature）（ID 指向 creature\_template.entry）
-   1=游戏对象（GameObject）（ID 指向 gameobject\_template.entry）

### GreetEmoteType

任务 NPC 的 [表情](emotes)

### GreetEmoteDelay

以毫秒为单位的表情延迟

### Greeting

要显示的文本

### VerifiedBuild

此字段用于确定一个模板是否已通过 WDB 文件验证。

- 如果值为 0，则表示尚未解析。
- 如果值大于 0，则表示已使用该特定客户端 build 的 WDB 文件进行了解析。
- 如果值为 -1，则只是一个占位符，直到在 WDB 中找到正确的数据。
- 如果值为 -Client Build，则表示已使用该特定客户端 build 的 WDB 文件进行了解析，并出于某些特殊需要稍后进行了手动编辑。

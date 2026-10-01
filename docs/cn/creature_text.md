# creature\_text

# 表：creature\_text

**简介：**

该表保存了 [SMART\_SCRIPTS](http://www.azerothcore.org/wiki/smart_scripts) 表和核心脚本所使用的所有语音文本（气泡和聊天窗口中的低语、说、喊、表情文本）。

**详细介绍：**

你是否曾好奇像 ***辛达苟萨***（→ [wowhead](http://www.wowhead.com/npc=36853/sindragosa)）这样的 BOSS 是如何被脚本化的？无需再好奇，你可以亲眼看到！(→ [辛达苟萨脚本文件](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/scripts/Northrend/IcecrownCitadel/boss_sindragosa.cpp))

我知道，我知道——这看起来极其复杂，超过 1600 行代码！但没必要一次就理解所有内容。让我们聚焦于一些简单但非常重要的东西，好吗？

如果你查看代码的开头，可以找到一个名为 *Texts* 的 *enum*，它由 12 个元素组成（数字从 0 到 11），让我们仔细看看这个 *enum* 的第一个元素：

**boss\_sindragosa.cpp** 展开源码

```cpp
 enum Texts
 {
     SAY_AGGRO = 0, // You are fools to have come to this place! The icy winds of Northrend will consume your souls!
     ...
 };
```

你可以亲自在游戏中验证，当你开始与她战斗时，***辛达苟萨*** 会喊出这段话。
你是否注意到了一些有趣的事情？实际文本位于 // 之后，这意味着这些信息是注释，
我们的编译器会忽略它。另一方面，我们清楚地看到她确实喊出了那段话，这怎么可能呢？

## 这些信息存储在哪里？我该如何找到它？

你可能会说——这有 1600 多行，肯定有什么东西，只是我们还没找到。
我可以向你保证，你找不到任何东西，如果你不信，就用 CTRL+F 快捷键搜索一番找找乐子吧！

什么都没有？真遗憾，但也许、也许你还有机会发现点什么？

**boss\_sindragosa.cpp** 展开源码

```cpp
 void EnterCombat(Unit* victim) override
 {
     ...
     Talk(SAY_AGGRO); // interesting!
 }
```

你看到这个函数的最后一行了吗？他们使用了某些本不该起作用的东西！
我们可以推断，当 ***辛达苟萨*** 进入战斗时（看看函数名！）会调用这个函数，
所以现在我们明白为什么她在开始时喊话了。

仍然有一个根本性的问题——这段文本的信息存储在哪里？答案比你想象的要简单。
它存储在 **CREATURE\_TEXT** 表中！

*未完待续...*

## 结构

| 字段                 | 类型         | 属性          | 键 | 空 | 默认值 | 额外 | 注释                     |
|-----------------------|--------------|-----------------|-----|------|---------|-------|-------------------------|
| [CreatureID][1]       | MEDIUMINT | UNSIGNED        | PRI | NO   |         |       | creature_template entry |
| [GroupID][2]          | TINYINT   | UNSIGNED        | PRI | NO   |         |       |                         |
| [ID][3]               | TINYINT   | UNSIGNED        | PRI | NO   |         |       |                         |
| [Text][4]             | longtext     | utf8_general_ci |     | YES  | NULL    |       |                         |
| [Type][5]             | TINYINT   | UNSIGNED        |     | NO   |         |       |                         |
| [Language][6]         | TINYINT   | UNSIGNED        |     | NO   |         |       |                         |
| [Probability][7]      | FLOAT        | SIGNED          |     | NO   |         |       |                         |
| [Emote][8]            | MEDIUMINT | UNSIGNED        |     | NO   |         |       |                         |
| [Duration][9]         | MEDIUMINT | UNSIGNED        |     | NO   |         |       |                         |
| [Sound][10]           | MEDIUMINT | UNSIGNED        |     | NO   |         |       |                         |
| [BroadcastTextId][11] | MEDIUMINT | SIGNED          |     | NO   |         |       |                         |
| [TextRange][12]       | TINYINT   | UNSIGNED        |     | NO   |         |       |                         |
| [comment][13]         | VARCHAR(255) | utf8_general_ci |     | YES  | NULL    |       |                         |

[1]: #creatureid
[2]: #groupid
[3]: #id
[4]: #text
[5]: #type
[6]: #language
[7]: #probability
[8]: #emote
[9]: #duration
[10]: #sound
[11]: #broadcasttextid
[12]: #textrange
[13]: #comment

## 字段说明

### CreatureID

这是脚本所关联的 [creature\_template.entry](http://www.azerothcore.org/wiki/creature_template#creature_template-entry)。

### GroupID

如果同一个 entry 有多个条目（生物说的文本不止一条），此列用于决定是随机说还是按顺序列出。如果一个生物有多个需要按给定顺序显示的文本，那么每个匹配的新条目都必须递增（例如 0、1、2、3...）。如果只有一个条目或只有一个组，此值应为 0。如果有多个文本组，此值在组内保持不变，而 id 在同一组内递增。

来自暴风城卫兵（生物 68）的示例：

| CreatureID | GroupID | ID  | Text                                                                                                                       |
|------------|---------|-----|----------------------------------------------------------------------------------------------------------------------------|
| 68         | 0       | 0   | Taste blade, mongrel!                                                                                                      |
| 68         | 0       | 1   | Please tell me that you didn't just do what I think you just did. Please tell me that I'm not going to have to hurt you... |
| 68         | 0       | 2   | As if we don't have enough problems, you go and create more!                                                               |
| 68         | 2       | 0   | %s throws a rotten apple at $n.                                                                                            |
| 68         | 3       | 0   | %s throws rotten banana on $n.                                                                                             |
| 68         | 4       | 0   | %s spits on $n.                                                                                                            |
| 68         | 5       | 0   | Monster!                                                                                                                   |
| 68         | 5       | 1   | Murderer!                                                                                                                  |
| 68         | 5       | 2   | GET A ROPE!                                                                                                                |
| 68         | 5       | 3   | How dare you set foot in our city!                                                                                         |
| 68         | 5       | 4   | You disgust me.                                                                                                            |
| 68         | 5       | 5   | Looks like we're going to have ourselves an execution.                                                                     |
| 68         | 5       | 6   | Traitorous dog.                                                                                                            |
| 68         | 5       | 7   | My family was wiped out by the Scourge! MONSTER!                                                                           |

### ID

每个文本组的条目。当 entry（生物）相同且 groupid 不变时，这是唯一标识符，必须递增（例如 0、1、2、3...）。将根据其所属的 groupid 从该列表中随机选择生物要说的话。

### Text

生物将要说出的文本。

### Type

| 值 | 旧值 | 本地化    | 图片示例                               |
|-------|-----------|--------------|-----------------------------------------------|
| 12    | 0         | 说 (Say)     | ![Say](assets/images/Say.png)                 |
| 14    | 1         | 喊 (Yell)    | ![Yell](assets/images/Yell.png)               |
| 16    | 2         | 表情 (Emote) | ![Emote](assets/images/Emote.png)             |
| 41    | 3         | 首领表情 (Boss Emote) | ![BossEmote](assets/images/BossEmote.png)     |
| 15    | 4         | 低语 (Whisper) | ![Whisper](assets/images/Whisper.png)         |
| 42    | 5         | 首领低语 (Boss Whisper) | ![BossWhisper](assets/images/BossWhisper.png) |

### Language

来自 [Languages.dbc](languages) 的值（+ 来自该 dbc 文件的 wiki 表）。当设置为 0 时，将使用当前默认语言。

### Probability

1-100 之间的值，表示此文本被执行的百分比概率。

该值必须 >= 0。如果该值不满足条件，SQL 将在 `creature_text_chk_1` 上失败。

### Emote

文本执行时生物所播放的表情。此字段中要使用的值可以从 [emote.dbc](emotes) 获取。

### Duration

显示文本的时间（毫秒）。
0 为默认值，由核心计算。

### Sound

生物在文本执行的同时播放的声音条目。声音可以在 SoundEntries.dbc 中找到。

### BroadcastTextId

在 [broadcast\_text](broadcast_text) 中找到的等效文本的 Id。

### TextRange

| 值 | 范围            |
|-------|----------------|
| 0     | 普通/默认 (Normal/Default) |
| 1     | 区域 (Area)     |
| 2     | 地区 (Zone)     |
| 3     | 地图 (Map)      |
| 4     | 世界 (World)    |

### comment

此字段允许你为文本条目添加标签。

## 相关表

- [creature\_text\_options](creature_text_options) — 为 (CreatureID, GroupID) 对分配可复用的选项规则集，以强制执行冷却、触发概率和仅玩家过滤。
- [creature\_text\_option\_sets](creature_text_option_sets) — 定义 `creature_text_options` 所引用的可复用规则集。

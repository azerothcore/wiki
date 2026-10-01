# 如何使用游戏事件

这是一个简单的示例，演示如何使用 `game_event` 和 `game_event_creature` 表来触发重复进行的游戏内事件。这是一个简单的示例，但应该足以让读者初步了解开始使用游戏内事件所需的内容。

**注意：** 请在对数据库进行任何更改（包括下面的更改）之前做好数据库备份。这只是为了防止你覆盖某些内容或做出破坏性更改。

## 快速入门

下面是一些可以对 \`acore_world\` 数据库执行的 SQL 更改，它们将导致三个"迪菲亚强盗"（Defias Cutpurse）NPC 每两（2）分钟在艾尔文森林出现和消失一次。这被设计为一个简单示例，并不代表对游戏世界的任何改进。

我们假设你使用 `mysql` 命令行工具来操作数据库，但你也可以使用任何允许运行自定义 SQL 查询的工具。

使用 WoW 客户端登录游戏世界，然后传送到我们打算工作的区域。使用以下 GM 命令（可能首先需要 `.gm on`）：`.go xyz -9168.486 86.90783 77.05649 0 0.006`。你会看到三个 NPC 在一个帐篷周围走动，就像这样：

![NPCs Visible](assets/images/tutorials/game_event_example/npcs.png)

接下来，连接到 AzerothCore MySQL 数据库，并确保你正在使用正确的表：\`use acore_world\`。

接下来，应用以下 SQL 在你的世界中创建一个 ID 为 91 的新事件（**注意**：这将删除任何现有的 ID 为 91 的事件条目）：

```sql
DELETE FROM game_event WHERE eventEntry = 91;
INSERT INTO game_event (
	eventEntry,
	start_time,
	end_time,
	occurence,
	length,
	holiday,
	holidayStage,
	description,
	world_event,
	announce
) VALUES (
	91,
	"2000-01-01 14:00:00",
	"2030-12-31 14:00:00",
	2,
	1,
	0,
	0,
	"TESTING EVENT",
	0,
	1
);
```

这将每 `occurence` 分钟触发一次，在本例中为 `2` 分钟。事件将持续 `length` 分钟，对我们来说是 `1` 分钟，这意味着在一（1）分钟后 NPC 将被重新添加回游戏世界。

现在通过应用以下 SQL 更新 `game_event_creature` 表：

```sql
DELETE FROM game_event_creature WHERE guid=79888;
DELETE FROM game_event_creature WHERE guid=79889;
DELETE FROM game_event_creature WHERE guid=79890;

INSERT INTO game_event_creature (eventEntry,guid) VALUES (-91,79888);
INSERT INTO game_event_creature (eventEntry,guid) VALUES (-91,79889);
INSERT INTO game_event_creature (eventEntry,guid) VALUES (-91,79890);
```

这定义了我们要游戏事件从世界中**移除（despawn）** 的具体 NPC GUID。它并不会生成生物，因为它们已经存在。还有其他 `game_event_*` 表用于管理其他事物，一些更复杂的东西，但我们选择这个表是因为它易于使用，可以用来演示事件如何工作。注意，我们将 `eventEntry` 字段设置为**负数**——即 `-91`——而不是（正的）`91`，因为我们希望这个事件**移除**这些 NPC。别担心，当事件在 `length` 分钟后结束时，NPC 会再次重新生成。如果你希望事件生成你定义的生物，那么你应该使用正的 GUID。

最后重启你的 AzerothCore 世界服务器。因为游戏世界已经重启，而你不得不重新登录游戏，你将错过事件的第一次运行，因此也会错过公告（在我们的示例 SQL 中设置为 `1`）。这意味着，根据你传送到上面坐标的速度，你可能会发现 NPC 还在，或者已经被移除了。

当你在上面坐标附近区域逗留时，你最终会看到 NPC 消失：

![No NPCs Visible](assets/images/tutorials/game_event_example/no-npcs.png)

## 撤销一切

如果你现在想从数据库中移除这个事件，可以使用以下 SQL：

```sql
DELETE FROM game_event WHERE eventEntry = 91;
DELETE FROM game_event_creature WHERE guid=79888;
DELETE FROM game_event_creature WHERE guid=79889;
DELETE FROM game_event_creature WHERE guid=79890;
```

你可能需要重新加载 AzerothCore 的"世界服务器"（World Server）才能使上述更改生效。

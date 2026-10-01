# SmartAI 简介

## 目录
- [第一部分：编写一个简单的脚本化巡逻](#part-i-scripting-a-simple-scripted-patrol)
- [第二部分：事件阶段（Event Phases）与链接（Links）](#part-ii-event-phases-and-links)
- [第三部分：条件（Conditions）、唯一 AI 与数据集（Data Set）](#part-iii-conditions-unique-ai-and-data-set)

---

## 第一部分：编写一个简单的脚本化巡逻 {#part-i-scripting-a-simple-scripted-patrol}

为此我们将编写一个简单的巡逻 RP 脚本，一个每隔一段时间通过计时器触发并涉及一条路径的脚本。

在编写仿暴雪（blizzlike）脚本时，这些数据大部分都可以在嗅探（sniffs）中收集到。使用诸如解析器、WDBE 或 WaypointCreator 之类的工具，我们可以提取路径点（waypoints），然后编写要执行的动作。

在解析的文件中，你可以搜索唯一的生物 GUID，查看执行了哪些动作。例如，NPCFlag、UnitFlag、StandState、EmoteState 和一次性表情（Oneshot Emotes）都可以在解析文件中找到。有些动作最终会被隐藏，但那时我们可以发挥创意甚至进一步调查。例如，在黑暗神殿中，有些生物通过施放一个服务器端法术来执行进食表情，但这并不常见。

我们将要实现的事件只包含站立状态（StandStates）和台词。

首先我们详细说明将要发生什么以及何时发生：

```sql
UPDATE `creature` SET `MovementType` = 2 WHERE `id1` = 23600 AND `guid` = 18604;

DELETE FROM `creature_addon` WHERE (`guid` IN (18604));
INSERT INTO `creature_addon` (`guid`, `path_id`, `mount`, `bytes1`, `bytes2`, `emote`, `visibilityDistanceType`, `auras`) VALUES
(18604, 186040, 0, 0, 1, 0, 0, NULL);

DELETE FROM `waypoint_data` WHERE `id` = 186040;
INSERT INTO `waypoint_data` (`id`, `point`, `position_x`, `position_y`, `position_z`, `orientation`, `delay`) VALUES
(186040, 1, -4044.12, -3393.59, 38.1363, NULL, 6000), -- 1s, Talk 0, 5s, Talk 1
(186040, 2, -4044.21, -3394.23, 38.3905, NULL, 0),
(186040, 3, -4042.96, -3396.48, 38.3905, NULL, 0),
(186040, 4, -4041.71, -3397.23, 38.3905, NULL, 0),
(186040, 5, -4040.8, -3396.88, 38.1447, NULL, 16000), -- 2s, Emote 16, 6s, Talk 2, 6s, Garion Talk 0
(186040, 6, -4043.67, -3395.27, 38.1634, NULL, 0),
(186040, 7, -4043.67, -3395.27, 38.1634, 3.87463, 240000);
```

逐行分析：

```sql
UPDATE `creature` SET `MovementType` = 2 WHERE `id1` = 23600 AND `guid` = 18604;
```

我们不是在放置一个新的生物，而是为现有的生物添加行为，所以我们只修改它的 MovementType，它告诉生物将使用其 creature_addon 条目中设置的路径。

```sql
DELETE FROM `creature_addon` WHERE (`guid` IN (18604));
INSERT INTO `creature_addon` (`guid`, `path_id`, `mount`, `bytes1`, `bytes2`, `emote`, `visibilityDistanceType`, `auras`) VALUES
(18604, 186040, 0, 0, 1, 0, 0, NULL);
```

这是它的 creature_addon 条目。按照惯例，巡逻路径的 id 等于 GUID*10。bytes2（也称为 SheateState）最常见的值是 1，表示生物的近战武器。它还包含与 RP 相关的物品，例如灯笼、瓶子等。

```sql
DELETE FROM `waypoint_data` WHERE `id` = 186040;
INSERT INTO `waypoint_data` (`id`, `point`, `position_x`, `position_y`, `position_z`, `orientation`, `delay`) VALUES
(186040, 1, -4044.12, -3393.59, 38.1363, NULL, 6000), -- 1s, Talk 0, 5s, Talk 1
(186040, 2, -4044.21, -3394.23, 38.3905, NULL, 0),
(186040, 3, -4042.96, -3396.48, 38.3905, NULL, 0),
(186040, 4, -4041.71, -3397.23, 38.3905, NULL, 0),
(186040, 5, -4040.8, -3396.88, 38.1447, NULL, 16000), -- 2s, Emote 16, 6s, Talk 2, 6s, Garion Talk 0
(186040, 6, -4043.67, -3395.27, 38.1634, NULL, 0),
(186040, 7, -4043.67, -3395.27, 38.1634, 3.87463, 180000);
```

这是分配给该生物的路径点巡逻。我把它缩短了，去掉了一些我们用不到的列。

x、y、z 值不言自明。方向（orientation）的变化需要一个从前一个点复制来的额外点，否则它为空。delay 决定了到达该路径点后的等待时间，因此当生物在第 7 点走完路径后，它会等待 3 分钟，然后再次开始巡逻。

我还添加了一些注释，详细说明在哪些路径点上执行哪些动作。这是我们将要写入 Actionlist 的简化版本。

我使用 Keira 来编辑 SmartAI，所以本教程将使用它。

![Keira Editor](assets/images/sai_tutorial/sai_tutor_1.png)

由于我们使用巡逻，我们将使用一个名为 WAYPOINT_REACHED 的事件。我们也可以使用 MOVEMENTINFORM，尤其当我们处理的是单个点而不是完整路径时非常有用。

然后 Keira 会生成我们要复制粘贴的输出。

```sql
UPDATE `creature_template` SET `AIName` = 'SmartAI' WHERE `entry` = 23600;
DELETE FROM `smart_scripts` WHERE (`source_type` = 0 AND `entryorguid` = 23600);
INSERT INTO `smart_scripts` (`entryorguid`, `source_type`, `id`, `link`, `event_type`, `event_phase_mask`, `event_chance`, `event_flags`, `event_param1`, `event_param2`, `event_param3`, `event_param4`, `event_param5`, `event_param6`, `action_type`, `action_param1`, `action_param2`, `action_param3`, `action_param4`, `action_param5`, `action_param6`, `target_type`, `target_param1`, `target_param2`, `target_param3`, `target_param4`, `target_x`, `target_y`, `target_z`, `target_o`, `comment`) VALUES
(23600, 0, 0, 0, 108, 0, 100, 0, 1, 0, 0, 0, 0, 0, 80, 2360000, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - On Point 1 of Path Any Reached - Run Script'),
(23600, 0, 1, 0, 108, 0, 100, 0, 5, 0, 0, 0, 0, 0, 80, 2360001, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - On Point 5 of Path Any Reached - Run Script');
```

这看起来比我在注释中描述的要简单。这是因为我们实际上并不在这里执行动作。我们将使用 SmartAI 的另一个机制，称为 Actionlists（动作列表），或 Script9，它是一系列在给定计时器上执行的动作。这样我们可以更容易地制作延迟动作。按照惯例，Actionlists 的脚本 ID 编号为 CreatureEntry*100，每个唯一的列表加 1。由于我们将使用 2 组不同的动作，我们使用 ID 2360000 和 2360001。

在事件参数中，我们将 pathId 参数保留为 0，因为我们预计除了我们添加的路径外没有其他巡逻，所以如果我们不将其保留为 0，那也只是一个始终返回 true 的无意义检查，因此我们忽略它。

对于目标参数，我们将其保留为 1，因为调用 Actionlists 的动作除了自身之外不需要任何目标。

现在我们将打开 Actionlist 编辑器并制作两个脚本。

```sql
DELETE FROM `smart_scripts` WHERE (`source_type` = 9 AND `entryorguid` IN (2360000, 2360001));
INSERT INTO `smart_scripts` (`entryorguid`, `source_type`, `id`, `link`, `event_type`, `event_phase_mask`, `event_chance`, `event_flags`, `event_param1`, `event_param2`, `event_param3`, `event_param4`, `event_param5`, `event_param6`, `action_type`, `action_param1`, `action_param2`, `action_param3`, `action_param4`, `action_param5`, `action_param6`, `target_type`, `target_param1`, `target_param2`, `target_param3`, `target_param4`, `target_x`, `target_y`, `target_z`, `target_o`, `comment`) VALUES
(2360000, 9, 0, 0, 0, 0, 100, 0, 1000, 1000, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - Actionlist - Say Line 0'),
(2360000, 9, 1, 0, 0, 0, 100, 0, 5000, 5000, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - Actionlist - Say Line 1'),

(2360001, 9, 0, 0, 0, 0, 100, 0, 2000, 2000, 0, 0, 0, 0, 5, 16, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - Actionlist - Play Emote 16'),
(2360001, 9, 1, 0, 0, 0, 100, 0, 6000, 6000, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - Actionlist - Say Line 2'),
(2360001, 9, 2, 0, 0, 0, 100, 0, 6000, 6000, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 19, 23601, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - Actionlist - Say Line 0 (Apprentice Garion)');
```

这里是脚本的核心。第一个脚本很简单，只执行说话动作。

第二个脚本播放一个表情，让我们的生物 Morlann 说话，然后让一个**不同的**生物说话。当我们为 TALK 动作使用一个目标，并将第三个参数保留为 0 时，我们可以远程让目标生物说话，而不必制作更复杂或更繁琐的脚本。第三个参数在设置为 1 且存在有效目标时，例如会以名称或职业来称呼目标，例如直接叫玩家的名字。

所以会发生的是：
1. 生物生成并第一次开始巡逻
2. 当到达一个点时，它会触发该事件，检查到达的点是 1 还是 5，如果是，则执行动作
3. 执行动作并给生物分配一个 Actionlist，它将播放一系列延迟动作
4. 一旦巡逻完成，它会等待 3 分钟然后重新开始

## 第二部分：事件阶段（Event Phases）与链接（Links） {#part-ii-event-phases-and-links}

大多数敌对生物都比较简单，遵循一两个计时器并施放几个法术，几分钟内就能轻松完成。SmartAI 的强大之处并不在于遵循简单的法术计时器。为了举例说明，我们来看看一些外域生物的脚本，我觉得它们相当有趣。在外域有几种虚空生物，其中的施法者具有一种彼此共享的特殊脚本结构。

起初，它们只施放暗影箭，并且没有特殊的抗性。然而一旦玩家用例如冰霜箭命中它们，它们就会对自己施放一个冰霜伤害减免法术，说一句话，然后开始对玩家施放冰霜箭。那么我们如何在 SmartAI 中实现这一点呢？

一个现成的例子是虚空尖啸者（Voidshrieker）。

![Voidshrieker Script](assets/images/sai_tutorial/sai_tutor_2.png)

难以阅读，对吧？但我会尽量让它更容易解析。但首先我们需要理解事件阶段（Event Phases）是如何工作的。

简单来说，阶段允许我们以某种方式规定可以播放哪些类型的事件，因为每个事件都被分配了一个阶段。阶段 0 是总括阶段。无论生物当前处于哪个阶段，放置在阶段 0 中的任何内容都会被播放。

设置生物的事件阶段是一个动作，并且当生物脱离战斗（evade）、死亡或重生时会重置，所以最好也把事件阶段重置为我们想要的值。

看脚本的 id 2。在进入战斗（Aggro）时，事件阶段将被设置为 1，那么哪些事件属于事件阶段 1 集合呢？简而言之，第 3 行到第 18 行的所有行，占脚本的很大一部分。

![Event Phase Logic](assets/images/sai_tutorial/sai_tutor_3.png)

这些。在虚空尖啸者被上述某个学派（schools）的法术命中后，它会播放一系列动作，通过 EVENT_LINK 链接在一起，然后改变自己的阶段。注意事件阶段 1 只在进入战斗（Aggro）时设置，所以这种行为每次战斗只能播放**一次**。如果我对其施放火系法术，该事件会播放并改变阶段，所以如果我再施放冰系法术，它就不会施放 `冰霜伤害减免`，因为它现在不在阶段 1，而是处于阶段 3。

此外，虽然此示例中没有显示，事件阶段是一个掩码（mask），而不是枚举值。这意味着我们可以将事件阶段层层叠加。如果我们愿意，我们可以让虚空尖啸者叠加抗性，并通过累积事件阶段而不是替换它们来施放完整的元素法术梯度。

附注：事件标志 1（不重复，No Repeat）会在战斗结束后重置！若要永不重置并确保生物永远不再播放该事件，请使用标志 256（不重置，Don't Reset）！

有了这些事件，我们将用它们让生物根据它当前所处的阶段施放不同的法术。

![Spell Cast Events](assets/images/sai_tutorial/sai_tutor_4.png)

上面所有这些事件都与计时器绑定，而不是像 On Spellhit 那样的触发器。看到 `施放暗影箭` 了吗？它绑定到两个事件阶段，就像我提到的维恩图示例一样。如果玩家没有施放法术，或者例如是个战士，虚空尖啸者默认会施放暗影箭，同样如果玩家施放了暗影系法术，它也会施放。那么心灵尖啸（Psychic Scream）呢？它绑定到事件阶段 0，这意味着无论生物当前处于哪个阶段，它都会运行计时器并执行该事件。

回到流程图，我还没有正确解释这些动作是如何相互链接的。在第 1 部分中我介绍了 Actionlists 的概念。这很类似。

链接（Links）允许我们瞬间按顺序播放多个动作，所以它不允许我们制作延迟。要使用它，你需要在 `link` 字段中设置将被链接的事件的 id。

[Linked Events](assets/images/sai_tutorial/sai_tutor_5.png)

如你所见，事件 3 链接到事件 4，所以当事件 3 被执行时，事件 4 也会自动执行。被链接的事件必须是事件类型 61，即 EVENT_LINK。

多个事件可以链接到同一个事件。例如，如果一个生物在施放几个不同的法术后说同一句话，那么所有这些法术都可以链接到同一个说话动作。

如果我们制作太多链接，它们会使脚本更难以维护，因为更改一行可能需要更改所有行。对于一系列中的多个链接，我通常更喜欢使用定时 Actionlists，使用 TimerType 2 以确保它在战斗中也能播放。这样可以更容易地将迷你脚本封装在主生物脚本中，而不会产生混乱的链接（spaghetti links）。

## 第三部分：条件（Conditions）、唯一 AI 与数据集（Data Set） {#part-iii-conditions-unique-ai-and-data-set}

在破碎大厅（Shattered Halls）中，有一种名为碎手军团士兵（Shattered Hand Legionnaire）的生物。

嗯，实际上有 8 个。而且它们……全都……有……不同的……AI。

它们使用的战斗机制和法术是共同的。它们都会激怒，都会痛击施法者，并且都会施放纪律光环（Aura of Discipline）。

![Shattered Hand Legionnaire](assets/images/sai_tutorial/sai_tutor_6.png)

但让我们看看，例如，GUID 151010 的 AI，为此我们检查其 guid 特定的条目。转到 SmartAI 面板并按如下方式按实体搜索。

![SmartAI Search Panel](assets/images/sai_tutorial/sai_tutor_7.png)

你会看到几行，所有行的 id 都编号 >1000，并且具有特定于此 GUID 的独特行为

![GUID Specific Scripts](assets/images/sai_tutorial/sai_tutor_8.png)

第 1001 到 1004 行是 RP 脚本。重点关注下面的行。例如，在第一张图片的通用脚本中，我们看到一旦生物收到数据集（DATA SET）——一个允许我们在生物之间通信的动作——它就会激怒。这个副本中的其他每个生物在死亡时都有一个脚本来对最近的军团士兵设置数据（SET DATA），这样它们都会激怒。但如果你包含这个 guid 特定的脚本，这个特定的军团士兵不仅会激怒，还会说一句特殊台词并召唤一个处于独特位置的生物。然后我们使用事件阶段来一次只允许一个生物生成。

现在，重要的是通常这些 guid 特定的脚本会覆盖生物的正常脚本，因此我们必须复制过来，造成大量冗余。但大约在我们重写破碎大厅的时候，我的一个朋友为生物添加了一个额外的标志，使它们既加载与条目（entry）相关的通用 SmartAI，也加载与其 guid 相关的 SmartAI。

![Creature Template Flags](assets/images/sai_tutorial/sai_tutor_9.png)

这极其重要，因为大量生物具有独特行为，所以为了避免大量无用的行，我们使用这个标志。请注意，在这种情况下制作 guid 特定的 SAI 时我们使用 1000+ 的 id，因为行 id 不应重叠！

现在，让我们看看这些召唤物。它们是如何工作的？嗯，碰巧每个召唤物**也**具有独特行为！因为好几个军团士兵会在不同位置召唤它们。而且每个都可以做不同的事情。

![Summon Scripts](assets/images/sai_tutorial/sai_tutor_10.png)

问题在于召唤物没有我们可以为其创建 guid 特定脚本的 guid。

上面的脚本是给召唤物的，注意当它们被召唤（On Summoned）时，它们会执行几个不同的脚本。它们不会重叠吗？按理说应该会。但在这种情况下不会，因为我们使用了条件（conditions）。

条件是非常强大的工具，我们可以直接将它们绑定到 SmartAI，用于每一行和任何行。

![Conditions Panel](assets/images/sai_tutorial/sai_tutor_11.png)

看到 ConditionValue 是 151010 的地方了吗？这意味着在 SmartAI id 10（11 - 1）中，只有当触发者（Invoker，此处即召唤者）是 GUID 为 151010 的军团士兵时，该事件才会播放。

你现在应该开始看到 SmartAI 可以多么强大了。每一行都可以被设置条件。另一个有趣的案例研究是一个任务对象，它检测玩家推进了多远，以便执行台词和生成生物。在其中，每次玩家交互时脚本都会被调用，但只有满足条件时才会执行。

触发者（Invokers）并不是所有事件都有。例如，当使用事件 OOC_LOS（检查玩家进入我们生物视线）时，触发者就是进入视线的玩家。当你召唤生物（Summon Creature）时，触发者就是召唤者。触发者也可以用作 target_type。例如，当执行事件 On Quest Accepted 时，使用动作 64（STORE_TARGET_LIST）保存触发者，甚至使用 target_type 16 保存触发者的整个队伍，可能会很好。

你可能会问，如果我们能使用条件，为什么还需要 guid 特定的 SAI？因为我们需要在每次事件触发时进行检查。对于一两个具有 guid 特定 AI 的生物来说，这可能没问题，但在暗影迷宫（Shadow Labyrinth）中，你有几十个。每隔几秒你就得进行几十次甚至一百次检查。

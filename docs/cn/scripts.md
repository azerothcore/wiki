# Script 表

[<-返回至:World](database-world)

# 表：\*\*\*\_scripts

此表格式用于 3 个不同的表，以控制由不同动作触发的可能脚本：

**spell\_scripts：** 保存可由具有 SPELL\_EFFECT\_SCRIPT\_EFFECT (77) 或 SPELL\_EFFECT\_DUMMY(3) 效果的法术触发的脚本。

**event\_scripts：** 保存每当事件被激活时触发的脚本，无论是由对象触发，还是作为法术效果 SPELL\_EFFECT\_SEND\_EVENT (61) 触发。

**waypoint\_scripts：** 保存在 [waypoint\_data](waypoint_data) 表中使用的脚本。有关路径点的一般信息，另请参阅 [路径点信息](waypoints-information)。

注意：此表中的一条记录可能对应多行，因为一个脚本可能执行多个动作。此外，脚本执行的每个动作都可以附带单独的延迟。在这种情况下，核心（core）会在正确的延迟之后激活相应的动作。

**表结构**

| Field                     | Type  | Attributes | Key | Null | Default | Extra                                                                                                                          | Comment |
| ------------------------- | ----- | ---------- | --- | ---- | ------- | ------------------------------------------------------------------------------------------------------------------------------ | ------- |
| [id](#id)                 | INT   | UNSIGNED   |     | NO   | 0       |                                                                                                                                |         |
| [effIndex](#effindex)     | INT   | UNSIGNED   |     | NO   | 0       | 仅用于 spell_scripts                                                                                                           |         |
| [delay](#delay)           | INT   | UNSIGNED   |     | NO   | 0       |                                                                                                                                |         |
| [command](#command)       | INT   | UNSIGNED   |     | NO   | 0       |                                                                                                                                |         |
| [datalong](#otherfields)  | INT   | UNSIGNED   |     | NO   | 0       |                                                                                                                                |         |
| [datalong2](#otherfields) | INT   | UNSIGNED   |     | NO   | 0       |                                                                                                                                |         |
| [dataint](#otherfields)   | INT   |            |     | NO   | 0       |                                                                                                                                |         |
| [x](#otherfields)         | FLOAT |            |     | NO   | 0       |                                                                                                                                |         |
| [y](#otherfields)         | FLOAT |            |     | NO   | 0       |                                                                                                                                |         |
| [z](#otherfields)         | FLOAT |            |     | NO   | 0       |                                                                                                                                |         |
| [o](#otherfields)         | FLOAT |            |     | NO   | 0       |                                                                                                                                |         |
| [guid](#guid)             | INT   |            | PRI | NO   | 0       | 仅用于 waypoint_scripts；作为主键，并通过 [GM 命令](gm-commands) 'wp event add' 自动设置                                            |         |

## **字段说明**

### id

对于 **spell\_scripts**，它是法术 ID。参见 [Spell.dbc](spell)

对于 **event\_scripts**，它是事件 ID。目前不存在完整的事件列表。无论如何，事件 ID 直接取自 gameobject WDB 数据或法术效果数据。如果游戏对象（gameobject）和法术激活同一事件，则它们的 ID 将匹配。

对于 **waypoint\_scripts**，它是 [action](waypoint_data#action) ID。

### effIndex

此脚本所要应用的法术效果索引。

### delay

此脚本步骤激活前的延迟秒数。0 = 立即。

### command

脚本在 [delay](#delay) 秒过后执行的动作类型。此字段的值会影响还需要设置哪些其他字段。可以使用以下命令：

| Command | Name                                                               | Description                                                              |
| ------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| 0       | [TALK](#scriptcommandtalk--0)                                      | 生物的说话/耳语/大喊/文字表情。                                           |
| 1       | [EMOTE](#scriptcommandemote--1)                                    | 在生物上播放表情。                                                       |
| 2       | [FIELD\_SET](#scriptcommandfieldset--2)                            | 更改玩家的某个索引处的字段值。                                           |
| 3       | [MOVE\_TO](#scriptcommandmoveto--3)                                | 将生物移动到目的地。                                                     |
| 4       | [FLAG\_SET](#scriptcommandflagset--4)                              | 开启玩家某个索引处的标志字段上的位。                                     |
| 5       | [FLAG\_REMOVE](#scriptcommandflagremove--5)                        | 关闭玩家某个索引处的标志字段上的位。                                     |
| 6       | [TELEPORT\_TO](#scriptcommandteleportto--6)                        | 将玩家传送到某个位置。                                                   |
| 7       | [QUEST\_EXPLORED](#scriptcommandquestexplored--7)                  | 满足某个任务的探索要求。                                                 |
| 8       | [KILL\_CREDIT](#scriptcommandkillcredit--8)                        | 给予玩家击杀计数。                                                       |
| 9       | [RESPAWN\_GAMEOBJECT](#scriptcommandrespawngameobject--9)          | 生成一个已消失的游戏对象。                                               |
| 10      | [TEMP\_SUMMON\_CREATURE](#scriptcommandtempsummoncreature--10)     | 临时召唤一个生物。                                                       |
| 11      | [OPEN\_DOOR](#scriptcommandopendoor--11)                           | 打开一个门游戏对象（类型 0）。                                           |
| 12      | [CLOSE\_DOOR](#scriptcommandclosedoor--12)                         | 关闭一个门游戏对象（类型 0）。                                           |
| 13      | [ACTIVATE\_OBJECT](#scriptcommandactivateobject--13)               | 激活一个对象。                                                           |
| 14      | [REMOVE\_AURA](#scriptcommandremoveaura--14)                       | 移除由某个法术引起的光环。                                               |
| 15      | [CAST\_SPELL](#scriptcommandcastspell--15)                         | 施放一个法术。                                                           |
| 16      | [PLAY\_SOUND](#scriptcommandplaysound--16)                         | 播放一个声音。                                                           |
| 17      | [CREATE\_ITEM](#scriptcommandcreateitem--17)                       | 为玩家创建指定数量的物品。                                               |
| 18      | [DESPAWN\_SELF](#scriptcommanddespawnself--18)                     | 强制生物消失。                                                           |
| 20      | [LOAD\_PATH](#scriptcommandloadpath--20)                           | 将路径加载到单位，然后单位开始路径点移动。                               |
| 21      | [CALLSCRIPT\_TO\_UNIT](#scriptcommandcallscripttounit--21)         | 以给定的单位作为源，从某个 \*\_scripts 表中调用脚本。                    |
| 22      | [KILL](#scriptcommandkill--22)                                     | 将生物状态更改为死亡，并可选地移除其尸体。                               |
| 30      | [ORIENTATION](#scriptcommandorientation--30)                       | 更改单位的方向（用于路径点脚本）                                         |
| 31      | [EQUIP](#scriptcommandequip--31)                                   | 设置生物的装备。                                                         |
| 32      | [MODEL](#scriptcommandmodel--32)                                   | 设置生物的模型。                                                         |
| 33      | [CLOSE\_GOSSIP](#scriptcommandclosegossip--33)                     | 关闭交谈窗口。此命令仅用于交谈脚本。                                     |
| 34      | [PLAYMOVIE](#scriptcommandplaymovie--34)                           | 播放过场动画。                                                           |
| 35      | [MOVEMENT](#scriptcommandmovement--35)                             | 更改移动类型。                                                           |

### OtherFields

根据所使用的命令，以下字段的含义和用途会有所不同。

#### \*SCRIPT\_COMMAND\_TALK = 0

- source（源）：Creature（生物）。
- target（目标）：any/Player（用于耳语）。
- datalong：0=说话，1=大喊，2=文字表情，3=首领表情，4=耳语，5=首领耳语
- dataint：引用 [broadcast\_text.id](broadcast_text)

#### \*SCRIPT\_COMMAND\_EMOTE = 1

- source 或 target：Creature（生物）。
- datalong：要播放的表情 ID。
- datalong2：如果此值 &gt; 0，NPC 将播放表情状态而不是一次性播放。

#### \*SCRIPT\_COMMAND\_FIELD\_SET = 2

- source 或 target：Creature（生物）。
- datalong：字段的索引。
- datalong2：要放置在该索引处的值。

#### \*SCRIPT\_COMMAND\_MOVE\_TO = 3

- source：Creature（生物）。
- datalong2：移动的时长（以时间为单位）。
- x：要移动到的 X 位置。
- y：要移动到的 Y 位置。
- z：要移动到的 Z 位置。

#### \*SCRIPT\_COMMAND\_FLAG\_SET = 4

- source 或 target：Creature（生物）。
- datalong：要设置的字段索引。
- datalong2：要设置的标志位。

#### \*SCRIPT\_COMMAND\_FLAG\_REMOVE = 5

- source 或 target：Creature（生物）。
- datalong：要取消设置的字段索引。
- datalong2：要取消设置的标志位。

#### \*SCRIPT\_COMMAND\_TELEPORT\_TO = 6

- source 或 target：Player（datalong2 0）或 Creature（datalong2 1）。
- datalong：目标地图 ID。参见 [Map.dbc](map)
- x：传送目标的 x 坐标。
- y：传送目标的 y 坐标。
- z：传送目标的 z 坐标。
- o：传送目标的朝向。

#### \*SCRIPT\_COMMAND\_QUEST\_EXPLORED = 7

- source 或 target：Player（玩家）。
- target 或 source：WorldObject（世界对象）。
- datalong：应满足外部状态的任务条目。参见 [quest\_template.id](quest_template#id)。
- datalong2：玩家可以与 NPC/对象保持的距离，在此距离内脚本仍然生效（最小值为 5）。

#### \*SCRIPT\_COMMAND\_KILL\_CREDIT = 8

- target 或 source：Player（玩家）。
- datalong：击杀计数的生物条目。参见 [creature\_template.entry](creature_template#entry)。
- datalong2：如果值 &gt; 0，则给予玩家所属整个队伍的击杀计数，否则给予个人击杀计数。

#### \*SCRIPT\_COMMAND\_RESPAWN\_GAMEOBJECT = 9

- source：WorldObject（召唤者）。
- datalong：要重新生成的游戏对象的 Guid。参见 [gameobject.guid](gameobject#guid)。
- datalong2：消失时间（秒）。如果该值 &lt; 5 秒：则使用 5。

#### \*SCRIPT\_COMMAND\_TEMP\_SUMMON\_CREATURE = 10

- source：WorldObject（召唤者）。
- datalong：被召唤生物的条目。参见 [creature\_template.entry](creature_template#entry)。
- datalong2：消失时间（毫秒）。
- x：召唤目标的 x 坐标。
- y：召唤目标的 y 坐标。
- z：召唤目标的 z 坐标。
- o：召唤目标的朝向。

#### \*SCRIPT\_COMMAND\_OPEN\_DOOR = 11

- source：WorldObject（世界对象）。
- datalong：被激活的门 Guid。参见 [gameobject.guid](gameobject#guid)。
- datalong2：再次关闭门之前的延迟。如果该值 &lt; 15 秒：则使用 15。

#### \*SCRIPT\_COMMAND\_CLOSE\_DOOR = 12

- source：WorldObject（世界对象）。
- datalong：被激活的门 Guid。参见 [gameobject.guid](gameobject#guid)。
- datalong2：再次打开门之前的延迟。如果该值 &lt; 15 秒：则使用 15。

#### \*SCRIPT\_COMMAND\_ACTIVATE\_OBJECT = 13

- source：Unit（单位）。
- target：GameObject（游戏对象）。

#### \*SCRIPT\_COMMAND\_REMOVE\_AURA = 14

- source（datalong2 != 0）或 target（datalong2 == 0）：Unit（单位）。
- datalong：法术 ID。参见 [Spell.dbc](spell)
- datalong2：如果值 &gt; 0，则从 source 移除；否则从 target 移除。

#### \*SCRIPT\_COMMAND\_CAST\_SPELL = 15

- source：Unit（单位）。
- target：Unit（单位）。
- datalong：法术 ID。参见 [Spell.dbc](spell)
- datalong2：
  - 0 - Source-&gt;Target
  - 1 - Source-&gt;Source（自我施放，用于 dummy 法术）
  - 2 - Target-&gt;Target
  - 3 - Target-&gt;Source
  - 4 - Source-&gt;最近的 dataint 条目。
- dataint：如果 datalong2 值为 4，则为要作为目标的生物条目；在其他情况下，则为 CastSpell 方法的触发属性。
- x：如果 datalong2 值为 4，则为生物条目（dataint）的搜索范围。

#### \*SCRIPT\_COMMAND\_PLAY\_SOUND = 16

- source：WorldObject（世界对象）。
- target：无（datalong2 & 1 == 0）或 Player（datalong2 & 1 != 0）。
- datalong：声音 ID。
- datalong2：
  - 0 - 向所有人直接播放声音。
  - 1 - 向目标直接播放声音（必须是 Player）。
  - 2 - 向所有人播放带距离衰减的声音。
  - 3 - 向目标播放带距离衰减的声音（必须是 Player）。
  - 4 - 向半径范围内的任何人播放声音。
- dataint：如果 datalong2 值为 4，则为半径

#### \*SCRIPT\_COMMAND\_CREATE\_ITEM = 17

- target 或 source：Player（玩家）。
- datalong：要创建的物品条目。参见 [item\_template.entry](item_template#entry)。
- datalong2：要创建的物品数量。

#### \*SCRIPT\_COMMAND\_DESPAWN\_SELF = 18

- target：Creature（生物）。
- datalong：消失延迟。

#### \*SCRIPT\_COMMAND\_LOAD\_PATH = 20

- source：Unit（单位）。
- datalong：路径 ID。参见 [waypoint\_data.id](waypoint_data#id)。
- datalong2：如果值 &gt; 0，表示路径点移动可重复。

#### \*SCRIPT\_COMMAND\_CALLSCRIPT\_TO\_UNIT = 21

- source：如果存在，用作搜索中心。
- datalong：被搜索生物的条目；如果 source 存在，则为生物的 guid。
        \*\*datalong2：来自 \*\_scripts 表的脚本 ID。
- dataint：
  - 3 - 使用 spell\_scripts 表；
  - 5 - 使用 event\_scripts 表；
  - 6 - 使用 waypoint\_scripts 表。

#### \*SCRIPT\_COMMAND\_KILL = 22

- source：Creature（生物）。
- dataint：如果值 == 1，移除尸体。

#### \*SCRIPT\_COMMAND\_ORIENTATION = 30

- source：Unit（单位）。
- target：Unit（datalong != 0）。
- datalong：如果值 != 0，则转向面向目标；否则转向字段 \`o\` 中的值。
- o：将朝向设置为字段 \`o\` 中的值。

#### \*SCRIPT\_COMMAND\_EQUIP = 31

- source：Creature（生物）。
- datalong：来自装备条目的 ID（1、2、3 ...）。参见 [creature\_equip\_template.id](creature_equip_template#id)

#### \*SCRIPT\_COMMAND\_MODEL = 32

- source：Creature（生物）。
- datalong：模型 ID。

#### \*SCRIPT\_COMMAND\_CLOSE\_GOSSIP = 33

- source：Player（玩家）。

#### \*SCRIPT\_COMMAND\_PLAYMOVIE = 34

- source：Player（玩家）。
- datalong：电影 ID。

#### \*SCRIPT\_COMMAND\_MOVEMENT = 35

- source：Creature（生物）。
- datalong：MovementType（移动类型）。
- datalong2：MovementDistance（移动距离，例如 MovementType 1 的 wander_distance）。
- dataint：pathid（用于 MovementType 2，参见 [waypoint\_data.id](waypoint_data#id)）。

### guid

仅存在于 'waypoint_scripts' 中，并在其中作为主键；它通过 [GM 命令](gm-commands) 'wp event add' 自动设置。

# achievement\_criteria\_data

[<-返回至:World](database-world)

**`achievement\_criteria\_data` 表**

此表包含玩家为获得某个成就而需要获得/完成的数据。

**表结构**

| Field            | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [criteria_id][1] | MEDIUMINT |            | PRI | NO   |         |       |         |
| [type][2]        | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |         |
| [value1][3]      | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [value2][4]      | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [ScriptName][5]  | char(64)  |            |     | NO   |         |       |         |

[1]: #criteriaid
[2]: #type
[3]: #value1
[4]: #value2
[5]: #scriptname

**字段说明**

### criteria\_id

这是 [Achievement\_Criteria.dbc](achievement_criteria) 中的 ID。

### type

根据此值，将决定 value1 和 value2 的用法。

| 类型 | 名称                       |
| ---- | -------------------------- |
| 0    | TYPE_NONE                  |
| 1    | TYPE_T_CREATURE            |
| 2    | TYPE_T_PLAYER_CLASS_RACE   |
| 3    | TYPE_T_PLAYER_LESS_HEALTH  |
| 4    | TYPE_T_PLAYER_DEAD         |
| 5    | TYPE_S_AURA                |
| 6    | TYPE_S_AREA                |
| 7    | TYPE_T_AURA                |
| 8    | TYPE_VALUE                 |
| 9    | TYPE_T_LEVEL               |
| 10   | TYPE_T_GENDER              |
| 11   | TYPE_SCRIPT                |
| 12   | TYPE_MAP_DIFFICULTY        |
| 13   | TYPE_MAP_PLAYER_COUNT      |
| 14   | TYPE_T_TEAM                |
| 15   | TYPE_S_DRUNK               |
| 16   | TYPE_HOLIDAY               |
| 17   | TYPE_BG_LOSS_TEAM_SCORE    |
| 18   | TYPE_INSTANCE_SCRIPT       |
| 19   | TYPE_S_EQUIPED_ITEM        |
| 20   | TYPE_MAP_ID                |
| 21   | TYPE_S_PLAYER_CLASS_RACE   |
| 22   | TYPE_NTH_BIRTHDAY          |
| 23   | TYPE_S_KNOWN_TITLE         |

### value1

**TYPE\_T\_CREATURE**

-   此处的目标必须是 creature\_template 中的有效条目

**TYPE\_T\_PLAYER\_CLASS\_RACE**

-   此处的目标是一个有效的职业（粘贴职业列表）。还必须设置 value2

**TYPE\_T\_PLAYER\_LESS\_HEALTH**

-   目标必须达到的生命值百分比。

**TYPE\_T\_PLAYER\_DEAD**

-   目标玩家的阵营（必须与尝试完成成就的玩家匹配）。

**TYPE\_S\_AURA**

-   必须施加在玩家身上的光环的法术 ID。还必须设置 value2。

**TYPE\_S\_AREA**

-   AreaTable.dbc 中的区域 ID

**TYPE\_T\_AURA**

-   必须施加在目标身上的光环的法术 ID。还必须设置 value2。

**TYPE\_VALUE**

-   用于比较达成成就所需的值。此值与另一种类型一起使用。（比较类型见 value2）

**TYPE\_T\_LEVEL**

-   目标可以达到的最低等级。

**TYPE\_T\_GENDER**

-   性别：0=男，1=女

**TYPE\_SCRIPT**

-   如果未定义所有要求，则用于禁用某个成就。通常在没有完全了解所有要求时使用。

**TYPE\_MAP\_DIFFICULTY**

-   地图难度：（对于地下城）
    - 普通 = 0
    - 英雄 = 1
-   地图难度：（对于团队副本）
    - 10 人普通 = 0
    - 25 人普通 = 1
    - 10 人英雄 = 2
    - 25 人英雄 = 3

**TYPE\_MAP\_PLAYER\_COUNT**

-   必须在该区域中的其他玩家数量。（不确定是最小值还是最大值）。

**TYPE\_T\_TEAM**

-   目标必须在此阵营：联盟 = 469，部落 = 67

**TYPE\_S\_DRUNK**

-   玩家必须醉到什么程度：
    - DRUNKEN\_SOBER = 0
    - DRUNKEN\_TIPSY = 1
    - DRUNKEN\_DRUNK = 2
    - DRUNKEN\_SMASHED = 3

**TYPE\_HOLIDAY**

-   Holiday.dbc 和 game\_event 中的节日 ID。必须是正在进行的节日。

**TYPE\_BG\_LOSS\_TEAM\_SCORE**

-   玩家的队伍赢得战场，且对方队伍的比分在某个范围内。// 最低分

**TYPE\_INSTANCE\_SCRIPT**

-   让副本脚本调用以检查当前条件是否满足成就要求。

**TYPE\_S\_EQUIPED\_ITEM**

-   物品等级

**TYPE\_MAP\_ID**

-   玩家必须在 mapId 上

**TYPE\_S\_PLAYER\_CLASS\_RACE**

-   此处的来源是一个有效的职业（粘贴职业列表）。还必须设置 value2
 

**TYPE\_NTH\_BIRTHDAY**

-   生日序号

**TYPE\_S\_KNOWN\_TITLE**

-   此处的值是一个有效的 titleId。参见 CharTitles.dbc

### value2

**TYPE\_T\_PLAYER\_CLASS\_RACE**
**TYPE\_S\_PLAYER\_CLASS\_RACE**

-   此处的值是一个有效的种族 ID。参见 ChrRaces.dbc

**TYPE\_S\_AURA**

-   光环的效果索引

**TYPE\_T\_AURA**

-   光环的效果索引

**TYPE\_BG\_LOSS\_TEAM\_SCORE**

-   最高分

**TYPE\_S\_EQUIPED\_ITEM**

-   物品品质

**TYPE\_VALUE**

| 比较类型                 |
| ------------------------ |
| COMP\_TYPE\_EQ = 0       |
| COMP\_TYPE\_HIGH = 1     |
| COMP\_TYPE\_LOW = 2      |
| COMP\_TYPE\_HIGH\_EQ = 3 |
| COMP\_TYPE\_LOW\_EQ = 4  |

### ScriptName

在核心中编写脚本时使用的 ScriptName。
它也可能是 'SmartTrigger'。在这种情况下将使用 [SmartAI](smart_scripts)。

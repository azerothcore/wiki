# faction

[`返回:DBC`](dbc-index)

**\`Faction.dbc\` 表**

该 DBC 文件包含所有基础阵营的信息。这些阵营是唯一的，代表玩家可以获得声望的阵营。

**重要提示：** 这些值用于**所有**表，**除了** [creature_template](creature_template) 和 [gameobject_template_addon](gameobject_template_addon) 表。

[如何将 DBC 数据导入数据库](how-to-import-dbc-data-in-db)

## 结构

| 列   | 字段                 | 类型                                         | 备注                                                                                                                                                                                                                                                                                                             |
| ---- | -------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | ID                   | Integer                                      |                                                                                                                                                                                                                                                                                                                  |
| 2    | reputationIndex      | Integer                                      | 每个可获得声望的阵营都有一个唯一的编号。所有无法获得声望的阵营均为 -1。                                                                                                                                                                                                                                          |
| 3    | reputationRaceMask   | BitMask                                      | &lt;.. 指向另一个 Allied / AtWar ID                                                                                                                                                                                                                                                                              |
| 4    | reputationRaceMask   | BitMask                                      | .. 例如 Honor Hold 为 1101,690，Thrallmar 为 690,1101。 ..&gt;                                                                                                                                                                                                                                                   |
| 5    | reputationRaceMask   | BitMask                                      | 只有城市阵营有值。可能与 Modifiers 和 17 有关（1 = Stormwind；2 = Orgrimmar；4 = Wildhammer Clan & Iron Forge；8 = Darnassus；16 = Undercity；64 = Gnomeregan Exiles；512 = Shattrath City Factions & Silvermoon City；528 = Thunder Bluff & Darkspear Trolls；1024 = Exodar）                                    |
| 6    | reputationRaceMask   | BitMask                                      | 只有部落城市有值。可能与 Modifiers 和 18 有关（16 = Silvermoon City；32 = Thunder Bluff；128 = Darkspear Trolls；512 = Undercity；528 = Orgrimmar）                                                                                                                                                                |
| 7    | reputationClassMask  | BitMask                                      | (479 = Cenerion Circle；1503 = Lower City、"Friendly, Hidden"、Netherwing；Shatari Skyguards)                                                                                                                                                                                                                     |
| 8    | reputationClassMask  | BitMask                                      | (1024 = Cenerion Circle；)                                                                                                                                                                                                                                                                                        |
| 9    | reputationClassMask  | BitMask                                      | 在 3.\* 之前从未设置，但 "Kirin Tor" 上为 0x80                                                                                                                                                                                                                                                                    |
| 10   | reputationClassMask  | BitMask                                      | 在 3.\* 之前从未设置，但 "Kirin Tor" 上为 0x80                                                                                                                                                                                                                                                                    |
| 11   | reputationBase       | Integer\[4\]                                 | 基于 0 = 中立                                                                                                                                                                                                                                                                                                    |
| 15   | reputationFlags      | Integer\[4\]                                 |                                                                                                                                                                                                                                                                                                                  |
| 19   | **parentFactionID**  | iRefID                                       | 递归。例如 Undercity 列出 ID 67，即 Horde                                                                                                                                                                                                                                                                        |
| 20   | parentFactionMod     | Float\[2\]                                   |                                                                                                                                                                                                                                                                                                                  |
| 22   | parentFactionCap     | Integer\[2\]                                 |                                                                                                                                                                                                                                                                                                                  |
| 24   | Name                 | [Loc](https://wowdev.wiki/Localization "Loc") | 阵营的显示名称                                                                                                                                                                                                                                                                                                   |
| 41   | Description          | [Loc](https://wowdev.wiki/Localization "Loc") | 点击时在声望界面中显示。                                                                                                                                                                                                                                                                                          |

### 标志（Flags）

       FACTION_FLAG_NONE             = 0x00, // 无阵营标志
       FACTION_FLAG_VISIBLE          = 0x01, // 使客户端可见（在与该阵营的目标交互时设置或可被设置）
       FACTION_FLAG_AT_WAR           = 0x02, // 启用客户端的 AtWar 按钮。由玩家控制（敌对阵营除外，始终处于战争状态），该标志仅在初始创建时设置
       FACTION_FLAG_HIDDEN           = 0x04, // 在客户端的声望面板中隐藏阵营（玩家可以获得声望，但该更新不会发送给客户端）
       FACTION_FLAG_INVISIBLE_FORCED = 0x08, // 始终覆盖 FACTION_FLAG_VISIBLE 并在声望列表中隐藏阵营，用于隐藏敌对阵营
       FACTION_FLAG_PEACE_FORCED     = 0x10, // 始终覆盖 FACTION_FLAG_AT_WAR，用于防止与己方阵营发生战争
       FACTION_FLAG_INACTIVE         = 0x20, // 由玩家控制，状态存储在 characters.data 中（CMSG_SET_FACTION_INACTIVE）
       FACTION_FLAG_RIVAL            = 0x40, // 用于两个相互竞争的外域阵营的标志
       FACTION_FLAG_SPECIAL          = 0x80 // 部落和联盟的主城及其诺森德盟友拥有此标志

### 内容

当引用生物的 [faction](creature_template#faction) 时，我们使用 [ID](#id) 值。

当引用声望获取（例如：`.modify reputation`）时，我们使用 [Faction](#faction) 值。

| [ID](#id) | [Faction](#faction) |            阵营名称             |   声望索引   |
| :-------: | :-----------------: | :-----------------------------: | :----------: |
|     1     |          1          |            PLAYER, Human            | 无法获得声望 |
|     2     |          2          |             PLAYER, Orc             | 无法获得声望 |
|     3     |          3          |            PLAYER, Dwarf            | 无法获得声望 |
|     4     |          4          |          PLAYER, Night Elf          | 无法获得声望 |
|     5     |          5          |           PLAYER, Undead            | 无法获得声望 |
|     6     |          6          |           PLAYER, Tauren            | 无法获得声望 |
|     7     |          7          |              Creature               | 无法获得声望 |
|    10     |         40          |              Escortee               | 无法获得声望 |
|    11     |         72          |              Stormwind              |          19           |
|    12     |         72          |              Stormwind              |          19           |
|    14     |         14          |               Monster               | 无法获得声望 |
|    15     |          7          |              Creature               | 无法获得声望 |
|    16     |         14          |               Monster               | 无法获得声望 |
|    17     |         15          |         Defias Brotherhood          | 无法获得声望 |
|    18     |         19          |               Murloc                | 无法获得声望 |
|    19     |         17          |          Gnoll - Redridge           | 无法获得声望 |
|    20     |         16          |          Gnoll - Riverpaw           | 无法获得声望 |
|    21     |         20          |           Undead, Scourge           | 无法获得声望 |
|    22     |         22          |           Beast - Spider            | 无法获得声望 |
|    23     |         54          |          Gnomeregan Exiles          |          18           |
|    24     |         24          |               Worgen                | 无法获得声望 |
|    25     |         25          |               Kobold                | 无法获得声望 |
|    26     |         25          |               Kobold                | 无法获得声望 |
|    27     |         15          |         Defias Brotherhood          | 无法获得声望 |
|    28     |         26          |          Troll, Bloodscalp          | 无法获得声望 |
|    29     |         76          |              Orgrimmar              |          14           |
|    30     |         27          |        Troll, Skullsplitter         | 无法获得声望 |
|    31     |         28          |                Prey                 | 无法获得声望 |
|    32     |         29          |            Beast - Wolf             | 无法获得声望 |
|    33     |         40          |              Escortee               | 无法获得声望 |
|    34     |         15          |         Defias Brotherhood          | 无法获得声望 |
|    35     |         31          |              Friendly               | 无法获得声望 |
|    36     |         32          |                Trogg                | 无法获得声望 |
|    37     |         33          |          Troll, Frostmane           | 无法获得声望 |
|    38     |         29          |            Beast - Wolf             | 无法获得声望 |
|    39     |         18          |         Gnoll - Shadowhide          | 无法获得声望 |
|    40     |         34          |           Orc, Blackrock            | 无法获得声望 |
|    41     |         35          |               Villian               | 无法获得声望 |
|    42     |         36          |               Victim                | 无法获得声望 |
|    43     |         35          |               Villian               | 无法获得声望 |
|    44     |         37          |            Beast - Bear             | 无法获得声望 |
|    45     |         38          |                Ogre                 | 无法获得声望 |
|    46     |         39          |        Kurzen\'s Mercenaries        | 无法获得声望 |
|    47     |         41          |           Venture Company           | 无法获得声望 |
|    48     |         42          |           Beast - Raptor            | 无法获得声望 |
|    49     |         43          |              Basilisk               | 无法获得声望 |
|    50     |         44          |         Dragonflight, Green         | 无法获得声望 |
|    51     |         45          |              Lost Ones              | 无法获得声望 |
|    52     |         769         |          Gizlock\'s Dummy           | 无法获得声望 |
|    53     |         49          |         Human, Night Watch          | 无法获得声望 |
|    54     |         48          |          Dark Iron Dwarves          | 无法获得声望 |
|    55     |         47          |              Ironforge              |          20           |
|    56     |         49          |         Human, Night Watch          | 无法获得声望 |
|    57     |         47          |              Ironforge              |          20           |
|    58     |          7          |              Creature               | 无法获得声望 |
|    59     |         32          |                Trogg                | 无法获得声望 |
|    60     |         50          |          Dragonflight, Red          | 无法获得声望 |
|    61     |         51          |          Gnoll - Mosshide           | 无法获得声望 |
|    62     |         52          |           Orc, Dragonmaw            | 无法获得声望 |
|    63     |         53          |            Gnome - Leper            | 无法获得声望 |
|    64     |         54          |          Gnomeregan Exiles          |          18           |
|    65     |         76          |              Orgrimmar              |          14           |
|    66     |         55          |               Leopard               | 无法获得声望 |
|    67     |         56          |           Scarlet Crusade           | 无法获得声望 |
|    68     |         68          |              Undercity              |          17           |
|    69     |         470         |               Ratchet               |           9           |
|    70     |         57          |           Gnoll - Rothide           | 无法获得声望 |
|    71     |         68          |              Undercity              |          17           |
|    72     |         58          |           Beast - Gorilla           | 无法获得声望 |
|    73     |         669         |        Beast - Carrion Bird         | 无法获得声望 |
|    74     |         60          |                Naga                 | 无法获得声望 |
|    76     |         61          |               Dalaran               | 无法获得声望 |
|    77     |         62          |           Forlorn Spirit            | 无法获得声望 |
|    78     |         63          |              Darkhowl               | 无法获得声望 |
|    79     |         69          |              Darnassus              |          21           |
|    80     |         69          |              Darnassus              |          21           |
|    81     |         64          |                Grell                | 无法获得声望 |
|    82     |         65          |               Furbolg               | 无法获得声望 |
|    83     |         66          |            Horde Generic            | 无法获得声望 |
|    84     |         189         |          Alliance Generic           | 无法获得声望 |
|    85     |         76          |              Orgrimmar              |          14           |
|    86     |         770         |          Gizlock\'s Charm           | 无法获得声望 |
|    87     |         70          |              Syndicate              |           6           |
|    88     |         71          |          Hillsbrad Militia          | 无法获得声望 |
|    89     |         56          |           Scarlet Crusade           | 无法获得声望 |
|    90     |         73          |                Demon                | 无法获得声望 |
|    91     |         74          |              Elemental              | 无法获得声望 |
|    92     |         75          |               Spirit                | 无法获得声望 |
|    93     |         14          |               Monster               | 无法获得声望 |
|    94     |         77          |              Treasure               | 无法获得声望 |
|    95     |         78          |          Gnoll - Mudsnout           | 无法获得声望 |
|    96     |         79          |     HIllsbrad, Southshore Mayor     | 无法获得声望 |
|    97     |         70          |              Syndicate              |           6           |
|    98     |         68          |              Undercity              |          17           |
|    99     |         36          |               Victim                | 无法获得声望 |
|    100    |         77          |              Treasure               | 无法获得声望 |
|    101    |         77          |              Treasure               | 无法获得声望 |
|    102    |         77          |              Treasure               | 无法获得声望 |
|    103    |         80          |         Dragonflight, Black         | 无法获得声望 |
|    104    |         81          |            Thunder Bluff            |          16           |
|    105    |         81          |            Thunder Bluff            |          16           |
|    106    |         66          |            Horde Generic            | 无法获得声望 |
|    107    |         33          |          Troll, Frostmane           | 无法获得声望 |
|    108    |         70          |              Syndicate              |           6           |
|    109    |         110         |        Quilboar, Razormane 2        | 无法获得声望 |
|    110    |         110         |        Quilboar, Razormane 2        | 无法获得声望 |
|    111    |         85          |        Quilboar, Bristleback        | 无法获得声望 |
|    112    |         85          |        Quilboar, Bristleback        | 无法获得声望 |
|    113    |         40          |              Escortee               | 无法获得声望 |
|    114    |         77          |              Treasure               | 无法获得声望 |
|    115    |          8          |            PLAYER, Gnome            | 无法获得声望 |
|    116    |          9          |            PLAYER, Troll            | 无法获得声望 |
|    118    |         68          |              Undercity              |          17           |
|    119    |         87          |        Bloodsail Buccaneers         |           0           |
|    120    |         21          |              Booty Bay              |           1           |
|    121    |         21          |              Booty Bay              |           1           |
|    122    |         47          |              Ironforge              |          20           |
|    123    |         72          |              Stormwind              |          19           |
|    124    |         69          |              Darnassus              |          21           |
|    125    |         76          |              Orgrimmar              |          14           |
|    126    |         530         |          Darkspear Trolls           |          15           |
|    127    |         35          |               Villian               | 无法获得声望 |
|    128    |         88          |             Blackfathom             | 无法获得声望 |
|    129    |         89          |               Makrura               | 无法获得声望 |
|    130    |         90          |           Centaur, Kolkar           | 无法获得声望 |
|    131    |         91          |           Centaur, Galak            | 无法获得声望 |
|    132    |         92          |         Gelkis Clan Centaur         |           2           |
|    133    |         93          |         Magram Clan Centaur         |           3           |
|    134    |         94          |              Maraudine              | 无法获得声望 |
|    148    |         14          |               Monster               | 无法获得声望 |
|    149    |         108         |              Theramore              | 无法获得声望 |
|    150    |         108         |              Theramore              | 无法获得声望 |
|    151    |         108         |              Theramore              | 无法获得声望 |
|    152    |         109         |         Quilboar, Razorfen          | 无法获得声望 |
|    153    |         109         |         Quilboar, Razorfen          | 无法获得声望 |
|    154    |         111         |        Quilboar, Deathshead         | 无法获得声望 |
|    168    |         128         |                Enemy                | 无法获得声望 |
|    188    |         148         |               Ambient               | 无法获得声望 |
|    189    |          7          |              Creature               | 无法获得声望 |
|    190    |         148         |               Ambient               | 无法获得声望 |
|    208    |         168         |         Nethergarde Caravan         | 无法获得声望 |
|    209    |         168         |         Nethergarde Caravan         | 无法获得声望 |
|    210    |         189         |          Alliance Generic           | 无法获得声望 |
|    230    |         573         |        Southsea Freebooters         | 无法获得声望 |
|    231    |         40          |              Escortee               | 无法获得声望 |
|    232    |         40          |              Escortee               | 无法获得声望 |
|    233    |         20          |           Undead, Scourge           | 无法获得声望 |
|    250    |         40          |              Escortee               | 无法获得声望 |
|    270    |         229         |           Wailing Caverns           | 无法获得声望 |
|    290    |         40          |              Escortee               | 无法获得声望 |
|    310    |         249         |              Silithid               | 无法获得声望 |
|    311    |         249         |              Silithid               | 无法获得声望 |
|    312    |         22          |           Beast - Spider            | 无法获得声望 |
|    330    |         229         |           Wailing Caverns           | 无法获得声望 |
|    350    |         88          |             Blackfathom             | 无法获得声望 |
|    370    |         915         |          Armies of C\'Thun          | 无法获得声望 |
|    371    |         269         |         Silvermoon Remnant          | 无法获得声望 |
|    390    |         21          |              Booty Bay              |           1           |
|    410    |         43          |              Basilisk               | 无法获得声望 |
|    411    |         310         |             Beast - Bat             | 无法获得声望 |
|    412    |         510         |            The Defilers             |          52           |
|    413    |         309         |               Scorpid               | 无法获得声望 |
|    414    |         576         |           Timbermaw Hold            |          35           |
|    415    |         311         |                Titan                | 无法获得声望 |
|    416    |         311         |                Titan                | 无法获得声望 |
|    430    |         329         |         Taskmaster Fizzule          | 无法获得声望 |
|    450    |         229         |           Wailing Caverns           | 无法获得声望 |
|    470    |         311         |                Titan                | 无法获得声望 |
|    471    |         349         |             Ravenholdt              |           5           |
|    472    |         70          |              Syndicate              |           6           |
|    473    |         349         |             Ravenholdt              |           5           |
|    474    |         369         |              Gadgetzan              |           7           |
|    475    |         369         |              Gadgetzan              |           7           |
|    494    |         389         |           Gnomeregan Bug            | 无法获得声望 |
|    495    |         40          |              Escortee               | 无法获得声望 |
|    514    |         409         |                Harpy                | 无法获得声望 |
|    534    |         189         |          Alliance Generic           | 无法获得声望 |
|    554    |         429         |            Burning Blade            | 无法获得声望 |
|    574    |         449         |         Shadowsilk Poacher          | 无法获得声望 |
|    575    |         450         |           Searing Spider            | 无法获得声望 |
|    594    |         32          |                Trogg                | 无法获得声望 |
|    614    |         36          |               Victim                | 无法获得声望 |
|    634    |         14          |               Monster               | 无法获得声望 |
|    635    |         609         |           Cenarion Circle           |          36           |
|    636    |         576         |           Timbermaw Hold            |          35           |
|    637    |         470         |               Ratchet               |           9           |
|    654    |         82          |          Troll, Witherbark          | 无法获得声望 |
|    655    |         90          |           Centaur, Kolkar           | 无法获得声望 |
|    674    |         48          |          Dark Iron Dwarves          | 无法获得声望 |
|    694    |         189         |          Alliance Generic           | 无法获得声望 |
|    695    |         749         |        Hydraxian Waterlords         |          42           |
|    714    |         66          |            Horde Generic            | 无法获得声望 |
|    734    |         48          |          Dark Iron Dwarves          | 无法获得声望 |
|    735    |         489         |    Goblin, Dark Iron Bar Patron     | 无法获得声望 |
|    736    |         489         |    Goblin, Dark Iron Bar Patron     | 无法获得声望 |
|    754    |         48          |          Dark Iron Dwarves          | 无法获得声望 |
|    774    |         40          |              Escortee               | 无法获得声望 |
|    775    |         40          |              Escortee               | 无法获得声望 |
|    776    |         910         |          Brood of Nozdormu          |          54           |
|    777    |         912         |          Might of Kalimdor          | 无法获得声望 |
|    778    |         511         |                Giant                | 无法获得声望 |
|    794    |         529         |             Argent Dawn             |          13           |
|    795    |         572         |          Troll, Vilebranch          | 无法获得声望 |
|    814    |         529         |             Argent Dawn             |          13           |
|    834    |         74          |              Elemental              | 无法获得声望 |
|    854    |         577         |              Everlook               |          28           |
|    855    |         577         |              Everlook               |          28           |
|    874    |         589         |        Wintersaber Trainers         |          27           |
|    875    |         54          |          Gnomeregan Exiles          |          18           |
|    876    |         530         |          Darkspear Trolls           |          15           |
|    877    |         530         |          Darkspear Trolls           |          15           |
|    894    |         108         |              Theramore              | 无法获得声望 |
|    914    |         679         |           Training Dummy            | 无法获得声望 |
|    934    |         575         |        Furbolg, Uncorrupted         | 无法获得声望 |
|    954    |         73          |                Demon                | 无法获得声望 |
|    974    |         20          |           Undead, Scourge           | 无法获得声望 |
|    994    |         609         |           Cenarion Circle           |          36           |
|    995    |         81          |            Thunder Bluff            |          16           |
|    996    |         609         |           Cenarion Circle           |          36           |
|   1014    |         629         |         Shatterspear Trolls         | 无法获得声望 |
|   1015    |         629         |         Shatterspear Trolls         | 无法获得声望 |
|   1034    |         66          |            Horde Generic            | 无法获得声望 |
|   1054    |         189         |          Alliance Generic           | 无法获得声望 |
|   1055    |         189         |          Alliance Generic           | 无法获得声望 |
|   1074    |         76          |              Orgrimmar              |          14           |
|   1075    |         108         |              Theramore              | 无法获得声望 |
|   1076    |         69          |              Darnassus              |          21           |
|   1077    |         108         |              Theramore              | 无法获得声望 |
|   1078    |         72          |              Stormwind              |          19           |
|   1080    |         31          |              Friendly               | 无法获得声望 |
|   1081    |         74          |              Elemental              | 无法获得声望 |
|   1094    |         23          |            Beast - Boar             | 无法获得声望 |
|   1095    |         679         |           Training Dummy            | 无法获得声望 |
|   1096    |         108         |              Theramore              | 无法获得声望 |
|   1097    |         69          |              Darnassus              |          21           |
|   1114    |         689         |     Dragonflight, Black - Bait      | 无法获得声望 |
|   1134    |         68          |              Undercity              |          17           |
|   1154    |         68          |              Undercity              |          17           |
|   1174    |         76          |              Orgrimmar              |          14           |
|   1194    |         709         |        Battleground Neutral         | 无法获得声望 |
|   1214    |         729         |           Frostwolf Clan            |          41           |
|   1215    |         729         |           Frostwolf Clan            |          41           |
|   1216    |         730         |           Stormpike Guard           |          40           |
|   1217    |         730         |           Stormpike Guard           |          40           |
|   1234    |         750         |         Sulfuron Firelords          | 无法获得声望 |
|   1235    |         750         |         Sulfuron Firelords          | 无法获得声望 |
|   1236    |         750         |         Sulfuron Firelords          | 无法获得声望 |
|   1254    |         609         |           Cenarion Circle           |          36           |
|   1274    |          7          |              Creature               | 无法获得声望 |
|   1275    |          7          |              Creature               | 无法获得声望 |
|   1294    |         771         |               Gizlock               | 无法获得声望 |
|   1314    |         66          |            Horde Generic            | 无法获得声望 |
|   1315    |         189         |          Alliance Generic           | 无法获得声望 |
|   1334    |         730         |           Stormpike Guard           |          40           |
|   1335    |         729         |           Frostwolf Clan            |          41           |
|   1354    |         809         |            Shen\'dralar             |          44           |
|   1355    |         809         |            Shen\'dralar             |          44           |
|   1374    |         829         |      Ogre (Captain Kromcrush)       | 无法获得声望 |
|   1375    |         77          |              Treasure               | 无法获得声望 |
|   1394    |         80          |         Dragonflight, Black         | 无法获得声望 |
|   1395    |         916         |         Silithid Attackers          | 无法获得声望 |
|   1414    |         790         |       Spirit Guide - Alliance       | 无法获得声望 |
|   1415    |         849         |        Spirit Guide - Horde         | 无法获得声望 |
|   1434    |         869         |              Jaedenar               | 无法获得声望 |
|   1454    |         36          |               Victim                | 无法获得声望 |
|   1474    |         59          |         Thorium Brotherhood         |           4           |
|   1475    |         59          |         Thorium Brotherhood         |           4           |
|   1494    |         66          |            Horde Generic            | 无法获得声望 |
|   1495    |         66          |            Horde Generic            | 无法获得声望 |
|   1496    |         66          |            Horde Generic            | 无法获得声望 |
|   1514    |         890         |        Silverwing Sentinels         |          45           |
|   1515    |         889         |          Warsong Outriders          |          46           |
|   1534    |         730         |           Stormpike Guard           |          40           |
|   1554    |         729         |           Frostwolf Clan            |          41           |
|   1555    |         909         |           Darkmoon Faire            |          50           |
|   1574    |         270         |           Zandalar Tribe            |          51           |
|   1575    |         72          |              Stormwind              |          19           |
|   1576    |         269         |         Silvermoon Remnant          | 无法获得声望 |
|   1577    |         509         |        The League of Arathor        |          53           |
|   1594    |         69          |              Darnassus              |          21           |
|   1595    |         76          |              Orgrimmar              |          14           |
|   1596    |         730         |           Stormpike Guard           |          40           |
|   1597    |         729         |           Frostwolf Clan            |          41           |
|   1598    |         510         |            The Defilers             |          52           |
|   1599    |         509         |        The League of Arathor        |          53           |
|   1600    |         69          |              Darnassus              |          21           |
|   1601    |         910         |          Brood of Nozdormu          |          54           |
|   1602    |         911         |           Silvermoon City           |          55           |
|   1603    |         911         |           Silvermoon City           |          55           |
|   1604    |         911         |           Silvermoon City           |          55           |
|   1605    |         531         |        Dragonflight, Bronze         | 无法获得声望 |
|   1606    |          7          |              Creature               | 无法获得声望 |
|   1607    |          7          |              Creature               | 无法获得声望 |
|   1608    |         609         |           Cenarion Circle           |          36           |
|   1610    |         914         |          PLAYER, Blood Elf          | 无法获得声望 |
|   1611    |         47          |              Ironforge              |          20           |
|   1612    |         76          |              Orgrimmar              |          14           |
|   1613    |         912         |          Might of Kalimdor          | 无法获得声望 |
|   1614    |         14          |               Monster               | 无法获得声望 |
|   1615    |         169         |         Steamwheedle Cartel         |          10           |
|   1616    |         919         |             RC Objects              | 无法获得声望 |
|   1617    |         918         |             RC Enemies              | 无法获得声望 |
|   1618    |         47          |              Ironforge              |          20           |
|   1619    |         76          |              Orgrimmar              |          14           |
|   1620    |         128         |                Enemy                | 无法获得声望 |
|   1621    |         921         |                Blue                 | 无法获得声望 |
|   1622    |         920         |                 Red                 | 无法获得声望 |
|   1623    |         922         |            Tranquillien             |          56           |
|   1624    |         529         |             Argent Dawn             |          13           |
|   1625    |         529         |             Argent Dawn             |          13           |
|   1626    |         20          |           Undead, Scourge           | 无法获得声望 |
|   1627    |         923         |             Farstriders             | 无法获得声望 |
|   1628    |         922         |            Tranquillien             |          56           |
|   1629    |         927         |           PLAYER, Draenei           | 无法获得声望 |
|   1630    |         928         |          Scourge Invaders           | 无法获得声望 |
|   1634    |         928         |          Scourge Invaders           | 无法获得声望 |
|   1635    |         169         |         Steamwheedle Cartel         |          10           |
|   1636    |         923         |             Farstriders             | 无法获得声望 |
|   1637    |         923         |             Farstriders             | 无法获得声望 |
|   1638    |         930         |               Exodar                |          49           |
|   1639    |         930         |               Exodar                |          49           |
|   1640    |         930         |               Exodar                |          49           |
|   1641    |         889         |          Warsong Outriders          |          46           |
|   1642    |         890         |        Silverwing Sentinels         |          45           |
|   1643    |         937         |            Troll, Forest            | 无法获得声望 |
|   1644    |         940         |         The Sons of Lothar          | 无法获得声望 |
|   1645    |         940         |         The Sons of Lothar          | 无法获得声望 |
|   1646    |         930         |               Exodar                |          49           |
|   1647    |         930         |               Exodar                |          49           |
|   1648    |         940         |         The Sons of Lothar          | 无法获得声望 |
|   1649    |         940         |         The Sons of Lothar          | 无法获得声望 |
|   1650    |         941         |            The Mag\'har             |          61           |
|   1651    |         941         |            The Mag\'har             |          61           |
|   1652    |         941         |            The Mag\'har             |          61           |
|   1653    |         941         |            The Mag\'har             |          61           |
|   1654    |         930         |               Exodar                |          49           |
|   1655    |         930         |               Exodar                |          49           |
|   1656    |         911         |           Silvermoon City           |          55           |
|   1657    |         911         |           Silvermoon City           |          55           |
|   1658    |         911         |           Silvermoon City           |          55           |
|   1659    |         942         |         Cenarion Expedition         |          64           |
|   1660    |         942         |         Cenarion Expedition         |          64           |
|   1661    |         942         |         Cenarion Expedition         |          64           |
|   1662    |         943         |               Fel Orc               | 无法获得声望 |
|   1663    |         944         |            Fel Orc Ghost            | 无法获得声望 |
|   1664    |         945         |        Sons of Lothar Ghosts        | 无法获得声望 |
|   1666    |         946         |             Honor Hold              |          38           |
|   1667    |         946         |             Honor Hold              |          38           |
|   1668    |         947         |              Thrallmar              |          37           |
|   1669    |         947         |              Thrallmar              |          37           |
|   1670    |         947         |              Thrallmar              |          37           |
|   1671    |         946         |             Honor Hold              |          38           |
|   1672    |         949         |           Test Faction 1            |          85           |
|   1673    |         950         |            ToWoW - Flag             | 无法获得声望 |
|   1674    |         953         |           Test Faction 4            | 无法获得声望 |
|   1675    |         952         |           Test Faction 3            |          87           |
|   1676    |         954         |  ToWoW - Flag Trigger Horde (DND)   | 无法获得声望 |
|   1677    |         951         | ToWoW - Flag Trigger Alliance (DND) | 无法获得声望 |
|   1678    |         956         |              Ethereum               | 无法获得声望 |
|   1679    |         955         |               Broken                | 无法获得声望 |
|   1680    |         74          |              Elemental              | 无法获得声望 |
|   1681    |         957         |           Earth Elemental           | 无法获得声望 |
|   1682    |         958         |           Fighting Robots           | 无法获得声望 |
|   1683    |         959         |             Actor Good              | 无法获得声望 |
|   1684    |         960         |             Actor Evil              | 无法获得声望 |
|   1685    |         961         |          Stillpine Furbolg          | 无法获得声望 |
|   1686    |         961         |          Stillpine Furbolg          | 无法获得声望 |
|   1687    |         962         |            Crazed Owlkin            | 无法获得声望 |
|   1688    |         963         |           Chess Alliance            | 无法获得声望 |
|   1689    |         964         |             Chess Horde             | 无法获得声望 |
|   1690    |         963         |           Chess Alliance            | 无法获得声望 |
|   1691    |         964         |             Chess Horde             | 无法获得声望 |
|   1692    |         965         |            Monster Spar             | 无法获得声望 |
|   1693    |         966         |         Monster Spar Buddy          | 无法获得声望 |
|   1694    |         930         |               Exodar                |          49           |
|   1695    |         911         |           Silvermoon City           |          55           |
|   1696    |         967         |           The Violet Eye            |          63           |
|   1697    |         943         |               Fel Orc               | 无法获得声望 |
|   1698    |         930         |               Exodar                |          49           |
|   1699    |         930         |               Exodar                |          49           |
|   1700    |         930         |               Exodar                |          49           |
|   1701    |         968         |              Sunhawks               | 无法获得声望 |
|   1702    |         968         |              Sunhawks               | 无法获得声望 |
|   1703    |         679         |           Training Dummy            | 无法获得声望 |
|   1704    |         943         |               Fel Orc               | 无法获得声望 |
|   1705    |         943         |               Fel Orc               | 无法获得声望 |
|   1706    |         971         |            Fungal Giant             | 无法获得声望 |
|   1707    |         970         |              Sporeggar              |          65           |
|   1708    |         970         |              Sporeggar              |          65           |
|   1709    |         970         |              Sporeggar              |          65           |
|   1710    |         942         |         Cenarion Expedition         |          64           |
|   1711    |         973         |          Monster, Predator          | 无法获得声望 |
|   1712    |         974         |            Monster, Prey            | 无法获得声望 |
|   1713    |         974         |            Monster, Prey            | 无法获得声望 |
|   1714    |         968         |              Sunhawks               | 无法获得声望 |
|   1715    |         975         |            Void Anomaly             | 无法获得声望 |
|   1716    |         976         |           Hyjal Defenders           | 无法获得声望 |
|   1717    |         976         |           Hyjal Defenders           | 无法获得声望 |
|   1718    |         976         |           Hyjal Defenders           | 无法获得声望 |
|   1719    |         976         |           Hyjal Defenders           | 无法获得声望 |
|   1720    |         977         |           Hyjal Invaders            | 无法获得声望 |
|   1721    |         978         |               Kurenai               |          66           |
|   1722    |         978         |               Kurenai               |          66           |
|   1723    |         978         |               Kurenai               |          66           |
|   1724    |         978         |               Kurenai               |          66           |
|   1725    |         979         |            Earthen Ring             | 无法获得声望 |
|   1726    |         979         |            Earthen Ring             | 无法获得声望 |
|   1727    |         979         |            Earthen Ring             | 无法获得声望 |
|   1728    |         942         |         Cenarion Expedition         |          64           |
|   1729    |         947         |              Thrallmar              |          37           |
|   1730    |         933         |           The Consortium            |          60           |
|   1731    |         933         |           The Consortium            |          60           |
|   1732    |         189         |          Alliance Generic           | 无法获得声望 |
|   1733    |         189         |          Alliance Generic           | 无法获得声望 |
|   1734    |         66          |            Horde Generic            | 无法获得声望 |
|   1735    |         66          |            Horde Generic            | 无法获得声望 |
|   1736    |         966         |         Monster Spar Buddy          | 无法获得声望 |
|   1737    |         946         |             Honor Hold              |          38           |
|   1738    |         981         |               Arakkoa               | 无法获得声望 |
|   1739    |         982         |    Zangarmarsh Banner (Alliance)    | 无法获得声望 |
|   1740    |         983         |     Zangarmarsh Banner (Horde)      | 无法获得声望 |
|   1741    |         935         |            The Sha\'tar             |          39           |
|   1742    |         984         |    Zangarmarsh Banner (Neutral)     | 无法获得声望 |
|   1743    |         932         |              The Aldor              |          58           |
|   1744    |         934         |             The Scryers             |          62           |
|   1745    |         911         |           Silvermoon City           |          55           |
|   1746    |         934         |             The Scryers             |          62           |
|   1747    |         985         |      Caverns of Time - Thrall       | 无法获得声望 |
|   1748    |         986         |     Caverns of Time - Durnholde     | 无法获得声望 |
|   1749    |         987         | Caverns of Time - Southshore Guards | 无法获得声望 |
|   1750    |         988         |        Shadow Council Covert        | 无法获得声望 |
|   1751    |         14          |               Monster               | 无法获得声望 |
|   1752    |         993         |    Dark Portal Attacker, Legion     | 无法获得声望 |
|   1753    |         993         |    Dark Portal Attacker, Legion     | 无法获得声望 |
|   1754    |         993         |    Dark Portal Attacker, Legion     | 无法获得声望 |
|   1755    |         991         |   Dark Portal Defender, Alliance    | 无法获得声望 |
|   1756    |         991         |   Dark Portal Defender, Alliance    | 无法获得声望 |
|   1757    |         991         |   Dark Portal Defender, Alliance    | 无法获得声望 |
|   1758    |         992         |     Dark Portal Defender, Horde     | 无法获得声望 |
|   1759    |         992         |     Dark Portal Defender, Horde     | 无法获得声望 |
|   1760    |         992         |     Dark Portal Defender, Horde     | 无法获得声望 |
|   1761    |         994         |           Inciter Trigger           | 无法获得声望 |
|   1762    |         995         |          Inciter Trigger 2          | 无法获得声望 |
|   1763    |         996         |          Inciter Trigger 3          | 无法获得声望 |
|   1764    |         997         |          Inciter Trigger 4          | 无法获得声望 |
|   1765    |         998         |          Inciter Trigger 5          | 无法获得声望 |
|   1766    |         529         |             Argent Dawn             |          13           |
|   1767    |         529         |             Argent Dawn             |          13           |
|   1768    |         73          |                Demon                | 无法获得声望 |
|   1769    |         73          |                Demon                | 无法获得声望 |
|   1770    |         959         |             Actor Good              | 无法获得声望 |
|   1771    |         960         |             Actor Evil              | 无法获得声望 |
|   1772    |         999         |            Mana Creature            | 无法获得声望 |
|   1773    |        1000         |         Khadgar\'s Servant          | 无法获得声望 |
|   1774    |         31          |              Friendly               | 无法获得声望 |
|   1775    |         935         |            The Sha\'tar             |          39           |
|   1776    |         932         |              The Aldor              |          58           |
|   1777    |         932         |              The Aldor              |          58           |
|   1778    |         990         |       The Scale of the Sands        |          57           |
|   1779    |         989         |           Keepers of Time           |          67           |
|   1780    |        1001         |           Bladespire Clan           | 无法获得声望 |
|   1781    |         929         |           Bloodmaul Clan            | 无法获得声望 |
|   1782    |        1001         |           Bladespire Clan           | 无法获得声望 |
|   1783    |         929         |           Bloodmaul Clan            | 无法获得声望 |
|   1784    |        1001         |           Bladespire Clan           | 无法获得声望 |
|   1785    |         929         |           Bloodmaul Clan            | 无法获得声望 |
|   1786    |         73          |                Demon                | 无法获得声望 |
|   1787    |         14          |               Monster               | 无法获得声望 |
|   1788    |         933         |           The Consortium            |          60           |
|   1789    |         968         |              Sunhawks               | 无法获得声望 |
|   1790    |        1001         |           Bladespire Clan           | 无法获得声望 |
|   1791    |         929         |           Bloodmaul Clan            | 无法获得声望 |
|   1792    |         943         |               Fel Orc               | 无法获得声望 |
|   1793    |         968         |              Sunhawks               | 无法获得声望 |
|   1794    |        1003         |            Protectorate             | 无法获得声望 |
|   1795    |        1003         |            Protectorate             | 无法获得声望 |
|   1796    |         956         |              Ethereum               | 无法获得声望 |
|   1797    |        1003         |            Protectorate             | 无法获得声望 |
|   1798    |        1004         |      Arcane Annihilator (DNR)       | 无法获得声望 |
|   1799    |        1002         |         Ethereum Sparbuddy          | 无法获得声望 |
|   1800    |         956         |              Ethereum               | 无法获得声望 |
|   1801    |         67          |                Horde                |          12           |
|   1802    |         469         |              Alliance               |          11           |
|   1803    |         148         |               Ambient               | 无法获得声望 |
|   1804    |         148         |               Ambient               | 无法获得声望 |
|   1805    |         932         |              The Aldor              |          58           |
|   1806    |         31          |              Friendly               | 无法获得声望 |
|   1807    |        1003         |            Protectorate             | 无法获得声望 |
|   1808    |        1007         |        Kirin\'Var - Belmara         | 无法获得声望 |
|   1809    |        1009         |        Kirin\'Var - Cohlien         | 无法获得声望 |
|   1810    |        1006         |        Kirin\'Var - Dathric         | 无法获得声望 |
|   1811    |        1008         |       Kirin\'Var - Luminrath        | 无法获得声望 |
|   1812    |         31          |              Friendly               | 无法获得声望 |
|   1813    |        1010         |         Servant of Illidan          | 无法获得声望 |
|   1814    |         966         |         Monster Spar Buddy          | 无法获得声望 |
|   1815    |         29          |            Beast - Wolf             | 无法获得声望 |
|   1816    |         31          |              Friendly               | 无法获得声望 |
|   1818    |        1011         |             Lower City              |          69           |
|   1819    |         189         |          Alliance Generic           | 无法获得声望 |
|   1820    |        1012         |        Ashtongue Deathsworn         |          70           |
|   1821    |        1013         |       Spirits of Shadowmoon 1       | 无法获得声望 |
|   1822    |        1014         |       Spirits of Shadowmoon 2       | 无法获得声望 |
|   1823    |         956         |              Ethereum               | 无法获得声望 |
|   1824    |        1015         |             Netherwing              |          71           |
|   1825    |         73          |                Demon                | 无法获得声望 |
|   1826    |        1010         |         Servant of Illidan          | 无法获得声望 |
|   1827    |        1016         |              Wyrmcult               | 无法获得声望 |
|   1828    |        1017         |               Treant                | 无法获得声望 |
|   1829    |        1018         |          Leotheras Demon I          | 无法获得声望 |
|   1830    |        1019         |         Leotheras Demon II          | 无法获得声望 |
|   1831    |        1020         |         Leotheras Demon III         | 无法获得声望 |
|   1832    |        1021         |         Leotheras Demon IV          | 无法获得声望 |
|   1833    |        1022         |          Leotheras Demon V          | 无法获得声望 |
|   1834    |        1023         |               Azaloth               | 无法获得声望 |
|   1835    |         66          |            Horde Generic            | 无法获得声望 |
|   1836    |         933         |           The Consortium            |          60           |
|   1837    |         970         |              Sporeggar              |          65           |
|   1838    |         934         |             The Scryers             |          62           |
|   1839    |        1024         |             Rock Flayer             | 无法获得声望 |
|   1840    |        1025         |            Flayer Hunter            | 无法获得声望 |
|   1841    |        1026         |          Shadowmoon Shade           | 无法获得声望 |
|   1842    |        1027         |         Legion Communicator         | 无法获得声望 |
|   1843    |        1010         |         Servant of Illidan          | 无法获得声望 |
|   1844    |         932         |              The Aldor              |          58           |
|   1845    |         934         |             The Scryers             |          62           |
|   1846    |        1028         |         Ravenswood Ancients         | 无法获得声望 |
|   1847    |         965         |            Monster Spar             | 无法获得声望 |
|   1848    |         966         |         Monster Spar Buddy          | 无法获得声望 |
|   1849    |        1010         |         Servant of Illidan          | 无法获得声望 |
|   1850    |        1015         |             Netherwing              |          71           |
|   1851    |        1011         |             Lower City              |          69           |
|   1852    |        1029         |    Chess, Friendly to All Chess     | 无法获得声望 |
|   1853    |        1010         |         Servant of Illidan          | 无法获得声望 |
|   1854    |         932         |              The Aldor              |          58           |
|   1855    |         934         |             The Scryers             |          62           |
|   1856    |        1031         |         Sha\'tari Skyguard          |          72           |
|   1857    |         31          |              Friendly               | 无法获得声望 |
|   1858    |        1012         |        Ashtongue Deathsworn         |          70           |
|   1859    |        1033         |                Maiev                | 无法获得声望 |
|   1860    |        1034         |       Skettis Shadowy Arakkoa       | 无法获得声望 |
|   1862    |        1035         |           Skettis Arakkoa           | 无法获得声望 |
|   1863    |         52          |           Orc, Dragonmaw            | 无法获得声望 |
|   1864    |        1036         |           Dragonmaw Enemy           | 无法获得声望 |
|   1865    |         52          |           Orc, Dragonmaw            | 无法获得声望 |
|   1866    |        1012         |        Ashtongue Deathsworn         |          70           |
|   1867    |        1033         |                Maiev                | 无法获得声望 |
|   1868    |         966         |         Monster Spar Buddy          | 无法获得声望 |
|   1869    |         981         |               Arakkoa               | 无法获得声望 |
|   1870    |        1031         |         Sha\'tari Skyguard          |          72           |
|   1871    |        1035         |           Skettis Arakkoa           | 无法获得声望 |
|   1872    |        1038         |              Ogri\'la               |          73           |
|   1873    |        1024         |             Rock Flayer             | 无法获得声望 |
|   1874    |        1038         |              Ogri\'la               |          73           |
|   1875    |         932         |              The Aldor              |          58           |
|   1876    |         934         |             The Scryers             |          62           |
|   1877    |         52          |           Orc, Dragonmaw            | 无法获得声望 |
|   1878    |        1041         |               Frenzy                | 无法获得声望 |
|   1879    |        1042         |           Skyguard Enemy            | 无法获得声望 |
|   1880    |         52          |           Orc, Dragonmaw            | 无法获得声望 |
|   1881    |        1035         |           Skettis Arakkoa           | 无法获得声望 |
|   1882    |        1010         |         Servant of Illidan          | 无法获得声望 |
|   1883    |        1044         |         Theramore Deserter          | 无法获得声望 |
|   1884    |        1047         |               Tuskarr               | 无法获得声望 |
|   1885    |        1045         |               Vrykul                | 无法获得声望 |
|   1886    |          7          |              Creature               | 无法获得声望 |
|   1887    |          7          |              Creature               | 无法获得声望 |
|   1888    |        1046         |          Northsea Pirates           | 无法获得声望 |
|   1889    |        1048         |               UNUSED                | 无法获得声望 |
|   1890    |        1049         |            Troll, Amani             | 无法获得声望 |
|   1891    |        1050         |         Valiance Expedition         |          74           |
|   1892    |        1050         |         Valiance Expedition         |          74           |
|   1893    |        1050         |         Valiance Expedition         |          74           |
|   1894    |        1045         |               Vrykul                | 无法获得声望 |
|   1895    |        1045         |               Vrykul                | 无法获得声望 |
|   1896    |         909         |           Darkmoon Faire            |          50           |
|   1897    |        1067         |        The Hand of Vengeance        |          77           |
|   1898    |        1050         |         Valiance Expedition         |          74           |
|   1899    |        1050         |         Valiance Expedition         |          74           |
|   1900    |        1067         |        The Hand of Vengeance        |          77           |
|   1901    |        1052         |          Horde Expedition           |          75           |
|   1902    |         960         |             Actor Evil              | 无法获得声望 |
|   1904    |         960         |             Actor Evil              | 无法获得声望 |
|   1905    |        1055         |          Tamed Plaguehound          | 无法获得声望 |
|   1906    |        1054         |           Spotted Gryphon           | 无法获得声望 |
|   1907    |         949         |           Test Faction 1            |          85           |
|   1908    |         949         |           Test Faction 1            |          85           |
|   1909    |         42          |           Beast - Raptor            | 无法获得声望 |
|   1910    |        1056         |      Vrykul (Ancient Spirit 1)      | 无法获得声望 |
|   1911    |        1057         |      Vrykul (Ancient Siprit 2)      | 无法获得声望 |
|   1912    |        1058         |      Vrykul (Ancient Siprit 3)      | 无法获得声望 |
|   1913    |        1059         |        CTF - Flag - Alliance        | 无法获得声望 |
|   1914    |        1045         |               Vrykul                | 无法获得声望 |
|   1915    |        1060         |                Test                 | 无法获得声望 |
|   1916    |        1033         |                Maiev                | 无法获得声望 |
|   1917    |          7          |              Creature               | 无法获得声望 |
|   1918    |        1052         |          Horde Expedition           |          75           |
|   1919    |        1062         |          Vrykul Gladiator           | 无法获得声望 |
|   1920    |        1063         |         Valgarde Combatant          | 无法获得声望 |
|   1921    |        1064         |             The Taunka              |          76           |
|   1922    |        1064         |             The Taunka              |          76           |
|   1923    |        1064         |             The Taunka              |          76           |
|   1924    |        1065         |   Monster, Zone Force Reaction 1    | 无法获得声望 |
|   1925    |         14          |               Monster               | 无法获得声望 |
|   1926    |        1068         |         Explorers\' League          |          78           |
|   1927    |        1068         |         Explorers\' League          |          78           |
|   1928    |        1067         |        The Hand of Vengeance        |          77           |
|   1929    |        1067         |        The Hand of Vengeance        |          77           |
|   1930    |        1069         |       Ram Racing Powerup DND        | 无法获得声望 |
|   1931    |        1070         |         Ram Racing Trap DND         | 无法获得声望 |
|   1932    |         74          |              Elemental              | 无法获得声望 |
|   1933    |         31          |              Friendly               | 无法获得声望 |
|   1934    |         959         |             Actor Good              | 无法获得声望 |
|   1935    |         959         |             Actor Good              | 无法获得声望 |
|   1936    |        1071         |         Craig\'s Squirrels          | 无法获得声望 |
|   1937    |        1071         |         Craig\'s Squirrels          | 无法获得声望 |
|   1938    |        1071         |         Craig\'s Squirrels          | 无法获得声望 |
|   1939    |        1071         |         Craig\'s Squirrels          | 无法获得声望 |
|   1940    |        1071         |         Craig\'s Squirrels          | 无法获得声望 |
|   1941    |        1071         |         Craig\'s Squirrels          | 无法获得声望 |
|   1942    |        1071         |         Craig\'s Squirrels          | 无法获得声望 |
|   1943    |        1071         |         Craig\'s Squirrels          | 无法获得声望 |
|   1944    |        1071         |         Craig\'s Squirrels          | 无法获得声望 |
|   1945    |        1071         |         Craig\'s Squirrels          | 无法获得声望 |
|   1947    |        1071         |         Craig\'s Squirrels          | 无法获得声望 |
|   1948    |         921         |                Blue                 | 无法获得声望 |
|   1949    |        1073         |            The Kalu\'ak             |          79           |
|   1950    |        1073         |            The Kalu\'ak             |          79           |
|   1951    |         69          |              Darnassus              |          21           |
|   1952    |        1074         |       Holiday - Water Barrel        | 无法获得声望 |
|   1953    |         973         |          Monster, Predator          | 无法获得声望 |
|   1954    |        1076         |            Iron Dwarves             | 无法获得声望 |
|   1955    |        1076         |            Iron Dwarves             | 无法获得声望 |
|   1956    |        1077         |       Shattered Sun Offensive       |          80           |
|   1957    |        1077         |       Shattered Sun Offensive       |          80           |
|   1958    |         960         |             Actor Evil              | 无法获得声望 |
|   1959    |         960         |             Actor Evil              | 无法获得声望 |
|   1960    |        1077         |       Shattered Sun Offensive       |          80           |
|   1961    |        1078         |         Fighting Vanity Pet         | 无法获得声望 |
|   1962    |         20          |           Undead, Scourge           | 无法获得声望 |
|   1963    |         73          |                Demon                | 无法获得声望 |
|   1964    |         20          |           Undead, Scourge           | 无法获得声望 |
|   1965    |         965         |            Monster Spar             | 无法获得声望 |
|   1966    |         19          |               Murloc                | 无法获得声望 |
|   1967    |        1077         |       Shattered Sun Offensive       |          80           |
|   1968    |        1079         |          Murloc, Winterfin          | 无法获得声望 |
|   1969    |         19          |               Murloc                | 无法获得声望 |
|   1970    |         14          |               Monster               | 无法获得声望 |
|   1971    |        1080         |      Friendly, Force Reaction       | 无法获得声望 |
|   1972    |        1081         |       Object, Force Reaction        | 无法获得声望 |
|   1973    |        1050         |         Valiance Expedition         |          74           |
|   1974    |        1050         |         Valiance Expedition         |          74           |
|   1975    |         20          |           Undead, Scourge           | 无法获得声望 |
|   1976    |        1050         |         Valiance Expedition         |          74           |
|   1977    |        1050         |         Valiance Expedition         |          74           |
|   1978    |        1085         |          Warsong Offensive          |          81           |
|   1979    |        1085         |          Warsong Offensive          |          81           |
|   1980    |        1085         |          Warsong Offensive          |          81           |
|   1981    |        1085         |          Warsong Offensive          |          81           |
|   1982    |         20          |           Undead, Scourge           | 无法获得声望 |
|   1983    |         965         |            Monster Spar             | 无法获得声望 |
|   1984    |         966         |         Monster Spar Buddy          | 无法获得声望 |
|   1985    |         14          |               Monster               | 无法获得声望 |
|   1986    |         40          |              Escortee               | 无法获得声望 |
|   1987    |         942         |         Cenarion Expedition         |          64           |
|   1988    |         20          |           Undead, Scourge           | 无法获得声望 |
|   1989    |        1086         |               Poacher               | 无法获得声望 |
|   1990    |         148         |               Ambient               | 无法获得声望 |
|   1991    |         20          |           Undead, Scourge           | 无法获得声望 |
|   1992    |         14          |               Monster               | 无法获得声望 |
|   1993    |         965         |            Monster Spar             | 无法获得声望 |
|   1994    |         966         |         Monster Spar Buddy          | 无法获得声望 |
|   1995    |        1059         |        CTF - Flag - Alliance        | 无法获得声望 |
|   1997    |        1059         |        CTF - Flag - Alliance        | 无法获得声望 |
|   1998    |        1087         |           Holiday Monster           | 无法获得声望 |
|   1999    |         974         |            Monster, Prey            | 无法获得声望 |
|   2000    |         974         |            Monster, Prey            | 无法获得声望 |
|   2001    |        1088         |          Furbolg, Redfang           | 无法获得声望 |
|   2003    |        1089         |          Furbolg, Frostpaw          | 无法获得声望 |
|   2004    |        1050         |         Valiance Expedition         |          74           |
|   2005    |         20          |           Undead, Scourge           | 无法获得声望 |
|   2006    |        1090         |              Kirin Tor              |          84           |
|   2007    |        1090         |              Kirin Tor              |          84           |
|   2008    |        1090         |              Kirin Tor              |          84           |
|   2009    |        1090         |              Kirin Tor              |          84           |
|   2010    |        1091         |         The Wyrmrest Accord         |          83           |
|   2011    |        1091         |         The Wyrmrest Accord         |          83           |
|   2012    |        1091         |         The Wyrmrest Accord         |          83           |
|   2013    |        1091         |         The Wyrmrest Accord         |          83           |
|   2014    |        1092         |             Azjol-Nerub             | 无法获得声望 |
|   2016    |        1092         |             Azjol-Nerub             | 无法获得声望 |
|   2017    |        1092         |             Azjol-Nerub             | 无法获得声望 |
|   2018    |         20          |           Undead, Scourge           | 无法获得声望 |
|   2019    |        1064         |             The Taunka              |          76           |
|   2020    |        1085         |          Warsong Offensive          |          81           |
|   2021    |        1082         |                REUSE                |          82           |
|   2022    |         14          |               Monster               | 无法获得声望 |
|   2023    |         928         |          Scourge Invaders           | 无法获得声望 |
|   2024    |        1067         |        The Hand of Vengeance        |          77           |
|   2025    |        1094         |         The Silver Covenant         |          90           |
|   2026    |        1094         |         The Silver Covenant         |          90           |
|   2027    |        1094         |         The Silver Covenant         |          90           |
|   2028    |         148         |               Ambient               | 无法获得声望 |
|   2029    |         973         |          Monster, Predator          | 无法获得声望 |
|   2030    |         973         |          Monster, Predator          | 无法获得声望 |
|   2031    |         66          |            Horde Generic            | 无法获得声望 |
|   2032    |        1095         |        Grizzly Hills Trapper        | 无法获得声望 |
|   2033    |         14          |               Monster               | 无法获得声望 |
|   2034    |        1085         |          Warsong Offensive          |          81           |
|   2035    |         20          |           Undead, Scourge           | 无法获得声望 |
|   2036    |         31          |              Friendly               | 无法获得声望 |
|   2037    |        1050         |         Valiance Expedition         |          74           |
|   2038    |         148         |               Ambient               | 无法获得声望 |
|   2039    |         14          |               Monster               | 无法获得声望 |
|   2040    |        1050         |         Valiance Expedition         |          74           |
|   2041    |        1091         |         The Wyrmrest Accord         |          83           |
|   2042    |         20          |           Undead, Scourge           | 无法获得声望 |
|   2043    |         20          |           Undead, Scourge           | 无法获得声望 |
|   2044    |        1050         |         Valiance Expedition         |          74           |
|   2045    |        1085         |          Warsong Offensive          |          81           |
|   2046    |         40          |              Escortee               | 无法获得声望 |
|   2047    |        1073         |            The Kalu\'ak             |          79           |
|   2048    |         928         |          Scourge Invaders           | 无法获得声望 |
|   2049    |         928         |          Scourge Invaders           | 无法获得声望 |
|   2050    |        1098         |      Knights of the Ebon Blade      |          91           |
|   2051    |        1098         |      Knights of the Ebon Blade      |          91           |
|   2052    |        1099         |          Wrathgate Scourge          | 无法获得声望 |
|   2053    |        1100         |         Wrathgate Alliance          | 无法获得声望 |
|   2054    |        1101         |           Wrathgate Horde           | 无法获得声望 |
|   2055    |         965         |            Monster Spar             | 无法获得声望 |
|   2056    |         966         |         Monster Spar Buddy          | 无法获得声望 |
|   2057    |        1066         |   Monster, Zone Force Reaction 2    | 无法获得声望 |
|   2058    |        1102         |         CTF - Flag - Horde          | 无法获得声望 |
|   2059    |        1103         |        CTF - Flag - Neutral         | 无法获得声望 |
|   2060    |        1104         |          Frenzyheart Tribe          |          92           |
|   2061    |        1104         |          Frenzyheart Tribe          |          92           |
|   2062    |        1104         |          Frenzyheart Tribe          |          92           |
|   2063    |        1105         |             The Oracles             |          93           |
|   2064    |        1105         |             The Oracles             |          93           |
|   2065    |        1105         |             The Oracles             |          93           |
|   2066    |        1105         |             The Oracles             |          93           |
|   2067    |        1091         |         The Wyrmrest Accord         |          83           |
|   2068    |         20          |           Undead, Scourge           | 无法获得声望 |
|   2069    |        1107         |           Troll, Drakkari           | 无法获得声望 |
|   2070    |        1106         |           Argent Crusade            |          94           |
|   2071    |        1106         |           Argent Crusade            |          94           |
|   2072    |        1106         |           Argent Crusade            |          94           |
|   2073    |        1106         |           Argent Crusade            |          94           |
|   2074    |         986         |     Caverns of Time - Durnholde     | 无法获得声望 |
|   2075    |        1110         |             CoT Scourge             | 无法获得声望 |
|   2076    |        1108         |             CoT Arthas              | 无法获得声望 |
|   2077    |        1108         |             CoT Arthas              | 无法获得声望 |
|   2078    |        1109         |       CoT Stratholme Citizen        | 无法获得声望 |
|   2079    |        1108         |             CoT Arthas              | 无法获得声望 |
|   2080    |         20          |           Undead, Scourge           | 无法获得声望 |
|   2081    |        1111         |                Freya                | 无法获得声望 |
|   2082    |         20          |           Undead, Scourge           | 无法获得声望 |
|   2083    |         20          |           Undead, Scourge           | 无法获得声望 |
|   2084    |         20          |           Undead, Scourge           | 无法获得声望 |
|   2085    |         20          |           Undead, Scourge           | 无法获得声望 |
|   2086    |         529         |             Argent Dawn             |          13           |
|   2087    |         529         |             Argent Dawn             |          13           |
|   2088    |         960         |             Actor Evil              | 无法获得声望 |
|   2089    |         56          |           Scarlet Crusade           | 无法获得声望 |
|   2090    |        1112         |       Mount - Taxi - Alliance       | 无法获得声望 |
|   2091    |        1113         |        Mount - Taxi - Horde         | 无法获得声望 |
|   2092    |        1114         |       Mount - Taxi - Neutral        | 无法获得声望 |
|   2093    |         20          |           Undead, Scourge           | 无法获得声望 |
|   2094    |         20          |           Undead, Scourge           | 无法获得声望 |
|   2095    |         56          |           Scarlet Crusade           | 无法获得声望 |
|   2096    |         56          |           Scarlet Crusade           | 无法获得声望 |
|   2097    |         20          |           Undead, Scourge           | 无法获得声望 |
|   2098    |        1116         |           Elemental, Air            | 无法获得声望 |
|   2099    |        1115         |          Elemental, Water           | 无法获得声望 |
|   2100    |         20          |           Undead, Scourge           | 无法获得声望 |
|   2101    |         960         |             Actor Evil              | 无法获得声望 |
|   2102    |         960         |             Actor Evil              | 无法获得声望 |
|   2103    |         56          |           Scarlet Crusade           | 无法获得声望 |
|   2104    |         965         |            Monster Spar             | 无法获得声望 |
|   2105    |         966         |         Monster Spar Buddy          | 无法获得声望 |
|   2106    |         148         |               Ambient               | 无法获得声望 |
|   2107    |        1119         |          The Sons of Hodir          |          97           |
|   2108    |        1120         |             Iron Giants             | 无法获得声望 |
|   2109    |        1121         |            Frost Vrykul             | 无法获得声望 |
|   2110    |         31          |              Friendly               | 无法获得声望 |
|   2111    |         14          |               Monster               | 无法获得声望 |
|   2112    |        1119         |          The Sons of Hodir          |          97           |
|   2113    |        1121         |            Frost Vrykul             | 无法获得声望 |
|   2114    |        1045         |               Vrykul                | 无法获得声望 |
|   2115    |         959         |             Actor Good              | 无法获得声望 |
|   2116    |        1045         |               Vrykul                | 无法获得声望 |
|   2117    |         959         |             Actor Good              | 无法获得声望 |
|   2118    |        1122         |               Earthen               | 无法获得声望 |
|   2119    |        1123         |           Monster Referee           | 无法获得声望 |
|   2120    |        1123         |           Monster Referee           | 无法获得声望 |
|   2121    |        1124         |           The Sunreavers            |          98           |
|   2122    |        1124         |           The Sunreavers            |          98           |
|   2123    |        1124         |           The Sunreavers            |          98           |
|   2124    |         14          |               Monster               | 无法获得声望 |
|   2125    |        1121         |            Frost Vrykul             | 无法获得声望 |
|   2126    |        1121         |            Frost Vrykul             | 无法获得声望 |
|   2127    |         148         |               Ambient               | 无法获得声望 |
|   2128    |        1125         |              Hyldsmeet              | 无法获得声望 |
|   2129    |        1124         |           The Sunreavers            |          98           |
|   2130    |        1094         |         The Silver Covenant         |          90           |
|   2131    |        1106         |           Argent Crusade            |          94           |
|   2132    |        1085         |          Warsong Offensive          |          81           |
|   2133    |        1121         |            Frost Vrykul             | 无法获得声望 |
|   2134    |        1106         |           Argent Crusade            |          94           |
|   2135    |         31          |              Friendly               | 无法获得声望 |
|   2136    |         148         |               Ambient               | 无法获得声望 |
|   2137    |         31          |              Friendly               | 无法获得声望 |
|   2138    |        1106         |           Argent Crusade            |          94           |
|   2139    |         928         |          Scourge Invaders           | 无法获得声望 |
|   2140    |         31          |              Friendly               | 无法获得声望 |
|   2141    |         31          |              Friendly               | 无法获得声望 |
|   2142    |         469         |              Alliance               |          11           |
|   2143    |        1050         |         Valiance Expedition         |          74           |
|   2144    |        1098         |      Knights of the Ebon Blade      |          91           |
|   2145    |         928         |          Scourge Invaders           | 无法获得声望 |
|   2148    |        1073         |            The Kalu\'ak             |          79           |
|   2150    |         966         |         Monster Spar Buddy          | 无法获得声望 |
|   2155    |         47          |              Ironforge              |          20           |
|   2156    |         973         |          Monster, Predator          | 无法获得声望 |
|   2176    |         959         |             Actor Good              | 无法获得声望 |
|   2178    |         959         |             Actor Good              | 无法获得声望 |
|   2189    |        1145         |          Hates Everything           | 无法获得声望 |
|   2190    |        1145         |          Hates Everything           | 无法获得声望 |
|   2191    |        1145         |          Hates Everything           | 无法获得声望 |
|   2209    |         20          |           Undead, Scourge           | 无法获得声望 |
|   2210    |         911         |           Silvermoon City           |          55           |
|   2212    |         20          |           Undead, Scourge           | 无法获得声望 |
|   2214    |        1098         |      Knights of the Ebon Blade      |          91           |
|   2216    |        1156         |          The Ashen Verdict          |          104          |
|   2217    |        1156         |          The Ashen Verdict          |          104          |
|   2218    |        1156         |          The Ashen Verdict          |          104          |
|   2219    |        1156         |          The Ashen Verdict          |          104          |
|   2226    |        1098         |      Knights of the Ebon Blade      |          91           |
|   2230    |        1106         |           Argent Crusade            |          94           |
|   2235    |        1160         |        CTF - Flag - Horde 2         | 无法获得声望 |
|   2236    |        1159         |       CTF - Flag - Alliance 2       | 无法获得声望 |

# faction

[`Back-to:DBC`](dbc-index)

**The \`Faction.dbc\` table**

This DBC contains information on all of the base factions. These factions are unique and represent a faction with which a player can gain reputation.

**IMPORTANT:** These values are used for **ALL** tables **EXCEPT** the [creature_template](creature_template) and [gameobject_template_addon](gameobject_template_addon) tables.

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)

## Structure

| Column | Field               | Type                                          | Notes                                                                                                                                                                                                                                                                                                      |
| ------ | ------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1      | ID                  | Integer                                       |                                                                                                                                                                                                                                                                                                            |
| 2      | reputationIndex     | Integer                                       | Each faction that has gainable rep has a unique number. All factions that you can not gain rep with have -1.                                                                                                                                                                                               |
| 3      | reputationRaceMask  | BitMask                                       | &lt;.. Points to another Allied / AtWar ID                                                                                                                                                                                                                                                                 |
| 4      | reputationRaceMask  | BitMask                                       | .. Honor Hold has 1101,690 & Thrallmar 690,1101 for example. ..&gt;                                                                                                                                                                                                                                        |
| 5      | reputationRaceMask  | BitMask                                       | Only city factions have a value. Possible relationship to Modifiers and 17 (1 = Stormwind; 2 = Orgrimmar; 4 = Wildhammer Clan & Iron Forge; 8 = Darnassus; 16 = Undercity; 64 = Gnomeregan Exiles; 512 = Shattrath City Factions & Silvermoon City; 528 = Thunder Bluff & Darkspear Trolls; 1024 = Exodar) |
| 6      | reputationRaceMask  | BitMask                                       | Only Horde cities have a value. Possible relationship to Modifiers and 18 (16 = Silvermoon City; 32 = Thunder Bluff; 128 = Darkspear Trolls; 512 = Undercity; 528 = Orgrimmar)                                                                                                                             |
| 7      | reputationClassMask | BitMask                                       | (479 = Cenerion Circle; 1503 = Lower City, "Friendly, Hidden", Netherwing; Shatari Skyguards)                                                                                                                                                                                                              |
| 8      | reputationClassMask | BitMask                                       | (1024 = Cenerion Circle;)                                                                                                                                                                                                                                                                                  |
| 9      | reputationClassMask | BitMask                                       | Never set pre 3.\* but 0x80 on "Kirin Tor"                                                                                                                                                                                                                                                                 |
| 10     | reputationClassMask | BitMask                                       | Never set pre 3.\* but 0x80 on "Kirin Tor"                                                                                                                                                                                                                                                                 |
| 11     | reputationBase      | Integer\[4\]                                  | Based on 0 = Neutral                                                                                                                                                                                                                                                                                       |
| 15     | reputationFlags     | Integer\[4\]                                  |                                                                                                                                                                                                                                                                                                            |
| 19     | **parentFactionID** | iRefID                                        | Recursive. i.e. Undercity lists ID 67, which is Horde                                                                                                                                                                                                                                                      |
| 20     | parentFactionMod    | Float\[2\]                                    |                                                                                                                                                                                                                                                                                                            |
| 22     | parentFactionCap    | Integer\[2\]                                  |                                                                                                                                                                                                                                                                                                            |
| 24     | Name                | [Loc](Localization_lang)                      | Display name of the faction                                                                                                                                                                                                                                                                                |
| 41     | Description         | [Loc](https://wowdev.wiki/Localization "Loc") | Seen in the reputation-GUI on click.                                                                                                                                                                                                                                                                       |

### Flags

       FACTION_FLAG_NONE             = 0x00, // no faction flag
       FACTION_FLAG_VISIBLE          = 0x01, // makes visible in client (set or can be set at interaction with target of this faction)
       FACTION_FLAG_AT_WAR           = 0x02, // enable AtWar-button in client. player controlled (except opposition team always war state), Flag only set on initial creation
       FACTION_FLAG_HIDDEN           = 0x04, // hidden faction from reputation pane in client (player can gain reputation, but this update not sent to client)
       FACTION_FLAG_INVISIBLE_FORCED = 0x08, // always overwrite FACTION_FLAG_VISIBLE and hide faction in rep.list, used for hide opposite team factions
       FACTION_FLAG_PEACE_FORCED     = 0x10, // always overwrite FACTION_FLAG_AT_WAR, used for prevent war with own team factions
       FACTION_FLAG_INACTIVE         = 0x20, // player controlled, state stored in characters.data (CMSG_SET_FACTION_INACTIVE)
       FACTION_FLAG_RIVAL            = 0x40, // flag for the two competing outland factions
       FACTION_FLAG_SPECIAL          = 0x80 // horde and alliance home cities and their northrend allies have this flag

### Content

Note: When refering to a faction IDexample a creature's [faction](creature_template#faction) this refering to

When refering to a creature's [faction](creature_template#faction) we use the [ID](#id) value.

When refering to a reputation gain (example: `.modify reputation`) we use [Faction](#faction) value.

| [ID](#id) | [Faction](#faction) |            Faction Name             |   Reputation Index    |
| :-------: | :-----------------: | :---------------------------------: | :-------------------: |
|     1     |          1          |            PLAYER, Human            | Can't have reputation |
|     2     |          2          |             PLAYER, Orc             | Can't have reputation |
|     3     |          3          |            PLAYER, Dwarf            | Can't have reputation |
|     4     |          4          |          PLAYER, Night Elf          | Can't have reputation |
|     5     |          5          |           PLAYER, Undead            | Can't have reputation |
|     6     |          6          |           PLAYER, Tauren            | Can't have reputation |
|     7     |          7          |              Creature               | Can't have reputation |
|    10     |         40          |              Escortee               | Can't have reputation |
|    11     |         72          |              Stormwind              |          19           |
|    12     |         72          |              Stormwind              |          19           |
|    14     |         14          |               Monster               | Can't have reputation |
|    15     |          7          |              Creature               | Can't have reputation |
|    16     |         14          |               Monster               | Can't have reputation |
|    17     |         15          |         Defias Brotherhood          | Can't have reputation |
|    18     |         19          |               Murloc                | Can't have reputation |
|    19     |         17          |          Gnoll - Redridge           | Can't have reputation |
|    20     |         16          |          Gnoll - Riverpaw           | Can't have reputation |
|    21     |         20          |           Undead, Scourge           | Can't have reputation |
|    22     |         22          |           Beast - Spider            | Can't have reputation |
|    23     |         54          |          Gnomeregan Exiles          |          18           |
|    24     |         24          |               Worgen                | Can't have reputation |
|    25     |         25          |               Kobold                | Can't have reputation |
|    26     |         25          |               Kobold                | Can't have reputation |
|    27     |         15          |         Defias Brotherhood          | Can't have reputation |
|    28     |         26          |          Troll, Bloodscalp          | Can't have reputation |
|    29     |         76          |              Orgrimmar              |          14           |
|    30     |         27          |        Troll, Skullsplitter         | Can't have reputation |
|    31     |         28          |                Prey                 | Can't have reputation |
|    32     |         29          |            Beast - Wolf             | Can't have reputation |
|    33     |         40          |              Escortee               | Can't have reputation |
|    34     |         15          |         Defias Brotherhood          | Can't have reputation |
|    35     |         31          |              Friendly               | Can't have reputation |
|    36     |         32          |                Trogg                | Can't have reputation |
|    37     |         33          |          Troll, Frostmane           | Can't have reputation |
|    38     |         29          |            Beast - Wolf             | Can't have reputation |
|    39     |         18          |         Gnoll - Shadowhide          | Can't have reputation |
|    40     |         34          |           Orc, Blackrock            | Can't have reputation |
|    41     |         35          |               Villian               | Can't have reputation |
|    42     |         36          |               Victim                | Can't have reputation |
|    43     |         35          |               Villian               | Can't have reputation |
|    44     |         37          |            Beast - Bear             | Can't have reputation |
|    45     |         38          |                Ogre                 | Can't have reputation |
|    46     |         39          |        Kurzen\'s Mercenaries        | Can't have reputation |
|    47     |         41          |           Venture Company           | Can't have reputation |
|    48     |         42          |           Beast - Raptor            | Can't have reputation |
|    49     |         43          |              Basilisk               | Can't have reputation |
|    50     |         44          |         Dragonflight, Green         | Can't have reputation |
|    51     |         45          |              Lost Ones              | Can't have reputation |
|    52     |         769         |          Gizlock\'s Dummy           | Can't have reputation |
|    53     |         49          |         Human, Night Watch          | Can't have reputation |
|    54     |         48          |          Dark Iron Dwarves          | Can't have reputation |
|    55     |         47          |              Ironforge              |          20           |
|    56     |         49          |         Human, Night Watch          | Can't have reputation |
|    57     |         47          |              Ironforge              |          20           |
|    58     |          7          |              Creature               | Can't have reputation |
|    59     |         32          |                Trogg                | Can't have reputation |
|    60     |         50          |          Dragonflight, Red          | Can't have reputation |
|    61     |         51          |          Gnoll - Mosshide           | Can't have reputation |
|    62     |         52          |           Orc, Dragonmaw            | Can't have reputation |
|    63     |         53          |            Gnome - Leper            | Can't have reputation |
|    64     |         54          |          Gnomeregan Exiles          |          18           |
|    65     |         76          |              Orgrimmar              |          14           |
|    66     |         55          |               Leopard               | Can't have reputation |
|    67     |         56          |           Scarlet Crusade           | Can't have reputation |
|    68     |         68          |              Undercity              |          17           |
|    69     |         470         |               Ratchet               |           9           |
|    70     |         57          |           Gnoll - Rothide           | Can't have reputation |
|    71     |         68          |              Undercity              |          17           |
|    72     |         58          |           Beast - Gorilla           | Can't have reputation |
|    73     |         669         |        Beast - Carrion Bird         | Can't have reputation |
|    74     |         60          |                Naga                 | Can't have reputation |
|    76     |         61          |               Dalaran               | Can't have reputation |
|    77     |         62          |           Forlorn Spirit            | Can't have reputation |
|    78     |         63          |              Darkhowl               | Can't have reputation |
|    79     |         69          |              Darnassus              |          21           |
|    80     |         69          |              Darnassus              |          21           |
|    81     |         64          |                Grell                | Can't have reputation |
|    82     |         65          |               Furbolg               | Can't have reputation |
|    83     |         66          |            Horde Generic            | Can't have reputation |
|    84     |         189         |          Alliance Generic           | Can't have reputation |
|    85     |         76          |              Orgrimmar              |          14           |
|    86     |         770         |          Gizlock\'s Charm           | Can't have reputation |
|    87     |         70          |              Syndicate              |           6           |
|    88     |         71          |          Hillsbrad Militia          | Can't have reputation |
|    89     |         56          |           Scarlet Crusade           | Can't have reputation |
|    90     |         73          |                Demon                | Can't have reputation |
|    91     |         74          |              Elemental              | Can't have reputation |
|    92     |         75          |               Spirit                | Can't have reputation |
|    93     |         14          |               Monster               | Can't have reputation |
|    94     |         77          |              Treasure               | Can't have reputation |
|    95     |         78          |          Gnoll - Mudsnout           | Can't have reputation |
|    96     |         79          |     HIllsbrad, Southshore Mayor     | Can't have reputation |
|    97     |         70          |              Syndicate              |           6           |
|    98     |         68          |              Undercity              |          17           |
|    99     |         36          |               Victim                | Can't have reputation |
|    100    |         77          |              Treasure               | Can't have reputation |
|    101    |         77          |              Treasure               | Can't have reputation |
|    102    |         77          |              Treasure               | Can't have reputation |
|    103    |         80          |         Dragonflight, Black         | Can't have reputation |
|    104    |         81          |            Thunder Bluff            |          16           |
|    105    |         81          |            Thunder Bluff            |          16           |
|    106    |         66          |            Horde Generic            | Can't have reputation |
|    107    |         33          |          Troll, Frostmane           | Can't have reputation |
|    108    |         70          |              Syndicate              |           6           |
|    109    |         110         |        Quilboar, Razormane 2        | Can't have reputation |
|    110    |         110         |        Quilboar, Razormane 2        | Can't have reputation |
|    111    |         85          |        Quilboar, Bristleback        | Can't have reputation |
|    112    |         85          |        Quilboar, Bristleback        | Can't have reputation |
|    113    |         40          |              Escortee               | Can't have reputation |
|    114    |         77          |              Treasure               | Can't have reputation |
|    115    |          8          |            PLAYER, Gnome            | Can't have reputation |
|    116    |          9          |            PLAYER, Troll            | Can't have reputation |
|    118    |         68          |              Undercity              |          17           |
|    119    |         87          |        Bloodsail Buccaneers         |           0           |
|    120    |         21          |              Booty Bay              |           1           |
|    121    |         21          |              Booty Bay              |           1           |
|    122    |         47          |              Ironforge              |          20           |
|    123    |         72          |              Stormwind              |          19           |
|    124    |         69          |              Darnassus              |          21           |
|    125    |         76          |              Orgrimmar              |          14           |
|    126    |         530         |          Darkspear Trolls           |          15           |
|    127    |         35          |               Villian               | Can't have reputation |
|    128    |         88          |             Blackfathom             | Can't have reputation |
|    129    |         89          |               Makrura               | Can't have reputation |
|    130    |         90          |           Centaur, Kolkar           | Can't have reputation |
|    131    |         91          |           Centaur, Galak            | Can't have reputation |
|    132    |         92          |         Gelkis Clan Centaur         |           2           |
|    133    |         93          |         Magram Clan Centaur         |           3           |
|    134    |         94          |              Maraudine              | Can't have reputation |
|    148    |         14          |               Monster               | Can't have reputation |
|    149    |         108         |              Theramore              | Can't have reputation |
|    150    |         108         |              Theramore              | Can't have reputation |
|    151    |         108         |              Theramore              | Can't have reputation |
|    152    |         109         |         Quilboar, Razorfen          | Can't have reputation |
|    153    |         109         |         Quilboar, Razorfen          | Can't have reputation |
|    154    |         111         |        Quilboar, Deathshead         | Can't have reputation |
|    168    |         128         |                Enemy                | Can't have reputation |
|    188    |         148         |               Ambient               | Can't have reputation |
|    189    |          7          |              Creature               | Can't have reputation |
|    190    |         148         |               Ambient               | Can't have reputation |
|    208    |         168         |         Nethergarde Caravan         | Can't have reputation |
|    209    |         168         |         Nethergarde Caravan         | Can't have reputation |
|    210    |         189         |          Alliance Generic           | Can't have reputation |
|    230    |         573         |        Southsea Freebooters         | Can't have reputation |
|    231    |         40          |              Escortee               | Can't have reputation |
|    232    |         40          |              Escortee               | Can't have reputation |
|    233    |         20          |           Undead, Scourge           | Can't have reputation |
|    250    |         40          |              Escortee               | Can't have reputation |
|    270    |         229         |           Wailing Caverns           | Can't have reputation |
|    290    |         40          |              Escortee               | Can't have reputation |
|    310    |         249         |              Silithid               | Can't have reputation |
|    311    |         249         |              Silithid               | Can't have reputation |
|    312    |         22          |           Beast - Spider            | Can't have reputation |
|    330    |         229         |           Wailing Caverns           | Can't have reputation |
|    350    |         88          |             Blackfathom             | Can't have reputation |
|    370    |         915         |          Armies of C\'Thun          | Can't have reputation |
|    371    |         269         |         Silvermoon Remnant          | Can't have reputation |
|    390    |         21          |              Booty Bay              |           1           |
|    410    |         43          |              Basilisk               | Can't have reputation |
|    411    |         310         |             Beast - Bat             | Can't have reputation |
|    412    |         510         |            The Defilers             |          52           |
|    413    |         309         |               Scorpid               | Can't have reputation |
|    414    |         576         |           Timbermaw Hold            |          35           |
|    415    |         311         |                Titan                | Can't have reputation |
|    416    |         311         |                Titan                | Can't have reputation |
|    430    |         329         |         Taskmaster Fizzule          | Can't have reputation |
|    450    |         229         |           Wailing Caverns           | Can't have reputation |
|    470    |         311         |                Titan                | Can't have reputation |
|    471    |         349         |             Ravenholdt              |           5           |
|    472    |         70          |              Syndicate              |           6           |
|    473    |         349         |             Ravenholdt              |           5           |
|    474    |         369         |              Gadgetzan              |           7           |
|    475    |         369         |              Gadgetzan              |           7           |
|    494    |         389         |           Gnomeregan Bug            | Can't have reputation |
|    495    |         40          |              Escortee               | Can't have reputation |
|    514    |         409         |                Harpy                | Can't have reputation |
|    534    |         189         |          Alliance Generic           | Can't have reputation |
|    554    |         429         |            Burning Blade            | Can't have reputation |
|    574    |         449         |         Shadowsilk Poacher          | Can't have reputation |
|    575    |         450         |           Searing Spider            | Can't have reputation |
|    594    |         32          |                Trogg                | Can't have reputation |
|    614    |         36          |               Victim                | Can't have reputation |
|    634    |         14          |               Monster               | Can't have reputation |
|    635    |         609         |           Cenarion Circle           |          36           |
|    636    |         576         |           Timbermaw Hold            |          35           |
|    637    |         470         |               Ratchet               |           9           |
|    654    |         82          |          Troll, Witherbark          | Can't have reputation |
|    655    |         90          |           Centaur, Kolkar           | Can't have reputation |
|    674    |         48          |          Dark Iron Dwarves          | Can't have reputation |
|    694    |         189         |          Alliance Generic           | Can't have reputation |
|    695    |         749         |        Hydraxian Waterlords         |          42           |
|    714    |         66          |            Horde Generic            | Can't have reputation |
|    734    |         48          |          Dark Iron Dwarves          | Can't have reputation |
|    735    |         489         |    Goblin, Dark Iron Bar Patron     | Can't have reputation |
|    736    |         489         |    Goblin, Dark Iron Bar Patron     | Can't have reputation |
|    754    |         48          |          Dark Iron Dwarves          | Can't have reputation |
|    774    |         40          |              Escortee               | Can't have reputation |
|    775    |         40          |              Escortee               | Can't have reputation |
|    776    |         910         |          Brood of Nozdormu          |          54           |
|    777    |         912         |          Might of Kalimdor          | Can't have reputation |
|    778    |         511         |                Giant                | Can't have reputation |
|    794    |         529         |             Argent Dawn             |          13           |
|    795    |         572         |          Troll, Vilebranch          | Can't have reputation |
|    814    |         529         |             Argent Dawn             |          13           |
|    834    |         74          |              Elemental              | Can't have reputation |
|    854    |         577         |              Everlook               |          28           |
|    855    |         577         |              Everlook               |          28           |
|    874    |         589         |        Wintersaber Trainers         |          27           |
|    875    |         54          |          Gnomeregan Exiles          |          18           |
|    876    |         530         |          Darkspear Trolls           |          15           |
|    877    |         530         |          Darkspear Trolls           |          15           |
|    894    |         108         |              Theramore              | Can't have reputation |
|    914    |         679         |           Training Dummy            | Can't have reputation |
|    934    |         575         |        Furbolg, Uncorrupted         | Can't have reputation |
|    954    |         73          |                Demon                | Can't have reputation |
|    974    |         20          |           Undead, Scourge           | Can't have reputation |
|    994    |         609         |           Cenarion Circle           |          36           |
|    995    |         81          |            Thunder Bluff            |          16           |
|    996    |         609         |           Cenarion Circle           |          36           |
|   1014    |         629         |         Shatterspear Trolls         | Can't have reputation |
|   1015    |         629         |         Shatterspear Trolls         | Can't have reputation |
|   1034    |         66          |            Horde Generic            | Can't have reputation |
|   1054    |         189         |          Alliance Generic           | Can't have reputation |
|   1055    |         189         |          Alliance Generic           | Can't have reputation |
|   1074    |         76          |              Orgrimmar              |          14           |
|   1075    |         108         |              Theramore              | Can't have reputation |
|   1076    |         69          |              Darnassus              |          21           |
|   1077    |         108         |              Theramore              | Can't have reputation |
|   1078    |         72          |              Stormwind              |          19           |
|   1080    |         31          |              Friendly               | Can't have reputation |
|   1081    |         74          |              Elemental              | Can't have reputation |
|   1094    |         23          |            Beast - Boar             | Can't have reputation |
|   1095    |         679         |           Training Dummy            | Can't have reputation |
|   1096    |         108         |              Theramore              | Can't have reputation |
|   1097    |         69          |              Darnassus              |          21           |
|   1114    |         689         |     Dragonflight, Black - Bait      | Can't have reputation |
|   1134    |         68          |              Undercity              |          17           |
|   1154    |         68          |              Undercity              |          17           |
|   1174    |         76          |              Orgrimmar              |          14           |
|   1194    |         709         |        Battleground Neutral         | Can't have reputation |
|   1214    |         729         |           Frostwolf Clan            |          41           |
|   1215    |         729         |           Frostwolf Clan            |          41           |
|   1216    |         730         |           Stormpike Guard           |          40           |
|   1217    |         730         |           Stormpike Guard           |          40           |
|   1234    |         750         |         Sulfuron Firelords          | Can't have reputation |
|   1235    |         750         |         Sulfuron Firelords          | Can't have reputation |
|   1236    |         750         |         Sulfuron Firelords          | Can't have reputation |
|   1254    |         609         |           Cenarion Circle           |          36           |
|   1274    |          7          |              Creature               | Can't have reputation |
|   1275    |          7          |              Creature               | Can't have reputation |
|   1294    |         771         |               Gizlock               | Can't have reputation |
|   1314    |         66          |            Horde Generic            | Can't have reputation |
|   1315    |         189         |          Alliance Generic           | Can't have reputation |
|   1334    |         730         |           Stormpike Guard           |          40           |
|   1335    |         729         |           Frostwolf Clan            |          41           |
|   1354    |         809         |            Shen\'dralar             |          44           |
|   1355    |         809         |            Shen\'dralar             |          44           |
|   1374    |         829         |      Ogre (Captain Kromcrush)       | Can't have reputation |
|   1375    |         77          |              Treasure               | Can't have reputation |
|   1394    |         80          |         Dragonflight, Black         | Can't have reputation |
|   1395    |         916         |         Silithid Attackers          | Can't have reputation |
|   1414    |         790         |       Spirit Guide - Alliance       | Can't have reputation |
|   1415    |         849         |        Spirit Guide - Horde         | Can't have reputation |
|   1434    |         869         |              Jaedenar               | Can't have reputation |
|   1454    |         36          |               Victim                | Can't have reputation |
|   1474    |         59          |         Thorium Brotherhood         |           4           |
|   1475    |         59          |         Thorium Brotherhood         |           4           |
|   1494    |         66          |            Horde Generic            | Can't have reputation |
|   1495    |         66          |            Horde Generic            | Can't have reputation |
|   1496    |         66          |            Horde Generic            | Can't have reputation |
|   1514    |         890         |        Silverwing Sentinels         |          45           |
|   1515    |         889         |          Warsong Outriders          |          46           |
|   1534    |         730         |           Stormpike Guard           |          40           |
|   1554    |         729         |           Frostwolf Clan            |          41           |
|   1555    |         909         |           Darkmoon Faire            |          50           |
|   1574    |         270         |           Zandalar Tribe            |          51           |
|   1575    |         72          |              Stormwind              |          19           |
|   1576    |         269         |         Silvermoon Remnant          | Can't have reputation |
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
|   1605    |         531         |        Dragonflight, Bronze         | Can't have reputation |
|   1606    |          7          |              Creature               | Can't have reputation |
|   1607    |          7          |              Creature               | Can't have reputation |
|   1608    |         609         |           Cenarion Circle           |          36           |
|   1610    |         914         |          PLAYER, Blood Elf          | Can't have reputation |
|   1611    |         47          |              Ironforge              |          20           |
|   1612    |         76          |              Orgrimmar              |          14           |
|   1613    |         912         |          Might of Kalimdor          | Can't have reputation |
|   1614    |         14          |               Monster               | Can't have reputation |
|   1615    |         169         |         Steamwheedle Cartel         |          10           |
|   1616    |         919         |             RC Objects              | Can't have reputation |
|   1617    |         918         |             RC Enemies              | Can't have reputation |
|   1618    |         47          |              Ironforge              |          20           |
|   1619    |         76          |              Orgrimmar              |          14           |
|   1620    |         128         |                Enemy                | Can't have reputation |
|   1621    |         921         |                Blue                 | Can't have reputation |
|   1622    |         920         |                 Red                 | Can't have reputation |
|   1623    |         922         |            Tranquillien             |          56           |
|   1624    |         529         |             Argent Dawn             |          13           |
|   1625    |         529         |             Argent Dawn             |          13           |
|   1626    |         20          |           Undead, Scourge           | Can't have reputation |
|   1627    |         923         |             Farstriders             | Can't have reputation |
|   1628    |         922         |            Tranquillien             |          56           |
|   1629    |         927         |           PLAYER, Draenei           | Can't have reputation |
|   1630    |         928         |          Scourge Invaders           | Can't have reputation |
|   1634    |         928         |          Scourge Invaders           | Can't have reputation |
|   1635    |         169         |         Steamwheedle Cartel         |          10           |
|   1636    |         923         |             Farstriders             | Can't have reputation |
|   1637    |         923         |             Farstriders             | Can't have reputation |
|   1638    |         930         |               Exodar                |          49           |
|   1639    |         930         |               Exodar                |          49           |
|   1640    |         930         |               Exodar                |          49           |
|   1641    |         889         |          Warsong Outriders          |          46           |
|   1642    |         890         |        Silverwing Sentinels         |          45           |
|   1643    |         937         |            Troll, Forest            | Can't have reputation |
|   1644    |         940         |         The Sons of Lothar          | Can't have reputation |
|   1645    |         940         |         The Sons of Lothar          | Can't have reputation |
|   1646    |         930         |               Exodar                |          49           |
|   1647    |         930         |               Exodar                |          49           |
|   1648    |         940         |         The Sons of Lothar          | Can't have reputation |
|   1649    |         940         |         The Sons of Lothar          | Can't have reputation |
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
|   1662    |         943         |               Fel Orc               | Can't have reputation |
|   1663    |         944         |            Fel Orc Ghost            | Can't have reputation |
|   1664    |         945         |        Sons of Lothar Ghosts        | Can't have reputation |
|   1666    |         946         |             Honor Hold              |          38           |
|   1667    |         946         |             Honor Hold              |          38           |
|   1668    |         947         |              Thrallmar              |          37           |
|   1669    |         947         |              Thrallmar              |          37           |
|   1670    |         947         |              Thrallmar              |          37           |
|   1671    |         946         |             Honor Hold              |          38           |
|   1672    |         949         |           Test Faction 1            |          85           |
|   1673    |         950         |            ToWoW - Flag             | Can't have reputation |
|   1674    |         953         |           Test Faction 4            | Can't have reputation |
|   1675    |         952         |           Test Faction 3            |          87           |
|   1676    |         954         |  ToWoW - Flag Trigger Horde (DND)   | Can't have reputation |
|   1677    |         951         | ToWoW - Flag Trigger Alliance (DND) | Can't have reputation |
|   1678    |         956         |              Ethereum               | Can't have reputation |
|   1679    |         955         |               Broken                | Can't have reputation |
|   1680    |         74          |              Elemental              | Can't have reputation |
|   1681    |         957         |           Earth Elemental           | Can't have reputation |
|   1682    |         958         |           Fighting Robots           | Can't have reputation |
|   1683    |         959         |             Actor Good              | Can't have reputation |
|   1684    |         960         |             Actor Evil              | Can't have reputation |
|   1685    |         961         |          Stillpine Furbolg          | Can't have reputation |
|   1686    |         961         |          Stillpine Furbolg          | Can't have reputation |
|   1687    |         962         |            Crazed Owlkin            | Can't have reputation |
|   1688    |         963         |           Chess Alliance            | Can't have reputation |
|   1689    |         964         |             Chess Horde             | Can't have reputation |
|   1690    |         963         |           Chess Alliance            | Can't have reputation |
|   1691    |         964         |             Chess Horde             | Can't have reputation |
|   1692    |         965         |            Monster Spar             | Can't have reputation |
|   1693    |         966         |         Monster Spar Buddy          | Can't have reputation |
|   1694    |         930         |               Exodar                |          49           |
|   1695    |         911         |           Silvermoon City           |          55           |
|   1696    |         967         |           The Violet Eye            |          63           |
|   1697    |         943         |               Fel Orc               | Can't have reputation |
|   1698    |         930         |               Exodar                |          49           |
|   1699    |         930         |               Exodar                |          49           |
|   1700    |         930         |               Exodar                |          49           |
|   1701    |         968         |              Sunhawks               | Can't have reputation |
|   1702    |         968         |              Sunhawks               | Can't have reputation |
|   1703    |         679         |           Training Dummy            | Can't have reputation |
|   1704    |         943         |               Fel Orc               | Can't have reputation |
|   1705    |         943         |               Fel Orc               | Can't have reputation |
|   1706    |         971         |            Fungal Giant             | Can't have reputation |
|   1707    |         970         |              Sporeggar              |          65           |
|   1708    |         970         |              Sporeggar              |          65           |
|   1709    |         970         |              Sporeggar              |          65           |
|   1710    |         942         |         Cenarion Expedition         |          64           |
|   1711    |         973         |          Monster, Predator          | Can't have reputation |
|   1712    |         974         |            Monster, Prey            | Can't have reputation |
|   1713    |         974         |            Monster, Prey            | Can't have reputation |
|   1714    |         968         |              Sunhawks               | Can't have reputation |
|   1715    |         975         |            Void Anomaly             | Can't have reputation |
|   1716    |         976         |           Hyjal Defenders           | Can't have reputation |
|   1717    |         976         |           Hyjal Defenders           | Can't have reputation |
|   1718    |         976         |           Hyjal Defenders           | Can't have reputation |
|   1719    |         976         |           Hyjal Defenders           | Can't have reputation |
|   1720    |         977         |           Hyjal Invaders            | Can't have reputation |
|   1721    |         978         |               Kurenai               |          66           |
|   1722    |         978         |               Kurenai               |          66           |
|   1723    |         978         |               Kurenai               |          66           |
|   1724    |         978         |               Kurenai               |          66           |
|   1725    |         979         |            Earthen Ring             | Can't have reputation |
|   1726    |         979         |            Earthen Ring             | Can't have reputation |
|   1727    |         979         |            Earthen Ring             | Can't have reputation |
|   1728    |         942         |         Cenarion Expedition         |          64           |
|   1729    |         947         |              Thrallmar              |          37           |
|   1730    |         933         |           The Consortium            |          60           |
|   1731    |         933         |           The Consortium            |          60           |
|   1732    |         189         |          Alliance Generic           | Can't have reputation |
|   1733    |         189         |          Alliance Generic           | Can't have reputation |
|   1734    |         66          |            Horde Generic            | Can't have reputation |
|   1735    |         66          |            Horde Generic            | Can't have reputation |
|   1736    |         966         |         Monster Spar Buddy          | Can't have reputation |
|   1737    |         946         |             Honor Hold              |          38           |
|   1738    |         981         |               Arakkoa               | Can't have reputation |
|   1739    |         982         |    Zangarmarsh Banner (Alliance)    | Can't have reputation |
|   1740    |         983         |     Zangarmarsh Banner (Horde)      | Can't have reputation |
|   1741    |         935         |            The Sha\'tar             |          39           |
|   1742    |         984         |    Zangarmarsh Banner (Neutral)     | Can't have reputation |
|   1743    |         932         |              The Aldor              |          58           |
|   1744    |         934         |             The Scryers             |          62           |
|   1745    |         911         |           Silvermoon City           |          55           |
|   1746    |         934         |             The Scryers             |          62           |
|   1747    |         985         |      Caverns of Time - Thrall       | Can't have reputation |
|   1748    |         986         |     Caverns of Time - Durnholde     | Can't have reputation |
|   1749    |         987         | Caverns of Time - Southshore Guards | Can't have reputation |
|   1750    |         988         |        Shadow Council Covert        | Can't have reputation |
|   1751    |         14          |               Monster               | Can't have reputation |
|   1752    |         993         |    Dark Portal Attacker, Legion     | Can't have reputation |
|   1753    |         993         |    Dark Portal Attacker, Legion     | Can't have reputation |
|   1754    |         993         |    Dark Portal Attacker, Legion     | Can't have reputation |
|   1755    |         991         |   Dark Portal Defender, Alliance    | Can't have reputation |
|   1756    |         991         |   Dark Portal Defender, Alliance    | Can't have reputation |
|   1757    |         991         |   Dark Portal Defender, Alliance    | Can't have reputation |
|   1758    |         992         |     Dark Portal Defender, Horde     | Can't have reputation |
|   1759    |         992         |     Dark Portal Defender, Horde     | Can't have reputation |
|   1760    |         992         |     Dark Portal Defender, Horde     | Can't have reputation |
|   1761    |         994         |           Inciter Trigger           | Can't have reputation |
|   1762    |         995         |          Inciter Trigger 2          | Can't have reputation |
|   1763    |         996         |          Inciter Trigger 3          | Can't have reputation |
|   1764    |         997         |          Inciter Trigger 4          | Can't have reputation |
|   1765    |         998         |          Inciter Trigger 5          | Can't have reputation |
|   1766    |         529         |             Argent Dawn             |          13           |
|   1767    |         529         |             Argent Dawn             |          13           |
|   1768    |         73          |                Demon                | Can't have reputation |
|   1769    |         73          |                Demon                | Can't have reputation |
|   1770    |         959         |             Actor Good              | Can't have reputation |
|   1771    |         960         |             Actor Evil              | Can't have reputation |
|   1772    |         999         |            Mana Creature            | Can't have reputation |
|   1773    |        1000         |         Khadgar\'s Servant          | Can't have reputation |
|   1774    |         31          |              Friendly               | Can't have reputation |
|   1775    |         935         |            The Sha\'tar             |          39           |
|   1776    |         932         |              The Aldor              |          58           |
|   1777    |         932         |              The Aldor              |          58           |
|   1778    |         990         |       The Scale of the Sands        |          57           |
|   1779    |         989         |           Keepers of Time           |          67           |
|   1780    |        1001         |           Bladespire Clan           | Can't have reputation |
|   1781    |         929         |           Bloodmaul Clan            | Can't have reputation |
|   1782    |        1001         |           Bladespire Clan           | Can't have reputation |
|   1783    |         929         |           Bloodmaul Clan            | Can't have reputation |
|   1784    |        1001         |           Bladespire Clan           | Can't have reputation |
|   1785    |         929         |           Bloodmaul Clan            | Can't have reputation |
|   1786    |         73          |                Demon                | Can't have reputation |
|   1787    |         14          |               Monster               | Can't have reputation |
|   1788    |         933         |           The Consortium            |          60           |
|   1789    |         968         |              Sunhawks               | Can't have reputation |
|   1790    |        1001         |           Bladespire Clan           | Can't have reputation |
|   1791    |         929         |           Bloodmaul Clan            | Can't have reputation |
|   1792    |         943         |               Fel Orc               | Can't have reputation |
|   1793    |         968         |              Sunhawks               | Can't have reputation |
|   1794    |        1003         |            Protectorate             | Can't have reputation |
|   1795    |        1003         |            Protectorate             | Can't have reputation |
|   1796    |         956         |              Ethereum               | Can't have reputation |
|   1797    |        1003         |            Protectorate             | Can't have reputation |
|   1798    |        1004         |      Arcane Annihilator (DNR)       | Can't have reputation |
|   1799    |        1002         |         Ethereum Sparbuddy          | Can't have reputation |
|   1800    |         956         |              Ethereum               | Can't have reputation |
|   1801    |         67          |                Horde                |          12           |
|   1802    |         469         |              Alliance               |          11           |
|   1803    |         148         |               Ambient               | Can't have reputation |
|   1804    |         148         |               Ambient               | Can't have reputation |
|   1805    |         932         |              The Aldor              |          58           |
|   1806    |         31          |              Friendly               | Can't have reputation |
|   1807    |        1003         |            Protectorate             | Can't have reputation |
|   1808    |        1007         |        Kirin\'Var - Belmara         | Can't have reputation |
|   1809    |        1009         |        Kirin\'Var - Cohlien         | Can't have reputation |
|   1810    |        1006         |        Kirin\'Var - Dathric         | Can't have reputation |
|   1811    |        1008         |       Kirin\'Var - Luminrath        | Can't have reputation |
|   1812    |         31          |              Friendly               | Can't have reputation |
|   1813    |        1010         |         Servant of Illidan          | Can't have reputation |
|   1814    |         966         |         Monster Spar Buddy          | Can't have reputation |
|   1815    |         29          |            Beast - Wolf             | Can't have reputation |
|   1816    |         31          |              Friendly               | Can't have reputation |
|   1818    |        1011         |             Lower City              |          69           |
|   1819    |         189         |          Alliance Generic           | Can't have reputation |
|   1820    |        1012         |        Ashtongue Deathsworn         |          70           |
|   1821    |        1013         |       Spirits of Shadowmoon 1       | Can't have reputation |
|   1822    |        1014         |       Spirits of Shadowmoon 2       | Can't have reputation |
|   1823    |         956         |              Ethereum               | Can't have reputation |
|   1824    |        1015         |             Netherwing              |          71           |
|   1825    |         73          |                Demon                | Can't have reputation |
|   1826    |        1010         |         Servant of Illidan          | Can't have reputation |
|   1827    |        1016         |              Wyrmcult               | Can't have reputation |
|   1828    |        1017         |               Treant                | Can't have reputation |
|   1829    |        1018         |          Leotheras Demon I          | Can't have reputation |
|   1830    |        1019         |         Leotheras Demon II          | Can't have reputation |
|   1831    |        1020         |         Leotheras Demon III         | Can't have reputation |
|   1832    |        1021         |         Leotheras Demon IV          | Can't have reputation |
|   1833    |        1022         |          Leotheras Demon V          | Can't have reputation |
|   1834    |        1023         |               Azaloth               | Can't have reputation |
|   1835    |         66          |            Horde Generic            | Can't have reputation |
|   1836    |         933         |           The Consortium            |          60           |
|   1837    |         970         |              Sporeggar              |          65           |
|   1838    |         934         |             The Scryers             |          62           |
|   1839    |        1024         |             Rock Flayer             | Can't have reputation |
|   1840    |        1025         |            Flayer Hunter            | Can't have reputation |
|   1841    |        1026         |          Shadowmoon Shade           | Can't have reputation |
|   1842    |        1027         |         Legion Communicator         | Can't have reputation |
|   1843    |        1010         |         Servant of Illidan          | Can't have reputation |
|   1844    |         932         |              The Aldor              |          58           |
|   1845    |         934         |             The Scryers             |          62           |
|   1846    |        1028         |         Ravenswood Ancients         | Can't have reputation |
|   1847    |         965         |            Monster Spar             | Can't have reputation |
|   1848    |         966         |         Monster Spar Buddy          | Can't have reputation |
|   1849    |        1010         |         Servant of Illidan          | Can't have reputation |
|   1850    |        1015         |             Netherwing              |          71           |
|   1851    |        1011         |             Lower City              |          69           |
|   1852    |        1029         |    Chess, Friendly to All Chess     | Can't have reputation |
|   1853    |        1010         |         Servant of Illidan          | Can't have reputation |
|   1854    |         932         |              The Aldor              |          58           |
|   1855    |         934         |             The Scryers             |          62           |
|   1856    |        1031         |         Sha\'tari Skyguard          |          72           |
|   1857    |         31          |              Friendly               | Can't have reputation |
|   1858    |        1012         |        Ashtongue Deathsworn         |          70           |
|   1859    |        1033         |                Maiev                | Can't have reputation |
|   1860    |        1034         |       Skettis Shadowy Arakkoa       | Can't have reputation |
|   1862    |        1035         |           Skettis Arakkoa           | Can't have reputation |
|   1863    |         52          |           Orc, Dragonmaw            | Can't have reputation |
|   1864    |        1036         |           Dragonmaw Enemy           | Can't have reputation |
|   1865    |         52          |           Orc, Dragonmaw            | Can't have reputation |
|   1866    |        1012         |        Ashtongue Deathsworn         |          70           |
|   1867    |        1033         |                Maiev                | Can't have reputation |
|   1868    |         966         |         Monster Spar Buddy          | Can't have reputation |
|   1869    |         981         |               Arakkoa               | Can't have reputation |
|   1870    |        1031         |         Sha\'tari Skyguard          |          72           |
|   1871    |        1035         |           Skettis Arakkoa           | Can't have reputation |
|   1872    |        1038         |              Ogri\'la               |          73           |
|   1873    |        1024         |             Rock Flayer             | Can't have reputation |
|   1874    |        1038         |              Ogri\'la               |          73           |
|   1875    |         932         |              The Aldor              |          58           |
|   1876    |         934         |             The Scryers             |          62           |
|   1877    |         52          |           Orc, Dragonmaw            | Can't have reputation |
|   1878    |        1041         |               Frenzy                | Can't have reputation |
|   1879    |        1042         |           Skyguard Enemy            | Can't have reputation |
|   1880    |         52          |           Orc, Dragonmaw            | Can't have reputation |
|   1881    |        1035         |           Skettis Arakkoa           | Can't have reputation |
|   1882    |        1010         |         Servant of Illidan          | Can't have reputation |
|   1883    |        1044         |         Theramore Deserter          | Can't have reputation |
|   1884    |        1047         |               Tuskarr               | Can't have reputation |
|   1885    |        1045         |               Vrykul                | Can't have reputation |
|   1886    |          7          |              Creature               | Can't have reputation |
|   1887    |          7          |              Creature               | Can't have reputation |
|   1888    |        1046         |          Northsea Pirates           | Can't have reputation |
|   1889    |        1048         |               UNUSED                | Can't have reputation |
|   1890    |        1049         |            Troll, Amani             | Can't have reputation |
|   1891    |        1050         |         Valiance Expedition         |          74           |
|   1892    |        1050         |         Valiance Expedition         |          74           |
|   1893    |        1050         |         Valiance Expedition         |          74           |
|   1894    |        1045         |               Vrykul                | Can't have reputation |
|   1895    |        1045         |               Vrykul                | Can't have reputation |
|   1896    |         909         |           Darkmoon Faire            |          50           |
|   1897    |        1067         |        The Hand of Vengeance        |          77           |
|   1898    |        1050         |         Valiance Expedition         |          74           |
|   1899    |        1050         |         Valiance Expedition         |          74           |
|   1900    |        1067         |        The Hand of Vengeance        |          77           |
|   1901    |        1052         |          Horde Expedition           |          75           |
|   1902    |         960         |             Actor Evil              | Can't have reputation |
|   1904    |         960         |             Actor Evil              | Can't have reputation |
|   1905    |        1055         |          Tamed Plaguehound          | Can't have reputation |
|   1906    |        1054         |           Spotted Gryphon           | Can't have reputation |
|   1907    |         949         |           Test Faction 1            |          85           |
|   1908    |         949         |           Test Faction 1            |          85           |
|   1909    |         42          |           Beast - Raptor            | Can't have reputation |
|   1910    |        1056         |      Vrykul (Ancient Spirit 1)      | Can't have reputation |
|   1911    |        1057         |      Vrykul (Ancient Siprit 2)      | Can't have reputation |
|   1912    |        1058         |      Vrykul (Ancient Siprit 3)      | Can't have reputation |
|   1913    |        1059         |        CTF - Flag - Alliance        | Can't have reputation |
|   1914    |        1045         |               Vrykul                | Can't have reputation |
|   1915    |        1060         |                Test                 | Can't have reputation |
|   1916    |        1033         |                Maiev                | Can't have reputation |
|   1917    |          7          |              Creature               | Can't have reputation |
|   1918    |        1052         |          Horde Expedition           |          75           |
|   1919    |        1062         |          Vrykul Gladiator           | Can't have reputation |
|   1920    |        1063         |         Valgarde Combatant          | Can't have reputation |
|   1921    |        1064         |             The Taunka              |          76           |
|   1922    |        1064         |             The Taunka              |          76           |
|   1923    |        1064         |             The Taunka              |          76           |
|   1924    |        1065         |   Monster, Zone Force Reaction 1    | Can't have reputation |
|   1925    |         14          |               Monster               | Can't have reputation |
|   1926    |        1068         |         Explorers\' League          |          78           |
|   1927    |        1068         |         Explorers\' League          |          78           |
|   1928    |        1067         |        The Hand of Vengeance        |          77           |
|   1929    |        1067         |        The Hand of Vengeance        |          77           |
|   1930    |        1069         |       Ram Racing Powerup DND        | Can't have reputation |
|   1931    |        1070         |         Ram Racing Trap DND         | Can't have reputation |
|   1932    |         74          |              Elemental              | Can't have reputation |
|   1933    |         31          |              Friendly               | Can't have reputation |
|   1934    |         959         |             Actor Good              | Can't have reputation |
|   1935    |         959         |             Actor Good              | Can't have reputation |
|   1936    |        1071         |         Craig\'s Squirrels          | Can't have reputation |
|   1937    |        1071         |         Craig\'s Squirrels          | Can't have reputation |
|   1938    |        1071         |         Craig\'s Squirrels          | Can't have reputation |
|   1939    |        1071         |         Craig\'s Squirrels          | Can't have reputation |
|   1940    |        1071         |         Craig\'s Squirrels          | Can't have reputation |
|   1941    |        1071         |         Craig\'s Squirrels          | Can't have reputation |
|   1942    |        1071         |         Craig\'s Squirrels          | Can't have reputation |
|   1943    |        1071         |         Craig\'s Squirrels          | Can't have reputation |
|   1944    |        1071         |         Craig\'s Squirrels          | Can't have reputation |
|   1945    |        1071         |         Craig\'s Squirrels          | Can't have reputation |
|   1947    |        1071         |         Craig\'s Squirrels          | Can't have reputation |
|   1948    |         921         |                Blue                 | Can't have reputation |
|   1949    |        1073         |            The Kalu\'ak             |          79           |
|   1950    |        1073         |            The Kalu\'ak             |          79           |
|   1951    |         69          |              Darnassus              |          21           |
|   1952    |        1074         |       Holiday - Water Barrel        | Can't have reputation |
|   1953    |         973         |          Monster, Predator          | Can't have reputation |
|   1954    |        1076         |            Iron Dwarves             | Can't have reputation |
|   1955    |        1076         |            Iron Dwarves             | Can't have reputation |
|   1956    |        1077         |       Shattered Sun Offensive       |          80           |
|   1957    |        1077         |       Shattered Sun Offensive       |          80           |
|   1958    |         960         |             Actor Evil              | Can't have reputation |
|   1959    |         960         |             Actor Evil              | Can't have reputation |
|   1960    |        1077         |       Shattered Sun Offensive       |          80           |
|   1961    |        1078         |         Fighting Vanity Pet         | Can't have reputation |
|   1962    |         20          |           Undead, Scourge           | Can't have reputation |
|   1963    |         73          |                Demon                | Can't have reputation |
|   1964    |         20          |           Undead, Scourge           | Can't have reputation |
|   1965    |         965         |            Monster Spar             | Can't have reputation |
|   1966    |         19          |               Murloc                | Can't have reputation |
|   1967    |        1077         |       Shattered Sun Offensive       |          80           |
|   1968    |        1079         |          Murloc, Winterfin          | Can't have reputation |
|   1969    |         19          |               Murloc                | Can't have reputation |
|   1970    |         14          |               Monster               | Can't have reputation |
|   1971    |        1080         |      Friendly, Force Reaction       | Can't have reputation |
|   1972    |        1081         |       Object, Force Reaction        | Can't have reputation |
|   1973    |        1050         |         Valiance Expedition         |          74           |
|   1974    |        1050         |         Valiance Expedition         |          74           |
|   1975    |         20          |           Undead, Scourge           | Can't have reputation |
|   1976    |        1050         |         Valiance Expedition         |          74           |
|   1977    |        1050         |         Valiance Expedition         |          74           |
|   1978    |        1085         |          Warsong Offensive          |          81           |
|   1979    |        1085         |          Warsong Offensive          |          81           |
|   1980    |        1085         |          Warsong Offensive          |          81           |
|   1981    |        1085         |          Warsong Offensive          |          81           |
|   1982    |         20          |           Undead, Scourge           | Can't have reputation |
|   1983    |         965         |            Monster Spar             | Can't have reputation |
|   1984    |         966         |         Monster Spar Buddy          | Can't have reputation |
|   1985    |         14          |               Monster               | Can't have reputation |
|   1986    |         40          |              Escortee               | Can't have reputation |
|   1987    |         942         |         Cenarion Expedition         |          64           |
|   1988    |         20          |           Undead, Scourge           | Can't have reputation |
|   1989    |        1086         |               Poacher               | Can't have reputation |
|   1990    |         148         |               Ambient               | Can't have reputation |
|   1991    |         20          |           Undead, Scourge           | Can't have reputation |
|   1992    |         14          |               Monster               | Can't have reputation |
|   1993    |         965         |            Monster Spar             | Can't have reputation |
|   1994    |         966         |         Monster Spar Buddy          | Can't have reputation |
|   1995    |        1059         |        CTF - Flag - Alliance        | Can't have reputation |
|   1997    |        1059         |        CTF - Flag - Alliance        | Can't have reputation |
|   1998    |        1087         |           Holiday Monster           | Can't have reputation |
|   1999    |         974         |            Monster, Prey            | Can't have reputation |
|   2000    |         974         |            Monster, Prey            | Can't have reputation |
|   2001    |        1088         |          Furbolg, Redfang           | Can't have reputation |
|   2003    |        1089         |          Furbolg, Frostpaw          | Can't have reputation |
|   2004    |        1050         |         Valiance Expedition         |          74           |
|   2005    |         20          |           Undead, Scourge           | Can't have reputation |
|   2006    |        1090         |              Kirin Tor              |          84           |
|   2007    |        1090         |              Kirin Tor              |          84           |
|   2008    |        1090         |              Kirin Tor              |          84           |
|   2009    |        1090         |              Kirin Tor              |          84           |
|   2010    |        1091         |         The Wyrmrest Accord         |          83           |
|   2011    |        1091         |         The Wyrmrest Accord         |          83           |
|   2012    |        1091         |         The Wyrmrest Accord         |          83           |
|   2013    |        1091         |         The Wyrmrest Accord         |          83           |
|   2014    |        1092         |             Azjol-Nerub             | Can't have reputation |
|   2016    |        1092         |             Azjol-Nerub             | Can't have reputation |
|   2017    |        1092         |             Azjol-Nerub             | Can't have reputation |
|   2018    |         20          |           Undead, Scourge           | Can't have reputation |
|   2019    |        1064         |             The Taunka              |          76           |
|   2020    |        1085         |          Warsong Offensive          |          81           |
|   2021    |        1082         |                REUSE                |          82           |
|   2022    |         14          |               Monster               | Can't have reputation |
|   2023    |         928         |          Scourge Invaders           | Can't have reputation |
|   2024    |        1067         |        The Hand of Vengeance        |          77           |
|   2025    |        1094         |         The Silver Covenant         |          90           |
|   2026    |        1094         |         The Silver Covenant         |          90           |
|   2027    |        1094         |         The Silver Covenant         |          90           |
|   2028    |         148         |               Ambient               | Can't have reputation |
|   2029    |         973         |          Monster, Predator          | Can't have reputation |
|   2030    |         973         |          Monster, Predator          | Can't have reputation |
|   2031    |         66          |            Horde Generic            | Can't have reputation |
|   2032    |        1095         |        Grizzly Hills Trapper        | Can't have reputation |
|   2033    |         14          |               Monster               | Can't have reputation |
|   2034    |        1085         |          Warsong Offensive          |          81           |
|   2035    |         20          |           Undead, Scourge           | Can't have reputation |
|   2036    |         31          |              Friendly               | Can't have reputation |
|   2037    |        1050         |         Valiance Expedition         |          74           |
|   2038    |         148         |               Ambient               | Can't have reputation |
|   2039    |         14          |               Monster               | Can't have reputation |
|   2040    |        1050         |         Valiance Expedition         |          74           |
|   2041    |        1091         |         The Wyrmrest Accord         |          83           |
|   2042    |         20          |           Undead, Scourge           | Can't have reputation |
|   2043    |         20          |           Undead, Scourge           | Can't have reputation |
|   2044    |        1050         |         Valiance Expedition         |          74           |
|   2045    |        1085         |          Warsong Offensive          |          81           |
|   2046    |         40          |              Escortee               | Can't have reputation |
|   2047    |        1073         |            The Kalu\'ak             |          79           |
|   2048    |         928         |          Scourge Invaders           | Can't have reputation |
|   2049    |         928         |          Scourge Invaders           | Can't have reputation |
|   2050    |        1098         |      Knights of the Ebon Blade      |          91           |
|   2051    |        1098         |      Knights of the Ebon Blade      |          91           |
|   2052    |        1099         |          Wrathgate Scourge          | Can't have reputation |
|   2053    |        1100         |         Wrathgate Alliance          | Can't have reputation |
|   2054    |        1101         |           Wrathgate Horde           | Can't have reputation |
|   2055    |         965         |            Monster Spar             | Can't have reputation |
|   2056    |         966         |         Monster Spar Buddy          | Can't have reputation |
|   2057    |        1066         |   Monster, Zone Force Reaction 2    | Can't have reputation |
|   2058    |        1102         |         CTF - Flag - Horde          | Can't have reputation |
|   2059    |        1103         |        CTF - Flag - Neutral         | Can't have reputation |
|   2060    |        1104         |          Frenzyheart Tribe          |          92           |
|   2061    |        1104         |          Frenzyheart Tribe          |          92           |
|   2062    |        1104         |          Frenzyheart Tribe          |          92           |
|   2063    |        1105         |             The Oracles             |          93           |
|   2064    |        1105         |             The Oracles             |          93           |
|   2065    |        1105         |             The Oracles             |          93           |
|   2066    |        1105         |             The Oracles             |          93           |
|   2067    |        1091         |         The Wyrmrest Accord         |          83           |
|   2068    |         20          |           Undead, Scourge           | Can't have reputation |
|   2069    |        1107         |           Troll, Drakkari           | Can't have reputation |
|   2070    |        1106         |           Argent Crusade            |          94           |
|   2071    |        1106         |           Argent Crusade            |          94           |
|   2072    |        1106         |           Argent Crusade            |          94           |
|   2073    |        1106         |           Argent Crusade            |          94           |
|   2074    |         986         |     Caverns of Time - Durnholde     | Can't have reputation |
|   2075    |        1110         |             CoT Scourge             | Can't have reputation |
|   2076    |        1108         |             CoT Arthas              | Can't have reputation |
|   2077    |        1108         |             CoT Arthas              | Can't have reputation |
|   2078    |        1109         |       CoT Stratholme Citizen        | Can't have reputation |
|   2079    |        1108         |             CoT Arthas              | Can't have reputation |
|   2080    |         20          |           Undead, Scourge           | Can't have reputation |
|   2081    |        1111         |                Freya                | Can't have reputation |
|   2082    |         20          |           Undead, Scourge           | Can't have reputation |
|   2083    |         20          |           Undead, Scourge           | Can't have reputation |
|   2084    |         20          |           Undead, Scourge           | Can't have reputation |
|   2085    |         20          |           Undead, Scourge           | Can't have reputation |
|   2086    |         529         |             Argent Dawn             |          13           |
|   2087    |         529         |             Argent Dawn             |          13           |
|   2088    |         960         |             Actor Evil              | Can't have reputation |
|   2089    |         56          |           Scarlet Crusade           | Can't have reputation |
|   2090    |        1112         |       Mount - Taxi - Alliance       | Can't have reputation |
|   2091    |        1113         |        Mount - Taxi - Horde         | Can't have reputation |
|   2092    |        1114         |       Mount - Taxi - Neutral        | Can't have reputation |
|   2093    |         20          |           Undead, Scourge           | Can't have reputation |
|   2094    |         20          |           Undead, Scourge           | Can't have reputation |
|   2095    |         56          |           Scarlet Crusade           | Can't have reputation |
|   2096    |         56          |           Scarlet Crusade           | Can't have reputation |
|   2097    |         20          |           Undead, Scourge           | Can't have reputation |
|   2098    |        1116         |           Elemental, Air            | Can't have reputation |
|   2099    |        1115         |          Elemental, Water           | Can't have reputation |
|   2100    |         20          |           Undead, Scourge           | Can't have reputation |
|   2101    |         960         |             Actor Evil              | Can't have reputation |
|   2102    |         960         |             Actor Evil              | Can't have reputation |
|   2103    |         56          |           Scarlet Crusade           | Can't have reputation |
|   2104    |         965         |            Monster Spar             | Can't have reputation |
|   2105    |         966         |         Monster Spar Buddy          | Can't have reputation |
|   2106    |         148         |               Ambient               | Can't have reputation |
|   2107    |        1119         |          The Sons of Hodir          |          97           |
|   2108    |        1120         |             Iron Giants             | Can't have reputation |
|   2109    |        1121         |            Frost Vrykul             | Can't have reputation |
|   2110    |         31          |              Friendly               | Can't have reputation |
|   2111    |         14          |               Monster               | Can't have reputation |
|   2112    |        1119         |          The Sons of Hodir          |          97           |
|   2113    |        1121         |            Frost Vrykul             | Can't have reputation |
|   2114    |        1045         |               Vrykul                | Can't have reputation |
|   2115    |         959         |             Actor Good              | Can't have reputation |
|   2116    |        1045         |               Vrykul                | Can't have reputation |
|   2117    |         959         |             Actor Good              | Can't have reputation |
|   2118    |        1122         |               Earthen               | Can't have reputation |
|   2119    |        1123         |           Monster Referee           | Can't have reputation |
|   2120    |        1123         |           Monster Referee           | Can't have reputation |
|   2121    |        1124         |           The Sunreavers            |          98           |
|   2122    |        1124         |           The Sunreavers            |          98           |
|   2123    |        1124         |           The Sunreavers            |          98           |
|   2124    |         14          |               Monster               | Can't have reputation |
|   2125    |        1121         |            Frost Vrykul             | Can't have reputation |
|   2126    |        1121         |            Frost Vrykul             | Can't have reputation |
|   2127    |         148         |               Ambient               | Can't have reputation |
|   2128    |        1125         |              Hyldsmeet              | Can't have reputation |
|   2129    |        1124         |           The Sunreavers            |          98           |
|   2130    |        1094         |         The Silver Covenant         |          90           |
|   2131    |        1106         |           Argent Crusade            |          94           |
|   2132    |        1085         |          Warsong Offensive          |          81           |
|   2133    |        1121         |            Frost Vrykul             | Can't have reputation |
|   2134    |        1106         |           Argent Crusade            |          94           |
|   2135    |         31          |              Friendly               | Can't have reputation |
|   2136    |         148         |               Ambient               | Can't have reputation |
|   2137    |         31          |              Friendly               | Can't have reputation |
|   2138    |        1106         |           Argent Crusade            |          94           |
|   2139    |         928         |          Scourge Invaders           | Can't have reputation |
|   2140    |         31          |              Friendly               | Can't have reputation |
|   2141    |         31          |              Friendly               | Can't have reputation |
|   2142    |         469         |              Alliance               |          11           |
|   2143    |        1050         |         Valiance Expedition         |          74           |
|   2144    |        1098         |      Knights of the Ebon Blade      |          91           |
|   2145    |         928         |          Scourge Invaders           | Can't have reputation |
|   2148    |        1073         |            The Kalu\'ak             |          79           |
|   2150    |         966         |         Monster Spar Buddy          | Can't have reputation |
|   2155    |         47          |              Ironforge              |          20           |
|   2156    |         973         |          Monster, Predator          | Can't have reputation |
|   2176    |         959         |             Actor Good              | Can't have reputation |
|   2178    |         959         |             Actor Good              | Can't have reputation |
|   2189    |        1145         |          Hates Everything           | Can't have reputation |
|   2190    |        1145         |          Hates Everything           | Can't have reputation |
|   2191    |        1145         |          Hates Everything           | Can't have reputation |
|   2209    |         20          |           Undead, Scourge           | Can't have reputation |
|   2210    |         911         |           Silvermoon City           |          55           |
|   2212    |         20          |           Undead, Scourge           | Can't have reputation |
|   2214    |        1098         |      Knights of the Ebon Blade      |          91           |
|   2216    |        1156         |          The Ashen Verdict          |          104          |
|   2217    |        1156         |          The Ashen Verdict          |          104          |
|   2218    |        1156         |          The Ashen Verdict          |          104          |
|   2219    |        1156         |          The Ashen Verdict          |          104          |
|   2226    |        1098         |      Knights of the Ebon Blade      |          91           |
|   2230    |        1106         |           Argent Crusade            |          94           |
|   2235    |        1160         |        CTF - Flag - Horde 2         | Can't have reputation |
|   2236    |        1159         |       CTF - Flag - Alliance 2       | Can't have reputation |

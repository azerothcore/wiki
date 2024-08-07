﻿# worldstates

[<-Volver a:Characters](database-characters)

Leer en: [English :gb:](../worldstates) [Spanish :es:](worldstates)

**Tabla \`worldstates\`**

Esta tabla contiene datos que el Core necesita para manejar variables (como el temporizador para la descarga automática de puntos de arena).

**Estructura**

| Field        | Type          | Attributes | Key | Null | Default | Extra | Comment |
| -----------  | ------------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]   | INT           | UNSIGNED   | PRI | NO   | 0       |       |         |
| [value][2]   | INT           | UNSIGNED   |     | NO   | 0       |       |         |
| [comment][3] | TINYTEXT      | SIGNED     |     | YES  |         |       |         |

[1]: #entry
[2]: #value
[3]: #comment

**Descripción de los campos**

### entry

La entrada codificada relacionada con las variables debe ser guardada por el Core.
Por ejemplo, \`entry\` = 20001 es para que el temporizador descargue los puntos de la arena. Más ejemplos a continuación.

### value

Valor generado por el core con respecto a la entrada.

### comment

Comentario en formato de texto para que sea más fácil ver para qué es la entrada.

### id's conocidas de worldstate (entradas)

AV\_STORMPIKE\_LIEUTENANTS = 950, // $962w Stormpike Commander(s) and $950w Stormpike Lieutenant(s).  
AV\_STORMPIKE\_COMMANDERS = 962, // $962w Stormpike Commander(s) and $950w Stormpike Lieutenant(s).  
AV\_UNK\_01 = 964, // $964w, young $c.  
AV\_UNK\_02 = 966, // $966w, young $c.  


AV\_STONEHEART\_H\_C = 1301, //over ac  
AV\_STONEHEART\_A\_C = 1302, //Stoneheart Grave  
AV\_STONEHEART\_H\_A = 1303, //over aa  
AV\_STONEHEART\_A\_A = 1304, //over hc  
AV\_AID\_A\_C = 1325, //Stormpike first aid station  
AV\_AID\_A\_A = 1326,  
AV\_AID\_H\_C = 1327,  
AV\_AID\_H\_A = 1328,  
AV\_FROSTWOLFHUT\_A\_C = 1329, //over hc //Frostwolf Hut  
AV\_FROSTWOLFHUT\_H\_C = 1330,  
AV\_FROSTWOLFHUT\_A\_A = 1331, //over ha  
AV\_FROSTWOLFHUT\_H\_A = 1332, //over ac  
AV\_PIKEGRAVE\_A\_C = 1333, //Stormpike Graveyard  
AV\_PIKEGRAVE\_A\_A = 1,  
AV\_PIKEGRAVE\_H\_C = 1334,  
AV\_PIKEGRAVE\_H\_A = 1336,  
AV\_FROSTWOLF\_A\_C = 1337, //over hc //Frostwolf Grave  
AV\_FROSTWOLF\_H\_C = 1338,  
AV\_FROSTWOLF\_A\_A = 1339, //over ac  
AV\_FROSTWOLF\_H\_A = 1340, //over aa  
AV\_SNOWFALL\_A\_C = 1341, //over hc  
AV\_SNOWFALL\_H\_C = 1342,  
AV\_SNOWFALL\_A\_A = 1343, //over ha  
AV\_SNOWFALL\_H\_A = 1344, //over ac  
AV\_ICEBLOOD\_A\_C = 1346, //over hc //Horde //Iceblood grave  
AV\_ICEBLOOD\_A\_A = 1348, //over ac  
AV\_ICEBLOOD\_H\_C = 1347,  
AV\_ICEBLOOD\_H\_A = 1349, //over aa  
AV\_S\_MINE\_A = 1355,  
AV\_S\_MINE\_H = 1356,  
AV\_S\_MINE\_N = 1357,  
AV\_N\_MINE\_A = 1358,  
AV\_N\_MINE\_H = 1359,  
AV\_N\_MINE\_N = 1360, //mines  
AV\_DUNS\_CONTROLLED = 1361, //Alliance //Dunbaldar South Bunker  
AV\_DUNN\_CONTROLLED = 1362, //Dunbaldar North Bunker  
AV\_ICEWING\_CONTROLLED = 1363, //Stoneheart Bunker  
AV\_STONEH\_CONTROLLED = 1364,  
AV\_FROSTWOLFW\_DESTROYED = 1365, //over controlled  
AV\_FROSTWOLFE\_DESTROYED = 1366,  
AV\_TOWERPOINT\_DESTROYED = 1367, //goes over controlled  
AV\_ICEBLOOD\_DESTROYED = 1368,  
AV\_DUNS\_DESTROYED = 1370,  
AV\_DUNN\_DESTROYED = 1371,  
AV\_ICEWING\_DESTROYED = 1372,  
AV\_STONEH\_DESTROYED = 1373,  
AV\_DUNN\_UNUSED = 1374,  
AV\_DUNS\_UNUSED = 1375,  
AV\_ICEWING\_UNUSED = 1376,  
AV\_STONEH\_UNUSED = 1377,  
AV\_DUNS\_ASSAULTED = 1378,  
AV\_DUNN\_ASSAULTED = 1379,  
AV\_ICEWING\_ASSAULTED = 1380,  
AV\_STONEH\_ASSAULTED = 1381,  
AV\_FROSTWOLFW\_CONTROLLED = 1382,  
AV\_FROSTWOLFE\_CONTROLLED = 1383,  
AV\_TOWERPOINT\_CONTROLLED = 1384, //Tower Point  
AV\_ICEBLOOD\_CONTROLLED = 1385, //Horde //Iceblood Tower  
AV\_FROSTWOLFW\_ASSAULTED = 1387, //over destroyed  
AV\_FROSTWOLFE\_ASSAULTED = 1388,  
AV\_TOWERPOINT\_ASSAULTED = 1389, //goes over destroyed  
AV\_ICEBLOOD\_ASSAULTED = 1390,  
AV\_FROSTWOLFW\_UNUSED = 1392  
AV\_FROSTWOLFE\_UNUSED = 1393,  
AV\_TOWERPOINT\_UNUSED = 1394,  
AV\_ICEBLOOD\_UNUSED = 1395,


BG\_WS\_FLAG\_UNK\_ALLIANCE = 1545, // unk, set to 1 on alliance flag pickup... // ???  
BG\_WS\_FLAG\_UNK\_HORDE = 1546, // unk, set to 1 on horde flag pickup, after drop it's -1 // ???  
BG\_WS\_FLAG\_UNK\_01 = 1547, // unk // ???  
BG\_WS\_FLAG\_CAPTURES\_ALLIANCE = 1581, // alliance flag captures  
BG\_WS\_FLAG\_CAPTURES\_HORDE = 1582, // horde flag captures  
BG\_WS\_FLAG\_CAPTURES\_MAX = 1601, // unk (max flag captures?)


BG\_AB\_OP\_STABLE\_STATE\_ALIENCE = 1767, //Stable map state (ALIENCE)  
BG\_AB\_OP\_STABLE\_STATE\_HORDE = 1768, //Stable map state (HORDE)  
BG\_AB\_OP\_STABLE\_STATE\_CON\_ALI = 1769, //Stable map state (CON ALIENCE)  
BG\_AB\_OP\_STABLE\_STATE\_CON\_HOR = 1770, //Stable map state (CON HORDE)  
BG\_AB\_OP\_FARM\_STATE\_ALIENCE = 1772, //Farm state (ALIENCE)  
BG\_AB\_OP\_FARM\_STATE\_HORDE = 1773, //Farm state (HORDE)  
BG\_AB\_OP\_FARM\_STATE\_CON\_ALI = 1774, //Farm state (CON ALIENCE)  
BG\_AB\_OP\_FARM\_STATE\_CON\_HOR = 1775, //Farm state (CON HORDE)  
BG\_AB\_OP\_RESOURCES\_ALLY = 1776,  
BG\_AB\_OP\_RESOURCES\_HORDE = 1777,  
BG\_AB\_OP\_OCCUPIED\_BASES\_HORDE = 1778,  
BG\_AB\_OP\_OCCUPIED\_BASES\_ALLY = 1779,  
BG\_AB\_OP\_RESOURCES\_MAX = 1780,  
BG\_AB\_OP\_BLACKSMITH\_STATE\_ALIENCE = 1782, //Blacksmith map state (ALIENCE)  
BG\_AB\_OP\_BLACKSMITH\_STATE\_HORDE = 1783, //Blacksmith map state (HORDE)  
BG\_AB\_OP\_BLACKSMITH\_STATE\_CON\_ALI = 1784, //Blacksmith map state (CON ALIENCE)  
BG\_AB\_OP\_BLACKSMITH\_STATE\_CON\_HOR = 1785, //Blacksmith map state (CON HORDE)  
BG\_AB\_OP\_GOLDMINE\_STATE\_ALIENCE = 1787, //Gold Mine map state (ALIENCE)  
BG\_AB\_OP\_GOLDMINE\_STATE\_HORDE = 1788, //Gold Mine map state (HORDE)  
BG\_AB\_OP\_GOLDMINE\_STATE\_CON\_ALI = 1789, //Gold Mine map state (CON ALIENCE  
BG\_AB\_OP\_GOLDMINE\_STATE\_CON\_HOR = 1790, //Gold Mine map state (CON HORDE)  
BG\_AB\_OP\_LUMBERMILL\_STATE\_ALIENCE = 1792, //Lumber Mill map state (ALIENCE)  
BG\_AB\_OP\_LUMBERMILL\_STATE\_HORDE = 1793, //Lumber Mill map state (HORDE)  
BG\_AB\_OP\_LUMBERMILL\_STATE\_CON\_ALI = 1794, //Lumber Mill map state (CON ALIENCE)  
BG\_AB\_OP\_LUMBERMILL\_STATE\_CON\_HOR = 1795, //Lumber Mill map state (CON HORDE)


BG\_AB\_OP\_STABLE\_ICON = 1842, //Stable map icon (NONE)  
BG\_AB\_OP\_GOLDMINE\_ICON = 1843, //Gold Mine map icon (NONE)  
BG\_AB\_OP\_LUMBERMILL\_ICON = 1844, //Lumber Mill map icon (NONE)  
BG\_AB\_OP\_FARM\_ICON = 1845, //Farm map icon (NONE)  
BG\_AB\_OP\_BLACKSMITH\_ICON = 1846, //Blacksmith map icon (NONE)  
BG\_AB\_UNK\_01 = 1861, // default value 2 // ???


BG\_AB\_OP\_RESOURCES\_WARNING = 1955, // warning limit (1800)  
AV\_SNOWFALL\_N = 1966, //over aa //Neutral //Snowfall Grave


AQ\_WORLDSTATE\_ALLIANCE\_COPPERBAR\_CURRENT = 1997,  
AQ\_WORLDSTATE\_SHARED\_COPPERBAR\_REQUIRE = 1998,  
AQ\_WORLDSTATE\_ALLIANCE\_IRONBAR\_CURRENT = 2002,  
AQ\_WORLDSTATE\_ALLIANCE\_IRONBAR\_REQUIRE = 2003,  
AQ\_WORLDSTATE\_HORDE\_TINBAR\_CURRENT = 2005,  
AQ\_WORLDSTATE\_HORDE\_TINBAR\_REQUIRE = 2006,  
AQ\_WORLDSTATE\_HORDE\_MITHRILBAR\_CURRENT = 2008,  
AQ\_WORLDSTATE\_HORDE\_MITRHILBAR\_REQUIRE = 2009,  
AQ\_WORLDSTATE\_ALLIANCE\_THORIUMBAR\_CURRENT = 2011,  
AQ\_WORLDSTATE\_ALLIANCE\_THORIUMBAR\_REQUIRE = 2012,  
AQ\_WORLDSTATE\_HORDE\_COPPERBAR\_CURRENT = 2018,  
AQ\_WORLDSTATE\_HORDE\_PEACEBLOOM\_CURRENT = 2021, // Yes, these Peacebloom are intentionally out of order.  
AQ\_WORLDSTATE\_HORDE\_PEACEBLOOM\_REQUIRE = 2020,  
AQ\_WORLDSTATE\_ALLIANCE\_STRANGLEKELP\_CURRENT = 2047,  
AQ\_WORLDSTATE\_ALLIANCE\_STRANGLEKELP\_REQUIRE = 2048,  
AQ\_WORLDSTATE\_HORDE\_FIREBLOOM\_CURRENT = 2050,  
AQ\_WORLDSTATE\_HORDE\_FIREBLOOM\_REQUIRE = 2051,  
AQ\_WORLDSTATE\_ALLIANCE\_PURPLELOTUS\_CURRENT = 2053,  
AQ\_WORLDSTATE\_HORDE\_PURPLELOTUS\_CURRENT = 2054,  
AQ\_WORLDSTATE\_SHARED\_PURPLELOTUS\_REQUIRE = 2055,  
AQ\_WORLDSTATE\_ALLIANCE\_ARTHASTEAR\_CURRENT = 2057,  
AQ\_WORLDSTATE\_ALLIANCE\_ARTHASTEAR\_REQUIRE = 2058,  
AQ\_WORLDSTATE\_ALLIANCE\_LIGHTLEATHER\_CURRENT = 2060,  
AQ\_WORLDSTATE\_ALLIANCE\_LIGHTLEATHER\_REQUIRE = 2061,  
AQ\_WORLDSTATE\_ALLIANCE\_MEDIUMLEATHER\_CURRENT = 2063,  
AQ\_WORLDSTATE\_ALLIANCE\_MEDIUMLEATHER\_REQUIRE = 2064,  
AQ\_WORLDSTATE\_HORDE\_HEAVYLEATHER\_CURRENT = 2066,  
AQ\_WORLDSTATE\_HORDE\_HEAVYLEATHER\_REQUIRE = 2067,  
AQ\_WORLDSTATE\_ALLIANCE\_THICKLEATHER\_CURRENT = 2069,  
AQ\_WORLDSTATE\_HORDE\_THICKLEATHER\_CURRENT = 2070,  
AQ\_WORLDSTATE\_SHARED\_THICKLEATHER\_REQUIRE = 2071,  
AQ\_WORLDSTATE\_HORDE\_RUGGEDLEATHER\_CURRENT = 2073,  
AQ\_WORLDSTATE\_HORDE\_RUGGEDLEATHER\_REQUIRE = 2074,  
AQ\_WORLDSTATE\_ALLIANCE\_LINENBANDAGE\_CURRENT = 2076,  
AQ\_WORLDSTATE\_ALLIANCE\_LINENBANDAGE\_REQUIRE = 2077,  
AQ\_WORLDSTATE\_HORDE\_WOOLBANDAGE\_CURRENT = 2079,  
AQ\_WORLDSTATE\_HORDE\_WOOLBANDAGE\_REQUIRE = 2080,  
AQ\_WORLDSTATE\_ALLIANCE\_SILKBANDAGE\_CURRENT = 2082,  
AQ\_WORLDSTATE\_ALLIANCE\_SILKBANDAGE\_REQUIRE = 2083,  
AQ\_WORLDSTATE\_HORDE\_MAGEBANDAGE\_CURRENT = 2085,  
AQ\_WORLDSTATE\_HORDE\_MAGEBANDAGE\_REQUIRE = 2086,  
AQ\_WORLDSTATE\_ALLIANCE\_RUNEBANDAGE\_CURRENT = 2088,  
AQ\_WORLDSTATE\_HORDE\_RUNEBANDAGE\_CURRENT = 2089,  
AQ\_WORLDSTATE\_SHARED\_RUNEBANDAGE\_REQUIRE = 2090,  
AQ\_WORLDSTATE\_ALLIANCE\_RBOWALBA\_CURRENT = 2092,  
AQ\_WORLDSTATE\_ALLIANCE\_RBOWALBA\_REQUIRE = 2093,  
AQ\_WORLDSTATE\_HORDE\_LEANWOLF\_CURRENT = 2095,  
AQ\_WORLDSTATE\_HORDE\_LEANWOLF\_REQUIRE = 2096,  
AQ\_WORLDSTATE\_ALLIANCE\_ROASTRAPTOR\_CURRENT = 2098,  
AQ\_WORLDSTATE\_ALLIANCE\_ROASTRAPTOR\_REQUIRE = 2099,


AQ\_WORLDSTATE\_ALLIANCE\_SPOTYELLOW\_CURRENT = 2101,  
AQ\_WORLDSTATE\_HORDE\_SPOTYELLOW\_CURRENT = 2102,  
AQ\_WORLDSTATE\_SHARED\_SPOTYELLOW\_REQUIRE = 2103,  
AQ\_WORLDSTATE\_HORDE\_BAKEDSALMON\_CURRENT = 2105,  
AQ\_WORLDSTATE\_HORDE\_BAKEDSALMON\_REQUIRE = 2106,  
AQ\_WORLDSTATE\_TRANSITION\_DAYS\_REMAINING = 2113,  


EVENT\_LOVE\_VOTES\_THRALL = 2200, // Here are the final standings!$B$BThrall: $2200w$B$BCairne: $2201w$B$BSylvanas: $2202w$B$BTotal Horde: $2207w$B$B$BBolvar: $2203w$B$BMagni: $2204w$B$BTyrande: $2205w$B$BTotal Alliance: $2206w$B$BThe Horde and the Alliance tied in total votes!  
EVENT\_LOVE\_VOTES\_CAIRNE = 2201,  
EVENT\_LOVE\_VOTES\_SYLVANAS = 2202,  
EVENT\_LOVE\_VOTES\_VARIAN = 2203,  
EVENT\_LOVE\_VOTES\_MAGNI = 2204,  
EVENT\_LOVE\_VOTES\_TYRANDE = 2205,  
EVENT\_LOVE\_TOTAL\_ALLIANCE = 2206,  
EVENT\_LOVE\_TOTAL\_HORDE = 2207,


WORLDSTATE\_SI\_BATTLES\_WON = 2219, // We have won $2219W battles against the Scourge. Gird yourself, $n, for this war is far from over. & We have won $2219W battles against the Scourge. Take heart, $n. While many battles lie ahead, heroes, heroes from every realm have risen to fight them. & We have won $2219W battles against the Scourge. Stand firm, $n! We must persevere!  


SCOURGE\_EVENT\_WORLDSTATE\_WINTERSPRING = 2259, // 2259 - Icon on map  
SCOURGE\_EVENT\_WORLDSTATE\_AZSHARA = 2260, // 2260 - Icon on map  
SCOURGE\_EVENT\_WORLDSTATE\_BLASTED\_LANDS = 2261, // 2261 - Icon on map  
SCOURGE\_EVENT\_WORLDSTATE\_BURNING\_STEPPES = 2262, // 2262 - Icon on map  
SCOURGE\_EVENT\_WORLDSTATE\_TANARIS = 2263, // 2263 - Icon on map  
SCOURGE\_EVENT\_WORLDSTATE\_EASTERN\_PLAGUELANDS = 2264, // 2264 - Icon on map  


WORLDSTATE\_SI\_AZSHARA\_REMAINING = 2279, // The Scourge infestation grows in Azshara. Every able bodied warrior is needed to stem the tide of their invasion.$B$BNumber of Necropolises remaining: $2279W  
WORLDSTATE\_SI\_BLASTED\_LANDS\_REMAINING = 2280, // The Scourge infestation grows in the Blasted Lands. Every able bodied warrior is needed to stem the tide of their invasion.$B$BNumber of Necropolises remaining: $2280W  
WORLDSTATE\_SI\_BURNING\_STEPPES\_REMAINING = 2281, // If additional support is not soon sent to the Burning Steppes, I fear the Scourge will establish a base of operations there. If you can, you should go there to aid the defenders.$B$BNumber of Necropolises remaining: $2281W  
WORLDSTATE\_SI\_EASTERN\_PLAGUELANDS = 2282, // The Scourge infestation grows in the Eastern Plaguelands. Every able bodied warrior is needed to stem the tide of their invasion.$B$BNumber of Necropolises remaining: $2282W  
WORLDSTATE\_SI\_TANARIS = 2283, // It seems the army of the Scourge has come to Tanaris. A significant number of their necropolises and other forces have been dispatched there.$B$BNumber of Necropolises remaining: $2283W  
WORLDSTATE\_SI\_WINTERSPRING = 2284, // Indeed, the hills of Winterspring are currently attempting to withstand a renewed Scourge assault. Your assistance would help them greatly.$B$BNumber of Necropolises remaining: $2284W  
WORLDSTATE\_SI\_UNK = 2285, // saved world state is: $2285W // ???  


SI\_GATHERED\_A = 2313, // ally silityst gathered  
SI\_GATHERED\_H = 2314, // horde silityst gathered  
SI\_SILITHYST\_MAX = 2317, // max silithyst  


AQ\_SANDWORM\_N = 2322,
AQ\_SANDWORM\_S = 2323,  
AQ\_SANDWORM\_SW = 2324,  
AQ\_SANDWORM\_E = 2325,


EP\_UI\_TOWER\_COUNT\_A = 2327,  
EP\_UI\_TOWER\_COUNT\_H = 2328,  


BG\_WS\_FLAG\_STATE\_HORDE = 2338, // horde (0 - hide, 1 - flag ok, 2 - flag picked up (flashing), 3 - flag picked up (not flashing)  
BG\_WS\_FLAG\_STATE\_ALLIANCE = 2339, // alliance (0 - hide, 1 - flag ok, 2 - flag picked up (flashing), 3 - flag picked up (not flashing)  


EP\_NPT\_N = 2352, // default value 1  
EP\_PWT\_N\_H = 2353, // 2367 not present! use neutral!  
EP\_PWT\_N = 2353, // default value 1  
EP\_EWT\_A = 2354, // default value 0  
EP\_CGT\_N = 2355, // default value 1  
EP\_EWT\_H = 2356, // default value 0  
GENERAL\_WORLDSTATES\_06 = 2357, // default value 0 // ???  
GENERAL\_WORLDSTATES\_07 = 2358, // default value 0 // ???  
EP\_EWT\_N\_A = 2359, // ally conquested // default value 0  
EP\_EWT\_N\_H = 2360, // default value 0  
EP\_EWT\_N = 2361, // default value 1  
EP\_NPT\_N\_A = 2362, // default value 0  
GENERAL\_WORLDSTATES\_08 = 2363, // default value 0 // ???  
GENERAL\_WORLDSTATES\_09 = 2364, // default value 0 // ???  
GENERAL\_WORLDSTATES\_10 = 2365, // default value 0 // ???  
EP\_PWT\_N\_A = 2366, // default value 0  
GENERAL\_WORLDSTATES\_13 = 2367, // default value 1 // grey horde not in dbc! send for consistency's sake, and to match field count // ???  
GENERAL\_WORLDSTATES\_11 = 2368, // default value 0 // ???  
GENERAL\_WORLDSTATES\_12 = 2369, // default value 0 // ???  


EP\_PWT\_A = 2370, // default value 0  
EP\_PWT\_H = 2371, // default value 0  
EP\_NPT\_A = 2372, // default value 0  
EP\_NPT\_H = 2373, // default value 0  
EP\_CGT\_N\_A = 2374,  
EP\_CGT\_N\_H = 2375, // default value 0  
GENERAL\_WORLDSTATES\_04 = 2376, // default value 0 // ???  
GENERAL\_WORLDSTATES\_05 = 2377, // default value 0 // ???  
EP\_CGT\_A = 2378, // default value 0  
EP\_CGT\_H = 2379, // default value 0  


GENERAL\_WORLDSTATES\_01 = 2426, //SendInitWorldStates // 10 2426 // // default value 0 // ???  
GENERAL\_WORLDSTATES\_02 = 2427, // Progress: %2427w //SendInitWorldStates // 13 2427 // default value 50 // ???  
GENERAL\_WORLDSTATES\_03 = 2428, //SendInitWorldStates // 14 2428 // default value 50 // ???  


OHF\_INCENDIARY\_BOMBS\_SET = 2436, // Incendiary Bombs Set = %2436w/5 // Number of Incendiary Bombs Placed in Durnholde // <http://www.wowhead.com/quest=29598/tarethas-diversion>  
OHF\_INVADING ENEMIES = 2454, // Invading Enemies = %2454w  


HP\_UI\_TOWER\_COUNT\_A = 2476,  
HP\_UI\_TOWER\_COUNT\_H = 2478,  


HP\_UI\_SHOW\_ALLY\_OVERLOOK\_ICON = 2480, // default value 0  
HP\_UI\_SHOW\_THE\_OVERLOOK\_ARROW = 2481, // default value 1  
HP\_UI\_SHOW\_NEUTRAL\_OVERLOOK\_ICON = 2482, // default value 0  
HP\_UI\_ALLY\_BROKEN\_HILL\_ICON = 2483, // default value 0  
HP\_UI\_ABOVE\_BROKEN\_HILL\_ICON = 2484, // default value 1  
HP\_UI\_NEUTRAL\_BROKEN\_HILL\_ICON = 2485, // default value 0  


HP\_UI\_TOWER\_DISPLAY\_H = 2489,  
HP\_UI\_TOWER\_DISPLAY\_A = 2490,  
NA\_UI\_GUARDS\_LEFT = 2491,  
NA\_UI\_GUARDS\_MAX = 2493, // Outland // default value 0  
NA\_UI\_UNK\_1 = 2494, // default value 0 // ???  
NA\_UI\_OUTLAND\_01 = 2495, // Outland // default value 0 // Last Winner: Alliance // Controlled: %2476w InterfaceWorldStateFrameAllianceTower  
NA\_UI\_UNK\_2 = 2497, // default value 0 // ???  


NA\_UI\_ALLIANCE\_GUARDS\_SHOW = 2502,  
NA\_UI\_HORDE\_GUARDS\_SHOW = 2503,  


TF\_UI\_LOCKED\_DISPLAY\_NEUTRAL = 2508, // neutral locked time show  
TF\_UI\_LOCKED\_TIME\_HOURS = 2509, // locked time remaining minutes  
TF\_UI\_LOCKED\_TIME\_MINUTES\_SECOND\_DIGIT = 2510, // locked time remaining seconds second digit  
TF\_UI\_LOCKED\_TIME\_MINUTES\_FIRST\_DIGIT = 2512, // locked time remaining seconds first digit // default value 5  


ZM\_UNK\_3 = 2527, // default value 0 // ???  
ZM\_UNK\_2 = 2528, // default value 0 // ???  
ZM\_UNK\_1 = 2529, // default value 0 // ???  
ZM\_UNK\_6 = 2533, // default value 0 // ???  
ZM\_UNK\_5 = 2534, // default value 0 // ???  
ZM\_UNK\_4 = 2535, // default value 0 // ???  


COT\_OPENING\_THE\_DARK\_PORTAL\_MEDIVHS\_SHIELD\_REMANING = 2540, // Medivh's Shield Remaining: %2540w%  


BATTLEGROUND\_BLADES\_EDGE\_ARENA\_GOLD = 2547, // 7 gold  
BATTLEGROUND\_BLADES\_EDGE\_ARENA\_GREEN = 2547, // 8 green  
BATTLEGROUND\_BLADES\_EDGE\_ARENA\_SHOW = 2547, // 9 show // default value 1 // ???  


ZM\_UI\_TOWER\_WEST\_A = 2555,  
ZM\_UI\_TOWER\_WEST\_H = 2556,  
ZM\_UI\_TOWER\_WEST\_N = 2557,  
ZM\_UI\_TOWER\_EAST\_A = 2558,  
ZM\_UI\_TOWER\_EAST\_H = 2559,  
ZM\_UI\_TOWER\_EAST\_N = 2560,  


GENERAL\_WORLDSTATES\_14 = 2565,// 2565 unk, constant? // default value = 142  


BATTLEGROUND\_NAGRAND\_ARENA\_GOLD = 2575, // 7 gold // default value 0 // ???  
BATTLEGROUND\_NAGRAND\_ARENA\_GREEN = 2576, // 8 green // default value 0 // ???  
BATTLEGROUND\_NAGRAND\_ARENA\_SHOW = 2577, // 9 show // default value 1 // ???  


TF\_UI\_TOWERS\_CONTROLLED\_DISPLAY = 2620, // show towers controlled  
TF\_UI\_TOWER\_COUNT\_A = 2621, // ally towers controlled // default value 5  
TF\_UI\_TOWER\_COUNT\_H = 2622, // horde towers controlled  


TF\_UI\_SHOW CAPTURE BAR = 2623, // show capture bar  
TF\_UI\_CAPTURE\_BAR\_NEUTRAL = 2624, // capture bar pos  
TF\_UI\_CAPTURE\_BAR\_POS = 2625, // capture bar pos  


ZM\_MAP\_TOWER\_WEST\_A = 2644,  
ZM\_MAP\_TOWER\_WEST\_H = 2645,  
ZM\_MAP\_TOWER\_WEST\_N = 2646,  
ZM\_MAP\_GRAVEYARD\_N = 2647,  
ZM\_MAP\_GRAVEYARD\_A = 2648,  
ZM\_MAP\_GRAVEYARD\_H = 2649, // default value 1 // Twin spire graveyard horde 12?  
ZM\_MAP\_TOWER\_EAST\_A = 2650,  
ZM\_MAP\_TOWER\_EAST\_H = 2651,  
ZM\_MAP\_TOWER\_EAST\_N = 2652, // east beacon neutral  
ZM\_WORLDSTATE\_UNK\_1 = 2653, // default value 1  
ZM\_UNK\_7 = 2654, // ???  
ZM\_MAP\_ALLIANCE\_FLAG\_READY = 2655, // default value 0  
ZM\_MAP\_ALLIANCE\_FLAG\_NOT\_READY = 2656, // default value 1  
ZM\_MAP\_HORDE\_FLAG\_NOT\_READY = 2657, // default value 1  
ZM\_MAP\_HORDE\_FLAG\_READY = 2658,  
NA\_MAP\_WYVERN\_EAST\_NEU\_A = 2659,  
NA\_MAP\_WYVERN\_EAST\_H = 2660,  
NA\_MAP\_WYVERN\_EAST\_A = 2661,  
NA\_MAP\_WYVERN\_NORTH\_NEU\_A = 2662,  
NA\_MAP\_WYVERN\_NORTH\_H = 2663,  
NA\_MAP\_WYVERN\_NORTH\_A = 2664,  
NA\_MAP\_WYVERN\_WEST\_H = 2665,  
NA\_MAP\_WYVERN\_WEST\_A = 2666,  
NA\_MAP\_WYVERN\_WEST\_NEU\_A = 2667,  
NA\_MAP\_WYVERN\_SOUTH\_H = 2668,  
NA\_MAP\_WYVERN\_SOUTH\_A = 2669,  
NA\_MAP\_WYVERN\_SOUTH\_NEU\_A = 2670,  
NA\_MAP\_HALAA\_NEUTRAL = 2671,  
NA\_MAP\_HALAA\_HORDE = 2672,  
NA\_MAP\_HALAA\_ALLIANCE = 2673,  
NA\_MAP\_HALAA\_NEU\_A = 2676,  
NA\_MAP\_HALAA\_NEU\_H = 2677,  


TF\_TOWER\_NUM\_01 = 2681, // NW Neutral  
TF\_TOWER\_NUM\_02 = 2682, // NW Horde  
TF\_TOWER\_NUM\_03 = 2683, // NW Ally  
TF\_TOWER\_NUM\_04 = 2684, // N Ally  
TF\_TOWER\_NUM\_05 = 2685, // N Horde  
TF\_TOWER\_NUM\_06 = 2686, // N Neu  
TF\_TOWER\_NUM\_16 = 2687, // ???  
TF\_TOWER\_NUM\_07 = 2688, // NE Ally  
TF\_TOWER\_NUM\_08 = 2689, // NE Horde  
TF\_TOWER\_NUM\_09 = 2690, // NE Neu  
TF\_TOWER\_NUM\_10 = 2691, // S Ally  
TF\_TOWER\_NUM\_11 = 2692, // S Horde  
TF\_TOWER\_NUM\_12 = 2693, // S Neutral  
TF\_TOWER\_NUM\_13 = 2694, // SE Ally  
TF\_TOWER\_NUM\_14 = 2695, // SE Horde  
TF\_TOWER\_NUM\_15 = 2696,  


PROGRESS\_BAR\_SHOW = 2718, //1 init, 0 druhy send - bez messagu, 1 = controlled aliance  
PROGRESS\_BAR\_STATUS = 2719, //50 init!, 48 ... hordak bere .. 33 .. 0 = full 100% hordacky, 100 = full alliance  
PROGRESS\_BAR\_PERCENT\_GREY = 2720, //100 = empty (only grey), 0 = blue|red (no grey)  
BLOOD\_ELF\_UNCONTROL = 2722,  
BLOOD\_ELF\_ALLIANCE\_CONTROL = 2723,  
BLOOD\_ELF\_HORDE\_CONTROL = 2724,  
FEL\_REAVER\_UNCONTROL = 2725,  
FEL\_REAVER\_ALLIANCE\_CONTROL = 2726,  
FEL\_REAVER\_HORDE\_CONTROL = 2727,  
MAGE\_TOWER\_UNCONTROL = 2728,  
MAGE\_TOWER\_HORDE\_CONTROL = 2729,  
MAGE\_TOWER\_ALLIANCE\_CONTROL = 2730,  
DRAENEI\_RUINS\_UNCONTROL = 2731, // Draenei uncontrolled (1 - yes, 0 - no)  
DRAENEI\_RUINS\_ALLIANCE\_CONTROL = 2732, // Draenei - Alliance control  
DRAENEI\_RUINS\_HORDE\_CONTROL = 2733, // Draenei - Horde control  


EYE\_OF\_THE\_STORM\_BE\_TOWER\_CONFLICT = 2735, // default value 0 // "Blood Elf Tower",,,,,,,,,,,,,,,,0xFF01FE,"In Conflict",,,,,,,,,,,,,,,,0xFF01FE,2735,,  
EYE\_OF\_THE\_STORM\_BE\_TOWER\_CONFLICT2 = 2736, // default value 0 // "Blood Elf Tower",,,,,,,,,,,,,,,,0xFF01FE,"In Conflict",,,,,,,,,,,,,,,,0xFF01FE,2736,,  
EYE\_OF\_THE\_STORM\_03 = 2737, // default value 0 // Draenei - Horde conflict  
EYE\_OF\_THE\_STORM\_04 = 2738, // default value 0 // Draenei - Alliance conflict  
EYE\_OF\_THE\_STORM\_05 = 2739, // default value 0 // Fel Reaver - Alliance conflict  
EYE\_OF\_THE\_STORM\_06 = 2740, // default value 0 // Fel Reaver - Horde conflict  
EYE\_OF\_THE\_STORM\_07 = 2741, // default value 0 // Mage Tower - Alliance conflict  
EYE\_OF\_THE\_STORM\_08 = 2742, // default value 0 // Mage Tower - Horde conflict  


EY\_ALLIANCE\_RESOURCES = 2749,  
EY\_HORDE\_RESOURCES = 2750,  
EY\_ALLIANCE\_BASE = 2752, // Alliance Bases  
EY\_HORDE\_BASE = 2753, // Horde Bases  


NETHERSTORM\_FLAG = 2757, // Flag (1 - show, 0 - hide) - doesn't work exactly this way!  


NA\_MAP\_WYVERN\_SOUTH\_NEU\_H = 2760,  
NA\_MAP\_WYVERN\_WEST\_NEU\_H = 2761,  
NA\_MAP\_WYVERN\_NORTH\_NEU\_H = 2762,  
NA\_MAP\_WYVERN\_EAST\_NEU\_H = 2763,  


TF\_UI\_LOCKED\_DISPLAY\_ALLIANCE = 2767, // ally locked time show  
TF\_UI\_LOCKED\_DISPLAY\_HORDE = 2768, // horde locked time show  


NETHERSTORM\_FLAG\_STATE\_ALLIANCE = 2769, // //set to 2 when flag is picked up, and to 1 if it is dropped / Alliance top-stats (1 - show, 0 - hide) // 02 -&gt; alliance picked up the flag // default value 1  
NETHERSTORM\_FLAG\_STATE\_HORDE = 2770, // default value 1 // Horde top-stats (1 - show, 0 - hide) // 02 -&gt; horde picked up the flag  


COT\_OPENING\_THE\_DARK\_PORTAL\_TIME\_RIFTS\_OPENED = 2784, // Time Rifts Opened: %2784w/18  


BATTELGROUND\_RUINS\_OF\_LORDAERNON\_GOLD = 3000, // 7 gold // ???  
BATTELGROUND\_RUINS\_OF\_LORDAERNON\_GREEN = 3000, // 8 green // ???  
BATTELGROUND\_RUINS\_OF\_LORDAERNON\_SHOW = 3002, // 9 show // default value 1 // ???  


QUEST\_BREAK\_THE\_BLOCKADE\_MINUTES\_AWAY = 3078, // Our stolen zeppelin's less than $3078w minutes away. // Break the Blockade quest=11153  
EYE\_OF\_THE\_STORM\_09 = 3085, // default value 379 // ???  
QUEST\_BREAK\_THE\_BLOCKADE\_DWARFS\_ACTIVATED = 3094, // There are $3094W activated dwarves!  
QUEST\_BREAK\_THE\_BLOCKADE\_TOTAL\_INJURED = 3096, // We did it boys! Now back to the Grim Guzzler and we'll drink to the $3096W that were injuredl! // RETREAT!! We've already lost $3096W and we can't afford to lose any more!!  


BG\_AV\_Alliance\_Score = 3127,  
BG\_AV\_Horde\_Score = 3128,  
BG\_AV\_SHOW\_H\_SCORE = 3133,  
BG\_AV\_SHOW\_A\_SCORE = 3134,  


QUEST\_UNK\_01\_TOTAL\_CASUALTIES = 3151, // RETREAT!! We've taken a beating and had $3151W casualties! We can't keep taking these losses! FALL BACK!! // We did it boys! Now back to the Grim Guzzler and we'll drink to the $3151W that were injuredl!  


ARENA\_SEASON\_IN\_PROGRESS = 3191, // CONFIG\_ARENA\_SEASON\_IN\_PROGRESS // Arena season in progress, 0 - end of season //SendInitWorldStates  


QUEST\_DISCOVERING\_PERCENT\_RAZORTHORN\_ROOTS = 3223, // Good day to you, $c.$b$bThere's much to be done to assist in the effort here. Sadly, there's very little I can do for you until I get all of my supplies.$b$bI've now got $3223w percent of the razorthorn roots I need to get started. Any assistance you provide will be well worth the effort, I assure you. // The alchemy lab is not quite yet ready, $n. Mar'nah says that she is $3223w percent done with its assembly, however.$B$BIf you would   like to help her with that, you will find her inside the inn at the Sun's Reach Harbor. // quest=11522 <http://www.wowhead.com/quest=11520/discovering-your-roots>  
QUEST\_MAKING READY\_TOTAL\_GOAL = 3228, // <http://www.wowhead.com/npc=25046/smith-hauthaa> // Hello, $r.$b$bLet's get busy! No sense waiting around for supplies that may never arrive.$b$bI need my anvil in order to outfit our troops properly. Right now It's $3228w percent complete.$b$bAnd when the anvil is completed, there will be many more powerful items that I will be able to smith for you. // Last I heard from Hauthaa, she indicated that we are $3228w percent of the way there.$B$BI cannot   express how vital it is to our efforts that we get them created. Our men and women are going to need better armor and weapons, and the anvil and forge are the key to that.$B$BYou will find the smith behind the Sun's Reach Armory, $n.  
QUEST\_UNK\_02\_TOTAL\_GOAL = 3233, // My orders are to create a distraction at the Dead Scar so our forces can take the Sun's Reach Armory. It might not be as glamorous as killing demons face to face, but if it wins us this battle then I'm all for it.$B$BWe are $3233w percent done with our goal. // Capturing the Sun's Reach Sanctum was the first step in our battle plan. Our orders are to take control of the armory next.$B$BWe are $3233w percent done with our goal. // I am glad that you ask.   Our efforts to take the armory are at $3233w percent of our projections.$B$BI know that Battlemage Arynna and Harbinger Inuuro need your help. Seek them inside the Sun's Reach Sanctum on the Isle of Quel'Danas. // <http://www.wowhead.com/quest=11539/taking-the-harbor>  
QUEST\_UNK\_03\_TOTAL\_GOAL = 3238, // No, unfortunately we have not yet taken the harbor. However, reports indicate that we are $3238w percent of the way towards doing so.$B$B$n, if you want to help out, look for Magister Ilastar and Vindicator Kaalan at the Sun's Reach Armory on the Isle of Quel'Danas.  
QUEST\_FURTHER\_CONVERSIONS\_TOTAL\_GOAL = 3244, // Have you seen the damaged sentries that wander the island? A few modifications to the crystals that control their behavior will allow us to gain control of them and use them to secure tactical locations.$B$BThe Sun's Reach Sanctum will be ours in no time. We are $3244w percent done with this goal. // Arming the wards at the sanctum will help us secure it faster. We don't want any Wretched getting in our way when we unleash a full scale attack   on the Legion and Kael.$B$BWe are $3244w percent done with our goal. // <http://www.wowhead.com/quest=11525/further-conversions>  
QUEST\_UNK\_04\_GATE\_1\_TOTAL\_GOAL = 3255, // The first gate, Agamath, has been dismantled! The second gate of Rohendor now blocks our passage.$B$BOur mages are $3255w percent through the defenses of the second gate, Rohendor.  
QUEST\_UNK\_05\_GATE\_2\_TOTAL\_GOAL = 3257, // Rohendor has been obliterated. Only the gateway, Archonisus, remains.$B$BOur mages are $3257w percent through the defenses of the final gate, Archonisus.  
QUEST\_UNK\_02\_SUNWELL\_PORTAL\_PERCENT\_COMPLETED = 3269, // If we are to be successful in the creation of a portal to the Isle of Quel'Danas, and the Sunwell which rests upon it, we must acquire an energy source powerful enough to ignite the portal.$B$BWe are $3269w percent completed with our efforts. Will you assist us, $c?  
QUEST\_UNK\_06\_TOTAL\_GOAL = 3275, // I'm gathering funds to build a monument in honor of those who've died in the war. It is important to not forget the sacrifices we've made to achieve victory.$B$BWe are $3275w percent done with this goal.  


SUNS\_REACH\_ARMORY\_ENEMY = 3414, // 2098,0,0,0,0,0,0,0,0,0,0,0,12683.2001953,-6957.77978516,15.5542001724,530,516,4080,"Sun's Reach Armory",,,,,,,,,,,,,,,,0xFF01FE,"Held by the enemy",,,,,,,,,,,,,,,,0xFF01FE,3414,,  
SUNS\_REACH\_ARMORY\_SHATTERED\_SUN = 3415, // 2099,0,0,0,0,0,0,0,0,0,0,0,12683.2998047,-6957.79980469,15.5542001724,530,516,4080,"Sun's Reach Armory",,,,,,,,,,,,,,,,0xFF01FE,"Shattered Sun Offensive",,,,,,,,,,,,,,,,0xFF01FE,3415,,  
SUNS\_REACH\_HARBOR\_ENEMY = 3416, // 2100,0,0,0,0,0,0,0,0,0,0,0,12825.5996094,-7015.24023438,18.5926990509,530,516,4080,"Sun's Reach Harbor",,,,,,,,,,,,,,,,0xFF01FE,"Held by the enemy",,,,,,,,,,,,,,,,0xFF01FE,3416,,  
SUNS\_REACH\_HARBOR\_SHATTERED\_SUN = 3417, // 2101,0,0,0,0,0,0,0,0,0,0,0,12825.7001953,-7015.16992187,18.5926990509,530,516,4080,"Sun's Reach Harbor",,,,,,,,,,,,,,,,0xFF01FE,"Shattered Sun Offensive",,,,,,,,,,,,,,,,0xFF01FE,3417,,  
SUNS\_REACH\_SANCTUM\_ENEMY = 3418, // 2096,0,0,0,0,0,0,0,0,0,0,0,12787.2998047,-6885.54003906,13.3893995285,530,516,4080,"Sun's Reach Sanctum",,,,,,,,,,,,,,,,0xFF01FE,"Held by the enemy",,,,,,,,,,,,,,,,0xFF01FE,3418,,  
SUNS\_REACH\_SANCTUM\_SHATTERED\_SUN = 3419, // 2097,0,0,0,0,0,0,0,0,0,0,0,12787.4003906,-6885.60009766,13.3893995285,530,516,4080,"Sun's Reach Sanctum",,,,,,,,,,,,,,,,0xFF01FE,"Shattered Sun Offensive",,,,,,,,,,,,,,,,0xFF01FE,3419,,  


COT\_WORLDSTATE\_SHOW\_CRATES = 3479,  
COT\_WORLDSTATE\_CRATES\_REVEALED = 3480,  


OCULUS\_WORLD\_STATE\_CENTRIFUGE\_CONSTRUCT\_AMOUNT = 3486 // $3486W Centrifuge Constructs remain. We must find and destroy them to disable Varos Cloudstrider's protective shield. The constructs should be about halfway up The Oculus, on the Band of Acceleration.  


BATTLEFIELD\_WG\_WORLD\_STATE\_VEHICLE\_H = 3490,  
BATTLEFIELD\_WG\_WORLD\_STATE\_MAX\_VEHICLE\_H = 3491,  


COT\_WORLDSTATE\_WAVE\_COUNT = 3504,  


OCULUS\_WORLD\_STATE\_CENTRIFUGE\_CONSTRUCT\_SHOW = 3524,  


BG\_SA\_TIMER\_MINS = 3559,  
BG\_SA\_TIMER\_SEC\_TENS = 3560,  
BG\_SA\_TIMER\_SEC\_DECS = 3561,  
BG\_SA\_ENABLE\_TIMER = 3564,  
BG\_SA\_BONUS\_TIMER = 3571,  


// 2106,0,45,0,0,0,0,0,0,0,0,0,2279.16992188,1138.85998535,138.046005249,595,259,4100,"Elder's Square Gate",,,,,,,,,,,,,,,,0xFF01FE,"Elder's Square Gate",,,,,,,,,,,,,,,,0xFF01FE,3581,,  
// 2107,0,45,0,0,0,0,0,0,0,0,0,2184.2800293,1236.68994141,136.48399353,595,259,4100,"Festival Lane Gate",,,,,,,,,,,,,,,,0xFF01FE,"Festival Lane Gate",,,,,,,,,,,,,,,,0xFF01FE,3582,,  
// 2109,0,45,0,0,0,0,0,0,0,0,0,2122.57006836,1354.60998535,131.48399353,595,259,4100,"King's Square Fountain",,,,,,,,,,,,,,,,0xFF01FE,"King's Square Fountain",,,,,,,,,,,,,,,,0xFF01FE,3583,,  
// 2108,0,45,0,0,0,0,0,0,0,0,0,2225.75,1331.91003418,127.005996704,595,259,4100,"Market Row Gate",,,,,,,,,,,,,,,,0xFF01FE,"Market Row Gate",,,,,,,,,,,,,,,,0xFF01FE,3584,,  
// 2105,0,45,0,0,0,0,0,0,0,0,0,2355.43994141,1195.52001953,130.520996094,595,259,4100,"Town Hall",,,,,,,,,,,,,,,,0xFF01FE,"Town Hall",,,,,,,,,,,,,,,,0xFF01FE,3585,,  


ARENA\_WORLD\_STATE\_ALIVE\_PLAYERS\_GREEN = 3600,  
ARENA\_WORLD\_STATE\_ALIVE\_PLAYERS\_GOLD = 3601  
ARENA\_WORLD\_STATE\_ALIVE\_PLAYERS\_SHOW = 3610, // default value 1 // ???  
//BG\_RING\_OF\_VALOR\_WORLD\_STATE = 3610, // default value 1 // ???  


BG\_SA\_PURPLE\_GATEWS = 3614, // 2111,0,105,106,107,105,106,107,74,75,76,0,1216.32995605,79.1828994751,53.3525009155,607,647,4384,"Gate of the Purple Amethyst",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3614,,  
BG\_SA\_RED\_GATEWS = 3617, // 2114,0,77,78,79,77,78,79,74,75,76,0,1232.38000488,-210.044006348,55.118598938,607,935,4384,"Gate of the Red Sun",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3617,,  
BG\_SA\_BLUE\_GATEWS = 3620, // 2117,0,80,81,82,80,81,82,74,75,76,0,1433.06994629,-216.330993652,30.8668003082,607,959,4384,"Gate of the Blue Sapphire",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3620,,  
BG\_SA\_GREEN\_GATEWS = 3623, // 2120,0,108,109,110,108,109,110,74,75,76,0,1414.54003906,104.746002197,29.9468002319,607,959,4384,"Gate of the Green Emerald",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3623,,  
BG\_SA\_LEFT\_ATT\_TOKEN\_ALL = 3626, // 2123,0,46,0,0,0,0,0,0,0,0,0,1571.42004395,87.6970977783,4.29728984833,607,959,4384,"The Frostbreaker",,,,,,,,,,,,,,,,0xFF01FE,"Alliance Offense",,,,,,,,,,,,,,,,0xFF01FE,3626,,  
BG\_SA\_RIGHT\_ATT\_TOKEN\_ALL = 3627, // 2124,0,46,0,0,0,0,0,0,0,0,0,1570.41003418,-145.680999756,5.71539020538,607,959,4384,"The Graceful Maiden",,,,,,,,,,,,,,,,0xFF01FE,"Alliance Offense",,,,,,,,,,,,,,,,0xFF01FE,3627,,  
BG\_SA\_RIGHT\_ATT\_TOKEN\_HRD = 3628, // 2125,0,48,0,0,0,0,0,0,0,0,0,1571.33996582,-143.830001831,5.95772981644,607,959,4384,"The Blightbringer",,,,,,,,,,,,,,,,0xFF01FE,"Horde Offense",,,,,,,,,,,,,,,,0xFF01FE,3628,,  
BG\_SA\_LEFT\_ATT\_TOKEN\_HRD = 3629, // 2126,0,48,0,0,0,0,0,0,0,0,0,1571.31005859,87.2816009521,4.24728012085,607,959,4384,"The Casket Carrier",,,,,,,,,,,,,,,,0xFF01FE,"Horde Offense",,,,,,,,,,,,,,,,0xFF01FE,3629,,  
BG\_SA\_ALLIANCE\_DEFENCE\_TOKEN = 3630, // 2128,0,46,0,0,0,0,0,0,0,0,0,794.854003906,-108.88999939,499.253997803,607,959,4384,"Alliance Defense",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3630,,  
BG\_SA\_HORDE\_DEFENCE\_TOKEN = 3631, // 2127,0,48,0,0,0,0,0,0,0,0,0,794.828979492,-108.57800293,499.238006592,607,959,4384,"Horde Defense",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3631,,  
BG\_SA\_RIGHT\_GY\_HORDE = 3632, // 2129,0,13,0,0,0,0,0,0,0,0,0,1338.26000977,-155.26499939,31.7632007599,607,959,4384,"East Graveyard",,,,,,,,,,,,,,,,0xFF01FE,"Horde Controlled",,,,,,,,,,,,,,,,0xFF01FE,3632,,  
BG\_SA\_LEFT\_GY\_HORDE = 3633, // 2324,0,13,0,0,0,0,0,0,0,0,0,1309.0,8.65515995026,30.8957996368,607,959,4384,"West Graveyard",,,,,,,,,,,,,,,,0xFF01FE,"Horde Controlled",,,,,,,,,,,,,,,,0xFF01FE,3633,,  
BG\_SA\_CENTER\_GY\_HORDE = 3634, // 2133,0,13,0,0,0,0,0,0,0,0,0,1220.73999023,-70.5093994141,70.4493026733,607,959,4384,"South Graveyard",,,,,,,,,,,,,,,,0xFF01FE,"Horde Controlled",,,,,,,,,,,,,,,,0xFF01FE,3634,,  
BG\_SA\_LEFT\_GY\_ALLIANCE = 3635, // 2132,0,15,0,0,0,0,0,0,0,0,0,1308.59997559,8.67329025269,31.7639007568,607,959,4384,"West Graveyard",,,,,,,,,,,,,,,,0xFF01FE,"Alliance Controlled",,,,,,,,,,,,,,,,0xFF01FE,3635,,  
BG\_SA\_RIGHT\_GY\_ALLIANCE = 3636, // 2130,0,15,0,0,0,0,0,0,0,0,0,1338.91003418,-155.733001709,31.7633991241,607,959,4384,"East Graveyard",,,,,,,,,,,,,,,,0xFF01FE,"Alliance Controlled",,,,,,,,,,,,,,,,0xFF01FE,3636,,  
BG\_SA\_CENTER\_GY\_ALLIANCE = 3637, // 2134,0,15,0,0,0,0,0,0,0,0,0,1220.39001465,-70.6196975708,70.4493026733,607,959,4384,"South Graveyard",,,,,,,,,,,,,,,,0xFF01FE,"Alliance Controlled",,,,,,,,,,,,,,,,0xFF01FE,3637,,  
BG\_SA\_YELLOW\_GATEWS = 3638, // 2135,0,102,103,104,102,103,104,74,75,76,0,1058.7199707,-107.526000977,81.8201980591,607,959,4384,"Gate of the Yellow Moon",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3638,,  


CHRISTMAS\_EVENT\_MINUTES\_BEFORE\_CHRISTMAS = 3658, // Only $3658E shopping minutes before Christmas!  
CHRISTMAS\_EVENT\_MINUTES\_REMAINING = 3659, // Well then, there are only $3659E minutes left to party!  


BATTLEFIELD\_WG\_WORLD\_STATE\_VEHICLE\_A = 3680,  
BATTLEFIELD\_WG\_WORLD\_STATE\_MAX\_VEHICLE\_A = 3681,  


WORLDSTATE\_WORKSHOP\_K\_W = 3698, // 2150,0,65,66,67,68,69,70,71,72,73,0,5390.87988281,2979.47998047,442.290985107,571,903,4197,"Fortress Vehicle Workshop (W)",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3698,,  
WORLDSTATE\_WORKSHOP\_K\_E = 3699, // 2149,0,65,66,67,68,69,70,71,72,73,0,5389.97021484,2712.17993164,442.118011475,571,903,4197,"Fortress Vehicle Workshop (E)",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3699,,  
WORLDSTATE\_WORKSHOP\_NW = 3700,  
WORLDSTATE\_WORKSHOP\_NE = 3701, // 2265,0,8,8,8,13,13,13,15,15,15,0,5105.60986328,2300.67993164,368.484985352,571,903,4197,"Sunken Ring Graveyard",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3701,,  
// 2154,0,65,66,67,68,69,70,71,72,73,0,4942.81982422,2390.42993164,353.221008301,571,903,4197,"Sunken Ring Vehicle Workshop",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3701,,  
WORLDSTATE\_WORKSHOP\_SW = 3702, // 2269,0,8,8,8,13,13,13,15,15,15,0,4336.27978516,3234.62988281,390.25100708,571,903,4197,"Southwest Graveyard",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3702,,  
WORLDSTATE\_WORKSHOP\_SE = 3703, // 2151,0,65,66,67,68,69,70,71,72,73,0,4360.35009766,2352.27001953,409.367004395,571,903,4197,"Eastspark Vehicle Workshop",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3703,,  
// 2141,0,6,54,55,10,52,53,11,50,51,0,4556.97998047,3623.77001953,449.096984863,571,903,4197,"Shadowsight Tower",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3704,,  
// 2142,0,6,54,55,10,52,53,11,50,51,0,4397.97021484,2822.60009766,458.842010498,571,903,4197,"Winter's Edge Tower",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3705,,  
// 2143,0,6,54,55,10,52,53,11,50,51,0,4458.95019531,1944.13000488,488.205993652,571,903,4197,"Flamewatch Tower",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3706,,  


BATTLEFIELD\_WG\_WORLD\_STATE\_SHOW\_WORLDSTATE = 3710,  


// 2199,0,101,0,0,0,0,0,0,0,0,0,5048.52001953,2847.41992188,392.942993164,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3723,,  
// 2200,0,101,0,0,0,0,0,0,0,0,0,4484.43994141,2826.66992188,394.625,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3724,,  
// 2201,0,101,0,0,0,0,0,0,0,0,0,4763.66992188,2881.20996094,377.484008789,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3725,,  
// 2203,0,101,0,0,0,0,0,0,0,0,0,5052.91015625,3192.64990234,356.550994873,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3729,,  
// 2205,0,101,0,0,0,0,0,0,0,0,0,4812.10009766,3304.63989258,366.601989746,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3730,,  
// 2206,0,101,0,0,0,0,0,0,0,0,0,4730.25,2414.64990234,360.359985352,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3727,,  
// 2207,0,101,0,0,0,0,0,0,0,0,0,5018.89013672,2578.15991211,354.454986572,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3726,,  
// 2208,0,101,0,0,0,0,0,0,0,0,0,4493.02978516,3337.2800293,359.486999512,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3731,,  
// 2209,0,101,0,0,0,0,0,0,0,0,0,4497.72021484,2326.90991211,367.381988525,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3728,,  
// 2210,0,101,0,0,0,0,0,0,0,0,0,5010.87988281,2701.45996094,369.533996582,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3739,,  
// 2211,0,101,0,0,0,0,0,0,0,0,0,4821.56005859,2618.59008789,356.04598999,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3740,,  
// 2212,0,101,0,0,0,0,0,0,0,0,0,4450.37011719,2529.12011719,358.291992187,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3741,,  
// 2213,0,101,0,0,0,0,0,0,0,0,0,4516.68017578,2087.62011719,395.444000244,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3738,,  
// 2214,0,101,0,0,0,0,0,0,0,0,0,4774.62988281,2045.92004395,425.678009033,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3737,,  
// 2215,0,101,0,0,0,0,0,0,0,0,0,4402.91992188,3090.83007813,358.639007568,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3742,,  
// 2216,0,101,0,0,0,0,0,0,0,0,0,4789.56982422,3074.77001953,357.010009766,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3743,,  
// 2217,0,101,0,0,0,0,0,0,0,0,0,5046.72021484,3024.93994141,367.503997803,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3744,,  
// 2218,0,101,0,0,0,0,0,0,0,0,0,4400.10009766,3479.48999023,359.026000977,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3745,,  
// 2219,0,101,0,0,0,0,0,0,0,0,0,4558.39990234,3490.12988281,366.602996826,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3746,,  
// 2220,0,101,0,0,0,0,0,0,0,0,0,4837.70996094,3456.31005859,360.519012451,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3747,,  
// 2221,0,101,0,0,0,0,0,0,0,0,0,5085.95996094,3437.92993164,356.640014648,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3748,,  
// 2247,0,101,0,0,0,0,0,0,0,0,0,5217.20019531,2842.44995117,409.191009521,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3774,,  
// 2248,0,101,0,0,0,0,0,0,0,0,0,5214.83984375,3011.20996094,404.37701416,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3775,,  
// 2249,0,101,0,0,0,0,0,0,0,0,0,5213.37011719,2684.87988281,406.243011475,571,903,4253,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3776,,  
// 2250,0,101,0,0,0,0,0,0,0,0,0,5339.85009766,2700.89990234,409.165985107,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3777,,  
// 2251,0,101,0,0,0,0,0,0,0,0,0,5338.95019531,2841.38989258,409.239013672,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3778,,  
// 2252,0,101,0,0,0,0,0,0,0,0,0,5336.29003906,2978.42993164,409.191009521,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3779,,  
// 2253,0,101,0,0,0,0,0,0,0,0,0,4481.81982422,1993.33996582,431.45098877,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3794,,  
// 2254,0,101,0,0,0,0,0,0,0,0,0,4403.41992188,2349.10009766,375.57901001,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3791,,  
// 2255,0,101,0,0,0,0,0,0,0,0,0,4446.22021484,2820.73999023,402.838989258,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3795,,  
// 2256,0,101,0,0,0,0,0,0,0,0,0,4530.66015625,3584.57006836,396.104003906,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3793,,  
// 2257,0,101,0,0,0,0,0,0,0,0,0,4394.79003906,3294.73999023,372.428985596,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3792,,  
// 2258,0,101,0,0,0,0,0,0,0,0,0,4946.41992188,3331.66992188,376.881988525,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3788,,  
// 2259,0,101,0,0,0,0,0,0,0,0,0,4932.31005859,2440.4699707,320.175994873,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3790,,  
// 2260,0,101,0,0,0,0,0,0,0,0,0,4860.39990234,2023.32995605,396.597991943,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3797,,  
// 2261,0,101,0,0,0,0,0,0,0,0,0,4310.33007813,1810.35998535,348.632995605,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3798,,  
// 2262,0,101,0,0,0,0,0,0,0,0,0,4489.00976563,4028.88989258,411.912994385,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3799,,  
// 2263,0,101,0,0,0,0,0,0,0,0,0,4696.33007813,3806.98999023,362.268005371,571,903,4197,"PvP Activity Detected",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3796,,  


// 2246,0,74,75,76,77,78,79,80,81,82,0,5394.58007813,2841.48999023,418.914001465,571,903,4197,"Wintergrasp Fortress",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3773,,  
// 2229,0,74,75,76,77,78,79,80,81,82,0,5162.54003906,2841.25,438.039001465,571,1927,4197,"Wintergrasp Fortress Gate",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3763,,  
// 2146,0,6,54,55,10,52,53,11,50,51,0,5279.47021484,2632.11010742,462.265014648,571,903,4197,"Wintergrasp Fortress Tower (NE)",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3712,,  
// 2147,0,6,54,55,10,52,53,11,50,51,0,5280.06982422,3046.51000977,461.024993896,571,903,4197,"Wintergrasp Fortress Tower (NW)",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3711,,  
// 2145,0,6,54,55,10,52,53,11,50,51,0,5164.64013672,2747.97998047,462.356994629,571,903,4197,"Wintergrasp Fortress Tower (SE)",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3714,,  
// 2144,0,6,54,55,10,52,53,11,50,51,0,5161.25976563,2934.32006836,462.305999756,571,903,4197,"Wintergrasp Fortress Tower (SW)",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3713,,  
// 2222,0,92,93,94,95,96,97,98,99,100,0,5372.89013672,3047.30004883,431.065002441,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3749,,  
// 2223,0,92,93,94,95,96,97,98,99,100,0,5331.85009766,3046.55004883,431.403015137,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3750,,  
// 2224,0,83,84,85,86,87,88,89,90,91,0,5280.79980469,2995.92993164,432.302001953,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3751,,  
// 2225,0,83,84,85,86,87,88,89,90,91,0,5279.12988281,2954.81005859,432.095001221,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3752,,  
// 2226,0,92,93,94,95,96,97,98,99,100,0,5255.60009766,2934.08007813,432.835998535,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3753,,  
// 2227,0,92,93,94,95,96,97,98,99,100,0,5216.08007813,2933.98999023,432.678985596,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3754,,  
// 2228,0,83,84,85,86,87,88,89,90,91,0,5162.25,2882.84008789,433.731994629,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3755,,  
// 2230,0,83,84,85,86,87,88,89,90,91,0,5163.70996094,2798.7199707,432.717010498,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3756,,  
// 2231,0,92,93,94,95,96,97,98,99,100,0,5215.35986328,2747.98999023,432.666992188,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3757,,  
// 2232,0,92,93,94,95,96,97,98,99,100,0,5256.52001953,2747.55004883,433.229003906,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3758,,  
// 2233,0,83,84,85,86,87,88,89,90,91,0,5279.75976563,2725.12011719,433.42300415,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3759,,  
// 2234,0,83,84,85,86,87,88,89,90,91,0,5279.45019531,2683.90991211,433.322998047,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3760,,  
// 2235,0,92,93,94,95,96,97,98,99,100,0,5330.66015625,2630.68994141,432.759002686,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3761,,  
// 2236,0,92,93,94,95,96,97,98,99,100,0,5372.93017578,2630.77001953,431.928985596,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3762,,  
// 2237,0,92,93,94,95,96,97,98,99,100,0,5386.45996094,2909.88989258,433.194000244,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3764,,  
// 2238,0,92,93,94,95,96,97,98,99,100,0,5343.39013672,2909.18994141,432.778015137,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3765,,  
// 2239,0,92,93,94,95,96,97,98,99,100,0,5300.49023438,2909.33007813,433.359008789,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3766,,  
// 2240,0,83,84,85,86,87,88,89,90,91,0,5279.33984375,2883.15991211,433.020996094,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3767,,  
// 2241,0,83,84,85,86,87,88,89,90,91,0,5280.85986328,2840.39990234,433.471984863,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3768,,  
// 2242,0,83,84,85,86,87,88,89,90,91,0,5280.31982422,2798.61010742,433.476989746,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3769,,  
// 2243,0,92,93,94,95,96,97,98,99,100,0,5302.00976563,2771.66992188,433.389007568,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3770,,  
// 2244,0,92,93,94,95,96,97,98,99,100,0,5343.66015625,2771.01000977,432.82699585,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FE,3771,,  
// 2245,0,92,93,94,95,96,97,98,99,100,0,5384.39990234,2772.5300293,433.743988037,571,391,4197,"Wintergrasp Fortress Wall",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3772,,  


WG\_FORTRESS\_GRAVEYARD = 3773, // 2268,0,8,8,8,13,13,13,15,15,15,0,5538.37988281,2894.84008789,517.054992676,571,903,4197,"Fortress Graveyard",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3773,,  


WG\_CLOCKWORLDSTATE = 3781,  
BFTU\_TIME\_MIN\_03 = 3782, // // The next battle begins in $3975w:$3976w$3782w:$3784w$3785w.  
BFTU\_TIME\_MIN\_04 = 3784,  
BFTU\_TIME\_MIN\_05 = 3785,  


BATTLEFIELD\_WG\_WORLD\_STATE\_ACTIVE = 3801,  
BATTLEFIELD\_WG\_WORLD\_STATE\_DEFENDER = 3802,  
BATTLEFIELD\_WG\_WORLD\_STATE\_ATTACKER = 3803,  
2264,0,48,46,101,0,0,0,0,0,0,0,5121.37988281,2845.13989258,405.680999756,571,424,4197,"Wintergrasp",,,,,,,,,,,,,,,,0xFF01FE,"Control of Wintergrasp",,,,,,,,,,,,,,,,0xFF01FE,3804,,  
2142,0,6,54,55,10,52,53,11,50,51,0,4397.97021484,2822.60009766,458.842010498,571,903,4197,"Winter's Edge Tower",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3705,,  


VH\_WORLD\_STATE\_WAVE\_COUNT = 3810,  
VH\_WORLD\_STATE\_PRISON\_STATE = 3815,  
VH\_WORLD\_STATE\_SHOW = 3816,  


BG\_SA\_ANCIENT\_GATEWS = 3849, // 2292,0,80,81,82,77,78,79,74,75,76,0,881.70300293,-108.355007,109.834999084,607,959,4384,"Chamber of Ancient Relics",,,,,,,,,,,,,,,,0xFF01FE,"",,,,,,,,,,,,,,,,0xFF01FC,3849,,  


BATTLE\_FOR\_THE\_UNDERCITY\_UI\_BATTLE\_BEGUN = 3875, // The battle for Undercity has begun!  
BATTLE\_FOR\_THE\_UNDERCITY\_UI\_TIME\_REMANING = 3876,  
BATTLE\_FOR\_THE\_UNDERCITY\_TIME\_REMANING = 3877, // %3877w minutes until the battle for the Undercity begins!  


3885 // unknown  


ARENA\_SEASON\_ID = 3901, // CONFIG\_ARENA\_SEASON\_ID // SendInitWorldStates  


TIME\_UNTIL\_CHRISTMAS = 3930, // Days is $3930e. // Time until Christmas: $3930d.  


COT\_WORLDSTATE\_TIME\_GUARDIAN = 3931,  
COT\_WORLDSTATE\_TIME\_GUARDIAN\_SHOW = 3932,  


BFTU\_TIME\_MIN\_01 = 3975,// The next battle begins in $3975w:$3976w$3782w:$3784w$3785w. // <http://www.wowhead.com/quest=13267/the-battle-for-the-undercity>  
BFTU\_TIME\_MIN\_02 = 3976,  


BATTLEFIELD\_WG\_WORLD\_STATE\_ATTACKED\_H = 4022,  
BATTLEFIELD\_WG\_WORLD\_STATE\_ATTACKED\_A = 4023,  
BATTLEFIELD\_WG\_WORLD\_STATE\_DEFENDED\_H = 4024,  
BATTLEFIELD\_WG\_WORLD\_STATE\_DEFENDED\_A = 4025,  


ULDUAR\_WORLD\_STATE\_ALGALON\_DESPAWN\_TIMER = 4131, // default value 60  
ULDUAR\_WORLD\_STATE\_ALGALON\_TIMER\_ENABLED = 4132,  


// 2332,0,10,52,53,6,0,0,0,0,0,0,-79.7774963379,89.0569992065,483.743011475,603,903,4445,"Tower of Flames",,,,,,,,,,,,,,,,0xFF01FE,"Provides power to Mimiron's Inferno",,,,,,,,,,,,,,,,0xFF01FE,4195,,  
// 2333,0,10,52,53,6,0,0,0,0,0,0,82.2553024292,-392.476013184,460.160003662,603,903,4445,"Tower of Frost",,,,,,,,,,,,,,,,0xFF01FE,"Provides power to Hodir's Fury",,,,,,,,,,,,,,,,0xFF01FE,4196,,  
// 2331,0,10,52,53,6,0,0,0,0,0,0,-223.332000732,-299.079986572,418.652008057,603,903,4273,"Tower of Life",,,,,,,,,,,,,,,,0xFF01FE,"Supplies power to Freya's Ward",,,,,,,,,,,,,,,,0xFF01FE,4053,,  
// 2334,0,10,52,53,6,0,0,0,0,0,0,341.265991211,317.850006104,459.083007813,603,903,4445,"Tower of Storms",,,,,,,,,,,,,,,,0xFF01FE,"Provides power to Thorim's Hammer",,,,,,,,,,,,,,,,0xFF01FE,4197,,  


BG\_IC\_ALLIANCE\_RENFORT\_SET = 4221,  
BG\_IC\_HORDE\_RENFORT\_SET = 4222,  
BG\_IC\_ALLIANCE\_RENFORT = 4226,  
BG\_IC\_HORDE\_RENFORT = 4227,  
BG\_IC\_WORKSHOP\_CONFLICT\_A = 4228,  
BG\_IC\_WORKSHOP\_CONTROLLED\_A = 4229,  
BG\_IC\_WORKSHOP\_CONTROLLED\_H = 4230,  
BG\_IC\_UNK1 = 4243,  
BG\_IC\_UNK2 = 4345,  
BG\_WS\_STATE\_TIMER\_ACTIVE = 4247,  
BG\_WS\_STATE\_TIMER = 4248,  


EVENT\_ARENA\_TOURNAMENT\_COUNTDOWN = 4262, // Countdown to February 16th, 2007: $4262d$BRaw number: $4262e // The goblin Steamwheedle Fighting Circuit is beginning soon. They're holding practice matches in their arenas now, but ranking fights begin in $4262d. // <https://web.archive.org/web/20070903121702/http://www.wowarmory.com/arena-tournament.xml>  
BG\_IC\_WORKSHOP\_CONFLICT\_H = 4293,  
BG\_IC\_WORKSHOP\_UNCONTROLLED = 4294,  
BG\_IC\_HANGAR\_UNCONTROLLED = 4296,  
BG\_IC\_HANGAR\_CONFLICT\_H = 4297,  
BG\_IC\_HANGAR\_CONTROLLED\_H = 4298,  
BG\_IC\_HANGAR\_CONTROLLED\_A = 4299,  
BG\_IC\_HANGAR\_CONFLICT\_A = 4300,  
BG\_IC\_DOCKS\_UNCONTROLLED = 4301,  
BG\_IC\_DOCKS\_CONFLICT\_H = 4302,  
BG\_IC\_DOCKS\_CONTROLLED\_H = 4303,  
BG\_IC\_DOCKS\_CONTROLLED\_A = 4304,  
BG\_IC\_DOCKS\_CONFLICT\_A = 4305,  
BG\_IC\_QUARRY\_UNCONTROLLED = 4306,  
BG\_IC\_QUARRY\_CONFLICT\_H = 4307,  
BG\_IC\_QUARRY\_CONTROLLED\_H = 4308,  
BG\_IC\_QUARRY\_CONTROLLED\_A = 4309,  
BG\_IC\_QUARRY\_CONFLICT\_A = 4310,  
BG\_IC\_REFINERY\_UNCONTROLLED = 4311,  
BG\_IC\_REFINERY\_CONFLICT\_A = 4315,  
BG\_IC\_REFINERY\_CONFLICT\_H = 4312,  
BG\_IC\_REFINERY\_CONTROLLED\_A = 4314,  
BG\_IC\_REFINERY\_CONTROLLED\_H = 4313,  


BG\_IC\_GATE\_FRONT\_H\_WS\_CLOSED = 4317,  
BG\_IC\_GATE\_WEST\_H\_WS\_CLOSED = 4318,  
BG\_IC\_GATE\_EAST\_H\_WS\_CLOSED = 4319,  
BG\_IC\_GATE\_EAST\_H\_WS\_OPEN = 4320,  
BG\_IC\_GATE\_WEST\_H\_WS\_OPEN = 4321,  
BG\_IC\_GATE\_FRONT\_H\_WS\_OPEN = 4322,  
BG\_IC\_GATE\_FRONT\_A\_WS\_OPEN = 4323,  
BG\_IC\_GATE\_WEST\_A\_WS\_OPEN = 4324,  
BG\_IC\_GATE\_EAST\_A\_WS\_OPEN = 4325,  
BG\_IC\_GATE\_EAST\_A\_WS\_CLOSED = 4326,  
BG\_IC\_GATE\_WEST\_A\_WS\_CLOSED = 4327,  
BG\_IC\_GATE\_FRONT\_A\_WS\_CLOSED = 4328,


BG\_IC\_ALLIANCE\_KEEP\_CONTROLLED\_A = 4339,  
BG\_IC\_ALLIANCE\_KEEP\_CONTROLLED\_H = 4340,  
BG\_IC\_ALLIANCE\_KEEP\_UNCONTROLLED = 4341,  
BG\_IC\_ALLIANCE\_KEEP\_CONFLICT\_A = 4342,  
BG\_IC\_ALLIANCE\_KEEP\_CONFLICT\_H = 4343,  
BG\_IC\_HORDE\_KEEP\_CONTROLLED\_A = 4344,  
BG\_IC\_HORDE\_KEEP\_CONTROLLED\_H = 4345,  
BG\_IC\_HORDE\_KEEP\_UNCONTROLLED = 4346,  
BG\_IC\_HORDE\_KEEP\_CONFLICT\_A = 4347,  
BG\_IC\_HORDE\_KEEP\_CONFLICT\_H = 4348,


BG\_SA\_ALLY\_ATTACKS = 4352,  
BG\_SA\_HORDE\_ATTACKS = 4353,  
WG\_CLOCKWORLDSTATE = 4354, // Greetings, $c.$B$BWhen the Alliance controls Wintergrasp Fortress, I will open a portal for those who wish to travel there.$B$BThe next battle begins in $4354k.  


// 2377,0,80,0,0,0,0,0,0,0,0,0,352.003479004,-901.043395996,49.9881515503,628,943,4710,"Alliance Gate",,,,,,,,,,,,,,,,0xFF01FE,"East Gate",,,,,,,,,,,,,,,,0xFF01FE,4326,,  
// 2378,0,82,0,0,0,0,0,0,0,0,0,411.385406494,-833.796875,49.3037834167,628,943,4710,"Alliance Gate",,,,,,,,,,,,,,,,0xFF01FE,"Destroyed",,,,,,,,,,,,,,,,0xFF01FE,4323,,  
// 2379,0,82,0,0,0,0,0,0,0,0,0,352.003479004,-901.043395996,49.9881515503,628,943,4710,"Alliance Gate",,,,,,,,,,,,,,,,0xFF01FE,"Destroyed",,,,,,,,,,,,,,,,0xFF01FE,4325,,  
// 2380,0,80,0,0,0,0,0,0,0,0,0,351.668395996,-764.717041016,50.141834259,628,943,4710,"Alliance Gate",,,,,,,,,,,,,,,,0xFF01FE,"West Gate",,,,,,,,,,,,,,,,0xFF01FE,4327,,  
// 2381,0,82,0,0,0,0,0,0,0,0,0,351.668395996,-764.717041016,50.141834259,628,943,4710,"Alliance Gate",,,,,,,,,,,,,,,,0xFF01FE,"Destroyed",,,,,,,,,,,,,,,,0xFF01FE,4324,,  
// 2382,0,80,0,0,0,0,0,0,0,0,0,411.385406494,-833.796875,49.3037834167,628,943,4710,"Alliance Gate",,,,,,,,,,,,,,,,0xFF01FE,"Front Gate",,,,,,,,,,,,,,,,0xFF01FE,4328,,  
// 2383,0,6,0,0,0,0,0,0,0,0,0,347.760406494,-831.559020996,48.9162483215,628,943,4710,"Alliance Keep",,,,,,,,,,,,,,,,0xFF01FE,"Uncontrolled",,,,,,,,,,,,,,,,0xFF01FE,4341,,  
// 2384,0,11,0,0,0,0,0,0,0,0,0,347.760406494,-831.559020996,48.9162483215,628,943,4710,"Alliance Keep",,,,,,,,,,,,,,,,0xFF01FE,"Alliance Controlled",,,,,,,,,,,,,,,,0xFF01FE,4339,,  
// 2385,0,9,0,0,0,0,0,0,0,0,0,347.760406494,-831.559020996,48.9162483215,628,943,4710,"Alliance Keep",,,,,,,,,,,,,,,,0xFF01FE,"In Conflict",,,,,,,,,,,,,,,,0xFF01FE,4342,,  
// 2386,0,12,0,0,0,0,0,0,0,0,0,347.760406494,-831.559020996,48.9162483215,628,943,4710,"Alliance Keep",,,,,,,,,,,,,,,,0xFF01FE,"In Conflict",,,,,,,,,,,,,,,,0xFF01FE,4343,,  
// 2387,0,10,0,0,0,0,0,0,0,0,0,347.760406494,-831.559020996,48.9162483215,628,943,4710,"Alliance Keep",,,,,,,,,,,,,,,,0xFF01FE,"Horde Controlled",,,,,,,,,,,,,,,,0xFF01FE,4340,, 
// 2356,0,147,0,0,0,0,0,0,0,0,0,796.994812012,-379.947906494,11.9058227539,628,943,4710,"Docks",,,,,,,,,,,,,,,,0xFF01FE,"In Conflict",,,,,,,,,,,,,,,,0xFF01FE,4305,,  
// 2357,0,148,0,0,0,0,0,0,0,0,0,797.00177002,-379.91494751,11.9058227539,628,943,4710,"Docks",,,,,,,,,,,,,,,,0xFF01FE,"Horde Controlled",,,,,,,,,,,,,,,,0xFF01FE,4303,,  
// 2358,0,146,0,0,0,0,0,0,0,0,0,797.006958008,-379.907989502,11.9058227539,628,943,4710,"Docks",,,,,,,,,,,,,,,,0xFF01FE,"Alliance Controlled",,,,,,,,,,,,,,,,0xFF01FE,4304,,  
// 2359,0,149,0,0,0,0,0,0,0,0,0,796.998291016,-379.911468506,11.9058227539,628,943,4710,"Docks",,,,,,,,,,,,,,,,0xFF01FE,"In Conflict",,,,,,,,,,,,,,,,0xFF01FE,4302,,  
// 2360,0,145,0,0,0,0,0,0,0,0,0,796.996520996,-379.9375,11.9058227539,628,943,4710,"Docks",,,,,,,,,,,,,,,,0xFF01FE,"Uncontrolled",,,,,,,,,,,,,,,,0xFF01FE,4301,,  
// 2350,0,141,0,0,0,0,0,0,0,0,0,690.293395996,-1125.38195801,133.705673218,628,943,4710,"Hangar",,,,,,,,,,,,,,,,0xFF01FE,"Alliance Controlled",,,,,,,,,,,,,,,,0xFF01FE,4299,,  
// 2352,0,143,0,0,0,0,0,0,0,0,0,690.288208008,-1125.39587402,133.705673218,628,943,4710,"Hangar",,,,,,,,,,,,,,,,0xFF01FE,"Horde Controlled",,,,,,,,,,,,,,,,0xFF01FE,4298,,  
// 2353,0,142,0,0,0,0,0,0,0,0,0,690.26739502,-1125.37158203,133.705673218,628,943,4710,"Hangar",,,,,,,,,,,,,,,,0xFF01FE,"In Conflict",,,,,,,,,,,,,,,,0xFF01FE,4300,,  
// 2354,0,144,0,0,0,0,0,0,0,0,0,690.302062988,-1125.38891602,133.705673218,628,943,4710,"Hangar",,,,,,,,,,,,,,,,0xFF01FE,"In Conflict",,,,,,,,,,,,,,,,0xFF01FE,4297,,  
// 2355,0,140,0,0,0,0,0,0,0,0,0,690.295166016,-1125.40454102,133.705673218,628,943,4710,"Hangar",,,,,,,,,,,,,,,,0xFF01FE,"Uncontrolled",,,,,,,,,,,,,,,,0xFF01FE,4296,,  
// 2371,0,77,0,0,0,0,0,0,0,0,0,1151.18920898,-762.526062012,49.4423904419,628,943,4710,"Horde Gate",,,,,,,,,,,,,,,,0xFF01FE,"Front Gate",,,,,,,,,,,,,,,,0xFF01FE,4317,,  
// 2372,0,79,0,0,0,0,0,0,0,0,0,1151.18920898,-762.526062012,49.4423904419,628,943,4710,"Horde Gate",,,,,,,,,,,,,,,,0xFF01FE,"Destroyed",,,,,,,,,,,,,,,,0xFF01FE,4322,,  
// 2373,0,77,0,0,0,0,0,0,0,0,0,1218.58508301,-850.993041992,50.1930656433,628,943,4710,"Horde Gate",,,,,,,,,,,,,,,,0xFF01FE,"East Gate",,,,,,,,,,,,,,,,0xFF01FE,4319,,  
// 2374,0,79,0,0,0,0,0,0,0,0,0,1218.63024902,-851.102416992,50.1930656433,628,943,4710,"Horde Gate",,,,,,,,,,,,,,,,0xFF01FE,"Destroyed",,,,,,,,,,,,,,,,0xFF01FE,4320,,  
// 2375,0,77,0,0,0,0,0,0,0,0,0,1218.078125,-677.081604004,49.5540847778,628,943,4710,"Horde Gate",,,,,,,,,,,,,,,,0xFF01FE,"West Gate",,,,,,,,,,,,,,,,0xFF01FE,4318,,  
// 2376,0,79,0,0,0,0,0,0,0,0,0,1218.05212402,-677.121520996,49.5540847778,628,943,4710,"Horde Gate",,,,,,,,,,,,,,,,0xFF01FE,"Destroyed",,,,,,,,,,,,,,,,0xFF01FE,4321,,  
// 2388,0,10,0,0,0,0,0,0,0,0,0,1212.89233398,-765.418395996,48.9162483215,628,943,4710,"Horde Keep",,,,,,,,,,,,,,,,0xFF01FE,"Horde Controlled",,,,,,,,,,,,,,,,0xFF01FE,4345,,  
// 2389,0,11,0,0,0,0,0,0,0,0,0,1212.89233398,-765.418395996,48.9162483215,628,943,4710,"Horde Keep",,,,,,,,,,,,,,,,0xFF01FE,"Alliance Controlled",,,,,,,,,,,,,,,,0xFF01FE,4344,, 
// 2390,0,9,0,0,0,0,0,0,0,0,0,1212.89233398,-765.418395996,48.9162483215,628,943,4710,"Horde Keep",,,,,,,,,,,,,,,,0xFF01FE,"In Conflict",,,,,,,,,,,,,,,,0xFF01FE,4347,,  
// 2391,0,12,0,0,0,0,0,0,0,0,0,1212.89233398,-765.418395996,48.9162483215,628,943,4710,"Horde Keep",,,,,,,,,,,,,,,,0xFF01FE,"In Conflict",,,,,,,,,,,,,,,,0xFF01FE,4348,,  
// 2392,0,6,0,0,0,0,0,0,0,0,0,1212.89233398,-765.418395996,48.9162483215,628,943,4710,"Horde Keep",,,,,,,,,,,,,,,,0xFF01FE,"Uncontrolled",,,,,,,,,,,,,,,,0xFF01FE,4346,,  
// 2361,0,16,0,0,0,0,0,0,0,0,0,225.038192749,-1188.75695801,8.06681919098,628,943,4710,"Quarry",,,,,,,,,,,,,,,,0xFF01FE,"Uncontrolled",,,,,,,,,,,,,,,,0xFF01FE,4306,,  
// 2362,0,18,0,0,0,0,0,0,0,0,0,225.038192749,-1188.75695801,8.06681919098,628,943,4710,"Quarry",,,,,,,,,,,,,,,,0xFF01FE,"Alliance Controlled",,,,,,,,,,,,,,,,0xFF01FE,4309,,  
// 2363,0,20,0,0,0,0,0,0,0,0,0,225.038192749,-1188.75695801,8.06681919098,628,943,4710,"Quarry",,,,,,,,,,,,,,,,0xFF01FE,"Horde Controlled",,,,,,,,,,,,,,,,0xFF01FE,4308,,  
// 2364,0,17,0,0,0,0,0,0,0,0,0,225.038192749,-1188.75695801,8.06681919098,628,943,4710,"Quarry",,,,,,,,,,,,,,,,0xFF01FE,"In Conflict",,,,,,,,,,,,,,,,0xFF01FE,4310,,  
// 2365,0,19,0,0,0,0,0,0,0,0,0,225.038192749,-1188.75695801,8.06681919098,628,943,4710,"Quarry",,,,,,,,,,,,,,,,0xFF01FE,"In Conflict",,,,,,,,,,,,,,,,0xFF01FE,4307,,  
// 2366,0,153,0,0,0,0,0,0,0,0,0,1267.11804199,-396.069458008,24.23371315,628,943,4710,"Refinery",,,,,,,,,,,,,,,,0xFF01FE,"Horde Controlled",,,,,,,,,,,,,,,,0xFF01FE,4313,,  
// 2367,0,151,0,0,0,0,0,0,0,0,0,1267.11804199,-396.069458008,24.23371315,628,943,4710,"Refinery",,,,,,,,,,,,,,,,0xFF01FE,"Alliance Controlled",,,,,,,,,,,,,,,,0xFF01FE,4314,,  
// 2368,0,154,0,0,0,0,0,0,0,0,0,1267.11804199,-396.069458008,24.23371315,628,943,4710,"Refinery",,,,,,,,,,,,,,,,0xFF01FE,"In Conflict",,,,,,,,,,,,,,,,0xFF01FE,4312,,  
// 2369,0,152,0,0,0,0,0,0,0,0,0,1267.11804199,-396.069458008,24.23371315,628,943,4710,"Refinery",,,,,,,,,,,,,,,,0xFF01FE,"In Conflict",,,,,,,,,,,,,,,,0xFF01FE,4315,,  
// 2370,0,150,0,0,0,0,0,0,0,0,0,1267.11804199,-396.069458008,24.23371315,628,943,4710,"Refinery",,,,,,,,,,,,,,,,0xFF01FE,"Uncontrolled",,,,,,,,,,,,,,,,0xFF01FE,4311,,  
// 2345,0,136,0,0,0,0,0,0,0,0,0,772.734375,-805.51739502,6.61754703522,628,943,4710,"Workshop",,,,,,,,,,,,,,,,0xFF01FE,"Alliance Controlled",,,,,,,,,,,,,,,,0xFF01FE,4229,,  
// 2346,0,138,0,0,0,0,0,0,0,0,0,772.734375,-805.51739502,6.61754703522,628,943,4710,"Workshop",,,,,,,,,,,,,,,,0xFF01FE,"Horde Controlled",,,,,,,,,,,,,,,,0xFF01FE,4230,,  
// 2347,0,137,0,0,0,0,0,0,0,0,0,772.734375,-805.51739502,6.61754703522,628,943,4710,"Workshop",,,,,,,,,,,,,,,,0xFF01FE,"In Conflict",,,,,,,,,,,,,,,,0xFF01FE,4228,,  
// 2348,0,139,0,0,0,0,0,0,0,0,0,772.734375,-805.51739502,6.61754703522,628,943,4710,"Workshop",,,,,,,,,,,,,,,,0xFF01FE,"In Conflict",,,,,,,,,,,,,,,,0xFF01FE,4293,,  
// 2349,0,135,0,0,0,0,0,0,0,0,0,772.734375,-805.51739502,6.61754703522,628,943,4710,"Workshop",,,,,,,,,,,,,,,,0xFF01FE,"Uncontrolled",,,,,,,,,,,,,,,,0xFF01FE,4294,,  


EVENT\_ELEMENTALS\_FIRES\_EXTINGUISHED = 4857, // Fires Extinguished: $4857W/$4864W  
EVENT\_ELEMENTALS\_FURIOUS\_FIRE\_ELEMENTALS\_TOTAL = 4562, // Furious Fire Elementals Killed: $4582W/$4862W // 4862 default value 1000  
EVENT\_ELEMENTALS\_SEARING\_FIRE\_ELEMENTALS\_TOTAL = 4563, // Searing Fire Elementals Killed: $4584W/$4863W // 4863 default value 300  
EVENT\_ELEMENTALS\_FIRES\_EXTINGUISHED\_TOTAL = 4864, // Fires Extinguished: $4857W/$4864W // 4864 default value 100  
QUEST\_ASSAULT\_ON\_BASH\_IR\_LANDING\_TIME = 4581, // We are launching an assault on Bash'ir Landing, to study their Crystalforge. Help us if you can! Our Skyguard Aether-tech will leave in about $4581d.  
EVENT\_ELEMENTALS\_FURIOUS\_FIRE\_ELEMENTALS\_KILLED = 4582, // Furious Fire Elementals Killed: $4582W/$4862W  
EVENT\_ELEMENTALS\_SEARING\_FIRE\_ELEMENTALS\_KILLED = 4584, // Searing Fire Elementals Killed: $4584W/$4863W  


HOR\_WORLD\_STATE\_HOR\_WAVES\_ENABLED = 4884,  
HOR\_WORLD\_STATE\_HOR\_WAVE\_COUNT = 4882,  


ICC\_WORLDSTATE\_SHOW\_TIMER = 4903,  
ICC\_WORLDSTATE\_EXECUTION\_TIME = 4904,  
ICC\_COUNT\_DOWN = 4939, // NOT IMPLEMENTED // His spirit is free from the grasp of the Lich King. We must now focus our attention on breaking down the walls that block our passage into the upper reaches. It is only a matter of time now, $n. The siege engineers should have the door down in $4939W days. // The barrier to the Crimson Hall be open, $g lad:lass;! I got me best gnomes workin' on gettin' the barrier to the Frostwing Halls open. Looks like it's gonna be another $4939W days! Fer now,   it's probably best that you go face the blood princes and their queen! // We got the door down and the barrier preventin' entry to the Plagueworks busted open! My gnomes are werkin' on gettin' the barrier to the Crimson Hall down. It'll be another $4939W days before that thing comes down.$B$BGet in there and take out some Scourge!  
ICC\_WORLDSTATE\_SHOW\_ATTEMPTS = 4940,  
ICC\_WORLDSTATE\_ATTEMPTS\_REMAINING = 4941,  
ICC\_WORLDSTATE\_ATTEMPTS\_MAX = 4942,  


RS\_WORLDSTATE\_CORPOREALITY\_MATERIAL = 5049,  
RS\_WORLDSTATE\_CORPOREALITY\_TWILIGHT = 5050,  
RS\_WORLDSTATE\_CORPOREALITY\_TOGGLE = 5051,  


EVENT\_ECHO\_ISLES\_TIME = 5071, // De Echo Isles attack be startin' soon!$B$BSit back and relax, dis song will be over in anotha $5071W minutes and then we'd be going. // Okay! We're running a little behind, but the assaut is SCHEDULED to start in $5071W minutes.$B$BI mean, everything looks ready to go, and the Gyrocopters, Mechanotanks and Infantry are all here.$B$BIt looks like Mekkatorque is waiting on a few more things before the assault begins. Let's hope we start on time or I may lose   my job!  


ARENA\_RANKED\_MATCHES\_TIME = 6318, // Ranked arena matches start again in $6318d.$B$BWould-be champions are already busy honing their skills and acquiring the best gear they can. Are you going to be ready?  

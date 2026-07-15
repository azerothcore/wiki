# quest\_template

[<-Volver a: World](database-world)

**Tabla: quest\_template**

Contiene todas las definiciones básicas de las misiones disponibles.

## **Estructura**

| Field                           | Type      | Attribute | Key | Null | Default | Extra | Comment |
| ------------------------------- | --------- | --------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]                         | MEDIUMINT | UNSIGNED  | PRI | NO   | 0       |       |         |
| [QuestType][2]                  | TINYINT   | UNSIGNED  |     | NO   | 2       |       |         |
| [QuestLevel][3]                 | SMALLINT  |           |     | NO   | 1       |       |         |
| [MinLevel][4]                   | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [QuestSortID][5]                | SMALLINT  |           |     | NO   | 0       |       |         |
| [QuestInfoID][6]                | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [SuggestedGroupNum][7]          | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredFactionId1][8]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredFactionId2][9]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredFactionValue1][10]     | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RequiredFactionValue2][11]     | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardNextQuest][12]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardXPDifficulty][13]        | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardMoney][14]               | INT       |           |     | NO   | 0       |       |         |
| [RewardMoneyDifficulty][15]     | INT       | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardDisplaySpell][16]        | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardSpell][17]               | INT       |           |     | NO   | 0       |       |         |
| [RewardHonor][18]               | INT       |           |     | NO   | 0       |       |         |
| [RewardKillHonor][19]           | FLOAT     |           |     | NO   | 0       |       |         |
| [StartItem][20]                 | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [Flags][21]                     | INT       | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredPlayerKills][22]       | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardItem1][23]               | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardAmount1][24]             | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardItem2][25]               | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardAmount2][26]             | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardItem3][27]               | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardAmount3][28]             | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardItem4][29]               | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardAmount4][30]             | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDrop1][31]                 | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDropQuantity1][32]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDrop2][33]                 | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDropQuantity2][34]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDrop3][35]                 | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDropQuantity3][36]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDrop4][37]                 | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDropQuantity4][38]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID1][39]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity1][40] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID2][41]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity2][42] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID3][43]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity3][44] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID4][45]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity4][46] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID5][47]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity5][48] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID6][49]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity6][50] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [POIContinent][51]              | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [POIx][52]                      | FLOAT     |           |     | NO   | 0       |       |         |
| [POIy][53]                      | FLOAT     |           |     | NO   | 0       |       |         |
| [POIPriority][54]               | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardTitle][55]               | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardTalents][56]             | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardArenaPoints][57]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionID1][58]          | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionValue1][59]       | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionOverride1][60]    | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionID2][61]          | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionValue2][62]       | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionOverride2][63]    | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionID3][64]          | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionValue3][65]       | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionOverride3][66]    | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionID4][67]          | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionValue4][68]       | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionOverride4][69]    | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionID5][70]          | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionValue5][71]       | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionOverride5][72]    | MEDIUMINT |           |     | NO   | 0       |       |         |
| [TimeAllowed][73]               | INT       | UNSIGNED  |     | NO   | 0       |       |         |
| [AllowableRaces][74]            | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [LogTitle][75]                  | TEXT      |           |     | YES  |         |       |         |
| [LogDescription][76]            | TEXT      |           |     | YES  |         |       |         |
| [QuestDescription][77]          | TEXT      |           |     | YES  |         |       |         |
| [AreaDescription][78]           | TEXT      |           |     | YES  |         |       |         |
| [QuestCompletionLog][79]        | TEXT      |           |     | YES  |         |       |         |
| [RequiredNpcOrGo1][80]          | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGo2][81]          | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGo3][82]          | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGo4][83]          | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount1][84]     | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount2][85]     | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount3][86]     | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount4][87]     | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId1][88]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId2][89]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId3][90]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId4][91]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId5][92]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId6][93]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount1][94]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount2][95]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount3][96]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount4][97]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount5][98]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount6][99]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [Unknown0][100]                 | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [ObjectiveText1][101]           | TEXT      |           |     | YES  |         |       |         |
| [ObjectiveText2][102]           | TEXT      |           |     | YES  |         |       |         |
| [ObjectiveText3][103]           | TEXT      |           |     | YES  |         |       |         |
| [ObjectiveText4][104]           | TEXT      |           |     | YES  |         |       |         |
| [VerifiedBuild][105]            | SMALLINT  |           |     | YES  | 0       |       |         |

[1]: #id
[2]: #questtype
[3]: #questlevel
[4]: #minlevel
[5]: #questsortid
[6]: #questinfoid
[7]: #suggestedgroupnum
[8]: #requiredfactionid1
[9]: #requiredfactionid2
[10]: #requiredfactionvalue1
[11]: #requiredfactionvalue2
[12]: #rewardnextquest
[13]: #rewardxpdifficulty
[14]: #rewardmoney
[15]: #rewardmoneydifficulty
[16]: #rewarddisplayspell
[17]: #rewardspell
[18]: #rewardhonor
[19]: #rewardkillhonor
[20]: #startitem
[21]: #flags
[22]: #requiredplayerkills
[23]: #rewarditem1
[24]: #rewardamount1
[25]: #rewarditem2
[26]: #rewardamount2
[27]: #rewarditem3
[28]: #rewardamount3
[29]: #rewarditem4
[30]: #rewardamount4
[31]: #itemdrop1
[32]: #itemdropquantity1
[33]: #itemdrop2
[34]: #itemdropquantity2
[35]: #itemdrop3
[36]: #itemdropquantity3
[37]: #itemdrop4
[38]: #itemdropquantity4
[39]: #rewardchoiceitemid1
[40]: #rewardchoiceitemquantity1
[41]: #rewardchoiceitemid2
[42]: #rewardchoiceitemquantity2
[43]: #rewardchoiceitemid3
[44]: #rewardchoiceitemquantity3
[45]: #rewardchoiceitemid4
[46]: #rewardchoiceitemquantity4
[47]: #rewardchoiceitemid5
[48]: #rewardchoiceitemquantity5
[49]: #rewardchoiceitemid6
[50]: #rewardchoiceitemquantity6
[51]: #poicontinent
[52]: #poix
[53]: #poiy
[54]: #poipriority
[55]: #rewardtitle
[56]: #rewardtalents
[57]: #rewardarenapoints
[58]: #rewardfactionid1
[59]: #rewardfactionvalue1
[60]: #rewardfactionoverride1
[61]: #rewardfactionid2
[62]: #rewardfactionvalue2
[63]: #rewardfactionoverride2
[64]: #rewardfactionid3
[65]: #rewardfactionvalue3
[66]: #rewardfactionoverride3
[67]: #rewardfactionid4
[68]: #rewardfactionvalue4
[69]: #rewardfactionoverride4
[70]: #rewardfactionid5
[71]: #rewardfactionvalue5
[72]: #rewardfactionoverride5
[73]: #timeallowed
[74]: #allowableraces
[75]: #logtitle
[76]: #logdescription
[77]: #questdescription
[78]: #areadescription
[79]: #questcompletionlog
[80]: #requirednpcorgo1
[81]: #requirednpcorgo2
[82]: #requirednpcorgo3
[83]: #requirednpcorgo4
[84]: #requirednpcorgocount1
[85]: #requirednpcorgocount2
[86]: #requirednpcorgocount3
[87]: #requirednpcorgocount4
[88]: #requireditemid1
[89]: #requireditemid2
[90]: #requireditemid3
[91]: #requireditemid4
[92]: #requireditemid5
[93]: #requireditemid6
[94]: #requireditemcount1
[95]: #requireditemcount2
[96]: #requireditemcount3
[97]: #requireditemcount4
[98]: #requireditemcount5
[99]: #requireditemcount6
[100]: #unknown0
[101]: #objectivetext1
[102]: #objectivetext2
[103]: #objectivetext3
[104]: #objectivetext4
[105]: #verifiedbuild


**Descripción de los campos**

### ID

El ID de la misión. Esta columna es la clave primaria de la tabla. ¡Cada ID de misión debe ser único!

### QuestType

Valores aceptados: 0, 1 o 2. Su significado se describe en la tabla siguiente.

| Value | Result                                                                                                   |
| ----- | -------------------------------------------------------------------------------------------------------- |
| 0     | La misión está habilitada, pero se completa automáticamente al aceptarse; esto omite los objetivos y los detalles de la misión. |
| 1     | La misión está deshabilitada (aún no implementado en el core).                                           |
| 2     | La misión está habilitada (no se completa automáticamente).                                              |

### QuestLevel

Nivel de la misión. El jugador recibe la cantidad completa de experiencia solo si su nivel es menor o igual a Level+5. Si Level se establece a -1, se usará el nivel del jugador como (Quest)Level para el cálculo de experiencia.

### MinLevel

Nivel mínimo al que un jugador puede obtener la misión.

### QuestSortID

Este campo define bajo qué categoría cae la misión en el registro de misiones.

Si **valor &gt; 0** entonces el valor son IDs de zona tomados de AreaTable.dbc.

si **valor &lt; 0** entonces (**-valor**) es el id de orden de misión (quest sort id): (en general misiones de profesión o de clase. Ver también [RequiredSkillPoints](#quest_template-RequiredSkillPoints) ). El valor es el ID de QuestSort.dbc

### QuestInfoID

Estos valores son IDs tomados de [QuestInfo.dbc](questinfo)

| Value | Result       |
| ----- | ------------ |
| 0     | None         |
| 1     | Group        |
| 21    | Life         |
| 41    | PvP          |
| 62    | Raid         |
| 81    | Dungeon      |
| 82    | Event        |
| 83    | Legendary    |
| 84    | Escort       |
| 85    | Heroic       |
| 88    | Raid (10)    |
| 89    | Raid (25)    |

### SuggestedGroupNum

Número recomendado de jugadores para hacer la misión juntos.

### RewardFactionId1

Id de facción (de Faction.dbc) para la que la misión da puntos de reputación.
Número de puntos de reputación ganados o perdidos para la facción al completar la misión. Esta es la recompensa de reputación especial. La recompensa de reputación normal para la facción de la criatura que recompensa la misión se calcula y añade automáticamente.

### RewardFactionId2

Id de facción (de Faction.dbc) para la que la misión da puntos de reputación.
Número de puntos de reputación ganados o perdidos para la facción al completar la misión. Esta es la recompensa de reputación especial. La recompensa de reputación normal para la facción de la criatura que recompensa la misión se calcula y añade automáticamente.

### RewardFactionValueId1

Este campo se usa para la búsqueda de reputación en QuestFactionReward.dbc si quest_template#RewardFactionValueId es 0. El valor X en este campo indica la columna RepX de QuestFactionReward.dbc. Si RewardRepValueId es positivo, se usará la reputación de la primera fila de QuestFactionReward.dbc; para valores negativos se usa la segunda fila.

### RewardFactionValueId2
Este campo se usa para la búsqueda de reputación en QuestFactionReward.dbc si quest_template#RewardFactionValueId es 0. El valor X en este campo indica la columna RepX de QuestFactionReward.dbc. Si RewardRepValueId es positivo, se usará la reputación de la primera fila de QuestFactionReward.dbc; para valores negativos se usa la segunda fila.

### RewardNextQuest

** RewardNextQuest (nombre antiguo del campo: NextQuestIdChain)**

El entry de misión de una **criatura** o **gameobject** que finaliza una misión e inicia una nueva. El resultado es que, si finalizas la misión, la nueva misión aparece al instante desde el que da la misión.

Ver la [sección de ejemplos](#quest_template-Examples) para ejemplos.

### RewardXPDifficulty

Según el [Level](#quest_template-Level), la experiencia básica con índice *RewardXPDifficulty* se toma de QuestXP.dbc.

Este campo también controla la XP otorgada, ya que la XP se calcula a partir del valor de este campo mediante la siguiente fórmula. Si la misión es repetible, la XP se dará solo una vez. La XP total que recibirá un personaje también se ve afectada por la diferencia de nivel entre el nivel del personaje y el nivel de la misión.

La fórmula para calcular la XP a partir del valor de este campo:
- **QuestLevel &gt;= 65:** XP = RewMoneyMaxLevel / 6.0
- **QuestLevel h1. 64:** XP = RewMoneyMaxLevel / 4.8
- **QuestLevel 63:** XP = RewMoneyMaxLevel / 3.6
- **QuestLevel h1. 62:** XP = RewMoneyMaxLevel / 2.4
- **QuestLevel 61:** XP = RewMoneyMaxLevel / 1.2
- **QuestLevel &lt;= 60:** XP = RewMoneyMaxLevel / 0.6

### RewardMoney

Dinero ganado al completar la misión (si el valor &gt; 0) o requisito de dinero para completar la misión (si el valor &lt; 0).

### RewardMoneyDifficulty

El ID hace referencia a uno de los factores de dinero incluidos en [MoneyFactor](quest_money_reward) ordenados por nivel.

### RewardDisplaySpell

Hechizo que se muestra como lanzado al completar la misión en el registro de misiones. Ten en cuenta que este hechizo NO se lanzará si [RewardSpell](#quest_template-RewardSpell) es distinto de cero. En su lugar se lanzará el hechizo del otro campo, en cuyo caso el hechizo de aquí solo sirve de visual en el registro de misiones.

### RewardSpell

Hechizo que se muestra como lanzado al completar la misión en el registro de misiones. Ten en cuenta que este hechizo NO se lanzará si [RewardSpell](quest_template#rewardspell) es distinto de cero. En su lugar se lanzará el hechizo del otro campo, en cuyo caso el hechizo de aquí solo sirve de visual en el registro de misiones.

NOTA: Este campo viene directamente del WDB y no debe cambiarse.

### RewardHonor

Número de honor de muerte honorable recompensado por completar esta misión.

Ejemplo: un valor de ejemplo es 15 para la misión 8388: a nivel 80 una muerte honorable vale 124 de honor. Multiplica esto por 15 y obtienes 1860; tras la multiplicación el valor se redondea hacia arriba. Así que el honor recompensado a nivel 80 es 1860 para esta misión.

### RewardKillHonor


### StartItem

Objetos entregados por el que da la misión al comienzo de la misión. Los objetos se eliminarán cuando se abandone la misión.

### Flags

Este campo de flag define más específicamente el tipo de misión que es. Aparte del flag diario (daily) y el flag compartible (sharable), este campo se usa solo con fines de agrupación y NO para ningún otro requisito de misión. Los requisitos de la misión se calculan a partir de valores distintos de cero en otros campos de la plantilla de misión. Además, aunque algunos de estos flags son conocidos, otros tienen todavía un propósito desconocido y los comentarios de abajo son simplemente conjeturas sobre ellos.

| Flag       | Name                                 | Comments                                                                                                                                                               |
| ---------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0          | QUEST_FLAGS_NONE                     | Sin flags, así que no hay grupos asignados a esta misión.                                                                                                              |
| 1          | QUEST_FLAGS_STAY_ALIVE               | Si el jugador muere, la misión falla.                                                                                                                                  |
| 2          | QUEST_FLAGS_PARTY_ACCEPT             | Misiones de escolta o cualquier otra misión dirigida por eventos. Si el jugador está en grupo, todos los jugadores que puedan aceptar esta misión recibirán un cuadro de confirmación para aceptarla. |
| 4          | QUEST_FLAGS_EXPLORATION              | Implica la activación de un areatrigger.                                                                                                                               |
| 8          | QUEST_FLAGS_SHARABLE                 | Permite compartir la misión con otros jugadores.                                                                                                                       |
| 16         | QUEST_FLAGS_HAS_CONDITION            | No se usa actualmente                                                                                                                                                  |
| 32         | QUEST_FLAGS_HIDE_REWARD_POI          | No se usa actualmente: contenido incierto                                                                                                                              |
| 64         | QUEST_FLAGS_RAID                     | Se puede completar estando en banda (raid)                                                                                                                             |
| 128        | QUEST_FLAGS_TBC                      | No se usa actualmente: disponible solo si la expansión TBC está habilitada                                                                                             |
| 256        | QUEST_FLAGS_NO_MONEY_FROM_XP         | No se usa actualmente: la experiencia no se convierte en oro al nivel máximo                                                                                           |
| 512        | QUEST_FLAGS_HIDDEN_REWARDS           | Las recompensas de objetos y monetarias están ocultas en la página inicial de detalles de la misión y en el registro de misiones, pero aparecerán una vez listas para recompensarse. |
| 1024       | QUEST_FLAGS_TRACKING                 | Estas misiones se recompensan automáticamente al completarse y nunca aparecerán en el registro de misiones del lado del cliente.                                       |
| 2048       | QUEST_FLAGS_DEPRECATE_REPUTATION     | No se usa actualmente                                                                                                                                                  |
| 4096       | QUEST_FLAGS_DAILY                    | Misiones diarias repetibles (el único flag para el que el core aplica un comportamiento específico)                                                                    |
| 8192       | QUEST_FLAGS_FLAGS_PVP                | Tener esta misión en el registro fuerza el flag de PvP                                                                                                                 |
| 16384      | QUEST_FLAGS_UNAVAILABLE              | Usado en misiones que no están disponibles de forma genérica                                                                                                           |
| 32768      | QUEST_FLAGS_WEEKLY                   | Misiones semanales repetibles (el único flag para el que el core aplica un comportamiento específico)                                                                  |
| 65536      | QUEST_FLAGS_AUTOCOMPLETE             | Autocompletado                                                                                                                                                         |
| 131072     | QUEST_FLAGS_DISPLAY_ITEM_IN_TRACKER  | Muestra un objeto usable en el rastreador de misiones                                                                                                                  |
| 262144     | QUEST_FLAGS_OBJ_TEXT                 | Usa el texto de objetivo como texto de completado                                                                                                                      |
| 524288     | QUEST_FLAGS_AUTO_ACCEPT              | El cliente reconoce este flag como aceptación automática. Sin embargo, NINGUNA de las misiones actuales (3.3.5a) tiene este flag. Quizá blizz lo usaba, o lo usará en el futuro. |
| 1048576    | QUEST_FLAGS_PLAYER_CAST_ON_ACCEPT    | En las misiones con este flag el jugador envía automáticamente mediante un botón especial en la GUI del jugador                                                        |
| 2097152    | QUEST_FLAGS_PLAYER_CAST_ON_COMPLETE  | Sugerencia automática de aceptar la misión. No desde un npc.                                                                                                           |
| 4194304    | QUEST_FLAGS_UPDATE_PHASE_SHIFT       |                                                                                                                                                                        |
| 8388608    | QUEST_FLAGS_SOR_WHITELIST            |                                                                                                                                                                        |
| 16777216   | QUEST_FLAGS_LAUNCH_GOSSIP_COMPLETE   |                                                                                                                                                                        |
| 54432      | QUEST_FLAGS_REMOVE_EXTRA_GET_ITEMS   |                                                                                                                                                                        |
| 67108864   | QUEST_FLAGS_HIDE_UNTIL_DISCOVERED    |                                                                                                                                                                        |
| 134217728  | QUEST_FLAGS_PORTRAIT_IN_QUEST_LOG    |                                                                                                                                                                        |
| 268435456  | QUEST_FLAGS_SHOW_ITEM_WHEN_COMPLETED |                                                                                                                                                                        |
| 536870912  | QUEST_FLAGS_LAUNCH_GOSSIP_ACCEPT     |                                                                                                                                                                        |
| 1073741824 | QUEST_FLAGS_ITEMS_GLOW_WHEN_DONE     |                                                                                                                                                                        |
| 2147483648 | QUEST_FLAGS_FAIL_ON_LOGOUT           |                                                                                                                                                                        |

Como todos los campos basados en flags, **QuestFlags** pueden sumarse para los distintos tipos de misión.

Ten en cuenta que algunos flags pueden no estar soportados por el core.

### RequiredPlayerKills

Muestra a cuántos jugadores necesitas matar betd class=td class=a class=/td data-linked-resource-default-alias=fore completar la misión.

### RewardItem1

[item Id 1](item_template#entry) entregado como recompensa (sin elección).

### RewardAmount1

Cantidad a obtener del objeto mencionado arriba

### RewardItem2

[item Id 2](item_template#entry) entregado como recompensa (sin elección).

### RewardAmount2

Cantidad a obtener del objeto mencionado arriba

### RewardItem3

[item Id 3](item_template#entry) entregado como recompensa (sin elección).

### RewardAmount3

Cantidad a obtener del objeto mencionado arriba

### RewardItem4

[item Id 4](item_template#entry) entregado como recompensa (sin elección).

### RewardAmount4

Cantidad a obtener del objeto mencionado arriba

### ItemDrop1



### ItemDropQuantity1



### ItemDrop2



### ItemDropQuantity2



### ItemDrop3



### ItemDropQuantity3



### ItemDrop4



### ItemDropQuantity4



### RewardChoiceItemID1



### RewardChoiceItemQuantity1


### RewardChoiceItemID2


### RewardChoiceItemQuantity2


### RewardChoiceItemID3


### RewardChoiceItemQuantity3


### RewardChoiceItemID4


### RewardChoiceItemQuantity4


### RewardChoiceItemID5


### RewardChoiceItemQuantity5


### RewardChoiceItemID6


### RewardChoiceItemQuantity6


### POIContinent

MapId de un punto de interés de misión (POI - Point Of Interest). El POI se mostrará en el mapa cuando la misión esté activa.

### POIx

Coordenada X del POI de la misión.

### POIy

Coordenada Y del POI de la misión.

### POIPriority

TODO

### RewardTitle


### RewardTalents


### RewardArenaPoints


### RewardFactionID1


### RewardFactionValue1


### RewardFactionOverride1


### RewardFactionID2


### RewardFactionValue2


### ItemDrop


### RewardFactionOverride2


### RewardFactionID3


### ItemDropQuantity

El número máximo de copias del objeto en ItemDrop que pueden recogerse (y soltarse por el core).

### RewardFactionValue3


### RewardFactionOverride3


### RewardFactionID4


### RewardFactionValue4


### RewardFactionOverride4


### RewardFactionID5


### RewardFactionValue5


### RewardFactionOverride5


### TimeAllowed


### AllowableRaces


### LogTitle

Título de la misión.

### LogDescription

Objetivos de la misión. Si está vacío, la misión es de autocompletado y puede finalizarse inmediatamente sin aceptarla primero.

### QuestDescription

El texto de la misión. Puedes usar ciertos placeholders que se rellenarán en el juego: $B - salto de línea, $N - nombre, $R - raza, $C - clase, $Gmasculino:femenino; (masculino y femenino pueden reemplazarse por cualquier sinónimo que quieras, pero el orden debe mantenerse. P. ej.: chico:chica / hombre:mujer / señor:señora / tío:tía)

### AreaDescription


### QuestCompletionLog

Texto enviado al jugador cuando el jugador intenta hablar con el NPC con la misión activa pero incompleta. (El texto bajo el título "Progreso" en Wowhead.) Puedes usar ciertos placeholders que se rellenarán en el juego: $B - salto de línea, $N - nombre, $R - raza, $C - clase, $Gmasculino:femenino; (masculino y femenino pueden reemplazarse por cualquier sinónimo que quieras, pero el orden debe mantenerse. P. ej.: chico:chica / hombre:mujer / señor:señora / tío:tía)

### RequiredNpcOrGo1
### RequiredNpcOrGo2
### RequiredNpcOrGo3
### RequiredNpcOrGo4

- Valor &gt; 0: ID de creature\_template requerido que el jugador necesita matar/lanzar sobre él para completar la misión.
- Valor &lt; 0: ID de gameobject\_template requerido sobre el que el jugador necesita lanzar para completar la misión.
- Si\*RequiredSpellCast\*es != 0, el objetivo es lanzar sobre el objetivo, si no, matar.

NOTA: Si RequiredSpellCast es != 0 y el hechizo tiene efectos Send Event o Quest Complete, este campo puede dejarse vacío.

### RequiredNpcOrGoCount1
### RequiredNpcOrGoCount2
### RequiredNpcOrGoCount3
### RequiredNpcOrGoCount4

El número de veces que la criatura o gameobject debe ser matado o lanzado sobre él.

### RequiredItemId1
### RequiredItemId2
### RequiredItemId3
### RequiredItemId4
### RequiredItemId5
### RequiredItemId6

[Id](item_template#entry) del objeto requerido para completar la misión.

### RequiredItemCount1
### RequiredItemCount2
### RequiredItemCount3
### RequiredItemCount4
### RequiredItemCount5
### RequiredItemCount6

Cantidad de objetos requeridos

### Unknown0


### ObjectiveText1
### ObjectiveText2
### ObjectiveText3
### ObjectiveText4

Se usa para definir textos de objetivo no estándar que aparecen en el registro de misiones. Ejemplo, "Curar al guerrero caído" y el número lo añaden los valores de Count.

### VerifiedBuild

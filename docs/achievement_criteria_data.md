# achievement\_criteria\_data

[<-Back-to:World](database-world)

**The \`achievement\_criteria\_data\` table**

This table contains the data that a player needs to obtain / complete in order to receive a given achievement.

**Table Structure**

| Field            | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [criteria_id][1] | MEDIUMINT |            | PRI | NO   |         |       |         |
| [type][2]        | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |         |
| [value1][3]      | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [value2][4]      | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [ScriptName][5]  | char(64)  |            |     | NO   |         |       |         |

[1]: #criteria_id
[2]: #type
[3]: #value1
[4]: #value2
[5]: #scriptname

**Description of the fields**

### criteria\_id

This is the ID from [Achievement\_Criteria.dbc](Achievement+Criteria).

### type

Depending on this value, it will determine how value1 and value2 are used.

| Type | Name                      |
| ---- | ------------------------- |
| 0    | TYPE_NONE                 |
| 1    | TYPE_T_CREATURE           |
| 2    | TYPE_T_PLAYER_CLASS_RACE  |
| 3    | TYPE_T_PLAYER_LESS_HEALTH |
| 4    | TYPE_T_PLAYER_DEAD        |
| 5    | TYPE_S_AURA               |
| 6    | TYPE_S_AREA               |
| 7    | TYPE_T_AURA               |
| 8    | TYPE_VALUE                |
| 9    | TYPE_T_LEVEL              |
| 10   | TYPE_T_GENDER             |
| 11   | TYPE_SCRIPT               |
| 12   | TYPE_MAP_DIFFICULTY       |
| 13   | TYPE_MAP_PLAYER_COUNT     |
| 14   | TYPE_T_TEAM               |
| 15   | TYPE_S_DRUNK              |
| 16   | TYPE_HOLIDAY              |
| 17   | TYPE_BG_LOSS_TEAM_SCORE   |
| 18   | TYPE_INSTANCE_SCRIPT      |
| 19   | TYPE_S_EQUIPED_ITEM       |
| 20   | TYPE_MAP_ID               |
| 21   | TYPE_S_PLAYER_CLASS_RACE  |
| 22   | TYPE_NTH_BIRTHDAY         |
| 23   | TYPE_S_KNOWN_TITLE        |

### value1

**TYPE\_T\_CREATURE**

-   The target here must be a valid entry from creature\_template

**TYPE\_T\_PLAYER\_CLASS\_RACE**

-   The target here is a valid class (paste class list). value2 must also be set

**TYPE\_T\_PLAYER\_LESS\_HEALTH**

-   The percentage of health that the target must reach.

**TYPE\_T\_PLAYER\_DEAD**

-   The faction of the target player (must match player attempting achievement).

**TYPE\_S\_AURA**

-   The spell ID of the aura that must be on the player. value2 must also be set.

**TYPE\_S\_AREA**

-   Area ID from AreaTable.dbc

**TYPE\_T\_AURA**

-   The spell ID of the aura that must be on the target. value2 must also be set.

**TYPE\_VALUE**

-   Value to compare needed to attain achievement. This value is used in conjunction with another type. (see value2 for comparisation type)

**TYPE\_T\_LEVEL**

-   The minimum level that the target can be.

**TYPE\_T\_GENDER**

-   Gender: 0=Male, 1=Female

**TYPE\_SCRIPT**

-   Used to disable an achievement if all requirements are not defined. Would usually be used if not all are known.

**TYPE\_MAP\_DIFFICULTY**

-   Map difficulty: (for dungeons)
    - Normal = 0
    - Heroic = 1
-   Map difficulty: (for raids)
    - 10 Man Normal = 0
    - 25 Man Normal = 1
    - 10 Man Heroic = 2
    - 25 Man Heroic = 3

**TYPE\_MAP\_PLAYER\_COUNT**

-   The number of other players that must be in the zone. (not sure if it is minimum or maximum).

**TYPE\_T\_TEAM**

-   The target must be on this team: Alliance = 469, Horde = 67

**TYPE\_S\_DRUNK**

-   How drunk the player must be:
    - DRUNKEN\_SOBER = 0
    - DRUNKEN\_TIPSY = 1
    - DRUNKEN\_DRUNK = 2
    - DRUNKEN\_SMASHED = 3

**TYPE\_HOLIDAY**

-   Holiday ID from Holiday.dbc and game\_event. Must be an active holiday.

**TYPE\_BG\_LOSS\_TEAM\_SCORE**

-   Player's team win bg and opposition team have team score in range. // Min. score

**TYPE\_INSTANCE\_SCRIPT**

-   Make instance script call for check current criteria requirements fit.

**TYPE\_S\_EQUIPED\_ITEM**

-   Item level

**TYPE\_MAP\_ID**

-   Player must be on mapId

**TYPE\_S\_PLAYER\_CLASS\_RACE**

-   The Source here is a valid class (paste class list). value2 must also be set
 

**TYPE\_NTH\_BIRTHDAY**

-   Number of Birthday

**TYPE\_S\_KNOWN\_TITLE**

-   The value here is a valid titleId. See CharTitles.dbc

### value2

**TYPE\_T\_PLAYER\_CLASS\_RACE**
**TYPE\_S\_PLAYER\_CLASS\_RACE**

-   The value here is a valid race ID. See ChrRaces.dbc

**TYPE\_S\_AURA**

-   Effect Index of the aura

**TYPE\_T\_AURA**

-   Effect Index of the aura

**TYPE\_BG\_LOSS\_TEAM\_SCORE**

-   Max. score

**TYPE\_S\_EQUIPED\_ITEM**

-   Item quality

**TYPE\_VALUE**

| ComparisationType        |
| ------------------------ |
| COMP\_TYPE\_EQ = 0       |
| COMP\_TYPE\_HIGH = 1     |
| COMP\_TYPE\_LOW = 2      |
| COMP\_TYPE\_HIGH\_EQ = 3 |
| COMP\_TYPE\_LOW\_EQ = 4  |

### ScriptName

The ScriptName for when scripting it in the core.
This might also be 'SmartTrigger'. It will than use [SmartAI](smart_scripts).

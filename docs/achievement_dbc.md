# achievement\_dbc

[<-Back-to:World](database-world)

**The \`achievement\_dbc\` table**

This table has the same columns as [Achievement.dbc](achievement). The core loads it after the DBC file: a row adds an achievement that is not in Achievement.dbc, or replaces the achievement with the same [ID](#id).

The core reads every column in order, so a row must have a value for all of them, even the columns the core does not use. An empty text column keeps the text from the DBC file.

**Table: achievement\_dbc's Structure**

| Field                                     | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                 | INT          |          | NO   | PRI | 0       |       |         |
| [Faction](#faction)                       | INT          |          | NO   |     | 0       |       |         |
| [Instance_Id](#instanceid)                | INT          |          | NO   |     | 0       |       |         |
| [Supercedes](#supercedes)                 | INT          |          | NO   |     | 0       |       |         |
| [Title_Lang_enUS](#titlelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Title_Lang_enGB](#titlelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Title_Lang_koKR](#titlelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Title_Lang_frFR](#titlelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Title_Lang_deDE](#titlelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Title_Lang_enCN](#titlelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Title_Lang_zhCN](#titlelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Title_Lang_enTW](#titlelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Title_Lang_zhTW](#titlelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Title_Lang_esES](#titlelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Title_Lang_esMX](#titlelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Title_Lang_ruRU](#titlelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Title_Lang_ptPT](#titlelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Title_Lang_ptBR](#titlelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Title_Lang_itIT](#titlelang)             | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Title_Lang_Unk](#titlelang)              | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Title_Lang_Mask](#titlelang)             | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Description_Lang_enUS](#descriptionlang) | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Description_Lang_enGB](#descriptionlang) | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Description_Lang_koKR](#descriptionlang) | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Description_Lang_frFR](#descriptionlang) | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Description_Lang_deDE](#descriptionlang) | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Description_Lang_enCN](#descriptionlang) | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Description_Lang_zhCN](#descriptionlang) | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Description_Lang_enTW](#descriptionlang) | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Description_Lang_zhTW](#descriptionlang) | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Description_Lang_esES](#descriptionlang) | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Description_Lang_esMX](#descriptionlang) | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Description_Lang_ruRU](#descriptionlang) | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Description_Lang_ptPT](#descriptionlang) | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Description_Lang_ptBR](#descriptionlang) | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Description_Lang_itIT](#descriptionlang) | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Description_Lang_Unk](#descriptionlang)  | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Description_Lang_Mask](#descriptionlang) | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Category](#category)                     | INT          |          | NO   |     | 0       |       |         |
| [Points](#points)                         | INT          |          | NO   |     | 0       |       |         |
| [Ui_Order](#uiorder)                      | INT          |          | NO   |     | 0       |       |         |
| [Flags](#flags)                           | INT          |          | NO   |     | 0       |       |         |
| [IconID](#iconid)                         | INT          |          | NO   |     | 0       |       |         |
| [Reward_Lang_enUS](#rewardlang)           | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Reward_Lang_enGB](#rewardlang)           | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Reward_Lang_koKR](#rewardlang)           | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Reward_Lang_frFR](#rewardlang)           | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Reward_Lang_deDE](#rewardlang)           | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Reward_Lang_enCN](#rewardlang)           | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Reward_Lang_zhCN](#rewardlang)           | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Reward_Lang_enTW](#rewardlang)           | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Reward_Lang_zhTW](#rewardlang)           | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Reward_Lang_esES](#rewardlang)           | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Reward_Lang_esMX](#rewardlang)           | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Reward_Lang_ruRU](#rewardlang)           | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Reward_Lang_ptPT](#rewardlang)           | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Reward_Lang_ptBR](#rewardlang)           | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Reward_Lang_itIT](#rewardlang)           | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Reward_Lang_Unk](#rewardlang)            | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Reward_Lang_Mask](#rewardlang)           | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Minimum_Criteria](#minimumcriteria)      | INT          |          | NO   |     | 0       |       |         |
| [Shares_Criteria](#sharescriteria)        | INT          |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The ID of the achievement. [Achievement\_Criteria.dbc](achievement_criteria) links criteria to it.

### Faction

| Value | Faction |
| ----- | ------- |
| -1    | Both    |
| 0     | Horde   |
| 1     | Alliance |

### Instance\_Id

Map ID the player must be on for the criteria to update. -1 if not set.

### Supercedes

ID of the achievement this one follows in a series. Not used by the core.

### Title\_Lang

`Title_Lang_enUS` to `Title_Lang_Unk` and `Title_Lang_Mask`. The name of the achievement. The mask is not used by the core.

The text columns are the 16 locale slots of the file. The core reads them by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Title_Lang_enUS` = enUS, `Title_Lang_enGB` = koKR, `Title_Lang_koKR` = frFR, `Title_Lang_frFR` = deDE, `Title_Lang_deDE` = zhCN, `Title_Lang_enCN` = zhTW, `Title_Lang_zhCN` = esES, `Title_Lang_enTW` = esMX, `Title_Lang_zhTW` = ruRU. The remaining text columns, `Title_Lang_esES` to `Title_Lang_Unk`, are not supported in 3.3.5a and are not used.

### Description\_Lang

`Description_Lang_enUS` to `Description_Lang_Unk` and `Description_Lang_Mask`. The description of the achievement. Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Description_Lang_enUS` = enUS, `Description_Lang_enGB` = koKR, `Description_Lang_koKR` = frFR, `Description_Lang_frFR` = deDE, `Description_Lang_deDE` = zhCN, `Description_Lang_enCN` = zhTW, `Description_Lang_zhCN` = esES, `Description_Lang_enTW` = esMX, `Description_Lang_zhTW` = ruRU. The remaining text columns, `Description_Lang_esES` to `Description_Lang_Unk`, are not supported in 3.3.5a and are not used.

### Category

ID from Achievement\_Category.dbc of the category the achievement is listed under.

### Points

Achievement points awarded for completing the achievement. Has no use serverside.

### Ui\_Order

Position of the achievement in its category. Not used by the core.

### Flags

| Value | Hex      | Flag                               | Comment                                                                                                                                                                                                     |
| :---- | :------: | :--------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | `0x0001` | ACHIEVEMENT_FLAG_COUNTER           | Just count statistic (never stop and complete)                                                                                                                                                              |
| 2     | `0x0002` | ACHIEVEMENT_FLAG_HIDDEN            | Not sent to client - internal use only                                                                                                                                                                      |
| 4     | `0x0004` | ACHIEVEMENT_FLAG_STORE_MAX_VALUE   | Store only max value? used only in "Reach level xx"                                                                                                                                                         |
| 8     | `0x0008` | ACHIEVEMENT_FLAG_SUMM              | Use summ criteria value from all reqirements (and calculate max value)                                                                                                                                      |
| 16    | `0x0010` | ACHIEVEMENT_FLAG_MAX_USED          | Show max criteria (and calculate max value ??)                                                                                                                                                              |
| 32    | `0x0020` | ACHIEVEMENT_FLAG_REQ_COUNT         | Use not zero req count (and calculate max value)                                                                                                                                                            |
| 64    | `0x0040` | ACHIEVEMENT_FLAG_AVERAGE           | Show as average value (value / time_in_days) depend from other flag (by def use last criteria value)                                                                                                        |
| 128   | `0x0080` | ACHIEVEMENT_FLAG_BAR               | Show as progress bar (value / max vale) depend from other flag (by def use last criteria value)                                                                                                             |
| 256   | `0x0100` | ACHIEVEMENT_FLAG_REALM_FIRST_REACH | Realm first achievement for reaching something, for example a level ([cmangos](https://github.com/cmangos/mangos-wotlk/blob/master/src/game/Server/DBCEnums.h) also names it ACHIEVEMENT_FLAG_SERVER_FIRST) |
| 512   | `0x0200` | ACHIEVEMENT_FLAG_REALM_FIRST_KILL  | Realm first achievement for a kill                                                                                                                                                                          |

### IconID

ID from SpellIcon.dbc of the achievement's icon. Not used by the core.

### Reward\_Lang

`Reward_Lang_enUS` to `Reward_Lang_Unk` and `Reward_Lang_Mask`. The reward text, for example "Reward: Title - Explorer". Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Reward_Lang_enUS` = enUS, `Reward_Lang_enGB` = koKR, `Reward_Lang_koKR` = frFR, `Reward_Lang_frFR` = deDE, `Reward_Lang_deDE` = zhCN, `Reward_Lang_enCN` = zhTW, `Reward_Lang_zhCN` = esES, `Reward_Lang_enTW` = esMX, `Reward_Lang_zhTW` = ruRU. The remaining text columns, `Reward_Lang_esES` to `Reward_Lang_Unk`, are not supported in 3.3.5a and are not used.

### Minimum\_Criteria

Number of criteria that must be completed to earn the achievement. 0 means all criteria.

### Shares\_Criteria

ID of another achievement whose criteria this achievement uses. 0 if the achievement has its own criteria.

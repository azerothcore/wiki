# item\_template

[<-返回至:World](database-world)

**表结构**

保存游戏中每个物品的信息。所有物品都由存储在此表中的模板创建。

（更多信息请参见 *ItemPrototype.h* 文件。）

| Field                           | Type         | Attributes | Key | Null | Default | extra | Comment             |
| ------------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------------- |
| [entry][1]                      | MEDIUMINT    | UNSIGNED   | PRI | NO   | 0       |       |                     |
| [class][2]                      | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [subclass][3]                   | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [SoundOverrideSubclass][4]      | TINYINT      | SIGNED     |     | NO   | -1      |       |                     |
| [name][5]                       | VARCHAR(255) | SIGNED     |     | NO   | NULL    |       |                     |
| [displayid][6]                  | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [Quality][7]                    | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [Flags][8]                      | BIGINT       | SIGNED     |     | NO   | 0       |       |                     |
| [FlagsExtra][9]                 | INT          | UNSIGNED   |     | NO   | 0       |       |                     |
| [BuyCount][10]                  | TINYINT      | UNSIGNED   |     | NO   | 1       |       |                     |
| [BuyPrice][11]                  | BIGINT       | SIGNED     |     | NO   | 0       |       |                     |
| [SellPrice][12]                 | INT          | UNSIGNED   |     | NO   | 0       |       |                     |
| [InventoryType][13]             | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [AllowableClass][14]            | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [AllowableRace][15]             | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [ItemLevel][16]                 | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [RequiredLevel][17]             | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [RequiredSkill][18]             | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [RequiredSkillRank][19]         | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [requiredspell][20]             | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [requiredhonorrank][21]         | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [RequiredCityRank][22]          | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [RequiredReputationFaction][23] | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [RequiredReputationRank][24]    | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [maxcount][25]                  | INT          | SIGNED     |     | NO   | 0       |       |                     |
| [stackable][26]                 | INT          | SIGNED     |     | NO   | 1       |       |                     |
| [ContainerSlots][27]            | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_type1][28]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value1][29]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type2][30]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value2][31]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type3][32]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value3][33]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type4][34]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value4][35]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type5][36]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value5][37]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type6][38]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value6][39]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type7][40]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value7][41]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type8][42]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value8][43]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type9][44]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value9][45]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type10][46]               | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value10][47]              | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [ScalingStatDistribution][48]   | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [ScalingStatValue][49]          | INT          | UNSIGNED   |     | NO   | 0       |       |                     |
| [dmg_min1][50]                  | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [dmg_max1][51]                  | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [dmg_type1][52]                 | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [dmg_min2][53]                  | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [dmg_max2][54]                 | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [dmg_type2][55]                 | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [armor][56]                     | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [holy_res][57]                  | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [fire_res][58]                  | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [nature_res][59]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [frost_res][60]                 | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [shadow_res][61]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [arcane_res][62]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [delay][63]                     | SMALLINT     | UNSIGNED   |     | NO   | 1000    |       |                     |
| [ammo_type][64]                 | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [RangedModRange][65]            | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [spellid_1][66]                 | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [spelltrigger_1][67]            | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcharges_1][68]            | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [spellppmRate_1][69]            | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [spellcooldown_1][70]           | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellcategory_1][71]           | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcategorycooldown_1][72]   | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellid_2][73]                 | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [spelltrigger_2][74]            | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcharges_2][75]            | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [spellppmRate_2][76]            | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [spellcooldown_2][77]           | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellcategory_2][78]           | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcategorycooldown_2][79]   | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellid_3][80]                 | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [spelltrigger_3][81]            | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcharges_3][82]            | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [spellppmRate_3][83]            | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [spellcooldown_3][84]           | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellcategory_3][85]           | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcategorycooldown_3][86]   | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellid_4][87]                 | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [spelltrigger_4][88]            | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcharges_4][89]            | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [spellppmRate_4][90]            | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [spellcooldown_4][91]           | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellcategory_4][92]           | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcategorycooldown_4][93]   | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellid_5][94]                 | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [spelltrigger_5][95]            | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcharges_5][96]            | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [spellppmRate_5][97]            | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [spellcooldown_5][98]           | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellcategory_5][99]           | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcategorycooldown_5][100]  | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [bonding][101]                  | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [description][102]              | VARCHAR(255) | SIGNED     |     | NO   | NULL    |       |                     |
| [PageText][103]                 | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [LanguageID][104]               | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [PageMaterial][105]             | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [startquest][106]               | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [lockid][107]                   | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [Material][108]                 | TINYINT      | SIGNED     |     | NO   | 0       |       |                     |
| [sheath][109]                   | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [RandomProperty][110]           | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [RandomSuffix][111]             | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [block][112]                    | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [itemset][113]                  | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [MaxDurability][114]            | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [area][115]                     | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [Map][116]                      | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [BagFamily][117]                | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [TotemCategory][118]            | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [socketColor_1][119]            | TINYINT      | SIGNED     |     | NO   | 0       |       |                     |
| [socketContent_1][120]          | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [socketColor_2][121]            | TINYINT      | SIGNED     |     | NO   | 0       |       |                     |
| [socketContent_2][122]          | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [socketColor_3][123]            | TINYINT      | SIGNED     |     | NO   | 0       |       |                     |
| [socketContent_3][124]          | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [socketBonus][125]              | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [GemProperties][126]            | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [RequiredDisenchantSkill][127]  | SMALLINT     | SIGNED     |     | NO   | -1      |       |                     |
| [ArmorDamageModifier][128]      | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [duration][129]                 | INT          | UNSIGNED   |     | NO   | 0       |       | 以秒为单位的持续时间 |
| [ItemLimitCategory][130]        | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [HolidayId][131]                | INT          | UNSIGNED   |     | NO   | 0       |       |                     |
| [ScriptName][132]               | VARCHAR(64)  | SIGNED     |     | NO   | NULL    |       |                     |
| [DisenchantID][133]             | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [FoodType][134]                 | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [minMoneyLoot][135]             | INT          | UNSIGNED   |     | NO   | 0       |       |                     |
| [maxMoneyLoot][136]             | INT          | UNSIGNED   |     | NO   | 0       |       |                     |
| [flagsCustom][137]              | INT          | UNSIGNED   |     | NO   | 0       |       |                     |
| [VerifiedBuild][138]            | SMALLINT     | SIGNED     |     | YES  | 1       |       | (WDBVerified)       |

[1]: #entry
[2]: #class
[3]: #subclass
[4]: #soundoverridesubclass
[5]: #name
[6]: #displayid
[7]: #quality
[8]: #flags
[9]: #flagsextra
[10]: #buycount
[11]: #buyprice
[12]: #sellprice
[13]: #inventorytype
[14]: #allowableclass
[15]: #allowablerace
[16]: #itemlevel
[17]: #requiredlevel
[18]: #requiredskill
[19]: #requiredskillrank
[20]: #requiredspell
[21]: #requiredhonorrank
[22]: #requiredcityrank
[23]: #requiredreputationfaction
[24]: #requiredreputationrank
[25]: #maxcount
[26]: #stackable
[27]: #containerslots
[28]: #stat_type1
[29]: #stat_value1
[30]: #stat_type2
[31]: #stat_value2
[32]: #stat_type3
[33]: #stat_value3
[34]: #stat_type4
[35]: #stat_value4
[36]: #stat_type5
[37]: #stat_value5
[38]: #stat_type6
[39]: #stat_value6
[40]: #stat_type7
[41]: #stat_value7
[42]: #stat_type8
[43]: #stat_value8
[44]: #stat_type9
[45]: #stat_value9
[46]: #stat_type10
[47]: #stat_value10
[48]: #scalingstatdistribution
[49]: #scalingstatvalue
[50]: #dmg_min1
[51]: #dmg_max1
[52]: #dmg_type1
[53]: #dmg_min2
[54]: #dmg_max2
[55]: #dmg_type2
[56]: #armor
[57]: #holyres
[58]: #fireres
[59]: #natureres
[60]: #frostres
[61]: #shadowres
[62]: #arcaneres
[63]: #delay
[64]: #ammotype
[65]: #rangedmodrange
[66]: #spellid_1
[67]: #spelltrigger_1
[68]: #spellcharges_1
[69]: #spellppmrate_1
[70]: #spellcooldown_1
[71]: #spellcategory_1
[72]: #spellcategorycooldown_1
[73]: #spellid_2
[74]: #spelltrigger_2
[75]: #spellcharges_2
[76]: #spellppmrate_2
[77]: #spellcooldown_2
[78]: #spellcategory_2
[79]: #spellcategorycooldown_2
[80]: #spellid_3
[81]: #spelltrigger_3
[82]: #spellcharges_3
[83]: #spellppmrate_3
[84]: #spellcooldown_3
[85]: #spellcategory_3
[86]: #spellcategorycooldown_3
[87]: #spellid_4
[88]: #spelltrigger_4
[89]: #spellcharges_4
[90]: #spellppmrate_4
[91]: #spellcooldown_4
[92]: #spellcategory_4
[93]: #spellcategorycooldown_4
[94]: #spellid_5
[95]: #spelltrigger_5
[96]: #spellcharges_5
[97]: #spellppmrate_5
[98]: #spellcooldown_5
[99]: #spellcategory_5
[100]: #spellcategorycooldown_5
[101]: #bonding
[102]: #description
[103]: #pagetext
[104]: #languageid
[105]: #pagematerial
[106]: #startquest
[107]: #lockid
[108]: #material
[109]: #sheath
[110]: #randomproperty
[111]: #randomsuffix
[112]: #block
[113]: #itemset
[114]: #maxdurability
[115]: #area
[116]: #map
[117]: #bagfamily
[118]: #totemcategory
[119]: #socketcolor_1
[120]: #socketcontent_1
[121]: #socketcolor_2
[122]: #socketcontent_2
[123]: #socketcolor_3
[124]: #socketcontent_3
[125]: #socketbonus
[126]: #gemproperties
[127]: #requireddisenchantskill
[128]: #armordamagemodifier
[129]: #duration
[130]: #itemlimitcategory
[131]: #holidayid
[132]: #scriptname
[133]: #disenchantid
[134]: #foodtype
[135]: #minmoneyloot
[136]: #maxmoneyloot
[137]: #flagscustom
[138]: #verifiedbuild

**字段说明**

### entry

物品的唯一 ID。

### class

| ID  | Name                |
| --- | ------------------- |
| 0   | Consumable          |
| 1   | Container           |
| 2   | Weapon              |
| 3   | Gem                 |
| 4   | Armor               |
| 5   | Reagent             |
| 6   | Projectile          |
| 7   | Trade Goods         |
| 8   | Generic(OBSOLETE)   |
| 9   | Recipe              |
| 10  | Money(OBSOLETE)     |
| 11  | Quiver              |
| 12  | Quest               |
| 13  | Key                 |
| 14  | Permanent(OBSOLETE) |
| 15  | Miscellaneous       |
| 16  | Glyph               |

### subclass

下表列出了所有可用的子类与职业组合以及子类名称。

| Class ID | Subclass ID | Subclass Name      | Comments                                              |
| -------- | ----------- | ------------------ | ----------------------------------------------------- |
| 0        | 0           | Consumable         | 是否可在战斗中使用由所分配的法术决定。                |
| 0        | 1           | Potion             |                                                       |
| 0        | 2           | Elixir             |                                                       |
| 0        | 3           | Flask              |                                                       |
| 0        | 4           | Scroll             |                                                       |
| 0        | 5           | Food & Drink       |                                                       |
| 0        | 6           | Item Enhancement   |                                                       |
| 0        | 7           | Bandage            |                                                       |
| 0        | 8           | Other              |                                                       |
| 1        | 0           | Bag                |                                                       |
| 1        | 1           | Soul Bag           |                                                       |
| 1        | 2           | Herb Bag           |                                                       |
| 1        | 3           | Enchanting Bag     |                                                       |
| 1        | 4           | Engineering Bag    |                                                       |
| 1        | 5           | Gem Bag            |                                                       |
| 1        | 6           | Mining Bag         |                                                       |
| 1        | 7           | Leatherworking Bag |                                                       |
| 1        | 8           | Inscription Bag    |                                                       |
| 2        | 0           | Axe                | 单手                                                  |
| 2        | 1           | Axe                | 双手                                                  |
| 2        | 2           | Bow                |                                                       |
| 2        | 3           | Gun                |                                                       |
| 2        | 4           | Mace               | 单手                                                  |
| 2        | 5           | Mace               | 双手                                                  |
| 2        | 6           | Polearm            |                                                       |
| 2        | 7           | Sword              | 单手                                                  |
| 2        | 8           | Sword              | 双手                                                  |
| 2        | 9           | Obsolete           |                                                       |
| 2        | 10          | Staff              |                                                       |
| 2        | 11          | Exotic             |                                                       |
| 2        | 12          | Exotic             |                                                       |
| 2        | 13          | Fist Weapon        |                                                       |
| 2        | 14          | Miscellaneous      | （锻造锤、采矿镐等）                                   |
| 2        | 15          | Dagger             |                                                       |
| 2        | 16          | Thrown             |                                                       |
| 2        | 17          | Spear              |                                                       |
| 2        | 18          | Crossbow           |                                                       |
| 2        | 19          | Wand               |                                                       |
| 2        | 20          | Fishing Pole       |                                                       |
| 3        | 0           | Red                |                                                       |
| 3        | 1           | Blue               |                                                       |
| 3        | 2           | Yellow             |                                                       |
| 3        | 3           | Purple             |                                                       |
| 3        | 4           | Green              |                                                       |
| 3        | 5           | Orange             |                                                       |
| 3        | 6           | Meta               |                                                       |
| 3        | 7           | Simple             |                                                       |
| 3        | 8           | Prismatic          |                                                       |
| 4        | 0           | Miscellaneous      |                                                       |
| 4        | 1           | Cloth              |                                                       |
| 4        | 2           | Leather            |                                                       |
| 4        | 3           | Mail               |                                                       |
| 4        | 4           | Plate              |                                                       |
| 4        | 5           | Buckler(OBSOLETE)  |                                                       |
| 4        | 6           | Shield             |                                                       |
| 4        | 7           | Libram             |                                                       |
| 4        | 8           | Idol               |                                                       |
| 4        | 9           | Totem              |                                                       |
| 4        | 10          | Sigil              |                                                       |
| 5        | 0           | Reagent            |                                                       |
| 6        | 0           | Wand(OBSOLETE)     |                                                       |
| 6        | 1           | Bolt(OBSOLETE)     |                                                       |
| 6        | 2           | Arrow              |                                                       |
| 6        | 3           | Bullet             |                                                       |
| 6        | 4           | Thrown(OBSOLETE)   |                                                       |
| 7        | 0           | Trade Goods        |                                                       |
| 7        | 1           | Parts              |                                                       |
| 7        | 2           | Explosives         |                                                       |
| 7        | 3           | Devices            |                                                       |
| 7        | 4           | Jewelcrafting      |                                                       |
| 7        | 5           | Cloth              |                                                       |
| 7        | 6           | Leather            |                                                       |
| 7        | 7           | Metal & Stone      |                                                       |
| 7        | 8           | Meat               |                                                       |
| 7        | 9           | Herb               |                                                       |
| 7        | 10          | Elemental          |                                                       |
| 7        | 11          | Other              |                                                       |
| 7        | 12          | Enchanting         |                                                       |
| 7        | 13          | Materials          |                                                       |
| 7        | 14          | Armor Enchantment  |                                                       |
| 7        | 15          | Weapon Enchantment |                                                       |
| 8        | 0           | Generic(OBSOLETE)  |                                                       |
| 9        | 0           | Book               |                                                       |
| 9        | 1           | Leatherworking     |                                                       |
| 9        | 2           | Tailoring          |                                                       |
| 9        | 3           | Engineering        |                                                       |
| 9        | 4           | Blacksmithing      |                                                       |
| 9        | 5           | Cooking            |                                                       |
| 9        | 6           | Alchemy            |                                                       |
| 9        | 7           | First Aid          |                                                       |
| 9        | 8           | Enchanting         |                                                       |
| 9        | 9           | Fishing            |                                                       |
| 9        | 10          | Jewelcrafting      |                                                       |
| 10       | 0           | Money(OBSOLETE)    |                                                       |
| 11       | 0           | Quiver(OBSOLETE)   |                                                       |
| 11       | 1           | Quiver(OBSOLETE)   |                                                       |
| 11       | 2           | Quiver             | 可容纳箭矢                                              |
| 11       | 3           | Ammo Pouch         | 可容纳子弹                                              |
| 12       | 0           | Quest              |                                                       |
| 13       | 0           | Key                |                                                       |
| 13       | 1           | Lockpick           |                                                       |
| 14       | 0           | Permanent          |                                                       |
| 15       | 0           | Junk               |                                                       |
| 15       | 1           | Reagent            |                                                       |
| 15       | 2           | Pet                |                                                       |
| 15       | 3           | Holiday            |                                                       |
| 15       | 4           | Other              |                                                       |
| 15       | 5           | Mount              |                                                       |
| 16       | 1           | Warrior            |                                                       |
| 16       | 2           | Paladin            |                                                       |
| 16       | 3           | Hunter             |                                                       |
| 16       | 4           | Rogue              |                                                       |
| 16       | 5           | Priest             |                                                       |
| 16       | 6           | Death Knight       |                                                       |
| 16       | 7           | Shaman             |                                                       |
| 16       | 8           | Mage               |                                                       |
| 16       | 9           | Warlock            |                                                       |
| 16       | 11          | Druid              |                                                       |

### SoundOverrideSubclass

武器在命中时会有特殊的音效。此列用于通过指定另一个子类来覆盖这些音效。

例如，一个杂项（misc）子类的物品可以通过在此覆盖子类，使其命中时听起来像法杖。

### name

物品的名称。

### displayid

物品的模型 ID。每个模型都有其分配的图标，因此此字段同时控制模型外观和图标。

### Quality

物品的品质。

| ID  | Color  | Quality                                   |
| --- | ------ | ----------------------------------------- |
| 0   | Grey   | Poor                                      |
| 1   | White  | Common                                    |
| 2   | Green  | Uncommon                                  |
| 3   | Blue   | Rare                                      |
| 4   | Purple | Epic                                      |
| 5   | Orange | Legendary                                 |
| 6   | Red    | Artifact                                  |
| 7   | Gold   | Heirlooms (or some Bind to Account items) |

### Flags

包含物品所具有的标志的位掩码字段。与所有其他此类字段一样，只需将各标志值相加即可组合它们。可能的标志如下所列。

| Flag       | Bit        | Name                             | Comment                                                                                                                              |
| ---------- | ---------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| 0x01       | 1          | ITEM_FLAG_NO_PICKUP              | （尚未实现）                                                                                                                         |
| 0x02       | 2          |                                  | 召唤（Conjured）物品                                                                                                                 |
| 0x04       | 4          |                                  | 可打开（可通过右键单击打开）                                                                                                         |
| 0x08       | 8          | ITEM_FLAG_HEROIC_TOOLTIP         | （尚未实现）- 使物品上出现绿色"英雄"（Heroic）文字                                                                                    |
| 0x10       | 16         | ITEM_FLAG_DEPRECATED             | （尚未实现）- 已废弃物品                                                                                                             |
| 0x20       | 32         |                                  | 物品无法被摧毁，除非通过使用法术（物品可以作为法术的材料）                                                                          |
| 0x40       | 64         | ITEM_FLAG_PLAYERCAST             | （尚未实现）- 物品的法术可由玩家施放                                                                                                |
| 0x80       | 128        | ITEM_FLAG_NO_EQUIP_COOLDOWN      |                                                                                                                                      |
| 0x0100     | 256        | ITEM_FLAG_MULTI_LOOT_QUEST       | （尚未实现）                                                                                                                         |
| 0x0200     | 512        |                                  | 包装物：物品可以包装其他物品                                                                                                         |
| 0x0400     | 1024       | ITEM_FLAG_USES_RESOURCES         | （尚未实现）                                                                                                                         |
| 0x0800     | 2048       |                                  | 物品是队伍掉落，所有人都可以拾取                                                                                                     |
| 0x01000    | 4096       |                                  | 物品可退款                                                                                                                           |
| 0x02000    | 8192       |                                  | 契约（竞技场或公会）                                                                                                                 |
| 0x04000    | 16384      | ITEM_FLAG_HAS_TEXT               | （尚未实现）- 只有可读物品具有此标志（但并非全部）                                                                                    |
| 0x08000    | 32768      | ITEM_FLAG_NO_DISENCHANT          | （尚未实现）- 如果启用，则禁止分解。在另一列 `RequiredDisenchantSkill` 中实现                                                      |
| 0x010000   | 65536      | ITEM_FLAG_REAL_DURATION          | （尚未实现）- 可能是真实时间持续时间。在另一列 `flagsCustom` 中实现                                                                 |
| 0x020000   | 131072     | ITEM_FLAG_NO_CREATOR             | （尚未实现或部分实现）- 可能是为了移除制作/召唤物品上的"由 XX 制作"消息，或用于签署契约                                          |
| 0x040000   | 262144     |                                  | 物品可以被选矿（prospected）                                                                                                        |
| 0x080000   | 524288     |                                  | 唯一装备（玩家同一时间只能装备一个，但背包中可以有任意多个；如果 maxcount = 1，仍会显示唯一装备）                                  |
| 0x0100000  | 1048576    | ITEM_FLAG_IGNORE_FOR_AURAS       | （尚未实现）- ??                                                                                                                    |
| 0x0200000  | 2097152    |                                  | 物品可以在竞技场比赛中使用                                                                                                           |
| 0x0400000  | 4194304    |                                  | 可投掷（用于游戏内提示）                                                                                                             |
| 0x0800000  | 8388608    |                                  | 物品可以在变形状态下使用                                                                                                             |
| 0x01000000 | 16777216   | ITEM_FLAG_HAS_QUEST_GLOW         | （尚未实现）                                                                                                                         |
| 0x02000000 | 33554432   |                                  | 专业配方：只有在你满足要求且尚未学会时才可拾取                                                                                       |
| 0x04000000 | 67108864   |                                  | 物品不能在竞技场中使用                                                                                                               |
| 0x08000000 | 134217728  |                                  | 账号绑定（需要设置 Bonding > 0）                                                                                                     |
| 0x10000000 | 268435456  | ITEM_FLAG_NO_REAGENT_COST        | 法术以触发标志施放（在代码中写作 `Spell is cast ignoring reagents`）                                                                |
| 0x20000000 | 536870912  |                                  | 可研磨（Millable）                                                                                                                   |
| 0x40000000 | 1073741824 | ITEM_FLAG_REPORT_TO_GUILD_CHAT   | （尚未实现）                                                                                                                         |
| 0x80000000 | 2147483648 | ITEM_FLAG_NO_PROGRESSIVE_LOOT    | （尚未实现）                                                                                                                         |

### FlagsExtra

| Flag       | Bit        | Name                                                | Comment                                 |
| ---------- | ---------- | --------------------------------------------------- | --------------------------------------- |
| 0x00000001 | 1          | ITEM_FLAG2_FACTION_HORDE                            | 仅限部落                                |
| 0x00000002 | 2          | ITEM_FLAG2_FACTION_ALLIANCE                         | 仅限联盟                                |
| 0x00000004 | 4          | ITEM_FLAG2_DONT_IGNORE_BUY_PRICE                    | 当物品在 npc_vendor 中使用 ExtendedCost 时，同时还需要金币 |
| 0x00000008 | 8          | ITEM_FLAG2_CLASSIFY_AS_CASTER                       | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x00000010 | 16         | ITEM_FLAG2_CLASSIFY_AS_PHYSICAL                     | 尚未实现（NYI）                         |
| 0x00000020 | 32         | ITEM_FLAG2_EVERYONE_CAN_ROLL_NEED                   | 任何人都可以掷需求（need）              |
| 0x00000040 | 64         | ITEM_FLAG2_NO_TRADE_BIND_ON_ACQUIRE                 | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x00000080 | 128        | ITEM_FLAG2_CAN_TRADE_BIND_ON_ACQUIRE                | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x00000100 | 256        | ITEM_FLAG2_CAN_ONLY_ROLL_GREED                      | 使此物品的需求（need）掷骰被禁用        |
| 0x00000200 | 512        | ITEM_FLAG2_CASTER_WEAPON                            | 尚未实现（NYI）                         |
| 0x00000400 | 1024       | ITEM_FLAG2_DELETE_ON_LOGIN                          | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x00000800 | 2048       | ITEM_FLAG2_INTERNAL_ITEM                            | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x00001000 | 4096       | ITEM_FLAG2_NO_VENDOR_VALUE                          | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x00002000 | 8192       | ITEM_FLAG2_SHOW_BEFORE_DISCOVERED                   | 尚未实现（NYI）                         |
| 0x00004000 | 16384      | ITEM_FLAG2_OVERRIDE_GOLD_COST                       | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x00008000 | 32768      | ITEM_FLAG2_IGNORE_DEFAULT_RATED_BG_RESTRICTIONS     | 尚未实现（NYI）                         |
| 0x00010000 | 65536      | ITEM_FLAG2_NOT_USABLE_IN_RATED_BG                   | 尚未实现（NYI）                         |
| 0x00020000 | 131072     | ITEM_FLAG2_BNET_ACCOUNT_TRADE_OK                    | 尚未实现（NYI）                         |
| 0x00040000 | 262144     | ITEM_FLAG2_CONFIRM_BEFORE_USE                       | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x00080000 | 524288     | ITEM_FLAG2_REEVALUATE_BONDING_ON_TRANSFORM          | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x00100000 | 1048576    | ITEM_FLAG2_NO_TRANSFORM_ON_CHARGE_DEPLETION         | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x00200000 | 2097152    | ITEM_FLAG2_NO_ALTER_ITEM_VISUAL                     | 尚未实现（NYI）                         |
| 0x00400000 | 4194304    | ITEM_FLAG2_NO_SOURCE_FOR_ITEM_VISUAL                | 尚未实现（NYI）                         |
| 0x00800000 | 8388608    | ITEM_FLAG2_IGNORE_QUALITY_FOR_ITEM_VISUAL_SOURCE    | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x01000000 | 16777216   | ITEM_FLAG2_NO_DURABILITY                            | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x02000000 | 33554432   | ITEM_FLAG2_ROLE_TANK                                | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x04000000 | 67108864   | ITEM_FLAG2_ROLE_HEALER                              | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x08000000 | 134217728  | ITEM_FLAG2_ROLE_DAMAGE                              | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x10000000 | 268435456  | ITEM_FLAG2_CAN_DROP_IN_CHALLENGE_MODE               | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x20000000 | 536870912  | ITEM_FLAG2_NEVER_STACK_IN_LOOT_UI                   | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x40000000 | 1073741824 | ITEM_FLAG2_DISENCHANT_TO_LOOT_TABLE                 | 尚未实现（NYI）- 在 item_template 中未使用 |
| 0x80000000 | 2147483648 | ITEM_FLAG2_USED_IN_A_TRADESKILL                     | 尚未实现（NYI）- 在 item_template 中未使用 |

### BuyCount

商人出售该物品时的堆叠数量。此外，如果商人的此物品库存有限，每次刷新商人列表（参见 [npc\_vendor.incrtime](http://www.azerothcore.org/wiki/npc_vendor#incrtime)）时，库存数量都会按此数值增加。

### BuyPrice

从商人处购买此物品所需支付的价钱，以铜币为单位。

### SellPrice

当你出售物品且该物品可以出售时，商人愿意支付的价钱，以铜币为单位。如果物品无法出售给商人，则填写 0。

### InventoryType

该物品将被装备在哪个槽位。

| ID  | Slot Name                                                                                                                              |
| --- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 0   | Non equipable                                                                                                                          |
| 1   | Head                                                                                                                                   |
| 2   | Neck                                                                                                                                   |
| 3   | Shoulder                                                                                                                               |
| 4   | Shirt                                                                                                                                  |
| 5   | Chest (see also Robe = 20)                                                                                                             |
| 6   | Waist                                                                                                                                  |
| 7   | Legs                                                                                                                                   |
| 8   | Feet                                                                                                                                   |
| 9   | Wrists                                                                                                                                 |
| 10  | Hands                                                                                                                                  |
| 11  | Finger                                                                                                                                 |
| 12  | Trinket                                                                                                                                |
| 13  | One-Hand (not to confuse with Off-Hand = 22)                                                                                           |
| 14  | Shield (class = armor, not weapon even if in weapon slot)                                                                              |
| 15  | Ranged (Bows) (see also Ranged right = 26)                                                                                             |
| 16  | Back                                                                                                                                   |
| 17  | Two-Hand                                                                                                                               |
| 18  | Bag                                                                                                                                    |
| 19  | Tabard                                                                                                                                 |
| 20  | Robe (see also Chest = 5)                                                                                                              |
| 21  | Main hand                                                                                                                              |
| 22  | Off Hand weapons (see also One-Hand = 13)                                                                                              |
| 23  | Held in Off-Hand (tome, cane, flowers, torches, orbs etc... See also Off-Hand = 22) (class = armor, not weapon even if in weapon slot) |
| 24  | Ammo                                                                                                                                   |
| 25  | Thrown                                                                                                                                 |
| 26  | Ranged right (Wands, Guns) (see also Ranged = 15)                                                                                      |
| 27  | Quiver                                                                                                                                 |
| 28  | Relic (class = armor, not weapon even if in weapon slot)                                                                               

### AllowableClass

控制哪些职业可以使用此物品的位掩码。将各 ID 相加即可组合职业选项。如果所有职业都可以使用，则使用 -1。

职业的 ID 请参见 [ChrClasses DBC 文件](chrclasses)。

### AllowableRace

控制哪些种族可以使用此物品的位掩码。将各 ID 相加即可组合种族选项。所有种族可用时使用 -1。

种族的 ID 请参见 [ChrRaces DBC 文件](chrraces)。

### ItemLevel

基础物品等级。

### RequiredLevel

玩家装备该物品所需达到的等级。

### RequiredSkill

使用此物品所需的技能。可在此处使用的 ID 请参见 [SkillLine DBC 文件](skillline)。

### RequiredSkillRank

玩家使用此物品所需拥有的技能等级。

### requiredspell

玩家使用此物品所需学会的法术。

### requiredhonorrank

玩家使用此物品所需拥有的军衔。

### RequiredCityRank

其用途未知。所有物品均为 0。

### RequiredReputationFaction

玩家需要与之建立一定声望等级的阵营的阵营模板 ID。如果此值为 0，则使用物品出售者的阵营。

所有阵营的 ID 请参见 [Faction DBC 文件](faction)。

### RequiredReputationRank

玩家需要与 [RequiredReputationFaction](#requiredreputationfaction) 中的阵营达到的声望等级。

| ID  | Rank       |
| --- | ---------- |
| 0   | Hated      |
| 1   | Hostile    |
| 2   | Unfriendly |
| 3   | Neutral    |
| 4   | Friendly   |
| 5   | Honored    |
| 6   | Revered    |
| 7   | Exalted    |

### maxcount

玩家可以拥有的此物品的最大数量。使用 0 表示无限。

### stackable

可以堆叠在同一槽位中的此物品数量。

### ContainerSlots

如果物品是背包，此字段控制背包拥有的槽位数。

### stat\_type

要修改的属性类型。

| ID  | Stat Type                                        |
| --- | ------------------------------------------------ |
| 0   | ITEM_MOD_MANA                                    |
| 1   | ITEM_MOD_HEALTH                                  |
| 3   | ITEM_MOD_AGILITY                                 |
| 4   | ITEM_MOD_STRENGTH                                |
| 5   | ITEM_MOD_INTELLECT                               |
| 6   | ITEM_MOD_SPIRIT                                  |
| 7   | ITEM_MOD_STAMINA                                 |
| 12  | ITEM_MOD_DEFENSE_SKILL_RATING                    |
| 13  | ITEM_MOD_DODGE_RATING                            |
| 14  | ITEM_MOD_PARRY_RATING                            |
| 15  | ITEM_MOD_BLOCK_RATING                            |
| 16  | ITEM_MOD_HIT_MELEE_RATING                        |
| 17  | ITEM_MOD_HIT_RANGED_RATING                       |
| 18  | ITEM_MOD_HIT_SPELL_RATING                        |
| 19  | ITEM_MOD_CRIT_MELEE_RATING                       |
| 20  | ITEM_MOD_CRIT_RANGED_RATING                      |
| 21  | ITEM_MOD_CRIT_SPELL_RATING                       |
| 22  | ITEM_MOD_HIT_TAKEN_MELEE_RATING                  |
| 23  | ITEM_MOD_HIT_TAKEN_RANGED_RATING                 |
| 24  | ITEM_MOD_HIT_TAKEN_SPELL_RATING                  |
| 25  | ITEM_MOD_CRIT_TAKEN_MELEE_RATING                 |
| 26  | ITEM_MOD_CRIT_TAKEN_RANGED_RATING                |
| 27  | ITEM_MOD_CRIT_TAKEN_SPELL_RATING                 |
| 28  | ITEM_MOD_HASTE_MELEE_RATING                      |
| 29  | ITEM_MOD_HASTE_RANGED_RATING                     |
| 30  | ITEM_MOD_HASTE_SPELL_RATING                      |
| 31  | ITEM_MOD_HIT_RATING                              |
| 32  | ITEM_MOD_CRIT_RATING                             |
| 33  | ITEM_MOD_HIT_TAKEN_RATING                        |
| 34  | ITEM_MOD_CRIT_TAKEN_RATING                       |
| 35  | ITEM_MOD_RESILIENCE_RATING                       |
| 36  | ITEM_MOD_HASTE_RATING                            |
| 37  | ITEM_MOD_EXPERTISE_RATING                        |
| 38  | ITEM_MOD_ATTACK_POWER                            |
| 39  | ITEM_MOD_RANGED_ATTACK_POWER                     |
| 40  | ITEM_MOD_FERAL_ATTACK_POWER (not used as of 3.3) |
| 41  | ITEM_MOD_SPELL_HEALING_DONE                      |
| 42  | ITEM_MOD_SPELL_DAMAGE_DONE                       |
| 43  | ITEM_MOD_MANA_REGENERATION                       |
| 44  | ITEM_MOD_ARMOR_PENETRATION_RATING                |
| 45  | ITEM_MOD_SPELL_POWER                             |
| 46  | ITEM_MOD_ HEALTH_REGEN                           |
| 47  | ITEM_MOD_SPELL_PENETRATION                       |
| 48  | ITEM_MOD_BLOCK_VALUE                             |

### stat\_value

要将属性类型改为的值。

### ScalingStatDistribution

与静态属性类似，这些属性会随着使用者等级的增长而增长（主要是传家宝练级装备）。用法与静态属性相同。

### ScalingStatValue

缩放属性的最终（80 级）值

### dmg\_min

物品的最小伤害。

### dmg\_max

物品的最大伤害。

### dmg\_type

物品所使用的伤害类型。

| ID  | Damage Type |
| --- | ----------- |
| 0   | Physical    |
| 1   | Holy        |
| 2   | Fire        |
| 3   | Nature      |
| 4   | Frost       |
| 5   | Shadow      |
| 6   | Arcane      |

### armor

物品的护甲值。

### holy\_res

神圣抗性。

### fire\_res

火焰抗性。

### nature\_res

自然抗性。

### frost\_res

冰霜抗性。

### shadow\_res

暗影抗性。

### arcane\_res

奥术抗性。

### delay

连续两次命中之间的时间，以毫秒为单位。

### ammo\_type

物品所使用的弹药类型。箭矢 = 2；子弹 = 3

### RangedModRange

弓/枪/弩的射程修正：

默认射程在 0.3 到 0.4 码之间，

所有暴雪的远程武器都有 RangedModRange100

### spellid

物品可以施放或触发的法术的法术 ID。

### spelltrigger

法术的触发类型。

| ID  | Trigger Type      |
| --- | ----------------- |
| 0   | Use               |
| 1   | On Equip          |
| 2   | Chance on Hit     |
| 4   | Soulstone         |
| 5   | Use with no delay |
| 6   | Learn Spell ID    |

### spellcharges

物品可以施放法术的次数。如果为 0，则可以无限次使用。如果为负数，则当次数用尽后，物品也会被删除。如果为正数，则即使所有次数用尽，物品也不会被删除。

### spellppmRate

控制法术触发频率的每分钟触发率（ppm）（当 [\#spelltrigger](#spelltrigger) == 2 时）。

### spellcooldown

特定法术的冷却时间，以毫秒为单位，控制法术可使用的频率。使用 -1 以使用默认法术冷却时间。  
注意：这不是通常出现在如具有"命中时几率"效果的饰品等物品上的触发（proc）的"内部冷却时间"。

### spellcategory

法术所在的类别。你可以从 DBC `SpellCategory.dbc` 中选择一个，或者为你的自定义物品创建一个新的类别（> 1260）。

### spellcategorycooldown

应用于与触发法术同一类别中的所有其他法术的冷却时间，以毫秒为单位。使用 -1 以使用默认法术冷却时间。  
注意：你可以同时设置 `spellcooldown` 和 `spellcategorycooldown`，它们并不互斥。

### bonding

物品的绑定类型。

**注意：** 要使用"账号绑定"（Bind to Account）类型，物品的 `flags` 必须设置为 134217728（最小值），且 `bonding` > 0（例如：1、2、3）。

| ID  | Bonding Type         |
| --- | -------------------- |
| 0   | No bounds            |
| 1   | Binds when picked up |
| 2   | Binds when equipped  |
| 3   | Binds when used      |
| 4   | Quest item           |
| 5   | Quest Item1          |

### description

出现在物品提示信息底部、以橙色字母显示的描述。

### PageText

指向物品将显示文本的 ID（如果它是书或信件等）。该物品在游戏中会显示放大镜光标，右键单击时会显示文本。参见 [page\_text.entry](http://www.azerothcore.org/wiki/page_text#entry)

### LanguageID

物品文本所使用的语言。

所有语言的 ID 请参见 [Languages DBC 文件](languages)。

### PageMaterial

出现在页面文本窗口中的背景纹理。

所有材质类型的 ID 请参见 [PageTextMaterial DBC 文件](pagetextmaterial)。

### startquest

右键单击此物品时将启动的任务的 ID。参见 [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id)

### lockid

此物品（作为钥匙使用）所关联的锁的条目 ID。此字段用于钥匙-门机制。

参见 [Lock DBC 文件](https://wowdev.wiki/DB/Lock)。

### Material

物品的材质。此处的值会影响物品移动时发出的声音。对于食物、材料等消耗品，使用 -1。

| ID  | Material    | Comment                |
| --- | ----------- | ---------------------- |
| -1  | Consumables | 食物、材料等             |
| 0   | Not Defined |                        |
| 1   | Metal       |                        |
| 2   | Wood        |                        |
| 3   | Liquid      |                        |
| 4   | Jewelry     |                        |
| 5   | Chain       |                        |
| 6   | Plate       |                        |
| 7   | Cloth       |                        |
| 8   | Leather     |                        |

### sheath

控制物品如何在角色身上收放。按下 'Z' 快捷键可以收起和拔出你的武器。

| ID  | Type              | Position                                         |
| --- | ----------------- | ------------------------------------------------ |
| 1   | Two Handed Weapon | 斜挎在后背，指向下方。                             |
| 2   | Staff             | 斜挎在后背，指向上方。                             |
| 3   | One Handed        | 在角色腰部的左侧。                                 |
| 4   | Shield            | 在角色背部的中央。                                 |
| 5   | Enchanter's Rod   |                                                  |
| 7   | Off hand          | 在角色腰部的右侧。                                 |

### RandomProperty

此字段中的数字指向 [item\_enchantment\_template.entry](http://www.azerothcore.org/wiki/item_enchantment_template#entry)，并与物品首次出现时附带随机属性的几率相关联。此字段与 [RandomSuffix](#randomsuffix) 字段不能同时为非零值。要么填写其中一个，要么填写另一个。此外，此字段中数字的主要来源是 WDB。

### RandomSuffix

此字段中的数字指向 [item\_enchantment\_template.entry](http://www.azerothcore.org/wiki/item_enchantment_template#entry)，并与物品首次出现时附带随机后缀的几率相关联。此字段与 [RandomProperty](#randomproperty) 字段不能同时为非零值。要么填写其中一个，要么填写另一个。此外，此字段中数字的主要来源是 WDB。

### block

如果物品是盾牌，则为盾牌的格挡几率。

### itemset

此物品所属物品套装的 ID。为了节省你的时间，请注意你不能创造新的物品套装。物品套装在 ItemSet DBC 文件中定义。

### MaxDurability

此物品的最大耐久度。

### area

可以使用此物品的区域的 ID。如果离开该区域，物品将从背包中被删除。

### Map

可以使用此物品的地图的 ID。如果离开该地图，物品将从背包中被删除。

### BagFamily

如果物品是背包，此字段是控制哪些类型的物品可以放入此背包的位掩码。你可以通过将各位数相加来组合不同类型。

| ID    | Bag Family Mask         |
| ----- | ----------------------- |
| 0     | None                    |
| 1     | Arrows                  |
| 2     | Bullets                 |
| 4     | Soul Shards             |
| 8     | Leatherworking Supplies |
| 16    | Inscription Supplies    |
| 32    | Herbs                   |
| 64    | Enchanting Supplies     |
| 128   | Engineering Supplies    |
| 256   | Keys                    |
| 512   | Gems                    |
| 1024  | Mining Supplies         |
| 2048  | Soulbound Equipment     |
| 4096  | Vanity Pets             |
| 8192  | Currency Tokens         |
| 16384 | Quest Items             |

### TotemCategory

与 [TotemCategory DBC 文件](totemcategory) 中的 ID 对应。

| ID  | Name                     |
| --- | ------------------------ |
| 1   | Skinning Knife (OLD)     |
| 2   | Earth Totem              |
| 3   | Air Totem                |
| 4   | Fire Totem               |
| 5   | Water Totem              |
| 6   | Runed Copper Rod         |
| 7   | Runed Silver Rod         |
| 8   | Runed Golden Rod         |
| 9   | Runed Truesilver Rod     |
| 10  | Runed Arcanite Rod       |
| 11  | Mining Pick (OLD)        |
| 12  | Philosopher's Stone      |
| 13  | Blacksmith Hammer (OLD)  |
| 14  | Arclight Spanner         |
| 15  | Gyromatic Micro-Adjustor |
| 21  | Master Totem             |
| 41  | Runed Fel Iron Rod       |
| 62  | Runed Adamantite Rod     |
| 63  | Runed Eternium Rod       |
| 81  | Hollow Quill             |
| 101 | Runed Azurite Rod        |
| 121 | Virtuoso Inking Set      |
| 141 | Drums                    |
| 161 | Gnomish Army Knife       |
| 162 | Blacksmith Hammer        |
| 165 | Mining Pick              |
| 166 | Skinning Knife           |
| 167 | Hammer Pick              |
| 168 | Bladed Pickaxe           |
| 169 | Flint and Tinder         |
| 189 | Runed Cobalt Rod         |
| 190 | Runed Titanium Rod       |

### socketColor

可以插入此物品的插槽的颜色。

| ID  | Color  |
| --- | ------ |
| 1   | Meta   |
| 2   | Red    |
| 4   | Yellow |
| 8   | Blue   |

### socketContent

SocketColor1 颜色的宝石数量

### socketBonus

常用的插槽奖励 ID

| ID   | Effect                     |
| ---- | -------------------------- |
| 3015 | +2 Strength                |
| 2879 | +3 Strength                |
| 2927 | +4 Strength                |
| 3357 | +6 Strength                |
| 3312 | +8 Strength                |
| 3149 | +2 Agility                 |
| 2893 | +3 Agility                 |
| 2877 | +4 Agility                 |
| 3355 | +6 Agility                 |
| 3313 | +8 Agility                 |
| 3164 | +3 Stamina                 |
| 2895 | +4 Stamina                 |
| 2882 | +6 Stamina                 |
| 3307 | +9 Stamina                 |
| 3766 | +12 Stamina                |
| 3016 | +2 Intellect               |
| 2863 | +3 Intellect               |
| 2869 | +4 Intellect               |
| 3310 | +6 Intellect               |
| 3353 | +8 Intellect               |
| 3097 | +2 Spirit                  |
| 2866 | +3 Spirit                  |
| 2890 | +4 Spirit                  |
| 3311 | +6 Spirit                  |
| 3352 | +8 Spirit                  |
| 3114 | +4 Attack Power            |
| 2973 | +6 Attack Power            |
| 2936 | +8 Attack Power            |
| 3764 | +12 Attack Power           |
| 3877 | +16 Attack Power           |
| 1597 | +32 Attack Power           |
| 3153 | +2 Spell Power             |
| 2974 | +4 Spell Power             |
| 3752 | +5 Spell Power             |
| 3602 | +7 Spell Power             |
| 3753 | +9 Spell Power             |
| 2941 | +2 Hit Rating              |
| 2880 | +3 Hit Rating              |
| 2908 | +4 Hit Rating              |
| 3351 | +6 Hit Rating              |
| 2844 | +8 Hit Rating              |
| 3152 | +2 Critical Strike Rating  |
| 3205 | +3 Critical Strike Rating  |
| 3263 | +4 Critical Strike Rating  |
| 3316 | +6 Critical Strike Rating  |
| 3314 | +8 Critical Strike Rating  |
| 3308 | +4 Haste Rating            |
| 3309 | +6 Haste Rating            |
| 3303 | +8 Haste Rating            |
| 3094 | +4 Expertise Rating        |
| 3362 | +6 Expertise Rating        |
| 3778 | +8 Expertise Rating        |
| 3765 | +4 Armor Penetration       |
| 3880 | +6 Armor Penetration       |
| 3882 | +8 Armor Penetration       |
| 2976 | +2 Defense Rating          |
| 2861 | +3 Defense Rating          |
| 2932 | +4 Defense Rating          |
| 3857 | +6 Defense Rating          |
| 3302 | +8 Defense Rating          |
| 2926 | +2 Dodge Rating            |
| 2876 | +3 Dodge Rating            |
| 2871 | +4 Dodge Rating            |
| 3358 | +6 Dodge Rating            |
| 3304 | +8 Dodge Rating            |
| 2907 | +2 Parry Rating            |
| 2870 | +3 Parry Rating            |
| 3359 | +4 Parry Rating            |
| 3871 | +6 Parry Rating            |
| 3360 | +8 Parry Rating            |
| 3017 | +3 Block Rating            |
| 2972 | +4 Block Rating            |
| 3361 | +6 Block Rating            |
| 2975 | +5 Block Value             |
| 2888 | +6 Block Value             |
| 3363 | +9 Block Value             |
| 2881 | +1 Mana per 5 sec          |
| 2865 | +2 Mana per 5 sec          |
| 2370 | +3 Mana per 5 sec          |
| 2371 | +4 Mana per 5 sec          |
| 2392 | +12 Mana per 5 sec         |
| 2867 | +2 Resilience Rating       |
| 2862 | +3 Resilience Rating       |
| 2878 | +4 Resilience Rating       |
| 3600 | +6 Resilience Rating       |
| 3821 | +8 Resilience Rating       |

### GemProperties

此处的值与 GemProperties.dbc 中的 ID 对应。

### RequiredDisenchantSkill

玩家需要拥有的分解熟练度才能分解此物品。
如果设置为 -1，则物品无法被分解。

### ArmorDamageModifier

`field-no-description|76`

### duration

物品的游戏内持续时间，以秒为单位。
如需真实时间，请在 *flagsCustom* 中设置 ITEM\_FLAGS\_CU\_DURATION\_REAL\_TIME。在这种情况下，即使玩家离线，物品持续时间也会继续计时。

### ItemLimitCategory

这与 ItemLimitCategory.dbc 相关。
它是一个定义物品是否属于某个"类别"（如"法力宝石"或"治疗石"）的属性，并定义你在背包中可以拥有该类别物品的数量（即"限制"）。
例如，对于治疗石，有诸如"次级治疗石、强效治疗石等"几种物品，但你的背包中只能携带一个（例如可以查看值 3 或 4）。

### HolidayId

所有节日的 ID 请参见 [Holidays DBC 文件](holidays)。

### ScriptName

物品应使用的脚本的名称。不存在 'internalitemhandler' 或 'internalitemhanler' 脚本，因此 Trinity 会忽略此字段中的任何此类值。

### DisenchantID

分解掉落模板 ID。参见 [disenchant\_loot\_template.entry](http://www.azerothcore.org/wiki/loot_template#loot_template-Entry)

### FoodType

如果此物品是食物类物品，此字段定义它属于哪种食物类型，供想要喂养宠物的猎人使用。它控制该食物属于哪种饮食类别。

注意：生肉和生鱼与普通的肉和鱼不同。似乎最后两种饮食类别包含灰色"粗糙"（poor）类型的食物，玩家没有用处，但某些宠物似乎可以吃。此外，这些食物类型出现在 TBC 中，因此很可能只有 TBC 的宠物才有这些饮食类别。

| ID  | Type     |
| --- | -------- |
| 1   | Meat     |
| 2   | Fish     |
| 3   | Cheese   |
| 4   | Bread    |
| 5   | Fungus   |
| 6   | Fruit    |
| 7   | Raw Meat |
| 8   | Raw Fish |

### minMoneyLoot

如果物品是可以容纳金钱的容器，则此字段定义容器中持有的最小货币量，以铜币为单位。

### maxMoneyLoot

如果物品是可以容纳金钱的容器，则此字段定义容器中持有的最大货币量，以铜币为单位。

### flagsCustom

| Flag       | Bit | Name                              | Comment                                                              |
| ---------- | --- | --------------------------------- | -------------------------------------------------------------------- |
| 0x00000001 | 1   | ITEM_FLAGS_CU_DURATION_REAL_TIME  | 即使玩家离线，物品持续时间也会继续计时                                |
| 0x00000002 | 2   | ITEM_FLAGS_CU_IGNORE_QUEST_STATUS | 当此物品掉落时不会检查任务状态                                        |
| 0x00000004 | 4   | ITEM_FLAGS_CU_FOLLOW_LOOT_RULES   | 物品将始终遵循队伍/队长/需求优先于贪婪的拾取规则                      |

### VerifiedBuild

该字段用于确定模板是否已通过 WDB 文件验证。
- 如果值为 0，则说明尚未解析。
- 如果值大于 0，则说明已使用来自该特定客户端构建的 WDB 文件进行解析。
- 如果值为 -1，则说明在 WDB 中找到正确数据之前，它只是一个占位符。

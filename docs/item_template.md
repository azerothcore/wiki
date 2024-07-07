# item\_template

[<-Back-to:World](database-world)

**Table Structure**

Holds information on every item that exists in the game. All items are created from their template stored in this table.

(See additional information in the *ItemPrototype.h* file.)

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
| [StatsCount][28]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_type1][29]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value1][30]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type2][31]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value2][32]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type3][33]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value3][34]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type4][35]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value4][36]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type5][37]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value5][38]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type6][39]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value6][40]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type7][41]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value7][42]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type8][43]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value8][44]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type9][45]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value9][46]               | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [stat_type10][47]               | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [stat_value10][48]              | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [ScalingStatDistribution][49]   | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [ScalingStatValue][50]          | INT          | UNSIGNED   |     | NO   | 0       |       |                     |
| [dmg_min1][51]                  | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [dmg_max1][52]                  | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [dmg_type1][53]                 | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [dmg_min2][54]                  | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [dmg_max2][55]                  | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [dmg_type2][56]                 | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [armor][57]                     | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [holy_res][58]                  | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [fire_res][59]                  | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [nature_res][60]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [frost_res][61]                 | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [shadow_res][62]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [arcane_res][63]                | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [delay][64]                     | SMALLINT     | UNSIGNED   |     | NO   | 1000    |       |                     |
| [ammo_type][65]                 | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [RangedModRange][66]            | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [spellid_1][67]                 | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [spelltrigger_1][68]            | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcharges_1][69]            | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [spellppmRate_1][70]            | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [spellcooldown_1][71]           | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellcategory_1][72]           | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcategorycooldown_1][73]   | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellid_2][74]                 | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [spelltrigger_2][75]            | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcharges_2][76]            | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [spellppmRate_2][77]            | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [spellcooldown_2][78]           | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellcategory_2][79]           | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcategorycooldown_2][80]   | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellid_3][81]                 | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [spelltrigger_3][82]            | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcharges_3][83]            | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [spellppmRate_3][84]            | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [spellcooldown_3][85]           | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellcategory_3][86]           | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcategorycooldown_3][87]   | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellid_4][88]                 | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [spelltrigger_4][89]            | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcharges_4][90]            | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [spellppmRate_4][91]            | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [spellcooldown_4][92]           | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellcategory_4][93]           | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcategorycooldown_4][94]   | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellid_5][95]                 | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [spelltrigger_5][96]            | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcharges_5][97]            | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [spellppmRate_5][98]            | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [spellcooldown_5][99]           | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [spellcategory_5][100]          | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [spellcategorycooldown_5][101]  | INT          | SIGNED     |     | NO   | -1      |       |                     |
| [bonding][102]                  | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [description][103]              | VARCHAR(255) | SIGNED     |     | NO   | NULL    |       |                     |
| [PageText][104]                 | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [LanguageID][105]               | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [PageMaterial][106]             | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [startquest][107]               | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [lockid][108]                   | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [Material][109]                 | TINYINT      | SIGNED     |     | NO   | 0       |       |                     |
| [sheath][110]                   | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [RandomProperty][111]           | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [RandomSuffix][112]             | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [block][113]                    | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [itemset][114]                  | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [MaxDurability][115]            | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |                     |
| [area][116]                     | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [Map][117]                      | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [BagFamily][118]                | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [TotemCategory][119]            | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [socketColor_1][120]            | TINYINT      | SIGNED     |     | NO   | 0       |       |                     |
| [socketContent_1][121]          | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [socketColor_2][122]            | TINYINT      | SIGNED     |     | NO   | 0       |       |                     |
| [socketContent_2][123]          | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [socketColor_3][124]            | TINYINT      | SIGNED     |     | NO   | 0       |       |                     |
| [socketContent_3][125]          | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [socketBonus][126]              | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [GemProperties][127]            | MEDIUMINT    | SIGNED     |     | NO   | 0       |       |                     |
| [RequiredDisenchantSkill][128]  | SMALLINT     | SIGNED     |     | NO   | -1      |       |                     |
| [ArmorDamageModifier][129]      | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
| [duration][130]                 | INT          | UNSIGNED   |     | NO   | 0       |       | Duration in seconds |
| [ItemLimitCategory][131]        | SMALLINT     | SIGNED     |     | NO   | 0       |       |                     |
| [HolidayId][132]                | INT          | UNSIGNED   |     | NO   | 0       |       |                     |
| [ScriptName][133]               | VARCHAR(64)  | SIGNED     |     | NO   | NULL    |       |                     |
| [DisenchantID][134]             | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |                     |
| [FoodType][135]                 | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                     |
| [minMoneyLoot][136]             | INT          | UNSIGNED   |     | NO   | 0       |       |                     |
| [maxMoneyLoot][137]             | INT          | UNSIGNED   |     | NO   | 0       |       |                     |
| [flagsCustom][138]              | INT          | UNSIGNED   |     | NO   | 0       |       |                     |
| [VerifiedBuild][139]            | SMALLINT     | SIGNED     |     | YES  | 1       |       | (WDBVerified)       |

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
[28]: #statscount
[29]: #stat_type1
[30]: #stat_value1
[31]: #stat_type2
[32]: #stat_value2
[33]: #stat_type3
[34]: #stat_value3
[35]: #stat_type4
[36]: #stat_value4
[37]: #stat_type5
[38]: #stat_value5
[39]: #stat_type6
[40]: #stat_value6
[41]: #stat_type7
[42]: #stat_value7
[43]: #stat_type8
[44]: #stat_value8
[45]: #stat_type9
[46]: #stat_value9
[47]: #stat_type10
[48]: #stat_value10
[49]: #scalingstatdistribution
[50]: #scalingstatvalue
[51]: #dmg_min1
[52]: #dmg_max1
[53]: #dmg_type1
[54]: #dmg_min2
[55]: #dmg_max2
[56]: #dmg_type2
[57]: #armor
[58]: #holy_res
[59]: #fire_res
[60]: #nature_res
[61]: #frost_res
[62]: #shadow_res
[63]: #arcane_res
[64]: #delay
[65]: #ammo_type
[66]: #rangedmodrange
[67]: #spellid_1
[68]: #spelltrigger_1
[69]: #spellcharges_1
[70]: #spellppmrate_1
[71]: #spellcooldown_1
[72]: #spellcategory_1
[73]: #spellcategorycooldown_1
[74]: #spellid_2
[75]: #spelltrigger_2
[76]: #spellcharges_2
[77]: #spellppmrate_2
[78]: #spellcooldown_2
[79]: #spellcategory_2
[80]: #spellcategorycooldown_2
[81]: #spellid_3
[82]: #spelltrigger_3
[83]: #spellcharges_3
[84]: #spellppmrate_3
[85]: #spellcooldown_3
[86]: #spellcategory_3
[87]: #spellcategorycooldown_3
[88]: #spellid_4
[89]: #spelltrigger_4
[90]: #spellcharges_4
[91]: #spellppmrate_4
[92]: #spellcooldown_4
[93]: #spellcategory_4
[94]: #spellcategorycooldown_4
[95]: #spellid_5
[96]: #spelltrigger_5
[97]: #spellcharges_5
[98]: #spellppmrate_5
[99]: #spellcooldown_5
[100]: #spellcategory_5
[101]: #spellcategorycooldown_5
[102]: #bonding
[103]: #description
[104]: #pagetext
[105]: #languageid
[106]: #pagematerial
[107]: #startquest
[108]: #lockid
[109]: #material
[110]: #sheath
[111]: #randomproperty
[112]: #randomsuffix
[113]: #block
[114]: #itemset
[115]: #maxdurability
[116]: #area
[117]: #map
[118]: #bagfamily
[119]: #totemcategory
[120]: #socketcolor_1
[121]: #socketcontent_1
[122]: #socketcolor_2
[123]: #socketcontent_2
[124]: #socketcolor_3
[125]: #socketcontent_3
[126]: #socketbonus
[127]: #gemproperties
[128]: #requireddisenchantskill
[129]: #armordamagemodifier
[130]: #duration
[131]: #itemlimitcategory
[132]: #holidayid
[133]: #scriptname
[134]: #disenchantid
[135]: #foodtype
[136]: #minmoneyloot
[137]: #maxmoneyloot
[138]: #flagscustom
[139]: #verifiedbuild

**Field Descriptions**

### entry

The unique ID of the item.

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

The following table lists all available subclass and class combinations and the subclass name.

| Class ID | Subclass ID | Subclass Name      | Comments                                              |
| -------- | ----------- | ------------------ | ----------------------------------------------------- |
| 0        | 0           | Consumable         | Usability in combat is decided by the spell assigned. |
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
| 2        | 0           | Axe                | One handed                                            |
| 2        | 1           | Axe                | Two handed                                            |
| 2        | 2           | Bow                |                                                       |
| 2        | 3           | Gun                |                                                       |
| 2        | 4           | Mace               | One handed                                            |
| 2        | 5           | Mace               | Two handed                                            |
| 2        | 6           | Polearm            |                                                       |
| 2        | 7           | Sword              | One handed                                            |
| 2        | 8           | Sword              | Two handed                                            |
| 2        | 9           | Obsolete           |                                                       |
| 2        | 10          | Staff              |                                                       |
| 2        | 11          | Exotic             |                                                       |
| 2        | 12          | Exotic             |                                                       |
| 2        | 13          | Fist Weapon        |                                                       |
| 2        | 14          | Miscellaneous      | (Blacksmith Hammer, Mining Pick, etc.)                |
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
| 11       | 2           | Quiver             | Can hold arrows                                       |
| 11       | 3           | Ammo Pouch         | Can hold bullets                                      |
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

Weapons have special sounds on impact. This column is used to override these sounds by specifying another subclass.

For example an item with misc subclass can sound like a stave on impact by overriding the subclass here.

### name

The name of the item.

### displayid

The model ID of the item. Each model has its own icon assigned so this field controls both the model appearance and the icon.

### Quality

The quality of the item.

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

Bitmask field that contains flags that the item has on it. As all other such fields, just add the flags together to combine them. Possible flags are listed below.

| Flag       |             | Comments                                                                                                                                                         |
| ---------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1          | 0x01        | ITEM_FLAG_NO_PICKUP (NOT IMPLEMENTED)                                                                                                                            |
| 2          | 0x02        | Conjured item                                                                                                                                                    |
| 4          | 0x04        | Openable (can be opened by right-click)                                                                                                                          |
| 8          | 0x08        | ITEM_FLAG_HEROIC_TOOLTIP (NOT IMPLEMENTED) - Makes green "Heroic" text appear on item                                                                            |
| 16         | 0x010       | ITEM_FLAG_DEPRECATED (NOT IMPLEMENTED) - Deprecated Item                                                                                                         |
| 32         | 0x020       | Item can not be destroyed, except by using spell (item can be reagent for spell)                                                                                 |
| 64         | 0x040       | ITEM_FLAG_PLAYERCAST (NOT IMPLEMENTED) - Item's spells are castable by players                                                                                   |
| 128        | 0x080       | ITEM_FLAG_NO_EQUIP_COOLDOWN                                                                                                                                      |
| 256        | 0x0100      | ITEM_FLAG_MULTI_LOOT_QUEST (NOT IMPLEMENTED)                                                                                                                     |
| 512        | 0x0200      | Wrapper : Item can wrap other items                                                                                                                              |
| 1024       | 0x0400      | ITEM_FLAG_USES_RESOURCES (NOT IMPLEMENTED)                                                                                                                       |
| 2048       | 0x0800      | Item is party loot and can be looted by all                                                                                                                      |
| 4096       | 0x01000     | Item is refundable                                                                                                                                               |
| 8192       | 0x02000     | Charter (Arena or Guild)                                                                                                                                         |
| 16384      | 0x04000     | ITEM_FLAG_HAS_TEXT (NOT IMPLEMENTED) - Only readable items have this (but not all)                                                                               |
| 32768      | 0x08000     | ITEM_FLAG_NO_DISENCHANT (NOT IMPLEMENTED) - If enabled, prevent disenchanting. Implemented in another column `RequiredDisenchantSkill`                           |
| 65536      | 0x010000    | ITEM_FLAG_REAL_DURATION (NOT IMPLEMENTED) - Probably real time duration. Implemented in another column `flagsCustom`                                             |
| 131072     | 0x020000    | ITEM_FLAG_NO_CREATOR (NOT IMPLEMENTED OR PARTIALLY) - Maybe to remove the "Made by XX" message on crafted/summoned item or for signing charters                  |
| 262144     | 0x040000    | Item can be prospected                                                                                                                                           |
| 524288     | 0x080000    | Unique equipped (player can only have one equipped at the same time but as many as he wants in his bags, if maxcount = 1, it will still display Unique-Equipped) |
| 1048576    | 0x0100000   | ITEM_FLAG_IGNORE_FOR_AURAS (NOT IMPLEMENTED) - ??                                                                                                                |
| 2097152    | 0x0200000   | Item can be used during arena match                                                                                                                              |
| 4194304    | 0x0400000   | Throwable (for tooltip ingame)                                                                                                                                   |
| 8388608    | 0x0800000   | Item can be used in shapeshift forms                                                                                                                             |
| 16777216   | 0x01000000  | ITEM_FLAG_HAS_QUEST_GLOW (NOT IMPLEMENTED)                                                                                                                       |
| 33554432   | 0x02000000  | Profession recipes: can only be looted if you meet requirements and don't already know it                                                                        |
| 67108864   | 0x04000000  | Item cannot be used in arena                                                                                                                                     |
| 134217728  | 0x08000000  | Bind to Account (Requires to set Bonding > 0)                                                                                                                    |
| 268435456  | 0x010000000 | Spell is cast with triggered flag (in code it's written `Spell is cast ignoring reagents` and the flag is called ITEM_FLAG_NO_REAGENT_COST)                      |
| 536870912  | 0x020000000 | Millable                                                                                                                                                         |
| 1073741824 | 0x040000000 | ITEM_FLAG_REPORT_TO_GUILD_CHAT (NOT IMPLEMENTED)                                                                                                                 |
| 2147483648 | 0x080000000 | ITEM_FLAG_NO_PROGRESSIVE_LOOT (NOT IMPLEMENTED)                                                                                                                  |

### FlagsExtra

| Flag    |           | Comments                                                         |
| ------- | --------- | ---------------------------------------------------------------- |
| 1       | 0x01      | Horde Only                                                       |
| 2       | 0x02      | Alliance Only                                                    |
| 4       | 0x04      | When item uses ExtendedCost in npc_vendor, gold is also required |
| 256     | 0x0100    | Makes need roll for this item disabled                           |
| 512     | 0x0200    | NEED_ROLL_DISABLED                                               |
| 16384   | 0x04000   | HAS_NORMAL_PRICE                                                 |
| 131072  | 0x020000  | BNET_ACCOUNT_BOUND (seems useless on 3.3.5a)                     |
| 2097152 | 0x0200000 | CANNOT_BE_TRANSMOG                                               |
| 4194304 | 0x0400000 | CANNOT_TRANSMOG                                                  |
| 8388608 | 0x0800000 | CAN_TRANSMOG                                                     |

### BuyCount

The size of the item stack when sold by vendors. Also if a vendor has limited copies of this item available, everytime the vendor list is refreshed (See [npc\_vendor.incrtime](http://www.azerothcore.org/wiki/npc_vendor#incrtime)), the number of copies increases by this number.

### BuyPrice

The price required to pay to buy this item from a vendor, in copper.

### SellPrice

The price that the vendor will pay you for the item when you sell it and if it is possible to be sold, in copper. Put in 0 if the item cannot be sold to a vendor.

### InventoryType

In what slot the item can be equipped.

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
| 28  | Relic (class = armor, not weapon even if in weapon slot)                                                                               |

### AllowableClass

Bitmask controlling which classes can use this item. Add ids together to combine class possibilities. Use -1 if all classes can use it.

See the [ChrClasses DBC file](ChrClasses) for the IDs of the classes.

### AllowableRace

Bitmask controlling which races can use this item. Add ids together to combine race possibilities. Use -1 for all races.

See the [ChrRaces DBC file](ChrRaces) for the IDs of the races.

### ItemLevel

Base item level.

### RequiredLevel

The level that a player must be to equip the item.

### RequiredSkill

The skill required to use this item. See the [SkillLine DBC file](SkillLine) for IDs which can be used here.

### RequiredSkillRank

The required skill rank the player needs to have to use this item.

### requiredspell

The required spell that the player needs to have to use this item.

### requiredhonorrank

The honor rank the player needs to have to use this item.

### RequiredCityRank

Its use is unknown. All items have 0.

### RequiredReputationFaction

The faction template ID  of the faction that the player has to have a certain ranking with. If this value is 0, the faction of the seller of the item is used.

See the [Faction DBC file](Faction) for the IDs of all of the factions.

### RequiredReputationRank

The rank the player has to have with the faction from [RequiredReputationFaction](#item_template-RequiredReputationFaction).

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

Maximum number of copies of this item which a player can have. Use 0 for infinite.

### stackable

The number of copies of this item that can be stacked in the same slot.

### ContainerSlots

If the item is a bag, this field controls the number of slots the bag has.

### StatsCount

When an item has entries in [stat\_type](#item_template-stat_type), this must be updated to display those entries
(Unknown how this works)

### stat\_type

The type of stat to modify.

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

The value to change the stat type to.

### ScalingStatDistribution

Similar to Static Stats these are the Stats that grow along with the users level (mainly heirloom leveling gear)
use like static stats

### ScalingStatValue

Final (level 80) value of the scaling-stat

### dmg\_min

The minimum damage of the item.

### dmg\_max

The maximum damage of the item.

### dmg\_type

The damage type that the item uses.

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

The armor value of the item.

### holy\_res

Holy resistance.

### fire\_res

Fire resistance.

### nature\_res

Nature resistance.

### frost\_res

Frost resistance.

### shadow\_res

Shadow resistance.

### arcane\_res

Arcane resistance.

### delay

The time in milliseconds between successive hits.

### ammo\_type

The type of ammunition the item uses. Arrows = 2; Bullets = 3

### RangedModRange

Range Modifier for bows/guns/crossbows:

Default range is somewhere between 0.3 and 0.4 yards,

all blizzard ranged weapons have RangedModRange100

### spellid

The spell ID of the spell that the item can cast or trigger.

### spelltrigger

The type of trigger for the spell.

| ID  | Trigger Type      |
| --- | ----------------- |
| 0   | Use               |
| 1   | On Equip          |
| 2   | Chance on Hit     |
| 4   | Soulstone         |
| 5   | Use with no delay |
| 6   | Learn Spell ID    |

### spellcharges

The number of times that the item can cast the spell. If 0, then infinite charges are possible. If negative, then after the number of charges is depleted, the item is deleted as well. If positive, then the item is not deleted after all the charges are spent.

### spellppmRate

The proc per minute rate controlling how often the spell is triggered (if [\#spelltrigger](#item_template-spelltrigger) == 2).

### spellcooldown

The cooldown in milliseconds for the specific spell controlling how often the spell can be used. Use -1 to use the default spell cooldown.  
Note: this is not the "internal cooldown" of procs commonly found on items such as trinkets with "Chance on hit" effects.

### spellcategory

The category that the spell is in. You can choose one from the DBC `SpellCategory.dbc` or invent a new one (> 1260) for your custom item.

### spellcategorycooldown

The cooldown time in milliseconds that is applied to all other spells in the category that the triggered spell is also in. Use -1 to use the default spell cooldown.  
Note: you can have a `spellcooldown` and a `spellcategorycooldown`, they're not mutually exclusive.

### bonding

The bonding for the item.

**Note:** To use the "Bind to Account" bonding, the item must have its `flags` set to 134217728 (minimum) and a `bonding` > 0 (ex: 1,2,3).

| ID  | Bonding Type         |
| --- | -------------------- |
| 0   | No bounds            |
| 1   | Binds when picked up |
| 2   | Binds when equipped  |
| 3   | Binds when used      |
| 4   | Quest item           |
| 5   | Quest Item1          |

### description

The description that appears in orange letters at the bottom of the item tooltip.

### PageText

The ID referring to the text that the item will show (if it is a book or a letter, etc). The item will have a magnifying glass cursor in the game and will show the text when right-clicked. See [page\_text.entry](http://www.azerothcore.org/wiki/page_text#entry)

### LanguageID

The language that the item text is written in.

See the [Languages DBC file](Languages) for the IDs of all of the languages.

### PageMaterial

The background texture that appears in the page text window.

See the [PageTextMaterial DBC file](PageTextMaterial) for the IDs of all of the material types.

### startquest

The ID of the quest that this item will start if right-clicked. See [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id)

### lockid

The lock entry ID that this item (which serves as a key) is tied to. This field is used in key-door mechanics.

See the [Lock DBC file](Lock).

### Material

The material that the item is made of. The value here affects the sound that the item makes when moved. Use -1 for consumable items like food, reagents, etc.

| ID  | Material    | Comment                |
| --- | ----------- | ---------------------- |
| -1  | Consumables | Food, reagents, etc... |
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

Controls how the item is put away on the character. Press the 'Z' hotkey to sheath and unsheathe your weapons.

| ID  | Type              | Position                                         |
| --- | ----------------- | ------------------------------------------------ |
| 1   | Two Handed Weapon | Diagonally across the back pointing downwards.   |
| 2   | Staff             | Diagonally across the back pointing upwards.     |
| 3   | One Handed        | On the left-hand side of the character's waist.  |
| 4   | Shield            | On the middle of the character's back.           |
| 5   | Enchanter's Rod   |                                                  |
| 6   | Off hand          | On the right-hand side of the character's waist. |

### RandomProperty

The number in this field points to [item\_enchantment\_template.entry](http://www.azerothcore.org/wiki/item_enchantment_template#entry) and ties in an item's chance at having a random property attached to it when it shows up for the first time. This field and the [RandomSuffix](#item_template-RandomSuffix) field CANNOT both have non-zero values. Either one is filled, or the other. Also, the primary source for the number in this field are WDBs.

### RandomSuffix

The number in this field points to [item\_enchantment\_template.entry](http://www.azerothcore.org/wiki/item_enchantment_template#entry) and ties in an item's chance at having a random suffix attached to it when it shows up for the first time. This field and the [RandomProperty](#item_template-RandomProperty) field CANNOT both have non-zero values. Either one is filled, or the other. Also, the primary source for the number in this field are WDBs.

### block

If the item is a shield, the block chance of the shield.

### itemset

The ID of the item set that this item belongs to. To save you some time, you CAN NOT make up new item sets. Item sets are defined in the ItemSet DBC file.

### MaxDurability

The maximum durability of this item.

### area

The ID of the zone in which this item can be used. If you leave the area, the item will be deleted from the inventory.

### Map

The ID of the map in which this item can be used. If you leave the map, the item will be deleted from the inventory.

### BagFamily

If the item is a bag, this field is a bitmask controlling what types of items can be put in this bag. You can combine different types by adding up the bit numbers.

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

Corresponds to the ID in the [TotemCategory DBC file](TotemCategory).

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

The color of the socket that can be placed in this item.

| ID  | Color  |
| --- | ------ |
| 1   | Meta   |
| 2   | Red    |
| 4   | Yellow |
| 8   | Blue   |

### socketContent

Amount of Gems of SocketColor1

### socketBonus

commonly used socket bonus IDs

| ID   | Effect           |
| ---- | ---------------- |
| 3312 | +8 Strength      |
| 3313 | +8 Agility       |
| 3305 | +12 Stamina      |
| 3    | +8 Intellect     |
| 2872 | +9 Healing       |
| 3753 | +9 Spell Power   |
| 3877 | +16 Attack Power |

### GemProperties

The value here corresponds to the ID in GemProperties.dbc.

### RequiredDisenchantSkill

The required proficiency in disenchanting that the player needs to have to be able to disenchant this item.
If set to -1, the item can't be disenchanted.

### ArmorDamageModifier

`field-no-description|76`

### duration

The duration of the item in seconds ingame time.
Set ITEM\_FLAGS\_CU\_DURATION\_REAL\_TIME in *flagsCustom* for real time. In that case the item duration will tick even if player is offline.

### ItemLimitCategory

This is related to ItemLimitCategory.dbc.
It is a property that defines if an item belongs to a "category", like "Mana Gems" or "Healthstone" and it defines how many items of the category you can have in the bag (this is the "limit").
For example, for Healthstone, there are several items like "Lesser Healthstone, Greater Healthstone, etc." but you can have only one in your bag (check as example value 3 or 4).

### HolidayId

See the [Holidays DBC file](Holidays) for the IDs of all of the holidays.

### ScriptName

The name of the script that the item should use. There is no 'internalitemhandler' or 'internalitemhanler' script so trinity will ignore any such values in this field.

### DisenchantID

The disenchant loot template ID. See [disenchant\_loot\_template.entry](http://www.azerothcore.org/wiki/loot_template#loot_template-Entry)

### FoodType

If this item is a food type item, this field defines what type of food it is for hunters who want to feed their pets. It controls in what diet this food item falls in.

NOTE: Raw meat and fish is not the same as regular meat and fish. It seems that the last two types of diets include grey "poor" types of food that players have no use for but some pets seem to be able to eat. Also, those food types appeared in TBC so most likely only TBC pets will have those types of diets.

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

If the item is a container that can contain money, then this field defines the minimum coinage held in this container, in copper.

### maxMoneyLoot

If the item is a container that can contain money, then this field defines the maximum coinage held in this container, in copper.

### flagsCustom

| Flag | Name                              | Comment                                                              |
| ---- | --------------------------------- | -------------------------------------------------------------------- |
| 1    | ITEM_FLAGS_CU_DURATION_REAL_TIME  | Item duration will tick even if player is offline                    |
| 2    | ITEM_FLAGS_CU_IGNORE_QUEST_STATUS | No quest status will be checked when this item drops                 |
| 4    | ITEM_FLAGS_CU_FOLLOW_LOOT_RULES   | Item will always follow group/master/need before greed looting rules |

### VerifiedBuild

This field was used to determine whether a template has been verified from WDB files.
- If value is 0 then it has not been parsed yet.
- If value is above 0 then it has been parsed with WDB files from that specific client build.
- If value is -1 then it is just a place holder until proper data are found on WDBs.

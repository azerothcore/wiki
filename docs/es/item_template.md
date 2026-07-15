# item\_template

[<-Volver a: World](database-world)

**Estructura**

Contiene información sobre cada objeto que existe en el juego. Todos los objetos se crean a partir de su plantilla almacenada en esta tabla.

(Ver información adicional en el archivo *ItemPrototype.h*.)

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
| [dmg_max2][54]                  | FLOAT        | SIGNED     |     | NO   | 0       |       |                     |
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
| [duration][129]                 | INT          | UNSIGNED   |     | NO   | 0       |       | Duration in seconds |
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
[57]: #holy_res
[58]: #fire_res
[59]: #nature_res
[60]: #frost_res
[61]: #shadow_res
[62]: #arcane_res
[63]: #delay
[64]: #ammo_type
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

**Descripción de los campos**

### entry

El ID único del objeto.

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

La siguiente tabla lista todas las combinaciones disponibles de subclass y class y el nombre de la subclase.

| Class ID | Subclass ID | Subclass Name      | Comments                                              |
| -------- | ----------- | ------------------ | ----------------------------------------------------- |
| 0        | 0           | Consumable         | La usabilidad en combate la decide el hechizo asignado. |
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
| 2        | 0           | Axe                | Una mano                                              |
| 2        | 1           | Axe                | Dos manos                                             |
| 2        | 2           | Bow                |                                                       |
| 2        | 3           | Gun                |                                                       |
| 2        | 4           | Mace               | Una mano                                              |
| 2        | 5           | Mace               | Dos manos                                             |
| 2        | 6           | Polearm            |                                                       |
| 2        | 7           | Sword              | Una mano                                              |
| 2        | 8           | Sword              | Dos manos                                             |
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
| 11       | 2           | Quiver             | Puede contener flechas                                |
| 11       | 3           | Ammo Pouch         | Puede contener balas                                  |
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

Las armas tienen sonidos especiales al impactar. Esta columna se usa para sobrescribir esos sonidos especificando otra subclase.

Por ejemplo, un objeto con subclase misc puede sonar como un bastón (stave) al impactar sobrescribiendo aquí la subclase.

### name

El nombre del objeto.

### displayid

El ID del modelo del objeto. Cada modelo tiene su propio icono asignado, así que este campo controla tanto la apariencia del modelo como el icono.

### Quality

La calidad del objeto.

| ID  | Color  | Quality                                   |
| --- | ------ | ----------------------------------------- |
| 0   | Grey   | Poor                                      |
| 1   | White  | Common                                    |
| 2   | Green  | Uncommon                                  |
| 3   | Blue   | Rare                                      |
| 4   | Purple | Epic                                      |
| 5   | Orange | Legendary                                 |
| 6   | Red    | Artifact                                  |
| 7   | Gold   | Heirlooms (o algunos objetos Bind to Account) |

### Flags

Campo bitmask que contiene los flags que tiene el objeto. Como en todos los campos de este tipo, basta sumar los flags para combinarlos. Los flags posibles se listan a continuación.

| Flag       | Bit        | Name                             | Comment                                                                                                                              |
| ---------- | ---------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| 0x01       | 1          | ITEM_FLAG_NO_PICKUP              | (NO IMPLEMENTADO)                                                                                                                   |
| 0x02       | 2          |                                  | Objeto invocado (conjurado)                                                                                                         |
| 0x04       | 4          |                                  | Abrible (se puede abrir con click derecho)                                                                                          |
| 0x08       | 8          | ITEM_FLAG_HEROIC_TOOLTIP         | (NO IMPLEMENTADO) - Hace aparecer el texto verde "Heroic" en el objeto                                                             |
| 0x10       | 16         | ITEM_FLAG_DEPRECATED             | (NO IMPLEMENTADO) - Objeto obsoleto                                                                                                |
| 0x20       | 32         |                                  | El objeto no puede destruirse, salvo mediante un hechizo (el objeto puede ser reactivo de un hechizo)                              |
| 0x40       | 64         | ITEM_FLAG_PLAYERCAST             | (NO IMPLEMENTADO) - Los hechizos del objeto pueden ser lanzados por los jugadores                                                 |
| 0x80       | 128        | ITEM_FLAG_NO_EQUIP_COOLDOWN      |                                                                                                                                      |
| 0x0100     | 256        | ITEM_FLAG_MULTI_LOOT_QUEST       | (NO IMPLEMENTADO)                                                                                                                   |
| 0x0200     | 512        |                                  | Envoltorio: el objeto puede envolver otros objetos                                                                                 |
| 0x0400     | 1024       | ITEM_FLAG_USES_RESOURCES         | (NO IMPLEMENTADO)                                                                                                                   |
| 0x0800     | 2048       |                                  | El objeto es botín de grupo y todos pueden saquearlo                                                                               |
| 0x01000    | 4096       |                                  | El objeto es reembolsable                                                                                                          |
| 0x02000    | 8192       |                                  | Estatuto (Arena o Hermandad)                                                                                                       |
| 0x04000    | 16384      | ITEM_FLAG_HAS_TEXT               | (NO IMPLEMENTADO) - Solo los objetos legibles tienen esto (pero no todos)                                                          |
| 0x08000    | 32768      | ITEM_FLAG_NO_DISENCHANT          | (NO IMPLEMENTADO) - Si se habilita, impide el desencantamiento. Implementado en otra columna `RequiredDisenchantSkill`            |
| 0x010000   | 65536      | ITEM_FLAG_REAL_DURATION          | (NO IMPLEMENTADO) - Probablemente duración en tiempo real. Implementado en otra columna `flagsCustom`                             |
| 0x020000   | 131072     | ITEM_FLAG_NO_CREATOR             | (NO IMPLEMENTADO O PARCIALMENTE) - Quizá para eliminar el mensaje "Made by XX" en objetos fabricados/invocados o para firmar estatutos |
| 0x040000   | 262144     |                                  | El objeto puede prospectarse                                                                                                       |
| 0x080000   | 524288     |                                  | Equipado único (el jugador solo puede tener uno equipado al mismo tiempo pero tantos como quiera en sus bolsas; si maxcount = 1, seguirá mostrando Equipado único) |
| 0x0100000  | 1048576    | ITEM_FLAG_IGNORE_FOR_AURAS       | (NO IMPLEMENTADO) - ??                                                                                                              |
| 0x0200000  | 2097152    |                                  | El objeto puede usarse durante un combate de arena                                                                                 |
| 0x0400000  | 4194304    |                                  | Arrojadizo (para el tooltip en el juego)                                                                                           |
| 0x0800000  | 8388608    |                                  | El objeto puede usarse en formas de cambio de forma                                                                               |
| 0x01000000 | 16777216   | ITEM_FLAG_HAS_QUEST_GLOW         | (NO IMPLEMENTADO)                                                                                                                   |
| 0x02000000 | 33554432   |                                  | Recetas de profesión: solo pueden saquearse si cumples los requisitos y no la conoces ya                                          |
| 0x04000000 | 67108864   |                                  | El objeto no puede usarse en arena                                                                                                 |
| 0x08000000 | 134217728  |                                  | Vinculado a la cuenta (requiere establecer Bonding > 0)                                                                            |
| 0x10000000 | 268435456  | ITEM_FLAG_NO_REAGENT_COST        | El hechizo se lanza con el flag triggered (en el código está escrito `Spell is cast ignoring reagents`)                            |
| 0x20000000 | 536870912  |                                  | Molturable                                                                                                                         |
| 0x40000000 | 1073741824 | ITEM_FLAG_REPORT_TO_GUILD_CHAT   | (NO IMPLEMENTADO)                                                                                                                   |
| 0x80000000 | 2147483648 | ITEM_FLAG_NO_PROGRESSIVE_LOOT    | (NO IMPLEMENTADO)                                                                                                                   |

### FlagsExtra

| Flag       | Bit        | Name                                                | Comment                                 |
| ---------- | ---------- | --------------------------------------------------- | --------------------------------------- |
| 0x00000001 | 1          | ITEM_FLAG2_FACTION_HORDE                            | Solo Horda                              |
| 0x00000002 | 2          | ITEM_FLAG2_FACTION_ALLIANCE                         | Solo Alianza                            |
| 0x00000004 | 4          | ITEM_FLAG2_DONT_IGNORE_BUY_PRICE                    | Cuando el objeto usa ExtendedCost en npc_vendor, también se requiere oro |
| 0x00000008 | 8          | ITEM_FLAG2_CLASSIFY_AS_CASTER                       | NYI - Sin usar en item_template         |
| 0x00000010 | 16         | ITEM_FLAG2_CLASSIFY_AS_PHYSICAL                     | NYI                                     |
| 0x00000020 | 32         | ITEM_FLAG2_EVERYONE_CAN_ROLL_NEED                   | Cualquiera puede tirar por necesidad (need) |
| 0x00000040 | 64         | ITEM_FLAG2_NO_TRADE_BIND_ON_ACQUIRE                 | NYI - Sin usar en item_template         |
| 0x00000080 | 128        | ITEM_FLAG2_CAN_TRADE_BIND_ON_ACQUIRE                | NYI - Sin usar en item_template         |
| 0x00000100 | 256        | ITEM_FLAG2_CAN_ONLY_ROLL_GREED                      | Deshabilita la tirada por necesidad (need) para este objeto |
| 0x00000200 | 512        | ITEM_FLAG2_CASTER_WEAPON                            | NYI                                     |
| 0x00000400 | 1024       | ITEM_FLAG2_DELETE_ON_LOGIN                          | NYI - Sin usar en item_template         |
| 0x00000800 | 2048       | ITEM_FLAG2_INTERNAL_ITEM                            | NYI - Sin usar en item_template         |
| 0x00001000 | 4096       | ITEM_FLAG2_NO_VENDOR_VALUE                          | NYI - Sin usar en item_template         |
| 0x00002000 | 8192       | ITEM_FLAG2_SHOW_BEFORE_DISCOVERED                   | NYI                                     |
| 0x00004000 | 16384      | ITEM_FLAG2_OVERRIDE_GOLD_COST                       | NYI - Sin usar en item_template         |
| 0x00008000 | 32768      | ITEM_FLAG2_IGNORE_DEFAULT_RATED_BG_RESTRICTIONS     | NYI                                     |
| 0x00010000 | 65536      | ITEM_FLAG2_NOT_USABLE_IN_RATED_BG                   | NYI                                     |
| 0x00020000 | 131072     | ITEM_FLAG2_BNET_ACCOUNT_TRADE_OK                    | NYI                                     |
| 0x00040000 | 262144     | ITEM_FLAG2_CONFIRM_BEFORE_USE                       | NYI - Sin usar en item_template         |
| 0x00080000 | 524288     | ITEM_FLAG2_REEVALUATE_BONDING_ON_TRANSFORM          | NYI - Sin usar en item_template         |
| 0x00100000 | 1048576    | ITEM_FLAG2_NO_TRANSFORM_ON_CHARGE_DEPLETION         | NYI - Sin usar en item_template         |
| 0x00200000 | 2097152    | ITEM_FLAG2_NO_ALTER_ITEM_VISUAL                     | NYI                                     |
| 0x00400000 | 4194304    | ITEM_FLAG2_NO_SOURCE_FOR_ITEM_VISUAL                | NYI                                     |
| 0x00800000 | 8388608    | ITEM_FLAG2_IGNORE_QUALITY_FOR_ITEM_VISUAL_SOURCE    | NYI - Sin usar en item_template         |
| 0x01000000 | 16777216   | ITEM_FLAG2_NO_DURABILITY                            | NYI - Sin usar en item_template         |
| 0x02000000 | 33554432   | ITEM_FLAG2_ROLE_TANK                                | NYI - Sin usar en item_template         |
| 0x04000000 | 67108864   | ITEM_FLAG2_ROLE_HEALER                              | NYI - Sin usar en item_template         |
| 0x08000000 | 134217728  | ITEM_FLAG2_ROLE_DAMAGE                              | NYI - Sin usar en item_template         |
| 0x10000000 | 268435456  | ITEM_FLAG2_CAN_DROP_IN_CHALLENGE_MODE               | NYI - Sin usar en item_template         |
| 0x20000000 | 536870912  | ITEM_FLAG2_NEVER_STACK_IN_LOOT_UI                   | NYI - Sin usar en item_template         |
| 0x40000000 | 1073741824 | ITEM_FLAG2_DISENCHANT_TO_LOOT_TABLE                 | NYI - Sin usar en item_template         |
| 0x80000000 | 2147483648 | ITEM_FLAG2_USED_IN_A_TRADESKILL                     | NYI - Sin usar en item_template         |

### BuyCount

El tamaño de la pila del objeto cuando lo venden los vendedores. Además, si un vendedor tiene copias limitadas de este objeto disponibles, cada vez que se refresca la lista del vendedor (ver [npc\_vendor.incrtime](http://www.azerothcore.org/wiki/npc_vendor#incrtime)), el número de copias aumenta en este número.

### BuyPrice

El precio que hay que pagar para comprar este objeto a un vendedor, en cobre.

### SellPrice

El precio que el vendedor te pagará por el objeto cuando lo vendas y si es posible venderlo, en cobre. Pon 0 si el objeto no puede venderse a un vendedor.

### InventoryType

En qué ranura (slot) se equipará el objeto.

| ID  | Slot Name                                                                                                                              |
| --- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 0   | Non equipable                                                                                                                          |
| 1   | Head                                                                                                                                   |
| 2   | Neck                                                                                                                                   |
| 3   | Shoulder                                                                                                                               |
| 4   | Shirt                                                                                                                                  |
| 5   | Chest (ver también Robe = 20)                                                                                                          |
| 6   | Waist                                                                                                                                  |
| 7   | Legs                                                                                                                                   |
| 8   | Feet                                                                                                                                   |
| 9   | Wrists                                                                                                                                 |
| 10  | Hands                                                                                                                                  |
| 11  | Finger                                                                                                                                 |
| 12  | Trinket                                                                                                                                |
| 13  | One-Hand (no confundir con Off-Hand = 22)                                                                                              |
| 14  | Shield (clase = armadura, no arma aunque esté en ranura de arma)                                                                       |
| 15  | Ranged (arcos) (ver también Ranged right = 26)                                                                                         |
| 16  | Back                                                                                                                                   |
| 17  | Two-Hand                                                                                                                               |
| 18  | Bag                                                                                                                                    |
| 19  | Tabard                                                                                                                                 |
| 20  | Robe (ver también Chest = 5)                                                                                                           |
| 21  | Main hand                                                                                                                              |
| 22  | Off Hand weapons (ver también One-Hand = 13)                                                                                           |
| 23  | Held in Off-Hand (tomo, bastón, flores, antorchas, orbes, etc... Ver también Off-Hand = 22) (clase = armadura, no arma aunque esté en ranura de arma) |
| 24  | Ammo                                                                                                                                   |
| 25  | Thrown                                                                                                                                 |
| 26  | Ranged right (varitas, armas de fuego) (ver también Ranged = 15)                                                                       |
| 27  | Quiver                                                                                                                                 |
| 28  | Relic (clase = armadura, no arma aunque esté en ranura de arma)                                                                        

### AllowableClass

Bitmask que controla qué clases pueden usar este objeto. Suma los ids para combinar las posibilidades de clase. Usa -1 si todas las clases pueden usarlo.

Ver el [archivo DBC ChrClasses](chrclasses) para los IDs de las clases.

### AllowableRace

Bitmask que controla qué razas pueden usar este objeto. Suma los ids para combinar las posibilidades de raza. Usa -1 para todas las razas.

Ver el [archivo DBC ChrRaces](chrraces) para los IDs de las razas.

### ItemLevel

Nivel base del objeto.

### RequiredLevel

El nivel que un jugador debe tener para equipar el objeto.

### RequiredSkill

La habilidad requerida para usar este objeto. Ver el [archivo DBC SkillLine](skillline) para los IDs que pueden usarse aquí.

### RequiredSkillRank

El rango de habilidad requerido que el jugador necesita tener para usar este objeto.

### requiredspell

El hechizo requerido que el jugador necesita tener para usar este objeto.

### requiredhonorrank

El rango de honor que el jugador necesita tener para usar este objeto.

### RequiredCityRank

Su uso es desconocido. Todos los objetos tienen 0.

### RequiredReputationFaction

El ID de la plantilla de facción de la facción con la que el jugador debe tener cierto rango. Si este valor es 0, se usa la facción del vendedor del objeto.

Ver el [archivo DBC Faction](faction) para los IDs de todas las facciones.

### RequiredReputationRank

El rango que el jugador debe tener con la facción de [RequiredReputationFaction](#item_template-RequiredReputationFaction).

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

Número máximo de copias de este objeto que un jugador puede tener. Usa 0 para infinito.

### stackable

El número de copias de este objeto que pueden apilarse en la misma ranura.

### ContainerSlots

Si el objeto es una bolsa, este campo controla el número de ranuras que tiene la bolsa.

### stat\_type

El tipo de estadística a modificar.

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

El valor al que cambiar el tipo de estadística.

### ScalingStatDistribution

Similar a las estadísticas estáticas, estas son las estadísticas que crecen junto con el nivel del usuario (principalmente equipo de subida de nivel de tipo heirloom).
Se usa como las estadísticas estáticas.

### ScalingStatValue

Valor final (nivel 80) de la estadística escalable.

### dmg\_min

El daño mínimo del objeto.

### dmg\_max

El daño máximo del objeto.

### dmg\_type

El tipo de daño que usa el objeto.

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

El valor de armadura del objeto.

### holy\_res

Resistencia a lo sagrado (holy).

### fire\_res

Resistencia al fuego.

### nature\_res

Resistencia a la naturaleza.

### frost\_res

Resistencia a la escarcha.

### shadow\_res

Resistencia a la sombra.

### arcane\_res

Resistencia a lo arcano.

### delay

El tiempo en milisegundos entre golpes sucesivos.

### ammo\_type

El tipo de munición que usa el objeto. Flechas = 2; Balas = 3

### RangedModRange

Modificador de rango para arcos/armas de fuego/ballestas:

El rango por defecto está en algún punto entre 0.3 y 0.4 yardas,

todas las armas a distancia de blizzard tienen RangedModRange100.

### spellid

El ID del hechizo que el objeto puede lanzar o activar.

### spelltrigger

El tipo de activación (trigger) del hechizo.

| ID  | Trigger Type      |
| --- | ----------------- |
| 0   | Use               |
| 1   | On Equip          |
| 2   | Chance on Hit     |
| 4   | Soulstone         |
| 5   | Use with no delay |
| 6   | Learn Spell ID    |

### spellcharges

El número de veces que el objeto puede lanzar el hechizo. Si es 0, entonces son posibles cargas infinitas. Si es negativo, entonces tras agotarse el número de cargas el objeto también se elimina. Si es positivo, entonces el objeto no se elimina tras gastar todas las cargas.

### spellppmRate

La tasa de procs por minuto que controla con qué frecuencia se activa el hechizo (si [\#spelltrigger](#item_template-spelltrigger) == 2).

### spellcooldown

El cooldown en milisegundos del hechizo específico que controla con qué frecuencia puede usarse. Usa -1 para usar el cooldown por defecto del hechizo.  
Nota: este no es el "cooldown interno" de los procs que suelen encontrarse en objetos como abalorios con efectos "Chance on hit".

### spellcategory

La categoría en la que está el hechizo. Puedes elegir una del DBC `SpellCategory.dbc` o inventar una nueva (> 1260) para tu objeto personalizado.

### spellcategorycooldown

El tiempo de cooldown en milisegundos que se aplica a todos los demás hechizos de la categoría en la que también está el hechizo activado. Usa -1 para usar el cooldown por defecto del hechizo.  
Nota: puedes tener un `spellcooldown` y un `spellcategorycooldown`, no son mutuamente excluyentes.

### bonding

El vínculo (bonding) del objeto.

**Nota:** Para usar el vínculo "Bind to Account", el objeto debe tener sus `flags` establecidos a 134217728 (mínimo) y un `bonding` > 0 (ej: 1,2,3).

| ID  | Bonding Type         |
| --- | -------------------- |
| 0   | No bounds            |
| 1   | Binds when picked up |
| 2   | Binds when equipped  |
| 3   | Binds when used      |
| 4   | Quest item           |
| 5   | Quest Item1          |

### description

La descripción que aparece en letras naranjas al final del tooltip del objeto.

### PageText

El ID que referencia el texto que mostrará el objeto (si es un libro o una carta, etc.). El objeto tendrá un cursor de lupa en el juego y mostrará el texto al hacer click derecho. Ver [page\_text.entry](http://www.azerothcore.org/wiki/page_text#entry)

### LanguageID

El idioma en el que está escrito el texto del objeto.

Ver el [archivo DBC Languages](languages) para los IDs de todos los idiomas.

### PageMaterial

La textura de fondo que aparece en la ventana de texto de página.

Ver el [archivo DBC PageTextMaterial](pagetextmaterial) para los IDs de todos los tipos de material.

### startquest

El ID de la misión que este objeto iniciará si se hace click derecho. Ver [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id)

### lockid

El ID de la entrada de cerradura (lock) a la que está vinculado este objeto (que sirve de llave). Este campo se usa en mecánicas de llave-puerta.

Ver el [archivo DBC Lock](lock).

### Material

El material del que está hecho el objeto. El valor aquí afecta al sonido que hace el objeto al moverse. Usa -1 para objetos consumibles como comida, reactivos, etc.

| ID  | Material    | Comment                |
| --- | ----------- | ---------------------- |
| -1  | Consumables | Comida, reactivos, etc... |
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

Controla cómo se guarda el objeto en el personaje. Pulsa la tecla 'Z' para enfundar y desenfundar tus armas.

| ID  | Type              | Position                                         |
| --- | ----------------- | ------------------------------------------------ |
| 1   | Two Handed Weapon | En diagonal a lo largo de la espalda apuntando hacia abajo. |
| 2   | Staff             | En diagonal a lo largo de la espalda apuntando hacia arriba. |
| 3   | One Handed        | En el lado izquierdo de la cintura del personaje. |
| 4   | Shield            | En el centro de la espalda del personaje.        |
| 5   | Enchanter's Rod   |                                                  |
| 7   | Off hand          | En el lado derecho de la cintura del personaje.  |

### RandomProperty

El número de este campo apunta a [item\_enchantment\_template.entry](http://www.azerothcore.org/wiki/item_enchantment_template#entry) y determina la probabilidad de que un objeto tenga una propiedad aleatoria adjunta cuando aparece por primera vez. Este campo y el campo [RandomSuffix](#item_template-RandomSuffix) NO pueden tener ambos valores distintos de cero. O se rellena uno, o el otro. Además, la fuente principal del número de este campo son los WDB.

### RandomSuffix

El número de este campo apunta a [item\_enchantment\_template.entry](http://www.azerothcore.org/wiki/item_enchantment_template#entry) y determina la probabilidad de que un objeto tenga un sufijo aleatorio adjunto cuando aparece por primera vez. Este campo y el campo [RandomProperty](#item_template-RandomProperty) NO pueden tener ambos valores distintos de cero. O se rellena uno, o el otro. Además, la fuente principal del número de este campo son los WDB.

### block

Si el objeto es un escudo, la probabilidad de bloqueo del escudo.

### itemset

El ID del conjunto de objetos (item set) al que pertenece este objeto. Para ahorrarte tiempo, NO PUEDES inventar nuevos conjuntos de objetos. Los conjuntos de objetos se definen en el archivo DBC ItemSet.

### MaxDurability

La durabilidad máxima de este objeto.

### area

El ID de la zona en la que puede usarse este objeto. Si sales del área, el objeto se eliminará del inventario.

### Map

El ID del mapa en el que puede usarse este objeto. Si sales del mapa, el objeto se eliminará del inventario.

### BagFamily

Si el objeto es una bolsa, este campo es un bitmask que controla qué tipos de objetos pueden meterse en esta bolsa. Puedes combinar distintos tipos sumando los números de bit.

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

Corresponde al ID en el [archivo DBC TotemCategory](totemcategory).

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

El color de la ranura (socket) que puede colocarse en este objeto.

| ID  | Color  |
| --- | ------ |
| 1   | Meta   |
| 2   | Red    |
| 4   | Yellow |
| 8   | Blue   |

### socketContent

Cantidad de gemas de SocketColor1.

### socketBonus

IDs de bonus de ranura (socket bonus) usados comúnmente.

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

El valor aquí corresponde al ID en GemProperties.dbc.

### RequiredDisenchantSkill

La competencia requerida en desencantamiento que el jugador necesita tener para poder desencantar este objeto.
Si se establece en -1, el objeto no puede desencantarse.

### ArmorDamageModifier

`campo-sin-descripción|76`

### duration

La duración del objeto en segundos de tiempo de juego.
Establece ITEM\_FLAGS\_CU\_DURATION\_REAL\_TIME en *flagsCustom* para tiempo real. En ese caso la duración del objeto correrá aunque el jugador esté desconectado.

### ItemLimitCategory

Esto está relacionado con ItemLimitCategory.dbc.
Es una propiedad que define si un objeto pertenece a una "categoría", como "Mana Gems" o "Healthstone", y define cuántos objetos de la categoría puedes tener en la bolsa (este es el "límite").
Por ejemplo, para Healthstone hay varios objetos como "Lesser Healthstone, Greater Healthstone, etc." pero solo puedes tener uno en tu bolsa (comprueba como ejemplo el valor 3 o 4).

### HolidayId

Ver el [archivo DBC Holidays](holidays) para los IDs de todas las festividades.

### ScriptName

El nombre del script que debe usar el objeto. No existe ningún script 'internalitemhandler' ni 'internalitemhanler', así que trinity ignorará cualquier valor de ese tipo en este campo.

### DisenchantID

El ID de la plantilla de botín de desencantamiento. Ver [disenchant\_loot\_template.entry](http://www.azerothcore.org/wiki/loot_template#loot_template-Entry)

### FoodType

Si este objeto es un objeto de tipo comida, este campo define qué tipo de comida es para los cazadores que quieran alimentar a sus mascotas. Controla en qué dieta cae este objeto de comida.

NOTA: La carne y el pescado crudos no son lo mismo que la carne y el pescado normales. Parece que los dos últimos tipos de dieta incluyen tipos de comida gris "poor" que los jugadores no aprovechan pero que algunas mascotas parecen poder comer. Además, esos tipos de comida aparecieron en TBC, así que lo más probable es que solo las mascotas de TBC tengan esos tipos de dieta.

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

Si el objeto es un contenedor que puede contener dinero, entonces este campo define la moneda mínima contenida en este contenedor, en cobre.

### maxMoneyLoot

Si el objeto es un contenedor que puede contener dinero, entonces este campo define la moneda máxima contenida en este contenedor, en cobre.

### flagsCustom

| Flag       | Bit | Name                              | Comment                                                              |
| ---------- | --- | --------------------------------- | -------------------------------------------------------------------- |
| 0x00000001 | 1   | ITEM_FLAGS_CU_DURATION_REAL_TIME  | La duración del objeto correrá aunque el jugador esté desconectado   |
| 0x00000002 | 2   | ITEM_FLAGS_CU_IGNORE_QUEST_STATUS | No se comprobará ningún estado de misión cuando caiga este objeto    |
| 0x00000004 | 4   | ITEM_FLAGS_CU_FOLLOW_LOOT_RULES   | El objeto seguirá siempre las reglas de botín group/master/need before greed |

### VerifiedBuild

Este campo se usaba para determinar si una plantilla ha sido verificada a partir de archivos WDB.
- Si el valor es 0, entonces aún no ha sido parseada.
- Si el valor es mayor que 0, entonces ha sido parseada con archivos WDB de esa build de cliente específica.
- Si el valor es -1, entonces es solo un marcador de posición hasta que se encuentren datos adecuados en los WDB.

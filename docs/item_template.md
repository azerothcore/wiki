# item\_template

[<-Back-to:World](database-world)

**Table: item\_template's Structure**

Holds information on every item that exists in the game. All items are created from their template stored in this table.

(See additional information in the *[ItemTemplate.h](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Entities/Item/ItemTemplate.h)* file.)

| Field                                                   | Type         |          | Null | Key | Default | Extra | Comment             |
| :------------------------------------------------------ | :----------- | :------- | :--: | :-: | :-----: | :---: | :------------------ |
| [entry](#entry)                                         | INT          | UNSIGNED | NO   | PRI | 0       |       |                     |
| [class](#class)                                         | TINYINT      | UNSIGNED | NO   | MUL | 0       |       |                     |
| [subclass](#subclass)                                   | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [SoundOverrideSubclass](#soundoverridesubclass)         | TINYINT      |          | NO   |     | -1      |       |                     |
| [name](#name)                                           | VARCHAR(255) |          | NO   | MUL | ''      |       |                     |
| [displayid](#displayid)                                 | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [Quality](#quality)                                     | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [Flags](#flags)                                         | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [FlagsExtra](#flagsextra)                               | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [BuyCount](#buycount)                                   | TINYINT      | UNSIGNED | NO   |     | 1       |       |                     |
| [BuyPrice](#buyprice)                                   | BIGINT       |          | NO   |     | 0       |       |                     |
| [SellPrice](#sellprice)                                 | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [InventoryType](#inventorytype)                         | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [AllowableClass](#allowableclass)                       | INT          |          | NO   |     | -1      |       |                     |
| [AllowableRace](#allowablerace)                         | INT          |          | NO   |     | -1      |       |                     |
| [ItemLevel](#itemlevel)                                 | SMALLINT     | UNSIGNED | NO   |     | 0       |       |                     |
| [RequiredLevel](#requiredlevel)                         | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [RequiredSkill](#requiredskill)                         | SMALLINT     | UNSIGNED | NO   |     | 0       |       |                     |
| [RequiredSkillRank](#requiredskillrank)                 | SMALLINT     | UNSIGNED | NO   |     | 0       |       |                     |
| [requiredspell](#requiredspell)                         | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [requiredhonorrank](#requiredhonorrank)                 | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [RequiredCityRank](#requiredcityrank)                   | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [RequiredReputationFaction](#requiredreputationfaction) | SMALLINT     | UNSIGNED | NO   |     | 0       |       |                     |
| [RequiredReputationRank](#requiredreputationrank)       | SMALLINT     | UNSIGNED | NO   |     | 0       |       |                     |
| [maxcount](#maxcount)                                   | INT          |          | NO   |     | 0       |       |                     |
| [stackable](#stackable)                                 | INT          |          | YES  |     | 1       |       |                     |
| [ContainerSlots](#containerslots)                       | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [stat_type1](#stattype)                                 | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [stat_value1](#statvalue)                               | INT          |          | NO   |     | 0       |       |                     |
| [stat_type2](#stattype)                                 | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [stat_value2](#statvalue)                               | INT          |          | NO   |     | 0       |       |                     |
| [stat_type3](#stattype)                                 | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [stat_value3](#statvalue)                               | INT          |          | NO   |     | 0       |       |                     |
| [stat_type4](#stattype)                                 | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [stat_value4](#statvalue)                               | INT          |          | NO   |     | 0       |       |                     |
| [stat_type5](#stattype)                                 | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [stat_value5](#statvalue)                               | INT          |          | NO   |     | 0       |       |                     |
| [stat_type6](#stattype)                                 | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [stat_value6](#statvalue)                               | INT          |          | NO   |     | 0       |       |                     |
| [stat_type7](#stattype)                                 | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [stat_value7](#statvalue)                               | INT          |          | NO   |     | 0       |       |                     |
| [stat_type8](#stattype)                                 | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [stat_value8](#statvalue)                               | INT          |          | NO   |     | 0       |       |                     |
| [stat_type9](#stattype)                                 | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [stat_value9](#statvalue)                               | INT          |          | NO   |     | 0       |       |                     |
| [stat_type10](#stattype)                                | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [stat_value10](#statvalue)                              | INT          |          | NO   |     | 0       |       |                     |
| [ScalingStatDistribution](#scalingstatdistribution)     | SMALLINT     |          | NO   |     | 0       |       |                     |
| [ScalingStatValue](#scalingstatvalue)                   | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [dmg_min1](#dmgmin)                                     | FLOAT        |          | NO   |     | 0       |       |                     |
| [dmg_max1](#dmgmax)                                     | FLOAT        |          | NO   |     | 0       |       |                     |
| [dmg_type1](#dmgtype)                                   | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [dmg_min2](#dmgmin)                                     | FLOAT        |          | NO   |     | 0       |       |                     |
| [dmg_max2](#dmgmax)                                     | FLOAT        |          | NO   |     | 0       |       |                     |
| [dmg_type2](#dmgtype)                                   | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [armor](#armor)                                         | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [holy_res](#holyres)                                    | SMALLINT     |          | YES  |     | NULL    |       |                     |
| [fire_res](#fireres)                                    | SMALLINT     |          | YES  |     | NULL    |       |                     |
| [nature_res](#natureres)                                | SMALLINT     |          | YES  |     | NULL    |       |                     |
| [frost_res](#frostres)                                  | SMALLINT     |          | YES  |     | NULL    |       |                     |
| [shadow_res](#shadowres)                                | SMALLINT     |          | YES  |     | NULL    |       |                     |
| [arcane_res](#arcaneres)                                | SMALLINT     |          | YES  |     | NULL    |       |                     |
| [delay](#delay)                                         | SMALLINT     | UNSIGNED | NO   |     | 1000    |       |                     |
| [ammo_type](#ammotype)                                  | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [RangedModRange](#rangedmodrange)                       | FLOAT        |          | NO   |     | 0       |       |                     |
| [spellid_1](#spellid)                                   | INT          |          | NO   |     | 0       |       |                     |
| [spelltrigger_1](#spelltrigger)                         | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [spellcharges_1](#spellcharges)                         | SMALLINT     |          | NO   |     | 0       |       |                     |
| [spellppmRate_1](#spellppmrate)                         | FLOAT        |          | NO   |     | 0       |       |                     |
| [spellcooldown_1](#spellcooldown)                       | INT          |          | NO   |     | -1      |       |                     |
| [spellcategory_1](#spellcategory)                       | SMALLINT     | UNSIGNED | NO   |     | 0       |       |                     |
| [spellcategorycooldown_1](#spellcategorycooldown)       | INT          |          | NO   |     | -1      |       |                     |
| [spellid_2](#spellid)                                   | INT          |          | NO   |     | 0       |       |                     |
| [spelltrigger_2](#spelltrigger)                         | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [spellcharges_2](#spellcharges)                         | SMALLINT     |          | NO   |     | 0       |       |                     |
| [spellppmRate_2](#spellppmrate)                         | FLOAT        |          | NO   |     | 0       |       |                     |
| [spellcooldown_2](#spellcooldown)                       | INT          |          | NO   |     | -1      |       |                     |
| [spellcategory_2](#spellcategory)                       | SMALLINT     | UNSIGNED | NO   |     | 0       |       |                     |
| [spellcategorycooldown_2](#spellcategorycooldown)       | INT          |          | NO   |     | -1      |       |                     |
| [spellid_3](#spellid)                                   | INT          |          | NO   |     | 0       |       |                     |
| [spelltrigger_3](#spelltrigger)                         | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [spellcharges_3](#spellcharges)                         | SMALLINT     |          | NO   |     | 0       |       |                     |
| [spellppmRate_3](#spellppmrate)                         | FLOAT        |          | NO   |     | 0       |       |                     |
| [spellcooldown_3](#spellcooldown)                       | INT          |          | NO   |     | -1      |       |                     |
| [spellcategory_3](#spellcategory)                       | SMALLINT     | UNSIGNED | NO   |     | 0       |       |                     |
| [spellcategorycooldown_3](#spellcategorycooldown)       | INT          |          | NO   |     | -1      |       |                     |
| [spellid_4](#spellid)                                   | INT          |          | NO   |     | 0       |       |                     |
| [spelltrigger_4](#spelltrigger)                         | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [spellcharges_4](#spellcharges)                         | SMALLINT     |          | NO   |     | 0       |       |                     |
| [spellppmRate_4](#spellppmrate)                         | FLOAT        |          | NO   |     | 0       |       |                     |
| [spellcooldown_4](#spellcooldown)                       | INT          |          | NO   |     | -1      |       |                     |
| [spellcategory_4](#spellcategory)                       | SMALLINT     | UNSIGNED | NO   |     | 0       |       |                     |
| [spellcategorycooldown_4](#spellcategorycooldown)       | INT          |          | NO   |     | -1      |       |                     |
| [spellid_5](#spellid)                                   | INT          |          | NO   |     | 0       |       |                     |
| [spelltrigger_5](#spelltrigger)                         | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [spellcharges_5](#spellcharges)                         | SMALLINT     |          | NO   |     | 0       |       |                     |
| [spellppmRate_5](#spellppmrate)                         | FLOAT        |          | NO   |     | 0       |       |                     |
| [spellcooldown_5](#spellcooldown)                       | INT          |          | NO   |     | -1      |       |                     |
| [spellcategory_5](#spellcategory)                       | SMALLINT     | UNSIGNED | NO   |     | 0       |       |                     |
| [spellcategorycooldown_5](#spellcategorycooldown)       | INT          |          | NO   |     | -1      |       |                     |
| [bonding](#bonding)                                     | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [description](#description)                             | VARCHAR(255) |          | NO   |     | ''      |       |                     |
| [PageText](#pagetext)                                   | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [LanguageID](#languageid)                               | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [PageMaterial](#pagematerial)                           | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [startquest](#startquest)                               | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [lockid](#lockid)                                       | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [Material](#material)                                   | TINYINT      |          | NO   |     | 0       |       |                     |
| [sheath](#sheath)                                       | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [RandomProperty](#randomproperty)                       | INT          |          | NO   |     | 0       |       |                     |
| [RandomSuffix](#randomsuffix)                           | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [block](#block)                                         | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [itemset](#itemset)                                     | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [MaxDurability](#maxdurability)                         | SMALLINT     | UNSIGNED | NO   |     | 0       |       |                     |
| [area](#area)                                           | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [Map](#map)                                             | SMALLINT     |          | NO   |     | 0       |       |                     |
| [BagFamily](#bagfamily)                                 | INT          |          | NO   |     | 0       |       |                     |
| [TotemCategory](#totemcategory)                         | INT          |          | NO   |     | 0       |       |                     |
| [socketColor_1](#socketcolor)                           | TINYINT      |          | NO   |     | 0       |       |                     |
| [socketContent_1](#socketcontent)                       | INT          |          | NO   |     | 0       |       |                     |
| [socketColor_2](#socketcolor)                           | TINYINT      |          | NO   |     | 0       |       |                     |
| [socketContent_2](#socketcontent)                       | INT          |          | NO   |     | 0       |       |                     |
| [socketColor_3](#socketcolor)                           | TINYINT      |          | NO   |     | 0       |       |                     |
| [socketContent_3](#socketcontent)                       | INT          |          | NO   |     | 0       |       |                     |
| [socketBonus](#socketbonus)                             | INT          |          | NO   |     | 0       |       |                     |
| [GemProperties](#gemproperties)                         | INT          |          | NO   |     | 0       |       |                     |
| [RequiredDisenchantSkill](#requireddisenchantskill)     | SMALLINT     |          | NO   |     | -1      |       |                     |
| [ArmorDamageModifier](#armordamagemodifier)             | FLOAT        |          | NO   |     | 0       |       |                     |
| [duration](#duration)                                   | INT          | UNSIGNED | NO   |     | 0       |       | Duration in seconds |
| [ItemLimitCategory](#itemlimitcategory)                 | SMALLINT     |          | NO   |     | 0       |       |                     |
| [HolidayId](#holidayid)                                 | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [ScriptName](#scriptname)                               | VARCHAR(64)  |          | NO   |     | ''      |       |                     |
| [DisenchantID](#disenchantid)                           | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [FoodType](#foodtype)                                   | TINYINT      | UNSIGNED | NO   |     | 0       |       |                     |
| [minMoneyLoot](#minmoneyloot)                           | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [maxMoneyLoot](#maxmoneyloot)                           | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [flagsCustom](#flagscustom)                             | INT          | UNSIGNED | NO   |     | 0       |       |                     |
| [VerifiedBuild](#verifiedbuild)                         | INT          |          | YES  |     | NULL    |       | (WDBVerified)       |

**Description of the table's fields**

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

| Value      | Hex          | Flag                           | Comment                                                                                                                                                             |
| :--------- | :----------: | :----------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1          | `0x00000001` | ITEM_FLAG_NO_PICKUP            | (NOT IMPLEMENTED)                                                                                                                                                   |
| 2          | `0x00000002` |                                | Conjured item                                                                                                                                                       |
| 4          | `0x00000004` |                                | Openable (can be opened by right-click)                                                                                                                             |
| 8          | `0x00000008` | ITEM_FLAG_HEROIC_TOOLTIP       | (NOT IMPLEMENTED) - Makes green "Heroic" text appear on item                                                                                                        |
| 16         | `0x00000010` | ITEM_FLAG_DEPRECATED           | (NOT IMPLEMENTED) - Deprecated Item                                                                                                                                 |
| 32         | `0x00000020` |                                | Item cannot be destroyed, except by using spell (item can be reagent for spell)                                                                                     |
| 64         | `0x00000040` | ITEM_FLAG_PLAYERCAST           | (NOT IMPLEMENTED) - Item's spells are castable by players                                                                                                           |
| 128        | `0x00000080` | ITEM_FLAG_NO_EQUIP_COOLDOWN    | No default 30 seconds cooldown when the item is equipped                                                                                                            |
| 256        | `0x00000100` | ITEM_FLAG_MULTI_LOOT_QUEST     | (NOT IMPLEMENTED)                                                                                                                                                   |
| 512        | `0x00000200` |                                | Wrapper : Item can wrap other items                                                                                                                                 |
| 1024       | `0x00000400` | ITEM_FLAG_USES_RESOURCES       | (NOT IMPLEMENTED)                                                                                                                                                   |
| 2048       | `0x00000800` |                                | Item is party loot and can be looted by all                                                                                                                         |
| 4096       | `0x00001000` |                                | Item is refundable                                                                                                                                                  |
| 8192       | `0x00002000` |                                | Charter (Arena or Guild)                                                                                                                                            |
| 16384      | `0x00004000` | ITEM_FLAG_HAS_TEXT             | (NOT IMPLEMENTED) - Only readable items have this (but not all)                                                                                                     |
| 32768      | `0x00008000` | ITEM_FLAG_NO_DISENCHANT        | (NOT IMPLEMENTED) - If enabled, prevent disenchanting. Implemented in another column `RequiredDisenchantSkill`                                                      |
| 65536      | `0x00010000` | ITEM_FLAG_REAL_DURATION        | (NOT IMPLEMENTED) - Probably real time duration. Implemented in another column `flagsCustom`                                                                        |
| 131072     | `0x00020000` | ITEM_FLAG_NO_CREATOR           | (NOT IMPLEMENTED OR PARTIALLY) - Maybe to remove the "Made by XX" message on crafted/summoned item or for signing charters                                          |
| 262144     | `0x00040000` |                                | Item can be prospected                                                                                                                                              |
| 524288     | `0x00080000` |                                | Unique equipped (player can only have one equipped at the same time but as many as they want in their bags, if maxcount = 1, it will still display Unique-Equipped) |
| 1048576    | `0x00100000` | ITEM_FLAG_IGNORE_FOR_AURAS     | (NOT IMPLEMENTED) - ??                                                                                                                                              |
| 2097152    | `0x00200000` |                                | Item can be used during arena match                                                                                                                                 |
| 4194304    | `0x00400000` |                                | Throwable (for tooltip ingame)                                                                                                                                      |
| 8388608    | `0x00800000` |                                | Item can be used in shapeshift forms                                                                                                                                |
| 16777216   | `0x01000000` | ITEM_FLAG_HAS_QUEST_GLOW       | (NOT IMPLEMENTED)                                                                                                                                                   |
| 33554432   | `0x02000000` |                                | Profession recipes: can only be looted if you meet requirements and don't already know it                                                                           |
| 67108864   | `0x04000000` |                                | Item cannot be used in arena                                                                                                                                        |
| 134217728  | `0x08000000` |                                | Bind to Account (Requires to set Bonding > 0)                                                                                                                       |
| 268435456  | `0x10000000` | ITEM_FLAG_NO_REAGENT_COST      | Spell is cast with triggered flag (in code it's written `Spell is cast ignoring reagents`)                                                                          |
| 536870912  | `0x20000000` |                                | Millable                                                                                                                                                            |
| 1073741824 | `0x40000000` | ITEM_FLAG_REPORT_TO_GUILD_CHAT | (NOT IMPLEMENTED)                                                                                                                                                   |
| 2147483648 | `0x80000000` | ITEM_FLAG_NO_PROGRESSIVE_LOOT  | (NOT IMPLEMENTED)                                                                                                                                                   |

### FlagsExtra

| Value      | Hex          | Flag                                             | Comment                                                          |
| :--------- | :----------: | :----------------------------------------------- | :--------------------------------------------------------------- |
| 1          | `0x00000001` | ITEM_FLAG2_FACTION_HORDE                         | Horde Only                                                       |
| 2          | `0x00000002` | ITEM_FLAG2_FACTION_ALLIANCE                      | Alliance Only                                                    |
| 4          | `0x00000004` | ITEM_FLAG2_DONT_IGNORE_BUY_PRICE                 | When item uses ExtendedCost in npc_vendor, gold is also required |
| 8          | `0x00000008` | ITEM_FLAG2_CLASSIFY_AS_CASTER                    | NYI - Unused in item_template                                    |
| 16         | `0x00000010` | ITEM_FLAG2_CLASSIFY_AS_PHYSICAL                  | NYI                                                              |
| 32         | `0x00000020` | ITEM_FLAG2_EVERYONE_CAN_ROLL_NEED                | Anyone can roll need                                             |
| 64         | `0x00000040` | ITEM_FLAG2_NO_TRADE_BIND_ON_ACQUIRE              | NYI - Unused in item_template                                    |
| 128        | `0x00000080` | ITEM_FLAG2_CAN_TRADE_BIND_ON_ACQUIRE             | NYI - Unused in item_template                                    |
| 256        | `0x00000100` | ITEM_FLAG2_CAN_ONLY_ROLL_GREED                   | Makes need roll for this item disabled                           |
| 512        | `0x00000200` | ITEM_FLAG2_CASTER_WEAPON                         | NYI                                                              |
| 1024       | `0x00000400` | ITEM_FLAG2_DELETE_ON_LOGIN                       | NYI - Unused in item_template                                    |
| 2048       | `0x00000800` | ITEM_FLAG2_INTERNAL_ITEM                         | NYI - Unused in item_template                                    |
| 4096       | `0x00001000` | ITEM_FLAG2_NO_VENDOR_VALUE                       | NYI - Unused in item_template                                    |
| 8192       | `0x00002000` | ITEM_FLAG2_SHOW_BEFORE_DISCOVERED                | NYI                                                              |
| 16384      | `0x00004000` | ITEM_FLAG2_OVERRIDE_GOLD_COST                    | NYI - Unused in item_template                                    |
| 32768      | `0x00008000` | ITEM_FLAG2_IGNORE_DEFAULT_RATED_BG_RESTRICTIONS  | NYI                                                              |
| 65536      | `0x00010000` | ITEM_FLAG2_NOT_USABLE_IN_RATED_BG                | NYI                                                              |
| 131072     | `0x00020000` | ITEM_FLAG2_BNET_ACCOUNT_TRADE_OK                 | NYI                                                              |
| 262144     | `0x00040000` | ITEM_FLAG2_CONFIRM_BEFORE_USE                    | NYI - Unused in item_template                                    |
| 524288     | `0x00080000` | ITEM_FLAG2_REEVALUATE_BONDING_ON_TRANSFORM       | NYI - Unused in item_template                                    |
| 1048576    | `0x00100000` | ITEM_FLAG2_NO_TRANSFORM_ON_CHARGE_DEPLETION      | NYI - Unused in item_template                                    |
| 2097152    | `0x00200000` | ITEM_FLAG2_NO_ALTER_ITEM_VISUAL                  | NYI                                                              |
| 4194304    | `0x00400000` | ITEM_FLAG2_NO_SOURCE_FOR_ITEM_VISUAL             | NYI                                                              |
| 8388608    | `0x00800000` | ITEM_FLAG2_IGNORE_QUALITY_FOR_ITEM_VISUAL_SOURCE | NYI - Unused in item_template                                    |
| 16777216   | `0x01000000` | ITEM_FLAG2_NO_DURABILITY                         | NYI - Unused in item_template                                    |
| 33554432   | `0x02000000` | ITEM_FLAG2_ROLE_TANK                             | NYI - Unused in item_template                                    |
| 67108864   | `0x04000000` | ITEM_FLAG2_ROLE_HEALER                           | NYI - Unused in item_template                                    |
| 134217728  | `0x08000000` | ITEM_FLAG2_ROLE_DAMAGE                           | NYI - Unused in item_template                                    |
| 268435456  | `0x10000000` | ITEM_FLAG2_CAN_DROP_IN_CHALLENGE_MODE            | NYI - Unused in item_template                                    |
| 536870912  | `0x20000000` | ITEM_FLAG2_NEVER_STACK_IN_LOOT_UI                | NYI - Unused in item_template                                    |
| 1073741824 | `0x40000000` | ITEM_FLAG2_DISENCHANT_TO_LOOT_TABLE              | NYI - Unused in item_template                                    |
| 2147483648 | `0x80000000` | ITEM_FLAG2_USED_IN_A_TRADESKILL                  | NYI - Unused in item_template                                    |

### BuyCount

The size of the item stack when sold by vendors. Also if a vendor has limited copies of this item available, everytime the vendor list is refreshed (See [npc\_vendor.incrtime](http://www.azerothcore.org/wiki/npc_vendor#incrtime)), the number of copies increases by this number.

### BuyPrice

The price required to pay to buy this item from a vendor, in copper.

### SellPrice

The price that the vendor will pay you for the item when you sell it and if it is possible to be sold, in copper. Put in 0 if the item cannot be sold to a vendor.

### InventoryType

Which slot the Item will be equipped on.

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

Bitmask controlling which classes can use this item. Add ids together to combine class possibilities. Use -1 if all classes can use it.

See the [ChrClasses DBC file](chrclasses) for the IDs of the classes.

### AllowableRace

Bitmask controlling which races can use this item. Add ids together to combine race possibilities. Use -1 for all races.

See the [ChrRaces DBC file](chrraces) for the IDs of the races.

### ItemLevel

Base item level.

### RequiredLevel

The level that a player must be to equip the item.

### RequiredSkill

The skill required to use this item. See the [SkillLine DBC file](skillline) for IDs which can be used here.

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

See the [Faction DBC file](faction) for the IDs of all of the factions.

### RequiredReputationRank

The rank the player has to have with the faction from [RequiredReputationFaction](#requiredreputationfaction).

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

The proc per minute rate controlling how often the spell is triggered (if [\#spelltrigger](#spelltrigger) == 2).

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

The ID referring to the text that the item will show (if it is a book or a letter, etc). The item will have a magnifying glass cursor in the game and will show the text when right-clicked. See [page\_text.ID](page_text#id)

### LanguageID

The language that the item text is written in.

See the [Languages DBC file](languages) for the IDs of all of the languages.

### PageMaterial

The background texture that appears in the page text window.

See the [PageTextMaterial DBC file](pagetextmaterial) for the IDs of all of the material types.

### startquest

The ID of the quest that this item will start if right-clicked. See [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id)

### lockid

The lock entry ID that this item (which serves as a key) is tied to. This field is used in key-door mechanics.

See the [Lock DBC file](https://wowdev.wiki/DB/Lock).

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
| 7   | Off hand          | On the right-hand side of the character's waist. |

### RandomProperty

The number in this field points to [item\_enchantment\_template.entry](http://www.azerothcore.org/wiki/item_enchantment_template#entry) and ties in an item's chance at having a random property attached to it when it shows up for the first time. This field and the [RandomSuffix](#randomsuffix) field CANNOT both have non-zero values. Either one is filled, or the other. Also, the primary source for the number in this field are WDBs.

### RandomSuffix

The number in this field points to [item\_enchantment\_template.entry](http://www.azerothcore.org/wiki/item_enchantment_template#entry) and ties in an item's chance at having a random suffix attached to it when it shows up for the first time. This field and the [RandomProperty](#randomproperty) field CANNOT both have non-zero values. Either one is filled, or the other. Also, the primary source for the number in this field are WDBs.

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

| Value | Hex      | Flag                    | Comment |
| :---- | :------: | :---------------------- | :------ |
| 0     | `0x0000` | None                    |         |
| 1     | `0x0001` | Arrows                  |         |
| 2     | `0x0002` | Bullets                 |         |
| 4     | `0x0004` | Soul Shards             |         |
| 8     | `0x0008` | Leatherworking Supplies |         |
| 16    | `0x0010` | Inscription Supplies    |         |
| 32    | `0x0020` | Herbs                   |         |
| 64    | `0x0040` | Enchanting Supplies     |         |
| 128   | `0x0080` | Engineering Supplies    |         |
| 256   | `0x0100` | Keys                    |         |
| 512   | `0x0200` | Gems                    |         |
| 1024  | `0x0400` | Mining Supplies         |         |
| 2048  | `0x0800` | Soulbound Equipment     |         |
| 4096  | `0x1000` | Vanity Pets             |         |
| 8192  | `0x2000` | Currency Tokens         |         |
| 16384 | `0x4000` | Quest Items             |         |

### TotemCategory

Corresponds to the ID in the [TotemCategory DBC file](totemcategory).

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

| Value | Hex    | Flag   | Comment |
| :---- | :----: | :----- | :------ |
| 1     | `0x01` | Meta   |         |
| 2     | `0x02` | Red    |         |
| 4     | `0x04` | Yellow |         |
| 8     | `0x08` | Blue   |         |

### socketContent

Amount of Gems of SocketColor1

### socketBonus

Commonly used socket bonus IDs

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

The value here corresponds to the ID in GemProperties.dbc.

### RequiredDisenchantSkill

The required proficiency in disenchanting that the player needs to have to be able to disenchant this item.
If set to -1, the item can't be disenchanted.

### ArmorDamageModifier

Part of the item's [armor](#armor) that counts as bonus armor. It is taken off the base armor and added back as bonus armor, so effects that increase the armor from items only affect the rest.

### duration

The duration of the item in seconds ingame time.
Set ITEM\_FLAGS\_CU\_DURATION\_REAL\_TIME in *flagsCustom* for real time. In that case the item duration will tick even if player is offline.

### ItemLimitCategory

This is related to ItemLimitCategory.dbc.
It is a property that defines if an item belongs to a "category", like "Mana Gems" or "Healthstone" and it defines how many items of the category you can have in the bag (this is the "limit").
For example, for Healthstone, there are several items like "Lesser Healthstone, Greater Healthstone, etc." but you can have only one in your bag (check as example value 3 or 4).

### HolidayId

See the [Holidays DBC file](holidays) for the IDs of all of the holidays.

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

| Value | Hex    | Flag                              | Comment                                                              |
| :---- | :----: | :-------------------------------- | :------------------------------------------------------------------- |
| 1     | `0x01` | ITEM_FLAGS_CU_DURATION_REAL_TIME  | Item duration will tick even if player is offline                    |
| 2     | `0x02` | ITEM_FLAGS_CU_IGNORE_QUEST_STATUS | No quest status will be checked when this item drops                 |
| 4     | `0x04` | ITEM_FLAGS_CU_FOLLOW_LOOT_RULES   | Item will always follow group/master/need before greed looting rules |

### VerifiedBuild

This field was used to determine whether a template has been verified from WDB files.
- If value is 0 then it has not been parsed yet.
- If value is above 0 then it has been parsed with WDB files from that specific client build.
- If value is -1 then it is just a place holder until proper data are found on WDBs.

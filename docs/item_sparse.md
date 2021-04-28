# item\_sparse

**`Back-to:Hotfixes`**

**The \`item\_appearance\` table**

This table holds information on every applied item hotfix and can overwrite existing items within the game. Together with item, item\_modified\_appearance and item\_modified\_appearance they present the means to hotfix an item.

**Structure**

| Field                                                                     | Type        | Attributes | Key | Null | Default | Extra | Comment                  |
|---------------------------------------------------------------------------|-------------|------------|-----|------|---------|-------|--------------------------|
| [ID](#item_sparse-ID)                                                     | int(10)     | unsigned   | PRI | NO   | 0       |       |                          |
| [Quality](#item_sparse-Quality)                                           | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [Flags](#item_sparse-Flags)                                               | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [Unk1](#item_sparse-Unk1)                                                 | FLOAT       | signed     |     | NO   | 0       |       |                          |
| [Unk2](#item_sparse-Unk2)                                                 | FLOAT       | signed     |     | NO   | 0       |       |                          |
| [BuyCount](#item_sparse-BuyCount)                                         | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [BuyPrice](#item_sparse-BuyPrice)                                         | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [SellPrice](#item_sparse-SellPrice)                                       | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [InventoryType](#item_sparse-InventoryType)                               | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [AllowableClass](#item_sparse-AllowableClass)                             | int(11)     | signed     |     | NO   | 0       |       |                          |
| [AllowableRace](#item_sparse-AllowableRace)                               | int(11)     | signed     |     | NO   | 0       |       |                          |
| [ItemLevel](#item_sparse-ItemLevel)                                       | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [RequiredLevel](#item_sparse-RequiredLevel)                               | int(10)     | signed     |     | NO   | 0       |       |                          |
| [RequiredSkill](#item_sparse-RequiredSkill)                               | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [RequiredSkillRank](#item_sparse-RequiredSkillRank)                       | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [RequiredSpell](#item_sparse-RequiredSpell)                               | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [RequiredHonorRank](#item_sparse-RequiredHonorRank)                       | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [RequiredCityRank](#item_sparse-RequiredCityRank)                         | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [RequiredReputationFaction](#item_sparse-RequiredReputationFaction)       | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [RequiredReputationRank](#item_sparse-RequiredReputationRank)             | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [MaxCount](#item_sparse-MaxCount)                                         | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [Stackable](#item_sparse-Stackable)                                       | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [ContainerSlots](#item_sparse-ContainerSlots)                             | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [ItemStatType](#item_sparse-ItemStatType)                                 | int(11)     | signed     |     | NO   | 0       |       |                          |
| [ItemStatValue](#item_sparse-ItemStatValue)                               | int(11)     | signed     |     | NO   | 0       |       |                          |
| [ItemStatAllocation](#item_sparse-ItemStatAllocation)                     | int(11)     | signed     |     | NO   | 0       |       |                          |
| [ItemStatSocketCostMultiplier](#item_sparse-ItemStatSocketCostMultiplier) | FLOAT       | signed     |     | NO   | 0       |       |                          |
| [ScalingStatDistribution](#item_sparse-ScalingStatDistribution)           | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [DamageType](#item_sparse-DamageType)                                     | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [Delay](#item_sparse-Delay)                                               | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [RangedModRange](#item_sparse-RangedModRange)                             | FLOAT       | signed     |     | NO   | 0       |       |                          |
| [Bonding](#item_sparse-Bonding)                                           | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [Name](#item_sparse-Name)                                                 | TEXT        |            |     | YES  |         |       |                          |
| [Description](#item_sparse-Description)                                   | TEXT        |            |     | YES  |         |       |                          |
| [PageText](#item_sparse-PageText)                                         | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [LanguageID](#item_sparse-LanguageID)                                     | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [PageMaterial](#item_sparse-PageMaterial)                                 | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [StartQuest](#item_sparse-StartQuest)                                     | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [LockID](#item_sparse-LockID)                                             | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [Material](#item_sparse-Material)                                         | int(11)     | signed     |     | NO   | 0       |       |                          |
| [Sheath](#item_sparse-Sheath)                                             | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [RandomProperty](#item_sparse-RandomProperty)                             | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [RandomSuffix](#item_sparse-RandomSuffix)                                 | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [ItemSet](#item_sparse-ItemSet)                                           | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [Area](#item_sparse-Area)                                                 | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [Map](#item_sparse-Map)                                                   | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [BagFamily](#item_sparse-BagFamily)                                       | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [TotemCategory](#item_sparse-TotemCategory)                               | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [SocketColor](item_sparse)                                                | int(10)     | unsigned   |     | NO   | 0       |       | SocketColor1 can be NULL |
| [SocketBonus](#item_sparse-SocketBonus)                                   | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [GemProperties](#item_sparse-GemProperties)                               | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [ArmorDamageModifier](#item_sparse-ArmorDamageModifier)                   | FLOAT       | signed     |     | NO   | 0       |       |                          |
| [Duration](#item_sparse-Duration)                                         | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [ItemLimitCategory](#item_sparse-ItemLimitCategory)                       | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [HolidayID](#item_sparse-HolidayID)                                       | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [StatScalingFactor](#item_sparse-StatScalingFactor)                       | FLOAT       | signed     |     | NO   | 0       |       |                          |
| [CurrencySubstitutionID](#item_sparse-CurrencySubstitutionID)             | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [CurrencySubstitutionCount](#item_sparse-CurrencySubstitutionCount)       | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [ItemNameDescriptionID](#item_sparse-ItemNameDescriptionID)               | int(10)     | unsigned   |     | NO   | 0       |       |                          |
| [VerifiedBuild](#item_sparse-VerifiedBuild)                               | SMALLINT(6) | signed     |     | NO   | 0       |       |                          |

**Description of the fields**

### ID

The unique ID of the item.Choosing an existing item ID will overwrite that item ID with the hotfix changes.

### Quality

The quality of the item. To use the Bind to Battle.net account quality, the item must have its flags set to 134221824.

| ID | Color  | Quality                               |
|----|--------|---------------------------------------|
| 0  | Grey   | Poor                                  |
| 1  | White  | Common                                |
| 2  | Green  | Uncommon                              |
| 3  | Blue   | Rare                                  |
| 4  | Purple | Epic                                  |
| 5  | Orange | Legendary                             |
| 6  | Red    | Artifact                              |
| 7  | Gold   | Heirloom / Bind to Battle.net account |
| 8  | Aqua   | WoW Token                             |

### Flags

Flags1 to Flags3 are bitmask fields that contains flags that the item has on it. As all other such fields, just add the flags together to combine them. Possible flags are listed below.

 **Note:** The item system for 6xx  gives more than one flag bitmask field and each of these can be populated individually.

| Flag       |             | Comments                                                                                   |
|------------|-------------|--------------------------------------------------------------------------------------------|
| 1          | 0x01        | UNK1                                                                                       |
| 2          | 0x02        | Conjured item                                                                              |
| 4          | 0x04        | Openable (can be opened by right-click)                                                    |
| 8          | 0x08        | Makes green "Heroic" text appear on item                                                   |
| 16         | 0x010       | Deprecated Item                                                                            |
| 32         | 0x020       | Item can not be destroyed, except by using spell (item can be reagent for spell)           |
| 64         | 0x040       | UNK2                                                                                       |
| 128        | 0x080       | No default 30 seconds cooldown when equipped                                               |
| 256        | 0x0100      | UNK3                                                                                       |
| 512        | 0x0200      | Wrapper : Item can wrap other items                                                        |
| 1024       | 0x0400      | UNK4                                                                                       |
| 2048       | 0x0800      | Item is party loot and can be looted by all                                                |
| 4096       | 0x01000     | Item is refundable                                                                         |
| 8192       | 0x02000     | Charter (Arena or Guild)                                                                   |
| 16384      | 0x04000     | UNK5 // comment in code : Only readable items have this (but not all)                      |
| 32768      | 0x08000     | UNK6                                                                                       |
| 65536      | 0x010000    | UNK7                                                                                       |
| 131072     | 0x020000    | UNK8                                                                                       |
| 262144     | 0x040000    | Item can be prospected                                                                     |
| 524288     | 0x080000    | Unique equipped (player can only have one equipped at the same time)                       |
| 1048576    | 0x0100000   | UNK9                                                                                       |
| 2097152    | 0x0200000   | Item can be used during arena match                                                        |
| 4194304    | 0x0400000   | Throwable (for tooltip ingame)                                                             |
| 8388608    | 0x0800000   | Item can be used in shapeshift forms                                                       |
| 16777216   | 0x01000000  |  UNK10                                                                                     |
| 54432      | 0x02000000  |  Profession recipes: can only be looted if you meet requirements and don't already know it |
| 67108864   | 0x04000000  |  Item cannot be used in arena                                                              |
| 134217728  | 0x08000000  | Bind to Account (Also needs Quality = 7 set)                                               |
| 268435456  | 0x010000000 | Spell is cast with triggered flag                                                          |
| 536870912  | 0x020000000 | Millable                                                                                   |
| 1073741824 | 0x040000000 |  UNK11                                                                                     |
| 2147483648 | 0x080000000 | Bind on Pickup tradeable8192                                                               |

### Unk1

`field-no-description|6`

### Unk2

`field-no-description|7`

### BuyCount

The size of the item stack when sold by vendors. Also if a vendor has limited copies of this item available, everytime the vendor list is refreshed (See [npc\_vendor.incrtime](npc_vendor_2130245.html#npc_vendor-incrtime)), the number of copies increases by this number.

### BuyPrice

The price required to pay to buy this item from a vendor, in copper.

### SellPrice

The price that the vendor will pay you for the item when you sell it and if it is possible to be sold, in copper. Put in 0 if the item cannot be sold to a vendor.

### InventoryType

In what slot the item can be equipped.

| ID | Slot Name     | ID | Slot Name                  |
|----|---------------|----|----------------------------|
| 0  | Non equipable | 15 | Ranged (Bows)              |
| 1  | Head          | 16 | Back                       |
| 2  | Neck          | 17 | Two-Hand                   |
| 3  | Shoulder      | 18 | Bag                        |
| 4  | Shirt         | 19 | Tabard                     |
| 5  | Chest         | 20 | Robe                       |
| 6  | Waist         | 21 | Main hand                  |
| 7  | Legs          | 22 | Off hand                   |
| 8  | Feet          | 23 | Holdable (Tome)            |
| 9  | Wrists        | 24 | Ammo                       |
| 10 | Hands         | 25 | Thrown                     |
| 11 | Finger        | 26 | Ranged right (Wands, Guns) |
| 12 | Trinket       | 27 | Quiver                     |
| 13 | Weapon        | 28 | Relic                      |
| 14 | Shield        |    |                            |

### AllowableClass

Bitmask controlling which classes can use this item. Add ids together to combine class possibilities. Use -1 if all classes can use it.

See the ChrClasses DBC file for the IDs of the classes.

### AllowableRace

Bitmask controlling which races can use this item. Add ids together to combine race possibilities. Use -1 for all races.

See the ChrRaces DBC file for the IDs of the races.

### ItemLevel

Base item level.

### RequiredLevel

The level that a player must be to equip the item.

### RequiredSkill

The skill required to use this item. See the [SkillLine DBC file](SkillLine6x) for IDs which can be used here.

### RequiredSkillRank

The required skill rank the player needs to have to use this item.

### RequiredSpell

The required spell that the player needs to have to use this item.

### RequiredHonorRank

The honor rank the player needs to have to use this item.

### RequiredCityRank

`field-no-description|20`

### RequiredReputationFaction

The faction template ID  of the faction that the player has to have a certain ranking with. If this value is 0, the faction of the seller of the item is used.

See the [Faction DBC file](Faction6x) for the IDs of all of the factions.

### RequiredReputationRank

The rank the player has to have with the faction from [RequiredReputationFaction](#item_sparse-RequiredReputationFaction).

| ID | Rank       |
|----|------------|
| 0  | Hated      |
| 1  | Hostile    |
| 2  | Unfriendly |
| 3  | Neutral    |
| 4  | Friendly   |
| 5  | Honored    |
| 6  | Revered    |
| 7  | Exalted    |

### MaxCount

Maximum number of copies of this item a player can have. Use 0 for infinite.

### Stackable

The number of copies of this item that can be stacked in the same slot.

### ContainerSlots

If the item is a bag, this field controls the number of slots the bag has.

### ItemStatType

The type of stat to modify. A maximum of 10 stats can be set as seen by the column count.

| ID | Stat Type                         |
|----|-----------------------------------|
| 0  | ITEM_MOD_MANA                     |
| 1  | ITEM_MOD_HEALTH                   |
| 3  | ITEM_MOD_AGILITY                  |
| 4  | ITEM_MOD_STRENGTH                 |
| 5  | ITEM_MOD_INTELLECT                |
| 6  | ITEM_MOD_SPIRIT                   |
| 7  | ITEM_MOD_STAMINA                  |
| 12 | ITEM_MOD_DEFENSE_SKILL_RATING     |
| 13 | ITEM_MOD_DODGE_RATING             |
| 14 | ITEM_MOD_PARRY_RATING             |
| 15 | ITEM_MOD_BLOCK_RATING             |
| 16 | ITEM_MOD_HIT_MELEE_RATING         |
| 17 | ITEM_MOD_HIT_RANGED_RATING        |
| 18 | ITEM_MOD_HIT_SPELL_RATING         |
| 19 | ITEM_MOD_CRIT_MELEE_RATING        |
| 20 | ITEM_MOD_CRIT_RANGED_RATING       |
| 21 | ITEM_MOD_CRIT_SPELL_RATING        |
| 22 | ITEM_MOD_HIT_TAKEN_MELEE_RATING   |
| 23 | ITEM_MOD_HIT_TAKEN_RANGED_RATING  |
| 24 | ITEM_MOD_HIT_TAKEN_SPELL_RATING   |
| 25 | ITEM_MOD_CRIT_TAKEN_MELEE_RATING  |
| 26 | ITEM_MOD_CRIT_TAKEN_RANGED_RATING |
| 27 | ITEM_MOD_CRIT_TAKEN_SPELL_RATING  |
| 28 | ITEM_MOD_HASTE_MELEE_RATING       |
| 29 | ITEM_MOD_HASTE_RANGED_RATING      |
| 30 | ITEM_MOD_HASTE_SPELL_RATING       |
| 31 | ITEM_MOD_HIT_RATING               |
| 32 | ITEM_MOD_CRIT_RATING              |
| 33 | ITEM_MOD_HIT_TAKEN_RATING         |
| 34 | ITEM_MOD_CRIT_TAKEN_RATING        |
| 35 | ITEM_MOD_RESILIENCE_RATING        |
| 36 | ITEM_MOD_HASTE_RATING             |
| 37 | ITEM_MOD_EXPERTISE_RATING         |
| 38 | ITEM_MOD_ATTACK_POWER             |
| 39 | ITEM_MOD_RANGED_ATTACK_POWER      |
| 40 | ITEM_MOD_VERSATILITY              |
| 41 | ITEM_MOD_SPELL_HEALING_DONE       |
| 42 | ITEM_MOD_SPELL_DAMAGE_DONE        |
| 43 | ITEM_MOD_MANA_REGENERATION        |
| 44 | ITEM_MOD_ARMOR_PENETRATION_RATING |
| 45 | ITEM_MOD_SPELL_POWER              |
| 46 | ITEM_MOD_HEALTH_REGEN             |
| 47 | ITEM_MOD_SPELL_PENETRATION        |
| 48 | ITEM_MOD_BLOCK_VALUE              |
| 49 | ITEM_MOD_MASTERY_RATING           |
| 50 | ITEM_MOD_EXTRA_ARMOR              |
| 51 | ITEM_MOD_FIRE_RESISTANCE          |
| 52 | ITEM_MOD_FROST_RESISTANCE         |
| 53 | ITEM_MOD_HOLY_RESISTANCE          |
| 54 | ITEM_MOD_SHADOW_RESISTANCE        |
| 55 | ITEM_MOD_NATURE_RESISTANCE        |
| 56 | ITEM_MOD_ARCANE_RESISTANCE        |
| 57 | ITEM_MOD_PVP_POWER                |
| 58 | ITEM_MOD_CR_AMPLIFY               |
| 59 | ITEM_MOD_CR_MULTISTRIKE           |
| 60 | ITEM_MOD_CR_READINESS             |
| 61 | ITEM_MOD_CR_SPEED                 |
| 62 | ITEM_MOD_CR_LIFESTEAL             |
| 63 | ITEM_MOD_CR_AVOIDANCE             |
| 64 | ITEM_MOD_CR_STURDINESS            |
| 65 | ITEM_MOD_CR_UNUSED_7              |
| 66 | ITEM_MOD_CR_CLEAVE                |
| 67 | ITEM_MOD_CR_UNUSED_9              |
| 68 | ITEM_MOD_CR_UNUSED_10             |
| 69 | ITEM_MOD_CR_UNUSED_11             |
| 70 | ITEM_MOD_CR_UNUSED_12             |
| 71 | ITEM_MOD_AGI_STR_INT              |
| 72 | ITEM_MOD_AGI_STR                  |
| 73 | ITEM_MOD_AGI_INT                  |
| 74 | ITEM_MOD_STR_INT                  |

### ItemStatValue

The value to change the stat type to. A maximum of 10 stats can be set as seen by the column count.

### ItemStatAllocation

Determines the amount of stats. A maximum of 10 stats can be set as seen by the column count.

### ItemStatSocketCostMultiplier

`field-no-description|56 -> 65`

### ScalingStatDistribution

Similar to Static Stats whom are the Stats that grow along with the users level (mainly heirloom leveling gear).
Use this like the static stats.

### DamageType

The damage type that the item uses.

| ID | Damage Type |
|----|-------------|
| 0  | Physical    |
| 1  | Holy        |
| 2  | Fire        |
| 3  | Nature      |
| 4  | Frost       |
| 5  | Shadow      |
| 6  | Arcane      |

### Delay

The time in milliseconds between successive hits.

### RangedModRange

Range Modifier for bows/guns/crossbows: Default range is somewhere between 0.3 and 0.4 yards,

Note: All blizzard ranged weapons have RangedModRange of 100.

### Bonding

The bonding for the item.

| ID | Bonding Type         |
|----|----------------------|
| 0  | No bounds            |
| 1  | Binds when picked up |
| 2  | Binds when equipped  |
| 3  | Binds when used      |
| 4  | Quest item           |
| 5  | Quest Item1          |

### Name

The name of the item.

Note: Name2, Name3 and Name4 are kept empty.

### Description

The description that appears in orange letters at the bottom of the item tooltip.

### PageText

The ID referring to the text that the item will show (if it is a book or a letter, etc). The item will have a magnifying glass cursor in the game and will show the text when right-clicked. See [page\_text.entry](page_text#page_text-entry)

### LanguageID

The language that the item text is written in.

See the [Languages DBC file](Languages) for the IDs of all of the languages.

### PageMaterial

The background texture that appears in the page text window.

See the [PageTextMaterial DBC file](PageTextMaterial) for the IDs of all of the material types.

### StartQuest

The ID of the quest that this item will start if right-clicked. See [quest\_template.id](quest_template#quest_template-entry)

### LockID

The lock entry ID that this item (which serves as a key) is tied to. This field is used in key-door mechanics.

See the [Lock DBC file](Lock).

### Material

The material that the item is made of. The value here affects the sound that the item makes when moved. Use -1 for consumable items like food, reagents, etc.

| ID | Material    | Comment                |
|----|-------------|------------------------|
| -1 | Consumables | Food, reagents, etc... |
| 0  | Not Defined |                        |
| 1  | Metal       |                        |
| 2  | Wood        |                        |
| 3  | Liquid      |                        |
| 4  | Jewelry     |                        |
| 5  | Chain       |                        |
| 6  | Plate       |                        |
| 7  | Cloth       |                        |
| 8  | Leather     |                        |

### Sheath

Controls how the item is put away on the character. Press the 'Z' hotkey to sheath and unsheathe your weapons.

| ID | Type              | Position                                         |
|----|-------------------|--------------------------------------------------|
| 1  | Two Handed Weapon | Diagonally across the back pointing downwards.   |
| 2  | Staff             | Diagonally across the back pointing upwards.     |
| 3  | One Handed        | On the left-hand side of the character's waist.  |
| 4  | Shield            | On the middle of the character's back.           |
| 5  | Enchanter's Rod   |                                                  |
| 6  | Off hand          | On the right-hand side of the character's waist. |

### RandomProperty

The number in this field points to [item\_enchantment\_template.entry](item_enchantment_template#item_enchantment_template-entry) and ties in an item's chance at having a random property attached to it when it shows up for the first time. This field and the [RandomSuffix](item_template#item_template-RandomSuffix) field CANNOT both have non-zero values. Either one is filled, or the other. Also, the primary source for the number in this field are WDBs.

### RandomSuffix

The number in this field points to [item\_enchantment\_template.entry](item_enchantment_template#item_enchantment_template-entry) and ties in an item's chance at having a random suffix attached to it when it shows up for the first time. This field and the [RandomProperty](item_template#item_template-RandomProperty) field CANNOT both have non-zero values. Either one is filled, or the other. Also, the primary source for the number in this field are WDBs.

### ItemSet

The ID of the item set that this item belongs to. To save you some time, you CAN NOT make up new item sets. Item sets are defined in the ItemSet DBC file.

### Area

The ID of the zone in which this item can be used.

### Map

The ID of the map in which this item can be used.

### BagFamily

If the item is a bag, this field is a bitmask controlling what types of items can be put in this bag. You can combine different types by adding up the bit numbers.

| ID    | Bag Family Mask         |
|-------|-------------------------|
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

Corresponds to the ID in the TotemCategory DBC file.

| ID  | Name                     |
|-----|--------------------------|
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

### SocketColor

The color of the socket that can be placed in this item. A maximum of 3 socket colors can be set as seen by the column count.

| ID | Color  |
|----|--------|
| 1  | Meta   |
| 2  | Red    |
| 4  | Yellow |
| 8  | Blue   |

### SocketBonus

Commonly used socket bonus IDs

| ID   | Effect           |
|------|------------------|
| 3312 | +8 Strength      |
| 3313 | +8 Agility       |
| 3305 | +12 Stamina      |
| 3    | +8 Intellect     |
| 2872 | +9 Healing       |
| 3753 | +9 Spell Power   |
| 3877 | +16 Attack Power |

### GemProperties

The value here corresponds to the ID in GemProperties.dbc.

### ArmorDamageModifier

field-no-description|95

### Duration

The duration of the item in seconds ingame time.Set ITEM\_FLAGS\_CU\_DURATION\_REAL\_TIME in flags2 for real time. In that case the item duration will tick even if player is offline.

### ItemLimitCategory

field-no-description|97

### HolidayID

See the [Holidays DBC file](Holidays) for the IDs of all of the holidays.

### StatScalingFactor

The factor that is used during the scaling of stats.

### CurrencySubstitutionID

field-no-description|100

### CurrencySubstitutionCount

field-no-description|101

### ItemNameDescriptionID

field-no-description|102

### VerifiedBuild

This field was used to determine whether a template has been verified from WDB files.

If value is 0 then it has not been parsed yet.

If value is above 0 then it has been parsed with WDB files from that specific client build.

If value is -1 then it is just a place holder until proper data are found on WDBs.

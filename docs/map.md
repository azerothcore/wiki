---
redirect_from: "/Map"
---

# Map

**Map.dbc**

[`Back-to:DBC`](dbc-index)

This DBC contains the maps list.

**Version is : 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)  

## Structure

| Column | Field                     | Type   | map\_dbc column                                          | Comment                                                                                                                                      |
| :----: | :------------------------ | :----- | :------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| 0      | ID                        | uint32 | [ID](map_dbc#id)                                         |                                                                                                                                              |
| 1      | Directory                 | string | [Directory](map_dbc#directory)                           | reference to World\\Map\\ \[...\] \\                                                                                                         |
| 2      | InstanceType              | uint32 | [InstanceType](map_dbc#instancetype)                     | 0x100 - CAN\_CHANGE\_PLAYER\_DIFFICULTY                                                                                                      |
| 3      | Flags                     | uint32 | [Flags](map_dbc#flags)                                   | 0: none, 1: party, 2: raid, 3: pvp, 4: arena, &gt;=5: none (official from "IsInInstance()")                                                  |
| 4      | MapType                   | uint32 | [PVP](map_dbc#pvp)                                       | Boolean (1 = True, 0 = False)                                                                                                                |
| 5      | MapName_0                 | string | [MapName_Lang_enUS](map_dbc#mapnamelang)                 | [Localization](https://wowdev.wiki/Localization); displayed on World Map for example. Assumed enUS                                           |
| 6      | MapName_1                 | string | [MapName_Lang_enGB](map_dbc#mapnamelang)                 | Assumed enGB, not used in 3.3.5a                                                                                                             |
| 7      | MapName_2                 | string | [MapName_Lang_koKR](map_dbc#mapnamelang)                 | Assumed koKR                                                                                                                                 |
| 8      | MapName_3                 | string | [MapName_Lang_frFR](map_dbc#mapnamelang)                 | Assumed frFR                                                                                                                                 |
| 9      | MapName_4                 | string | [MapName_Lang_deDE](map_dbc#mapnamelang)                 | Assumed deDE                                                                                                                                 |
| 10     | MapName_5                 | string | [MapName_Lang_enCN](map_dbc#mapnamelang)                 | Assumed enCN, not used in 3.3.5a                                                                                                             |
| 11     | MapName_6                 | string | [MapName_Lang_zhCN](map_dbc#mapnamelang)                 | Assumed zhCN                                                                                                                                 |
| 12     | MapName_7                 | string | [MapName_Lang_enTW](map_dbc#mapnamelang)                 | Assumed enTW, not used in 3.3.5a                                                                                                             |
| 13     | MapName_8                 | string | [MapName_Lang_zhTW](map_dbc#mapnamelang)                 | Assumed zhTW                                                                                                                                 |
| 14     | MapName_9                 | string | [MapName_Lang_esES](map_dbc#mapnamelang)                 | Assumed esES                                                                                                                                 |
| 15     | MapName_10                | string | [MapName_Lang_esMX](map_dbc#mapnamelang)                 | Assumed esMX                                                                                                                                 |
| 16     | MapName_11                | string | [MapName_Lang_ruRU](map_dbc#mapnamelang)                 | Assumed ruRU                                                                                                                                 |
| 17     | MapName_12                | string | [MapName_Lang_ptPT](map_dbc#mapnamelang)                 | Assumed ptPT, not used in 3.3.5a                                                                                                             |
| 18     | MapName_13                | string | [MapName_Lang_ptBR](map_dbc#mapnamelang)                 | Assumed ptBR, not used in 3.3.5a                                                                                                             |
| 19     | MapName_14                | string | [MapName_Lang_itIT](map_dbc#mapnamelang)                 | Assumed itIT, not used in 3.3.5a                                                                                                             |
| 20     | MapName_15                | string | [MapName_Lang_Unk](map_dbc#mapnamelang)                  | Unknown language, unsure of the usage in 3.3.5a                                                                                              |
| 21     | MapName_lang_mask         | uint32 | [MapName_Lang_Mask](map_dbc#mapnamelang)                 | Assumed flags of the localized text                                                                                                          |
| 22     | AreaTableID               | uint32 | [AreaTableID](map_dbc#areatableid)                       | [AreaTableID](https://wowdev.wiki/DB/AreaTable): Ref-ID;. ID in [AreaTable.dbc](areatable)                                                   |
| 23     | MapDescription0_0         | string | [MapDescription0_Lang_enUS](map_dbc#mapdescription0lang) | [Localization](https://wowdev.wiki/Localization) Assumed enUS                                                                                |
| 24     | MapDescription0_1         | string | [MapDescription0_Lang_enGB](map_dbc#mapdescription0lang) | Assumed enGB, not used in 3.3.5a                                                                                                             |
| 25     | MapDescription0_2         | string | [MapDescription0_Lang_koKR](map_dbc#mapdescription0lang) | Assumed koKR                                                                                                                                 |
| 26     | MapDescription0_3         | string | [MapDescription0_Lang_frFR](map_dbc#mapdescription0lang) | Assumed frFR                                                                                                                                 |
| 27     | MapDescription0_4         | string | [MapDescription0_Lang_deDE](map_dbc#mapdescription0lang) | Assumed deDE                                                                                                                                 |
| 28     | MapDescription0_5         | string | [MapDescription0_Lang_enCN](map_dbc#mapdescription0lang) | Assumed enCN, not used in 3.3.5a                                                                                                             |
| 29     | MapDescription0_6         | string | [MapDescription0_Lang_zhCN](map_dbc#mapdescription0lang) | Assumed zhCN                                                                                                                                 |
| 30     | MapDescription0_7         | string | [MapDescription0_Lang_enTW](map_dbc#mapdescription0lang) | Assumed enTW, not used in 3.3.5a                                                                                                             |
| 31     | MapDescription0_8         | string | [MapDescription0_Lang_zhTW](map_dbc#mapdescription0lang) | Assumed zhTW                                                                                                                                 |
| 32     | MapDescription0_9         | string | [MapDescription0_Lang_esES](map_dbc#mapdescription0lang) | Assumed esES                                                                                                                                 |
| 33     | MapDescription0_10        | string | [MapDescription0_Lang_esMX](map_dbc#mapdescription0lang) | Assumed esMX                                                                                                                                 |
| 34     | MapDescription0_11        | string | [MapDescription0_Lang_ruRU](map_dbc#mapdescription0lang) | Assumed ruRU                                                                                                                                 |
| 35     | MapDescription0_12        | string | [MapDescription0_Lang_ptPT](map_dbc#mapdescription0lang) | Assumed ptPT, not used in 3.3.5a                                                                                                             |
| 36     | MapDescription0_13        | string | [MapDescription0_Lang_ptBR](map_dbc#mapdescription0lang) | Assumed ptBR, not used in 3.3.5a                                                                                                             |
| 37     | MapDescription0_14        | string | [MapDescription0_Lang_itIT](map_dbc#mapdescription0lang) | Assumed itIT, not used in 3.3.5a                                                                                                             |
| 38     | MapDescription0_15        | string | [MapDescription0_Lang_Unk](map_dbc#mapdescription0lang)  | Unknown language, unsure of the usage in 3.3.5a                                                                                              |
| 39     | MapDescription0_lang_mask | uint32 | [MapDescription0_Lang_Mask](map_dbc#mapdescription0lang) | Assumed flags of the localized text                                                                                                          |
| 40     | MapDescription1_0         | string | [MapDescription1_Lang_enUS](map_dbc#mapdescription1lang) | [Localization](https://wowdev.wiki/Localization) Assumed enUS                                                                                |
| 41     | MapDescription1_1         | string | [MapDescription1_Lang_enGB](map_dbc#mapdescription1lang) | Assumed enGB, not used in 3.3.5a                                                                                                             |
| 42     | MapDescription1_2         | string | [MapDescription1_Lang_koKR](map_dbc#mapdescription1lang) | Assumed koKR                                                                                                                                 |
| 43     | MapDescription1_3         | string | [MapDescription1_Lang_frFR](map_dbc#mapdescription1lang) | Assumed frFR                                                                                                                                 |
| 44     | MapDescription1_4         | string | [MapDescription1_Lang_deDE](map_dbc#mapdescription1lang) | Assumed deDE                                                                                                                                 |
| 45     | MapDescription1_5         | string | [MapDescription1_Lang_enCN](map_dbc#mapdescription1lang) | Assumed enCN, not used in 3.3.5a                                                                                                             |
| 46     | MapDescription1_6         | string | [MapDescription1_Lang_zhCN](map_dbc#mapdescription1lang) | Assumed zhCN                                                                                                                                 |
| 47     | MapDescription1_7         | string | [MapDescription1_Lang_enTW](map_dbc#mapdescription1lang) | Assumed enTW, not used in 3.3.5a                                                                                                             |
| 48     | MapDescription1_8         | string | [MapDescription1_Lang_zhTW](map_dbc#mapdescription1lang) | Assumed zhTW                                                                                                                                 |
| 49     | MapDescription1_9         | string | [MapDescription1_Lang_esES](map_dbc#mapdescription1lang) | Assumed esES                                                                                                                                 |
| 50     | MapDescription1_10        | string | [MapDescription1_Lang_esMX](map_dbc#mapdescription1lang) | Assumed esMX                                                                                                                                 |
| 51     | MapDescription1_11        | string | [MapDescription1_Lang_ruRU](map_dbc#mapdescription1lang) | Assumed ruRU                                                                                                                                 |
| 52     | MapDescription1_12        | string | [MapDescription1_Lang_ptPT](map_dbc#mapdescription1lang) | Assumed ptPT, not used in 3.3.5a                                                                                                             |
| 53     | MapDescription1_13        | string | [MapDescription1_Lang_ptBR](map_dbc#mapdescription1lang) | Assumed ptBR, not used in 3.3.5a                                                                                                             |
| 54     | MapDescription1_14        | string | [MapDescription1_Lang_itIT](map_dbc#mapdescription1lang) | Assumed itIT, not used in 3.3.5a                                                                                                             |
| 55     | MapDescription1_15        | string | [MapDescription1_Lang_Unk](map_dbc#mapdescription1lang)  | Unknown language, unsure of the usage in 3.3.5a                                                                                              |
| 56     | MapDescription1_lang_mask | uint32 | [MapDescription1_Lang_Mask](map_dbc#mapdescription1lang) | Assumed flags of the localized text                                                                                                          |
| 57     | LoadingScreenID           | uint32 | [LoadingScreenID](map_dbc#loadingscreenid)               | [LoadingScreen](https://wowdev.wiki/DB/LoadingScreens): Ref-ID; The LoadingScreen to Display. ID in [LoadingScreens.dbc](dbc-loadingscreens) |
| 58     | MinimapIconScale          | float  | [MinimapIconScale](map_dbc#minimapiconscale)             |                                                                                                                                              |
| 59     | CorpseMapID               | int32  | [CorpseMapID](map_dbc#corpsemapid)                       | Ref-ID; Points to column 1, -1 if none                                                                                                       |
| 60     | Corpse_X                  | float  | [CorpseX](map_dbc#corpsex)                               | The X-Coord of the instance entrance                                                                                                         |
| 61     | Corpse_Y                  | float  | [CorpseY](map_dbc#corpsey)                               | The Y-Coord of the instance entrance                                                                                                         |
| 62     | TimeOfDayOverride         | int32  | [TimeOfDayOverride](map_dbc#timeofdayoverride)           | Set to -1 for everything but Orgrimmar and Dalaran arena. For those, the time of day will change to this.                                    |
| 63     | ExpansionID               | uint32 | [ExpansionID](map_dbc#expansionid)                       | Classic: 0; BC: 1; WotLK: 2                                                                                                                  |
| 64     | RaidOffset                | uint32 | [RaidOffset](map_dbc#raidoffset)                         | Instance-Reset?                                                                                                                              |
| 65     | MaxPlayers                | uint32 | [MaxPlayers](map_dbc#maxplayers)                         |                                                                                                                                              |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

## Content

<details>
<summary>Show the content of Map.dbc</summary>

| ID  | Type | Name                                               | AreaTableID | Expansion | MaxPlayers |
| --- | ---- | -------------------------------------------------- | ----------- | --------- | ---------- |
| 0   | 0    | Eastern Kingdoms                                   | 0           | 0         | 0          |
| 1   | 0    | Kalimdor                                           | 0           | 0         | 0          |
| 13  | 0    | Testing                                            | 3817        | 0         | 0          |
| 25  | 0    | Scott Test                                         | 0           | 0         | 0          |
| 30  | 3    | Alterac Valley                                     | 0           | 0         | 0          |
| 33  | 1    | Shadowfang Keep                                    | 0           | 0         | 10         |
| 34  | 1    | Stormwind Stockade                                 | 717         | 0         | 10         |
| 35  | 0    | &lt;unused&gt;StormwindPrison                      | 717         | 0         | 0          |
| 36  | 1    | Deadmines                                          | 0           | 0         | 10         |
| 37  | 0    | Azshara Crater                                     | 0           | 0         | 0          |
| 42  | 0    | Collin's Test                                      | 0           | 0         | 0          |
| 43  | 1    | Wailing Caverns                                    | 718         | 0         | 10         |
| 44  | 1    | &lt;unused&gt; Monastery                           | 0           | 0         | 10         |
| 47  | 1    | Razorfen Kraul                                     | 0           | 0         | 10         |
| 48  | 1    | Blackfathom Deeps                                  | 719         | 0         | 10         |
| 70  | 1    | Uldaman                                            | 1337        | 0         | 10         |
| 90  | 1    | Gnomeregan                                         | 721         | 0         | 10         |
| 109 | 1    | Sunken Temple                                      | 1477        | 0         | 10         |
| 129 | 1    | Razorfen Downs                                     | 0           | 0         | 10         |
| 169 | 2    | Emerald Dream                                      | 0           | 0         | 40         |
| 189 | 1    | Scarlet Monastery                                  | 0           | 0         | 10         |
| 209 | 1    | Zul'Farrak                                         | 0           | 0         | 10         |
| 229 | 1    | Blackrock Spire                                    | 1583        | 0         | 10         |
| 230 | 1    | Blackrock Depths                                   | 1584        | 0         | 5          |
| 249 | 2    | Onyxia's Lair                                      | 2159        | 0         | 40         |
| 269 | 1    | Opening of the Dark Portal                         | 0           | 1         | 5          |
| 289 | 1    | Scholomance                                        | 0           | 0         | 5          |
| 309 | 2    | Zul'Gurub                                          | 1977        | 0         | 20         |
| 329 | 1    | Stratholme                                         | 0           | 0         | 5          |
| 349 | 1    | Maraudon                                           | 2100        | 0         | 10         |
| 369 | 0    | Deeprun Tram                                       | 2257        | 0         | 0          |
| 389 | 1    | Ragefire Chasm                                     | 2437        | 0         | 10         |
| 409 | 2    | Molten Core                                        | 2717        | 0         | 40         |
| 429 | 1    | Dire Maul                                          | 2557        | 0         | 5          |
| 449 | 0    | Alliance PVP Barracks                              | 2918        | 0         | 0          |
| 450 | 0    | Horde PVP Barracks                                 | 2917        | 0         | 0          |
| 451 | 0    | Development Land                                   | 0           | 2         | 0          |
| 469 | 2    | Blackwing Lair                                     | 2677        | 0         | 40         |
| 489 | 3    | Warsong Gulch                                      | 3277        | 0         | 0          |
| 509 | 2    | Ruins of Ahn'Qiraj                                 | 3429        | 0         | 20         |
| 529 | 3    | Arathi Basin                                       | 3358        | 0         | 0          |
| 530 | 0    | Outland                                            | 0           | 1         | 0          |
| 531 | 2    | Ahn'Qiraj Temple                                   | 3428        | 0         | 40         |
| 532 | 2    | Karazhan                                           | 3457        | 1         | 10         |
| 533 | 2    | Naxxramas                                          | 3456        | 2         | 25         |
| 534 | 2    | The Battle for Mount Hyjal                         | 616         | 1         | 25         |
| 540 | 1    | Hellfire Citadel: The Shattered Halls              | 3714        | 1         | 5          |
| 542 | 1    | Hellfire Citadel: The Blood Furnace                | 3713        | 1         | 5          |
| 543 | 1    | Hellfire Citadel: Ramparts                         | 3562        | 1         | 5          |
| 544 | 2    | Magtheridon's Lair                                 | 3836        | 1         | 25         |
| 545 | 1    | Coilfang: The Steamvault                           | 3715        | 1         | 5          |
| 546 | 1    | Coilfang: The Underbog                             | 3716        | 1         | 5          |
| 547 | 1    | Coilfang: The Slave Pens                           | 3717        | 1         | 5          |
| 548 | 2    | Coilfang: Serpentshrine Cavern                     | 3607        | 1         | 25         |
| 550 | 2    | Tempest Keep                                       | 3845        | 1         | 25         |
| 552 | 1    | Tempest Keep: The Arcatraz                         | 3848        | 1         | 5          |
| 553 | 1    | Tempest Keep: The Botanica                         | 3847        | 1         | 5          |
| 554 | 1    | Tempest Keep: The Mechanar                         | 3849        | 1         | 5          |
| 555 | 1    | Auchindoun: Shadow Labyrinth                       | 3789        | 1         | 5          |
| 556 | 1    | Auchindoun: Sethekk Halls                          | 3791        | 1         | 5          |
| 557 | 1    | Auchindoun: Mana-Tombs                             | 3792        | 1         | 5          |
| 558 | 1    | Auchindoun: Auchenai Crypts                        | 3790        | 1         | 5          |
| 559 | 4    | Nagrand Arena                                      | 0           | 0         | 0          |
| 560 | 1    | The Escape From Durnholde                          | 267         | 1         | 5          |
| 562 | 4    | Blade's Edge Arena                                 | 3702        | 0         | 0          |
| 564 | 2    | Black Temple                                       | 0           | 1         | 25         |
| 565 | 2    | Gruul's Lair                                       | 3923        | 1         | 25         |
| 566 | 3    | Eye of the Storm                                   | 0           | 1         | 0          |
| 568 | 2    | Zul'Aman                                           | 0           | 1         | 10         |
| 571 | 0    | Northrend                                          | 0           | 2         | 0          |
| 572 | 4    | Ruins of Lordaeron                                 | 0           | 0         | 0          |
| 573 | 0    | ExteriorTest                                       | 0           | 2         | 0          |
| 574 | 1    | Utgarde Keep                                       | 0           | 2         | 5          |
| 575 | 1    | Utgarde Pinnacle                                   | 0           | 2         | 5          |
| 576 | 1    | The Nexus                                          | 4265        | 2         | 5          |
| 578 | 1    | The Oculus                                         | 0           | 2         | 5          |
| 580 | 2    | The Sunwell                                        | 0           | 1         | 25         |
| 582 | 0    | Transport: Rut'theran to Auberdine                 | 0           | 0         | 0          |
| 584 | 0    | Transport: Menethil to Theramore                   | 0           | 0         | 0          |
| 585 | 1    | Magister's Terrace                                 | 0           | 1         | 5          |
| 586 | 0    | Transport: Exodar to Auberdine                     | 0           | 0         | 0          |
| 587 | 0    | Transport: Feathermoon Ferry                       | 0           | 0         | 0          |
| 588 | 0    | Transport: Menethil to Auberdine                   | 0           | 0         | 0          |
| 589 | 0    | Transport: Orgrimmar to Grom'Gol                   | 0           | 0         | 0          |
| 590 | 0    | Transport: Grom'Gol to Undercity                   | 0           | 0         | 0          |
| 591 | 0    | Transport: Undercity to Orgrimmar                  | 0           | 0         | 0          |
| 592 | 0    | Transport: Borean Tundra Test                      | 0           | 0         | 0          |
| 593 | 0    | Transport: Booty Bay to Ratchet                    | 0           | 0         | 0          |
| 594 | 0    | Transport: Howling Fjord Sister Mercy (Quest)      | 0           | 2         | 0          |
| 595 | 1    | The Culling of Stratholme                          | 0           | 2         | 5          |
| 596 | 0    | Transport: Naglfar                                 | 0           | 2         | 0          |
| 597 | 0    | Craig Test                                         | 0           | 0         | 0          |
| 598 | 1    | Sunwell Fix (Unused)                               | 0           | 1         | 5          |
| 599 | 1    | Halls of Stone                                     | 0           | 2         | 5          |
| 600 | 1    | Drak'Tharon Keep                                   | 0           | 2         | 5          |
| 601 | 1    | Azjol-Nerub                                        | 0           | 2         | 5          |
| 602 | 1    | Halls of Lightning                                 | 0           | 2         | 5          |
| 603 | 2    | Ulduar                                             | 0           | 2         | 5          |
| 604 | 1    | Gundrak                                            | 0           | 2         | 5          |
| 605 | 0    | Development Land (non-weighted textures)           | 0           | 0         | 0          |
| 606 | 0    | QA and DVD                                         | 0           | 2         | 0          |
| 607 | 3    | Strand of the Ancients                             | 0           | 2         | 0          |
| 608 | 1    | Violet Hold                                        | 0           | 2         | 5          |
| 609 | 0    | Ebon Hold                                          | 0           | 2         | 0          |
| 610 | 0    | Transport: Tirisfal to Vengeance Landing           | 0           | 0         | 0          |
| 612 | 0    | Transport: Menethil to Valgarde                    | 0           | 0         | 0          |
| 613 | 0    | Transport: Orgrimmar to Warsong Hold               | 0           | 0         | 0          |
| 614 | 0    | Transport: Stormwind to Valiance Keep              | 0           | 0         | 0          |
| 615 | 2    | The Obsidian Sanctum                               | 0           | 2         | 0          |
| 616 | 2    | The Eye of Eternity                                | 0           | 2         | 5          |
| 617 | 4    | Dalaran Sewers                                     | 0           | 0         | 0          |
| 618 | 4    | The Ring of Valor                                  | 0           | 0         | 0          |
| 619 | 1    | Ahn'kahet: The Old Kingdom                         | 0           | 2         | 0          |
| 620 | 0    | Transport: Moa'ki to Unu'pe                        | 0           | 2         | 0          |
| 621 | 0    | Transport: Moa'ki to Kamagua                       | 0           | 2         | 0          |
| 622 | 0    | Transport: Orgrim's Hammer                         | 0           | 2         | 0          |
| 623 | 0    | Transport: The Skybreaker                          | 0           | 2         | 0          |
| 624 | 2    | Vault of Archavon                                  | 0           | 2         | 0          |
| 628 | 3    | Isle of Conquest                                   | 0           | 2         | 0          |
| 631 | 2    | Icecrown Citadel                                   | 0           | 2         | 0          |
| 632 | 1    | The Forge of Souls                                 | 0           | 2         | 0          |
| 641 | 0    | Transport: Alliance Airship BG                     | 0           | 2         | 0          |
| 642 | 0    | Transport: HordeAirshipBG                          | 0           | 2         | 0          |
| 647 | 0    | Transport: Orgrimmar to Thunder Bluff              | 0           | 2         | 0          |
| 649 | 2    | Trial of the Crusader                              | 0           | 2         | 0          |
| 650 | 1    | Trial of the Champion                              | 0           | 2         | 0          |
| 658 | 1    | Pit of Saron                                       | 0           | 2         | 0          |
| 668 | 1    | Halls of Reflection                                | 0           | 2         | 0          |
| 672 | 0    | Transport: The Skybreaker (Icecrown Citadel Raid)  | 0           | 2         | 0          |
| 673 | 0    | Transport: Orgrim's Hammer (Icecrown Citadel Raid) | 0           | 2         | 0          |
| 712 | 0    | Transport: The Skybreaker (IC Dungeon)             | 0           | 2         | 0          |
| 713 | 0    | Transport: Orgrim's Hammer (IC Dungeon)            | 0           | 2         | 0          |
| 718 | 0    | Transport: The Mighty Wind (Icecrown Citadel Raid) | 0           | 2         | 0          |
| 723 | 0    | Stormwind                                          | 0           | 0         | 0          |
| 724 | 2    | The Ruby Sanctum                                   | 0           | 2         | 0          |

</details>



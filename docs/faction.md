# faction

[`Back-to:DBC`](dbc-index)

**The \`Faction.dbc\` table**

This DBC contains information on all of the base factions. These factions are unique and represent a faction with which a player can gain reputation.

**IMPORTANT:** These values are used for **ALL** tables **EXCEPT** the [creature_template](creature_template) and [gameobject_template_addon](gameobject_template_addon) tables.

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)

## Structure

| Column | Field                 | Type   | faction\_dbc column                                      | Comment                                                                                                                                                                                                                                                                                                                                                     |
| :----: | :-------------------- | :----- | :------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0      | ID                    | uint32 | [ID](faction_dbc#id)                                     |                                                                                                                                                                                                                                                                                                                                                             |
| 1      | ReputationIndex       | int32  | [ReputationIndex](faction_dbc#reputationindex)           | Each faction that has gainable rep has a unique number. All factions that you can not gain rep with have -1.                                                                                                                                                                                                                                                |
| 2      | ReputationRaceMask_0  | uint32 | [ReputationRaceMask_1](faction_dbc#reputationracemask)   | &lt;.. Points to another Allied / AtWar ID. Race mask. See [ChrRaces.dbc](chrraces#content)                                                                                                                                                                                                                                                                 |
| 3      | ReputationRaceMask_1  | uint32 | [ReputationRaceMask_2](faction_dbc#reputationracemask)   | .. Honor Hold has 1101, 690 & Thrallmar 690, 1101 for example. ..&gt;. Race mask. See [ChrRaces.dbc](chrraces#content)                                                                                                                                                                                                                                      |
| 4      | ReputationRaceMask_2  | uint32 | [ReputationRaceMask_3](faction_dbc#reputationracemask)   | Only city factions have a value. Possible relationship to Modifiers and 17 (1 = Stormwind; 2 = Orgrimmar; 4 = Wildhammer Clan & Iron Forge; 8 = Darnassus; 16 = Undercity; 64 = Gnomeregan Exiles; 512 = Shattrath City Factions & Silvermoon City; 528 = Thunder Bluff & Darkspear Trolls; 1024 = Exodar). Race mask. See [ChrRaces.dbc](chrraces#content) |
| 5      | ReputationRaceMask_3  | uint32 | [ReputationRaceMask_4](faction_dbc#reputationracemask)   | Only Horde cities have a value. Possible relationship to Modifiers and 18 (16 = Silvermoon City; 32 = Thunder Bluff; 128 = Darkspear Trolls; 512 = Undercity; 528 = Orgrimmar). Race mask. See [ChrRaces.dbc](chrraces#content)                                                                                                                             |
| 6      | ReputationClassMask_0 | uint32 | [ReputationClassMask_1](faction_dbc#reputationclassmask) | (479 = Cenerion Circle; 1503 = Lower City, "Friendly, Hidden", Netherwing; Shatari Skyguards). Class mask. See [ChrClasses.dbc](chrclasses#content)                                                                                                                                                                                                         |
| 7      | ReputationClassMask_1 | uint32 | [ReputationClassMask_2](faction_dbc#reputationclassmask) | (1024 = Cenerion Circle;). Class mask. See [ChrClasses.dbc](chrclasses#content)                                                                                                                                                                                                                                                                             |
| 8      | ReputationClassMask_2 | uint32 | [ReputationClassMask_3](faction_dbc#reputationclassmask) | Never set pre 3.\* but 0x80 on "Kirin Tor". Class mask. See [ChrClasses.dbc](chrclasses#content)                                                                                                                                                                                                                                                            |
| 9      | ReputationClassMask_3 | uint32 | [ReputationClassMask_4](faction_dbc#reputationclassmask) | Never set pre 3.\* but 0x80 on "Kirin Tor". Class mask. See [ChrClasses.dbc](chrclasses#content)                                                                                                                                                                                                                                                            |
| 10     | ReputationBase_0      | int32  | [ReputationBase_1](faction_dbc#reputationbase)           | Based on 0 = Neutral                                                                                                                                                                                                                                                                                                                                        |
| 11     | ReputationBase_1      | int32  | [ReputationBase_2](faction_dbc#reputationbase)           |                                                                                                                                                                                                                                                                                                                                                             |
| 12     | ReputationBase_2      | int32  | [ReputationBase_3](faction_dbc#reputationbase)           |                                                                                                                                                                                                                                                                                                                                                             |
| 13     | ReputationBase_3      | int32  | [ReputationBase_4](faction_dbc#reputationbase)           |                                                                                                                                                                                                                                                                                                                                                             |
| 14     | ReputationFlags_0     | uint32 | [ReputationFlags_1](faction_dbc#reputationflags)         |                                                                                                                                                                                                                                                                                                                                                             |
| 15     | ReputationFlags_1     | uint32 | [ReputationFlags_2](faction_dbc#reputationflags)         |                                                                                                                                                                                                                                                                                                                                                             |
| 16     | ReputationFlags_2     | uint32 | [ReputationFlags_3](faction_dbc#reputationflags)         |                                                                                                                                                                                                                                                                                                                                                             |
| 17     | ReputationFlags_3     | uint32 | [ReputationFlags_4](faction_dbc#reputationflags)         |                                                                                                                                                                                                                                                                                                                                                             |
| 18     | ParentFactionID       | uint32 | [ParentFactionID](faction_dbc#parentfactionid)           | Recursive. i.e. Undercity lists ID 67, which is Horde. ID in [Faction.dbc](faction)                                                                                                                                                                                                                                                                         |
| 19     | ParentFactionMod_0    | float  | [ParentFactionMod_1](faction_dbc#parentfactionmod)       |                                                                                                                                                                                                                                                                                                                                                             |
| 20     | ParentFactionMod_1    | float  | [ParentFactionMod_2](faction_dbc#parentfactionmod)       |                                                                                                                                                                                                                                                                                                                                                             |
| 21     | ParentFactionCap_0    | uint32 | [ParentFactionCap_1](faction_dbc#parentfactioncap)       |                                                                                                                                                                                                                                                                                                                                                             |
| 22     | ParentFactionCap_1    | uint32 | [ParentFactionCap_2](faction_dbc#parentfactioncap)       |                                                                                                                                                                                                                                                                                                                                                             |
| 23     | Name_0                | string | [Name_Lang_enUS](faction_dbc#namelang)                   | Display name of the faction. Assumed enUS                                                                                                                                                                                                                                                                                                                   |
| 24     | Name_1                | string | [Name_Lang_enGB](faction_dbc#namelang)                   | Assumed enGB, not used in 3.3.5a                                                                                                                                                                                                                                                                                                                            |
| 25     | Name_2                | string | [Name_Lang_koKR](faction_dbc#namelang)                   | Assumed koKR                                                                                                                                                                                                                                                                                                                                                |
| 26     | Name_3                | string | [Name_Lang_frFR](faction_dbc#namelang)                   | Assumed frFR                                                                                                                                                                                                                                                                                                                                                |
| 27     | Name_4                | string | [Name_Lang_deDE](faction_dbc#namelang)                   | Assumed deDE                                                                                                                                                                                                                                                                                                                                                |
| 28     | Name_5                | string | [Name_Lang_enCN](faction_dbc#namelang)                   | Assumed enCN, not used in 3.3.5a                                                                                                                                                                                                                                                                                                                            |
| 29     | Name_6                | string | [Name_Lang_zhCN](faction_dbc#namelang)                   | Assumed zhCN                                                                                                                                                                                                                                                                                                                                                |
| 30     | Name_7                | string | [Name_Lang_enTW](faction_dbc#namelang)                   | Assumed enTW, not used in 3.3.5a                                                                                                                                                                                                                                                                                                                            |
| 31     | Name_8                | string | [Name_Lang_zhTW](faction_dbc#namelang)                   | Assumed zhTW                                                                                                                                                                                                                                                                                                                                                |
| 32     | Name_9                | string | [Name_Lang_esES](faction_dbc#namelang)                   | Assumed esES                                                                                                                                                                                                                                                                                                                                                |
| 33     | Name_10               | string | [Name_Lang_esMX](faction_dbc#namelang)                   | Assumed esMX                                                                                                                                                                                                                                                                                                                                                |
| 34     | Name_11               | string | [Name_Lang_ruRU](faction_dbc#namelang)                   | Assumed ruRU                                                                                                                                                                                                                                                                                                                                                |
| 35     | Name_12               | string | [Name_Lang_ptPT](faction_dbc#namelang)                   | Assumed ptPT, not used in 3.3.5a                                                                                                                                                                                                                                                                                                                            |
| 36     | Name_13               | string | [Name_Lang_ptBR](faction_dbc#namelang)                   | Assumed ptBR, not used in 3.3.5a                                                                                                                                                                                                                                                                                                                            |
| 37     | Name_14               | string | [Name_Lang_itIT](faction_dbc#namelang)                   | Assumed itIT, not used in 3.3.5a                                                                                                                                                                                                                                                                                                                            |
| 38     | Name_15               | string | [Name_Lang_Unk](faction_dbc#namelang)                    | Unknown language, unsure of the usage in 3.3.5a                                                                                                                                                                                                                                                                                                             |
| 39     | Name_lang_mask        | uint32 | [Name_Lang_Mask](faction_dbc#namelang)                   | Assumed flags of the localized text                                                                                                                                                                                                                                                                                                                         |
| 40     | Description_0         | string | [Description_Lang_enUS](faction_dbc#descriptionlang)     | Seen in the reputation-GUI on click. Assumed enUS                                                                                                                                                                                                                                                                                                           |
| 41     | Description_1         | string | [Description_Lang_enGB](faction_dbc#descriptionlang)     | Assumed enGB, not used in 3.3.5a                                                                                                                                                                                                                                                                                                                            |
| 42     | Description_2         | string | [Description_Lang_koKR](faction_dbc#descriptionlang)     | Assumed koKR                                                                                                                                                                                                                                                                                                                                                |
| 43     | Description_3         | string | [Description_Lang_frFR](faction_dbc#descriptionlang)     | Assumed frFR                                                                                                                                                                                                                                                                                                                                                |
| 44     | Description_4         | string | [Description_Lang_deDE](faction_dbc#descriptionlang)     | Assumed deDE                                                                                                                                                                                                                                                                                                                                                |
| 45     | Description_5         | string | [Description_Lang_enCN](faction_dbc#descriptionlang)     | Assumed enCN, not used in 3.3.5a                                                                                                                                                                                                                                                                                                                            |
| 46     | Description_6         | string | [Description_Lang_zhCN](faction_dbc#descriptionlang)     | Assumed zhCN                                                                                                                                                                                                                                                                                                                                                |
| 47     | Description_7         | string | [Description_Lang_enTW](faction_dbc#descriptionlang)     | Assumed enTW, not used in 3.3.5a                                                                                                                                                                                                                                                                                                                            |
| 48     | Description_8         | string | [Description_Lang_zhTW](faction_dbc#descriptionlang)     | Assumed zhTW                                                                                                                                                                                                                                                                                                                                                |
| 49     | Description_9         | string | [Description_Lang_esES](faction_dbc#descriptionlang)     | Assumed esES                                                                                                                                                                                                                                                                                                                                                |
| 50     | Description_10        | string | [Description_Lang_esMX](faction_dbc#descriptionlang)     | Assumed esMX                                                                                                                                                                                                                                                                                                                                                |
| 51     | Description_11        | string | [Description_Lang_ruRU](faction_dbc#descriptionlang)     | Assumed ruRU                                                                                                                                                                                                                                                                                                                                                |
| 52     | Description_12        | string | [Description_Lang_ptPT](faction_dbc#descriptionlang)     | Assumed ptPT, not used in 3.3.5a                                                                                                                                                                                                                                                                                                                            |
| 53     | Description_13        | string | [Description_Lang_ptBR](faction_dbc#descriptionlang)     | Assumed ptBR, not used in 3.3.5a                                                                                                                                                                                                                                                                                                                            |
| 54     | Description_14        | string | [Description_Lang_itIT](faction_dbc#descriptionlang)     | Assumed itIT, not used in 3.3.5a                                                                                                                                                                                                                                                                                                                            |
| 55     | Description_15        | string | [Description_Lang_Unk](faction_dbc#descriptionlang)      | Unknown language, unsure of the usage in 3.3.5a                                                                                                                                                                                                                                                                                                             |
| 56     | Description_lang_mask | uint32 | [Description_Lang_Mask](faction_dbc#descriptionlang)     | Assumed flags of the localized text                                                                                                                                                                                                                                                                                                                         |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

### Flags

       FACTION_FLAG_NONE             = 0x00, // no faction flag
       FACTION_FLAG_VISIBLE          = 0x01, // makes visible in client (set or can be set at interaction with target of this faction)
       FACTION_FLAG_AT_WAR           = 0x02, // enable AtWar-button in client. player controlled (except opposition team always war state), Flag only set on initial creation
       FACTION_FLAG_HIDDEN           = 0x04, // hidden faction from reputation pane in client (player can gain reputation, but this update not sent to client)
       FACTION_FLAG_INVISIBLE_FORCED = 0x08, // always overwrite FACTION_FLAG_VISIBLE and hide faction in rep.list, used for hide opposite team factions
       FACTION_FLAG_PEACE_FORCED     = 0x10, // always overwrite FACTION_FLAG_AT_WAR, used for prevent war with own team factions
       FACTION_FLAG_INACTIVE         = 0x20, // player controlled, state stored in character_reputation.flags (CMSG_SET_FACTION_INACTIVE)
       FACTION_FLAG_RIVAL            = 0x40, // flag for the two competing outland factions
       FACTION_FLAG_SPECIAL          = 0x80 // horde and alliance home cities and their northrend allies have this flag

### Content

When referring to a creature's [faction](creature_template#faction) we use the ID value. It is the ID of [FactionTemplate.dbc](factiontemplate), and the Faction column is the ID of this file.

When referring to a reputation gain (example: `.modify reputation`) we use [Faction](#faction) value.

<details>
<summary>Show the content of Faction.dbc</summary>

| ID   | [Faction](#faction) | Faction Name                        | Reputation Index                                      |
| :--- | :------------------ | :---------------------------------- | :---------------------------------------------------- |
| 1    | 1                   | PLAYER, Human                       | -1 - Players cannot gain reputation with this faction |
| 2    | 2                   | PLAYER, Orc                         | -1 - Players cannot gain reputation with this faction |
| 3    | 3                   | PLAYER, Dwarf                       | -1 - Players cannot gain reputation with this faction |
| 4    | 4                   | PLAYER, Night Elf                   | -1 - Players cannot gain reputation with this faction |
| 5    | 5                   | PLAYER, Undead                      | -1 - Players cannot gain reputation with this faction |
| 6    | 6                   | PLAYER, Tauren                      | -1 - Players cannot gain reputation with this faction |
| 7    | 7                   | Creature                            | -1 - Players cannot gain reputation with this faction |
| 10   | 40                  | Escortee                            | -1 - Players cannot gain reputation with this faction |
| 11   | 72                  | Stormwind                           | 19 - Stormwind                                        |
| 12   | 72                  | Stormwind                           | 19 - Stormwind                                        |
| 14   | 14                  | Monster                             | -1 - Players cannot gain reputation with this faction |
| 15   | 7                   | Creature                            | -1 - Players cannot gain reputation with this faction |
| 16   | 14                  | Monster                             | -1 - Players cannot gain reputation with this faction |
| 17   | 15                  | Defias Brotherhood                  | -1 - Players cannot gain reputation with this faction |
| 18   | 19                  | Murloc                              | -1 - Players cannot gain reputation with this faction |
| 19   | 17                  | Gnoll - Redridge                    | -1 - Players cannot gain reputation with this faction |
| 20   | 16                  | Gnoll - Riverpaw                    | -1 - Players cannot gain reputation with this faction |
| 21   | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 22   | 22                  | Beast - Spider                      | -1 - Players cannot gain reputation with this faction |
| 23   | 54                  | Gnomeregan Exiles                   | 18 - Gnomeregan Exiles                                |
| 24   | 24                  | Worgen                              | -1 - Players cannot gain reputation with this faction |
| 25   | 25                  | Kobold                              | -1 - Players cannot gain reputation with this faction |
| 26   | 25                  | Kobold                              | -1 - Players cannot gain reputation with this faction |
| 27   | 15                  | Defias Brotherhood                  | -1 - Players cannot gain reputation with this faction |
| 28   | 26                  | Troll, Bloodscalp                   | -1 - Players cannot gain reputation with this faction |
| 29   | 76                  | Orgrimmar                           | 14 - Orgrimmar                                        |
| 30   | 27                  | Troll, Skullsplitter                | -1 - Players cannot gain reputation with this faction |
| 31   | 28                  | Prey                                | -1 - Players cannot gain reputation with this faction |
| 32   | 29                  | Beast - Wolf                        | -1 - Players cannot gain reputation with this faction |
| 33   | 40                  | Escortee                            | -1 - Players cannot gain reputation with this faction |
| 34   | 15                  | Defias Brotherhood                  | -1 - Players cannot gain reputation with this faction |
| 35   | 31                  | Friendly                            | -1 - Players cannot gain reputation with this faction |
| 36   | 32                  | Trogg                               | -1 - Players cannot gain reputation with this faction |
| 37   | 33                  | Troll, Frostmane                    | -1 - Players cannot gain reputation with this faction |
| 38   | 29                  | Beast - Wolf                        | -1 - Players cannot gain reputation with this faction |
| 39   | 18                  | Gnoll - Shadowhide                  | -1 - Players cannot gain reputation with this faction |
| 40   | 34                  | Orc, Blackrock                      | -1 - Players cannot gain reputation with this faction |
| 41   | 35                  | Villian                             | -1 - Players cannot gain reputation with this faction |
| 42   | 36                  | Victim                              | -1 - Players cannot gain reputation with this faction |
| 43   | 35                  | Villian                             | -1 - Players cannot gain reputation with this faction |
| 44   | 37                  | Beast - Bear                        | -1 - Players cannot gain reputation with this faction |
| 45   | 38                  | Ogre                                | -1 - Players cannot gain reputation with this faction |
| 46   | 39                  | Kurzen\'s Mercenaries               | -1 - Players cannot gain reputation with this faction |
| 47   | 41                  | Venture Company                     | -1 - Players cannot gain reputation with this faction |
| 48   | 42                  | Beast - Raptor                      | -1 - Players cannot gain reputation with this faction |
| 49   | 43                  | Basilisk                            | -1 - Players cannot gain reputation with this faction |
| 50   | 44                  | Dragonflight, Green                 | -1 - Players cannot gain reputation with this faction |
| 51   | 45                  | Lost Ones                           | -1 - Players cannot gain reputation with this faction |
| 52   | 769                 | Gizlock\'s Dummy                    | -1 - Players cannot gain reputation with this faction |
| 53   | 49                  | Human, Night Watch                  | -1 - Players cannot gain reputation with this faction |
| 54   | 48                  | Dark Iron Dwarves                   | -1 - Players cannot gain reputation with this faction |
| 55   | 47                  | Ironforge                           | 20 - Ironforge                                        |
| 56   | 49                  | Human, Night Watch                  | -1 - Players cannot gain reputation with this faction |
| 57   | 47                  | Ironforge                           | 20 - Ironforge                                        |
| 58   | 7                   | Creature                            | -1 - Players cannot gain reputation with this faction |
| 59   | 32                  | Trogg                               | -1 - Players cannot gain reputation with this faction |
| 60   | 50                  | Dragonflight, Red                   | -1 - Players cannot gain reputation with this faction |
| 61   | 51                  | Gnoll - Mosshide                    | -1 - Players cannot gain reputation with this faction |
| 62   | 52                  | Orc, Dragonmaw                      | -1 - Players cannot gain reputation with this faction |
| 63   | 53                  | Gnome - Leper                       | -1 - Players cannot gain reputation with this faction |
| 64   | 54                  | Gnomeregan Exiles                   | 18 - Gnomeregan Exiles                                |
| 65   | 76                  | Orgrimmar                           | 14 - Orgrimmar                                        |
| 66   | 55                  | Leopard                             | -1 - Players cannot gain reputation with this faction |
| 67   | 56                  | Scarlet Crusade                     | -1 - Players cannot gain reputation with this faction |
| 68   | 68                  | Undercity                           | 17 - Undercity                                        |
| 69   | 470                 | Ratchet                             | 9 - Ratchet                                           |
| 70   | 57                  | Gnoll - Rothide                     | -1 - Players cannot gain reputation with this faction |
| 71   | 68                  | Undercity                           | 17 - Undercity                                        |
| 72   | 58                  | Beast - Gorilla                     | -1 - Players cannot gain reputation with this faction |
| 73   | 669                 | Beast - Carrion Bird                | -1 - Players cannot gain reputation with this faction |
| 74   | 60                  | Naga                                | -1 - Players cannot gain reputation with this faction |
| 76   | 61                  | Dalaran                             | -1 - Players cannot gain reputation with this faction |
| 77   | 62                  | Forlorn Spirit                      | -1 - Players cannot gain reputation with this faction |
| 78   | 63                  | Darkhowl                            | -1 - Players cannot gain reputation with this faction |
| 79   | 69                  | Darnassus                           | 21 - Darnassus                                        |
| 80   | 69                  | Darnassus                           | 21 - Darnassus                                        |
| 81   | 64                  | Grell                               | -1 - Players cannot gain reputation with this faction |
| 82   | 65                  | Furbolg                             | -1 - Players cannot gain reputation with this faction |
| 83   | 66                  | Horde Generic                       | -1 - Players cannot gain reputation with this faction |
| 84   | 189                 | Alliance Generic                    | -1 - Players cannot gain reputation with this faction |
| 85   | 76                  | Orgrimmar                           | 14 - Orgrimmar                                        |
| 86   | 770                 | Gizlock\'s Charm                    | -1 - Players cannot gain reputation with this faction |
| 87   | 70                  | Syndicate                           | 6 - Syndicate                                         |
| 88   | 71                  | Hillsbrad Militia                   | -1 - Players cannot gain reputation with this faction |
| 89   | 56                  | Scarlet Crusade                     | -1 - Players cannot gain reputation with this faction |
| 90   | 73                  | Demon                               | -1 - Players cannot gain reputation with this faction |
| 91   | 74                  | Elemental                           | -1 - Players cannot gain reputation with this faction |
| 92   | 75                  | Spirit                              | -1 - Players cannot gain reputation with this faction |
| 93   | 14                  | Monster                             | -1 - Players cannot gain reputation with this faction |
| 94   | 77                  | Treasure                            | -1 - Players cannot gain reputation with this faction |
| 95   | 78                  | Gnoll - Mudsnout                    | -1 - Players cannot gain reputation with this faction |
| 96   | 79                  | HIllsbrad, Southshore Mayor         | -1 - Players cannot gain reputation with this faction |
| 97   | 70                  | Syndicate                           | 6 - Syndicate                                         |
| 98   | 68                  | Undercity                           | 17 - Undercity                                        |
| 99   | 36                  | Victim                              | -1 - Players cannot gain reputation with this faction |
| 100  | 77                  | Treasure                            | -1 - Players cannot gain reputation with this faction |
| 101  | 77                  | Treasure                            | -1 - Players cannot gain reputation with this faction |
| 102  | 77                  | Treasure                            | -1 - Players cannot gain reputation with this faction |
| 103  | 80                  | Dragonflight, Black                 | -1 - Players cannot gain reputation with this faction |
| 104  | 81                  | Thunder Bluff                       | 16 - Thunder Bluff                                    |
| 105  | 81                  | Thunder Bluff                       | 16 - Thunder Bluff                                    |
| 106  | 66                  | Horde Generic                       | -1 - Players cannot gain reputation with this faction |
| 107  | 33                  | Troll, Frostmane                    | -1 - Players cannot gain reputation with this faction |
| 108  | 70                  | Syndicate                           | 6 - Syndicate                                         |
| 109  | 110                 | Quilboar, Razormane 2               | -1 - Players cannot gain reputation with this faction |
| 110  | 110                 | Quilboar, Razormane 2               | -1 - Players cannot gain reputation with this faction |
| 111  | 85                  | Quilboar, Bristleback               | -1 - Players cannot gain reputation with this faction |
| 112  | 85                  | Quilboar, Bristleback               | -1 - Players cannot gain reputation with this faction |
| 113  | 40                  | Escortee                            | -1 - Players cannot gain reputation with this faction |
| 114  | 77                  | Treasure                            | -1 - Players cannot gain reputation with this faction |
| 115  | 8                   | PLAYER, Gnome                       | -1 - Players cannot gain reputation with this faction |
| 116  | 9                   | PLAYER, Troll                       | -1 - Players cannot gain reputation with this faction |
| 118  | 68                  | Undercity                           | 17 - Undercity                                        |
| 119  | 87                  | Bloodsail Buccaneers                | 0 - Bloodsail Buccaneers                              |
| 120  | 21                  | Booty Bay                           | 1 - Booty Bay                                         |
| 121  | 21                  | Booty Bay                           | 1 - Booty Bay                                         |
| 122  | 47                  | Ironforge                           | 20 - Ironforge                                        |
| 123  | 72                  | Stormwind                           | 19 - Stormwind                                        |
| 124  | 69                  | Darnassus                           | 21 - Darnassus                                        |
| 125  | 76                  | Orgrimmar                           | 14 - Orgrimmar                                        |
| 126  | 530                 | Darkspear Trolls                    | 15 - Darkspear Trolls                                 |
| 127  | 35                  | Villian                             | -1 - Players cannot gain reputation with this faction |
| 128  | 88                  | Blackfathom                         | -1 - Players cannot gain reputation with this faction |
| 129  | 89                  | Makrura                             | -1 - Players cannot gain reputation with this faction |
| 130  | 90                  | Centaur, Kolkar                     | -1 - Players cannot gain reputation with this faction |
| 131  | 91                  | Centaur, Galak                      | -1 - Players cannot gain reputation with this faction |
| 132  | 92                  | Gelkis Clan Centaur                 | 2 - Gelkis Clan Centaur                               |
| 133  | 93                  | Magram Clan Centaur                 | 3 - Magram Clan Centaur                               |
| 134  | 94                  | Maraudine                           | -1 - Players cannot gain reputation with this faction |
| 148  | 14                  | Monster                             | -1 - Players cannot gain reputation with this faction |
| 149  | 108                 | Theramore                           | -1 - Players cannot gain reputation with this faction |
| 150  | 108                 | Theramore                           | -1 - Players cannot gain reputation with this faction |
| 151  | 108                 | Theramore                           | -1 - Players cannot gain reputation with this faction |
| 152  | 109                 | Quilboar, Razorfen                  | -1 - Players cannot gain reputation with this faction |
| 153  | 109                 | Quilboar, Razorfen                  | -1 - Players cannot gain reputation with this faction |
| 154  | 111                 | Quilboar, Deathshead                | -1 - Players cannot gain reputation with this faction |
| 168  | 128                 | Enemy                               | -1 - Players cannot gain reputation with this faction |
| 188  | 148                 | Ambient                             | -1 - Players cannot gain reputation with this faction |
| 189  | 7                   | Creature                            | -1 - Players cannot gain reputation with this faction |
| 190  | 148                 | Ambient                             | -1 - Players cannot gain reputation with this faction |
| 208  | 168                 | Nethergarde Caravan                 | -1 - Players cannot gain reputation with this faction |
| 209  | 168                 | Nethergarde Caravan                 | -1 - Players cannot gain reputation with this faction |
| 210  | 189                 | Alliance Generic                    | -1 - Players cannot gain reputation with this faction |
| 230  | 573                 | Southsea Freebooters                | -1 - Players cannot gain reputation with this faction |
| 231  | 40                  | Escortee                            | -1 - Players cannot gain reputation with this faction |
| 232  | 40                  | Escortee                            | -1 - Players cannot gain reputation with this faction |
| 233  | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 250  | 40                  | Escortee                            | -1 - Players cannot gain reputation with this faction |
| 270  | 229                 | Wailing Caverns                     | -1 - Players cannot gain reputation with this faction |
| 290  | 40                  | Escortee                            | -1 - Players cannot gain reputation with this faction |
| 310  | 249                 | Silithid                            | -1 - Players cannot gain reputation with this faction |
| 311  | 249                 | Silithid                            | -1 - Players cannot gain reputation with this faction |
| 312  | 22                  | Beast - Spider                      | -1 - Players cannot gain reputation with this faction |
| 330  | 229                 | Wailing Caverns                     | -1 - Players cannot gain reputation with this faction |
| 350  | 88                  | Blackfathom                         | -1 - Players cannot gain reputation with this faction |
| 370  | 915                 | Armies of C\'Thun                   | -1 - Players cannot gain reputation with this faction |
| 371  | 269                 | Silvermoon Remnant                  | -1 - Players cannot gain reputation with this faction |
| 390  | 21                  | Booty Bay                           | 1 - Booty Bay                                         |
| 410  | 43                  | Basilisk                            | -1 - Players cannot gain reputation with this faction |
| 411  | 310                 | Beast - Bat                         | -1 - Players cannot gain reputation with this faction |
| 412  | 510                 | The Defilers                        | 52 - The Defilers                                     |
| 413  | 309                 | Scorpid                             | -1 - Players cannot gain reputation with this faction |
| 414  | 576                 | Timbermaw Hold                      | 35 - Timbermaw Hold                                   |
| 415  | 311                 | Titan                               | -1 - Players cannot gain reputation with this faction |
| 416  | 311                 | Titan                               | -1 - Players cannot gain reputation with this faction |
| 430  | 329                 | Taskmaster Fizzule                  | -1 - Players cannot gain reputation with this faction |
| 450  | 229                 | Wailing Caverns                     | -1 - Players cannot gain reputation with this faction |
| 470  | 311                 | Titan                               | -1 - Players cannot gain reputation with this faction |
| 471  | 349                 | Ravenholdt                          | 5 - Ravenholdt                                        |
| 472  | 70                  | Syndicate                           | 6 - Syndicate                                         |
| 473  | 349                 | Ravenholdt                          | 5 - Ravenholdt                                        |
| 474  | 369                 | Gadgetzan                           | 7 - Gadgetzan                                         |
| 475  | 369                 | Gadgetzan                           | 7 - Gadgetzan                                         |
| 494  | 389                 | Gnomeregan Bug                      | -1 - Players cannot gain reputation with this faction |
| 495  | 40                  | Escortee                            | -1 - Players cannot gain reputation with this faction |
| 514  | 409                 | Harpy                               | -1 - Players cannot gain reputation with this faction |
| 534  | 189                 | Alliance Generic                    | -1 - Players cannot gain reputation with this faction |
| 554  | 429                 | Burning Blade                       | -1 - Players cannot gain reputation with this faction |
| 574  | 449                 | Shadowsilk Poacher                  | -1 - Players cannot gain reputation with this faction |
| 575  | 450                 | Searing Spider                      | -1 - Players cannot gain reputation with this faction |
| 594  | 32                  | Trogg                               | -1 - Players cannot gain reputation with this faction |
| 614  | 36                  | Victim                              | -1 - Players cannot gain reputation with this faction |
| 634  | 14                  | Monster                             | -1 - Players cannot gain reputation with this faction |
| 635  | 609                 | Cenarion Circle                     | 36 - Cenarion Circle                                  |
| 636  | 576                 | Timbermaw Hold                      | 35 - Timbermaw Hold                                   |
| 637  | 470                 | Ratchet                             | 9 - Ratchet                                           |
| 654  | 82                  | Troll, Witherbark                   | -1 - Players cannot gain reputation with this faction |
| 655  | 90                  | Centaur, Kolkar                     | -1 - Players cannot gain reputation with this faction |
| 674  | 48                  | Dark Iron Dwarves                   | -1 - Players cannot gain reputation with this faction |
| 694  | 189                 | Alliance Generic                    | -1 - Players cannot gain reputation with this faction |
| 695  | 749                 | Hydraxian Waterlords                | 42 - Hydraxian Waterlords                             |
| 714  | 66                  | Horde Generic                       | -1 - Players cannot gain reputation with this faction |
| 734  | 48                  | Dark Iron Dwarves                   | -1 - Players cannot gain reputation with this faction |
| 735  | 489                 | Goblin, Dark Iron Bar Patron        | -1 - Players cannot gain reputation with this faction |
| 736  | 489                 | Goblin, Dark Iron Bar Patron        | -1 - Players cannot gain reputation with this faction |
| 754  | 48                  | Dark Iron Dwarves                   | -1 - Players cannot gain reputation with this faction |
| 774  | 40                  | Escortee                            | -1 - Players cannot gain reputation with this faction |
| 775  | 40                  | Escortee                            | -1 - Players cannot gain reputation with this faction |
| 776  | 910                 | Brood of Nozdormu                   | 54 - Brood of Nozdormu                                |
| 777  | 912                 | Might of Kalimdor                   | -1 - Players cannot gain reputation with this faction |
| 778  | 511                 | Giant                               | -1 - Players cannot gain reputation with this faction |
| 794  | 529                 | Argent Dawn                         | 13 - Argent Dawn                                      |
| 795  | 572                 | Troll, Vilebranch                   | -1 - Players cannot gain reputation with this faction |
| 814  | 529                 | Argent Dawn                         | 13 - Argent Dawn                                      |
| 834  | 74                  | Elemental                           | -1 - Players cannot gain reputation with this faction |
| 854  | 577                 | Everlook                            | 28 - Everlook                                         |
| 855  | 577                 | Everlook                            | 28 - Everlook                                         |
| 874  | 589                 | Wintersaber Trainers                | 27 - Wintersaber Trainers                             |
| 875  | 54                  | Gnomeregan Exiles                   | 18 - Gnomeregan Exiles                                |
| 876  | 530                 | Darkspear Trolls                    | 15 - Darkspear Trolls                                 |
| 877  | 530                 | Darkspear Trolls                    | 15 - Darkspear Trolls                                 |
| 894  | 108                 | Theramore                           | -1 - Players cannot gain reputation with this faction |
| 914  | 679                 | Training Dummy                      | -1 - Players cannot gain reputation with this faction |
| 934  | 575                 | Furbolg, Uncorrupted                | -1 - Players cannot gain reputation with this faction |
| 954  | 73                  | Demon                               | -1 - Players cannot gain reputation with this faction |
| 974  | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 994  | 609                 | Cenarion Circle                     | 36 - Cenarion Circle                                  |
| 995  | 81                  | Thunder Bluff                       | 16 - Thunder Bluff                                    |
| 996  | 609                 | Cenarion Circle                     | 36 - Cenarion Circle                                  |
| 1014 | 629                 | Shatterspear Trolls                 | -1 - Players cannot gain reputation with this faction |
| 1015 | 629                 | Shatterspear Trolls                 | -1 - Players cannot gain reputation with this faction |
| 1034 | 66                  | Horde Generic                       | -1 - Players cannot gain reputation with this faction |
| 1054 | 189                 | Alliance Generic                    | -1 - Players cannot gain reputation with this faction |
| 1055 | 189                 | Alliance Generic                    | -1 - Players cannot gain reputation with this faction |
| 1074 | 76                  | Orgrimmar                           | 14 - Orgrimmar                                        |
| 1075 | 108                 | Theramore                           | -1 - Players cannot gain reputation with this faction |
| 1076 | 69                  | Darnassus                           | 21 - Darnassus                                        |
| 1077 | 108                 | Theramore                           | -1 - Players cannot gain reputation with this faction |
| 1078 | 72                  | Stormwind                           | 19 - Stormwind                                        |
| 1080 | 31                  | Friendly                            | -1 - Players cannot gain reputation with this faction |
| 1081 | 74                  | Elemental                           | -1 - Players cannot gain reputation with this faction |
| 1094 | 23                  | Beast - Boar                        | -1 - Players cannot gain reputation with this faction |
| 1095 | 679                 | Training Dummy                      | -1 - Players cannot gain reputation with this faction |
| 1096 | 108                 | Theramore                           | -1 - Players cannot gain reputation with this faction |
| 1097 | 69                  | Darnassus                           | 21 - Darnassus                                        |
| 1114 | 689                 | Dragonflight, Black - Bait          | -1 - Players cannot gain reputation with this faction |
| 1134 | 68                  | Undercity                           | 17 - Undercity                                        |
| 1154 | 68                  | Undercity                           | 17 - Undercity                                        |
| 1174 | 76                  | Orgrimmar                           | 14 - Orgrimmar                                        |
| 1194 | 709                 | Battleground Neutral                | -1 - Players cannot gain reputation with this faction |
| 1214 | 729                 | Frostwolf Clan                      | 41 - Frostwolf Clan                                   |
| 1215 | 729                 | Frostwolf Clan                      | 41 - Frostwolf Clan                                   |
| 1216 | 730                 | Stormpike Guard                     | 40 - Stormpike Guard                                  |
| 1217 | 730                 | Stormpike Guard                     | 40 - Stormpike Guard                                  |
| 1234 | 750                 | Sulfuron Firelords                  | -1 - Players cannot gain reputation with this faction |
| 1235 | 750                 | Sulfuron Firelords                  | -1 - Players cannot gain reputation with this faction |
| 1236 | 750                 | Sulfuron Firelords                  | -1 - Players cannot gain reputation with this faction |
| 1254 | 609                 | Cenarion Circle                     | 36 - Cenarion Circle                                  |
| 1274 | 7                   | Creature                            | -1 - Players cannot gain reputation with this faction |
| 1275 | 7                   | Creature                            | -1 - Players cannot gain reputation with this faction |
| 1294 | 771                 | Gizlock                             | -1 - Players cannot gain reputation with this faction |
| 1314 | 66                  | Horde Generic                       | -1 - Players cannot gain reputation with this faction |
| 1315 | 189                 | Alliance Generic                    | -1 - Players cannot gain reputation with this faction |
| 1334 | 730                 | Stormpike Guard                     | 40 - Stormpike Guard                                  |
| 1335 | 729                 | Frostwolf Clan                      | 41 - Frostwolf Clan                                   |
| 1354 | 809                 | Shen\'dralar                        | 44 - Shen\'dralar                                     |
| 1355 | 809                 | Shen\'dralar                        | 44 - Shen\'dralar                                     |
| 1374 | 829                 | Ogre (Captain Kromcrush)            | -1 - Players cannot gain reputation with this faction |
| 1375 | 77                  | Treasure                            | -1 - Players cannot gain reputation with this faction |
| 1394 | 80                  | Dragonflight, Black                 | -1 - Players cannot gain reputation with this faction |
| 1395 | 916                 | Silithid Attackers                  | -1 - Players cannot gain reputation with this faction |
| 1414 | 790                 | Spirit Guide - Alliance             | -1 - Players cannot gain reputation with this faction |
| 1415 | 849                 | Spirit Guide - Horde                | -1 - Players cannot gain reputation with this faction |
| 1434 | 869                 | Jaedenar                            | -1 - Players cannot gain reputation with this faction |
| 1454 | 36                  | Victim                              | -1 - Players cannot gain reputation with this faction |
| 1474 | 59                  | Thorium Brotherhood                 | 4 - Thorium Brotherhood                               |
| 1475 | 59                  | Thorium Brotherhood                 | 4 - Thorium Brotherhood                               |
| 1494 | 66                  | Horde Generic                       | -1 - Players cannot gain reputation with this faction |
| 1495 | 66                  | Horde Generic                       | -1 - Players cannot gain reputation with this faction |
| 1496 | 66                  | Horde Generic                       | -1 - Players cannot gain reputation with this faction |
| 1514 | 890                 | Silverwing Sentinels                | 45 - Silverwing Sentinels                             |
| 1515 | 889                 | Warsong Outriders                   | 46 - Warsong Outriders                                |
| 1534 | 730                 | Stormpike Guard                     | 40 - Stormpike Guard                                  |
| 1554 | 729                 | Frostwolf Clan                      | 41 - Frostwolf Clan                                   |
| 1555 | 909                 | Darkmoon Faire                      | 50 - Darkmoon Faire                                   |
| 1574 | 270                 | Zandalar Tribe                      | 51 - Zandalar Tribe                                   |
| 1575 | 72                  | Stormwind                           | 19 - Stormwind                                        |
| 1576 | 269                 | Silvermoon Remnant                  | -1 - Players cannot gain reputation with this faction |
| 1577 | 509                 | The League of Arathor               | 53 - The League of Arathor                            |
| 1594 | 69                  | Darnassus                           | 21 - Darnassus                                        |
| 1595 | 76                  | Orgrimmar                           | 14 - Orgrimmar                                        |
| 1596 | 730                 | Stormpike Guard                     | 40 - Stormpike Guard                                  |
| 1597 | 729                 | Frostwolf Clan                      | 41 - Frostwolf Clan                                   |
| 1598 | 510                 | The Defilers                        | 52 - The Defilers                                     |
| 1599 | 509                 | The League of Arathor               | 53 - The League of Arathor                            |
| 1600 | 69                  | Darnassus                           | 21 - Darnassus                                        |
| 1601 | 910                 | Brood of Nozdormu                   | 54 - Brood of Nozdormu                                |
| 1602 | 911                 | Silvermoon City                     | 55 - Silvermoon City                                  |
| 1603 | 911                 | Silvermoon City                     | 55 - Silvermoon City                                  |
| 1604 | 911                 | Silvermoon City                     | 55 - Silvermoon City                                  |
| 1605 | 531                 | Dragonflight, Bronze                | -1 - Players cannot gain reputation with this faction |
| 1606 | 7                   | Creature                            | -1 - Players cannot gain reputation with this faction |
| 1607 | 7                   | Creature                            | -1 - Players cannot gain reputation with this faction |
| 1608 | 609                 | Cenarion Circle                     | 36 - Cenarion Circle                                  |
| 1610 | 914                 | PLAYER, Blood Elf                   | -1 - Players cannot gain reputation with this faction |
| 1611 | 47                  | Ironforge                           | 20 - Ironforge                                        |
| 1612 | 76                  | Orgrimmar                           | 14 - Orgrimmar                                        |
| 1613 | 912                 | Might of Kalimdor                   | -1 - Players cannot gain reputation with this faction |
| 1614 | 14                  | Monster                             | -1 - Players cannot gain reputation with this faction |
| 1615 | 169                 | Steamwheedle Cartel                 | 10 - Steamwheedle Cartel                              |
| 1616 | 919                 | RC Objects                          | -1 - Players cannot gain reputation with this faction |
| 1617 | 918                 | RC Enemies                          | -1 - Players cannot gain reputation with this faction |
| 1618 | 47                  | Ironforge                           | 20 - Ironforge                                        |
| 1619 | 76                  | Orgrimmar                           | 14 - Orgrimmar                                        |
| 1620 | 128                 | Enemy                               | -1 - Players cannot gain reputation with this faction |
| 1621 | 921                 | Blue                                | -1 - Players cannot gain reputation with this faction |
| 1622 | 920                 | Red                                 | -1 - Players cannot gain reputation with this faction |
| 1623 | 922                 | Tranquillien                        | 56 - Tranquillien                                     |
| 1624 | 529                 | Argent Dawn                         | 13 - Argent Dawn                                      |
| 1625 | 529                 | Argent Dawn                         | 13 - Argent Dawn                                      |
| 1626 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 1627 | 923                 | Farstriders                         | -1 - Players cannot gain reputation with this faction |
| 1628 | 922                 | Tranquillien                        | 56 - Tranquillien                                     |
| 1629 | 927                 | PLAYER, Draenei                     | -1 - Players cannot gain reputation with this faction |
| 1630 | 928                 | Scourge Invaders                    | -1 - Players cannot gain reputation with this faction |
| 1634 | 928                 | Scourge Invaders                    | -1 - Players cannot gain reputation with this faction |
| 1635 | 169                 | Steamwheedle Cartel                 | 10 - Steamwheedle Cartel                              |
| 1636 | 923                 | Farstriders                         | -1 - Players cannot gain reputation with this faction |
| 1637 | 923                 | Farstriders                         | -1 - Players cannot gain reputation with this faction |
| 1638 | 930                 | Exodar                              | 49 - Exodar                                           |
| 1639 | 930                 | Exodar                              | 49 - Exodar                                           |
| 1640 | 930                 | Exodar                              | 49 - Exodar                                           |
| 1641 | 889                 | Warsong Outriders                   | 46 - Warsong Outriders                                |
| 1642 | 890                 | Silverwing Sentinels                | 45 - Silverwing Sentinels                             |
| 1643 | 937                 | Troll, Forest                       | -1 - Players cannot gain reputation with this faction |
| 1644 | 940                 | The Sons of Lothar                  | -1 - Players cannot gain reputation with this faction |
| 1645 | 940                 | The Sons of Lothar                  | -1 - Players cannot gain reputation with this faction |
| 1646 | 930                 | Exodar                              | 49 - Exodar                                           |
| 1647 | 930                 | Exodar                              | 49 - Exodar                                           |
| 1648 | 940                 | The Sons of Lothar                  | -1 - Players cannot gain reputation with this faction |
| 1649 | 940                 | The Sons of Lothar                  | -1 - Players cannot gain reputation with this faction |
| 1650 | 941                 | The Mag\'har                        | 61 - The Mag\'har                                     |
| 1651 | 941                 | The Mag\'har                        | 61 - The Mag\'har                                     |
| 1652 | 941                 | The Mag\'har                        | 61 - The Mag\'har                                     |
| 1653 | 941                 | The Mag\'har                        | 61 - The Mag\'har                                     |
| 1654 | 930                 | Exodar                              | 49 - Exodar                                           |
| 1655 | 930                 | Exodar                              | 49 - Exodar                                           |
| 1656 | 911                 | Silvermoon City                     | 55 - Silvermoon City                                  |
| 1657 | 911                 | Silvermoon City                     | 55 - Silvermoon City                                  |
| 1658 | 911                 | Silvermoon City                     | 55 - Silvermoon City                                  |
| 1659 | 942                 | Cenarion Expedition                 | 64 - Cenarion Expedition                              |
| 1660 | 942                 | Cenarion Expedition                 | 64 - Cenarion Expedition                              |
| 1661 | 942                 | Cenarion Expedition                 | 64 - Cenarion Expedition                              |
| 1662 | 943                 | Fel Orc                             | -1 - Players cannot gain reputation with this faction |
| 1663 | 944                 | Fel Orc Ghost                       | -1 - Players cannot gain reputation with this faction |
| 1664 | 945                 | Sons of Lothar Ghosts               | -1 - Players cannot gain reputation with this faction |
| 1666 | 946                 | Honor Hold                          | 38 - Honor Hold                                       |
| 1667 | 946                 | Honor Hold                          | 38 - Honor Hold                                       |
| 1668 | 947                 | Thrallmar                           | 37 - Thrallmar                                        |
| 1669 | 947                 | Thrallmar                           | 37 - Thrallmar                                        |
| 1670 | 947                 | Thrallmar                           | 37 - Thrallmar                                        |
| 1671 | 946                 | Honor Hold                          | 38 - Honor Hold                                       |
| 1672 | 949                 | Test Faction 1                      | 85 - Test Faction 1                                   |
| 1673 | 950                 | ToWoW - Flag                        | -1 - Players cannot gain reputation with this faction |
| 1674 | 953                 | Test Faction 4                      | -1 - Players cannot gain reputation with this faction |
| 1675 | 952                 | Test Faction 3                      | 87 - Test Faction 3                                   |
| 1676 | 954                 | ToWoW - Flag Trigger Horde (DND)    | -1 - Players cannot gain reputation with this faction |
| 1677 | 951                 | ToWoW - Flag Trigger Alliance (DND) | -1 - Players cannot gain reputation with this faction |
| 1678 | 956                 | Ethereum                            | -1 - Players cannot gain reputation with this faction |
| 1679 | 955                 | Broken                              | -1 - Players cannot gain reputation with this faction |
| 1680 | 74                  | Elemental                           | -1 - Players cannot gain reputation with this faction |
| 1681 | 957                 | Earth Elemental                     | -1 - Players cannot gain reputation with this faction |
| 1682 | 958                 | Fighting Robots                     | -1 - Players cannot gain reputation with this faction |
| 1683 | 959                 | Actor Good                          | -1 - Players cannot gain reputation with this faction |
| 1684 | 960                 | Actor Evil                          | -1 - Players cannot gain reputation with this faction |
| 1685 | 961                 | Stillpine Furbolg                   | -1 - Players cannot gain reputation with this faction |
| 1686 | 961                 | Stillpine Furbolg                   | -1 - Players cannot gain reputation with this faction |
| 1687 | 962                 | Crazed Owlkin                       | -1 - Players cannot gain reputation with this faction |
| 1688 | 963                 | Chess Alliance                      | -1 - Players cannot gain reputation with this faction |
| 1689 | 964                 | Chess Horde                         | -1 - Players cannot gain reputation with this faction |
| 1690 | 963                 | Chess Alliance                      | -1 - Players cannot gain reputation with this faction |
| 1691 | 964                 | Chess Horde                         | -1 - Players cannot gain reputation with this faction |
| 1692 | 965                 | Monster Spar                        | -1 - Players cannot gain reputation with this faction |
| 1693 | 966                 | Monster Spar Buddy                  | -1 - Players cannot gain reputation with this faction |
| 1694 | 930                 | Exodar                              | 49 - Exodar                                           |
| 1695 | 911                 | Silvermoon City                     | 55 - Silvermoon City                                  |
| 1696 | 967                 | The Violet Eye                      | 63 - The Violet Eye                                   |
| 1697 | 943                 | Fel Orc                             | -1 - Players cannot gain reputation with this faction |
| 1698 | 930                 | Exodar                              | 49 - Exodar                                           |
| 1699 | 930                 | Exodar                              | 49 - Exodar                                           |
| 1700 | 930                 | Exodar                              | 49 - Exodar                                           |
| 1701 | 968                 | Sunhawks                            | -1 - Players cannot gain reputation with this faction |
| 1702 | 968                 | Sunhawks                            | -1 - Players cannot gain reputation with this faction |
| 1703 | 679                 | Training Dummy                      | -1 - Players cannot gain reputation with this faction |
| 1704 | 943                 | Fel Orc                             | -1 - Players cannot gain reputation with this faction |
| 1705 | 943                 | Fel Orc                             | -1 - Players cannot gain reputation with this faction |
| 1706 | 971                 | Fungal Giant                        | -1 - Players cannot gain reputation with this faction |
| 1707 | 970                 | Sporeggar                           | 65 - Sporeggar                                        |
| 1708 | 970                 | Sporeggar                           | 65 - Sporeggar                                        |
| 1709 | 970                 | Sporeggar                           | 65 - Sporeggar                                        |
| 1710 | 942                 | Cenarion Expedition                 | 64 - Cenarion Expedition                              |
| 1711 | 973                 | Monster, Predator                   | -1 - Players cannot gain reputation with this faction |
| 1712 | 974                 | Monster, Prey                       | -1 - Players cannot gain reputation with this faction |
| 1713 | 974                 | Monster, Prey                       | -1 - Players cannot gain reputation with this faction |
| 1714 | 968                 | Sunhawks                            | -1 - Players cannot gain reputation with this faction |
| 1715 | 975                 | Void Anomaly                        | -1 - Players cannot gain reputation with this faction |
| 1716 | 976                 | Hyjal Defenders                     | -1 - Players cannot gain reputation with this faction |
| 1717 | 976                 | Hyjal Defenders                     | -1 - Players cannot gain reputation with this faction |
| 1718 | 976                 | Hyjal Defenders                     | -1 - Players cannot gain reputation with this faction |
| 1719 | 976                 | Hyjal Defenders                     | -1 - Players cannot gain reputation with this faction |
| 1720 | 977                 | Hyjal Invaders                      | -1 - Players cannot gain reputation with this faction |
| 1721 | 978                 | Kurenai                             | 66 - Kurenai                                          |
| 1722 | 978                 | Kurenai                             | 66 - Kurenai                                          |
| 1723 | 978                 | Kurenai                             | 66 - Kurenai                                          |
| 1724 | 978                 | Kurenai                             | 66 - Kurenai                                          |
| 1725 | 979                 | Earthen Ring                        | -1 - Players cannot gain reputation with this faction |
| 1726 | 979                 | Earthen Ring                        | -1 - Players cannot gain reputation with this faction |
| 1727 | 979                 | Earthen Ring                        | -1 - Players cannot gain reputation with this faction |
| 1728 | 942                 | Cenarion Expedition                 | 64 - Cenarion Expedition                              |
| 1729 | 947                 | Thrallmar                           | 37 - Thrallmar                                        |
| 1730 | 933                 | The Consortium                      | 60 - The Consortium                                   |
| 1731 | 933                 | The Consortium                      | 60 - The Consortium                                   |
| 1732 | 189                 | Alliance Generic                    | -1 - Players cannot gain reputation with this faction |
| 1733 | 189                 | Alliance Generic                    | -1 - Players cannot gain reputation with this faction |
| 1734 | 66                  | Horde Generic                       | -1 - Players cannot gain reputation with this faction |
| 1735 | 66                  | Horde Generic                       | -1 - Players cannot gain reputation with this faction |
| 1736 | 966                 | Monster Spar Buddy                  | -1 - Players cannot gain reputation with this faction |
| 1737 | 946                 | Honor Hold                          | 38 - Honor Hold                                       |
| 1738 | 981                 | Arakkoa                             | -1 - Players cannot gain reputation with this faction |
| 1739 | 982                 | Zangarmarsh Banner (Alliance)       | -1 - Players cannot gain reputation with this faction |
| 1740 | 983                 | Zangarmarsh Banner (Horde)          | -1 - Players cannot gain reputation with this faction |
| 1741 | 935                 | The Sha\'tar                        | 39 - The Sha\'tar                                     |
| 1742 | 984                 | Zangarmarsh Banner (Neutral)        | -1 - Players cannot gain reputation with this faction |
| 1743 | 932                 | The Aldor                           | 58 - The Aldor                                        |
| 1744 | 934                 | The Scryers                         | 62 - The Scryers                                      |
| 1745 | 911                 | Silvermoon City                     | 55 - Silvermoon City                                  |
| 1746 | 934                 | The Scryers                         | 62 - The Scryers                                      |
| 1747 | 985                 | Caverns of Time - Thrall            | -1 - Players cannot gain reputation with this faction |
| 1748 | 986                 | Caverns of Time - Durnholde         | -1 - Players cannot gain reputation with this faction |
| 1749 | 987                 | Caverns of Time - Southshore Guards | -1 - Players cannot gain reputation with this faction |
| 1750 | 988                 | Shadow Council Covert               | -1 - Players cannot gain reputation with this faction |
| 1751 | 14                  | Monster                             | -1 - Players cannot gain reputation with this faction |
| 1752 | 993                 | Dark Portal Attacker, Legion        | -1 - Players cannot gain reputation with this faction |
| 1753 | 993                 | Dark Portal Attacker, Legion        | -1 - Players cannot gain reputation with this faction |
| 1754 | 993                 | Dark Portal Attacker, Legion        | -1 - Players cannot gain reputation with this faction |
| 1755 | 991                 | Dark Portal Defender, Alliance      | -1 - Players cannot gain reputation with this faction |
| 1756 | 991                 | Dark Portal Defender, Alliance      | -1 - Players cannot gain reputation with this faction |
| 1757 | 991                 | Dark Portal Defender, Alliance      | -1 - Players cannot gain reputation with this faction |
| 1758 | 992                 | Dark Portal Defender, Horde         | -1 - Players cannot gain reputation with this faction |
| 1759 | 992                 | Dark Portal Defender, Horde         | -1 - Players cannot gain reputation with this faction |
| 1760 | 992                 | Dark Portal Defender, Horde         | -1 - Players cannot gain reputation with this faction |
| 1761 | 994                 | Inciter Trigger                     | -1 - Players cannot gain reputation with this faction |
| 1762 | 995                 | Inciter Trigger 2                   | -1 - Players cannot gain reputation with this faction |
| 1763 | 996                 | Inciter Trigger 3                   | -1 - Players cannot gain reputation with this faction |
| 1764 | 997                 | Inciter Trigger 4                   | -1 - Players cannot gain reputation with this faction |
| 1765 | 998                 | Inciter Trigger 5                   | -1 - Players cannot gain reputation with this faction |
| 1766 | 529                 | Argent Dawn                         | 13 - Argent Dawn                                      |
| 1767 | 529                 | Argent Dawn                         | 13 - Argent Dawn                                      |
| 1768 | 73                  | Demon                               | -1 - Players cannot gain reputation with this faction |
| 1769 | 73                  | Demon                               | -1 - Players cannot gain reputation with this faction |
| 1770 | 959                 | Actor Good                          | -1 - Players cannot gain reputation with this faction |
| 1771 | 960                 | Actor Evil                          | -1 - Players cannot gain reputation with this faction |
| 1772 | 999                 | Mana Creature                       | -1 - Players cannot gain reputation with this faction |
| 1773 | 1000                | Khadgar\'s Servant                  | -1 - Players cannot gain reputation with this faction |
| 1774 | 31                  | Friendly                            | -1 - Players cannot gain reputation with this faction |
| 1775 | 935                 | The Sha\'tar                        | 39 - The Sha\'tar                                     |
| 1776 | 932                 | The Aldor                           | 58 - The Aldor                                        |
| 1777 | 932                 | The Aldor                           | 58 - The Aldor                                        |
| 1778 | 990                 | The Scale of the Sands              | 57 - The Scale of the Sands                           |
| 1779 | 989                 | Keepers of Time                     | 67 - Keepers of Time                                  |
| 1780 | 1001                | Bladespire Clan                     | -1 - Players cannot gain reputation with this faction |
| 1781 | 929                 | Bloodmaul Clan                      | -1 - Players cannot gain reputation with this faction |
| 1782 | 1001                | Bladespire Clan                     | -1 - Players cannot gain reputation with this faction |
| 1783 | 929                 | Bloodmaul Clan                      | -1 - Players cannot gain reputation with this faction |
| 1784 | 1001                | Bladespire Clan                     | -1 - Players cannot gain reputation with this faction |
| 1785 | 929                 | Bloodmaul Clan                      | -1 - Players cannot gain reputation with this faction |
| 1786 | 73                  | Demon                               | -1 - Players cannot gain reputation with this faction |
| 1787 | 14                  | Monster                             | -1 - Players cannot gain reputation with this faction |
| 1788 | 933                 | The Consortium                      | 60 - The Consortium                                   |
| 1789 | 968                 | Sunhawks                            | -1 - Players cannot gain reputation with this faction |
| 1790 | 1001                | Bladespire Clan                     | -1 - Players cannot gain reputation with this faction |
| 1791 | 929                 | Bloodmaul Clan                      | -1 - Players cannot gain reputation with this faction |
| 1792 | 943                 | Fel Orc                             | -1 - Players cannot gain reputation with this faction |
| 1793 | 968                 | Sunhawks                            | -1 - Players cannot gain reputation with this faction |
| 1794 | 1003                | Protectorate                        | -1 - Players cannot gain reputation with this faction |
| 1795 | 1003                | Protectorate                        | -1 - Players cannot gain reputation with this faction |
| 1796 | 956                 | Ethereum                            | -1 - Players cannot gain reputation with this faction |
| 1797 | 1003                | Protectorate                        | -1 - Players cannot gain reputation with this faction |
| 1798 | 1004                | Arcane Annihilator (DNR)            | -1 - Players cannot gain reputation with this faction |
| 1799 | 1002                | Ethereum Sparbuddy                  | -1 - Players cannot gain reputation with this faction |
| 1800 | 956                 | Ethereum                            | -1 - Players cannot gain reputation with this faction |
| 1801 | 67                  | Horde                               | 12 - Horde                                            |
| 1802 | 469                 | Alliance                            | 11 - Alliance                                         |
| 1803 | 148                 | Ambient                             | -1 - Players cannot gain reputation with this faction |
| 1804 | 148                 | Ambient                             | -1 - Players cannot gain reputation with this faction |
| 1805 | 932                 | The Aldor                           | 58 - The Aldor                                        |
| 1806 | 31                  | Friendly                            | -1 - Players cannot gain reputation with this faction |
| 1807 | 1003                | Protectorate                        | -1 - Players cannot gain reputation with this faction |
| 1808 | 1007                | Kirin\'Var - Belmara                | -1 - Players cannot gain reputation with this faction |
| 1809 | 1009                | Kirin\'Var - Cohlien                | -1 - Players cannot gain reputation with this faction |
| 1810 | 1006                | Kirin\'Var - Dathric                | -1 - Players cannot gain reputation with this faction |
| 1811 | 1008                | Kirin\'Var - Luminrath              | -1 - Players cannot gain reputation with this faction |
| 1812 | 31                  | Friendly                            | -1 - Players cannot gain reputation with this faction |
| 1813 | 1010                | Servant of Illidan                  | -1 - Players cannot gain reputation with this faction |
| 1814 | 966                 | Monster Spar Buddy                  | -1 - Players cannot gain reputation with this faction |
| 1815 | 29                  | Beast - Wolf                        | -1 - Players cannot gain reputation with this faction |
| 1816 | 31                  | Friendly                            | -1 - Players cannot gain reputation with this faction |
| 1818 | 1011                | Lower City                          | 69 - Lower City                                       |
| 1819 | 189                 | Alliance Generic                    | -1 - Players cannot gain reputation with this faction |
| 1820 | 1012                | Ashtongue Deathsworn                | 70 - Ashtongue Deathsworn                             |
| 1821 | 1013                | Spirits of Shadowmoon 1             | -1 - Players cannot gain reputation with this faction |
| 1822 | 1014                | Spirits of Shadowmoon 2             | -1 - Players cannot gain reputation with this faction |
| 1823 | 956                 | Ethereum                            | -1 - Players cannot gain reputation with this faction |
| 1824 | 1015                | Netherwing                          | 71 - Netherwing                                       |
| 1825 | 73                  | Demon                               | -1 - Players cannot gain reputation with this faction |
| 1826 | 1010                | Servant of Illidan                  | -1 - Players cannot gain reputation with this faction |
| 1827 | 1016                | Wyrmcult                            | -1 - Players cannot gain reputation with this faction |
| 1828 | 1017                | Treant                              | -1 - Players cannot gain reputation with this faction |
| 1829 | 1018                | Leotheras Demon I                   | -1 - Players cannot gain reputation with this faction |
| 1830 | 1019                | Leotheras Demon II                  | -1 - Players cannot gain reputation with this faction |
| 1831 | 1020                | Leotheras Demon III                 | -1 - Players cannot gain reputation with this faction |
| 1832 | 1021                | Leotheras Demon IV                  | -1 - Players cannot gain reputation with this faction |
| 1833 | 1022                | Leotheras Demon V                   | -1 - Players cannot gain reputation with this faction |
| 1834 | 1023                | Azaloth                             | -1 - Players cannot gain reputation with this faction |
| 1835 | 66                  | Horde Generic                       | -1 - Players cannot gain reputation with this faction |
| 1836 | 933                 | The Consortium                      | 60 - The Consortium                                   |
| 1837 | 970                 | Sporeggar                           | 65 - Sporeggar                                        |
| 1838 | 934                 | The Scryers                         | 62 - The Scryers                                      |
| 1839 | 1024                | Rock Flayer                         | -1 - Players cannot gain reputation with this faction |
| 1840 | 1025                | Flayer Hunter                       | -1 - Players cannot gain reputation with this faction |
| 1841 | 1026                | Shadowmoon Shade                    | -1 - Players cannot gain reputation with this faction |
| 1842 | 1027                | Legion Communicator                 | -1 - Players cannot gain reputation with this faction |
| 1843 | 1010                | Servant of Illidan                  | -1 - Players cannot gain reputation with this faction |
| 1844 | 932                 | The Aldor                           | 58 - The Aldor                                        |
| 1845 | 934                 | The Scryers                         | 62 - The Scryers                                      |
| 1846 | 1028                | Ravenswood Ancients                 | -1 - Players cannot gain reputation with this faction |
| 1847 | 965                 | Monster Spar                        | -1 - Players cannot gain reputation with this faction |
| 1848 | 966                 | Monster Spar Buddy                  | -1 - Players cannot gain reputation with this faction |
| 1849 | 1010                | Servant of Illidan                  | -1 - Players cannot gain reputation with this faction |
| 1850 | 1015                | Netherwing                          | 71 - Netherwing                                       |
| 1851 | 1011                | Lower City                          | 69 - Lower City                                       |
| 1852 | 1029                | Chess, Friendly to All Chess        | -1 - Players cannot gain reputation with this faction |
| 1853 | 1010                | Servant of Illidan                  | -1 - Players cannot gain reputation with this faction |
| 1854 | 932                 | The Aldor                           | 58 - The Aldor                                        |
| 1855 | 934                 | The Scryers                         | 62 - The Scryers                                      |
| 1856 | 1031                | Sha\'tari Skyguard                  | 72 - Sha\'tari Skyguard                               |
| 1857 | 31                  | Friendly                            | -1 - Players cannot gain reputation with this faction |
| 1858 | 1012                | Ashtongue Deathsworn                | 70 - Ashtongue Deathsworn                             |
| 1859 | 1033                | Maiev                               | -1 - Players cannot gain reputation with this faction |
| 1860 | 1034                | Skettis Shadowy Arakkoa             | -1 - Players cannot gain reputation with this faction |
| 1862 | 1035                | Skettis Arakkoa                     | -1 - Players cannot gain reputation with this faction |
| 1863 | 52                  | Orc, Dragonmaw                      | -1 - Players cannot gain reputation with this faction |
| 1864 | 1036                | Dragonmaw Enemy                     | -1 - Players cannot gain reputation with this faction |
| 1865 | 52                  | Orc, Dragonmaw                      | -1 - Players cannot gain reputation with this faction |
| 1866 | 1012                | Ashtongue Deathsworn                | 70 - Ashtongue Deathsworn                             |
| 1867 | 1033                | Maiev                               | -1 - Players cannot gain reputation with this faction |
| 1868 | 966                 | Monster Spar Buddy                  | -1 - Players cannot gain reputation with this faction |
| 1869 | 981                 | Arakkoa                             | -1 - Players cannot gain reputation with this faction |
| 1870 | 1031                | Sha\'tari Skyguard                  | 72 - Sha\'tari Skyguard                               |
| 1871 | 1035                | Skettis Arakkoa                     | -1 - Players cannot gain reputation with this faction |
| 1872 | 1038                | Ogri\'la                            | 73 - Ogri\'la                                         |
| 1873 | 1024                | Rock Flayer                         | -1 - Players cannot gain reputation with this faction |
| 1874 | 1038                | Ogri\'la                            | 73 - Ogri\'la                                         |
| 1875 | 932                 | The Aldor                           | 58 - The Aldor                                        |
| 1876 | 934                 | The Scryers                         | 62 - The Scryers                                      |
| 1877 | 52                  | Orc, Dragonmaw                      | -1 - Players cannot gain reputation with this faction |
| 1878 | 1041                | Frenzy                              | -1 - Players cannot gain reputation with this faction |
| 1879 | 1042                | Skyguard Enemy                      | -1 - Players cannot gain reputation with this faction |
| 1880 | 52                  | Orc, Dragonmaw                      | -1 - Players cannot gain reputation with this faction |
| 1881 | 1035                | Skettis Arakkoa                     | -1 - Players cannot gain reputation with this faction |
| 1882 | 1010                | Servant of Illidan                  | -1 - Players cannot gain reputation with this faction |
| 1883 | 1044                | Theramore Deserter                  | -1 - Players cannot gain reputation with this faction |
| 1884 | 1047                | Tuskarr                             | -1 - Players cannot gain reputation with this faction |
| 1885 | 1045                | Vrykul                              | -1 - Players cannot gain reputation with this faction |
| 1886 | 7                   | Creature                            | -1 - Players cannot gain reputation with this faction |
| 1887 | 7                   | Creature                            | -1 - Players cannot gain reputation with this faction |
| 1888 | 1046                | Northsea Pirates                    | -1 - Players cannot gain reputation with this faction |
| 1889 | 1048                | UNUSED                              | -1 - Players cannot gain reputation with this faction |
| 1890 | 1049                | Troll, Amani                        | -1 - Players cannot gain reputation with this faction |
| 1891 | 1050                | Valiance Expedition                 | 74 - Valiance Expedition                              |
| 1892 | 1050                | Valiance Expedition                 | 74 - Valiance Expedition                              |
| 1893 | 1050                | Valiance Expedition                 | 74 - Valiance Expedition                              |
| 1894 | 1045                | Vrykul                              | -1 - Players cannot gain reputation with this faction |
| 1895 | 1045                | Vrykul                              | -1 - Players cannot gain reputation with this faction |
| 1896 | 909                 | Darkmoon Faire                      | 50 - Darkmoon Faire                                   |
| 1897 | 1067                | The Hand of Vengeance               | 77 - The Hand of Vengeance                            |
| 1898 | 1050                | Valiance Expedition                 | 74 - Valiance Expedition                              |
| 1899 | 1050                | Valiance Expedition                 | 74 - Valiance Expedition                              |
| 1900 | 1067                | The Hand of Vengeance               | 77 - The Hand of Vengeance                            |
| 1901 | 1052                | Horde Expedition                    | 75 - Horde Expedition                                 |
| 1902 | 960                 | Actor Evil                          | -1 - Players cannot gain reputation with this faction |
| 1904 | 960                 | Actor Evil                          | -1 - Players cannot gain reputation with this faction |
| 1905 | 1055                | Tamed Plaguehound                   | -1 - Players cannot gain reputation with this faction |
| 1906 | 1054                | Spotted Gryphon                     | -1 - Players cannot gain reputation with this faction |
| 1907 | 949                 | Test Faction 1                      | 85 - Test Faction 1                                   |
| 1908 | 949                 | Test Faction 1                      | 85 - Test Faction 1                                   |
| 1909 | 42                  | Beast - Raptor                      | -1 - Players cannot gain reputation with this faction |
| 1910 | 1056                | Vrykul (Ancient Spirit 1)           | -1 - Players cannot gain reputation with this faction |
| 1911 | 1057                | Vrykul (Ancient Siprit 2)           | -1 - Players cannot gain reputation with this faction |
| 1912 | 1058                | Vrykul (Ancient Siprit 3)           | -1 - Players cannot gain reputation with this faction |
| 1913 | 1059                | CTF - Flag - Alliance               | -1 - Players cannot gain reputation with this faction |
| 1914 | 1045                | Vrykul                              | -1 - Players cannot gain reputation with this faction |
| 1915 | 1060                | Test                                | -1 - Players cannot gain reputation with this faction |
| 1916 | 1033                | Maiev                               | -1 - Players cannot gain reputation with this faction |
| 1917 | 7                   | Creature                            | -1 - Players cannot gain reputation with this faction |
| 1918 | 1052                | Horde Expedition                    | 75 - Horde Expedition                                 |
| 1919 | 1062                | Vrykul Gladiator                    | -1 - Players cannot gain reputation with this faction |
| 1920 | 1063                | Valgarde Combatant                  | -1 - Players cannot gain reputation with this faction |
| 1921 | 1064                | The Taunka                          | 76 - The Taunka                                       |
| 1922 | 1064                | The Taunka                          | 76 - The Taunka                                       |
| 1923 | 1064                | The Taunka                          | 76 - The Taunka                                       |
| 1924 | 1065                | Monster, Zone Force Reaction 1      | -1 - Players cannot gain reputation with this faction |
| 1925 | 14                  | Monster                             | -1 - Players cannot gain reputation with this faction |
| 1926 | 1068                | Explorers\' League                  | 78 - Explorers\' League                               |
| 1927 | 1068                | Explorers\' League                  | 78 - Explorers\' League                               |
| 1928 | 1067                | The Hand of Vengeance               | 77 - The Hand of Vengeance                            |
| 1929 | 1067                | The Hand of Vengeance               | 77 - The Hand of Vengeance                            |
| 1930 | 1069                | Ram Racing Powerup DND              | -1 - Players cannot gain reputation with this faction |
| 1931 | 1070                | Ram Racing Trap DND                 | -1 - Players cannot gain reputation with this faction |
| 1932 | 74                  | Elemental                           | -1 - Players cannot gain reputation with this faction |
| 1933 | 31                  | Friendly                            | -1 - Players cannot gain reputation with this faction |
| 1934 | 959                 | Actor Good                          | -1 - Players cannot gain reputation with this faction |
| 1935 | 959                 | Actor Good                          | -1 - Players cannot gain reputation with this faction |
| 1936 | 1071                | Craig\'s Squirrels                  | -1 - Players cannot gain reputation with this faction |
| 1937 | 1071                | Craig\'s Squirrels                  | -1 - Players cannot gain reputation with this faction |
| 1938 | 1071                | Craig\'s Squirrels                  | -1 - Players cannot gain reputation with this faction |
| 1939 | 1071                | Craig\'s Squirrels                  | -1 - Players cannot gain reputation with this faction |
| 1940 | 1071                | Craig\'s Squirrels                  | -1 - Players cannot gain reputation with this faction |
| 1941 | 1071                | Craig\'s Squirrels                  | -1 - Players cannot gain reputation with this faction |
| 1942 | 1071                | Craig\'s Squirrels                  | -1 - Players cannot gain reputation with this faction |
| 1943 | 1071                | Craig\'s Squirrels                  | -1 - Players cannot gain reputation with this faction |
| 1944 | 1071                | Craig\'s Squirrels                  | -1 - Players cannot gain reputation with this faction |
| 1945 | 1071                | Craig\'s Squirrels                  | -1 - Players cannot gain reputation with this faction |
| 1947 | 1071                | Craig\'s Squirrels                  | -1 - Players cannot gain reputation with this faction |
| 1948 | 921                 | Blue                                | -1 - Players cannot gain reputation with this faction |
| 1949 | 1073                | The Kalu\'ak                        | 79 - The Kalu\'ak                                     |
| 1950 | 1073                | The Kalu\'ak                        | 79 - The Kalu\'ak                                     |
| 1951 | 69                  | Darnassus                           | 21 - Darnassus                                        |
| 1952 | 1074                | Holiday - Water Barrel              | -1 - Players cannot gain reputation with this faction |
| 1953 | 973                 | Monster, Predator                   | -1 - Players cannot gain reputation with this faction |
| 1954 | 1076                | Iron Dwarves                        | -1 - Players cannot gain reputation with this faction |
| 1955 | 1076                | Iron Dwarves                        | -1 - Players cannot gain reputation with this faction |
| 1956 | 1077                | Shattered Sun Offensive             | 80 - Shattered Sun Offensive                          |
| 1957 | 1077                | Shattered Sun Offensive             | 80 - Shattered Sun Offensive                          |
| 1958 | 960                 | Actor Evil                          | -1 - Players cannot gain reputation with this faction |
| 1959 | 960                 | Actor Evil                          | -1 - Players cannot gain reputation with this faction |
| 1960 | 1077                | Shattered Sun Offensive             | 80 - Shattered Sun Offensive                          |
| 1961 | 1078                | Fighting Vanity Pet                 | -1 - Players cannot gain reputation with this faction |
| 1962 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 1963 | 73                  | Demon                               | -1 - Players cannot gain reputation with this faction |
| 1964 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 1965 | 965                 | Monster Spar                        | -1 - Players cannot gain reputation with this faction |
| 1966 | 19                  | Murloc                              | -1 - Players cannot gain reputation with this faction |
| 1967 | 1077                | Shattered Sun Offensive             | 80 - Shattered Sun Offensive                          |
| 1968 | 1079                | Murloc, Winterfin                   | -1 - Players cannot gain reputation with this faction |
| 1969 | 19                  | Murloc                              | -1 - Players cannot gain reputation with this faction |
| 1970 | 14                  | Monster                             | -1 - Players cannot gain reputation with this faction |
| 1971 | 1080                | Friendly, Force Reaction            | -1 - Players cannot gain reputation with this faction |
| 1972 | 1081                | Object, Force Reaction              | -1 - Players cannot gain reputation with this faction |
| 1973 | 1050                | Valiance Expedition                 | 74 - Valiance Expedition                              |
| 1974 | 1050                | Valiance Expedition                 | 74 - Valiance Expedition                              |
| 1975 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 1976 | 1050                | Valiance Expedition                 | 74 - Valiance Expedition                              |
| 1977 | 1050                | Valiance Expedition                 | 74 - Valiance Expedition                              |
| 1978 | 1085                | Warsong Offensive                   | 81 - Warsong Offensive                                |
| 1979 | 1085                | Warsong Offensive                   | 81 - Warsong Offensive                                |
| 1980 | 1085                | Warsong Offensive                   | 81 - Warsong Offensive                                |
| 1981 | 1085                | Warsong Offensive                   | 81 - Warsong Offensive                                |
| 1982 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 1983 | 965                 | Monster Spar                        | -1 - Players cannot gain reputation with this faction |
| 1984 | 966                 | Monster Spar Buddy                  | -1 - Players cannot gain reputation with this faction |
| 1985 | 14                  | Monster                             | -1 - Players cannot gain reputation with this faction |
| 1986 | 40                  | Escortee                            | -1 - Players cannot gain reputation with this faction |
| 1987 | 942                 | Cenarion Expedition                 | 64 - Cenarion Expedition                              |
| 1988 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 1989 | 1086                | Poacher                             | -1 - Players cannot gain reputation with this faction |
| 1990 | 148                 | Ambient                             | -1 - Players cannot gain reputation with this faction |
| 1991 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 1992 | 14                  | Monster                             | -1 - Players cannot gain reputation with this faction |
| 1993 | 965                 | Monster Spar                        | -1 - Players cannot gain reputation with this faction |
| 1994 | 966                 | Monster Spar Buddy                  | -1 - Players cannot gain reputation with this faction |
| 1995 | 1059                | CTF - Flag - Alliance               | -1 - Players cannot gain reputation with this faction |
| 1997 | 1059                | CTF - Flag - Alliance               | -1 - Players cannot gain reputation with this faction |
| 1998 | 1087                | Holiday Monster                     | -1 - Players cannot gain reputation with this faction |
| 1999 | 974                 | Monster, Prey                       | -1 - Players cannot gain reputation with this faction |
| 2000 | 974                 | Monster, Prey                       | -1 - Players cannot gain reputation with this faction |
| 2001 | 1088                | Furbolg, Redfang                    | -1 - Players cannot gain reputation with this faction |
| 2003 | 1089                | Furbolg, Frostpaw                   | -1 - Players cannot gain reputation with this faction |
| 2004 | 1050                | Valiance Expedition                 | 74 - Valiance Expedition                              |
| 2005 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 2006 | 1090                | Kirin Tor                           | 84 - Kirin Tor                                        |
| 2007 | 1090                | Kirin Tor                           | 84 - Kirin Tor                                        |
| 2008 | 1090                | Kirin Tor                           | 84 - Kirin Tor                                        |
| 2009 | 1090                | Kirin Tor                           | 84 - Kirin Tor                                        |
| 2010 | 1091                | The Wyrmrest Accord                 | 83 - The Wyrmrest Accord                              |
| 2011 | 1091                | The Wyrmrest Accord                 | 83 - The Wyrmrest Accord                              |
| 2012 | 1091                | The Wyrmrest Accord                 | 83 - The Wyrmrest Accord                              |
| 2013 | 1091                | The Wyrmrest Accord                 | 83 - The Wyrmrest Accord                              |
| 2014 | 1092                | Azjol-Nerub                         | -1 - Players cannot gain reputation with this faction |
| 2016 | 1092                | Azjol-Nerub                         | -1 - Players cannot gain reputation with this faction |
| 2017 | 1092                | Azjol-Nerub                         | -1 - Players cannot gain reputation with this faction |
| 2018 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 2019 | 1064                | The Taunka                          | 76 - The Taunka                                       |
| 2020 | 1085                | Warsong Offensive                   | 81 - Warsong Offensive                                |
| 2021 | 1082                | REUSE                               | 82 - REUSE                                            |
| 2022 | 14                  | Monster                             | -1 - Players cannot gain reputation with this faction |
| 2023 | 928                 | Scourge Invaders                    | -1 - Players cannot gain reputation with this faction |
| 2024 | 1067                | The Hand of Vengeance               | 77 - The Hand of Vengeance                            |
| 2025 | 1094                | The Silver Covenant                 | 90 - The Silver Covenant                              |
| 2026 | 1094                | The Silver Covenant                 | 90 - The Silver Covenant                              |
| 2027 | 1094                | The Silver Covenant                 | 90 - The Silver Covenant                              |
| 2028 | 148                 | Ambient                             | -1 - Players cannot gain reputation with this faction |
| 2029 | 973                 | Monster, Predator                   | -1 - Players cannot gain reputation with this faction |
| 2030 | 973                 | Monster, Predator                   | -1 - Players cannot gain reputation with this faction |
| 2031 | 66                  | Horde Generic                       | -1 - Players cannot gain reputation with this faction |
| 2032 | 1095                | Grizzly Hills Trapper               | -1 - Players cannot gain reputation with this faction |
| 2033 | 14                  | Monster                             | -1 - Players cannot gain reputation with this faction |
| 2034 | 1085                | Warsong Offensive                   | 81 - Warsong Offensive                                |
| 2035 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 2036 | 31                  | Friendly                            | -1 - Players cannot gain reputation with this faction |
| 2037 | 1050                | Valiance Expedition                 | 74 - Valiance Expedition                              |
| 2038 | 148                 | Ambient                             | -1 - Players cannot gain reputation with this faction |
| 2039 | 14                  | Monster                             | -1 - Players cannot gain reputation with this faction |
| 2040 | 1050                | Valiance Expedition                 | 74 - Valiance Expedition                              |
| 2041 | 1091                | The Wyrmrest Accord                 | 83 - The Wyrmrest Accord                              |
| 2042 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 2043 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 2044 | 1050                | Valiance Expedition                 | 74 - Valiance Expedition                              |
| 2045 | 1085                | Warsong Offensive                   | 81 - Warsong Offensive                                |
| 2046 | 40                  | Escortee                            | -1 - Players cannot gain reputation with this faction |
| 2047 | 1073                | The Kalu\'ak                        | 79 - The Kalu\'ak                                     |
| 2048 | 928                 | Scourge Invaders                    | -1 - Players cannot gain reputation with this faction |
| 2049 | 928                 | Scourge Invaders                    | -1 - Players cannot gain reputation with this faction |
| 2050 | 1098                | Knights of the Ebon Blade           | 91 - Knights of the Ebon Blade                        |
| 2051 | 1098                | Knights of the Ebon Blade           | 91 - Knights of the Ebon Blade                        |
| 2052 | 1099                | Wrathgate Scourge                   | -1 - Players cannot gain reputation with this faction |
| 2053 | 1100                | Wrathgate Alliance                  | -1 - Players cannot gain reputation with this faction |
| 2054 | 1101                | Wrathgate Horde                     | -1 - Players cannot gain reputation with this faction |
| 2055 | 965                 | Monster Spar                        | -1 - Players cannot gain reputation with this faction |
| 2056 | 966                 | Monster Spar Buddy                  | -1 - Players cannot gain reputation with this faction |
| 2057 | 1066                | Monster, Zone Force Reaction 2      | -1 - Players cannot gain reputation with this faction |
| 2058 | 1102                | CTF - Flag - Horde                  | -1 - Players cannot gain reputation with this faction |
| 2059 | 1103                | CTF - Flag - Neutral                | -1 - Players cannot gain reputation with this faction |
| 2060 | 1104                | Frenzyheart Tribe                   | 92 - Frenzyheart Tribe                                |
| 2061 | 1104                | Frenzyheart Tribe                   | 92 - Frenzyheart Tribe                                |
| 2062 | 1104                | Frenzyheart Tribe                   | 92 - Frenzyheart Tribe                                |
| 2063 | 1105                | The Oracles                         | 93 - The Oracles                                      |
| 2064 | 1105                | The Oracles                         | 93 - The Oracles                                      |
| 2065 | 1105                | The Oracles                         | 93 - The Oracles                                      |
| 2066 | 1105                | The Oracles                         | 93 - The Oracles                                      |
| 2067 | 1091                | The Wyrmrest Accord                 | 83 - The Wyrmrest Accord                              |
| 2068 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 2069 | 1107                | Troll, Drakkari                     | -1 - Players cannot gain reputation with this faction |
| 2070 | 1106                | Argent Crusade                      | 94 - Argent Crusade                                   |
| 2071 | 1106                | Argent Crusade                      | 94 - Argent Crusade                                   |
| 2072 | 1106                | Argent Crusade                      | 94 - Argent Crusade                                   |
| 2073 | 1106                | Argent Crusade                      | 94 - Argent Crusade                                   |
| 2074 | 986                 | Caverns of Time - Durnholde         | -1 - Players cannot gain reputation with this faction |
| 2075 | 1110                | CoT Scourge                         | -1 - Players cannot gain reputation with this faction |
| 2076 | 1108                | CoT Arthas                          | -1 - Players cannot gain reputation with this faction |
| 2077 | 1108                | CoT Arthas                          | -1 - Players cannot gain reputation with this faction |
| 2078 | 1109                | CoT Stratholme Citizen              | -1 - Players cannot gain reputation with this faction |
| 2079 | 1108                | CoT Arthas                          | -1 - Players cannot gain reputation with this faction |
| 2080 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 2081 | 1111                | Freya                               | -1 - Players cannot gain reputation with this faction |
| 2082 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 2083 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 2084 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 2085 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 2086 | 529                 | Argent Dawn                         | 13 - Argent Dawn                                      |
| 2087 | 529                 | Argent Dawn                         | 13 - Argent Dawn                                      |
| 2088 | 960                 | Actor Evil                          | -1 - Players cannot gain reputation with this faction |
| 2089 | 56                  | Scarlet Crusade                     | -1 - Players cannot gain reputation with this faction |
| 2090 | 1112                | Mount - Taxi - Alliance             | -1 - Players cannot gain reputation with this faction |
| 2091 | 1113                | Mount - Taxi - Horde                | -1 - Players cannot gain reputation with this faction |
| 2092 | 1114                | Mount - Taxi - Neutral              | -1 - Players cannot gain reputation with this faction |
| 2093 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 2094 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 2095 | 56                  | Scarlet Crusade                     | -1 - Players cannot gain reputation with this faction |
| 2096 | 56                  | Scarlet Crusade                     | -1 - Players cannot gain reputation with this faction |
| 2097 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 2098 | 1116                | Elemental, Air                      | -1 - Players cannot gain reputation with this faction |
| 2099 | 1115                | Elemental, Water                    | -1 - Players cannot gain reputation with this faction |
| 2100 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 2101 | 960                 | Actor Evil                          | -1 - Players cannot gain reputation with this faction |
| 2102 | 960                 | Actor Evil                          | -1 - Players cannot gain reputation with this faction |
| 2103 | 56                  | Scarlet Crusade                     | -1 - Players cannot gain reputation with this faction |
| 2104 | 965                 | Monster Spar                        | -1 - Players cannot gain reputation with this faction |
| 2105 | 966                 | Monster Spar Buddy                  | -1 - Players cannot gain reputation with this faction |
| 2106 | 148                 | Ambient                             | -1 - Players cannot gain reputation with this faction |
| 2107 | 1119                | The Sons of Hodir                   | 97 - The Sons of Hodir                                |
| 2108 | 1120                | Iron Giants                         | -1 - Players cannot gain reputation with this faction |
| 2109 | 1121                | Frost Vrykul                        | -1 - Players cannot gain reputation with this faction |
| 2110 | 31                  | Friendly                            | -1 - Players cannot gain reputation with this faction |
| 2111 | 14                  | Monster                             | -1 - Players cannot gain reputation with this faction |
| 2112 | 1119                | The Sons of Hodir                   | 97 - The Sons of Hodir                                |
| 2113 | 1121                | Frost Vrykul                        | -1 - Players cannot gain reputation with this faction |
| 2114 | 1045                | Vrykul                              | -1 - Players cannot gain reputation with this faction |
| 2115 | 959                 | Actor Good                          | -1 - Players cannot gain reputation with this faction |
| 2116 | 1045                | Vrykul                              | -1 - Players cannot gain reputation with this faction |
| 2117 | 959                 | Actor Good                          | -1 - Players cannot gain reputation with this faction |
| 2118 | 1122                | Earthen                             | -1 - Players cannot gain reputation with this faction |
| 2119 | 1123                | Monster Referee                     | -1 - Players cannot gain reputation with this faction |
| 2120 | 1123                | Monster Referee                     | -1 - Players cannot gain reputation with this faction |
| 2121 | 1124                | The Sunreavers                      | 98 - The Sunreavers                                   |
| 2122 | 1124                | The Sunreavers                      | 98 - The Sunreavers                                   |
| 2123 | 1124                | The Sunreavers                      | 98 - The Sunreavers                                   |
| 2124 | 14                  | Monster                             | -1 - Players cannot gain reputation with this faction |
| 2125 | 1121                | Frost Vrykul                        | -1 - Players cannot gain reputation with this faction |
| 2126 | 1121                | Frost Vrykul                        | -1 - Players cannot gain reputation with this faction |
| 2127 | 148                 | Ambient                             | -1 - Players cannot gain reputation with this faction |
| 2128 | 1125                | Hyldsmeet                           | -1 - Players cannot gain reputation with this faction |
| 2129 | 1124                | The Sunreavers                      | 98 - The Sunreavers                                   |
| 2130 | 1094                | The Silver Covenant                 | 90 - The Silver Covenant                              |
| 2131 | 1106                | Argent Crusade                      | 94 - Argent Crusade                                   |
| 2132 | 1085                | Warsong Offensive                   | 81 - Warsong Offensive                                |
| 2133 | 1121                | Frost Vrykul                        | -1 - Players cannot gain reputation with this faction |
| 2134 | 1106                | Argent Crusade                      | 94 - Argent Crusade                                   |
| 2135 | 31                  | Friendly                            | -1 - Players cannot gain reputation with this faction |
| 2136 | 148                 | Ambient                             | -1 - Players cannot gain reputation with this faction |
| 2137 | 31                  | Friendly                            | -1 - Players cannot gain reputation with this faction |
| 2138 | 1106                | Argent Crusade                      | 94 - Argent Crusade                                   |
| 2139 | 928                 | Scourge Invaders                    | -1 - Players cannot gain reputation with this faction |
| 2140 | 31                  | Friendly                            | -1 - Players cannot gain reputation with this faction |
| 2141 | 31                  | Friendly                            | -1 - Players cannot gain reputation with this faction |
| 2142 | 469                 | Alliance                            | 11 - Alliance                                         |
| 2143 | 1050                | Valiance Expedition                 | 74 - Valiance Expedition                              |
| 2144 | 1098                | Knights of the Ebon Blade           | 91 - Knights of the Ebon Blade                        |
| 2145 | 928                 | Scourge Invaders                    | -1 - Players cannot gain reputation with this faction |
| 2148 | 1073                | The Kalu\'ak                        | 79 - The Kalu\'ak                                     |
| 2150 | 966                 | Monster Spar Buddy                  | -1 - Players cannot gain reputation with this faction |
| 2155 | 47                  | Ironforge                           | 20 - Ironforge                                        |
| 2156 | 973                 | Monster, Predator                   | -1 - Players cannot gain reputation with this faction |
| 2176 | 959                 | Actor Good                          | -1 - Players cannot gain reputation with this faction |
| 2178 | 959                 | Actor Good                          | -1 - Players cannot gain reputation with this faction |
| 2189 | 1145                | Hates Everything                    | -1 - Players cannot gain reputation with this faction |
| 2190 | 1145                | Hates Everything                    | -1 - Players cannot gain reputation with this faction |
| 2191 | 1145                | Hates Everything                    | -1 - Players cannot gain reputation with this faction |
| 2209 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 2210 | 911                 | Silvermoon City                     | 55 - Silvermoon City                                  |
| 2212 | 20                  | Undead, Scourge                     | -1 - Players cannot gain reputation with this faction |
| 2214 | 1098                | Knights of the Ebon Blade           | 91 - Knights of the Ebon Blade                        |
| 2216 | 1156                | The Ashen Verdict                   | 104 - The Ashen Verdict                               |
| 2217 | 1156                | The Ashen Verdict                   | 104 - The Ashen Verdict                               |
| 2218 | 1156                | The Ashen Verdict                   | 104 - The Ashen Verdict                               |
| 2219 | 1156                | The Ashen Verdict                   | 104 - The Ashen Verdict                               |
| 2226 | 1098                | Knights of the Ebon Blade           | 91 - Knights of the Ebon Blade                        |
| 2230 | 1106                | Argent Crusade                      | 94 - Argent Crusade                                   |
| 2235 | 1160                | CTF - Flag - Horde 2                | -1 - Players cannot gain reputation with this faction |
| 2236 | 1159                | CTF - Flag - Alliance 2             | -1 - Players cannot gain reputation with this faction |

</details>

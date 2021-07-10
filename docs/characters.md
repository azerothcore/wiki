# characters 

[<-Back-to:Characters](database-characters.md)

**The \`characters\` table**

This table holds vital static information for each character. It is used to create the player objects in-game.

## Structure

| Field                      | Type         | Attributes | Key | Null | Default           | Extra  | Comment                  |
|----------------------------|--------------|------------|-----|------|-------------------|--------|--------------------------|
| [guid][1]                  | INT          | UNSIGNED   | PRI | NO   | 0                 | Unique | Global Unique Identifier |
| [account][2]               | INT          | UNSIGNED   |     | NO   | 0                 |        | Account Identifier       |
| [name][3]                  | VARCHAR(12)  | SIGNED     |     | NO   |                   |        |                          |
| [race][4]                  | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [class][5]                 | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [gender][6]                | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [level][7]                 | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [xp][8]                    | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [money][9]                 | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [skin][10]                 | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [face][11]                 | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [hairStyle][12]            | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [hairColor][13]            | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [facialStyle][14]          | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [bankSlots][15]            | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [restState][16]            | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [playerflags][17]          | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [position_x][18]           | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [position_y][19]           | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [position_z][20]           | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [map][21]                  | SMALLINT     | UNSIGNED   |     | NO   | 0                 |        | Map Identifier           |
| [instance_id][22]          | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [instance_mode_mask][23]   | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [orientation][24]          | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [taximask][25]             | TEXT         | SIGNED     |     | NO   |                   |        |                          |
| [online][26]               | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [cinematic][27]            | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [totaltime][28]            | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [leveltime][29]            | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [logout_time][30]          | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [is_logout_resting][31]    | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [rest_bonus][32]           | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [resettalents_cost][33]    | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [resettalents_time][34]    | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [trans_x][35]              | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [trans_y][36]              | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [trans_z][37]              | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [trans_o][38]              | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [transguid][39]            | MEDIUMINT    | SIGNED     |     | NO   | 0                 |        |                          |
| [extra_flags][40]          | SMALLINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [stable_slots][41]         | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [at_login][42]             | SMALLINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [zone][43]                 | SMALLINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [death_expire_time][44]    | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [taxi_path][45]            | TEXT         | SIGNED     |     | YES  |                   |        |                          |
| [arenaPoints][46]          | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [totalHonorPoints][47]     | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [todayHonorPoints][48]     | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [yesterdayHonorPoints][49] | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [totalKills][50]           | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [todayKills][51]           | SMALLINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [yesterdayKills][52]       | SMALLINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [chosenTitle][53]          | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [knownCurrencies][54]      | BIGINT       | UNSIGNED   |     | NO   | 0                 |        |                          |
| [watchedFaction][55]       | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [drunk][56]                | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [health][57]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power1][58]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power2][59]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power3][60]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power4][61]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power5][62]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power6][63]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power7][64]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [latency][65]              | MEDIUMINT    | UNSIGNED   |     | NO   | 0                 |        |                          |
| [talentGroupsCount][66]    | TINYINT      | UNSIGNED   |     | NO   | 1                 |        |                          |
| [activeTalentGroup][67]    | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [exploredZones][68]        | LONGTEXT     | SIGNED     |     | YES  |                   |        |                          |
| [equipmentCache][69]       | LONGTEXT     | SIGNED     |     | YES  |                   |        |                          |
| [ammoId][70]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [knownTitles][71]          | LONGTEXT     | SIGNED     |     | YES  |                   |        |                          |
| [actionBars][72]           | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [grantableLevels][73]      | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [order][74]                | TINYINT      | SIGNED     |     | YES  |                   |        |                          |
| [creation_date][75]        | TIMESTAMP    | SIGNED     |     | NO   | CURRENT_TIMESTAMP |        |                          |
| [deleteInfos_Account][76]  | INT          | UNSIGNED   |     | YES  |                   |        |                          |
| [deleteInfos_Name][77]     | VARCHAR(12)  | SIGNED     |     | YES  |                   |        |                          |
| [deleteDate][78]           | INT          | UNSIGNED   |     | YES  |                   |        |                          |
  
[1]: #guid
[2]: #account
[3]: #name
[4]: #race
[5]: #class
[6]: #gender
[7]: #level
[8]: #xp
[9]: #money
[10]: #skin
[11]: #face
[12]: #hairstyle
[13]: #haircolor
[14]: #facialstyle
[15]: #bankslots
[16]: #reststate
[17]: #playerflags
[18]: #position_x
[19]: #position_y
[20]: #position_z
[21]: #map
[22]: #instance_id
[23]: #instance_mode_mask
[24]: #orientation
[25]: #taximask
[26]: #online
[27]: #cinematic
[28]: #totaltime
[29]: #leveltime
[30]: #logout_time
[31]: #is_logout_resting
[32]: #rest_bonus
[33]: #resettalents_cost
[34]: #resettalents_time
[35]: #trans_x
[36]: #trans_y
[37]: #trans_z
[38]: #trans_o
[39]: #transguid
[40]: #extra_flags
[41]: #stable_slots
[42]: #at_login
[43]: #zone
[44]: #death_expire_time
[45]: #taxi_path
[46]: #arenaPoints
[47]: #totalhonorpoints
[48]: #todayhonorpoints
[49]: #yesterdayhonorpoints
[50]: #totalkills
[51]: #todaykills
[52]: #yesterdayKills
[53]: #chosentitle
[54]: #knowncurrencies
[55]: #watchedfaction
[56]: #drunk
[57]: #health
[58]: #power
[59]: #power
[60]: #power
[61]: #power
[62]: #power
[63]: #power
[64]: #power
[65]: #latency
[66]: #talentgroupscount
[67]: #activetalentgroup
[68]: #exploredzones
[69]: #equipmentcache
[70]: #ammoid
[71]: #knownTitles
[72]: #actionbars
[73]: #grantablelevels
[74]: #order
[75]: #creation_date
[76]: #deleteinfos_account
[77]: #deleteinfos_name
[78]: #deletedate

**Description of the fields**

### guid

The character global unique identifier. This number must be unique and is the best way to identify separate characters.

### account

The account ID in which this character resides. See [account.id](account#id). in the auth database.

### name

The name of the character. Max length is 12 characters.

### race

The race of the character. See [ChrRaces.dbc](chrraces).

### class

The class of the character: [ChrClasses.dbc](chrclasses).

### gender

The gender of the character.

| Id | Gender      |
| -- | ---         |
| 0  | Male        |
| 1  | Female      |
| 2  | Unknown (?) |

`2` is seen in table [`creature_model_info`](creature_model_info) notably.

### level

The level of the character.

### xp

The amount of experience this character has earned towards the next level.

### money

The amount of copper this character has.

### skin

Contains data about the skincolor of the character.
skinColor = playerbytes  % 256

### face

Contains data about the facestyle of the character.
faceStyle = (playerbytes &gt;&gt; 8) % 256

### hairStyle

Contains data about the hairStyle of the character.
hairStyle = (playerbytes &gt;&gt; 16) % 256

### hairColor

Contains data about the haircolor of the character.
hairColor = (playerbytes &gt;&gt; 24) % 256

### facialStyle

Contains data about facial hair of the character.
facialHair = playerBytes2 % 256

### bankSlots

`field-no-description|15`

### restState

`field-no-description|16`

### playerFlags

A bitmask that represents what Player flags the player has. Each bit controls a different flag and to combine flags, you can add each flag that you want, in effect activating the respective bits.

| Flag     |            | Name                          | Comment                                                                           |
|----------|------------|-------------------------------|-----------------------------------------------------------------------------------|
| 1        | 0x00000001 | PLAYER_FLAGS_GROUP_LEADER     |                                                                                   |
| 2        | 0x00000002 | PLAYER_FLAGS_AFK              |                                                                                   |
| 4        | 0x00000004 | PLAYER_FLAGS_DND              |                                                                                   |
| 8        | 0x00000008 | PLAYER_FLAGS_GM               |                                                                                   |
| 16       | 0x00000010 | PLAYER_FLAGS_GHOST            |                                                                                   |
| 32       | 0x00000020 | PLAYER_FLAGS_RESTING          |                                                                                   |
| 64       | 0x00000040 | PLAYER_FLAGS_UNK7             |                                                                                   |
| 128      | 0x00000080 | PLAYER_FLAGS_UNK8             | pre-3.0.3 PLAYER_FLAGS_FFA_PVP flag for FFA PVP state                             |
| 256      | 0x00000100 | PLAYER_FLAGS_CONTESTED_PVP    | Player has been involved in a PvP combat and will be attacked by contested guards |
| 512      | 0x00000200 | PLAYER_FLAGS_IN_PVP           |                                                                                   |
| 1024     | 0x00000400 | PLAYER_FLAGS_HIDE_HELM        |                                                                                   |
| 2048     | 0x00000800 | PLAYER_FLAGS_HIDE_CLOAK       |                                                                                   |
| 4096     | 0x00001000 | PLAYER_FLAGS_PLAYED_LONG_TIME | played long time                                                                  |
| 8192     | 0x00002000 | PLAYER_FLAGS_TOO_LONG         | played too long time                                                              |
| 16384    | 0x00004000 | PLAYER_FLAGS_IS_OUT_OF_BOUNDS |                                                                                   |
| 32768    | 0x00008000 | PLAYER_FLAGS_DEVELOPER        | prefix for something?                                                             |
| 65536    | 0x00010000 | PLAYER_FLAGS_UNK17            | pre-3.0.3 PLAYER_FLAGS_SANCTUARY flag for player entered sanctuary                |
| 131072   | 0x00020000 | PLAYER_FLAGS_TAXI_BENCHMARK   | taxi benchmark mode (on/off) (2.0.1)                                              |
| 262144   | 0x00040000 | PLAYER_FLAGS_PVP_TIMER        | 3.0.2, pvp timer active (after you disable pvp manually)                          |
| 524288   | 0x00080000 | PLAYER_FLAGS_UNK20            |                                                                                   |
| 1048576  | 0x00100000 | PLAYER_FLAGS_UNK21            |                                                                                   |
| 2097152  | 0x00200000 | PLAYER_FLAGS_UNK22            |                                                                                   |
| 4194304  | 0x00400000 | PLAYER_FLAGS_COMMENTATOR2     |                                                                                   |
| 8388608  | 0x00800000 | PLAYER_ALLOW_ONLY_ABILITY     | used by bladestorm and killing spree                                              |
| 16777216 | 0x01000000 | PLAYER_FLAGS_UNK25            | disabled all melee ability on tab include autoattack                              |
| 33554432 | 0x02000000 | PLAYER_FLAGS_NO_XP_GAIN       |                                                                                   |


### position_x

The x position of the character's location.

### position_y

The y position of the character's location.

### position_z

The z position of the character's location.

### map

The map ID the character is in.

### instance_id

The instance ID the character is currently in and bound to

### instance_mode_mask

The current dungeon difficulty that the player is in. This field is bitmask. Values are put together, however, only two of four should be used at once. This description may not be 100% correct.

| Flag | Comment |
|------|---------|
| 0    | Normal  |
| 1    | Heroic  |
| 16   | 10 man  |
| 32   | 25 man  |

### orientation

The orientation the character is facing. (North = 0.0, South = 3.14159)

### taximask

Known taxi nodes separated with space

### online

Records whether the character is online (1) or offline (0).

### cinematic

Boolean 1 or 0 controlling whether the start cinematic has been shown or not.

### totaltime

The total time that the character has been active in the world, measured in seconds.

### leveltime

The total time the character has spent in the world at the current level, measured in seconds.

### logout_time

The time when the character last logged out, measured in Unix time.

### is_logout_resting

Boolean 1 or 0 controlling if the character is currently in a resting zone or not.

### rest_bonus

The cumulated bonus of rested rate for gaining experience.

### resettalents_cost

The cost for the character to reset its talents, measured in copper.

### resettalents_time

`field-no-description|34`

### trans_x

The x position of the transport this character was on when they were last saved.

### trans_y

The y position of the transport this character was on when they were last saved.

### trans_z

The z position of the transport this character was on when they were last saved.

### trans_o

The orientation of the transport this character was on when they were last saved.

### transguid

The global unique identifier of the transport this character was on when they were last saved.

### extra_flags

These flags control certain player specific attributes, mostly GM features.

| Flag |            | Name                           | Description                                         |
|------|------------|--------------------------------|-----------------------------------------------------|
| 1    | 0x00000001 | PLAYER_EXTRA_GM_ON             | Defines GM state                                    |
| 2    | 0x00000002 | PLAYER_EXTRA_GM_ACCEPT_TICKETS | NO LONGER USED Defines if tickets are accepted      |
| 4    | 0x00000004 | PLAYER_EXTRA_ACCEPT_WHISPERS   | Defines if whispers are accepted                    |
| 8    | 0x00000008 | PLAYER_EXTRA_TAXICHEAT         | Sets taxicheat                                      |
| 16   | 0x00000010 | PLAYER_EXTRA_GM_INVISIBLE      | Defines GM visibility                               |
| 32   | 0x00000020 | PLAYER_EXTRA_GM_CHAT           | Show GM badge in chat messages                      |
| 64   | 0x00000040 | PLAYER_EXTRA_HAS_310_FLYER     | Marks if player already has 310% speed flying mount |
| 256  | 0x00000100 | PLAYER_EXTRA_PVP_DEATH         | Store PvP death status until corpse creating        |

### stable_slots

The Stable Slots available (bought) at the Stable Master.

### at_login

This field is a bitmask controlling different actions taken once a player logs in with the character.

| Flag |      | Name                       | Description                          |
|------|------|----------------------------|--------------------------------------|
| 1    | 0x01 | AT_LOGIN_RENAME            | Force character to change name       |
| 2    | 0x02 | AT_LOGIN_RESET_SPELLS      | Reset spells (professions as well)   |
| 4    | 0x04 | AT_LOGIN_RESET_TALENTS     | Reset talents                        |
| 8    | 0x08 | AT_LOGIN_CUSTOMIZE         | Customize Characters                 |
| 16   | 0x10 | AT_LOGIN_RESET_PET_TALENTS | Reset pet talents                    |
| 32   | 0x20 | AT_LOGIN_FIRST             | Set at and removed after first login |
| 64   | 0x40 | AT_LOGIN_CHANGE_FACTION    | Faction change                       |
| 128  | 0x80 | AT_LOGIN_CHANGE_RACE       | Race change                          |

For multiple actions, add values together.

### zone

The zone ID the character is in.

### death_expire_time

Time when a character can be resurrected in case of a server crash or client exit while in ghost form, measured in Unix time.

### taxi_path

Stores the players current taxi path ([TaxiPath.dbc](TaxiPath)) if logged off while on one.

### arenaPoints

The amount of arena points this character has stored up, and will receive next time arena points are distributed.

### totalHonorPoints

The amount of honor points this character has got.

### todayHonorPoints

The amount of honor points this character has gotten today.

### yesterdayHonorPoints

The amount of honor points this character got yesterday.

### totalKills

The amount of players this character has killed.

### todayKills

The amount of players this character has killed today.

### yesterdayKills

The amount of players this character killed yesterday.

### chosenTitle

Current title, using the bit_index field (InGameOrder in [CharTitles.dbc](CharTitles)).

### knownCurrencies

Known currencies (what to be listed in the Currency tab), bitmask of BitIndexes, see [CurrencyTypes.dbc](CurrencyTypes)

### watchedFaction

Tracked faction at experience bar (using reputation ID, see [Faction.dbc](faction))

### drunk

Character's drunk state, 0-100

-   0 = Sober
-   1-49 = Tipsy
-   50-89 = Drunk
-   90-100 = Smashed

### health

The characters current health.

### power

Current character powers (snapshot from when the character was saved).

| Field  | Power name  |
|--------|-------------|
| power1 | Mana        |
| power2 | Rage        |
| power3 | Focus       |
| power4 | Energy      |
| power5 | Happiness   |
| power6 | Runes       |
| power7 | Runic Power |

### latency

This characters latency, or ping, in milliseconds, as of the last update.

### talentGroupsCount

The number of specs this character has access to. Default value is 1. Maximum currently supported value is 2. Should never be 0 (this is a sign of a character created before the dual spec system).

### activeTalentGroup

The currently activated spec for this character, spec = 0 is the first spec, spec = 1 is the second spec.

### exploredZones

Bitmasks of explored zones (1 bit for explored, 0 bit for unexplored).

### equipmentCache

Character's equipment and bag cache. 

### ammoId

[Template ID](item_template#entry) of the ammo item.

### knownTitles

Contains data about known Titles stored in 6 x 16bit integers. To calculate where a knownTitle is in one of those 6 integers you do the following: We select one of the titles from [CharTitles.dbc](CharTitles), take Archmage title for example:

| TitleID | UnkRef? | MaleTitle   | FemaleTitle | InGameOrder |
|---------|---------|-------------|-------------|-------------|
| 93      | 0       | Archmage %s | Archmage %s | 61          |

We use the InGameOrder to calculate in which one of the 6 (16bit) integer is the title stored:

```
InGameOrder / 32 = X
61 / 32 = **1,90625** (1 - Do **NOT** round the value!)
```

so the 1st integer stores the title. Because counting starts from **0** to 5, it would be "0 **TITLE_BIT** 0 0 0 0".

Now which bit stores the title? We use modulo to calculate this.

```
InGameOrder Modulo 32 = X
61 Mod 32 = **29**
```
so the 29bit stores the title. This would be 2 ^ 29 = 536870912. This bit stores the Archmage title. This would mean if you **only** have the Archmage title, characters.knownTitles would be "0 536870912 0 0 0 0".

### actionBars

A bitmask that contains visible actionbars for the player.

| Flag |            | Comment          |
|------|------------|------------------|
| 1    | 0x00000001 | Bottom Left Bar  |
| 2    | 0x00000002 | Bottom Right Bar |
| 4    | 0x00000004 | Rigth Bar        |
| 8    | 0x00000008 | Right Bar 2      |

### grantableLevels

Recruit A Friend stuff.

### order

`field-no-description|74`

### creation_date

Character's creation date and time. Format YYY-MM-DD HH:MM:SS according to server's time.

### deleteInfos_Account

Stores the account id if the character is deleted and CharDelete.Method in worldserver.conf is set to 1.

### deleteInfos_Name

Stores the name of character if the character is deleted and CharDelete.Method in worldserver.conf is set to 1.

### deleteDate

Stores the date when the character was deleted and CharDelete.Method in worldserver.conf is set to 1. Will be checked by worldserver against CharDelete.KeepDays in worldserver.conf. If this value is lower than deleteDate + CharDelete.KeepDays the character will be purged.

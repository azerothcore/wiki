# characters

[<-Back-to:Characters](database-characters)

**The \`characters\` table**

This table holds vital static information for each character. It is used to create the player objects in-game.

**Table: characters's Structure**

| Field                                           | Type        |          | Null | Key | Default           | Extra | Comment                  |
| :---------------------------------------------- | :---------- | :------- | :--: | :-: | :---------------: | :---: | :----------------------- |
| [guid](#guid)                                   | INT         | UNSIGNED | NO   | PRI | 0                 |       | Global Unique Identifier |
| [account](#account)                             | INT         | UNSIGNED | NO   | MUL | 0                 |       | Account Identifier       |
| [name](#name)                                   | VARCHAR(12) |          | NO   | MUL |                   |       |                          |
| [race](#race)                                   | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [class](#class)                                 | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [gender](#gender)                               | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [level](#level)                                 | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [xp](#xp)                                       | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [money](#money)                                 | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [skin](#skin)                                   | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [face](#face)                                   | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [hairStyle](#hairstyle)                         | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [hairColor](#haircolor)                         | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [facialStyle](#facialstyle)                     | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [bankSlots](#bankslots)                         | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [restState](#reststate)                         | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [playerFlags](#playerflags)                     | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [position_x](#positionx)                        | FLOAT       |          | NO   |     | 0                 |       |                          |
| [position_y](#positiony)                        | FLOAT       |          | NO   |     | 0                 |       |                          |
| [position_z](#positionz)                        | FLOAT       |          | NO   |     | 0                 |       |                          |
| [map](#map)                                     | SMALLINT    | UNSIGNED | NO   |     | 0                 |       | Map Identifier           |
| [instance_id](#instanceid)                      | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [instance_mode_mask](#instancemodemask)         | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [orientation](#orientation)                     | FLOAT       |          | NO   |     | 0                 |       |                          |
| [taximask](#taximask)                           | TEXT        |          | NO   |     |                   |       |                          |
| [online](#online)                               | TINYINT     | UNSIGNED | NO   | MUL | 0                 |       |                          |
| [cinematic](#cinematic)                         | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [totaltime](#totaltime)                         | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [leveltime](#leveltime)                         | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [logout_time](#logouttime)                      | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [is_logout_resting](#islogoutresting)           | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [rest_bonus](#restbonus)                        | FLOAT       |          | NO   |     | 0                 |       |                          |
| [resettalents_cost](#resettalentscost)          | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [resettalents_time](#resettalentstime)          | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [trans_x](#transx)                              | FLOAT       |          | NO   |     | 0                 |       |                          |
| [trans_y](#transy)                              | FLOAT       |          | NO   |     | 0                 |       |                          |
| [trans_z](#transz)                              | FLOAT       |          | NO   |     | 0                 |       |                          |
| [trans_o](#transo)                              | FLOAT       |          | NO   |     | 0                 |       |                          |
| [transguid](#transguid)                         | INT         |          | YES  |     | 0                 |       |                          |
| [extra_flags](#extraflags)                      | SMALLINT    | UNSIGNED | NO   |     | 0                 |       |                          |
| [stable_slots](#stableslots)                    | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [at_login](#atlogin)                            | SMALLINT    | UNSIGNED | NO   |     | 0                 |       |                          |
| [zone](#zone)                                   | SMALLINT    | UNSIGNED | NO   |     | 0                 |       |                          |
| [death_expire_time](#deathexpiretime)           | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [taxi_path](#taxipath)                          | TEXT        |          | YES  |     | NULL              |       |                          |
| [arenaPoints](#arenapoints)                     | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [totalHonorPoints](#totalhonorpoints)           | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [todayHonorPoints](#todayhonorpoints)           | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [yesterdayHonorPoints](#yesterdayhonorpoints)   | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [totalKills](#totalkills)                       | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [todayKills](#todaykills)                       | SMALLINT    | UNSIGNED | NO   |     | 0                 |       |                          |
| [yesterdayKills](#yesterdaykills)               | SMALLINT    | UNSIGNED | NO   |     | 0                 |       |                          |
| [chosenTitle](#chosentitle)                     | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [knownCurrencies](#knowncurrencies)             | BIGINT      | UNSIGNED | NO   |     | 0                 |       |                          |
| [watchedFaction](#watchedfaction)               | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [drunk](#drunk)                                 | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [health](#health)                               | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [power1](#power)                                | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [power2](#power)                                | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [power3](#power)                                | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [power4](#power)                                | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [power5](#power)                                | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [power6](#power)                                | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [power7](#power)                                | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [latency](#latency)                             | INT         | UNSIGNED | YES  |     | 0                 |       |                          |
| [talentGroupsCount](#talentgroupscount)         | TINYINT     | UNSIGNED | NO   |     | 1                 |       |                          |
| [activeTalentGroup](#activetalentgroup)         | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [exploredZones](#exploredzones)                 | LONGTEXT    |          | YES  |     | NULL              |       |                          |
| [equipmentCache](#equipmentcache)               | LONGTEXT    |          | YES  |     | NULL              |       |                          |
| [ammoId](#ammoid)                               | INT         | UNSIGNED | NO   |     | 0                 |       |                          |
| [knownTitles](#knowntitles)                     | LONGTEXT    |          | YES  |     | NULL              |       |                          |
| [actionBars](#actionbars)                       | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [grantableLevels](#grantablelevels)             | TINYINT     | UNSIGNED | NO   |     | 0                 |       |                          |
| [order](#order)                                 | TINYINT     |          | YES  |     | NULL              |       |                          |
| [creation_date](#creationdate)                  | TIMESTAMP   |          | NO   |     | CURRENT_TIMESTAMP |       |                          |
| [deleteInfos_Account](#deleteinfosaccount)      | INT         | UNSIGNED | YES  |     | NULL              |       |                          |
| [deleteInfos_Name](#deleteinfosname)            | VARCHAR(12) |          | YES  |     | NULL              |       |                          |
| [deleteDate](#deletedate)                       | INT         | UNSIGNED | YES  |     | NULL              |       |                          |
| [innTriggerId](#inntriggerid)                   | INT         | UNSIGNED | NO   |     |                   |       |                          |
| [extraBonusTalentCount](#extrabonustalentcount) | INT         |          | NO   |     | 0                 |       |                          |
  

**Description of the table's fields**

### guid

The character global unique identifier. This number must be unique and is the best way to identify separate characters.

### account

The account ID in which this character resides. See [account.id](account#id) in the auth database.

### name

The name of the character. Max length is 12 characters.

### race

The race of the character. See [ChrRaces.dbc](chrraces).

### class

The class of the character: [ChrClasses.dbc](chrclasses).

### gender

The gender of the character.

| Id  | Gender      |
| --- | ----------- |
| 0   | Male        |
| 1   | Female      |
| 2   | Unknown (?) |

`2` is seen in table [creature\_model\_info](creature_model_info) notably.

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

Number of bank bag slots the character has bought.

### restState

| Value | State                                    |
| ----- | ---------------------------------------- |
| 1     | Rested                                   |
| 2     | Normal, not linked with Recruit-a-Friend |
| 3     | Tired                                    |
| 4     | Tired, 50% experience                    |
| 5     | Exhausted, 25% experience                |
| 6     | Linked with Recruit-a-Friend             |

### playerFlags

A bitmask that represents what Player flags the player has. Each bit controls a different flag and to combine flags, you can add each flag that you want, in effect activating the respective bits.

| Value    | Hex          | Flag                           | Comment                                                                                                                                                                                                                                                                        |
| :------- | :----------: | :----------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | `0x00000001` | PLAYER_FLAGS_GROUP_LEADER      | The player is the leader of a group                                                                                                                                                                                                                                            |
| 2        | `0x00000002` | PLAYER_FLAGS_AFK               | The player is away (AFK)                                                                                                                                                                                                                                                       |
| 4        | `0x00000004` | PLAYER_FLAGS_DND               | The player is in Do Not Disturb mode                                                                                                                                                                                                                                           |
| 8        | `0x00000008` | PLAYER_FLAGS_GM                | GM mode is on, the player shows the GM tag                                                                                                                                                                                                                                     |
| 16       | `0x00000010` | PLAYER_FLAGS_GHOST             | The player is a ghost                                                                                                                                                                                                                                                          |
| 32       | `0x00000020` | PLAYER_FLAGS_RESTING           | The player is resting (in an inn or a city)                                                                                                                                                                                                                                    |
| 64       | `0x00000040` | PLAYER_FLAGS_UNK6              | Not used by the core. [TrinityCore](https://github.com/TrinityCore/TrinityCore/blob/3.3.5/src/server/game/Entities/Player/Player.h) names it PLAYER_FLAGS_VOICE_CHAT, [mangos](https://github.com/mangostwo/server/blob/master/src/game/Object/Player.h) guesses an admin flag |
| 128      | `0x00000080` | PLAYER_FLAGS_UNK7              | pre-3.0.3 PLAYER_FLAGS_FFA_PVP flag for FFA PVP state                                                                                                                                                                                                                          |
| 256      | `0x00000100` | PLAYER_FLAGS_CONTESTED_PVP     | Player has been involved in a PvP combat and will be attacked by contested guards                                                                                                                                                                                              |
| 512      | `0x00000200` | PLAYER_FLAGS_IN_PVP            | The player is flagged for PvP. [cmangos](https://github.com/cmangos/mangos-wotlk/blob/master/src/game/Entities/Player.h) names it PLAYER_FLAGS_PVP_DESIRED, the PvP choice of the player                                                                                       |
| 1024     | `0x00000400` | PLAYER_FLAGS_HIDE_HELM         | The helm is hidden                                                                                                                                                                                                                                                             |
| 2048     | `0x00000800` | PLAYER_FLAGS_HIDE_CLOAK        | The cloak is hidden                                                                                                                                                                                                                                                            |
| 4096     | `0x00001000` | PLAYER_FLAGS_PARTIAL_PLAY_TIME | played long time                                                                                                                                                                                                                                                               |
| 8192     | `0x00002000` | PLAYER_FLAGS_NO_PLAY_TIME      | played too long time                                                                                                                                                                                                                                                           |
| 16384    | `0x00004000` | PLAYER_FLAGS_IS_OUT_OF_BOUNDS  | The player is outside the bounds of the map. Read by the client function IsOutOfBounds ([cmangos](https://github.com/cmangos/mangos-wotlk/blob/master/src/game/Entities/Player.h))                                                                                             |
| 32768    | `0x00008000` | PLAYER_FLAGS_DEVELOPER         | prefix for something?                                                                                                                                                                                                                                                          |
| 65536    | `0x00010000` | PLAYER_FLAGS_UNK16             | pre-3.0.3 PLAYER_FLAGS_SANCTUARY flag for player entered sanctuary                                                                                                                                                                                                             |
| 131072   | `0x00020000` | PLAYER_FLAGS_TAXI_BENCHMARK    | taxi benchmark mode (on/off) (2.0.1)                                                                                                                                                                                                                                           |
| 262144   | `0x00040000` | PLAYER_FLAGS_PVP_TIMER         | 3.0.2, pvp timer active (after you disable pvp manually)                                                                                                                                                                                                                       |
| 524288   | `0x00080000` | PLAYER_FLAGS_UBER              | The core does not let a player with this flag be attacked, like an arena spectator. [cmangos](https://github.com/cmangos/mangos-wotlk/blob/master/src/game/Entities/Player.h) names it PLAYER_FLAGS_COMMENTATOR                                                                |
| 1048576  | `0x00100000` | PLAYER_FLAGS_UNK20             | Unknown. It has no description in AzerothCore, TrinityCore, cmangos or mangos                                                                                                                                                                                                  |
| 2097152  | `0x00200000` | PLAYER_FLAGS_UNK21             | Unknown. It has no description in AzerothCore, TrinityCore, cmangos or mangos                                                                                                                                                                                                  |
| 4194304  | `0x00400000` | PLAYER_FLAGS_COMMENTATOR2      | Commentator mode, set and read by the core with SetCommentator and IsCommentator. [cmangos](https://github.com/cmangos/mangos-wotlk/blob/master/src/game/Entities/Player.h) names it PLAYER_FLAGS_COMMENTATOR_UBER                                                             |
| 8388608  | `0x00800000` | PLAYER_ALLOW_ONLY_ABILITY      | used by bladestorm and killing spree                                                                                                                                                                                                                                           |
| 16777216 | `0x01000000` | PLAYER_FLAGS_UNK24             | disabled all melee ability on tab include autoattack                                                                                                                                                                                                                           |
| 33554432 | `0x02000000` | PLAYER_FLAGS_NO_XP_GAIN        | The player turned off experience gain                                                                                                                                                                                                                                          |

### position\_x

The x position of the character's location.

### position\_y

The y position of the character's location.

### position\_z

The z position of the character's location.

### map

The map ID the character is in.

### instance\_id

The instance ID the character is currently in and bound to.

### instance\_mode\_mask

The current dungeon difficulty that the player is in. This field is bitmask. Values are put together, however, only two of four should be used at once. This description may not be 100% correct.

| Value | Hex    | Flag   | Comment |
| :---- | :----: | :----- | :------ |
| 0     | `0x00` | Normal |         |
| 1     | `0x01` | Heroic |         |
| 16    | `0x10` | 10 man |         |
| 32    | `0x20` | 25 man |         |

### orientation

The orientation the character is facing. (North = 0.0, South = 3.14159)

### taximask

Known taxi nodes separated with space.

### online

Records whether the character is online (1) or offline (0).

### cinematic

Boolean 1 or 0 controlling whether the start cinematic has been shown or not.

### totaltime

The total time that the character has been active in the world, measured in seconds.

### leveltime

The total time the character has spent in the world at the current level, measured in seconds.

### logout\_time

The time when the character last logged out, measured in Unix time.

### is\_logout\_resting

Boolean 1 or 0 controlling if the character is currently in a resting zone or not.

### rest_bonus

The cumulated bonus of rested rate for gaining experience.

### resettalents\_cost

The cost for the character to reset its talents, measured in copper.

### resettalents\_time

The time the character last reset their talents, in Unix time. Used to lower the reset cost over time.

### trans\_x

The x position of the transport this character was on when they were last saved.

### trans\_y

The y position of the transport this character was on when they were last saved.

### trans\_z

The z position of the transport this character was on when they were last saved.

### trans\_o

The orientation of the transport this character was on when they were last saved.

### transguid

The global unique identifier of the transport this character was on when they were last saved.

### extra\_flags

These flags control certain player specific attributes, mostly GM features.

| Value | Hex      | Flag                               | Comment                                             |
| :---- | :------: | :--------------------------------- | :-------------------------------------------------- |
| 1     | `0x0001` | PLAYER_EXTRA_GM_ON                 | Defines GM state                                    |
| 4     | `0x0004` | PLAYER_EXTRA_ACCEPT_WHISPERS       | Defines if whispers are accepted                    |
| 8     | `0x0008` | PLAYER_EXTRA_TAXICHEAT             | Sets taxicheat                                      |
| 16    | `0x0010` | PLAYER_EXTRA_GM_INVISIBLE          | Defines GM visibility                               |
| 32    | `0x0020` | PLAYER_EXTRA_GM_CHAT               | Show GM badge in chat messages                      |
| 64    | `0x0040` | PLAYER_EXTRA_HAS_310_FLYER         | Marks if player already has 310% speed flying mount |
| 128   | `0x0080` | PLAYER_EXTRA_SPECTATOR_ON          | Marks if the player is an arena spectator           |
| 256   | `0x0100` | PLAYER_EXTRA_PVP_DEATH             | Store PvP death status until corpse creating        |
| 1024  | `0x0400` | PLAYER_EXTRA_SHOW_DK_PET           | Shows the ghoul on the character select screen      |
| 2048  | `0x0800` | PLAYER_EXTRA_GM_SPECTATOR          | GM is spectating                                    |
| 4096  | `0x1000` | PLAYER_EXTRA_DECLINE_GROUP_INVITES | The player declines all group invites               |

### stable\_slots

The Stable Slots available (bought) at the Stable Master.

### at\_login

This field is a bitmask controlling different actions taken once a player logs in with the character.

| Value | Hex    | Flag                       | Comment                              |
| :---- | :----: | :------------------------- | :----------------------------------- |
| 1     | `0x01` | AT_LOGIN_RENAME            | Force character to change name       |
| 2     | `0x02` | AT_LOGIN_RESET_SPELLS      | Reset spells (professions as well)   |
| 4     | `0x04` | AT_LOGIN_RESET_TALENTS     | Reset talents                        |
| 8     | `0x08` | AT_LOGIN_CUSTOMIZE         | Customize Characters                 |
| 16    | `0x10` | AT_LOGIN_RESET_PET_TALENTS | Reset pet talents                    |
| 32    | `0x20` | AT_LOGIN_FIRST             | Set at and removed after first login |
| 64    | `0x40` | AT_LOGIN_CHANGE_FACTION    | Faction change                       |
| 128   | `0x80` | AT_LOGIN_CHANGE_RACE       | Race change                          |

For multiple actions, add values together.

### zone

The zone ID the character is in.

### death\_expire\_time

Time when a character can be resurrected in case of a server crash or client exit while in ghost form, measured in Unix time.

### taxi\_path

Stores the players current taxi path ([TaxiPath.dbc](https://wowdev.wiki/DB/TaxiPath)) if logged off while on one.

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

Current title, using the bit_index field (InGameOrder in [CharTitles.dbc](https://wowdev.wiki/DB/CharTitles)).

### knownCurrencies

Known currencies (what to be listed in the Currency tab), bitmask of BitIndexes, see [CurrencyTypes.dbc](https://wowdev.wiki/DB/CurrencyTypes).

### watchedFaction

Tracked faction at experience bar (using reputation ID, see [Faction.dbc](faction)).

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
| ------ | ----------- |
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

Contains data about known Titles stored in 6 x 16bit integers. To calculate where a knownTitle is in one of those 6 integers you do the following: We select one of the titles from [CharTitles.dbc](https://wowdev.wiki/DB/CharTitles), take Archmage title for example:

| TitleID | UnkRef? | MaleTitle   | FemaleTitle | InGameOrder |
| ------- | ------- | ----------- | ----------- | ----------- |
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

| Value | Hex    | Flag             | Comment |
| :---- | :----: | :--------------- | :------ |
| 1     | `0x01` | Bottom Left Bar  |         |
| 2     | `0x02` | Bottom Right Bar |         |
| 4     | `0x04` | Rigth Bar        |         |
| 8     | `0x08` | Right Bar 2      |         |

### grantableLevels

Recruit A Friend stuff.

### order

A field used to change the order in which the characters appear in the character selection screen. The order field is used first, then the [characters.guid](characters#guid), which means that if the order column is NULL for every character of an account, they will be sorted by [characters.guid](characters#guid) by default.

### creation\_date

Character's creation date and time. Format YYY-MM-DD HH:MM:SS according to server's time.

### deleteInfos\_Account

Stores the account id if the character is deleted and CharDelete.Method in worldserver.conf is set to 1.

### deleteInfos\_Name

Stores the name of character if the character is deleted and CharDelete.Method in worldserver.conf is set to 1.

### deleteDate

Stores the date when the character was deleted and CharDelete.Method in [worldserver.conf.dist](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/apps/worldserver/worldserver.conf.dist) is set to 1. Will be checked by worldserver against CharDelete.KeepDays in worldserver.conf.dist. If this value is lower than deleteDate + CharDelete.KeepDays the character will be purged.

### innTriggerId

The area trigger id of the inn where the character is currently bound to rest (set when resting at an inn). `0` if not resting at an inn.

### extraBonusTalentCount

Number of extra talent points granted to the character beyond those earned from levelling.

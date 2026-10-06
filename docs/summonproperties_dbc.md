# summonproperties\_dbc

[<-Back-to:World](database-world)

See also the [Spell Effects Reference](spell-effects-reference).

**The \`summonproperties\_dbc\` table**

This DBC contains Summon Properties (EffectMiscValueB) for Spell Effect SPELL_EFFECT_SUMMON (28)

**Version is : 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)  

**Table: summonproperties\_dbc's Structure**

| Field               | Type |     | Null | Key | Default | Extra | Comment     |
| :------------------ | :--- | :-- | :--: | :-: | :-----: | :---: | :---------- |
| [ID](#id)           | INT  |     | NO   | PRI | 0       |       | Unique ID   |
| [Control](#control) | INT  |     | NO   |     | 0       |       |             |
| [Faction](#faction) | INT  |     | NO   |     | 0       |       |             |
| [Title](#title)     | INT  |     | NO   |     | 0       |       | Summon Type |
| [Slot](#slot)       | INT  |     | NO   |     | 0       |       |             |
| [Flags](#flags)     | INT  |     | NO   |     | 0       |       |             |

**Description of the table's fields**

### ID

This is the ID from SummonProperties.dbc.

### Control

| ID  | Name                                        |
| --- | ------------------------------------------- |
| 0   | None                                        |
| 1   | Guardian                                    |
| 2   | Pet                                         |
| 3   | Possessed                                   |
| 4   | Possessed Vehicle                           |
| 5   | Vehicle (Wild, but Ride Spell will be cast) |

### Faction

ID from [Faction.dbc](faction).

### Title

Also known ans summon type.

| ID  | Name      |
| --- | --------- |
| 0   | None      |
| 1   | Pet       |
| 2   | Guardian  |
| 3   | Minion    |
| 4   | Totem     |
| 5   | Mini pet  |
| 6   | Guardian2 |
| 7   | Wild2     |
| 8   | Wild3     |
| 9   | Vehicle   |
| 10  | Vehicle2  |
| 11  | Lightwell |
| 12  | Jeeves    |

### Slot 

| ID  | Name                 |
| --- | -------------------- |
| 0   | None                 |
| 1   | Totem 1              |
| 2   | Totem 2              |
| 3   | Totem 3              |
| 4   | Totem 4              |
| 5   | Critter              |
| 6   | Quest (Players Only) |

### Flags
| Value      | Hex          | Flag         | Comment                                                                |
| :--------- | :----------: | :----------- | :--------------------------------------------------------------------- |
| 1          | `0x00000001` | `0x00000001` | Attack Summoner                                                        |
| 2          | `0x00000002` | `0x00000002` | Help when Summoned in combat                                           |
| 4          | `0x00000004` | `0x00000004` | Use Level Offset                                                       |
| 8          | `0x00000008` | `0x00000008` | Despawn on Summoner Death                                              |
| 16         | `0x00000010` | `0x00000010` | Only Visible to Summoner                                               |
| 32         | `0x00000020` | `0x00000020` | Cannot Dismiss Pet                                                     |
| 64         | `0x00000040` | `0x00000040` | Use Demon Timeout                                                      |
| 128        | `0x00000080` | `0x00000080` | Unlimited Summons                                                      |
| 256        | `0x00000100` | `0x00000100` | Use Creature Level                                                     |
| 512        | `0x00000200` | `0x00000200` | Join Summoner's Spawn Group                                            |
| 1024       | `0x00000400` | `0x00000400` | Do Not Toggle                                                          |
| 2048       | `0x00000800` | `0x00000800` | Despawn When Expired                                                   |
| 4096       | `0x00001000` | `0x00001000` | Use Summoner Faction                                                   |
| 8192       | `0x00002000` | `0x00002000` | Do Not Follow Mounted Summoner                                         |
| 16384      | `0x00004000` | `0x00004000` | Save Pet Autocast                                                      |
| 32768      | `0x00008000` | `0x00008000` | Ignore Summoner's Phase (Wild Only)                                    |
| 65536      | `0x00010000` | 00x00010000  | Only Visible to Summoner's Group                                       |
| 131072     | `0x00020000` | 00x00020000  | Despawn on Summoner Logout                                             |
| 262144     | `0x00040000` | 00x00040000  | Cast Ride Vehicle Spell on Summoner                                    |
| 524288     | `0x00080000` | 00x00080000  | Guardian Acts Like a Pet                                               |
| 1048576    | `0x00100000` | 00x00100000  | Don't Snap Sessile To Ground                                           |
| 2097152    | `0x00200000` | 00x00200000  | Summons from Battle Pet Journal                                        |
| 4194304    | `0x00400000` | 00x00400000  | Unit Clutter                                                           |
| 8388608    | `0x00800000` | 00x00800000  | Default Name Color                                                     |
| 16777216   | `0x01000000` | 00x01000000  | Use Own Invisibility Detection (Ignore Owner's Invisibility Detection) |
| 33554432   | `0x02000000` | 00x02000000  | Despawn When Replaced (Totem Slots Only)                               |
| 67108864   | `0x04000000` | 00x04000000  | Despawn When Teleporting Out of Range                                  |
| 134217728  | `0x08000000` | 00x08000000  | Summoned at Group Formation Position                                   |
| 268435456  | `0x10000000` | 00x10000000  | Don't Despawn On Summoner's Death                                      |
| 536870912  | `0x20000000` | 00x20000000  | Use Title As Creature Name                                             |
| 1073741824 | `0x40000000` | 00x40000000  | Attackable By Summoner                                                 |
| 2147483648 | `0x80000000` | 00x80000000  | Don't dismiss when an encounter is aborted                             |

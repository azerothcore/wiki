# summonproperties\_dbc

[`Back-to:Spell Effects Reference`](spell-effects-reference)

[`Back-to:DBC`](dbc-index)

**The \`summonproperties\_dbc\` table**

This DBC contains Summon Properties (EffectMiscValueB) for Spell Effect SPELL_EFFECT_SUMMON (28)

**Version is : 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)  

**Table Structure**

| Field        | Type | Attributes | Key | Null | Default | Extra | Comment     |
| ------------ | ---- | ---------- | --- | ---- | ------- | ----- | ----------- |
| [ID][1]      | INT  | SIGNED     | PRI | NO   | 0       |       | Unique ID   |
| [Control][2] | INT  | SIGNED     |     | NO   | 0       |       |             |
| [Faction][3] | INT  | SIGNED     |     | NO   | 0       |       |             |
| [Title][4]   | INT  | SIGNED     |     | NO   | 0       |       | Summon Type |
| [Slot][5]    | INT  | SIGNED     |     | NO   | 0       |       |             |
| [Flags][6]   | INT  | SIGNED     |     | NO   | 0       |       |             |

[1]: #id
[2]: #control
[3]: #faction
[4]: #title
[5]: #slot
[6]: #flags

**Description of the fields**

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
| Flag       | Bit Value   | Comment                                                                |
| ---------- | ----------- | ---------------------------------------------------------------------- |
| 1          | 00x00000001 | Attack Summoner                                                        |
| 2          | 00x00000002 | Help when Summoned in combat                                           |
| 4          | 00x00000004 | Use Level Offset                                                       |
| 8          | 00x00000008 | Despawn on Summoner Death                                              |
| 16         | 00x00000010 | Only Visible to Summoner                                               |
| 32         | 00x00000020 | Cannot Dismiss Pet                                                     |
| 64         | 00x00000040 | Use Demon Timeout                                                      |
| 128        | 00x00000080 | Unlimited Summons                                                      |
| 256        | 00x00000100 | Use Creature Level                                                     |
| 512        | 00x00000200 | Join Summoner's Spawn Group                                            |
| 1024       | 00x00000400 | Do Not Toggle                                                          |
| 2048       | 00x00000800 | Despawn When Expired                                                   |
| 4096       | 00x00001000 | Use Summoner Faction                                                   |
| 8192       | 00x00002000 | Do Not Follow Mounted Summoner                                         |
| 16384      | 00x00004000 | Save Pet Autocast                                                      |
| 32768      | 00x00008000 | Ignore Summoner's Phase (Wild Only)                                    |
| 65536      | 00x00010000 | Only Visible to Summoner's Group                                       |
| 131072     | 00x00020000 | Despawn on Summoner Logout                                             |
| 262144     | 00x00040000 | Cast Ride Vehicle Spell on Summoner                                    |
| 524288     | 00x00080000 | Guardian Acts Like a Pet                                               |
| 1048576    | 00x00100000 | Don't Snap Sessile To Ground                                           |
| 2097152    | 00x00200000 | Summons from Battle Pet Journal                                        |
| 4194304    | 00x00400000 | Unit Clutter                                                           |
| 8388608    | 00x00800000 | Default Name Color                                                     |
| 16777216   | 00x01000000 | Use Own Invisibility Detection (Ignore Owner's Invisibility Detection) |
| 33554432   | 00x02000000 | Despawn When Replaced (Totem Slots Only)                               |
| 67108864   | 00x04000000 | Despawn When Teleporting Out of Range                                  |
| 134217728  | 00x08000000 | Summoned at Group Formation Position                                   |
| 268435456  | 00x10000000 | Don't Despawn On Summoner's Death                                      |
| 536870912  | 00x20000000 | Use Title As Creature Name                                             |
| 1073741824 | 00x40000000 | Attackable By Summoner                                                 |
| 2147483648 | 00x80000000 | Don't dismiss when an encounter is aborted                             |

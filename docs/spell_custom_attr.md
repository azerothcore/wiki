# spell\_custom\_attr

[<-Back-to:World](database-world)

**The \`spell\_custom\_attr\` table**

Table used for storing custom spell attributes.

**Table: spell\_custom\_attr's Structure**

| Field                     | Type |          | Null | Key | Default | Extra | Comment               |
| :------------------------ | :--- | :------- | :--: | :-: | :-----: | :---: | :-------------------- |
| [spell_id](#spellid)      | INT  | UNSIGNED | NO   | PRI | 0       |       | spell id              |
| [attributes](#attributes) | INT  | UNSIGNED | NO   |     | 0       |       | SpellCustomAttributes |

**Description of the table's fields**

### spell_id

Spell ID. See [Spell.dbc](spell_dbc) .

### attributes

Spell custom attributes from the enumeration SpellCustomAttributes in [SpellInfo.h](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Spells/SpellInfo.h)

| Value      | Hex          | Flag                                         | Comment                                                                                                                            |
| :--------- | :----------: | :------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| 1          | `0x00000001` | SPELL_ATTR0_CU_ENCHANT_PROC                  | The aura comes from a weapon enchant proc. Auras from two different items can stack, for example when dual wielding                |
| 2          | `0x00000002` | SPELL_ATTR0_CU_CONE_BACK                     | The cone points behind the caster                                                                                                  |
| 4          | `0x00000004` | SPELL_ATTR0_CU_CONE_LINE                     | The cone is a line in front of the caster                                                                                          |
| 8          | `0x00000008` | SPELL_ATTR0_CU_SHARE_DAMAGE                  | Meteor like spells (divided damage among all targets)                                                                              |
| 16         | `0x00000010` | SPELL_ATTR0_CU_NO_INITIAL_THREAT             | Casting the spell causes no threat                                                                                                 |
| 32         | `0x00000020` | SPELL_ATTR0_CU_AURA_CC                       | The aura is a crowd control effect. Set by the core at startup                                                                     |
| 64         | `0x00000040` | SPELL_ATTR0_CU_DONT_BREAK_STEALTH            | The spell does not break stealth                                                                                                   |
| 128        | `0x00000080` | SPELL_ATTR0_CU_NO_PVP_FLAG                   | Does not PvP flag                                                                                                                  |
| 256        | `0x00000100` | SPELL_ATTR0_CU_DIRECT_DAMAGE                 | The spell deals direct damage. Set by the core at startup                                                                          |
| 512        | `0x00000200` | SPELL_ATTR0_CU_IGNORE_BINARY                 | Prevents automatic binary spell classification, allowing partial resists                                                           |
| 1024       | `0x00000400` | SPELL_ATTR0_CU_PICKPOCKET                    | The spell is a pick pocket spell. A resisted cast reveals the caster                                                               |
| 2048       | `0x00000800` | SPELL_ATTR0_CU_IGNORE_EVADE                  | Do not remove the specified aura upon evading                                                                                      |
| 4096       | `0x00001000` | SPELL_ATTR0_CU_NEGATIVE_EFF0                 | Effect 0 is negative                                                                                                               |
| 8192       | `0x00002000` | SPELL_ATTR0_CU_NEGATIVE_EFF1                 | Effect 1 is negative                                                                                                               |
| 16384      | `0x00004000` | SPELL_ATTR0_CU_NEGATIVE_EFF2                 | Effect 2 is negative                                                                                                               |
| 32768      | `0x00008000` | SPELL_ATTR0_CU_IGNORE_ARMOR                  | The damage ignores armor                                                                                                           |
| 65536      | `0x00010000` | SPELL_ATTR0_CU_REQ_TARGET_FACING_CASTER      | The target must face the caster                                                                                                    |
| 131072     | `0x00020000` | SPELL_ATTR0_CU_REQ_CASTER_BEHIND_TARGET      | The caster must be behind the target                                                                                               |
| 262144     | `0x00040000` | SPELL_ATTR0_CU_ALLOW_INFLIGHT_TARGET         | The spell can be cast on a player that is on a flight path                                                                         |
| 524288     | `0x00080000` | SPELL_ATTR0_CU_NEEDS_AMMO_DATA               | The ammo is sent to the client with the cast, as for spells that use the ranged slot                                               |
| 1048576    | `0x00100000` | SPELL_ATTR0_CU_BINARY_SPELL                  | The spell is binary: it is fully resisted or not resisted at all                                                                   |
| 2097152    | `0x00200000` | SPELL_ATTR0_CU_NO_POSITIVE_TAKEN_BONUS       | Effects that raise the damage or healing taken by the target do not apply                                                          |
| 4194304    | `0x00400000` | SPELL_ATTR0_CU_SINGLE_AURA_STACK             | All sources add stacks the same aura                                                                                               |
| 8388608    | `0x00800000` | SPELL_ATTR0_CU_SCHOOLMASK_NORMAL_WITH_MAGIC  | The spell had the physical school together with a magic school. The core removes the physical school at startup and sets this flag |
| 16777216   | `0x01000000` | SPELL_ATTR0_CU_AURA_CANNOT_BE_SAVED          | The aura is never saved to the database. It cannot be used with SPELL_ATTR0_CU_FORCE_AURA_SAVING                                   |
| 33554432   | `0x02000000` | SPELL_ATTR0_CU_POSITIVE_EFF0                 | Effect 0 is positive                                                                                                               |
| 67108864   | `0x04000000` | SPELL_ATTR0_CU_POSITIVE_EFF1                 | Effect 1 is positive                                                                                                               |
| 134217728  | `0x08000000` | SPELL_ATTR0_CU_POSITIVE_EFF2                 | Effect 2 is positive                                                                                                               |
| 268435456  | `0x10000000` | SPELL_ATTR0_CU_FORCE_SEND_CATEGORY_COOLDOWNS | The category cooldown is sent to the client                                                                                        |
| 536872960  | `0x20000800` | SPELL_ATTR0_CU_FORCE_AURA_SAVING             | The aura is always saved to the database                                                                                           |
| 536870912  | `0x20000000` | SPELL_ATTR0_CU_ONLY_ONE_AREA_AURA            | Only 1 Persistent Area Aura can be active (e.g Marrowgar's coldflame)                                                              |
| 1073741824 | `0x40000000` | SPELL_ATTR0_CU_ENCOUNTER_REWARD              | Set by the core at startup on the credit spells of [instance_encounters](instance_encounters)                                      |
| 2147483648 | `0x80000000` | SPELL_ATTR0_CU_BYPASS_MECHANIC_IMMUNITY      | The spell ignores the mechanic immunity of creatures                                                                               |

```sql
-- (@SPELL_ATTR0_CU_NEGATIVE = @SPELL_ATTR0_CU_NEGATIVE_EFF0 | @SPELL_ATTR0_CU_NEGATIVE_EFF1 | @SPELL_ATTR0_CU_NEGATIVE_EFF2)
-- (@SPELL_ATTR0_CU_POSITIVE = @SPELL_ATTR0_CU_POSITIVE_EFF0 | @SPELL_ATTR0_CU_POSITIVE_EFF1 | @SPELL_ATTR0_CU_POSITIVE_EFF2)

DELETE FROM `spell_custom_attr` WHERE `spell_id`=123;
INSERT INTO `spell_custom_attr` (`spell_id`, `attributes`) VALUES
(123, @SPELL_ATTR0_CU_FLAG1 | @SPELL_ATTR0_CU_FLAG2);
```

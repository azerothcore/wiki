# spell\_custom\_attr

[<-Back-to:World](database-world)

**The \`spell\_custom\_attr\` table**

Table used for storing custom spell attributes.

**Table Structure**

| Field           | Type      | Attributes | Key | Null | Default | Extra | Comment               |
| --------------- | --------- | ---------- | --- | ---- | ------- | ----- | --------------------- |
| [spell_id][1]   | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | spell id              |
| [attributes][2] | INT       | UNSIGNED   |     | NO   | 0       |       | SpellCustomAttributes |

[1]: #spell_id
[2]: #attributes

**Description of the fields**

### spell_id

Spell ID. See [Spell.dbc](spell_dbc) .

### attributes

Spell custom attributes from the enumeration SpellCustomAttributes in SpellInfo.h

| Attributes                                   | Flag       | Bit value  | Comment                                                               |
| -------------------------------------------- | ---------- | ---------- | --------------------------------------------------------------------- |
| SPELL_ATTR0_CU_ENCHANT_PROC                  | 1          | 0x00000001 |                                                                       |
| SPELL_ATTR0_CU_CONE_BACK                     | 2          | 0x00000002 |                                                                       |
| SPELL_ATTR0_CU_CONE_LINE                     | 4          | 0x00000004 |                                                                       |
| SPELL_ATTR0_CU_SHARE_DAMAGE                  | 8          | 0x00000008 | Meteor like spells (divided damage among all targets)                 |
| SPELL_ATTR0_CU_NO_INITIAL_THREAT             | 16         | 0x00000010 |                                                                       |
| SPELL_ATTR0_CU_AURA_CC                       | 32         | 0x00000020 |                                                                       |
| SPELL_ATTR0_CU_DONT_BREAK_STEALTH            | 64         | 0x00000040 |                                                                       |
| SPELL_ATTR0_CU_NO_PVP_FLAG                   | 128        | 0x00000080 | Does not PvP flag                                                     |
| SPELL_ATTR0_CU_DIRECT_DAMAGE                 | 256        | 0x00000100 |                                                                       |
| SPELL_ATTR0_CU_CHARGE                        | 512        | 0x00000200 |                                                                       |
| SPELL_ATTR0_CU_PICKPOCKET                    | 1024       | 0x00000400 |                                                                       |
| SPELL_ATTR0_CU_IGNORE_EVADE                  | 2048       | 0x00000800 | Do not remove the specified aura upon evading                         |
| SPELL_ATTR0_CU_NEGATIVE_EFF0                 | 4096       | 0x00001000 |                                                                       |
| SPELL_ATTR0_CU_NEGATIVE_EFF1                 | 8192       | 0x00002000 |                                                                       |
| SPELL_ATTR0_CU_NEGATIVE_EFF2                 | 16384      | 0x00004000 |                                                                       |
| SPELL_ATTR0_CU_IGNORE_ARMOR                  | 32768      | 0x00008000 |                                                                       |
| SPELL_ATTR0_CU_REQ_TARGET_FACING_CASTER      | 65536      | 0x00010000 |                                                                       |
| SPELL_ATTR0_CU_REQ_CASTER_BEHIND_TARGET      | 131072     | 0x00020000 |                                                                       |
| SPELL_ATTR0_CU_ALLOW_INFLIGHT_TARGET         | 262144     | 0x00040000 |                                                                       |
| SPELL_ATTR0_CU_NEEDS_AMMO_DATA               | 524288     | 0x00080000 |                                                                       |
| SPELL_ATTR0_CU_BINARY_SPELL                  | 1048576    | 0x00100000 |                                                                       |
| SPELL_ATTR0_CU_NO_POSITIVE_TAKEN_BONUS       | 2097152    | 0x00200000 |                                                                       |
| SPELL_ATTR0_CU_SINGLE_AURA_STACK             | 4194304    | 0x00400000 | All sources add stacks the same aura                                  |
| SPELL_ATTR0_CU_SCHOOLMASK_NORMAL_WITH_MAGIC  | 8388608    | 0x00800000 |                                                                       |
| SPELL_ATTR0_CU_AURA_CANNOT_BE_SAVED          | 16777216   | 0x01000000 |                                                                       |
| SPELL_ATTR0_CU_POSITIVE_EFF0                 | 33554432   | 0x02000000 |                                                                       |
| SPELL_ATTR0_CU_POSITIVE_EFF1                 | 67108864   | 0x04000000 |                                                                       |
| SPELL_ATTR0_CU_POSITIVE_EFF2                 | 134217728  | 0x08000000 |                                                                       |
| SPELL_ATTR0_CU_FORCE_SEND_CATEGORY_COOLDOWNS | 268435456  | 0x10000000 |                                                                       |
| SPELL_ATTR0_CU_FORCE_AURA_SAVING             | 536872960  | 0x20000800 |                                                                       |
| SPELL_ATTR0_CU_ONLY_ONE_AREA_AURA            | 536870912  | 0x20000000 | Only 1 Persistent Area Aura can be active (e.g Marrowgar's coldflame) |
| SPELL_ATTR0_CU_ENCOUNTER_REWARD              | 1073741824 | 0x40000000 |                                                                       |
| SPELL_ATTR0_CU_BYPASS_MECHANIC_IMMUNITY      | 2147483648 | 0x80000000 |                                                                       |

```sql
-- (@SPELL_ATTR0_CU_NEGATIVE = @SPELL_ATTR0_CU_NEGATIVE_EFF0 | @SPELL_ATTR0_CU_NEGATIVE_EFF1 | @SPELL_ATTR0_CU_NEGATIVE_EFF2)
-- (@SPELL_ATTR0_CU_POSITIVE = @SPELL_ATTR0_CU_POSITIVE_EFF0 | @SPELL_ATTR0_CU_POSITIVE_EFF1 | @SPELL_ATTR0_CU_POSITIVE_EFF2)

DELETE FROM `spell_custom_attr` WHERE `spell_id`=123;
INSERT INTO `spell_custom_attr` (`spell_id`, `attributes`) VALUES
(123, @SPELL_ATTR0_CU_FLAG1 | @SPELL_ATTR0_CU_FLAG2);
```

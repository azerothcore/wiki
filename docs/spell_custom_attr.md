# spell\_custom\_attr

[<-Back-to:World](database-world.md)

**The \`spell\_custom\_attr\` table**

Table used for storing custom spell attributes.

**Structure**

| Field           | Type          | Attributes | Key | Null | Default | Extra | Comment               |
|-----------------|---------------|------------|-----|------|---------|-------|-----------------------|
| [entry][1]      | medium int(8) | unsigned   | PRI | NO   | 0       |       | spell id              |
| [attributes][2] | medium int(8) | unsigned   |     | NO   | 0       |       | SpellCustomAttributes |

[1]: #entry
[2]: #attributes

**Description of the fields**

### entry

Spell ID. See [Spell.dbc](spell_dbc) .

### attributes

Spell custom attributes from the enumeration SpellCustomAttributes in SpellInfo.h

``` sql
SET @SPELL_ATTR0_CU_ENCHANT_PROC                  = 1,
    @SPELL_ATTR0_CU_CONE_BACK                     = 2,
    @SPELL_ATTR0_CU_CONE_LINE                     = 4,
    @SPELL_ATTR0_CU_SHARE_DAMAGE                  = 8,
    @SPELL_ATTR0_CU_NO_INITIAL_THREAT             = 16,
    @SPELL_ATTR0_CU_AURA_CC                       = 32,
    @SPELL_ATTR0_DONT_BREAK_STEALTH               = 64,
    SPELL_ATTR0_CU_NONE3                          = 128,
    @SPELL_ATTR0_CU_DIRECT_DAMAGE                 = 256,
    @SPELL_ATTR0_CU_CHARGE                        = 512,
    @SPELL_ATTR0_CU_PICKPOCKET                    = 1024,
    @SPELL_ATTR0_CU_NONE4                         = 2048,
    @SPELL_ATTR0_CU_NEGATIVE_EFF0                 = 4096,
    @SPELL_ATTR0_CU_NEGATIVE_EFF1                 = 8192,
    @SPELL_ATTR0_CU_NEGATIVE_EFF2                 = 16384,
    @SPELL_ATTR0_CU_NEGATIVE                      = 28672,
    @SPELL_ATTR0_CU_IGNORE_ARMOR                  = 32768,
    @SPELL_ATTR0_CU_REQ_TARGET_FACING_CASTER      = 65536,
    @SPELL_ATTR0_CU_REQ_CASTER_BEHIND_TARGET      = 131072,
    @SPELL_ATTR0_CU_ALLOW_INFLIGHT_TARGET         = 262144,
    @SPELL_ATTR0_CU_NONE6                         = 524288,
    @SPELL_ATTR0_CU_BINARY_SPELL                  = 1048576,
    @SPELL_ATTR0_CU_NO_POSITIVE_TAKEN_BONUS       = 2097152,
    @SPELL_ATTR0_CU_SINGLE_AURA_STACK             = 4194304,
    @SPELL_ATTR0_CU_SCHOOLMASK_NORMAL_WITH_MAGIC  = 8388608,
    @SPELL_ATTR0_CU_ENCOUNTER_REWARD              = 16777216,
    @SPELL_ATTR0_CU_POSITIVE_EFF0                 = 33554432,
    @SPELL_ATTR0_CU_POSITIVE_EFF1                 = 67108864,
    @SPELL_ATTR0_CU_POSITIVE_EFF2                 = 134217728;

-- (@SPELL_ATTR0_CU_NEGATIVE = @SPELL_ATTR0_CU_NEGATIVE_EFF0 | @SPELL_ATTR0_CU_NEGATIVE_EFF1 | @SPELL_ATTR0_CU_NEGATIVE_EFF2)
-- (@SPELL_ATTR0_CU_POSITIVE = @SPELL_ATTR0_CU_POSITIVE_EFF0 | @SPELL_ATTR0_CU_POSITIVE_EFF1 | @SPELL_ATTR0_CU_POSITIVE_EFF2)

DELETE FROM `spell_custom_attr` WHERE `entry`=123;
INSERT INTO `spell_custom_attr` (`entry`, `attributes`) VALUES
(123, @SPELL_ATTR0_CU_FLAG1 | @SPELL_ATTR0_CU_FLAG2);
```

# spell\_proc

[<-返回至:World](database-world)

**\`spell\_proc\` 表**

此表保存有关某些法术在哪些事件（或触发条件/proc）下被激活的信息。此表中的所有法术都必须带有 SPELL\_AURA\_PROC\_TRIGGER\_SPELL (42) 光环。此表中的任何条目都将覆盖法术 DBC 条目中现有的 proc 设置。

**表结构**

| Field                 | Type     | Attributes | Key | Null | Default | Extra  | Comment |
| --------------------- | -------- | ---------- | --- | ---- | ------- | ------ | ------- |
| [SpellId][1]          | INT      | SIGNED     | PRI | NO   | 0       | Unique |         |
| [SchoolMask][2]       | TINYINT  | UNSIGNED   |     | NO   | 0       |        |         |
| [SpellFamilyName][3]  | SMALLINT | UNSIGNED   |     | NO   | 0       |        |         |
| [SpellFamilyMask0][4] | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [SpellFamilyMask1][5] | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [SpellFamilyMask2][6] | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [ProcFlags][7]        | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [SpellTypeMask][8]    | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [SpellPhaseMask][9]   | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [HitMask][10]         | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [AttributesMask][11]     | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [DisableEffectsMask][12] | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [ProcsPerMinute][13]     | FLOAT    |            |     | NO   | 0       |        |         |
| [Chance][14]             | FLOAT    |            |     | NO   | 0       |        |         |
| [Cooldown][15]           | INT      | UNSIGNED   |     | NO   | 0       |        |         |
| [Charges][16]            | TINYINT  | UNSIGNED   |     | NO   | 0       |        |         |

[1]: #spellid
[2]: #schoolmask
[3]: #spellfamilyname
[4]: #spellfamilymask0
[5]: #spellfamilymask1
[6]: #spellfamilymask2
[7]: #procflags
[8]: #spelltypemask
[9]: #spellphasemask
[10]: #hitmask
[11]: #attributesmask
[12]: #disableeffectsmask
[13]: #procsperminute
[14]: #chance
[15]: #cooldown
[16]: #charges

**字段说明**

### SpellId

能够在某事件上触发（proc）的法术 ID。（对于有层级的法术可以使用负数 spellId）

### SchoolMask

此字段包含一个位掩码，用于控制可以在哪些类型的法术上触发 proc。例如，某个光环只在其被施加的单位被暗影法术命中时才触发（法术 34914）。要组合多种法术学派，只需将位值相加。

| School ID | Bit | Name     |
| --------- | --- | -------- |
| 0         | 1   | Physical |
| 1         | 2   | Holy     |
| 2         | 4   | Fire     |
| 3         | 8   | Nature   |
| 4         | 16  | Frost    |
| 5         | 32  | Shadow   |
| 6         | 64  | Arcane   |

### SpellFamilyName

此字段控制具有何种法术前缀（family name）的法术可以触发该被触发的法术。

| ID  | Family Name  |
| --- | ------------ |
| 0   | Generic      |
| 3   | Mage         |
| 4   | Warrior      |
| 5   | Warlock      |
| 6   | Priest       |
| 7   | Druid        |
| 8   | Rogue        |
| 9   | Hunter       |
| 10  | Paladin      |
| 11  | Shaman       |
| 13  | Potion       |
| 15  | Death Knight |
| 53  | Monk         |
| 107 | Demon Hunter |

### SpellFamilyMask0

此字段控制具有哪些法术家族标志（family flags）的法术可以触发该被触发的法术。

### SpellFamilyMask1

`field-no-description|5`

### SpellFamilyMask2

`field-no-description|6`

### ProcFlags

如果非零，则用于覆盖 DBC 中法术原有的 ProcFlags。

一个位掩码，控制哪些事件会触发该法术。要组合可能的事件，请将各 proc 位相加。

**示例:** 32+64=96 (PROC\_FLAG\_TAKEN\_MELEE\_SPELL\_HIT + PROC\_FLAG\_SUCCESSFUL\_RANGED\_HIT)

| Event                                   | Flag     | Bit value  | Comment                                                      |
| --------------------------------------- | -------- | ---------- | ------------------------------------------------------------ |
| PROC_FLAG_NONE                          | 0        | 0x00000000 |                                                              |
| PROC_FLAG_KILLED                        | 1        | 0x00000001 | 被攻击者击杀                                                 |
| PROC_FLAG_KILL_AND_GET_XP               | 2        | 0x00000002 | 击杀可获得经验或荣誉                                         |
| PROC_FLAG_SUCCESSFUL_MELEE_HIT          | 4        | 0x00000004 | 近战攻击命中成功                                             |
| PROC_FLAG_TAKEN_MELEE_HIT               | 8        | 0x00000008 | 受到近战命中造成的伤害                                       |
| PROC_FLAG_SUCCESSFUL_MELEE_SPELL_HIT    | 16       | 0x00000010 | 使用近战武器的法术攻击成功                                   |
| PROC_FLAG_TAKEN_MELEE_SPELL_HIT         | 32       | 0x00000020 | 受到使用近战武器的法术造成的伤害                             |
| PROC_FLAG_SUCCESSFUL_RANGED_HIT         | 64       | 0x00000040 | 远程攻击命中成功                                             |
| PROC_FLAG_TAKEN_RANGED_HIT              | 128      | 0x00000080 | 受到远程攻击命中造成的伤害                                   |
| PROC_FLAG_SUCCESSFUL_RANGED_SPELL_HIT   | 256      | 0x00000100 | 使用远程武器的法术远程攻击成功                               |
| PROC_FLAG_TAKEN_RANGED_SPELL_HIT        | 512      | 0x00000200 | 受到使用远程武器的法术造成的伤害                             |
| PROC_FLAG_SUCCESSFUL_POSITIVE_AOE_HIT   | 1024     | 0x00000400 | AoE 法术命中成功（不能 100% 确定是否未使用）                 |
| PROC_FLAG_TAKEN_POSITIVE_AOE            | 2048     | 0x00000800 | 受到增益性 AoE 法术命中（不能 100% 确定是否未使用）          |
| PROC_FLAG_SUCCESSFUL_AOE_SPELL_HIT      | 4096     | 0x00001000 | AoE 伤害法术命中成功（不能 100% 确定是否未使用）             |
| PROC_FLAG_TAKEN_AOE_SPELL_HIT           | 8192     | 0x00002000 | 受到 AoE 伤害法术命中（不能 100% 确定是否未使用）            |
| PROC_FLAG_SUCCESSFUL_POSITIVE_SPELL     | 16384    | 0x00004000 | 增益性法术施放成功（默认仅在治疗时）                         |
| PROC_FLAG_TAKEN_POSITIVE_SPELL          | 32768    | 0x00008000 | 受到增益性法术命中（默认仅在治疗时）                         |
| PROC_FLAG_SUCCESSFUL_NEGATIVE_SPELL_HIT | 65536    | 0x00010000 | 伤害性法术施放成功（默认仅在造成伤害时）                     |
| PROC_FLAG_TAKEN_NEGATIVE_SPELL_HIT      | 131072   | 0x00020000 | 受到伤害性法术命中（默认仅在造成伤害时）                     |
| PROC_FLAG_DONE_PERIODIC                 | 262144   | 0x00040000 | 造成的周期性伤害/治疗，由标志 14-17 决定                     |
| PROC_FLAG_TAKEN_PERIODIC                | 524288   | 0x00080000 | 受到的周期性伤害/治疗，由标志 14-17 决定                     |
| PROC_FLAG_TAKEN_ANY_DAMAGE              | 1048576  | 0x00100000 | 受到任何伤害                                               |
| PROC_FLAG_ON_TRAP_ACTIVATION            | 2097152  | 0x00200000 | 陷阱激活时                                                 |
| PROC_FLAG_TAKEN_OFFHAND_HIT             | 4194304  | 0x00400000 | 受到的副手近战攻击（未使用）                               |
| PROC_FLAG_SUCCESSFUL_OFFHAND_HIT        | 8388608  | 0x00800000 | 副手近战攻击成功                                           |
| PROC_FLAG_DEATH                         | 16777216 | 0x01000000 | 以任何方式死亡                                             |

### SpellTypeMask

用于选择哪些类型的法术可以触发该 proc，要组合多种类型，只需将位值相加。

| Event                       | Flag | Bit        | Comment              |
| --------------------------- | ---- | ---------- | -------------------- |
| PROC_SPELL_TYPE_NONE        | 0    | 0x00000000 |                      |
| PROC_SPELL_TYPE_DAMAGE      | 1    | 0x00000001 | 仅伤害性法术         |
| PROC_SPELL_TYPE_HEAL        | 2    | 0x00000002 | 仅治疗法术           |
| PROC_SPELL_TYPE_NO_DMG_HEAL | 4    | 0x00000004 | 所有其他法术         |
| PROC_SPELL_TYPE_MASK_ALL    | 7    | 0x00000007 | 所有掩码的组合       |

### SpellPhaseMask

法术在哪个阶段可以触发该 proc。通常同时使用其中一个，但也可以组合使用。

| Event                     | Flag | Bit        | Comment                                                     |
| ------------------------- | ---- | ---------- | ----------------------------------------------------------- |
| PROC_SPELL_PHASE_NONE     | 0    | 0x00000000 |                                                             |
| PROC_SPELL_PHASE_CAST     | 1    | 0x00000001 | 当法术刚刚施放完成时触发                                    |
| PROC_SPELL_PHASE_HIT      | 2    | 0x00000002 | 当法术命中其目标时触发                                      |
| PROC_SPELL_PHASE_FINISH   | 4    | 0x00000004 | 当法术对所有目标完成所有效果之后触发                        |
| PROC_SPELL_PHASE_MASK_ALL | 7    | 0x00000007 | 所有掩码的组合                                              |

### HitMask

用于为法术添加特殊条件，例如某些法术可能只在暴击时触发。

| Event                   | Flag  | Bit        | Comment                          |
| ----------------------- | ----- | ---------- | -------------------------------- |
| PROC\_HIT\_NONE         | 0     | 0x00000000 | （特殊，见脚注）                 |
| PROC\_HIT\_NORMAL       | 1     | 0x00000001 | 仅非暴击命中                     |
| PROC\_HIT\_CRITICAL     | 2     | 0x00000002 | 仅暴击命中                       |
| PROC\_HIT\_MISS         | 4     | 0x00000004 | 顾名思义                         |
| PROC\_HIT\_FULL\_RESIST | 8     | 0x00000008 | 仅在完全抵抗时（无部分抵抗）     |
| PROC\_HIT\_DODGE        | 16    | 0x00000010 | 顾名思义                         |
| PROC\_HIT\_PARRY        | 32    | 0x00000020 | 顾名思义                         |
| PROC\_HIT\_BLOCK        | 64    | 0x00000040 | 部分或完全格挡                   |
| PROC\_HIT\_EVADE        | 128   | 0x00000080 | 顾名思义                         |
| PROC\_HIT\_IMMUNE       | 256   | 0x00000100 | 顾名思义                         |
| PROC\_HIT\_DEFLECT      | 512   | 0x00000200 | 顾名思义                         |
| PROC\_HIT\_ABSORB       | 1024  | 0x00000400 | 部分或完全吸收                   |
| PROC\_HIT\_REFLECT      | 2048  | 0x00000800 | 顾名思义                         |
| PROC\_HIT\_INTERRUPT    | 4096  | 0x00001000 | （目前未使用）                   |
| PROC\_HIT\_FULL\_BLOCK  | 8192  | 0x00002000 | 仅在完全格挡时                   |
| PROC\_HIT\_MASK\_ALL    | 12287 | 0x00002FFF | 所有掩码的组合                   |

PROC\_HIT\_NONE 将在以下情况触发：

-   PROC\_HIT\_NORMAL+PROC\_HIT\_CRITICAL，当触发为 TAKEN（受到）时
-   PROC\_HIT\_NORMAL+PROC\_HIT\_CRITICAL+PROC\_HIT\_ABSORB，当触发为 DONE（造成）时

### AttributesMask

为 proc 添加特殊行为，只有在满足这些条件时法术才能触发 proc。

| Event                                   | Flag | Bit       | Comment                                                                                  |
| --------------------------------------- | ---- | --------- | ---------------------------------------------------------------------------------------- |
| PROC\_ATTR\_REQ\_EXP\_OR\_HONOR         | 1    | 0x0000001 | 要求触发目标给予经验或荣誉，光环才能触发 proc                                            |
| PROC\_ATTR\_TRIGGERED\_CAN\_PROC        | 2    | 0x0000002 | 即使是被触发的法术（triggered spells）也能使光环触发 proc                                |
| PROC\_ATTR\_REQ\_MANA\_COST             | 4    | 0x0000004 | 要求触发法术有法力消耗，光环才能触发 proc                                                |
| PROC\_ATTR\_REQ\_SPELLMOD               | 8    | 0x0000008 | 要求触发法术受触发 proc 的光环影响，才会消耗层数                                        |
| PROC\_ATTR\_USE\_STACKS\_FOR\_CHARGES   | 16   | 0x0000010 | 消耗 proc 时从触发 proc 的光环上减少一层叠加，而不是减少充能数                           |
| PROC\_ATTR\_REDUCE\_PROC\_60            | 128  | 0x0000080 | 如果触发 proc 的角色等级 > 60，光环应有更低的触发概率                                   |
| PROC\_ATTR\_CANT\_PROC\_FROM\_ITEM_CAST| 256  | 0x0000100 | 如果 proc 是由物品施放的法术引起，则不允许光环触发 proc                                 |

### DisableEffectsMask

用于显式禁用特定光环效果触发 proc 的位掩码。这允许对多效果光环的哪些效果可以触发 proc 进行细粒度控制。

| Effect | Flag | Comment                                |
| ------ | ---- | -------------------------------------- |
| 0      | 1    | 禁用光环 proc 效果 0                   |
| 1      | 2    | 禁用光环 proc 效果 1                   |
| 2      | 4    | 禁用光环 proc 效果 2                   |

### ProcsPerMinute

如果非零，此字段控制该法术每分钟应触发的次数。你不应同时设置 ProcsPerMinute 和 Chance；在这种情况下，ProcsPerMinute 优先。

### Chance

如果非零，表示法术触发的概率。如果 ProcsPerMinute 和 Chance 都留为零，则采用 DBC 中的 ProcChance。

### Cooldown

定义该法术的隐藏冷却时间，以毫秒为单位。也称为 proc 的内部冷却时间，或 ICD。

值必须 >=0。如果该值不满足条件，SQL 将在 `spell_proc_chk_1` 上失败。

### Charges

如果非零，则覆盖可供触发 proc 的光环充能次数。否则该值取自 DBC。

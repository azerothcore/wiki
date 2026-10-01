# creature_immunities

[<-返回至:World](database-world)

**`creature_immunities` 表**

此表集中管理生物和法术的免疫。`creature_template.CreatureImmunitiesId` 指向此表中的一条记录。法术也可以通过光环 ID 147（`SPELL_AURA_MECHANIC_IMMUNITY_MASK`）引用 `creature_immunities` 记录，其中 `misc` 存储所引用的 ID。

**表结构**

| 字段 | 类型 | 属性 | 键 | 空 | 默认值 | 额外 | 注释 |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id) | MEDIUMINT | UNSIGNED | PRI | NO | 0 | | 标识符 |
| [SchoolMask](#schoolmask) | TINYINT | UNSIGNED | | NO | 0 | | 法术学派位掩码 |
| [DispelTypeMask](#dispeltypemask) | SMALLINT | UNSIGNED | | NO | 0 | | 驱散类型掩码 |
| [MechanicsMask](#mechanicsmask) | BIGINT | UNSIGNED | | NO | 0 | | 机制免疫位掩码 |
| [Effects](#effects) | MEDIUMTEXT | | | NO | (NULL) | | 此记录阻挡的效果 ID 或列表 |
| [Auras](#auras) | MEDIUMTEXT | | | NO | (NULL) | | 此记录阻挡的光环 ID 或列表 |
| [ImmuneAoE](#immuneaoe) | TINYINT(1) | | | NO | 0 | | 阻挡范围效果法术（布尔值） |
| [ImmuneChain](#immunechain) | TINYINT(1) | | | NO | 0 | | 阻挡链式效果（布尔值） |
| [Comment](#comment) | MEDIUMTEXT | | | NO | (NULL) | | 自由文本描述 |

**字段说明**

### ID

- 正数引用通常来自确认存在免疫的法术（光环 ID 147 `SPELL_AURA_MECHANIC_IMMUNITY_MASK`）。
- 负数是为引擎/核心自定义设置的免疫。


### SchoolMask

| 值    | 名称 |
| -----:| ---- |
| 1 | SPELL_SCHOOL_NORMAL |
| 2 | SPELL_SCHOOL_HOLY |
| 4 | SPELL_SCHOOL_FIRE |
| 8 | SPELL_SCHOOL_NATURE |
| 16 | SPELL_SCHOOL_FROST |
| 32 | SPELL_SCHOOL_SHADOW |
| 64 | SPELL_SCHOOL_ARCANE |

完整掩码（所有学派）= `1+2+4+8+16+32+64 = 127`

### DispelTypeMask

| 值    | 名称 |
| -----:| ---- |
| 1 | DISPEL_NONE |
| 2 | DISPEL_MAGIC |
| 4 | DISPEL_CURSE |
| 8 | DISPEL_DISEASE |
| 16 | DISPEL_POISON |
| 32 | DISPEL_STEALTH |
| 64 | DISPEL_INVISIBILITY |
| 128 | DISPEL_ALL |
| 256 | DISPEL_SPE_NPC_ONLY |
| 512 | DISPEL_ENRAGE |
| 1024 | DISPEL_ZG_TICKET |
| 2048 | DESPEL_OLD_UNUSED |

`DISPEL_ALL_MASK`（用于移除常见有害学派的常见掩码）是魔法/诅咒/疾病/毒药位的组合：

数值：`2 | 4 | 8 | 16 = 30`

### MechanicsMask

| 值    | 名称 | 注释 |
| -----:| ---- | ----- |
| 0x1 | CHARM |
| 0x2 | DISORIENTED |
| 0x4 | DISARM |
| 0x8 | DISTRACT |
| 0x10 | FEAR |
| 0x20 | GRIP | 死亡之握及类似效果 |
| 0x40 | ROOT |
| 0x80 | SLOW_ATTACK |
| 0x100 | SILENCE |
| 0x200 | SLEEP |
| 0x400 | SNARE |
| 0x800 | STUN |
| 0x1000 | FREEZE |
| 0x2000 | KNOCKOUT | 瘫痪效果（例如 忏悔） |
| 0x4000 | BLEED |
| 0x8000 | BANDAGE | 与治疗相关的机制 |
| 0x10000 | POLYMORPH |
| 0x20000 | BANISH |
| 0x40000 | SHIELD |
| 0x80000 | SHACKLE | 仅亡灵束缚 |
| 0x100000 | MOUNT |
| 0x200000 | INFECTED | 例如 冰霜疫病、血之疫病 |
| 0x400000 | TURN | 例如 超度邪恶 |
| 0x800000 | HORROR | 例如 死亡缠绕 |
| 0x1000000 | INVULNERABILITY | 仅 自律、虚空防护、外交免疫 |
| 0x2000000 | INTERRUPT |
| 0x4000000 | DAZE |
| 0x8000000 | DISCOVERY | 制造物品效果 |
| 0x10000000 | IMMUNE_SHIELD | 圣盾术、寒冰屏障、保护之手 |
| 0x20000000 | SAPPED |
| 0x40000000 | ENRAGED |

### Effects

参见[法术效果参考](spell-effects-reference)

### Auras

参见[法术光环参考](spell-aura-reference)

### ImmuneAoE

以前
- `creature_flags.extra` `+4194304` AVOID_AOE - 被范围攻击（AoE）忽略（用于 icc 鲜血王子议会 NPC - 黑暗核弹）

**示例**

- NO_TAUNT `creature_flags.extra` `+256`：效果 ATTACK_ME `114` 和 MOD_TAUNT 光环 `11`
- IMMUNITY_KNOCKBACK `creature_flags.extra` `+1073741824`：EFFECT_KNOCK_BACK、EFFECT_KNOCK_BACK_DEST、EFFECT_PULL_TOWARDS、EFFECT_PULL_TOWARDS_DEST 效果 `98,124,144,145`

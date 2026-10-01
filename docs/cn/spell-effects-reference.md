# 法术效果参考（Spell Effects Reference）

[<-返回至:spell_dbc](spell_dbc)

### 本页包含关于 EffectMiscValue 及其他法术效果（Spell Effect）值的用法说明。

### 包含所有法术效果的列表。

**版本为：3.3.5a**

### 相关信息
[召唤属性（Summon Properties）](summonproperties_dbc)

[法术光环（Spell Aura）](spell-aura-reference)

# 法术效果名称

SPELL_EFFECT_INSTAKILL = 1

SPELL_EFFECT_SCHOOL_DAMAGE = 2
- BasePoints：基础伤害
- Multiple：伤害倍率

SPELL_EFFECT_DUMMY = 3
- BasePoints：任意值

SPELL_EFFECT_PORTAL_TELEPORT = 4

SPELL_EFFECT_TELEPORT_UNITS = 5
- TargetB：传送位置

SPELL_EFFECT_APPLY_AURA = 6
- BasePoints：光环的值（取决于光环 ID）
- EffectAura：[法术光环](spell-aura-reference)

SPELL_EFFECT_ENVIRONMENTAL_DAMAGE = 7
- BasePoints：基础伤害

SPELL_EFFECT_POWER_DRAIN = 8
- BasePoints：基础吸取量
- Multiple：吸取倍率

SPELL_EFFECT_HEALTH_LEECH = 9
- BasePoints：基础吸取量
- Multiple：吸取倍率
- TargetB：如果使用，TargetA 会被治疗

SPELL_EFFECT_HEAL = 10
- BasePoints：基础治疗量
- Multiple：治疗倍率
- TargetB：如果使用，TargetA 会被治疗

SPELL_EFFECT_BIND = 11
- BasePoints：未知
- EffectMiscValueA：区域 ID（仅死亡之门）

SPELL_EFFECT_PORTAL = 12
- TargetA：传送目的地
- TargetB：目标

SPELL_EFFECT_RITUAL_BASE = 13 // 未使用

SPELL_EFFECT_RITUAL_SPECIALIZE = 14 // 未使用

SPELL_EFFECT_RITUAL_ACTIVATE_PORTAL = 15 // 未使用

SPELL_EFFECT_QUEST_COMPLETE = 16
- EffectMiscValueA：任务 ID
- TargetB：额外目标（法术 30790 使用）

SPELL_EFFECT_WEAPON_DAMAGE_NOSCHOOL = 17
- BasePoints：基础伤害

SPELL_EFFECT_RESURRECT = 18
- BasePoints：恢复的生命和法力百分比（%）
- TargetB：额外目标（法术 29820 使用，群体复活）

SPELL_EFFECT_ADD_EXTRA_ATTACKS = 19
- BasePoints：额外近战攻击次数

SPELL_EFFECT_DODGE = 20

SPELL_EFFECT_EVADE = 21

SPELL_EFFECT_PARRY = 22

SPELL_EFFECT_BLOCK = 23

SPELL_EFFECT_CREATE_ITEM = 24
- BasePoints：物品数量
- EffectItemType：[物品 ID](item_template)

SPELL_EFFECT_WEAPON = 25

SPELL_EFFECT_DEFENSE = 26

SPELL_EFFECT_PERSISTENT_AREA_AURA = 27
- BasePoints：取决于[法术光环](spell-aura-reference)

SPELL_EFFECT_SUMMON = 28
- BasePoints：召唤数量（有时用于设置被召唤生物的生命值）
- EffectMiscValueA：[生物 ID](creature_template)
- EffectMiscValueB：[召唤属性](summonproperties_dbc)
- Radius：刷新范围

SPELL_EFFECT_LEAP = 29
- TargetA：目标
- TargetB：目的地
- Radius：闪烁/跳跃距离

SPELL_EFFECT_ENERGIZE = 30
- BasePoints：数量
- TargetB：额外目标
- EffectMiscValueA：能量类型

| ID  | Type       |
| --- | ---------- |
| 0   | Mana       |
| 1   | Rage       |
| 2   | Focus      |
| 3   | Energy     |
| 4   | Happiness  |
| 5   | Rune       |
| 6   | Runic      |
| 7   | Max powers |
| 127 | All powers |
| -2  | HP         |

SPELL_EFFECT_WEAPON_PERCENT_DAMAGE = 31
- BasePoints：基础伤害百分比

SPELL_EFFECT_TRIGGER_MISSILE = 32
- TriggerSpell：法术 ID

SPELL_EFFECT_OPEN_LOCK = 33
- BasePoints：所需的开锁技能等级

SPELL_EFFECT_SUMMON_CHANGE_ITEM = 34 // 类似祝福（Benediction）这类武器
EffectItemType：新的[物品 ID](item_template)

SPELL_EFFECT_APPLY_AREA_AURA_PARTY = 35
- BasePoints：取决于[法术光环](spell-aura-reference)

SPELL_EFFECT_LEARN_SPELL = 36
- TriggerSpell：法术 ID

SPELL_EFFECT_SPELL_DEFENSE = 37

SPELL_EFFECT_DISPEL = 38
- BasePoints：要驱散的法术数量
- EffectMiscValueA：驱散类型

| ID | Type       | ID | Type         | ID | Type            |
| -- | ---------- | -- | ------------ | -- | --------------- |
| 0  | None       | 4  | Poison       | 8  | SPE_NPC_ONLY    |
| 1  | Magic      | 5  | Stealth      | 9  | Enrage          |
| 2  | Curse      | 6  | Invisibility | 10 | ZG Trinket      |
| 3  | Disease    | 7  | ALL          | 11 | Old Unseen      |

SPELL_EFFECT_LANGUAGE = 39
- EffectMiscValueA：[语言 ID](languages)

SPELL_EFFECT_DUAL_WIELD = 40

SPELL_EFFECT_JUMP = 41
- Multiple：未知
- EffectMiscValueA：XY 方向速度或 Z 方向速度
- EffectMiscValueB：XY 方向速度或 Z 方向速度

SPELL_EFFECT_JUMP_DEST = 42
- Multiple：未知
- EffectMiscValueA：XY 方向速度或 Z 方向速度
- EffectMiscValueB：XY 方向速度或 Z 方向速度

SPELL_EFFECT_TELEPORT_UNITS_FACE_CASTER = 43
- BasePoints：要传送的单位数量

SPELL_EFFECT_SKILL_STEP = 44
- BasePoints：未知
- EffectMiscValueA：[技能 ID](skillline)

SPELL_EFFECT_ADD_HONOR = 45
- BasePoints：要奖励的荣誉点数

SPELL_EFFECT_SPAWN = 46

SPELL_EFFECT_TRADE_SKILL = 47

SPELL_EFFECT_STEALTH = 48

SPELL_EFFECT_DETECT = 49

SPELL_EFFECT_TRANS_DOOR = 50
- EffectMiscValueA：[gameobject_template ID](gameobject_template)
- gameobject_template 的 Data0 是点击时与传送目的地相关联的法术。
- Data0 条目 = spell_target_position 表

SPELL_EFFECT_FORCE_CRITICAL_HIT = 51 // 未使用

SPELL_EFFECT_GUARANTEE_HIT = 52 // 未使用

SPELL_EFFECT_ENCHANT_ITEM = 53
- EffectItemType：[物品 ID](item_template)（卷轴/铭文）
- EffectMiscValueA：来自 SpellItemEnchantment.dbc 的 ID
- EffectMiscValueA：14 = 护甲，15 = 武器，与 EffectItemType 相关联。

SPELL_EFFECT_ENCHANT_ITEM_TEMPORARY = 54
- EffectMiscValueA：来自 SpellItemEnchantment.dbc 的 ID

SPELL_EFFECT_TAMECREATURE = 55

SPELL_EFFECT_SUMMON_PET = 56
- Multiple：相对于施法者等级（例如 -3 表示施法者等级 -3）。目前无效。
- EffectMiscValueA：[生物 ID](creature_template)

SPELL_EFFECT_LEARN_PET_SPELL = 57
- TriggerSpell：法术 ID

SPELL_EFFECT_WEAPON_DAMAGE = 58
- BasePoints：额外伤害
- TargetB：额外目标
- Chain Target：额外目标

SPELL_EFFECT_CREATE_RANDOM_ITEM = 59
- EffectMiscValueA：未知

SPELL_EFFECT_PROFICIENCY = 60

SPELL_EFFECT_SEND_EVENT = 61
- EffectMiscValueA：从 acevent_scripts 表调用一个事件。\
（大多数不匹配，但少数是正确的。）

SPELL_EFFECT_POWER_BURN = 62
- BasePoints：要燃烧的法力值
- TargetB：额外目标
- Multiple：转化为伤害的百分比（例如 0.5 表示每燃烧 1 点法力造成 0.5 点伤害）
- Chain Target：额外目标

SPELL_EFFECT_THREAT = 63
- BasePoints：要增加/移除的仇恨值

SPELL_EFFECT_TRIGGER_SPELL = 64
- TriggerSpell：法术 ID

SPELL_EFFECT_APPLY_AREA_AURA_RAID = 65
- BasePoints：取决于[法术光环](spell-aura-reference)
- EffectMiscValueA：未知

SPELL_EFFECT_CREATE_MANA_GEM = 66
- BasePoints：要补充的数量
- EffectItemType：要创建/补充的[物品 ID](item_template)

SPELL_EFFECT_HEAL_MAX_HEALTH = 67

SPELL_EFFECT_INTERRUPT_CAST = 68
- EffectMechanic：被中断

SPELL_EFFECT_DISTRACT = 69
- BasePoints：持续时间（秒）。

SPELL_EFFECT_PULL = 70

SPELL_EFFECT_PICKPOCKET = 71

SPELL_EFFECT_ADD_FARSIGHT = 72

SPELL_EFFECT_UNTRAIN_TALENTS = 73

SPELL_EFFECT_APPLY_GLYPH = 74
- EffectMiscValueA：来自 GlyphProperties.dbc 的 ID

SPELL_EFFECT_HEAL_MECHANICAL = 75
- BasePoints：数量

SPELL_EFFECT_SUMMON_OBJECT_WILD = 76
- EffectMiscValueA：[gameobject_template ID](gameobject_template)

SPELL_EFFECT_SCRIPT_EFFECT = 77 分配给数据库中的 [Core Script](/wiki/core-scripts#spell-scripts)。

SPELL_EFFECT_ATTACK = 78

SPELL_EFFECT_SANCTUARY = 79

SPELL_EFFECT_ADD_COMBO_POINTS = 80
- BasePoints：要添加的连击点数

SPELL_EFFECT_CREATE_HOUSE = 81

SPELL_EFFECT_BIND_SIGHT = 82

SPELL_EFFECT_DUEL = 83
- EffectMiscValueA：[gameobject_template ID](gameobject_template)（决斗旗帜）

SPELL_EFFECT_STUCK = 84

SPELL_EFFECT_SUMMON_PLAYER = 85

SPELL_EFFECT_ACTIVATE_OBJECT = 86
- EffectMiscValueA：未知

SPELL_EFFECT_GAMEOBJECT_DAMAGE = 87
- BasePoints：基础伤害

SPELL_EFFECT_GAMEOBJECT_REPAIR = 88

SPELL_EFFECT_GAMEOBJECT_SET_DESTRUCTION_STATE = 89
- EffectMiscValueA：状态

| ID | State      |
| -- | ---------- |
| 0  | Intact     |
| 1  | Damaged    |
| 2  | Destroyed  |
| 3  | Rebuilding |

SPELL_EFFECT_KILL_CREDIT = 90
- EffectMiscValueA：[生物 ID](creature_template)

SPELL_EFFECT_THREAT_ALL = 91 // 未使用

SPELL_EFFECT_ENCHANT_HELD_ITEM = 92
- EffectMiscValueA：来自 SpellItemEnchantment.dbc 的 ID

SPELL_EFFECT_FORCE_DESELECT = 93

SPELL_EFFECT_SELF_RESURRECT = 94
- BasePoints：正数 = 百分比，负数 = 固定值
- EffectMiscValueA：法力（固定值）

SPELL_EFFECT_SKINNING = 95

SPELL_EFFECT_CHARGE = 96

SPELL_EFFECT_CAST_BUTTON = 97 （自 3.2.2a 起为图腾条）
- EffectMiscValueA：图腾组合 = 0、4、8
- EffectMiscValueB：未知（通常为 4），可能是图腾数量

SPELL_EFFECT_KNOCK_BACK = 98
- BasePoints：距离
- EffectMiscValueA：距离

SPELL_EFFECT_DISENCHANT = 99

SPELL_EFFECT_INEBRIATE = 100
- BasePoints：醉酒值

SPELL_EFFECT_FEED_PET = 101
- BasePoints：快乐值
- TriggerSpell：法术 ID

SPELL_EFFECT_DISMISS_PET = 102

SPELL_EFFECT_REPUTATION = 103
- BasePoints：声望值
- EffectMiscValueA：来自 [faction.dbc](faction) 的 ID

SPELL_EFFECT_SUMMON_OBJECT_SLOT1 = 104
- EffectMiscValueA：[gameobject_template ID](gameobject_template)

SPELL_EFFECT_SUMMON_OBJECT_SLOT2 = 105
- EffectMiscValueA：[gameobject_template ID](gameobject_template)

SPELL_EFFECT_SUMMON_OBJECT_SLOT3 = 106
- EffectMiscValueA：[gameobject_template ID](gameobject_template)

SPELL_EFFECT_SUMMON_OBJECT_SLOT4 = 107 // 未使用

SPELL_EFFECT_DISPEL_MECHANIC = 108
- EffectMiscValueA：驱散机制

| ID | Mechanic   | ID | Mechanic   | ID | Mechanic        |
| -- | ---------- | -- | ---------- | -- | --------------- |
| 0  | None       | 11 | Snare      | 22 | Infected        |
| 1  | Charm      | 12 | Stun       | 23 | Turn            |
| 2  | Disorient  | 13 | Freeze     | 24 | Horror          |
| 3  | Disarm     | 14 | Knockout   | 25 | Invulnerability |
| 4  | Distract   | 15 | Bleed      | 26 | Interrupt       |
| 5  | Fear       | 16 | Bandage    | 27 | Daze            |
| 6  | Grip       | 17 | Polymorph  | 28 | Discovery       |
| 7  | Root       | 18 | Banish     | 29 | immunity shield |
| 8  | Slow       | 19 | Shield     | 30 | All powers      |
| 9  | Silence    | 20 | Shackle    | 31 | Sap             |
| 10 | Sleep      | 21 | Mount      | 31 | Enrage          |

SPELL_EFFECT_RESURRECT_PET = 109
- BasePoints：要治疗的基础生命值百分比

SPELL_EFFECT_DESTROY_ALL_TOTEMS = 110
- BasePoints：法力返还百分比

SPELL_EFFECT_DURABILITY_DAMAGE = 111
- BasePoints：正数 = 耐久度损失，负数 = 耐久度恢复
- EffectMiscValueA：未知

SPELL_EFFECT_112 = 112 // 未使用

SPELL_EFFECT_RESURRECT_NEW = 113
- BasePoints：要恢复的生命值（固定值）
- EffectMiscValueA：法力（固定值）

SPELL_EFFECT_ATTACK_ME = 114

SPELL_EFFECT_DURABILITY_DAMAGE_PCT = 115
- BasePoints：耐久度损失百分比
- EffectMiscValueA：未知

SPELL_EFFECT_SKIN_PLAYER_CORPSE = 116

SPELL_EFFECT_SPIRIT_HEAL = 117
- BasePoints：生命值百分比

SPELL_EFFECT_SKILL = 118
- BasePoints：未知
- EffectMiscValueA：[技能 ID](skillline)

SPELL_EFFECT_APPLY_AREA_AURA_PET = 119
- BasePoints：取决于[法术光环](spell-aura-reference)

SPELL_EFFECT_TELEPORT_GRAVEYARD = 120

SPELL_EFFECT_NORMALIZED_WEAPON_DMG = 121
- BasePoints：基础伤害
- Chain Target：额外目标

SPELL_EFFECT_122 = 122 // 未使用

SPELL_EFFECT_SEND_TAXI = 123
- EffectMiscValueA：来自 TaxiPath.dbc 的 ID

SPELL_EFFECT_PULL_TOWARDS = 124
- EffectMiscValueA：拉拽速度

SPELL_EFFECT_MODIFY_THREAT_PERCENT = 125
- BasePoints：仇恨百分比

SPELL_EFFECT_STEAL_BENEFICIAL_BUFF = 126
- BasePoints：要偷取的增益数量

SPELL_EFFECT_PROSPECTING = 127

SPELL_EFFECT_APPLY_AREA_AURA_FRIEND = 128
- BasePoints：取决于[法术光环](spell-aura-reference)

SPELL_EFFECT_APPLY_AREA_AURA_ENEMY = 129
- BasePoints：取决于[法术光环](spell-aura-reference)

SPELL_EFFECT_REDIRECT_THREAT = 130
- BasePoints：要转移的仇恨百分比
- TargetB：仇恨转移的目标单位

SPELL_EFFECT_PLAY_SOUND = 131
- EffectMiscValueA：来自 SoundEntries.dbc 的 ID

SPELL_EFFECT_PLAY_MUSIC = 132
- EffectMiscValueA：来自 SoundEntries.dbc 的 ID

SPELL_EFFECT_UNLEARN_SPECIALIZATION = 133
- TriggerSpell：法术 ID

SPELL_EFFECT_KILL_CREDIT2 = 134
- EffectMiscValueA：[生物 ID](creature_template)

SPELL_EFFECT_CALL_PET = 135

SPELL_EFFECT_HEAL_PCT = 136
- BasePoints：治疗百分比

SPELL_EFFECT_ENERGIZE_PCT = 137
- BasePoints：恢复百分比
- EffectMiscValueA：能量类型（与效果 30 相同）

SPELL_EFFECT_LEAP_BACK = 138
- BasePoints：距离
- EffectMiscValueA：距离

SPELL_EFFECT_CLEAR_QUEST = 139
- BasePoints：要清除的第二个任务 ID（例如法术 ID 56518）
- EffectMiscValueA：任务 ID

SPELL_EFFECT_FORCE_CAST = 140
- TriggerSpell：法术 ID

SPELL_EFFECT_FORCE_CAST_WITH_VALUE = 141
- BasePoints：触发法术的值
- TriggerSpell：法术 ID

SPELL_EFFECT_TRIGGER_SPELL_WITH_VALUE = 142
- BasePoints：触发法术的值
- TriggerSpell：法术 ID

SPELL_EFFECT_APPLY_AREA_AURA_OWNER = 143
- BasePoints：取决于[法术光环](spell-aura-reference)

SPELL_EFFECT_KNOCK_BACK_DEST = 144
- BasePoints：距离
- TargetB：目的地
- EffectMiscValueA：距离

SPELL_EFFECT_PULL_TOWARDS_DEST = 145 （黑洞效果）
- EffectMiscValueA：距离

SPELL_EFFECT_ACTIVATE_RUNE = 146
- BasePoints：要激活的符文数量（1 或 2）
- EffectMiscValueA：符文类型

SPELL_EFFECT_QUEST_FAIL = 147
- EffectMiscValueA：任务 ID

SPELL_EFFECT_TRIGGER_MISSILE_SPELL_WITH_VALUE = 148
- BasePoints：值
- TriggerSpell：法术 ID

SPELL_EFFECT_CHARGE_DEST = 149

SPELL_EFFECT_QUEST_START = 150
- EffectMiscValueA：任务 ID

SPELL_EFFECT_TRIGGER_SPELL_2 = 151
- TriggerSpell：法术 ID

SPELL_EFFECT_SUMMON_RAF_FRIEND = 152
- TriggerSpell：法术 ID（召唤）

SPELL_EFFECT_CREATE_TAMED_PET = 153
- EffectMiscValueA：[生物 ID](creature_template)

SPELL_EFFECT_DISCOVER_TAXI = 154
- EffectMiscValueA：来自 TaxiNodes.dbc 的 ID

SPELL_EFFECT_TITAN_GRIP = 155
- EffectMiscValueA：法术 ID

SPELL_EFFECT_ENCHANT_ITEM_PRISMATIC = 156

SPELL_EFFECT_CREATE_ITEM_2 = 157
- EffectItemType：要转化的[物品 ID](item_template)
- EffectMiscValueA：未知

SPELL_EFFECT_MILLING = 158
- BasePoints：要研磨的药草数量。

SPELL_EFFECT_ALLOW_RENAME_PET = 159

SPELL_EFFECT_160 = 160

SPELL_EFFECT_TALENT_SPEC_COUNT = 161
- BasePoints：激活的天赋专精数量

SPELL_EFFECT_TALENT_SPEC_SELECT = 162
- BasePoints：要激活的天赋专精 ID

SPELL_EFFECT_163 = 163 // 未使用

SPELL_EFFECT_REMOVE_AURA = 164
- BasePoints：要移除的法术 ID 2
- TriggerSpell：要移除的法术 ID

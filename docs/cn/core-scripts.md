---
tableofcontents: 1
---

# 核心脚本

在处理生物（Creature）、游戏对象（GameObject）、法术（Spell）和副本（Instance）脚本时，我们应该始终使用在[此提交](https://github.com/azerothcore/azerothcore-wotlk/commit/430fa147fd340223400f6df968d0726510bb1c99)和[此提交](https://github.com/azerothcore/azerothcore-wotlk/commit/8cc47ab1f174e82d74b2e17b4af13ded0f37a693)中引入的新注册宏。

## 生物脚本

### 世界刷新的生物

```cpp
struct npc_scripted_creature : public CreatureAI
{
public:
    npc_scripted_creature(Creature* creature) : CreatureAI(creature) { }

    void EnterCombat(Unit* /*who*/) override
    {
        /* 一些代码 */
    }
}

/* 在脚本文件的末尾，你会找到注册所有脚本的位置。 */
void AddSC_scripts()
{
    /* RegisterCreatureAI(creatureScript); */
    RegisterCreatureAI(npc_scripted_creature);
}
```

### 副本内刷新的生物

如果生物是在副本（instance）内编写脚本的，我们将它们注册为工厂（factory）。

为此，在副本的头文件中添加如下定义：

```cpp
#define Register"IntanceName"CreatureAI(ai_name) RegisterCreatureAIWithFactory(ai_name, Get"InstanceName"AI)

/* 来自 icecrown_citadel.h 的示例 */
#define RegisterIcecrownCitadelCreatureAI(ai_name) RegisterCreatureAIWithFactory(ai_name, GetIcecrownCitadelAI)
```

在脚本文件中注册方式如下：

```cpp
/* 来自 boss_lord_marrowgar.cpp 的示例 */
struct boss_lord_marrowgar : public BossAI
{
public:
    boss_lord_marrowgar(Creature* creature) : BossAI(creature, DATA_LORD_MARROWGAR) { }

    void EnterCombat(Unit* /*who*/) override
    {
        /* 一些代码 */
    }
}

void AddSC_boss_lord_marrowgar()
{
    /* RegisterIcecrownCitadelCreatureAI(creatureScript); */
    RegisterIcecrownCitadelCreatureAI(boss_lord_marrowgar);
}
```

### 不同类型的生物 AI

| 名称            |
| --------------- |
| CreatureAI      |
| BossAI          |
| GuardianAI      |
| PetAI           |
| NullCreatureAI  |

## 游戏对象脚本

### 世界刷新的游戏对象

```cpp
struct go_scripted_gameobject : public GameObjectAI
{
    go_scripted_gameobject(GameObject* go) : GameObjectAI(go) { }

    void UpdateAI(uint32 const /*diff*/) override
    {
        /* 一些代码 */
    }
}

/* 在脚本文件的末尾，你会找到注册所有脚本的位置。 */
void AddSC_scripts()
{
    /* RegisterGameObjectAI(gameObjectScript); */
    RegisterGameObjectAI(go_scripted_gameobject);
}
```

### 副本内刷新的游戏对象

如果游戏对象是在副本（instance）内编写脚本的，我们将它们注册为工厂（factory）。

为此，在副本的头文件中添加如下定义：

```cpp
#define Register"IntanceName"GameObjectAI(ai_name) RegisterGameObjectAIWithFactory(ai_name, Get"InstanceName"AI)
```

## 法术脚本

### 脚本中使用法术的验证

在脚本中使用的法术**应始终**在脚本顶部进行验证。

这样可以防止我们在脚本中尝试使用不存在的法术时可能导致的崩溃。

```cpp
class spell_pri_power_word_shield_aura : public AuraScript
{
    PrepareAuraScript(spell_pri_power_word_shield_aura);

    bool Validate(SpellInfo const* /*spellInfo*/) override
    {
        return ValidateSpellInfo({ SPELL_1, SPELL_2 });
    }
}
```

### 独立的 SpellScript 和 AuraScript

对于不需要任何参数、只要在数据库中分配好即可生效的独立 SpellScript 和 AuraScript，处理方式如下：

```cpp
class spell_pri_shadow_word_death : public SpellScript
{
public:
    PrepareSpellScript(spell_pri_shadow_word_death);

    void HandleDamage()
    {
        /* 一些代码 */
    }

    void Register() override
    {
        OnHit += SpellHitFn(spell_pri_shadow_word_death::HandleDamage);
    }
}

void AddSC_priest_spell_scripts()
{
    /* RegisterSpellScript(spell/auraScript); */
    RegisterSpellScript(spell_pri_shadow_word_death);
}
```

### 法术与光环脚本配对

对于成对出现的 SpellScript 和 AuraScript，我们分别编写脚本，然后在注册时将它们关联起来。

当两个脚本要关联时，它们始终共享相同的名称。因此，在这种情况下，我们总是为 AuraScript 添加 \_aura 后缀。

```cpp
class spell_pri_power_word_shield_aura : public AuraScript
{
    PrepareAuraScript(spell_pri_power_word_shield_aura);

    bool Validate(SpellInfo const* /*spellInfo*/) override
    {
        return ValidateSpellInfo({ SPELL_1 });
    }

    void CalculateAmount(AuraEffect const* aurEff, int32& amount, bool& canBeRecalculated)
    {
        /* 一些代码 */
    }

    void Register() override
    {
        DoEffectCalcAmount += AuraEffectCalcAmountFn(spell_pri_power_word_shield_aura::CalculateAmount, EFFECT_0, SPELL_AURA_SCHOOL_ABSORB);
    }
}

class spell_pri_power_word_shield : public SpellScript
{
    PrepareSpellScript(spell_pri_power_word_shield);

    SpellCastResult CheckCast()
    {
        /* 一些代码 */
    }

    void Register() override
    {
        OnCheckCast += SpellCheckCastFn(spell_pri_power_word_shield::CheckCast);
    }
}

void AddSC_priest_spell_scripts()
{
    /* 我们使用 RegisterSpellAndAuraScriptPair 将两个脚本关联起来。
     * RegisterSpellAndAuraScriptPair(spellScript, auraScript) */
    RegisterSpellAndAuraScriptPair(spell_pri_power_word_shield, spell_pri_power_word_shield_aura);
}
```

### 带参数的法术脚本

有时我们会编写更通用的 SpellScript，然后在注册时为其分配并传入其他参数。

```cpp
class spell_item_defibrillate : public SpellScript
{
    PrepareSpellScript(spell_item_defibrillate);

public:
    spell_item_defibrillate(uint8 chance, uint32 failSpell = 0) : SpellScript(), _chance(chance), _failSpell(failSpell) { }

    void HandleScript(SpellEffIndex effIndex)
    {
        /* 一些代码 */
    }

    void Register() override
    {
        OnEffectHitTarget += SpellEffectFn(spell_item_defibrillate::HandleScript, EFFECT_0, SPELL_EFFECT_RESURRECT);
    }
}

void AddSC_item_spell_scripts()
{
    /* RegisterSpellScriptWithArgs(spellScript, scriptName, args...); */
    RegisterSpellScriptWithArgs(spell_item_defibrillate, "spell_item_goblin_jumper_cables", 67, SPELL_GOBLIN_JUMPER_CABLES_FAIL);
    RegisterSpellScriptWithArgs(spell_item_defibrillate, "spell_item_goblin_jumper_cables_xl", 50, SPELL_GOBLIN_JUMPER_CABLES_XL_FAIL);
    RegisterSpellScriptWithArgs(spell_item_defibrillate, "spell_item_gnomish_army_knife", 33);
}
```

## 副本脚本

```cpp
#define RegisterInstanceScript(script_name, mapId) new GenericInstanceMapScript<script_name>(#script_name, mapId)
```

示例：
```cpp
// instance.cpp
class instance_instance_script : public InstanceScript
{
public:
    instance_instance_script(Map* map) : InstanceScript(map) { }

    void SomeFunction(uint32 /*var*/)
    {
        /* 一些代码 */
    }
}

void AddSC_instance()
{
    /* RegisterInstanceScript(script_name, mapId); */
    RegisterInstanceScript(instance_instance_script, 533);
}
```

## 在数据库中分配脚本

所有脚本都在世界数据库（world database）中分配。

### 生物脚本

生物脚本可以在两个表中分配。

| 表                | 列          |
| ----------------- | ----------- |
| creature_template | ScriptName  |
| creature          | ScriptName  |

在 **creature_template** 中，我们将脚本分配给生物 entry，这意味着所有使用该 entry 刷新的生物都会使用此脚本。

在 **creature** 中，我们将脚本分配给生物的 GUID，这意味着该特定的刷新点会使用此脚本。

**ScriptName** 与核心中分配的脚本名称一致。例如 *boss_lord_marrowgar*。

### 法术脚本

法术脚本在单个表中分配。

| 表                  | 列1       | 列2        |
| ------------------- | --------- | ---------- |
| spell_script_names  | spell_id  | ScriptName |

**spell_id** 是你要为其分配脚本的法术 ID。一个法术 ID 可以分配多个脚本。

**ScriptName** 取决于你使用的注册方式类型。一个 ScriptName 可以分配给多个法术。

| 注册方式                                                    | ScriptName  |
| ----------------------------------------------------------- | ----------- |
| RegisterSpellScript(spellScript)                            | spellScript |
| RegisterSpellAndAuraScriptPair(spellScript, auraScript)     | spellScript |
| RegisterSpellScriptWithArgs(spellScript, scriptName, args...) | scriptName  |

#### SQL 部分

由于一个脚本可以分配给多个法术，我们**始终**希望同时删除 spell_id 和 ScriptName，以避免影响其他法术。

```sql
DELETE FROM `spell_script_names` WHERE `spell_id` = 1 AND `ScriptName` = 'spell_pri_death_touch';
```

唯一可以只删除 ScriptName 的情况是当我们在核心中删除或添加新脚本时。

### 副本脚本

| 表                | 列    |
| ----------------- | ----- |
| instance_template | script |

在 **instance_template** 中，我们将脚本分配给副本的地图 ID。

**script** 与分配给副本的名称一致。例如 *instance_instance_script*。

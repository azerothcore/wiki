---
tableofcontents: 1
---

# Core Scripts

When dealing with Creature- and Spell scripts we should always use the new registry macros introduced in [this](https://github.com/azerothcore/azerothcore-wotlk/commit/430fa147fd340223400f6df968d0726510bb1c99) commit.

## Creature Scripts

### World Spawned Creatures

```cpp
struct npc_scripted_creature : public CreatureAI
{
public:
    npc_scripted_creature(Creature* creature) : CreatureAI(creature) { }

    void EnterCombat(Unit* /*who*/) override
    {
        /* Some code */
    }
}

/* At the end of a script file you will find a place where we register all
 * the scripts. */
void AddSC_scripts()
{
    /* RegisterCreatureAI(creatureScript); */
    RegisterCreatureAI(npc_scripted_creature);
}
```

### Instance Spawned Creatures

If a creature is scripted inside an instance we register them as factory.

To do this, in the headerfile of the instance we add this define:

```cpp
#define Register"InstanceName"CreatureAI(ai_name) RegisterCreatureAIWithFactory(ai_name, Get"InstanceName"AI)

/* Example from icecrown_citadel.h */
#define RegisterIcecrownCitadelCreatureAI(ai_name) RegisterCreatureAIWithFactory(ai_name, GetIcecrownCitadelAI)
```

And within the script file it would be registered like this:

```cpp
/* Example from boss_lord_marrowgar.cpp */
struct boss_lord_marrowgar : public BossAI
{
public:
    boss_lord_marrowgar(Creature* creature) : BossAI(creature, DATA_LORD_MARROWGAR) { }

    void EnterCombat(Unit* /*who*/) override
    {
        /* Some code */
    }
}

void AddSC_boss_lord_marrowgar()
{
    /* RegisterIcecrownCitadelCreatureAI(creatureScript); */
    RegisterIcecrownCitadelCreatureAI(boss_lord_marrowgar);
}
```

### Different types of Creature AI's

| Name           |
| -------------- |
| CreatureAI     |
| BossAI         |
| GuardianAI     |
| PetAI          |
| NullCreatureAI |

## Spell Scripts

### Validation of spells used in a script

Spells used **within** the SpellScript should **always** be validated at the top of the script.

This will prevent potential crashes if we try to use a spell that doesn't exist in a script.

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

### Stand alone SpellScripts and AuraScripts

For stand alone SpellScripts and AuraScripts that do not require any args, and just work once you have assigned them in the databases are handled like below:

```cpp
class spell_pri_shadow_word_death : public SpellScript
{
public:
    PrepareSpellScript(spell_pri_shadow_word_death);

    void HandleDamage()
    {
        /* Some code */
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

### Spell- and Aurascript Pairs

For SpellScripts and AuraScripts that pair together, we script them by themselves and link them at the registry.

When two scripts are going to be linked, they will always share the same name. Therefore we always suffix the AuraScript with \_aura in these cases.

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
        /* Some code */
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
        /* Some code */
    }

    void Register() override
    {
        OnCheckCast += SpellCheckCastFn(spell_pri_power_word_shield::CheckCast);
    }
}

void AddSC_priest_spell_scripts()
{
    /* We link the two scripts together with RegisterSpellAndAuraScriptPair.
     * RegisterSpellAndAuraScriptPair(spellScript, auraScript) */
    RegisterSpellAndAuraScriptPair(spell_pri_power_word_shield, spell_pri_power_word_shield_aura);
}
```

### SpellScripts with Args

Sometimes we make more generic SpellScripts that we later assign and pass other args to in the registry.

```cpp
class spell_item_defibrillate : public SpellScript
{
    PrepareSpellScript(spell_item_defibrillate);

public:
    spell_item_defibrillate(uint8 chance, uint32 failSpell = 0) : SpellScript(), _chance(chance), _failSpell(failSpell) { }

    void HandleScript(SpellEffIndex effIndex)
    {
        /* Some code */
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

## Assigning Script in the Database

All scripts are assigned in the world database.

### CreatureScripts

CreatureScripts can be assigned in two tables.

| Table             | Column     |
| ----------------- | ---------- |
| creature_template | ScriptName |
| creature          | ScriptName |

In **creature_template** we assign the Script to the creature entry, meaning all spawned creatures with that entry will use the script.

In **creature** we assign the Script to the creature GUID, meaning that specific spawn will use the script.

The **ScriptName** is the same as the assigned script name in the core. F.ex *boss_lord_marrowgar*.

### SpellScripts

SpellScripts are assigned in one table.

| Table              | Column1  | Column2    |
| ------------------ | -------- | ---------- |
| spell_script_names | spell_id | ScriptName |

The **spell_id** is the id of the spell you want to assign a script to. One Spell id can assign multiple Scripts.

The **ScriptName** is depending on what type of registry you used. One ScriptName can be assigned to multiple spells.

| Registry                                                      | ScriptName  |
| ------------------------------------------------------------- | ----------- |
| RegisterSpellScript(spellScript)                              | spellScript |
| RegisterSpellAndAuraScriptPair(spellScript, auraScript)       | spellScript |
| RegisterSpellScriptWithArgs(spellScript, scriptName, args...) | scriptName  |

#### SQL part

As a Script can be assigned to multiple spells we **always** want to delete both the spell_id and the ScriptName to avoid messing up other spells.

```sql
DELETE FROM `spell_script_names` WHERE `spell_id` = 1 AND `ScriptName` = 'spell_pri_death_touch';
```

The only time it is okay to only delete the ScriptName is when we are deleting or adding a new script in the core.

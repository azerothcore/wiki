# Scripts básicos

Cuando se trata de scripts de criaturas y hechizos, siempre debemos utilizar las nuevas macros de registro introducidas en el commit [this](https://github.com/azerothcore/azerothcore-wotlk/commit/430fa147fd340223400f6df968d0726510bb1c99).

## Creature Scripts

### Criaturas en el mundo

```cpp
struct npc_scripted_creature : public CreatureAI
{
public:
    npc_scripted_creature(Creature* creature) : CreatureAI(creature) { }

    void EnterCombat(Unit* /*who*/) override
    {
        /* Algo de código */
    }
}

/* Al final de un archivo de script encontrarás un lugar donde registramos todos los scripts. */
void AddSC_scripts()
{
    /* RegisterCreatureAI(creatureScript); */
    RegisterCreatureAI(npc_scripted_creature);
}
```

### Criaturas en la instancia

Si una criatura tiene un script dentro de una instancia la registramos como fábrica.

Para ello, en el archivo de cabecera de la instancia añadimos esta definición:

```cpp
#define Register"InstanceName"CreatureAI(ai_name) RegisterCreatureAIWithFactory(ai_name, Get"InstanceName"AI)

/* Ejemplo de icecrown_citadel.h */
#define RegisterIcecrownCitadelCreatureAI(ai_name) RegisterCreatureAIWithFactory(ai_name, GetIcecrownCitadelAI)
```

Y dentro del archivo de script se registraría así:

```cpp
/* Ejemplo de boss_lord_marrowgar.cpp */
struct boss_lord_marrowgar : public BossAI
{
public:
    boss_lord_marrowgar(Creature* creature) : BossAI(creature, DATA_LORD_MARROWGAR) { }

    void EnterCombat(Unit* /*who*/) override
    {
        /* Algo de código */
    }
}

void AddSC_boss_lord_marrowgar()
{
    /* RegisterIcecrownCitadelCreatureAI(creatureScript); */
    RegisterIcecrownCitadelCreatureAI(boss_lord_marrowgar);
}
```

### Diferentes tipos de IA de criaturas

- CreatureAI
- BossAI
- GuardianAI
- PetAI
- NullCreatureAI

## Spell Scripts

### Validación de los hechizos utilizados en un script

Los hechizos utilizados **dentro** del SpellScript deben **siempre** ser validados en la parte superior del script.

Esto evitará posibles fallos si intentamos utilizar un hechizo que no existe en un script.

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

### SpellScripts y AuraScripts independientes

Para los SpellScripts y AuraScripts independientes que no requieren ningún argumento, y que sólo funcionan una vez que los has asignado en las bases de datos, se manejan como se indica a continuación:

```cpp
class spell_pri_shadow_word_death : public SpellScript
{
public:
    PrepareSpellScript(spell_pri_shadow_word_death);

    void HandleDamage()
    {
        /* Algo de código */
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

### Pares de scripts de hechizos y auras

Para los SpellScripts y AuraScripts que se emparejan, los escribimos por sí mismos y los enlazamos en el registro.

Cuando dos scripts van a ser enlazados, siempre compartirán el mismo nombre. Por lo tanto, en estos casos siempre añadimos el sufijo \_aura al AuraScript.

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
        /* Algo de código */
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
        /* Algo de código */
    }

    void Register() override
    {
        OnCheckCast += SpellCheckCastFn(spell_pri_power_word_shield::CheckCast);
    }
}

void AddSC_priest_spell_scripts()
{
    /* Unimos los dos scripts con RegisterSpellAndAuraScriptPair.
     * RegisterSpellAndAuraScriptPair(spellScript, auraScript) */
    RegisterSpellAndAuraScriptPair(spell_pri_power_word_shield, spell_pri_power_word_shield_aura);
}
```

### SpellScripts con argumentos

A veces hacemos SpellScripts más genéricos que luego asignamos y pasamos otros argumentos en el registro.

```cpp
class spell_item_defibrillate : public SpellScript
{
    PrepareSpellScript(spell_item_defibrillate);

public:
    spell_item_defibrillate(uint8 chance, uint32 failSpell = 0) : SpellScript(), _chance(chance), _failSpell(failSpell) { }

    void HandleScript(SpellEffIndex effIndex)
    {
        /* Algo de código */
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

## Asignación de scripts en la base de datos

Todos los guiones se asignan en la base de datos `world`.

### CreatureScripts

Los CreatureScripts se pueden asignar en dos tablas.

| Table             | Column     |
| ----------------- | ---------- |
| creature_template | ScriptName |
| creature          | ScriptName |

- En **creature_template** asignamos el Script al `entry` de la criatura, lo que significa que todas las criaturas engendradas con el `entry` utilizarán el script.
- En **creature** asignamos el Script al GUID de la criatura, lo que significa que ese spawn específico utilizará el script.
- El **ScriptName** es el mismo que el nombre del script asignado en el núcleo. Por ejemplo, **boss_lord_marrowgar**.

### SpellScripts

Los SpellScripts se asignan en una tabla.

| Table              | Column1  | Column2    |
| ------------------ | -------- | ---------- |
| spell_script_names | spell_id | ScriptName |

- El **spell_id** es el id del hechizo al que quiere asignar un script. Un id de hechizo puede asignar múltiples scripts.
- El **ScriptName** depende del tipo de registro que hayas utilizado. Un ScriptName puede ser asignado a múltiples hechizos.

| Registry                                                      | ScriptName  |
| ------------------------------------------------------------- | ----------- |
| RegisterSpellScript(spellScript)                              | spellScript |
| RegisterSpellAndAuraScriptPair(spellScript, auraScript)       | spellScript |
| RegisterSpellScriptWithArgs(spellScript, scriptName, args...) | scriptName  |

#### SQL part

Como un Script puede ser asignado a múltiples hechizos, **siempre** queremos borrar tanto el spell_id como el ScriptName para evitar estropear otros hechizos.

```sql
DELETE FROM `spell_script_names` WHERE `spell_id`=1 AND `ScriptName`='spell_pri_death_touch';
```

El único momento en el que está bien borrar sólo el ScriptName es cuando estamos borrando o añadiendo un nuevo script en el núcleo.

# Spell Effects Reference

[<-Volver a: spell_dbc](spell_dbc)

### Esta página contiene la descripción del uso de EffectMiscValue y otros valores de Spell Effects.

### Contiene la lista de todos los Spell Effects.

**La versión es: 3.3.5a**

### Información relacionada
[Summon Properties](summonproperties_dbc)

[Spell Aura](spell-aura-reference)

# Nombres de Spell Effect

SPELL_EFFECT_INSTAKILL = 1

SPELL_EFFECT_SCHOOL_DAMAGE = 2
- BasePoints: Daño base
- Multiple: Multiplicador de daño

SPELL_EFFECT_DUMMY = 3
- BasePoints: Cualquier cosa

SPELL_EFFECT_PORTAL_TELEPORT = 4

SPELL_EFFECT_TELEPORT_UNITS = 5
- TargetB: Ubicación de teletransporte

SPELL_EFFECT_APPLY_AURA = 6
- BasePoints: Valor del aura (depende del Aura ID)
- EffectAura: [Spell Aura](spell-aura-reference)

SPELL_EFFECT_ENVIRONMENTAL_DAMAGE = 7
- BasePoints: Daño base

SPELL_EFFECT_POWER_DRAIN = 8
- BasePoints: Drenaje base
- Multiple: Multiplicador de drenaje

SPELL_EFFECT_HEALTH_LEECH = 9
- BasePoints: Drenaje base 
- Multiple: Multiplicador de drenaje
- TargetB: Si se usa, TargetA es curado

SPELL_EFFECT_HEAL = 10
- BasePoints: Curación base
- Multiple: Multiplicador de curación
- TargetB: Si se usa, TargetA es curado

SPELL_EFFECT_BIND = 11
- BasePoints: Desconocido
- EffectMiscValueA: Area ID (solo Death Gate)

SPELL_EFFECT_PORTAL = 12
- TargetA: Destino de teletransporte
- TargetB: Objetivos

SPELL_EFFECT_RITUAL_BASE = 13 // Sin usar

SPELL_EFFECT_RITUAL_SPECIALIZE = 14 // Sin usar

SPELL_EFFECT_RITUAL_ACTIVATE_PORTAL = 15 // Sin usar

SPELL_EFFECT_QUEST_COMPLETE = 16
- EffectMiscValueA: Quest ID
- TargetB: Objetivos adicionales (usado por 30790)

SPELL_EFFECT_WEAPON_DAMAGE_NOSCHOOL = 17
- BasePoints: Daño base

SPELL_EFFECT_RESURRECT = 18
- BasePoints: Porcentaje (%) de salud y maná restaurados
- TargetB: Objetivos adicionales (usado por 29820, resurrección masiva)

SPELL_EFFECT_ADD_EXTRA_ATTACKS = 19
- BasePoints: Número de ataques cuerpo a cuerpo extra

SPELL_EFFECT_DODGE = 20

SPELL_EFFECT_EVADE = 21

SPELL_EFFECT_PARRY = 22

SPELL_EFFECT_BLOCK = 23

SPELL_EFFECT_CREATE_ITEM = 24
- BasePoints: Número de objetos
- EffectItemType: [Item ID](item_template)

SPELL_EFFECT_WEAPON = 25

SPELL_EFFECT_DEFENSE = 26

SPELL_EFFECT_PERSISTENT_AREA_AURA = 27
- BasePoints: Depende de [Spell Aura](spell-aura-reference)

SPELL_EFFECT_SUMMON = 28
- BasePoints: Número de invocaciones (a veces se usa para establecer la HP de la criatura invocada)
- EffectMiscValueA: [Creature ID](creature_template)
- EffectMiscValueB: [Summon Properties](summonproperties_dbc)
- Radius: Rango de aparición

SPELL_EFFECT_LEAP = 29
- TargetA: Objetivo
- TargetB: Destino
- Radius: Distancia de parpadeo/salto

SPELL_EFFECT_ENERGIZE = 30
- BasePoints: Cantidad
- TargetB: Objetivos adicionales
- EffectMiscValueA: Power Type

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
- BasePoints: Porcentaje de daño base

SPELL_EFFECT_TRIGGER_MISSILE = 32
- TriggerSpell: Spell ID

SPELL_EFFECT_OPEN_LOCK = 33
- BasePoints: Nivel de habilidad de forzar cerraduras requerido

SPELL_EFFECT_SUMMON_CHANGE_ITEM = 34 // Armas como las Bendiciones
EffectItemType: Nuevo [Item ID](item_template)

SPELL_EFFECT_APPLY_AREA_AURA_PARTY = 35
- BasePoints: Depende de [Spell Aura](spell-aura-reference)

SPELL_EFFECT_LEARN_SPELL = 36
- TriggerSpell: Spell ID

SPELL_EFFECT_SPELL_DEFENSE = 37

SPELL_EFFECT_DISPEL = 38
- BasePoints: Número de hechizos a disipar
- EffectMiscValueA: Dispel Type

| ID | Type       | ID | Type         | ID | Type            |
| -- | ---------- | -- | ------------ | -- | --------------- |
| 0  | None       | 4  | Poison       | 8  | SPE_NPC_ONLY    |
| 1  | Magic      | 5  | Stealth      | 9  | Enrage          |
| 2  | Curse      | 6  | Invisibility | 10 | ZG Trinket      |
| 3  | Disease    | 7  | ALL          | 11 | Old Unseen      |

SPELL_EFFECT_LANGUAGE = 39
- EffectMiscValueA: [Language ID](languages)

SPELL_EFFECT_DUAL_WIELD = 40

SPELL_EFFECT_JUMP = 41
- Multiple: Desconocido
- EffectMiscValueA: Velocidad XY o velocidad Z
- EffectMiscValueB: Velocidad XY o velocidad Z

SPELL_EFFECT_JUMP_DEST = 42
- Multiple: Desconocido
- EffectMiscValueA: Velocidad XY o velocidad Z
- EffectMiscValueB: Velocidad XY o velocidad Z

SPELL_EFFECT_TELEPORT_UNITS_FACE_CASTER = 43
- BasePoints: Número de unidades a teletransportar

SPELL_EFFECT_SKILL_STEP = 44
- BasePoints: Desconocido
- EffectMiscValueA: [Skill ID](skillline)

SPELL_EFFECT_ADD_HONOR = 45
- BasePoints: Puntos de honor a recompensar

SPELL_EFFECT_SPAWN = 46

SPELL_EFFECT_TRADE_SKILL = 47

SPELL_EFFECT_STEALTH = 48

SPELL_EFFECT_DETECT = 49

SPELL_EFFECT_TRANS_DOOR = 50
- EffectMiscValueA: [gameobject_template ID](gameobject_template)
- El Data0 de gameobject_template es el hechizo que se vincula al destino del teletransporte al hacer click.
- Entrada Data0 = tabla spell_target_position

SPELL_EFFECT_FORCE_CRITICAL_HIT = 51 // Sin usar

SPELL_EFFECT_GUARANTEE_HIT = 52 // Sin usar

SPELL_EFFECT_ENCHANT_ITEM = 53
- EffectItemType: [Item ID](item_template) (Pergaminos/Inscripción)
- EffectMiscValueA: ID de SpellItemEnchantment.dbc
- EffectMiscValueA: 14 = armadura, 15 = arma, ligado a EffectItemType.

SPELL_EFFECT_ENCHANT_ITEM_TEMPORARY = 54
- EffectMiscValueA: ID de SpellItemEnchantment.dbc

SPELL_EFFECT_TAMECREATURE = 55

SPELL_EFFECT_SUMMON_PET = 56
- Multiple: Relativo al nivel del lanzador (p. ej. un valor de -3 será el nivel del lanzador -3). Actualmente no funciona.
- EffectMiscValueA: [Creature ID](creature_template)

SPELL_EFFECT_LEARN_PET_SPELL = 57
- TriggerSpell: Spell ID

SPELL_EFFECT_WEAPON_DAMAGE = 58
- BasePoints: Daño adicional
- TargetB: Objetivos adicionales
- Chain Target: Objetivos adicionales

SPELL_EFFECT_CREATE_RANDOM_ITEM = 59
- EffectMiscValueA: Desconocido

SPELL_EFFECT_PROFICIENCY = 60

SPELL_EFFECT_SEND_EVENT = 61
- EffectMiscValueA: Llama a un evento de la tabla acevent_scripts.\
(La mayoría no coinciden, pero hay unos pocos que son correctos.)

SPELL_EFFECT_POWER_BURN = 62
- BasePoints: Cantidad de maná a quemar
- TargetB: Objetivos adicionales
- Multiple: % de conversión a daño (p. ej. si 0.5, por 1 de maná quemado, inflige 0.5 de daño)
- Chain Target: Objetivos adicionales

SPELL_EFFECT_THREAT = 63
- BasePoints: Cantidad de amenaza a añadir/quitar

SPELL_EFFECT_TRIGGER_SPELL = 64
- TriggerSpell: Spell ID

SPELL_EFFECT_APPLY_AREA_AURA_RAID = 65
- BasePoints: Depende de [Spell Aura](spell-aura-reference)
- EffectMiscValueA: Desconocido

SPELL_EFFECT_CREATE_MANA_GEM = 66
- BasePoints: Número a rellenar
- EffectItemType: [Item ID](item_template) a crear/rellenar

SPELL_EFFECT_HEAL_MAX_HEALTH = 67

SPELL_EFFECT_INTERRUPT_CAST = 68
- EffectMechanic: Interrumpido

SPELL_EFFECT_DISTRACT = 69
- BasePoints: Duración en segundos.

SPELL_EFFECT_PULL = 70

SPELL_EFFECT_PICKPOCKET = 71

SPELL_EFFECT_ADD_FARSIGHT = 72

SPELL_EFFECT_UNTRAIN_TALENTS = 73

SPELL_EFFECT_APPLY_GLYPH = 74
- EffectMiscValueA: ID de GlyphProperties.dbc

SPELL_EFFECT_HEAL_MECHANICAL = 75
- BasePoints: Cantidad

SPELL_EFFECT_SUMMON_OBJECT_WILD = 76
- EffectMiscValueA: [gameobject_template ID](gameobject_template)

SPELL_EFFECT_SCRIPT_EFFECT = 77 Asignado a un [Core Script](/wiki/core-scripts#spell-scripts) en la BD.

SPELL_EFFECT_ATTACK = 78

SPELL_EFFECT_SANCTUARY = 79

SPELL_EFFECT_ADD_COMBO_POINTS = 80
- BasePoints: Número de puntos de combo a añadir

SPELL_EFFECT_CREATE_HOUSE = 81

SPELL_EFFECT_BIND_SIGHT = 82

SPELL_EFFECT_DUEL = 83
- EffectMiscValueA: [gameobject_template ID](gameobject_template) (Bandera de duelo)

SPELL_EFFECT_STUCK = 84

SPELL_EFFECT_SUMMON_PLAYER = 85

SPELL_EFFECT_ACTIVATE_OBJECT = 86
- EffectMiscValueA: Desconocido

SPELL_EFFECT_GAMEOBJECT_DAMAGE = 87
- BasePoints: Daño base

SPELL_EFFECT_GAMEOBJECT_REPAIR = 88

SPELL_EFFECT_GAMEOBJECT_SET_DESTRUCTION_STATE = 89
- EffectMiscValueA: State

| ID | State      |
| -- | ---------- |
| 0  | Intact     |
| 1  | Damaged    |
| 2  | Destroyed  |
| 3  | Rebuilding |

SPELL_EFFECT_KILL_CREDIT = 90
- EffectMiscValueA: [Creature ID](creature_template)

SPELL_EFFECT_THREAT_ALL = 91 // Sin usar

SPELL_EFFECT_ENCHANT_HELD_ITEM = 92
- EffectMiscValueA: ID de SpellItemEnchantment.dbc

SPELL_EFFECT_FORCE_DESELECT = 93

SPELL_EFFECT_SELF_RESURRECT = 94
- BasePoints: Positivo = %, Negativo = Valor plano
- EffectMiscValueA: Maná (Valor plano)

SPELL_EFFECT_SKINNING = 95

SPELL_EFFECT_CHARGE = 96

SPELL_EFFECT_CAST_BUTTON = 97 (Barra de tótems desde 3.2.2a)
- EffectMiscValueA: Combinaciones de tótems = 0,4,8
- EffectMiscValueB: Desconocido (siempre 4), posiblemente la cantidad de tótems

SPELL_EFFECT_KNOCK_BACK = 98
- BasePoints: Distancia
- EffectMiscValueA: Distancia

SPELL_EFFECT_DISENCHANT = 99

SPELL_EFFECT_INEBRIATE = 100
- BasePoints: Poder de embriaguez

SPELL_EFFECT_FEED_PET = 101
- BasePoints: Cantidad de felicidad (Happiness)
- TriggerSpell: Spell ID

SPELL_EFFECT_DISMISS_PET = 102

SPELL_EFFECT_REPUTATION = 103
- BasePoints: Cantidad de reputación
- EffectMiscValueA: ID de [faction.dbc](faction)

SPELL_EFFECT_SUMMON_OBJECT_SLOT1 = 104
- EffectMiscValueA: [gameobject_template ID](gameobject_template) 

SPELL_EFFECT_SUMMON_OBJECT_SLOT2 = 105
- EffectMiscValueA: [gameobject_template ID](gameobject_template) 

SPELL_EFFECT_SUMMON_OBJECT_SLOT3 = 106
- EffectMiscValueA: [gameobject_template ID](gameobject_template) 

SPELL_EFFECT_SUMMON_OBJECT_SLOT4 = 107 // Sin usar

SPELL_EFFECT_DISPEL_MECHANIC = 108
- EffectMiscValueA: Dispel Mechanic

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
- BasePoints: % de salud base a curar

SPELL_EFFECT_DESTROY_ALL_TOTEMS = 110
- BasePoints: % de reembolso de maná

SPELL_EFFECT_DURABILITY_DAMAGE = 111
- BasePoints: Positivo = daño de durabilidad, Negativo = restauración de durabilidad
- EffectMiscValueA: Desconocido

SPELL_EFFECT_112 = 112 // Sin usar

SPELL_EFFECT_RESURRECT_NEW = 113
- BasePoints: Salud a restaurar (Valor plano)
- EffectMiscValueA: Maná (Valor plano)

SPELL_EFFECT_ATTACK_ME = 114

SPELL_EFFECT_DURABILITY_DAMAGE_PCT = 115
- BasePoints: % de daño de durabilidad
- EffectMiscValueA: Desconocido

SPELL_EFFECT_SKIN_PLAYER_CORPSE = 116

SPELL_EFFECT_SPIRIT_HEAL = 117
- BasePoints: % de salud

SPELL_EFFECT_SKILL = 118
- BasePoints: Desconocido
- EffectMiscValueA: [Skill ID](skillline)

SPELL_EFFECT_APPLY_AREA_AURA_PET = 119
- BasePoints: Depende de [Spell Aura](spell-aura-reference)

SPELL_EFFECT_TELEPORT_GRAVEYARD = 120

SPELL_EFFECT_NORMALIZED_WEAPON_DMG = 121
- BasePoints: Daño base
- Chain Target: Objetivos adicionales

SPELL_EFFECT_122 = 122 // Sin usar

SPELL_EFFECT_SEND_TAXI = 123
- EffectMiscValueA: ID de TaxiPath.dbc

SPELL_EFFECT_PULL_TOWARDS = 124
- EffectMiscValueA: Velocidad del tirón

SPELL_EFFECT_MODIFY_THREAT_PERCENT = 125
- BasePoints: % de amenaza

SPELL_EFFECT_STEAL_BENEFICIAL_BUFF = 126
- BasePoints: Número de buffs a robar

SPELL_EFFECT_PROSPECTING = 127

SPELL_EFFECT_APPLY_AREA_AURA_FRIEND = 128
- BasePoints: Depende de [Spell Aura](spell-aura-reference)

SPELL_EFFECT_APPLY_AREA_AURA_ENEMY = 129
- BasePoints: Depende de [Spell Aura](spell-aura-reference)

SPELL_EFFECT_REDIRECT_THREAT = 130
- BasePoints: % de amenaza a redirigir
- TargetB: Unidad a la que redirigir la amenaza 

SPELL_EFFECT_PLAY_SOUND = 131
- EffectMiscValueA: ID de SoundEntries.dbc

SPELL_EFFECT_PLAY_MUSIC = 132
- EffectMiscValueA: ID de SoundEntries.dbc

SPELL_EFFECT_UNLEARN_SPECIALIZATION = 133
- TriggerSpell: Spell ID

SPELL_EFFECT_KILL_CREDIT2 = 134
- EffectMiscValueA: [Creature ID](creature_template)

SPELL_EFFECT_CALL_PET = 135

SPELL_EFFECT_HEAL_PCT = 136
- BasePoints: % de curación

SPELL_EFFECT_ENERGIZE_PCT = 137
- BasePoints: % a restaurar
- EffectMiscValueA: Power Type (igual que EFFECT 30)

SPELL_EFFECT_LEAP_BACK = 138
- BasePoints: Distancia
- EffectMiscValueA: Distancia

SPELL_EFFECT_CLEAR_QUEST = 139
- BasePoints: 2.º Quest ID a limpiar (p. ej. Spell ID 56518)
- EffectMiscValueA: Quest ID

SPELL_EFFECT_FORCE_CAST = 140
- TriggerSpell: Spell ID

SPELL_EFFECT_FORCE_CAST_WITH_VALUE = 141
- BasePoints: Valor para el TriggerSpell 
- TriggerSpell: Spell ID

SPELL_EFFECT_TRIGGER_SPELL_WITH_VALUE = 142
- BasePoints: Valor para el TriggerSpell 
- TriggerSpell: Spell ID

SPELL_EFFECT_APPLY_AREA_AURA_OWNER = 143
- BasePoints: Depende de [Spell Aura](spell-aura-reference)

SPELL_EFFECT_KNOCK_BACK_DEST = 144
- BasePoints: Distancia
- TargetB: Destino
- EffectMiscValueA: Distancia

SPELL_EFFECT_PULL_TOWARDS_DEST = 145 (Efecto Agujero Negro)
- EffectMiscValueA: Distancia

SPELL_EFFECT_ACTIVATE_RUNE = 146
- BasePoints: Número de runas a activar (1 o 2)
- EffectMiscValueA: Rune Type

SPELL_EFFECT_QUEST_FAIL = 147
- EffectMiscValueA: Quest ID

SPELL_EFFECT_TRIGGER_MISSILE_SPELL_WITH_VALUE = 148
- BasePoints: Valor
- TriggerSpell: Spell ID

SPELL_EFFECT_CHARGE_DEST = 149

SPELL_EFFECT_QUEST_START = 150
- EffectMiscValueA: Quest ID

SPELL_EFFECT_TRIGGER_SPELL_2 = 151
- TriggerSpell: Spell ID

SPELL_EFFECT_SUMMON_RAF_FRIEND = 152
- TriggerSpell: Spell ID (Invocación)

SPELL_EFFECT_CREATE_TAMED_PET = 153
- EffectMiscValueA: [Creature ID](creature_template)

SPELL_EFFECT_DISCOVER_TAXI = 154
- EffectMiscValueA: ID de TaxiNodes.dbc

SPELL_EFFECT_TITAN_GRIP = 155
- EffectMiscValueA: Spell ID

SPELL_EFFECT_ENCHANT_ITEM_PRISMATIC = 156

SPELL_EFFECT_CREATE_ITEM_2 = 157
- EffectItemType: [Item ID](item_template) a transformar
- EffectMiscValueA: Desconocido

SPELL_EFFECT_MILLING = 158
- BasePoints: Número de hierbas a moler.

SPELL_EFFECT_ALLOW_RENAME_PET = 159

SPELL_EFFECT_160 = 160

SPELL_EFFECT_TALENT_SPEC_COUNT = 161
- BasePoints: Número de especializaciones de talentos activas

SPELL_EFFECT_TALENT_SPEC_SELECT = 162
- BasePoints: Talent spec ID a activar

SPELL_EFFECT_163 = 163 // Sin usar

SPELL_EFFECT_REMOVE_AURA = 164
- BasePoints:  Spell ID a eliminar 2
- TriggerSpell: Spell ID a eliminar

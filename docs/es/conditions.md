# conditions

[<-Volver a: World](database-world)

**Tabla \`conditions\`**

Esta tabla te permite definir condiciones para varios sistemas: Gossip, loot, etc.

**Estructura**

| Field                                                 | Type               | Null | Key | Default | Extra | Comment                                                                          |
| ----------------------------------------------------- | ------------------ | ---- | --- | ------- | ----- | -------------------------------------------------------------------------------- |
| [SourceTypeOrReferenceId](#sourcetypeorreferenceid)   | MEDIUMINT SIGNED   | NO   | PRI | 0       |       |                                                                                  |
| [SourceGroup](#sourcegroup)                           | MEDIUMINT UNSIGNED | NO   | PRI | 0       |       |                                                                                  |
| [SourceEntry](#sourceentry)                           | MEDIUMINT SIGNED   | NO   | PRI | 0       |       |                                                                                  |
| [SourceId](#condition_source_type_smart_event=22)     | INT SIGNED         | NO   | PRI | 0       |       | [smart_scripts.source_type](smart_scripts#sourcetype) \|\| 0 for everything else |
| [ElseGroup](#elsegroup)                               | MEDIUMINT UNSIGNED | NO   | PRI | 0       |       |                                                                                  |
| [ConditionTypeOrReference](#conditiontypeorreference) | MEDIUMINT SIGNED   | NO   | PRI | 0       |       |                                                                                  |
| [ConditionTarget](#conditiontarget)                   | TINYINT UNSIGNED   | NO   | PRI | 0       |       |                                                                                  |
| [ConditionValue1](#conditionvalue1)                   | INT UNSIGNED       | NO   | PRI | 0       |       |                                                                                  |
| [ConditionValue2](#conditionvalue2)                   | INT UNSIGNED       | NO   | PRI | 0       |       |                                                                                  |
| [ConditionValue3](#conditionvalue3)                   | INT UNSIGNED       | NO   | PRI | 0       |       |                                                                                  |
| [NegativeCondition](#negativecondition)               | TINYINT UNSIGNED   | NO   |     | 0       |       | Boolean 0 or 1 (if [NegativeCondition](#negativecondition))                      |
| [ErrorType](#errortype)                               | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                                                                  |
| [ErrorTextId](#errortextid)                           | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                                                                  |
| [ScriptName](#scriptname)                             | char(64) SIGNED    | NO   |     | ' '     |       |                                                                                  |
| [Comment](#comment)                                   | VARCHAR(255)       | YES  |     | NULL    |       |                                                                                  |

**Descripción de los campos**

### SourceTypeOrReferenceId

Si es negativo, entonces es una plantilla de referencia.

| SourceTypeOrReferenceId                           | ID  | SourceGroup                                                                               | SourceEntry                                                                         | [SourceId](conditions#condition_source_type_smart_event=22)        | ConditionTarget                                                                                                              | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------- | --- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CONDITION_SOURCE_TYPE_NONE                        | 0   | **[See REFERENCE TEMPLATES](#referencetemplates)**                                        | (REFERENCE TEMPLATES)                                                               | Always 0                                                           | (See below)                                                                                                                  | **Only used in [Reference Templates! See below.](#referencetemplates)**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| CONDITION_SOURCE_TYPE_CREATURE_LOOT_TEMPLATE      | 1   | [creature_loot_template.Entry or reference_loot_template.Entry](loot_template#entry)      | item id [_loot_template.Item or reference_loot_template.Item)](loot_template#item)  | Always 0                                                           | Always 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_DISENCHANT_LOOT_TEMPLATE    | 2   | [disenchant_loot_template.Entry or reference_loot_template.Entry](loot_template#entry)    | item id [_loot_template.Item or reference_loot_template.Item)](loot_template#item)  | Always 0                                                           | Always 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_FISHING_LOOT_TEMPLATE       | 3   | [fishing_loot_template.Entry or reference_loot_template.Entry](loot_template#entry)       | item id [_loot_template.Item or reference_loot_template.Item)](loot_template#item)  | Always 0                                                           | Always 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_GAMEOBJECT_LOOT_TEMPLATE    | 4   | [gameobject_loot_template.Entry or reference_loot_template.Entry](loot_template#entry)    | item id [_loot_template.Item or reference_loot_template.Item)](loot_template#item)  | Always 0                                                           | Always 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_ITEM_LOOT_TEMPLATE          | 5   | [item_loot_template.Entry or reference_loot_template.Entry](loot_template#entry)          | item id [_loot_template.Item or reference_loot_template.Item)](loot_template#item)  | Always 0                                                           | Always 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_MAIL_LOOT_TEMPLATE          | 6   | [mail_loot_template.Entry or reference_loot_template.Entry](loot_template#entry)          | item id [_loot_template.Item or reference_loot_template.Item)](loot_template#item)  | Always 0                                                           | Always 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_MILLING_LOOT_TEMPLATE       | 7   | [milling_loot_template.Entry or reference_loot_template.Entry](loot_template#entry)       | item id [_loot_template.Item or reference_loot_template.Item)](loot_template#item)  | Always 0                                                           | Always 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_PICKPOCKETING_LOOT_TEMPLATE | 8   | [pickpocketing_loot_template.Entry or reference_loot_template.Entry](loot_template#entry) | item id [_loot_template.Item or reference_loot_template.Item)](loot_template#item)  | Always 0                                                           | Always 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_PROSPECTING_LOOT_TEMPLATE   | 9   | [prospecting_loot_template.Entry or reference_loot_template.Entry](loot_template#entry)   | item id [_loot_template.Item or reference_loot_template.Item)](loot_template#item)  | Always 0                                                           | Always 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_REFERENCE_LOOT_TEMPLATE     | 10  | [reference_loot_template.Entry](loot_template#entry)                                      | item id [_loot_template.Item or reference_loot_template.Item)](loot_template#item)  | Always 0                                                           | Always 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_SKINNING_LOOT_TEMPLATE      | 11  | [skinning_loot_template.Entry or reference_loot_template.Entry](loot_template#entry)      | item id ([_loot_template.Item or reference_loot_template.Item)](loot_template#item) | Always 0                                                           | Always 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_SPELL_LOOT_TEMPLATE         | 12  | [spell_loot_template.Entry or reference_loot_template.Entry](loot_template#entry)         | item id ([_loot_template.Item or reference_loot_template.Item)](loot_template#item) | Always 0                                                           | Always 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_SPELL_IMPLICIT_TARGET       | 13  | Mask of effects to be affected by condition:<br>1 = EFFECT_0, 2 = EFFECT_1, 4 = EFFECT_2  | Spell Id from [Spell.dbc](Spell)                                                    | Always 0                                                           | 0 : Potential spell Target<br>1 : spell Caster                                                                               | Don't use wowhead to get number of effects, data from wowhead sometimes doesn't match real effect number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| CONDITION_SOURCE_TYPE_GOSSIP_MENU                 | 14  | [gossip_menu.MenuID](gossip_menu#menuid)                                                  | [gossip_menu.TextID](gossip_menu#textid) (points to npc_text.ID)                    | Always 0                                                           | 0 = Player<br>1 = WorldObject                                                                                                | The core iterates over all TextIDs for that menu from smallest to largest and keeps overwriting TextID when conditions pass, so the last matching row wins.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| CONDITION_SOURCE_TYPE_GOSSIP_MENU_OPTION          | 15  | [gossip_menu_option.MenuID](gossip_menu_option#menuid)                                    | [gossip_menu_option.OptionID](gossip_menu_option#optionid)                          | Always 0                                                           | 0 = Player<br>1 = WorldObject                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_CREATURE_TEMPLATE_VEHICLE   | 16  | Always 0                                                                                  | creature entry ([creature_template.entry](creature_template#entry))                 | Always 0                                                           | 0 = Player riding vehicle<br>1 = Vehicle creature                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_SPELL                       | 17  | Always 0                                                                                  | Spell ID from [Spell.dbc](Spell)                                                    | Always 0                                                           | 0 = spell Caster<br>1 = Explicit Target of the spell (only for spells which take the object selected by caster into account) | This source type allows you to define caster/explicit target requirements for spell to be cast.<br>Explicit target of the spell is the target which is selected by player during cast, not all spells take that target into account. non-explicit targets of the spell (the ones which are selected by spell like area or nearby targets for example) are not affected by this condition source type, if you want to affect those use CONDITION_SOURCE_TYPE_SPELL_IMPLICIT_TARGET instead.<br>If you are looking for old CONDITION_SOURCE_TYPE_ITEM_REQUIRED_TARGET, use this condition source type instead (ConditionTarget = 1 allows you to set requirements for a given spell, so to use this condition type you need spellid of the spell cast on item use).<br>Remember that conditions with the same ElseGroup value will be used to make logical AND check, so to allow different targets for the same spell effect you have to set ElseGroup respectively. |
| CONDITION_SOURCE_TYPE_SPELL_CLICK_EVENT           | 18  | creature entry ([npc_spellclick_spells.npc_entry](npc_spellclick_spells#npcentry))        | Spell ([npc_spellclick_spells.spell_id](npc_spellclick_spells#spellid))             | Always 0                                                           | 0 = Clicker<br>1 = Spellclick target (clickee)                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_QUEST_AVAILABLE             | 19  | Always 0                                                                                  | [Quest ID](quest_template#id)                                                       | Always 0                                                           | Always 0                                                                                                                     | Condition must be met for quest to be available to player.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| CONDITION_SOURCE_TYPE_GOSSIP_HELLO                | 20  | Always 0                                                                                  | creature entry ([creature_template.entry](creature_template#entry))                 | Always 0                                                           | 0 = Player<br>1 = WorldObject                                                                                                | Prevents opening the gossip menu from an NPC if the condition is not met.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| CONDITION_SOURCE_TYPE_VEHICLE_SPELL               | 21  | creature entry ([creature_template.entry](creature_template#entry))                       | Spell ID from [Spell.dbc](Spell)                                                    | Always 0                                                           | 0 = Player for whom spell bar is shown<br>1 = Vehicle creature                                                               | This will show or hide spells in vehicle spell bar.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| CONDITION_SOURCE_TYPE_SMART_EVENT                 | 22  | ID ([smart_scripts.id](smart_scripts#id)) + 1                                             | EntryOrGuid ([smart_scripts.entryorguid](smart_scripts#entryorguid))                | SourceType ([smart_scripts.source_type](smart_scripts#sourcetype)) | 0 = Invoker<br>1 = Object                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_NPC_VENDOR                  | 23  | vendor entry ([npc_vendor.entry](npc_vendor#entry))                                       | item entry ([npc_vendor.item](npc_vendor#item))                                     | Always 0                                                           | Always 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_SPELL_PROC                  | 24  | Always 0                                                                                  | Spell ID of aura which triggers the proc                                            | Always 0                                                           | 0 = Actor<br>1 = ActionTarget                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_PLAYER_LOOT_TEMPLATE        | 28  | player_loot_template.entry                                                                | Always 0                                                                            | Always 0                                                           | Always 0                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_CREATURE_RESPAWN            | 29  | enum-no-details\|29                                                                       | enum-no-details\|29                                                                 | enum-no-details\|29                                                | enum-no-details\|29                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CONDITION_SOURCE_TYPE_OBJECT_VISIBILITY           | 30  | 0 = Creature, 1 = GameObject                                                              | creature entry ([creature_template.entry](creature_template#entry)) or gameobject entry ([gameobject_template.entry](gameobject_template#entry)) | 0 = any guid (entry-level), or specific creature/gameobject guid   | 0 = Player<br>1 = WorldObject (creature/gameobject)                                                                          | Controls visibility of creatures and game objects. If set by guid (SourceId), conditions take precedence over entry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| CONDITION_SOURCE_TYPE_MAX                         | 31  |                                                                                           |                                                                                     |                                                                    |                                                                                                                              | (Placeholder)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### SourceGroup

Ver arriba.

### SourceEntry

Ver arriba.

### ElseGroup

Permite construir condiciones agrupadas: todas las entradas pertenecientes a la misma condición (mismo [SourceType](#conditions-SourceTypeOrReferenceId), [SourceGroup](#conditions-SourceGroup) y [SourceEntry](#conditions-SourceEntry)) que comparten el mismo número en ElseGroup definen un grupo. La **condición completa** se cumple cuando **cualquiera de sus grupos** se cumple (OR lógico). El **grupo** se cumple cuando **todas sus entradas se cumplen** (AND lógico).

Ejemplo:

Dos condiciones con el mismo SourceType, SourceGroup y SourceEntry pero con una Condition diferente, la primera tiene ElseGroup = 1 y la segunda tiene ElseGroup = 2; esto crea un OR lógico.

Dos condiciones con el mismo SourceType, SourceGroup y SourceEntry pero con una Condition diferente, ambas tienen ElseGroup = 1; esto crea un AND lógico.

### ConditionTypeOrReference

| ConditionTypeOrReference (name)    | Value | ConditionValue1                                                                                                                                                                                                                                                                                                                             | ConditionValue2                                                                                                                                                                                                                                                                                                                                                                                                     | ConditionValue3                                                                                                                                                                                                                                                                                         |
| ---------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CONDITION_NONE                     | 0     | (Never used)                                                                                                                                                                                                                                                                                                                                | (Never used)                                                                                                                                                                                                                                                                                                                                                                                                        | (Never used)                                                                                                                                                                                                                                                                                            |
| CONDITION_AURA                     | 1     | Spell ID from [Spell.dbc](Spell)                                                                                                                                                                                                                                                                                                            | Effect index (0-2)                                                                                                                                                                                                                                                                                                                                                                                                  | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_ITEM                     | 2     | item entry ([item_template.entry](item_template#entry))                                                                                                                                                                                                                                                                                     | item count                                                                                                                                                                                                                                                                                                                                                                                                          | 0 = not in bank, 1 = in bank                                                                                                                                                                                                                                                                            |
| CONDITION_ITEM_EQUIPPED            | 3     | item entry ([item_template.entry](item_template#entry))                                                                                                                                                                                                                                                                                     | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_ZONEID                   | 4     | Zone ID where this condition will be true.                                                                                                                                                                                                                                                                                                  | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_REPUTATION_RANK          | 5     | Faction template ID from [Faction.dbc](Faction)                                                                                                                                                                                                                                                                                             | rank:<br>1 = Hated<br>2 = Hostile<br>4 = Unfriendly<br>8 = Neutral<br>16 = Friendly<br>32 = Honored<br>64 = Revered<br>128 = Exalted<br><br>Add the target ranks together for the condition to be true for all those ranks.                                                                                                                                                                                         | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_TEAM                     | 6     | Team id :Alliance = 469 / Horde = 67                                                                                                                                                                                                                                                                                                        | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_SKILL                    | 7     | Required skill. See [SkillLine.dbc](SkillLine) .                                                                                                                                                                                                                                                                                            | Skill rank value (e.g. from 1 to 450 for the 3.3.5 branch)                                                                                                                                                                                                                                                                                                                                                          | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_QUESTREWARDED            | 8     | Quest ID - see [quest_template.id](quest_template#id)                                                                                                                                                                                                                                                                                       | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_QUESTTAKEN               | 9     | Quest ID - see [quest_template.id](quest_template#id)                                                                                                                                                                                                                                                                                       | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_DRUNKENSTATE             | 10    | Sober=0; Tipsy=1, Drunk=2, Smashed=3                                                                                                                                                                                                                                                                                                        | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_WORLD_STATE              | 11    | World state index                                                                                                                                                                                                                                                                                                                           | World state value                                                                                                                                                                                                                                                                                                                                                                                                   | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_ACTIVE_EVENT             | 12    | Event entry ([game_event.eventEntry](game_event#evententry))                                                                                                                                                                                                                                                                                | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_INSTANCE_INFO            | 13    | **entry** (see corresponding source script files for info)                                                                                                                                                                                                                                                                                  | **data** (see corresponding script source files for more info)                                                                                                                                                                                                                                                                                                                                                      | 0=INSTANCE_INFO_DATA<br>1=INSTANCE_INFO_GUID_DATA<br>2=INSTANCE_INFO_BOSS_STATE<br>3=INSTANCE_INFO_DATA64                                                                                                                                                                                               |
| CONDITION_QUEST_NONE               | 14    | Quest ID - see [quest_template.id](quest_template#id)                                                                                                                                                                                                                                                                                       | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_CLASS                    | 15    | Class mask from [ChrClasses.dbc](chrclasses)<br>Add flags together for all classes where condition is true.                                                                                                                                                                                                                                 | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_RACE                     | 16    | Race mask from [ChrRaces.dbc](chrraces) .<br>Add flags together for all races where condition is true.                                                                                                                                                                                                                                      | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_ACHIEVEMENT              | 17    | Achievement ID from [Achievement.dbc](Achievement)                                                                                                                                                                                                                                                                                          | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_TITLE                    | 18    | Title ID from [CharTitles.dbc](CharTitles)                                                                                                                                                                                                                                                                                                  | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_SPAWNMASK                | 19    | spawnMask from<br>[Creature.spawnMask](creature#spawnmask) / [Gameobject.spawnMask](gameobject#spawnmask)                                                                                                                                                                                                                                   | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_GENDER                   | 20    | 0 = Male, 1 = Female, 2 = None                                                                                                                                                                                                                                                                                                              | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_UNIT_STATE               | 21    | UnitState ([enum from Unit.h](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Entities/Unit/Unit.h#L498))                                                                                                                                                                                                      | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_MAPID                    | 22    | Map entry from Map.dbc<br>(0=Eastern Kingdoms, 1=Kalimdor, - and so on.)                                                                                                                                                                                                                                                                    | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_AREAID                   | 23    | Area ID from AreaTable.dbc                                                                                                                                                                                                                                                                                                                  | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_CREATURE_TYPE            | 24    | Creature type from [creature_template.type](creature_template#type)<br>True if creature_template.type == ConditionValue1                                                                                                                                                                                                                    | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_SPELL                    | 25    | Spell ID from [Spell.dbc](Spell)                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_PHASEMASK                | 26    | phasemask value                                                                                                                                                                                                                                                                                                                             | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_LEVEL                    | 27    | Player level (1-80 in 3.3.5)                                                                                                                                                                                                                                                                                                                | Optional: 0 = Level must be equal, 1 = Level must be higher, 2 = Level must be lower,<br>3 = Level must be higher or equal, 4 = Level must be lower or equal.                                                                                                                                                                                                                                                       | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_QUEST_COMPLETE           | 28    | Quest ID - see [quest_template.id](quest_template#id)                                                                                                                                                                                                                                                                                       | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_NEAR_CREATURE            | 29    | Creature entry from [creature_template.entry](creature_template#entry)                                                                                                                                                                                                                                                                      | Distance in yards                                                                                                                                                                                                                                                                                                                                                                                                   | Alive=0 / Dead=1                                                                                                                                                                                                                                                                                        |
| CONDITION_NEAR_GAMEOBJECT          | 30    | Gameobject entry from [gameobject_template.entry](gameobject_template#entry)                                                                                                                                                                                                                                                                | Distance in yards                                                                                                                                                                                                                                                                                                                                                                                                   | GoState<br><br>0 = ignore, 1 = Ready, 2 = Not Ready                                                                                                                                                                                                                                                     |
| CONDITION_OBJECT_ENTRY_GUID        | 31    | TypeID. Available object types:<br>3 : TYPEID_UNIT<br>4 : TYPEID_PLAYER<br>5 : TYPEID_GAMEOBJECT<br>7 : TYPEID_CORPSE (player corpse, after spirit release)                                                                                                                                                                                 | 0 = Any object of given TypeID<br>if TypeID = TYPEID_UNIT => Creature entry from [creature_template.entry](creature_template#entry)<br>if TypeID = TYPEID_GAMEOBJECT => Gameobject entry from [gameobject_template.entry](gameobject_template#entry)                                                                                                                                                                | 0 = Any object of given type<br>1 - 500k : creature / gameobject GUID                                                                                                                                                                                                                                   |
| CONDITION_TYPE_MASK                | 32    | TypeMask - a bitmask of following object types:<br>0x0008 - TYPEMASK_UNIT (8)<br>0x0010 - TYPEMASK_PLAYER (16)<br>0x0020 - TYPEMASK_GAMEOBJECT (32)<br>0x0080 - TYPEMASK_CORPSE (player corpse after spirit release) (128)                                                                                                                  | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_RELATION_TO              | 33    | Target to which relation is checked.<br>- one of the ConditionTargets available in current [SourceType](#sourcetypeorreferenceid)                                                                                                                                                                                                           | RelationType - defines relation of current ConditionTarget to target specified in ConditionValue1.<br>0 - RELATION_SELF<br>1 - RELATION_IN_PARTY<br>2 - RELATION_IN_RAID_OR_PARTY<br>3 - RELATION_OWNED_BY (ConditionTarget is owned by ConditionValue1)<br>4 - RELATION_PASSENGER_OF (ConditionTarget is passenger of ConditionValue1)<br>5 - RELATION_CREATED_BY (ConditionTarget is summoned by ConditionValue1) | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_REACTION_TO              | 34    | Target to which reaction is checked.<br>- one of the ConditionTargets available in current [SourceType](#sourcetypeorreferenceid)                                                                                                                                                                                                           | rankMask: This bitmask defines the reaction(s) of the current ConditionTarget to the target specified in ConditionValue1 (which are allowed).<br>Flags for the reactions are:<br>1 = Hated<br>2 = Hostile<br>4 = Unfriendly<br>8 = Neutral<br>16 = Friendly<br>32 = Honored<br>64 = Revered<br>128 = Exalted                                                                                                        | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_DISTANCE_TO              | 35    | Target to which distance is checked<br>- one of ConditionTargets available in current [SourceType](#sourcetypeorreferenceid)                                                                                                                                                                                                                | Distance.<br>Defines distance between current ConditionTarget and target specified in ConditionValue1                                                                                                                                                                                                                                                                                                               | ComparisionType:<br>0 = distance must be equal to ConditionValue2<br>1 = distance must be higher than ConditionValue2<br>2 = distance must be lower than ConditionValue2<br>3 = distance must be equal to or higher than ConditionValue2<br>4 = distance must be equal to or lower than ConditionValue2 |
| CONDITION_ALIVE                    | 36    | Always 0 - Use NegativeCondition and the following settings:<br>NegativeCondition = 0 if target needs to be ALIVE.<br>NegativeCondition = 1 if target needs to be DEAD.<br>NOTE: A creature corpse and a creature that_looks_dead<br>are two different things. One is actually dead<br>and the other is just using an emote to appear dead. | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_HP_VAL                   | 37    | HP value                                                                                                                                                                                                                                                                                                                                    | ComparisionType:<br>0 = HP must be equal<br>1 = HP must be higher<br>2 = HP must be lesser<br>3 = HP must be equal or higher<br>4 = HP must be equal or lower                                                                                                                                                                                                                                                       | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_HP_PCT                   | 38    | Percentage of max HP                                                                                                                                                                                                                                                                                                                        | ComparisionType:<br>0 = Percentage of max HP must be equal<br>1 = Percentage of max HP must be higher<br>2 = Percentage of max HP must be lower<br>3 = Percentage of max HP must be equal or higher<br>4 = Percentage of max HP must be equal or lower                                                                                                                                                              | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_REALM_ACHIEVEMENT        | 39    | Achievement ID from [Achievement.dbc](Achievement)                                                                                                                                                                                                                                                                                          | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_IN_WATER                 | 40    | Always 0 - Use NegativeCondition and the following settings: NegativeCondition = 0 If target needs to be on land NegativeCondition = 1 If target needs to be in water                                                                                                                                                                       | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_STAND_STATE              | 42    | stateType (exact or any): 0 = **Exact** state used in ConditionValue2 1 = **Any** type of state in ConditionValue2                                                                                                                                                                                                                          | Exact stand state, or generic state (stand / sit), depending on value 10 = Standing 1 = Sitting                                                                                                                                                                                                                                                                                                                     | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_DAILY_QUEST_DONE         | 43    | Quest ID - see [quest_template.id](quest_template#id)                                                                                                                                                                                                                                                                                       | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_CHARMED                  | 44    | Always 0                                                                                                                                                                                                                                                                                                                                    | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_PET_TYPE                 | 45    | mask                                                                                                                                                                                                                                                                                                                                        | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_TAXI                     | 46    | Always 0                                                                                                                                                                                                                                                                                                                                    | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_QUESTSTATE               | 47    | Quest ID - see [quest_template.id](quest_template#id)                                                                                                                                                                                                                                                                                       | state_mask:<br>1 = Not taken<br>2 = Completed<br>8 = In progress<br>32 = Failed<br>64 = Rewarded                                                                                                                                                                                                                                                                                                                    | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_QUEST_OBJECTIVE_PROGRESS | 48    | Quest ID - see [quest_template.id](quest_template#id)                                                                                                                                                                                                                                                                                       | Quest Objective ID - see [quest_template.RequiredNpcOrGo](quest_template#requirednpcorgo)                                                                                                                                                                                                                                                                                                                           | Quest Objective Count                                                                                                                                                                                                                                                                                   |
| CONDITION_DIFFICULTY_ID            | 49    | Difficulty                                                                                                                                                                                                                                                                                                                                  | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_QUEST_SATISFY_EXCLUSIVE  | 101   | quest_id                                                                                                                                                                                                                                                                                                                                    | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_HAS_AURA_TYPE            | 102   | aura_type                                                                                                                                                                                                                                                                                                                                   | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_WORLD_SCRIPT             | 103   | conditionId                                                                                                                                                                                                                                                                                                                                 | state                                                                                                                                                                                                                                                                                                                                                                                                               | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_AI_DATA                  | 104   | dataId (true if AI::GetData(uint32 dataId) returns value)                                                                                                                                                                                                                                                                                   | value                                                                                                                                                                                                                                                                                                                                                                                                               | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_RANDOM_DUNGEON           | 105   | checkDifficulty                                                                                                                                                                                                                                                                                                                             | difficulty                                                                                                                                                                                                                                                                                                                                                                                                          | Always 0                                                                                                                                                                                                                                                                                                |
| CONDITION_UNIT_IN_COMBAT           | 106   | Always 0                                                                                                                                                                                                                                                                                                                                    | Always 0                                                                                                                                                                                                                                                                                                                                                                                                            | Always 0                                                                                                                                                                                                                                                                                                |

### ConditionTarget

Permite seleccionar un objeto para el que se comprobarán las condiciones. Los objetos disponibles dependen de SourceTypeOrReferenceId; para más detalles ver la referencia del source type respectivo.

### ConditionValue1

Ver abajo

### ConditionValue2

Ver abajo

### ConditionValue3

Ver abajo

### NegativeCondition

Si se establece en 1, la condición se "invertirá"

Ejemplo: CONDITION\_AURA con NegativeCondition será verdadera cuando el jugador NO tenga el aura.

### ErrorType

Id de [/src/server/game/Miscellaneous/SharedDefines.h#L830](https://github.com/azerothcore/azerothcore-wotlk/blob/97e65bd4479272106bba87364d35233d2e4bd2ef/src/server/game/Miscellaneous/SharedDefines.h#L830). Solo se mostrará para el siguiente [source type](#conditions-SourceTypeOrReferenceId) de condición:

CONDITION\_SOURCE\_TYPE\_SPELL = 17

### ErrorTextId

Id de [/src/server/game/Miscellaneous/SharedDefines.h#L1024](https://github.com/azerothcore/azerothcore-wotlk/blob/97e65bd4479272106bba87364d35233d2e4bd2ef/src/server/game/Miscellaneous/SharedDefines.h#L1024). Solo se mostrará para el siguiente [source type](#conditions-SourceTypeOrReferenceId) de condición:

CONDITION\_SOURCE\_TYPE\_SPELL = 17

(ErrorType debe ser SPELL\_FAILED\_CUSTOM\_ERROR (209), de lo contrario 0)

### ScriptName

El ScriptName que usa esta condición, si lo hay.

### Comment

Explicación de esta condición o referencia

### Explicación de los tipos de condición

El contenido de los campos [SourceGroup](#conditions-SourceGroup) y [SourceEntry](#conditions-SourceEntry) depende de [SourceTypeOrReferenceId](#conditions-SourceTypeOrReferenceId)

**CONDITION\_SOURCE\_TYPE\_NONE = 0**

**¡Solo se usa en las Reference Templates! Ver abajo.**

**CONDITION\_SOURCE\_TYPE\_ \* \_LOOT\_TEMPLATE = 1 - 12**
\***SourceGroup: loot entry (**\_loot\_template.Entry or Reference\_loot\_template.Entry)
\***SourceEntry: item id (**\_loot\_template.Item or Reference\_loot\_template.Item)

-   -   ConditionTarget: siempre 0

*ejemplo: si usas el tipo 1 (creature\_loot\_template) entonces usa los campos entry e item de esa tabla*

**CONDITION\_SOURCE\_TYPE\_SPELL\_IMPLICIT\_TARGET = 13**

-   -   SourceGroup: máscara de efectos que serán afectados por la condición (1 - EFFECT\_0, 2 - EFFECT\_1, 4 - EFFECT\_2 - no uses wowhead para obtener el número de efectos, los datos de wowhead a veces no coinciden con el número de efecto real)
    -   SourceEntry: spell (Spell Id de  [Spell.dbc](spell).)
    -   ConditionTarget:
        -   0 - Objetivo potencial del hechizo
        -   1 - Lanzador del hechizo

Notas:

-   este condition source type permite definir un filtro para los posibles objetivos del spell effect, de modo que solo los objetivos que cumplan la condición se seleccionarán como objetivos implícitos del hechizo. Solo se pueden filtrar los tipos de objetivo: *AREA*, *NEARBY* y *CONE*. Este source type solo afecta a los objetivos seleccionados por el hechizo, no afecta al objetivo del hechizo seleccionado por el jugador al lanzar; para afectar a ese objetivo usa CONDITION\_SOURCE\_TYPE\_SPELL.
-   para restringir los objetivos solo a jugadores usa CONDITION\_TYPEMASK con TYPEMASK\_PLAYER + TYPEMASK\_CORPSE para permitir apuntar a jugadores muertos.
-   recuerda que las condiciones con el mismo valor de ElseGroup se usarán para hacer una comprobación AND lógico, así que para permitir distintos objetivos para el mismo spell effect tienes que establecer ElseGroup en consecuencia.
-   si buscas el antiguo CONDITION\_SOURCE\_TYPE\_SPELL\_SCRIPT\_TARGET, usa este condition source type en su lugar

**CONDITION\_SOURCE\_TYPE\_GOSSIP\_MENU = 14**

-   -   SourceGroup: gossip menu entry ([gossip\_menu.MenuID](gossip_menu#menuid))
    -   SourceEntry: gossip menu text id ([gossip\_menu.TextID](gossip_menu#textid))
    -   ConditionTarget:
        -   0 - Jugador para el que se muestra el texto del gossip
        -   1 - WorldObject que proporciona el gossip

**CONDITION\_SOURCE\_TYPE\_GOSSIP\_MENU\_OPTION = 15**

-   -   SourceGroup: gossip menu entry ([gossip\_menu\_option.MenuID](gossip_menu_option#menuid))
    -   SourceEntry: gossip menu option id ([gossip\_menu\_option.OptionID](gossip_menu_option#optionid))
    -   ConditionTarget:
        -   0 - Jugador para el que se muestra el texto del gossip
        -   1 - WorldObject que proporciona el gossip

**CONDITION\_SOURCE\_TYPE\_CREATURE\_TEMPLATE\_VEHICLE = 16**

-   -   SourceGroup: siempre 0
    -   SourceEntry: creature entry ([creature\_template.entry](creature_template#entry))
    -   ConditionTarget:
        -   0 - Jugador montando un vehículo
        -   1 - Creature del vehículo

Nota: la creature entry debe ser un vehículo. Ejemplo: si esto se usa con CONDITION\_AREA, el jugador será desmontado del vehículo si el jugador montado abandona esa área.

**CONDITION\_SOURCE\_TYPE\_SPELL = 17**

-   -   SourceGroup: siempre 0
    -   SourceEntry: spell (Spell Id de [Spell.dbc](spell))
    -   ConditionTarget:
        -   0 - Lanzador del hechizo
        -   1 - Objetivo explícito del hechizo (solo para hechizos que tienen en cuenta el objeto seleccionado por el lanzador)

Notas:

-   este source type te permite definir requisitos de lanzador/objetivo explícito para que el hechizo se lance.
-   el objetivo explícito del hechizo es el objetivo que selecciona el jugador durante el lanzamiento; no todos los hechizos tienen en cuenta ese objetivo. Los objetivos no explícitos del hechizo (los que selecciona el hechizo, como los objetivos de área o cercanos, por ejemplo) no se ven afectados por este condition source type; si quieres afectar a esos usa CONDITION\_SOURCE\_TYPE\_SPELL\_IMPLICIT\_TARGET en su lugar.
-   si buscas el antiguo CONDITION\_SOURCE\_TYPE\_ITEM\_REQUIRED\_TARGET, usa este condition source type en su lugar (ConditionTarget = 1 te permite establecer requisitos para un hechizo dado, así que para usar este tipo de condición necesitas el spellid del hechizo lanzado al usar el item)
-   recuerda que las condiciones con el mismo valor de ElseGroup se usarán para hacer una comprobación AND lógico, así que para permitir distintos objetivos para el mismo spell effect tienes que establecer ElseGroup en consecuencia.

**CONDITION\_SOURCE\_TYPE\_SPELL\_CLICK\_EVENT = 18**

-   -   SourceGroup: creature entry ([npc\_spellclick\_spells.npc\_entry](npc_spellclick_spells#npcentry))
    -   SourceEntry: spell ([npc\_spellclick\_spells.spell\_id](npc_spellclick_spells#spellid))
    -   ConditionTarget:
        -   0 - El que hace click
        -   1 - Objetivo del spellclick (el que recibe el click)

**CONDITION\_SOURCE\_TYPE\_QUEST\_ACCEPT = 19**

-   -   SourceGroup: ?
    -   SourceEntry: Quest [id](quest_template#id))
    -   ConditionTarget: siempre 0

**CONDITION\_SOURCE\_TYPE\_GOSSIP\_HELLO = 20**

-   -   SourceGroup: siempre 0
    -   SourceEntry: creature entry ([creature\_template.entry](creature_template#entry))
    -   ConditionTarget:
        -   0 - Player
        -   1 - WorldObject (creature)

Nota: esta condición impide abrir el menú de gossip de un NPC si la condición no se cumple.

**CONDITION\_SOURCE\_TYPE\_VEHICLE\_SPELL = 21**

-   -   SourceGroup: creature entry ([creature\_template.entry](creature_template#entry))
    -   SourceEntry: spell (Spell Id de [Spell.dbc](spell))
    -   ConditionTarget:
        -   0 - Jugador para el que se muestra la barra de hechizos
        -   1 - Creature del vehículo

Nota: mostrará u ocultará hechizos en la barra de hechizos del vehículo.

**CONDITION\_SOURCE\_TYPE\_SMART\_EVENT = 22**

-   -   SourceGroup: Id ([smart\_scripts.id](smart_scripts#id)) + 1
    -   SourceEntry: EntryOrGuid ([smart\_scripts.entryorguid](smart_scripts#entryorguid))
    -   SourceId: SourceType ([smart\_scripts.source\_type](smart_scripts#sourcetype))
    -   ConditionTarget:
        -   0 - Invoker
        -   1 - Object

**CONDITION\_SOURCE\_TYPE\_NPC\_VENDOR = 23**

-   -   SourceGroup: vendor entry ([npc\_vendor.entry](npc_vendor#entry))
    -   SourceEntry: item entry ([npc\_vendor.item](npc_vendor#item))
    -   SourceId: siempre 0

**CONDITION\_SOURCE\_TYPE\_SPELL\_PROC = 24**

-   -   SourceGroup: siempre 0
    -   SourceEntry: spell id del aura que dispara el proc
    -   ConditionTarget:
        -   0 - Actor
        -   1 - ActionTarget

**CONDITION\_SOURCE\_TYPE\_OBJECT\_VISIBILITY = 30**

-   -   SourceGroup: 0 para Creature, 1 para GameObject
    -   SourceEntry: creature entry ([creature\_template.entry](creature_template#entry)) o gameobject entry ([gameobject\_template.entry](gameobject_template#entry))
    -   SourceId: 0 para cualquier guid (a nivel de entry), o un guid específico de creature/gameobject
    -   ConditionTarget:
        -   0 - Player
        -   1 - WorldObject (creature/gameobject)

Nota: esta condición controla la visibilidad de creatures y game objects según las condiciones evaluadas contra el jugador. Si las condiciones se establecen por guid (SourceId), tienen prioridad sobre las condiciones a nivel de entry.

### Explicación de los campos ConditionValueX

**CONDITION\_NONE = 0**

**Nunca se usa**

**CONDITION\_AURA = 1**

-   -   ConditionValue1: spell (Spell Id de [Spell.dbc](spell))
    -   ConditionValue2: effect index (0-2)
    -   ConditionValue3: siempre 0

**CONDITION\_ITEM = 2**

-   -   ConditionValue1: item entry ([item\_template.entry](item_template#entry))
    -   ConditionValue2: item count
    -   ConditionValue3: ¿en el banco? (true=1)

**CONDITION\_ITEM\_EQUIPPED = 3**

-   -   ConditionValue1: item entry ([item\_template.entry](item_template#entry))
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_ZONEID = 4**

-   -   ConditionValue1: zone ID donde esta condición será verdadera
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_REPUTATION\_RANK = 5**

-   -   ConditionValue1: faction template ID (de [Faction.dbc](faction))
    -   ConditionValue2: rank (Hated - 1, Hostile - 2, Unfriendly - 4, Neutral - 8, Friendly - 16, Honored - 32, Revered - 64, Exalted - 128) Los flags se pueden sumar para todos los rangos en los que la condición debe ser verdadera.
    -   ConditionValue3: siempre 0

**CONDITION\_TEAM = 6**

-   -   ConditionValue1: team id (469 - Alliance, 67 - Horde)
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_SKILL = 7**

-   -   ConditionValue1: skill requerido, ver [SkillLine.dbc](skillline)
    -   ConditionValue2: skill value
    -   ConditionValue3: siempre 0

**CONDITION\_QUESTREWARDED = 8**

-   -   ConditionValue1: ([quest\_template.id](quest_template#id))
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_QUESTTAKEN = 9**

-   -   ConditionValue1: ([quest\_template.id](quest_template#id))
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_DRUNKENSTATE = 10**

-   -   ConditionValue1: drunken state: 0 - sober; 1 - tipsy, 2 - drunk, 3 - smashed
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0
    -   (Antes AD\_COMMISSION\_AURA)

**CONDITION\_WORLD\_STATE = 11**

-   -   ConditionValue1: world state index
    -   ConditionValue2: world state value
    -   ConditionValue3: siempre 0

**CONDITION\_ACTIVE\_EVENT= 12**

-   -   ConditionValue1: event entry ([game\_event.eventEntry](game_event#evententry))
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_INSTANCE\_INFO = 13**

-   -   ConditionValue1: entry //ver los archivos fuente de script correspondientes para más info
    -   ConditionValue2: data //ver los archivos fuente de script correspondientes para más info
    -   ConditionValue3: type:
        -   0 - INSTANCE\_INFO\_DATA
        -   1 - INSTANCE\_INFO\_GUID\_DATA
        -   2 - INSTANCE\_INFO\_BOSS\_STATE
        -   3 - INSTANCE\_INFO\_DATA64

**CONDITION\_QUEST\_NONE = 14**

-   -   ConditionValue1: ([quest\_template.id](quest_template#id))
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_CLASS = 15**

-   -   ConditionValue1: class mask. Suma los flags para todas las clases en las que la condición debe ser verdadera. Ver [ChrClasses.dbc](chrclasses)
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_RACE = 16**

-   -   ConditionValue1: race mask. Suma los flags para todas las razas en las que la condición debe ser verdadera. Ver [ChrRaces.dbc](chrraces)
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_ACHIEVEMENT = 17**

-   -   ConditionValue1: achievement ID de [Achievement.dbc](achievement)
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_TITLE = 18**

-   -   ConditionValue1: title ID de [CharTitles.dbc](chartitles)
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_SPAWNMASK = 19**

-   -   ConditionValue1: spawnMask (ver [Gameobject.spawnMask](gameobject#spawnmask)/[Creature.spawnMask](creature#spawnmask))
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_GENDER = 20**

-   -   ConditionValue1: 0 = Male, 1 = Female, 2 = None
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_UNIT\_STATE = 21**

-   -   ConditionValue1: UnitState ([enum](https://github.com/azerothcore/azerothcore-wotlk/blob/97e65bd4479272106bba87364d35233d2e4bd2ef/src/server/game/Entities/Unit/Unit.h#L451))
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_MAPID = 22**

-   -   ConditionValue1: Map entry
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_AREAID = 23**

-   -   ConditionValue1: Area ID
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_CREATURE\_TYPE = 24**

-   -   ConditionValue1: Creature type ([creature\_template.type](creature_template#entry)). La condición es verdadera si creature\_template.type == ConditionValue1
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_SPELL = 25**

-   -   ConditionValue1: spell (Spell Id de [Spell.dbc](spell))
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_PHASEMASK = 26**

-   -   ConditionValue1: phasemask value
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_LEVEL = 27**

-   -   ConditionValue1: Player level
    -   ConditionValue2: Opcional
        -   0 = El nivel debe ser igual
        -   1 = El nivel debe ser mayor
        -   2 = El nivel debe ser menor
        -   3 = El nivel debe ser igual o mayor
        -   4 = El nivel debe ser igual o menor
    -   ConditionValue3: siempre 0

**CONDITION\_QUEST\_COMPLETE = 28**

-   -   ConditionValue1: Quest [id](quest_template#id)
    -   ConditionValue2: Siempre 0
    -   ConditionValue3: siempre 0

*Solo si el jugador tiene todos los objetivos de la quest completos, pero aún no recompensados.*

**CONDITION\_NEAR\_CREATURE = 29**

-   -   ConditionValue1: Creature [entry](creature_template#entry)
    -   ConditionValue2: Distancia (yd)
    -   ConditionValue3: 0 = Alive , 1 = Dead

**CONDITION\_NEAR\_GAMEOBJECT = 30**

-   -   ConditionValue1: Gameobject [entry](gameobject_template#entry)
    -   ConditionValue2: Distancia (yd)
    -   ConditionValue3: GoState, 0 = ignore, 1 = Ready, 2 = Not Ready

**CONDITION\_OBJECT\_ENTRY\_GUID= 31**

-   -   ConditionValue1: TypeID - tipos de objeto disponibles:
        -   3 - TYPEID\_UNIT
        -   4 - TYPEID\_PLAYER
        -   5 - TYPEID\_GAMEOBJECT
        -   7 - TYPEID\_CORPSE (cadáver de jugador, tras liberar el espíritu)
    -   ConditionValue2: Entry
        -   0 para cualquier objeto del tipo dado
        -   [Gameobject entry](gameobject_template#entry) para TypeID = TYPEID\_GAMEOBJECT
        -   [Creature entry](creature_template#entry) para TypeID = TYPEID\_UNIT
    -   ConditionValue3 0 para cualquier objeto del tipo dado, cualquier otro valor para coincidir con ese guid

**CONDITION\_TYPE\_MASK= 32**

-   -   ConditionValue1: TypeMask - una máscara de bits de los siguientes tipos de objeto:
        -   0x0008 - TYPEMASK\_UNIT
        -   0x0010 - TYPEMASK\_PLAYER
        -   0x0020 - TYPEMASK\_GAMEOBJECT
        -   0x0080 - TYPEMASK\_CORPSE (cadáver de jugador, tras liberar el espíritu)
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_RELATION\_TO= 33**

-   -   ConditionValue1: objetivo con el que se comprueba la relación - uno de los ConditionTargets disponibles en el SourceType actual.
    -   ConditionValue2: RelationType - define la relación del ConditionTarget actual con el objetivo especificado en ConditionValue1.
        -   0 - RELATION\_SELF
        -   1 - RELATION\_IN\_PARTY
        -   2 - RELATION\_IN\_RAID\_OR\_PARTY
        -   3 - RELATION\_OWNED\_BY (ConditionTarget es propiedad de ConditionValue1)
        -   4 - RELATION\_PASSENGER\_OF (ConditionTarget es pasajero de ConditionValue1)
        -   5 - RELATION\_CREATED\_BY (ConditionTarget fue invocado por ConditionValue1)
    -   ConditionValue3: siempre 0

**CONDITION\_REACTION\_TO= 34**

-   -   ConditionValue1: objetivo con el que se comprueba la reacción - uno de los ConditionTargets disponibles en el SourceType actual.
    -   ConditionValue2: rankMask- define las reacciones del ConditionTarget actual hacia el objetivo especificado en ConditionValue1 que están permitidas. Esto es una máscara de bits, los flags para las reacciones son:
        -   1 - Hated
        -   2 - Hostile
        -   4 - Unfriendly
        -   8 - Neutral
        -   16 - Friendly
        -   32 - Honored
        -   64 - Revered
        -   128 - Exalted
    -   ConditionValue3: siempre 0

**CONDITION\_DISTANCE\_TO= 35**

-   -   ConditionValue1: objetivo con el que se comprueba la distancia - uno de los ConditionTargets disponibles en el SourceType actual.
    -   ConditionValue2: distancia - define la distancia entre el ConditionTarget actual y el objetivo especificado en ConditionValue1.
    -   ConditionValue3: ComparisionType:
        -   0 = la distancia debe ser igual a ConditionValue2
        -   1 = la distancia debe ser mayor que ConditionValue2
        -   2 = la distancia debe ser menor que ConditionValue2
        -   3 = la distancia debe ser igual o mayor que ConditionValue2
        -   4 = la distancia debe ser igual o menor que ConditionValue2

**CONDITION\_ALIVE= 36**

-   -   ConditionValue1: siempre 0
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0
    -   NegativeCondition:
        -   0 (Si el objetivo necesita estar VIVO)
        -   1 (Si el objetivo necesita estar MUERTO)
            *NOTA: el cadáver de una creature y una creature that\_looks\_dead son dos cosas diferentes. Una está realmente muerta y la otra solo usa un emote para parecer muerta.*

**CONDITION\_HP\_VAL = 37**

-   -   ConditionValue1: HP
    -   ConditionValue2: ComparisionType:
        -   0 = HP debe ser igual
        -   1 = HP debe ser mayor
        -   2 = HP debe ser menor
        -   3 = HP debe ser igual o mayor
        -   4 = HP debe ser igual o menor
    -   ConditionValue3: siempre 0

**CONDITION\_HP\_PCT = 38**

-
    -   ConditionValue1: Porcentaje del HP máximo
    -   ConditionValue2: ComparisionType:
        -   0 = El porcentaje del HP máximo debe ser igual
        -   1 = El porcentaje del HP máximo debe ser mayor
        -   2 = El porcentaje del HP máximo debe ser menor
        -   3 = El porcentaje del HP máximo debe ser igual o mayor
        -   4 = El porcentaje del HP máximo debe ser igual o menor
    -   ConditionValue3: siempre 0

**CONDITION\_REALM\_ACHIEVEMENT = 39**

-   -   ConditionValue1: achievement ID de [Achievement.dbc](achievement)
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0

**CONDITION\_IN\_WATER = 40**

-   -   ConditionValue1: siempre 0
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0
    -   NegativeCondition:
        -   0 (Si el objetivo necesita estar en tierra)
        -   1 (Si el objetivo necesita estar en el agua)

**CONDITION\_STAND\_STATE = 42**

-   -   ConditionValue1: stateType (exact or any)
        -   0 = Estado exacto usado en ConditionValue2
        -   1 = Cualquier tipo de estado en ConditionValue2
    -   ConditionValue2: Estado exacto de pie, o estado genérico (stand / sit), dependiendo del valor 1
        -   0 = Standing
        -   1 = Sitting
    -   ConditionValue3: siempre 0

**CONDITION\_WORLD\_SCRIPT = 103**

-   -   ConditionValue1: WorldStateCondition definido en WorldState.h
    -   ConditionValue2: state o 0 (WORLD_STATE_CONDITION_STATE_NONE)
    -   ConditionValue3: siempre 0
        *NOTA: la condición es verdadera si WorldState::IsConditionFulfilled devuelve true*

**CONDITION\_AI\_DATA = 104**

Devuelve true cuando `AI::GetData(ConditionValue1)` devuelve el valor especificado en `ConditionValue2`. Funciona tanto en creatures como en gameobjects que usan SmartAI. Los datos se almacenan mediante `SMART_ACTION_SET_DATA`.

-   -   ConditionValue1: dataId — la clave pasada a `AI::GetData()`
    -   ConditionValue2: valor esperado — el valor con el que comparar el resultado
    -   ConditionValue3: siempre 0

**CONDITION\_RANDOM\_DUNGEON = 105**

Devuelve true cuando el jugador está en cola para un dungeon aleatorio mediante el sistema LFG/RDF.

- - `ConditionValue1`: 0 = no comprobar dificultad; 1 = comprobar dificultad (`ConditionValue2`).
  - `ConditionValue2`: si `ConditionValue1 = 1`, compara con la dificultad de mapa actual del jugador. El valor debe ser menor que `MAX_DIFFICULTY`
  - `ConditionValue3`: siempre 0

**CONDITION\_UNIT\_IN\_COMBAT = 106**

Devuelve true cuando la unidad objetivo está actualmente en combate.

-   -   ConditionValue1: siempre 0
    -   ConditionValue2: siempre 0
    -   ConditionValue3: siempre 0
    -   NegativeCondition:
        -   0 (true si el objetivo ESTÁ en combate)
        -   1 (true si el objetivo NO está en combate)

*Se puede usar con `CONDITION_SOURCE_TYPE_GOSSIP_HELLO` (tipo 20) y `NegativeCondition = 1` (ConditionTarget = 1 para apuntar a la creature) para impedir que los jugadores abran el menú de gossip de creatures específicas mientras están en combate.*

### \***REFERENCE TEMPLATES**

-   -   SourceTypeOrReferenceId : usado como negativo, para el reference ID
    -   SourceGroup  : siempre 0
    -   SourceEntry  : siempre 0
    -   ElseGroup  : modificador OR
    -   ConditionTypeOrReference: [ConditionTypeOrReference](#conditions-ConditionTypeOrReference)
    -   ConditionValue1  : ver arriba
    -   ConditionValue2  : ver arriba
    -   ConditionValue3  : ver arriba
    -   ErrorType  : ver arriba
    -   ErrorTextId  : ver arriba
    -   Comment  : ver arriba

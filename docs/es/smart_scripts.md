---
redirect_from: "/sai"
---

# smart_scripts

[<-Volver a: World](es/database-world)

La tabla `smart_scripts` tiene 31 atributos. Sirve para hacer scripts en lenguaje SQL. Lo importante es analizar siempre cuál es el evento que motiva la ejecución de una acción y, por supuesto, cuál es el objetivo. Como recomendación, puedes revisar los scripts que ya están dentro de la tabla para entender cómo funciona. La ventaja, por la que varios usan este método, es que no se requiere compilar al añadir registros; con reiniciar el servidor, si está bien programado, puedes apreciar los cambios. Otra razón es la portabilidad, pero eso depende del punto de vista del desarrollador y de la respuesta que puedas obtener.

**Estructura**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [entryorguid][1] | INT | SIGNED | PRI | NO | | | |
| [source_type][2] | TINYINT | UNSIGNED | PRI | NO | 0 | | |
| [id][3] | SMALLINT | UNSIGNED | PRI | NO | 0 | | |
| [link][4] | SMALLINT | UNSIGNED | PRI | NO | 0 | | |
| [event_type][5] | TINYINT | UNSIGNED | | NO | 0 | | |
| [event_phase_mask][6] | SMALLINT | UNSIGNED | | NO | 0 | | |
| [event_chance][7] | TINYINT | UNSIGNED | | NO | 100 | | |
| [event_flags][8] | SMALLINT | UNSIGNED | | NO | 0 | | |
| [event_param1][5] | INT | UNSIGNED | | NO | 0 | | |
| [event_param2][5] | INT | UNSIGNED | | NO | 0 | | |
| [event_param3][5] | INT | UNSIGNED | | NO | 0 | | |
| [event_param4][5] | INT | UNSIGNED | | NO | 0 | | |
| [event_param5][5] | INT | UNSIGNED | | NO | 0 | | |
| [event_param6][5] | INT | UNSIGNED | | NO | 0 | | |
| [action_type][9] | TINYINT | UNSIGNED | | NO | 0 | | |
| [action_param1][9] | INT | UNSIGNED | | NO | 0 | | |
| [action_param2][9] | INT | UNSIGNED | | NO | 0 | | |
| [action_param3][9] | INT | UNSIGNED | | NO | 0 | | |
| [action_param4][9] | INT | UNSIGNED | | NO | 0 | | |
| [action_param5][9] | INT | UNSIGNED | | NO | 0 | | |
| [action_param6][9] | INT | UNSIGNED | | NO | 0 | | |
| [target_type][10] | TINYINT | UNSIGNED | | NO | 0 | | |
| [target_param1][10] | INT | UNSIGNED | | NO | 0 | | |
| [target_param2][10] | INT | UNSIGNED | | NO | 0 | | |
| [target_param3][10] | INT | UNSIGNED | | NO | 0 | | |
| [target_param4][10] | INT | UNSIGNED | | NO | 0 | | |
| [target_x][10] | FLOAT | SIGNED | | NO | 0 | | |
| [target_y][10] | FLOAT | SIGNED | | NO | 0 | | |
| [target_z][10] | FLOAT | SIGNED | | NO | 0 | | |
| [target_o][10] | FLOAT | SIGNED | | NO | 0 | | |
| [comment][11] | text | | | NO | | | Event Comment |

[1]: #entryorguid
[2]: #sourcetype
[3]: #id
[4]: #link
[5]: #eventtype
[6]: #eventphasemask
[7]: #eventchance
[8]: #eventflags
[9]: #actiontype
[10]: #targettype
[11]: #comment

**Descripción de los campos**

### entryorguid

- EntryOrGuid > 0: `entry` de la creature / game object / etc.
- EntryOrGuid < 0: `guid` de la creature / game object / etc.
- **Depende de source_type.**

Al usar SAI específico de GUID, el extra_flag DONT_OVERRIDE_SAI_ENTRY nos permite no tener que duplicar las filas compartidas entre todas las creatures del mismo entry.

Por ejemplo, puedes mantener todo el scripting relacionado con el movimiento en el script del GUID, mientras que el scripting de combate lo gestiona el script del ENTRY.

Para las creatures que usan este flag, los IDs de fila de SAI no pueden solaparse, por lo que usamos IDs de fila que empiezan en 1000 y se van incrementando (p. ej. 1000, 1001, 1002, ...).

### source_type

Tipo de objeto: creature, game object, spell. Ver la tabla de abajo para los valores.

| Name | Value |
| --- | --- |
| SMART_SCRIPT_TYPE_CREATURE | 0 |
| SMART_SCRIPT_TYPE_GAMEOBJECT | 1 |
| SMART_SCRIPT_TYPE_AREATRIGGER | 2 |
| SMART_SCRIPT_TYPE_TIMED_ACTIONLIST | 9 |

### id

Id incremental *ligado* a cada entryorguid y source_type (0, 1, 2, ...).

### link

Enlazado simple de eventos;

- Ejemplo: si id = 0 y link = 1; el id 1 solo podrá ocurrir si el id = 0 se disparó (el id 1 tiene que usar event_type SMART_EVENT_LINK).
- Smart_event a usar.

**Gracias al uso de los links, puedes ejecutar varias acciones manteniendo el mismo evento.**

### event_phase_mask

Al trabajar con phases, hay que usar los *IDs de phase*. Hay 13 (12+1) phases diferentes: 1, 2, ... 12 y la 0 por defecto.

**Ejemplo:** el script está en la phase 0 por defecto. Si queremos que pase a la phase 1, tenemos dos opciones:

- SMART_ACTION_INC_PHASE en 1 o SMART_ACTION_SET_PHASE 1

Si el script está en la phase 0 y quiere saltar a la phase 2:

- SMART_ACTION_INC_PHASE en 2 o SMART_ACTION_SET_PHASE 2

Si el script está en la phase 1 y quiere saltar a la phase 2:

- SMART_ACTION_INC_PHASE en 1 o SMART_ACTION_SET_PHASE 2

| Name | Flag | Hex | Comment |
| --- | --- | --- | --- |
| SMART_EVENT_PHASE_ALWAYS_BIT | 0 | 0x000 | Significa todas las phases (1 ... 12) |
| SMART_EVENT_PHASE_1 | 1 | 0x001 | Solo phase 1. |
| SMART_EVENT_PHASE_2 | 2 | 0x002 | Solo phase 2. |
| SMART_EVENT_PHASE_3 | 4 | 0x004 | Solo phase 3. |
| SMART_EVENT_PHASE_4 | 8 | 0x008 | Solo phase 4. |
| SMART_EVENT_PHASE_5 | 16 | 0x010 | Solo phase 5. |
| SMART_EVENT_PHASE_6 | 32 | 0x020 | Solo phase 6. |
| SMART_EVENT_PHASE_7 | 64 | 0x040 | Solo phase 7. |
| SMART_EVENT_PHASE_8 | 128 | 0x080 | Solo phase 8. |
| SMART_EVENT_PHASE_9 | 256 | 0x100 | Solo phase 9. |
| SMART_EVENT_PHASE_10 | 512 | 0x200 | Solo phase 10. |
| SMART_EVENT_PHASE_11 | 1024 | 0x400 | Solo phase 11. |
| SMART_EVENT_PHASE_12 | 2048 | 0x800 | Solo phase 12. |

- El evento solo podrá ocurrir si la creature/GO está en esta phase.
- Ejemplo: si queremos que un evento solo pueda ocurrir en las phases 1 y 4, **event_phase_mask** = 1+8 = 9.

### event_chance

Esta es la probabilidad de que ocurra el evento como porcentaje de 0 a 100. Así, si quieres que el evento ocurra aproximadamente la mitad de las veces, establécelo en 50. 

### event_flags

| Name | Flag | Hex | Comment |
| --- | --- | --- | --- |
| SMART_EVENT_FLAG_NOT_REPEATABLE | 1 | 0x01 | El evento no se puede repetir |
| SMART_EVENT_FLAG_DIFFICULTY_0 | 2 | 0x02 | El evento solo ocurre en dungeon normal |
| SMART_EVENT_FLAG_DIFFICULTY_1 | 4 | 0x04 | El evento solo ocurre en dungeon heroico |
| SMART_EVENT_FLAG_DIFFICULTY_2 | 8 | 0x08 | El evento solo ocurre en raid normal |
| SMART_EVENT_FLAG_DIFFICULTY_3 | 16 | 0x10 | El evento solo ocurre en raid heroico |
| SMART_EVENT_FLAG_RESERVED_5 | 32 | 0x20 | |
| SMART_EVENT_FLAG_RESERVED_6 | 64 | 0x40 | |
| SMART_EVENT_FLAG_DEBUG_ONLY | 128 | 0x80 | El evento solo ocurre en build de debug |
| SMART_EVENT_FLAG_DONT_RESET | 256 | 0x100 | El evento no se reseteará en SmartScript::OnReset() |
| SMART_EVENT_FLAG_WHILE_CHARMED | 512 | 0x200 | El evento ocurre incluso si el propietario de la IA está encantado |

- Establece si el evento no debe repetirse o solo debe ocurrir en una dificultad de instancia/dungeon dada (si aplica);
- Los valores se pueden sumar (matemática de bits).

### event_type

| Name | Value | Param1 | Param2 | Param3 | Param4 | Param5 | Param6 | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SMART_EVENT_UPDATE_IC | 0 | InitialMin | InitialMax | RepeatMin | RepeatMax | | | En combate. |
| SMART_EVENT_UPDATE_OOC | 1 | InitialMin | InitialMax | RepeatMin | RepeatMax | | | Fuera de combate. |
| SMART_EVENT_HEALTH_PCT | 2 | HPMin% | HPMax% | RepeatMin | RepeatMax | | | Porcentaje de salud |
| SMART_EVENT_MANA_PCT | 3 | ManaMin% | ManaMax% | RepeatMin | RepeatMax | | | Porcentaje de maná |
| SMART_EVENT_AGGRO | 4 | | | | | | | Al hacer aggro la creature |
| SMART_EVENT_KILL | 5 | CooldownMin | CooldownMax | Player only (0/1) | Creature entry (if param3 is 0) | | | Al matar la creature |
| SMART_EVENT_DEATH | 6 | | | | | | | A la muerte de la creature |
| SMART_EVENT_EVADE | 7 | | | | | | | Al evadir la creature el ataque |
| SMART_EVENT_SPELLHIT | 8 | SpellID | School | CooldownMin | CooldownMax | | | Al recibir un impacto de hechizo la creature/gameobject |
| SMART_EVENT_RANGE | 9 | InitialMin | InitialMax | RepeatMin | RepeatMax | MinDist | MaxDist | Con la víctima en rango |
| SMART_EVENT_OOC_LOS | 10 | NoHostile | MaxRange | CooldownMin | CooldownMax | 0/1 Player Only | | Con el objetivo a distancia fuera de combate |
| SMART_EVENT_RESPAWN | 11 | type (None = 0, Map = 1, Area = 2) | MapId | ZoneId | | | | Al respawnear la creature/gameobject |
| SMART_EVENT_TARGET_HEALTH_PCT | 12 | HPMin% | HPMax% | RepeatMin | RepeatMax | | | Según el porcentaje de salud del objetivo |
| SMART_EVENT_VICTIM_CASTING | 13 | RepeatMin | RepeatMax | Spell id (0 any) | | | | Cuando el objetivo está lanzando un hechizo |
| SMART_EVENT_FRIENDLY_HEALTH | 14 | HPDeficit | Radius | RepeatMin | RepeatMax | | | Con déficit de salud en un aliado |
| SMART_EVENT_FRIENDLY_IS_CC | 15 | Radius | RepeatMin | RepeatMax | | | | |
| SMART_EVENT_FRIENDLY_MISSING_BUFF | 16 | SpellId | Radius | RepeatMin | RepeatMax | onlyInCombat | | Cuando un aliado pierde un buff |
| SMART_EVENT_SUMMONED_UNIT | 17 | CretureId (0 all) | CooldownMin | CooldownMax | | | | Al invocar una unidad la creature/gameobject |
| SMART_EVENT_TARGET_MANA_PCT | 18 | ManaMin% | ManaMax% | RepeatMin | RepeatMax | | | Según el porcentaje de maná del objetivo |
| SMART_EVENT_ACCEPTED_QUEST | 19 | QuestID (0 any) | CooldownMin | CooldownMax | | | | Cuando el objetivo acepta una quest |
| SMART_EVENT_REWARD_QUEST | 20 | QuestID (0 any) | CooldownMin | CooldownMax | | | | Cuando el objetivo recibe la recompensa de una quest |
| SMART_EVENT_REACHED_HOME | 21 | | | | | | | Cuando la creature llega a casa |
| SMART_EVENT_RECEIVE_EMOTE | 22 | EmoteId | CooldownMin | CooldownMax | | | | Al recibir un emote. |
| SMART_EVENT_HAS_AURA | 23 | SpellID | Stacks | RepeatMin | RepeatMax | | | Cuando la creature tiene un aura |
| SMART_EVENT_TARGET_BUFFED | 24 | SpellID | Stacks | RepeatMin | RepeatMax | | | Cuando el objetivo tiene un buff de un hechizo |
| SMART_EVENT_RESET | 25 | | | | | | | Tras el combate, al respawnear o spawnear |
| SMART_EVENT_IC_LOS | 26 | NoHostile | MaxRange | CooldownMin | CooldownMax | 0/1 Player Only | | Con el objetivo a distancia en combate |
| SMART_EVENT_PASSENGER_BOARDED | 27 | CooldownMin | CooldownMax | | | | | |
| SMART_EVENT_PASSENGER_REMOVED | 28 | CooldownMin | CooldownMax | | | | | |
| SMART_EVENT_CHARMED | 29 | onRemove (0 - on apply, 1 - on remove) | | | | | | Cuando la creature es encantada |
| SMART_EVENT_CHARMED_TARGET | 30 | | | | | | | Cuando el objetivo es encantado |
| SMART_EVENT_SPELLHIT_TARGET | 31 | SpellId | School | RepeatMin | RepeatMax | | | Al impactar un hechizo en el objetivo |
| SMART_EVENT_DAMAGED | 32 | MinDmg | MaxDmg | RepeatMin | RepeatMax | HpPct (1-100) | | Al recibir daño la creature. Si se establece HpPct, se dispara una vez cuando el daño baja la salud por debajo de ese porcentaje. |
| SMART_EVENT_DAMAGED_TARGET | 33 | MinDmg | MaxDmg | RepeatMin | RepeatMax | | | Al recibir daño el objetivo |
| SMART_EVENT_MOVEMENTINFORM | 34 | MovementType (0=any) | PointID | | | | | ESCORT_MOTION_TYPE = 17, POINT_MOTION_TYPE = 8 |
| SMART_EVENT_SUMMON_DESPAWNED | 35 | Entry | CooldownMin | CooldownMax | | | | Al despawnear una unidad invocada |
| SMART_EVENT_CORPSE_REMOVED | 36 | | | | | | | Al eliminarse el cadáver de la creature |
| SMART_EVENT_AI_INIT | 37 | | | | | | | |
| SMART_EVENT_DATA_SET | 38 | Field | Value | CooldownMin | CooldownMax | | | Al establecer data en la creature/gameobject. Se puede usar con SMART_ACTION_SET_DATA |
| SMART_EVENT_ESCORT_START | 39 | PointId (0 any) | pathId (0 any) | | | | | Cuando se inicia el Escort ID de la creature |
| SMART_EVENT_ESCORT_REACHED | 40 | PointId (0 any) | pathId (0 any) | | | | | Cuando la creature alcanza el Escort ID. Usa la tabla 'waypoints' |
| SMART_EVENT_AREATRIGGER_ONTRIGGER | 46 | TriggerId (0 any) | | | | | | |
| SMART_EVENT_TEXT_OVER | 52 | creature_text.GroupID | creature.id (0 any) | | | | | Al dispararse el evento TEXT_OVER tras SMART_ACTION_TALK |
| SMART_EVENT_RECEIVE_HEAL | 53 | MinHeal | MaxHeal | CooldownMin | CooldownMax | | | Al recibir sanación la creature |
| SMART_EVENT_JUST_SUMMONED | 54 | | | | | | | Cuando la creature acaba de spawnear |
| SMART_EVENT_ESCORT_PAUSED | 55 | PointId (0 any) | pathID (0 any) | | | | | Cuando la creature se pausa en el Escort ID |
| SMART_EVENT_ESCORT_RESUMED | 56 | PointId (0 any) | pathID (0 any) | | | | | Cuando la creature reanuda tras el Escort ID |
| SMART_EVENT_ESCORT_STOPPED | 57 | PointId (0 any) | pathID (0 any) | | | | | Cuando la creature se detiene en el Escort ID |
| SMART_EVENT_ESCORT_ENDED | 58 | PointId (0 any) | pathID (0 any) | | | | | Cuando termina la ruta de Escort de la creature. Usa la tabla 'waypoints' |
| SMART_EVENT_TIMED_EVENT_TRIGGERED | 59 | Id | | | | | | |
| SMART_EVENT_UPDATE | 60 | InitialMin | InitialMax | RepeatMin | RepeatMax | | | |
| SMART_EVENT_LINK | 61 | | | | | | | Se usa para enlazar varios eventos como una cadena de eventos. |
| SMART_EVENT_GOSSIP_SELECT | 62 | gossip_menu_option.MenuID | gossip_menu_option.OptionID | | | | | Al hacer click en el gossip (gossip_menu_option). |
| SMART_EVENT_JUST_CREATED | 63 | | | | | | | Cuando el gameobject acaba de spawnear |
| SMART_EVENT_GOSSIP_HELLO | 64 | gossipHello.filter (0 - always, 1  - GossipHello, 2 - reportUse) | | | | | | Al hacer click derecho en una creature/gameobject que tiene gossip habilitado. |
| SMART_EVENT_FOLLOW_COMPLETED | 65 | | | | | | | |
| SMART_EVENT_EVENT_PHASE_CHANGE | 66 | event phase mask | | | | | | Al establecerse el event phase mask |
| SMART_EVENT_IS_BEHIND_TARGET | 67 | InitialMin | InitialMax | RepeatMin | RepeatMax | RangeMin | RangeMax | Cuando la creature está detrás del objetivo. |
| SMART_EVENT_GAME_EVENT_START | 68 | game_event.eventEntry | | | | | | Al iniciarse un game_event. |
| SMART_EVENT_GAME_EVENT_END | 69 | game_event.eventEntry | | | | | | Al terminar un game_event. |
| SMART_EVENT_GO_STATE_CHANGED | 70 | State (0 - Active, 1 - Ready, 2 - Active alternative) | | | | | | |
| SMART_EVENT_GO_EVENT_INFORM | 71 | EventId | | | | | | |
| SMART_EVENT_ACTION_DONE | 72 | EventId | CooldownMin (ms) | CooldownMax (ms) | | | | Se dispara cuando un doAction con el EventId coincidente se completa. Cooldown opcional entre disparos. |
| SMART_EVENT_ON_SPELLCLICK | 73 | | | | | | | |
| SMART_EVENT_FRIENDLY_HEALTH_PCT | 74 | InitialMin | InitialMax | RepeatMin | RepeatMax | Hp Percentage | Range | Cuando una creature aliada dentro del rango cae por debajo del porcentaje de HP |
| SMART_EVENT_DISTANCE_CREATURE | 75 | database guid | database entry | distance | repeat interval (ms) | | | Cuando el guid de una creature O cualquier instancia del entry de creature está dentro de la distancia. |
| SMART_EVENT_DISTANCE_GAMEOBJECT | 76 | database guid | database entry | distance | repeat interval (ms) | | | Cuando el guid de un gameobject O cualquier instancia del entry de gameobject está dentro de la distancia. |
| SMART_EVENT_COUNTER_SET | 77 | counterID | value | cooldownMin | cooldownMax | | | Si el valor del counterID especificado es igual a un valor especificado |
| SMART_EVENT_SUMMONED_UNIT_DIES | 82 | CreatureId (0 all) | CooldownMin | CooldownMax | | | | |
| SMART_EVENT_NEAR_PLAYERS | 101 | minPlayers | Range (yards) | FirstCheck (ms) | RepeatMin (ms) | RepeatMax (ms) | | El evento se disparará si hay más o igual que minPlayers en el rango. |
| SMART_EVENT_NEAR_PLAYERS_NEGATION | 102 | maxPlayers | Range (yards) | FirstCheck (ms) | RepeatMin (ms) | RepeatMax (ms) | | El evento se disparará si hay menos de maxPlayers en el rango. |
| SMART_EVENT_NEAR_UNIT | 103 | Unit type to check (0: creature 1: gob) | Entry (template) | Count | Range | Timer (ms) | | Comprobará si hay >= count del entry especificado dentro del rango |
| SMART_EVENT_NEAR_UNIT_NEGATION | 104 | Unit type to check (0: creature 1: gob) | Entry (template) | Count | Range | Timer (ms) | | Comprobará si hay < count del entry especificado dentro del rango |
| SMART_EVENT_AREA_CASTING | 105 | InitialMin | InitialMax | RepeatMin | RepeatMax | RangeMin | RangeMax | Comprueba la lista de amenaza en busca de hostiles lanzando hechizos. Si no encuentra ninguno, repite en 1200ms |
| SMART_EVENT_AREA_RANGE | 106 | InitialMin | InitialMax | RepeatMin | RepeatMax | RangeMin | RangeMax | Comprueba la lista de amenaza en busca de hostiles en rango. Si no encuentra ninguno, repite en 1200ms |
| SMART_EVENT_SUMMONED_UNIT_EVADE | 107 | CreatureId (0 all) | CooldownMin | CooldownMax | | | | Al evadir una unidad invocada |
| SMART_EVENT_WAYPOINT_REACHED | 108 | PointId (0 any) | pathId (0 any) | | | | | Cuando la creature alcanza un waypoint. Usa la tabla 'waypoint_data' |
| SMART_EVENT_WAYPOINT_ENDED | 109 | PointId (0 any) | pathId (0 any) | | | | | Cuando la creature termina un waypoint. Usa la tabla 'waypoint_data' |
| SMART_EVENT_IS_IN_MELEE_RANGE | 110 | InitialMin | InitialMax | RepeatMin | RepeatMax | Distance | Invert | Cuando la creature está en rango cuerpo a cuerpo del objetivo |
### action_type

| Name | Value | Param1 | Param2 | Param3 | Param4 | Param5 | Param6 | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SMART_ACTION_NONE | 0 | | | | | | | No hacer nada |
| SMART_ACTION_TALK | 1 | creature_text.GroupID | Duration to wait before SMART_EVENT_TEXT_OVER is triggered. | 0 It will try to trigger talk of the target<br/>1 Set target as talk target (used for $vars in texts and whisper target) | Delay between ACTION_TALK being triggered and the NPC speaking. If 0, the NPC will speak instantly. | | | Param2 y Param4 en milisegundos. |
| SMART_ACTION_SET_FACTION | 2 | FactionID (or 0 for default) | | | | | | Establece la facción de la creature. |
| SMART_ACTION_MORPH_TO_ENTRY_OR_MODEL | 3 | creature_template.entry(param1) | creature_template.modelidx(param2) | | | | | Toma el DisplayID de la creature (param1) O cambia al DisplayID (param2) O ambos = 0 para Demorph |
| SMART_ACTION_SOUND | 4 | SoundId | onlySelf (0/1) | distance | | | | Reproduce un sonido; onlySelf = 1 solo envía el sonido a uno mismo, onlySelf = 0 envía el sonido a todos en el rango de visibilidad |
| SMART_ACTION_PLAY_EMOTE | 5 | EmoteId | | | | | | Hace que el objetivo realice un Emote |
| SMART_ACTION_FAIL_QUEST | 6 | QuestID | | | | | | Falla la quest del objetivo |
| SMART_ACTION_OFFER_QUEST | 7 | quest_template.id | directAdd (0/1) | | | | | Añade la quest al objetivo |
| SMART_ACTION_SET_REACT_STATE | 8 | ReactState | | | | | | React State. Puede ser Passive (0), Defensive (1), Aggressive (2). |
| SMART_ACTION_ACTIVATE_GOBJECT | 9 | | | | | | | Activa el objeto |
| SMART_ACTION_RANDOM_EMOTE | 10 | EmoteId1 | EmoteId2 | EmoteId3 | EmoteId4 | EmoteId5 | EmoteId6 | Reproduce un emote aleatorio |
| SMART_ACTION_CAST | 11 | SpellId | [castFlags](#cast-flags) | [triggeredFlags](#triggered-flags) | limitTargets (0 = all) | | | Lanza el Spell ID sobre el/los objetivo(s) |
| SMART_ACTION_SUMMON_CREATURE | 12 | creature_template.entry | Summon type | duration in ms | attackInvoker (0/1/2) | attackScriptOwner (0/1) | | Invoca una unidad; attackInvoker 1: ataca al objetivo; attackInvoker 2: ataca al invoker real |
| SMART_ACTION_THREAT_SINGLE_PCT | 13 | Threat% inc | Threat% dec | | | | | Cambia el porcentaje de amenaza para un solo objetivo |
| SMART_ACTION_THREAT_ALL_PCT | 14 | Threat% inc | Threat% dec | | | | | Cambia el porcentaje de amenaza para todos los enemigos |
| SMART_ACTION_CALL_AREAEXPLOREDOREVENTHAPPENS | 15 | quest_template.id | | | | | | |
| SMART_ACTION_SET_EMOTE_STATE | 17 | EmoteId | | | | | | Reproduce el emote de forma continua |
| SMART_ACTION_SET_UNIT_FLAG | 18 | (may be more than one field OR'd together) | type<br/>If false   set creature_template.unit_flags<br/>If true   set creature_template.unit_flags2 | | | | | Puede establecer varios flags a la vez |
| SMART_ACTION_REMOVE_UNIT_FLAG | 19 | (may be more than one field OR'd together) | type<br/>If false   set creature_template.unit_flags<br/>If true   set creature_template.unit_flags2 | | | | | Puede eliminar varios flags a la vez |
| SMART_ACTION_AUTO_ATTACK | 20 | AllowAttackState (0 = Stop attack, anything else means continue   attacking) | | | | | | Detiene o continúa el ataque automático. |
| SMART_ACTION_ALLOW_COMBAT_MOVEMENT | 21 | AllowCombatMovement (0 = Stop combat based movement, anything else   continue attacking) | | | | | | Permite o desactiva el movimiento de combate |
| SMART_ACTION_SET_EVENT_PHASE | 22 | mEventPhase | | | | | | Establece la event phase 0-12 (¡los valores reales, no una máscara de bits!) |
| SMART_ACTION_INC_EVENT_PHASE | 23 | Increment | Decrement | | | | | Establece param1 O param2 (no ambos). El valor 0 no tiene efecto. |
| SMART_ACTION_EVADE | 24 | | | | | | | Evade el ataque entrante |
| SMART_ACTION_FLEE_FOR_ASSIST | 25 | 0/1 (If you want the fleeing NPC to say attempts to flee text on flee,   use 1 on param1. For no message use 0.) | | | | | | Si quieres que el NPC que huye diga '%s attempts to run away in fear' al huir, usa 1 en param1. 0 para no mostrar mensaje. |
| SMART_ACTION_CALL_GROUPEVENTHAPPENS | 26 | quest_template.id | | | | | | |
| SMART_ACTION_COMBAT_STOP | 27 | | | | | | | |
| SMART_ACTION_REMOVEAURASFROMSPELL | 28 | Spellid (0 removes all auras) | charges (0 removes aura) | | | | | |
| SMART_ACTION_FOLLOW | 29 | Distance (0 = Default value) | Angle (0 = Default value) | End creature_template.entry | credit | creditType (0 monsterkill, 1 event) | aliveState (0 = creature must be alive to count as arrived, 1 = creature can be dead) | Sigue al objetivo. Si el target type es NONE o SELF, deja de seguir. param6 se niega internamente: aliveState=0 significa esperar a una creature viva, aliveState=1 significa que una creature muerta también cuenta como llegada. |
| SMART_ACTION_RANDOM_PHASE | 30 | event_phase_mask 1 | event_phase_mask 2 | event_phase_mask 3 | event_phase_mask 4 | event_phase_mask 5 | event_phase_mask 6 | |
| SMART_ACTION_RANDOM_PHASE_RANGE | 31 | event_phase_mask minimum | event_phase_mask maximum | | | | | |
| SMART_ACTION_RESET_GOBJECT | 32 | | | | | | | Resetea el gameobject |
| SMART_ACTION_CALL_KILLEDMONSTER | 33 | creature_template.entry | | | | | | Este es el ID de quest_template.RequiredNpcOrGo |
| SMART_ACTION_SET_INST_DATA | 34 | Field | Data | | Type (0 = SetData, 1 = SetBossState) | | | Establece Instance Data |
| SMART_ACTION_SET_INST_DATA64 | 35 | Field | | | | | | Establece Instance Data uint64 |
| SMART_ACTION_UPDATE_TEMPLATE | 36 | creature_template.entry | Update Level | | | | | Actualiza la creature_template al entry dado |
| SMART_ACTION_DIE | 37 | Milliseconds | | | | | | Mata al objetivo; si se establece param1, morirá tras param1 milisegundos. 0: sin retraso, el objetivo morirá al instante |
| SMART_ACTION_SET_IN_COMBAT_WITH_ZONE | 38 | Range in yards for all players to be forced into combat with the   creature. Only used in the open world. Leave as 0 if used in an instance. | | | | | | Pone a la creature en combate con su zona, se puede usar en instancias y mundo abierto. Útil para creatures dentro de instancias para que todos los jugadores entren en combate hasta que termine la pelea. |
| SMART_ACTION_CALL_FOR_HELP | 39 | Radius in yards that other creatures must be to acknowledge the cry for   help. | 0/1 (say calls for help text) | | | | | Si quieres que el NPC diga '%s calls for help!'. Usa 1 en param1, 0 para no mostrar mensaje. |
| SMART_ACTION_SET_SHEATH | 40 | Sheath (0-unarmed, 1-melee, 2-ranged) | | | | | | |
| SMART_ACTION_FORCE_DESPAWN | 41 | Despawn delay timer "ms" | Force Respawn Timer "s" | removeObjectFromWorld (0/1) | | | | Despawnea al objetivo tras param1 en milisegundos. Respawnea tras param2 en segundos. Elimina al objetivo del mundo si param3 es true. param1 y param2 no se pueden establecer si param3 está establecido. |
| SMART_ACTION_SET_INVINCIBILITY_HP_LEVEL | 42 | flat hp value | percent hp value | | | | | Si usas ambos parámetros, solo se usará el porcentaje. |
| SMART_ACTION_MOUNT_TO_ENTRY_OR_MODEL | 43 | creature_template.entry | creature_template.modelidx | | | | | Monta en el entry de creature (param1) O monta en el display de creature (param2) O ambos = 0 para desmontar |
| SMART_ACTION_SET_INGAME_PHASE_MASK | 44 | creature.phaseMask | | | | | | |
| SMART_ACTION_SET_DATA | 45 | Field | Data | | | | | Establece data para el objetivo, se puede usar con SMART_EVENT_DATA_SET |
| SMART_ACTION_MOVE_FORWARD | 46 | distance | | | | | | Mueve a uno mismo hacia delante la distancia especificada (point movement) |
| SMART_ACTION_SET_VISIBILITY | 47 | 0/1 | | | | | | Hace a la creature Visible = 1 o Invisible = 0 |
| SMART_ACTION_SET_ACTIVE | 48 | 0/1 | | | | | | Si una creature o GO se establece como activa, seguirá activa aunque no haya ningún jugador cerca. Ten cuidado, ya que necesita recursos adicionales (CPU/RAM) para mantenerla activa (otros objetos/creatures cercanos permanecen activos). |
| SMART_ACTION_ATTACK_START | 49 | | | | | | | Permite los golpes cuerpo a cuerpo básicos a la creature. |
| SMART_ACTION_SUMMON_GO | 50 | gameobject_template.entry | De-spawn time in seconds. | targetSummon (0/1) | summonType (0 - after a specified time OR when the summoner dies, 1 - after a specified time) | | | Spawnea un gameobject, usa target_type para establecer la posición de spawn; si se especifica una entidad como target y también se establecen coordenadas (target x,y,z), esas coordenadas se manejan como offset desde la posición del target; si targetSummon es 1, el target invocará el GO en la posición del actor |
| SMART_ACTION_KILL_UNIT | 51 | | | | | | | Mata la creature. |
| SMART_ACTION_ACTIVATE_TAXI | 52 | TaxiID | | | | | | Envía al jugador a una ruta de vuelo. Tienes que estar cerca del Flight Master que da el Taxi ID que necesitas. |
| SMART_ACTION_ESCORT_START | 53 | forcedMovement (0: none, 1: walk, 2: run) | waypoints.entry | canRepeat | quest_template.id | despawntime | ReactState (0=Passive, 1=Defensive, 2=Aggressive) | La creature inicia el movimiento de Escort. Usa la tabla waypoints para crear el movimiento. |
| SMART_ACTION_ESCORT_PAUSE | 54 | time (in ms) | | | | | | La creature pausa su movimiento de Escort durante el tiempo dado. |
| SMART_ACTION_ESCORT_STOP | 55 | despawnTime | quest_template.id | fail (0/1) | | | | La creature detiene su movimiento de Escort. |
| SMART_ACTION_ADD_ITEM | 56 | item_template.entry | count | | | | | Añade item(s) al jugador. |
| SMART_ACTION_REMOVE_ITEM | 57 | item_template.entry | count | | | | | Elimina item(s) del jugador. |
| SMART_ACTION_INSTALL_AI_TEMPLATE | 58 | TemplateID (see Predefined SAI templates below) | | | | | | |
| SMART_ACTION_SET_RUN | 59 | 0 = Off / 1 = On | | | | | | |
| SMART_ACTION_SET_FLY | 60 | fly (0/1) | speed | disable gravity (0/1) | | | | Solo funciona para creatures con inhabit air. |
| SMART_ACTION_SET_SWIM | 61 | 0 = Off / 1 = On | | | | | | |
| SMART_ACTION_TELEPORT | 62 | MapID | | | | | | Continúa esta acción con la columna TARGET_TYPE. Usa cualquier target_type (excepto 0), y usa target_x, target_y, target_z, target_o como coordenadas |
| SMART_ACTION_SET_COUNTER | 63 | counterID | value | reset (0/1) | | | | Si reset es 0, el counter con el ID especificado se incrementa en el valor dado; si reset es 1, el counter se establece al valor. |
| SMART_ACTION_STORE_TARGET_LIST | 64 | varID | | | | | | |
| SMART_ACTION_ESCORT_RESUME | 65 | | | | | | | La creature continúa su movimiento de Escort. |
| SMART_ACTION_SET_ORIENTATION | 66 | Quick Change | Random orientation? (0/1) | Turning Angle (degrees) - The value will turn the creature counterclockwise. target_type must be NONE | | | | Se usa para alterar la orientación de la fuente. Depende del target del script. Si SMART_TARGET_SELF, la orientación será la misma que en HomePosition; para SMART_TARGET_POSITION necesitas establecer target_o: 0 = North, West = 1.5, South = 3, East = 4.5 |
| SMART_ACTION_CREATE_TIMED_EVENT | 67 | id | InitialMin | InitialMax | RepeatMin(only if it repeats) | RepeatMax(only if it repeats) | chance | |
| SMART_ACTION_PLAYMOVIE | 68 | entry | | | | | | |
| SMART_ACTION_MOVE_TO_POS | 69 | PointId | isTransport (0 or 1) | controlled (0 or 1) | ContactDistance | CombatReach 0/1 (Move until contact is made with the unit, if ContactDistance > 0, then it will be added to it) | disableForceDestination  (0 or 1) - disable to let the creature reaching the coordinates using the normal path | PointId es llamado por SMART_EVENT_MOVEMENTINFORM. Continúa esta acción con la columna TARGET_TYPE. Usa cualquier target_type, y usa target_x, target_y, target_z como coordenadas; si se especifica una entidad como target y también se establecen coordenadas (target x,y,z), esas coordenadas se manejan como offset desde la posición del target |
| SMART_ACTION_RESPAWN_TARGET | 70 | Respawntime in seconds | | | | | | |
| SMART_ACTION_EQUIP | 71 | creature_equip_template.ID | Slotmask | Slot1 (item_template.entry) | Slot2 (item_template.entry) | Slot3 (item_template.entry) | | solo se enviarán al cliente los slots cuya máscara esté establecida, los bits son 1, 2, 4; dejar la máscara en 0 equivale a la máscara 7 (enviar todos); Slots1-3 solo se usan si no se establece Param1 |
| SMART_ACTION_CLOSE_GOSSIP | 72 | | | | | | | Cierra la ventana de gossip. |
| SMART_ACTION_TRIGGER_TIMED_EVENT | 73 | id(>1) | | | | | | |
| SMART_ACTION_REMOVE_TIMED_EVENT | 74 | id(>1) | | | | | | |
| SMART_ACTION_ADD_AURA | 75 | SpellId | | | | | | Añade un aura al/los jugador(es). Usa target_type 17 para hacer un aura AoE. |
| SMART_ACTION_OVERRIDE_SCRIPT_BASE_OBJECT | 76 | | | | | | | ADVERTENCIA: PUEDE CRASHEAR EL CORE, no lo uses si no sabes lo que haces |
| SMART_ACTION_RESET_SCRIPT_BASE_OBJECT | 77 | | | | | | | |
| SMART_ACTION_CALL_SCRIPT_RESET | 78 | | | | | | | |
| SMART_ACTION_SET_RANGED_MOVEMENT | 79 | attackDistance | attackAngle | | | | | Establece el movimiento para seguir a un rango específico del objetivo. |
| SMART_ACTION_CALL_TIMED_ACTIONLIST | 80 | EntryOrGuid * 100 (entryorguid with 00 added after the entry, or 01,   02, 03 etc. for multiple action lists) | timer update type(0 OOC, 1 IC, 2 ALWAYS) | allowOverride (0 - Must finish current actionlist, 1 - Allow starting new actionlist during previous actionlist) | | | | |
| SMART_ACTION_SET_NPC_FLAG | 81 | creature_template.npcflag | | | | | | |
| SMART_ACTION_ADD_NPC_FLAG | 82 | creature_template.npcflag | | | | | | |
| SMART_ACTION_REMOVE_NPC_FLAG | 83 | creature_template.npcflag | | | | | | |
| SMART_ACTION_SIMPLE_TALK | 84 | creature_text.GroupID | | | | | | Hace que un jugador diga un texto. SMART_EVENT_TEXT_OVER no se dispara y no se pueden usar susurros. |
| SMART_ACTION_SELF_CAST | 85 | SpellId | [castFlags](#cast-flags) | [triggeredFlags](#triggered-flags) | limitTargets (0 = all) | | | Hace que el objetivo lance el hechizo sobre sí mismo. |
| SMART_ACTION_CROSS_CAST | 86 | SpellID | castFlags | CasterTargetType (caster is selected here, use it as target_type) | CasterTarget (target_param1) | CasterTarget (target_param2) | CasterTarget (target_param3) | Esta acción se usa para hacer que el caster seleccionado (en CasterTargetType) lance el hechizo. El objetivo real se introduce en target_type como de costumbre. |
| SMART_ACTION_CALL_RANDOM_TIMED_ACTIONLIST | 87 | EntryOrGuid 1 (entryorguid * 100 + n) | EntryOrGuid 2 (entryorguid * 100 + n) | EntryOrGuid 3 (entryorguid * 100 + n) | EntryOrGuid 4 (entryorguid * 100 + n) | EntryOrGuid 5 (entryorguid * 100 + n) | EntryOrGuid 6 (entryorguid * 100 + n) | Seleccionará una entrada de las proporcionadas. 0 se ignora. |
| SMART_ACTION_CALL_RANDOM_RANGE_TIMED_ACTIONLIST | 88 | EntryOrGuid 1 (entryorguid * 100 + n) | EntryOrGuid 2 (entryorguid * 100 + n) | | | | | 0 se ignora. |
| SMART_ACTION_RANDOM_MOVE | 89 | Radius | | | | | | La creature se mueve a una posición aleatoria en el radio dado. Si el radio es 0, detiene el movimiento |
| SMART_ACTION_SET_UNIT_FIELD_BYTES_1 | 90 | Value | Type | | | | | |
| SMART_ACTION_REMOVE_UNIT_FIELD_BYTES_1 | 91 | Value | Type | | | | | |
| SMART_ACTION_INTERRUPT_SPELL | 92 | With delay (0/1) | SpellId | Instant (0/1) | | | | Esta acción te permite interrumpir el hechizo que se está lanzando actualmente. Si no estableces el spellId, el core encontrará el hechizo actual según los valores withDelay y withInstant. |
| SMART_ACTION_SEND_GO_CUSTOM_ANIM | 93 | animprogress (0-255) | | | | | | |
| SMART_ACTION_SET_DYNAMIC_FLAG | 94 | creature_template.dynamicflags | | | | | | |
| SMART_ACTION_ADD_DYNAMIC_FLAG | 95 | creature_template.dynamicflags | | | | | | |
| SMART_ACTION_REMOVE_DYNAMIC_FLAG | 96 | creature_template.dynamicflags | | | | | | |
| SMART_ACTION_JUMP_TO_POS | 97 | Speed XY | Speed Z | selfJump (0/1) | | | | Si selfJump es 1, el actor saltará al objetivo (puedes añadir un offset desde la posición del objetivo especificando también las coordenadas del objetivo); si selfJump es 0, la creature objetivo saltará a la posición del objetivo |
| SMART_ACTION_SEND_GOSSIP_MENU | 98 | gossip_menu.entry | gossip_menu.text_id<br/>(same value as npc_text.ID) | | | | | Se puede usar junto con 'SMART_EVENT_GOSSIP_HELLO' para establecer un gossip personalizado. |
| SMART_ACTION_GO_SET_LOOT_STATE | 99 | LootState (0 - Not ready, 1 - Ready, 2 - Activated, 3 - Just deactivated) | | | | | | |
| SMART_ACTION_SEND_TARGET_TO_TARGET | 100 | Id | | | | | | Envía los targets previamente almacenados con SMART_ACTION_STORE_TARGET a otro npc/go; el otro npc/go puede acceder a ellos como si fuera su propia lista almacenada |
| SMART_ACTION_SET_HOME_POS | 101 | 0: if the target is a creature, set it's current position as it's new   home position; if the target is SMART_TARGET_POSITION, use this position as   new home position for the actor<br/>1: if the target is a creature,   reset it's home position to the one from the DB; if the target is   SMART_TARGET_POSITION, reset the actor's home position to the one from the DB   (the actual values of the target position are ignored) | | | | | | |
| SMART_ACTION_SET_HEALTH_REGEN | 102 | 0/1 | | | | | | Activa o desactiva la regeneración de salud de la creature actual. |
| SMART_ACTION_SET_ROOT | 103 | 0/1 | | | | | | Activa o desactiva el movimiento de la creature |
| SMART_ACTION_SET_GO_FLAG | 104 | gameobject_template_addon.flags | | | | | | oldFlag = newFlag |
| SMART_ACTION_ADD_GO_FLAG | 105 | gameobject_template_addon.flags | | | | | | oldFlag \|= newFlag |
| SMART_ACTION_REMOVE_GO_FLAG | 106 | gameobject_template_addon.flags | | | | | | oldFlag &= ~newFlag |
| SMART_ACTION_SUMMON_CREATURE_GROUP | 107 | creature_summon_groups.groupId | attackInvoker (0/1) | attackScriptOwner (0/1) | | | | Usa la tabla creature_summon_groups. El target de SAI no tiene efecto, usa 0 |
| SMART_ACTION_SET_POWER | 108 | Power type | New power | | | | | |
| SMART_ACTION_ADD_POWER | 109 | Power type | Power to add | | | | | |
| SMART_ACTION_REMOVE_POWER | 110 | Power type | Power to remove | | | | | |
| SMART_ACTION_GAME_EVENT_STOP | 111 | game_event.eventEntry | | | | | | |
| SMART_ACTION_GAME_EVENT_START | 112 | game_event.eventEntry | | | | | | |
| SMART_ACTION_START_CLOSEST_WAYPOINT | 113 | pathId1 | pathId2 | repeat (0: no, 1: yes) | forcedMovement (0: none, 1: walk, 2: run) | pathSource (0: waypoint_data, 1: SmartScript waypoints) | | La creature inicia el movimiento de Waypoint usando el path id más cercano en el rango entre pathId1 y pathId2. Usa la tabla waypoints para crear el movimiento. |
| SMART_ACTION_RISE_UP | 114 | distance | | | | | | Se mueve hacia arriba la distancia especificada (advertencia: TC 3.3.5 usa otra acción aquí: SMART_ACTION_MOVE_OFFSET) |
| SMART_ACTION_RANDOM_SOUND | 115 | soundId1 | soundId2 | soundId3 | soundId4 | onlySelf (0/1) | distance | |
| SMART_ACTION_SET_CORPSE_DELAY | 116 | timer (secs) | | | | | | |
| SMART_ACTION_DISABLE_EVADE | 117 | 0/1 (1 = disabled, 0 = enabled) | | | | | | |
| SMART_ACTION_GO_SET_GO_STATE | 118 | state | | | | | | |
| SMART_ACTION_SET_SIGHT_DIST | 121 | SightDistance | | | | | | |
| SMART_ACTION_FLEE | 122 | FleeTime | | | | | | |
| SMART_ACTION_ADD_THREAT | 123 | +threat | -threat | | | | | |
| SMART_ACTION_LOAD_EQUIPMENT | 124 | Id | force | | | | | |
| SMART_ACTION_TRIGGER_RANDOM_TIMED_EVENT | 125 | id min range | id max range | | | | | |
| SMART_ACTION_REMOVE_ALL_GAMEOBJECTS | 126 | | | | | | | |
| SMART_ACTION_SPAWN_SPAWNGROUP | 131 | groupId ([spawn_group_template](spawn_group_template).groupId) | ignoreRespawn (0/1) - if 1, pending respawn timers are cleared | force (0/1) - if 1, existing spawns are replaced with fresh ones | | | | Spawnea todas las creatures y gameobjects pertenecientes al spawn group especificado. Requiere un contexto de WorldObject (script de creature o gameobject). |
| SMART_ACTION_DESPAWN_SPAWNGROUP | 132 | groupId ([spawn_group_template](spawn_group_template).groupId) | deleteRespawnTimes (0/1) - if 1, pending respawn timers are also cleared | | | | | Despawnea todas las creatures y gameobjects pertenecientes al spawn group especificado. Requiere un contexto de WorldObject (script de creature o gameobject). |
| SMART_ACTION_INVOKER_CAST | 134 | SpellId | CastFlags | TriggerFlags | LimitTargets - 0: all targets | | | Hace que el tipo de invoker de nuestra acción lance un hechizo sobre nuestro target type |
| SMART_ACTION_PLAY_CINEMATIC | 135 | entry | | | | | | |
| SMART_ACTION_SET_MOVEMENT_SPEED | 136 | movementType | speedInteger | speedFraction | | | | MOVE_WALK = 0, MOVE_RUN  = 1, MOVE_RUN_BACK = 2, MOVE_SWIM = 3, MOVE_SWIM_BACK= 4, MOVE_TURN_RATE= 5, MOVE_FLIGHT = 6, MOVE_FLIGHT_BACK = 7, MOVE_PITCH_RATE = 8 |
| SMART_ACTION_SET_HEALTH_PCT | 142 | percent | | | | | | |
| SMART_ACTION_MOVE_TO_POS_TARGET | 201 | pointId | disableForceDestination  (0 or 1) - disable to let the creature reaching the coordinates using the normal path | | | | | |
| SMART_ACTION_EXIT_VEHICLE | 203 | | | | | | | |
| SMART_ACTION_SET_UNIT_MOVEMENT_FLAGS | 204 | flags | | | | | | |
| SMART_ACTION_SET_COMBAT_DISTANCE | 205 | combatDistance | | | | | | |
| SMART_ACTION_DISMOUNT | 206 | | | | | | | |
| SMART_ACTION_SET_HOVER | 207 | 0/1 | | | | | | |
| SMART_ACTION_ADD_IMMUNITY | 208 | type | id | value | | | | |
| SMART_ACTION_REMOVE_IMMUNITY | 209 | type | id | value | | | | |
| SMART_ACTION_FALL | 210 | | | | | | | |
| SMART_ACTION_SET_EVENT_FLAG_RESET | 211 | allowPhaseReset (0=Disable, 1=Enable) | | | | | | |
| SMART_ACTION_STOP_MOTION | 212 | stopMoving | movementExpired | | | | | |
| SMART_ACTION_NO_ENVIRONMENT_UPDATE | 213 | | | | | | | |
| SMART_ACTION_ZONE_UNDER_ATTACK | 214 | | | | | | | |
| SMART_ACTION_LOAD_GRID | 215 | | | | | | | Carga el grid en las coordenadas del objetivo. Funciona tanto para creatures como para game objects. |
| SMART_ACTION_MUSIC | 216 | SoundId | onlySelf | type | | | | Reproduce el archivo de sonido especificado como música. Type puede ser uno de estos valores:<br/>0: reproduce la música para el/los objetivo(s) especificado(s)<br/>1: reproduce la música para todos los jugadores de toda la zona<br/>2: reproduce la música para todos los jugadores del área. |
| SMART_ACTION_RANDOM_MUSIC | 217 | SoundId1 | SoundId2 | SoundId3 | SoundId4 | onlySelf | type | Reproduce aleatoriamente uno de los archivos de sonido especificados como música. Type puede ser uno de estos valores:<br/>0: reproduce la música para el/los objetivo(s) especificado(s)<br/>1: reproduce la música para todos los jugadores de toda la zona<br/>2: reproduce la música para todos los jugadores del área. |
| SMART_ACTION_CUSTOM_CAST | 218 | spellId | castFlag | bp0 | bp1 | bp2 | | |
| SMART_ACTION_CONE_SUMMON | 219 | entry | Duration (ms)<br/>0 = permanent | Distance between rings (yards) | Distance between each summons in a row (yards) | Length of the cone (yards) | Width of the cone (angle 1°-360°) | Te permite spawnear creatures en cono (como se ve en expansiones posteriores). Útil para aoes de cono personalizados |
| SMART_ACTION_PLAYER_TALK | 220 | acore_string.id | yell? (0/1) | | | | | Hace que el jugador diga algo |
| SMART_ACTION_VORTEX_SUMMON | 221 | entry | Duration (ms)<br/>0 = permanent | Spiral scaling | Spiral appearance | range max | phi_delta | Te permite invocar creatures en una espiral (/vórtice) personalizable. Los parámetros pueden ser confusos, parámetros de ejemplo para probar: 5000 - duración de la invocación, 5 - Spiral Scaling, 25 - spiral appearance, 60 - range max, 40 - phi delta |
| SMART_ACTION_CU_ENCOUNTER_START | 222 | | | | | | | Resetea todos los cooldowns y elimina los debuffs de exhausted cuando se llama a la acción |
| SMART_ACTION_DO_ACTION | 223 | ActionId | | | | | | Permite llamar a un DoAction en el código |
| SMART_ACTION_ATTACK_STOP | 224 | | | | | | | Detiene el cuerpo a cuerpo, el lanzamiento de hechizos durante el combate, la persecución del objetivo y el encaramiento |
| SMART_ACTION_SET_GUID | 225 | 0/1 (0 = Self Guid, 1 = Invoker Guid) | Index | | | | | Permite al objetivo realizar una acción similar a DO_ACTION, pero permite enviar un guid |
| SMART_ACTION_SCRIPTED_SPAWN | 226 | state (0: Disable Respawn and await script; 1: Respawn Once; 2: Respawn and Enable Respawning) | Minimum Spawn Timer (Delay in seconds until first spawn, if 0 respawn immediately) | Maximum Spawn Timer (Delay in seconds until first spawn, if 0 respawn immediately) | Respawn Delay (Delay in seconds to respawn after corpse is removed, if 0 use DB values) | Corpse Delay (Delay in seconds until the corpse despawns, if 0 use default) | Don't Despawn (if 1, won't despawn when state = 0) | Configura y permite el uso de un sistema de Scripted Spawn de SmartAI, que nos permite mantener GUIDs únicos despawneados hasta que un script los active. Consulta la quest 'The Deadliest Trap Ever Laid' para ver ejemplos de su uso. |
| SMART_ACTION_SET_SCALE | 227 | scale - this value is the percentage of the new scale the targets will take. 100 = default | | | | | | Establece la escala para las creatures objetivo |
| SMART_ACTION_SUMMON_RADIAL | 228 | summonEntry - CreatureID to be summoned | summonDuration - duration in ms which the summons will despawn after, if 0 then despawn on death | repetitions - amount of creatures to be summoned | startAngle - offset in degrees, 0: same as source | stepAngle - how many degrees to turn for each summon | dist - distance offset | Invoca un conjunto de creatures en un patrón radial, con el cambio de orientación especificado en los parámetros |
| SMART_ACTION_PLAY_SPELL_VISUAL | 229 | visualId - can be found within SpellVisual.dbc | | | | | | Hace que los objetivos reproduzcan el VisualKit ID especificado |
| SMART_ACTION_FOLLOW_GROUP | 230 | Follow State (0: Stop Follow, 1: Start Follow) | Smart Follow Type | Distance from Leader divided by 100 (300 = 3.f yards) | | | | Hace que los objetivos sigan a la creature fuente en la formación especificada. Ver Smart Follow Types abajo |
| SMART_ACTION_ORIENTATION_TARGET | 231 | Type (0: Reset to default, 1: Use target.o parameter, 2: Targets face this unit, 3: Use parameters to target a specific creature) | target_type | target_param1 | target_param2 | target_param3 | target_param4 | Hace que los objetivos se orienten en una dirección específica. Si type = 3, usa los parámetros como si fuera un smart target y se orientarán hacia la unidad recién seleccionada |
| SMART_ACTION_WAYPOINT_START | 232 | pathId (waypoint_data.id) | repeat (0: no, 1: yes) | pathSource (0: waypoint_data, 1: waypoints) | | | | La creature inicia el movimiento de Waypoint. Usa la tabla waypoint_data para crear el movimiento. |
| SMART_ACTION_WAYPOINT_DATA_RANDOM | 233 | pathId1 | pathId2 | repeat (0: no, 1: yes) | | | | La creature inicia el movimiento de Waypoint usando un path id aleatorio en el rango entre pathId1 y pathId2. Usa la tabla waypoint_data para crear el movimiento. |
| SMART_ACTION_MOVEMENT_STOP | 234 | | | | | | | Llama al MovementGenerator para detener el movimiento |
| SMART_ACTION_MOVEMENT_PAUSE | 235 | timer | | | | | | Llama al MovementGenerator para pausar el movimiento, similar a cuando un jugador interactúa con una creature en patrulla. El timer no está totalmente implementado |
| SMART_ACTION_MOVEMENT_RESUME | 236 | timerOverride | | | | | | Llama al MovementGenerator para reanudar el movimiento. No está totalmente implementado |
| SMART_ACTION_WORLD_SCRIPT | 237 | eventId | param | | | | | Llama a WorldState::HandleExternalEvent(WorldStateEvent eventId, uint32 param) |
| SMART_ACTION_DISABLE_REWARD | 238 | reputation (0/1) | loot (0/1) | | | | | Permite desactivar la recompensa de una creature. |
| SMART_ACTION_SET_ANIM_TIER | 239 | 0 = Ground, 1 = Swim, 2 = Hover, 3 = Fly, 4 = Submerged | | | | | | Permite establecer el anim tier de una creature. |
| SMART_ACTION_SET_GOSSIP_MENU | 240 | gossipMenuId | | | | | | Modifica el gossip menu ID del objetivo. |
| SMART_ACTION_SUMMON_GAMEOBJECT_GROUP | 241 | groupId (gameobject_summon_groups.groupId) | | | | | | Invoca todos los gameobjects del grupo especificado de la tabla [gameobject\_summon\_groups](gameobject_summon_groups) que coincidan con el entry del objeto fuente y el summonerType. |
| SMART_ACTION_INC_DATA | 242 | Field | Increment | | | | | Incrementa el campo de data especificado para el objetivo en el valor de incremento dado, y luego dispara [SMART_EVENT_DATA_SET](#eventtype). |
### Predefined SAI templates

| Description Name | Value (Param1) | Param2 | Param3 | Param4 | Param5 | Param6 | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SMARTAI_TEMPLATE_BASIC | 0 | | | | | | |
| SMARTAI_TEMPLATE_CASTER | 1 | spellid | repeatMin | repeatMax | range | manaPCT | +JOIN: target_param1 as castFlag |
| SMARTAI_TEMPLATE_TURRET | 2 | spellid | repeatMin | repeatMax | range | manaPCT | +JOIN: target_param1 as castflag |
| SMARTAI_TEMPLATE_PASSIVE | 3 | | | | | | |
| SMARTAI_TEMPLATE_CAGED_GO_PART | 4 | creatureID | give credit at point end (0/1) | | | | |
| SMARTAI_TEMPLATE_CAGED_NPC_PART | 5 | gameObjectID | despawntime | run (0/1) | dist | TextGroupID | |

### target_type

| Name | Value | target_param1 | target_param2 | target_param3 | target_param4 | target_x | target_y | target_z | target_o | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SMART_TARGET_NONE | 0 | | | | | | | | | Ninguno. |
| SMART_TARGET_SELF | 1 | | | | | | | | | Lanzamiento sobre uno mismo. |
| SMART_TARGET_VICTIM | 2 | | | | | | | | | Nuestro objetivo actual. (es decir: el de mayor aggro) |
| SMART_TARGET_HOSTILE_SECOND_AGGRO | 3 | Max Range (0: Unlimited) | Player Only (0/1) | Power Type + 1 | Missing Aura | | | | | Segundo mayor aggro. |
| SMART_TARGET_HOSTILE_LAST_AGGRO | 4 | Max Range (0: Unlimited) | Player Only (0/1) | Power Type + 1 | Missing Aura | | | | | El último en aggro. |
| SMART_TARGET_HOSTILE_RANDOM | 5 | Max Range (0: Unlimited) | Player Only (0/1) | Power Type + 1 | Missing Aura | | | | | Cualquier objetivo aleatorio de nuestra lista de amenaza. |
| SMART_TARGET_HOSTILE_RANDOM_NOT_TOP | 6 | Max Range (0: Unlimited) | Player Only (0/1) | Power Type + 1 | Missing Aura | | | | | Cualquier objetivo aleatorio excepto el de mayor amenaza. |
| SMART_TARGET_ACTION_INVOKER | 7 | | | | | | | | | La unidad que causó que ocurriera este evento. |
| SMART_TARGET_POSITION | 8 | | | | | x | y | z | o | Usa xyz de los parámetros del evento. |
| SMART_TARGET_CREATURE_RANGE | 9 | creature_template.entry (0 any) | minDist | maxDist | alive state (1 alive, 2 dead, 0 both) | | | | | Todas las creatures con el ID especificado dentro del rango especificado y el alive state especificado. |
| SMART_TARGET_CREATURE_GUID | 10 | creature.guid | creature_template.entry | getFromHashMap (0/1, this does not work in instances!) | | | | | | Creature con el GUID especificado y/o el ID de creature template especificado. |
| SMART_TARGET_CREATURE_DISTANCE | 11 | creature_template.entry (0 any) | maxDist | alive state (1 alive, 2 dead, 0 both) | | | | | | Todas las creatures con el ID especificado dentro de la distancia especificada y el alive state especificado. |
| SMART_TARGET_STORED | 12 | id | | | | | | | | Usa el/los target(s) pre-almacenado(s) |
| SMART_TARGET_GAMEOBJECT_RANGE | 13 | gameobject_template.entry (0 any) | minDist | maxDist | | | | | | Todos los game objects con el ID especificado dentro del rango especificado. |
| SMART_TARGET_GAMEOBJECT_GUID | 14 | gameobject.guid | gameobject_template.entry | getFromHashMap (0/1, this does not work in instances!) | | | | | | Objeto con el GUID especificado y/o el ID de game object template especificado. |
| SMART_TARGET_GAMEOBJECT_DISTANCE | 15 | gameobject_template.entry (0 any) | maxDist | | | | | | | Todos los objetos con el ID especificado dentro de la distancia especificada. |
| SMART_TARGET_INVOKER_PARTY | 16 | | | | | | | | | Los miembros del grupo del invoker |
| SMART_TARGET_PLAYER_RANGE | 17 | minDist | maxDist | maxCount | | | | | When target.o is set and it didnt find any targets in min-max range, it   will try all possible targets in max range instead. | Todos los jugadores hasta maxCount dentro del rango especificado. Excluyendo GMs y muertos. |
| SMART_TARGET_PLAYER_DISTANCE | 18 | maxDist | | | | | | | | Todos los jugadores dentro de la distancia especificada. |
| SMART_TARGET_CLOSEST_CREATURE | 19 | creature_template.entry (0 any) | maxDist (Can be from 0-100 yards) | dead? (0/1) | | | | | | La creature más cercana con el ID especificado dentro del rango especificado. |
| SMART_TARGET_CLOSEST_GAMEOBJECT | 20 | gameobject_template.entry (0 any) | maxDist (Can be from 0-100 yards) | | | | | | | El objeto más cercano con el ID especificado dentro del rango especificado. |
| SMART_TARGET_CLOSEST_PLAYER | 21 | maxDist | | | | | | | | El jugador más cercano dentro del rango especificado. |
| SMART_TARGET_ACTION_INVOKER_VEHICLE | 22 | | | | | | | | | El vehículo de la unidad que causó que ocurriera este evento |
| SMART_TARGET_OWNER_OR_SUMMONER | 23 | use owner of owner (0/1) | | | | | | | | El propietario o invocador de la unidad |
| SMART_TARGET_THREAT_LIST | 24 | maxDist (0 any) | | | | | | | | Todas las unidades de la lista de amenaza de la creature dentro de la distancia especificada si maxDist > 0 |
| SMART_TARGET_CLOSEST_ENEMY | 25 | maxDist | playerOnly (0/1) | | | | | | | Cualquier objetivo atacable (creature o jugador) dentro de maxDist |
| SMART_TARGET_CLOSEST_FRIENDLY | 26 | maxDist | playerOnly (0/1) | | | | | | | Cualquier unidad aliada (creature, jugador o mascota) dentro de maxDist |
| SMART_TARGET_LOOT_RECIPIENTS | 27 | | | | | | | | | Todos los jugadores que han marcado esta creature (para el kill credit) |
| SMART_TARGET_FARTHEST | 28 | maxDist | playerOnly (0/1) | isInLos (0/1) | minDist | | | | | La unidad más lejana de la lista de amenaza |
| SMART_TARGET_VEHICLE_PASSENGER | 29 | seat number (vehicle can target it's own accessory) | | | | | | | | |
| SMART_TARGET_PLAYER_WITH_AURA | 201 | spellID | Negative (0/1) | MaxDist | MinDist | | | | Number to resize the target list | Apunta a jugadores con o sin el aura |
| SMART_TARGET_RANDOM_POINT | 202 | range (yards) | amount (for summoning creature) | self as middle (0/1)<br/>else use xyz | | | | | | Esto solo funciona con SMART_ACTION_SUMMON_CREATURE, SMART_ACTION_MOVE_TO_POS y SMART_ACTION_JUMP_TO_POS |
| SMART_TARGET_ROLE_SELECTION | 203 | rangeMax (yards) | TargetMask (Tanks (1), Healer (2) Damage (4)) | Resize list | | | | | | Apunta a un rol Tank/Healer/DPS. Basado en la especialización de los jugadores. |
| SMART_TARGET_SUMMONED_CREATURES | 204 | [creature_template.Entry](creature_template#entry) | | | | | | | | |
| SMART_TARGET_INSTANCE_STORAGE | 205 | data index | Type (creature (1), gameobject (2)) | | | | | | | |
| SMART_TARGET_FORMATION | 206 | Type (0: members only, 1: leader only, 2: all) | creature_template.entry (0: Any) | ExcludeSelf (0/1) | | | | | | Apunta a los miembros de la formación de la creature. |

### comment

Comentar en SAI usa una plantilla que es la siguiente: (con un ejemplo)

"Creature name - Event - Action"

"Minion of Gurok - On spawn - Set Random Movement"

**Notas rápidas:**

- Actualiza siempre *creature_template*, *gameobject_template* o *areatrigger_scripts* con:

```sql
UPDATE `creature_template` SET `AIName` = 'SmartAI' WHERE `entry` = y;

UPDATE `gameobject_template` SET `AIName` = 'SmartGameObjectAI' WHERE `entry` = y;

INSERT INTO `areatrigger_scripts` (`entry`, `ScriptName`) VALUES (y, 'SmartTrigger');
```

- Si la creature o GO está dentro de un dungeon, establece *event_flags* según la dificultad de la instancia (heroico, 25 man, etc.).

**En caso de duda sobre un *Event*, *Action* o *Target*, revisa el código fuente (archivos *src/server/game/AI/SmartScripts*; principalmente \*SmartScript.cpp**)

### Cast Flags

| Name | Flag | Hex | Comment |
| --- | --- | --- | --- |
| SMARTCAST_INTERRUPT_PREVIOUS | 1 | 0x001 | Interrumpe cualquier lanzamiento de hechizo |
| SMARTCAST_TRIGGERED | 2 | 0x002 | Triggered (esto hace que el hechizo cueste cero maná y no tenga tiempo de lanzamiento) |
| SMARTCAST_AURA_NOT_PRESENT | 32 | 0x020 | Solo lanza el hechizo si el objetivo no tiene un aura del hechizo |
| SMARTCAST_COMBAT_MOVE | 64 | 0x040 | Impide el movimiento de combate al lanzar, lo permite si falla por rango, maná o LOS |
| SMARTCAST_THREATLIST_NOT_SINGLE | 128 | 0x080 | Solo lanza si la lista de amenaza de la fuente es mayor que uno. Esto incluye las mascotas |
| SMARTCAST_TARGET_POWER_MANA | 256 | 0x100 | Solo lanza si el objetivo tiene el power type maná |
| SMARTCAST_ENABLE_COMBAT_MOVE_ON_LOS | 512 | 0x200 | Activa el movimiento de persecución en combate cuando el hechizo falla por línea de visión. Usar con SMARTCAST_COMBAT_MOVE. |
| SMARTCAST_MAIN_SPELL | 1024 | 0x400 | Usar con SMARTCAST_COMBAT_MOVE para establecer la distancia de ataque según el rango del hechizo |

### Triggered Flags

| Name | Flag | Hex | Comment |
| --- | --- | --- | --- |
| TRIGGERED_NONE | 0 | 0x00000000 | No triggered |
| TRIGGERED_IGNORE_GCD | 1 | 0x00000001 | Ignorará el GCD |
| TRIGGERED_IGNORE_SPELL_AND_CATEGORY_CD | 2 | 0x00000002 | Ignorará los cooldowns de Spell y Category |
| TRIGGERED_IGNORE_POWER_AND_REAGENT_COST | 4 | 0x00000004 | Ignorará el coste de power y reagent |
| TRIGGERED_IGNORE_CAST_ITEM | 8 | 0x00000008 | No quitará el cast item ni actualizará el criterio de achievement relacionado |
| RIGGERED_IGNORE_AURA_SCALING | 16 | 0x00000010 | Ignorará el aura scaling |
| TRIGGERED_IGNORE_CAST_IN_PROGRESS | 32 | 0x00000020 | No comprobará si hay un cast en progreso |
| TRIGGERED_IGNORE_COMBO_POINTS | 64 | 0x00000040 | Ignorará el requisito de combo points |
| TRIGGERED_CAST_DIRECTLY | 128 | 0x00000080 | En Spell::prepare, se lanzará directamente sin establecer los contenedores para el hechizo ejecutado |
| TRIGGERED_IGNORE_AURA_INTERRUPT_FLAGS | 256 | 0x00000100 | Ignorará las auras interrumpibles al lanzar |
| TRIGGERED_IGNORE_SET_FACING | 512 | 0x00000200 | No ajustará el encaramiento al objetivo (si lo hay) |
| TRIGGERED_IGNORE_SHAPESHIFT | 1024 | 0x00000400 | Ignorará las comprobaciones de shapeshift |
| TRIGGERED_IGNORE_CASTER_AURASTATE | 2048 | 0x00000800 | Ignorará los aura states del caster, incluyendo los requisitos de combate y el estado de muerte |
| TRIGGERED_IGNORE_CASTER_MOUNTED_OR_ON_VEHICLE | 8192 | 0x00002000 | Ignorará las restricciones de estar montado/en vehículo |
| TRIGGERED_IGNORE_CASTER_AURAS | 65536 | 0x00010000 | Ignorará las restricciones o requisitos de auras del caster |
| TRIGGERED_DISALLOW_PROC_EVENTS | 131072 | 0x00020000 | No permite eventos de proc del hechizo triggered (por defecto) |
| TRIGGERED_DONT_REPORT_CAST_ERROR | 262144 | 0x00040000 | Devolverá SPELL_FAILED_DONT_REPORT en las funciones CheckCast |
| TRIGGERED_FULL_MASK | 524287 | 0x0007FFFF | Todos los triggered flags |
| TRIGGERED_IGNORE_EQUIPPED_ITEM_REQUIREMENT | 524288 | 0x00080000 | Ignorará los requisitos de item equipado |
| TRIGGERED_NO_PERIODIC_RESET | 1048576 | 0x00100000 | El tick del aura periódica no se reseteará al sobrescribir |
| TRIGGERED_IGNORE_EFFECTS | 2097152 | 0x00200000 | Ignora los efectos del hechizo - usado para los portales de ritual |
| TRIGGERED_FULL_DEBUG_MASK | 4294967295 | 0xFFFFFFFF | |

**AVISO:** si triggeredFlags = 0, el lanzamiento se disparará con TRIGGERED_FULL_MASK = 524287.

### React States

| Name | Value | Comment |
| --- | --- | --- |
| REACT_PASSIVE | 0 | No se defiende ni ataca en absoluto. No hace nada. |
| REACT_DEFENSIVE | 1 | Solo contraataca cuando es atacada. |
| REACT_AGGRESSIVE | 2 | Atacará si está en la lista de amenaza y dentro del radio de amenaza. (por defecto) |

### Summon Types

| Name | Value | Comment |
| --- | --- | --- |
| TEMPSUMMON_TIMED_OR_DEAD_DESPAWN | 1 | Despawnea tras un tiempo especificado O cuando la creature desaparece. |
| TEMPSUMMON_TIMED_OR_CORPSE_DESPAWN | 2 | Despawnea tras un tiempo especificado O cuando la creature muere. |
| TEMPSUMMON_TIMED_DESPAWN | 3 | Despawnea tras un tiempo especificado. |
| TEMPSUMMON_TIMED_DESPAWN_OUT_OF_COMBAT | 4 | Despawnea tras un tiempo especificado después de que la creature esté fuera de combate. |
| TEMPSUMMON_CORPSE_DESPAWN | 5 | Despawnea al instante tras la muerte. |
| TEMPSUMMON_CORPSE_TIMED_DESPAWN | 6 | Despawnea tras un tiempo especificado después de la muerte. |
| TEMPSUMMON_DEAD_DESPAWN | 7 | Despawnea cuando la creature desaparece. |
| TEMPSUMMON_MANUAL_DESPAWN | 8 | Despawnea cuando se llama a UnSummon() (o a la acción Force Despawn). |

### Smart Follow Types

| Name | Value | Comment |
| --- | --- | --- |
| FOLLOW_TYPE_CIRCLE | 1 | 360º grados alrededor del líder. 90º grados es el ángulo máximo. |
| FOLLOW_TYPE_SEMI_CIRCLE_BEHIND | 2 | 180º grados detrás del líder. |
| FOLLOW_TYPE_SEMI_CIRCLE_FRONT | 3 | 180º grados delante del líder. |
| FOLLOW_TYPE_LINE | 4 | Front \-\> Back \-\> Front \-\> Back. |
| FOLLOW_TYPE_COLUMN | 5 | Left \-\> Right \-\> Left \-\> Right. |
| FOLLOW_TYPE_ANGULAR | 6 | Formación tipo bandada de gansos, 135º y 225º grados detrás del líder. |

### Power Types

| Name | Value |
| --- | --- |
| POWER_MANA | 0 |
| POWER_RAGE | 1 |
| POWER_FOCUS | 2 |
| POWER_ENERGY | 3 |

### Invoker:

> lista blanca de eventos que realmente tienen un invoker pasado a ellos

> Las acciones como SMART_ACTION_INVOKER_CAST y los targets como SMART_TARGET_ACTION_INVOKER solo funcionarán si el evento está en esta lista:

- SMART_EVENT_AGGRO
- SMART_EVENT_DEATH
- SMART_EVENT_KILL
- SMART_EVENT_SUMMONED_UNIT
- SMART_EVENT_SPELLHIT
- SMART_EVENT_SPELLHIT_TARGET
- SMART_EVENT_DAMAGED
- SMART_EVENT_RECEIVE_HEAL
- SMART_EVENT_RECEIVE_EMOTE
- SMART_EVENT_JUST_SUMMONED
- SMART_EVENT_DAMAGED_TARGET
- SMART_EVENT_SUMMON_DESPAWNED
- SMART_EVENT_PASSENGER_BOARDED
- SMART_EVENT_PASSENGER_REMOVED
- SMART_EVENT_GOSSIP_HELLO
- SMART_EVENT_GOSSIP_SELECT
- SMART_EVENT_ACCEPTED_QUEST
- SMART_EVENT_REWARD_QUEST
- SMART_EVENT_FOLLOW_COMPLETED
- SMART_EVENT_ON_SPELLCLICK
- SMART_EVENT_GO_LOOT_STATE_CHANGED
- SMART_EVENT_AREATRIGGER_ONTRIGGER
- SMART_EVENT_IC_LOS
- SMART_EVENT_OOC_LOS
- SMART_EVENT_DISTANCE_CREATURE
- SMART_EVENT_FRIENDLY_HEALTH
- SMART_EVENT_FRIENDLY_HEALTH_PCT
- SMART_EVENT_FRIENDLY_IS_CC
- SMART_EVENT_FRIENDLY_MISSING_BUFF
- SMART_EVENT_ACTION_DONE
- SMART_EVENT_TARGET_HEALTH_PCT
- SMART_EVENT_TARGET_MANA_PCT
- SMART_EVENT_RANGE
- SMART_EVENT_VICTIM_CASTING
- SMART_EVENT_TARGET_BUFFED
- SMART_EVENT_IS_BEHIND_TARGET
- SMART_EVENT_INSTANCE_PLAYER_ENTER
- SMART_EVENT_TRANSPORT_ADDCREATURE
- SMART_EVENT_DATA_SET
- SMART_EVENT_AREA_CASTING
- SMART_EVENT_AREA_RANGE
- SMART_EVENT_SUMMONED_UNIT_EVADE
- SMART_EVENT_IS_IN_MELEE_RANGE


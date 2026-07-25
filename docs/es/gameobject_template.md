# gameobject\_template

Contiene la plantilla de todos los gameobjects

## Estructura

| Field          | Type         | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| entry          | MEDIUMINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| type           | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| displayId      | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| name           | VARCHAR(100) | SIGNED     |     | NO   | "       |       |         |
| IconName       | VARCHAR(100) | SIGNED     |     | NO   | "       |       |         |
| castBarCaption | VARCHAR(100) | SIGNED     |     | NO   | "       |       |         |
| unk1           | VARCHAR(100) | SIGNED     |     | NO   | "       |       |         |
| size           | FLOAT        | SIGNED     |     | NO   | 1       |       |         |
| data0          | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data1          | INT          | UNSIGNED   |     | NO   | -1      |       |         |
| data2          | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data3          | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data4          | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data5          | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data6          | INT          | UNSIGNED   |     | NO   | -1      |       |         |
| data7          | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data8          | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data9          | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data10         | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data11         | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data12         | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data13         | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data14         | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data15         | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data16         | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data17         | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data18         | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data19         | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data20         | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data21         | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data22         | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| data23         | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| AIName         | char(64)     | SIGNED     |     | NO   | "       |       |         |
| ScriptName     | VARCHAR(64)  | SIGNED     |     | NO   | "       |       |         |
| WDBVerified    | SMALLINT     | SIGNED     |     | YES  | 1       |       |         |

## Descripción de los campos

### entry

Id de la plantilla del gameobject. `WDB-fields`

### type 

| Name                                  | Value |
| ------------------------------------- | ----- |
| GAMEOBJECT_TYPE_DOOR                  | 0     |
| GAMEOBJECT_TYPE_BUTTON                | 1     |
| GAMEOBJECT_TYPE_QUESTGIVER            | 2     |
| GAMEOBJECT_TYPE_CHEST                 | 3     |
| GAMEOBJECT_TYPE_BINDER                | 4     |
| GAMEOBJECT_TYPE_GENERIC               | 5     |
| GAMEOBJECT_TYPE_TRAP                  | 6     |
| GAMEOBJECT_TYPE_CHAIR                 | 7     |
| GAMEOBJECT_TYPE_SPELL_FOCUS           | 8     |
| GAMEOBJECT_TYPE_TEXT                  | 9     |
| GAMEOBJECT_TYPE_GOOBER                | 10    |
| GAMEOBJECT_TYPE_TRANSPORT             | 11    |
| GAMEOBJECT_TYPE_AREADAMAGE            | 12    |
| GAMEOBJECT_TYPE_CAMERA                | 13    |
| GAMEOBJECT_TYPE_MAP_OBJECT            | 14    |
| GAMEOBJECT_TYPE_MO_TRANSPORT          | 15    |
| GAMEOBJECT_TYPE_DUEL_ARBITER          | 16    |
| GAMEOBJECT_TYPE_FISHINGNODE           | 17    |
| GAMEOBJECT_TYPE_RITUAL                | 18    |
| GAMEOBJECT_TYPE_MAILBOX               | 19    |
| GAMEOBJECT_TYPE_AUCTIONHOUSE          | 20    |
| GAMEOBJECT_TYPE_GUARDPOST             | 21    |
| GAMEOBJECT_TYPE_SPELLCASTER           | 22    |
| GAMEOBJECT_TYPE_MEETINGSTONE          | 23    |
| GAMEOBJECT_TYPE_FLAGSTAND             | 24    |
| GAMEOBJECT_TYPE_FISHINGHOLE           | 25    |
| GAMEOBJECT_TYPE_FLAGDROP              | 26    |
| GAMEOBJECT_TYPE_MINI_GAME             | 27    |
| GAMEOBJECT_TYPE_LOTTERY_KIOSK         | 28    |
| GAMEOBJECT_TYPE_CAPTURE_POINT         | 29    |
| GAMEOBJECT_TYPE_AURA_GENERATOR        | 30    |
| GAMEOBJECT_TYPE_DUNGEON_DIFFICULTY    | 31    |
| GAMEOBJECT_TYPE_BARBER_CHAIR          | 32    |
| GAMEOBJECT_TYPE_DESTRUCTIBLE_BUILDING | 33    |
| GAMEOBJECT_TYPE_GUILD_BANK            | 34    |
| GAMEOBJECT_TYPE_TRAPDOOR              | 35    |

### displayId

Id del modelo gráfico enviado al cliente desde GameObjectDisplayInfo.dbc `WDB-fields`

### name

El nombre del objeto. `WDB-fields`

### IconName

Funciona exactamente igual que el IconName de creature\_template.

IconNames que funcionan

- Taxi
- Talk
- Attack
- Directions
- Quest

Puede que experimentes algunos bugs menores al intentar que funcione Quest (el signo de exclamación amarillo).
No obstante, el resto de iconos listados funcionan.

`WDB-fields`

### castBarCaption

Muestra un texto único en la barra de lanzamiento del objeto cuando se usa el objeto. `WDB-fields`

### unk1

`campo-sin-descripción|7`

### size

El tamaño del objeto debe establecerse porque los modelos gráficos pueden remuestrearse. `WDB-fields`

### data0-23

El contenido de los campos data depende del [tipo de gameobject](#gameobject_template-type)

*Los valores de estos campos provienen de WDB y no deben cambiarse.*

**GAMEOBJECT\_TYPE\_DOOR = 0**

- data0: startOpen (flag booleano)
- data1: open (LockId de Lock.dbc)
- data2: autoClose (tiempo en milisegundos)
- data3: noDamageImmune (flag booleano)
- data4: openTextID (Text ID desconocido)
- data5: closeTextID (Text ID desconocido)
- data6: Ignorado por el pathfinding
- data7: Conditionid1
- data8: La puerta es opaca
- data9: Gigantic AOI
- data10: Infinite AOI

**GAMEOBJECT\_TYPE\_BUTTON = 1**

- data0: startOpen (State)
- data1: open (LockId de Lock.dbc)
- data2: autoClose (flag largo desconocido)
- data3: linkedTrap ([gameobject\_template.entry](#gameobject_template-entry) (GO generado de tipo 6))
- data4: noDamageImmune (flag booleano)
- data5: large? (flag booleano)
- data6: openTextID (Text ID desconocido)
- data7: closeTextID (Text ID desconocido)
- data8: losOK (flag booleano)
- data9: Conditionid1

**GAMEOBJECT\_TYPE\_QUESTGIVER = 2**

- data0: open (LockId de Lock.dbc)
- data1: questList (ID desconocido)
- data2: pageMaterial (PageTextMaterial.dbc)
- data3: gossipID (gossip\_menu\_option.menu\_id)
- data4: customAnim (valor desconocido de 1 a 4)
- data5: noDamageImmune (flag booleano)
- data6: openTextID (ID de broadcast\_text)
- data7: losOK (flag booleano)
- data8: allowMounted (flag booleano)
- data9: large? (flag booleano)
- data10: Conditionid1
- data11: Nunca usable mientras se está montado

**GAMEOBJECT\_TYPE\_CHEST = 3**

- data0: open (LockId de Lock.dbc)
- data1: chestLoot ([gameobject\_loot\_template.entry](http://www.azerothcore.org/wiki/loot_template#loot_template-Entry)) `WDB-fields`
- data2: chestRestockTime (tiempo en segundos)
- data3: consumable (State: flag booleano)
- data4: minRestock (Mín. de intentos de saqueo con éxito para Minería, Herboristería, etc.)
- data5: maxRestock (Máx. de intentos de saqueo con éxito para Minería, Herboristería, etc.)
- data6: lootedEvent (Event ID de la tabla event\_scripts)
- data7: linkedTrap ([gameobject\_template.entry](#gameobject_template-entry) (GO generado de tipo 6))
- data8: questID ([quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id) de misión completada)
- data9: level (nivel mínimo requerido para abrir este gameobject)
- data10: losOK (flag booleano)
- data11: leaveLoot (flag booleano)
- data12: notInCombat (flag booleano)
- data13: log loot (flag booleano)
- data14: openTextID (ID desconocido)
- data15: use group loot rules (flag booleano)
- data16: floating tooltip
- data17: conditionid1
- data18: xplevel
- data19: xpDifficulty
- data20: lootlevel
- data21: Group Xp
- data22: Damage Immune
- data23: trivialSkillLow

**GAMEOBJECT\_TYPE\_BINDER = 4**

Tipo de objeto sin usar

**GAMEOBJECT\_TYPE\_GENERIC = 5**

- data0: floatingTooltip (flag booleano)
- data1: highlight (flag booleano)
- data2: serverOnly? (Siempre 0)
- data3: large? (flag booleano)
- data4: floatOnWater (flag booleano)
- data5: questID (requiere una [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id) activa para funcionar)
- data6: conditionID1
- data7: LargeAOI
- data8: UseGarrisonOwnerGuildColors

**GAMEOBJECT\_TYPE\_TRAP = 6**

- data0: open (LockId de [Lock.dbc](lock) )
- data1: level (nivel equivalente de npc para el hechizo lanzado)
- data2: diameter (o sea radio \* 2)
- data3: spell (Spell Id de [Spell.dbc](spell))
- data4: type (0 trampa sin desaparecer tras lanzar. 1 la trampa desaparece tras lanzar. 2 bomba que lanza al aparecer)
- data5: cooldown (tiempo en segundos)
- data6:  ? (flag desconocido)
- data7: startDelay? (tiempo en segundos)
- data8: serverOnly? (siempre 0)
- data9: stealthed (flag booleano)
- data10: large? (flag booleano)
- data11: stealthAffected (flag booleano)
- data12: openTextID (ID desconocido)
- data13: closeTextID
- data14: IgnoreTotems
- data15: conditionID1
- data16: playerCast
- data17: SummonerTriggered
- data18: requireLOS

**GAMEOBJECT\_TYPE\_CHAIR = 7**

- data0: chairslots (número de jugadores que pueden sentarse en él)
- data1: height
- data2: onlyCreatorUse
- data3: triggeredEvent
- data4: conditionID1

**GAMEOBJECT\_TYPE\_SPELL\_FOCUS = 8**

- data0: spellFocusType (de SpellFocusObject.dbc; el valor también aparece como RequiresSpellFocus en [Spell.dbc](https://trinitycore.atlassian.net/wiki/display/tc/Spell))
- data1: diameter (o sea radio\*2)
- data2: linkedTrap ([gameobject\_template.entry](#gameobject_template-entry) (GO generado de tipo 6))
- data3: serverOnly? (Siempre 0)
- data4: questID (requiere una [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id) activa para funcionar)
- data5: large? (flag booleano)
- data6: floatingTooltip (flag booleano)
- data7: floatOnWater
- data8: conditionID1

**GAMEOBJECT\_TYPE\_TEXT = 9**

-   data0: pageID ([page\_text.entry](page_text_2130246.html#page_text-entry))
-   data1: language (de [Languages.dbc](languages))
-   data2: pageMaterial ([PageTextMaterial.dbc](pagetextmaterial))
-   data3: allowMounted
-   data4: conditionID1
-   data5: NeverUsableWhileMounted

**GAMEOBJECT\_TYPE\_GOOBER = 10**

-   data0: open (LockId de [Lock.dbc](lock))
-   data1: questID (requiere una [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id) activa para funcionar)
-   data2: eventID (id de event\_script)
-   data3:  Tiempo en ms antes de restaurar el estado inicial
-   data4: customAnim (desconocido)
-   data5: consumable (flag booleano que controla si el gameobject desaparecerá o no)
-   data6: cooldown (tiempo en segundos)
-   data7: pageID ([page\_text.entry](http://www.azerothcore.org/wiki/page_text#entry))
-   data8: language (de Languages.dbc)
-   data9: pageMaterial (PageTextMaterial.dbc)
-   data10: spell (Spell Id de Spell.dbc)
-   data11: noDamageImmune (flag booleano)
-   data12: linkedTrap ([gameobject\_template.entry](#gameobject_template-entry) (GO generado de tipo 6))
-   data13: large? (flag booleano)
-   data14: openTextID (ID desconocido)
-   data15: closeTextID (ID desconocido)
-   data16: losOK (flag booleano) (algo relacionado con los campos de batalla)
-   data19: gossipID - lanza el hechizo cuando se usa
-   data20: AllowMultiInteract
-   data21: floatOnWater
-   data22: conditionID1
-   data23: playerCast

**GAMEOBJECT\_TYPE\_TRANSPORT = 11**

-   data0: Timeto2ndfloor
-   data1: startOpen
-   data2: autoClose
-   data3: Reached1stfloor
-   data4: Reached2ndfloor
-   data5: SpawnMap
-   data6: Timeto3rdfloor
-   data7: Reached3rdfloor
-   data8: Timeto4rdfloor
-   data9: Reached4rdfloor
-   data10: Timeto5rdfloor
-   data11: Reached5rdfloor
-   data12: Timeto6rdfloor
-   data13: Reached6rdfloor
-   data14: Timeto7rdfloor
-   data15: Reached7rdfloor
-   data16: Timeto8rdfloor
-   data17: Reached8rdfloor
-   data18: Timeto9rdfloor
-   data19: Reached9rdfloor
-   data20: Timeto10rdfloor
-   data21: Reached10rdfloor
-   data22: onlychargeheightcheck
-   data23: onlychargetimecheck

**GAMEOBJECT\_TYPE\_AREADAMAGE = 12**

-   data0: open
-   data1: radius
-   data2: damageMin
-   data3: damageMax
-   data4: damageSchool
-   data5: autoClose
-   data6: openTextID
-   data7: closeTextID

**GAMEOBJECT\_TYPE\_CAMERA = 13**

-   data0: open (LockId de [Lock.dbc](lock))
-   data1: camera (entry de Cinematic de [CinematicCamera.dbc](cinematiccamera))
-   data2: eventID
-   data3: openTextID
-   data4: conditionID1

**GAMEOBJECT\_TYPE\_MAPOBJECT = 14**

No se usan datos, todos son siempre 0

**GAMEOBJECT\_TYPE\_MOTRANSPORT = 15**

-   data0: taxiPathID (Id de [TaxiPath.dbc](taxipath))
-   data1: moveSpeed
-   data2: accelRate
-   data3: startEventID
-   data4: stopEventID
-   data5: transportPhysics
-   data6: SpawnMap
-   data7: worldState1
-   data8: allowstopping
-   data9: InitStopped
-   data10: TrueInfiniteAOI

**GAMEOBJECT\_TYPE\_DUELFLAG = 16**

Solo un gameobject con este tipo (21680) y sin datos

**GAMEOBJECT\_TYPE\_FISHINGNODE = 17**

Solo un gameobject con este tipo (35591) y sin datos

**GAMEOBJECT\_TYPE\_RITUAL = 18**

-   data0: casters?
-   data1: spell (Spell Id de [Spell.dbc](spell))
-   data2: animSpell (Spell Id de [Spell.dbc](spell))
-   data3: ritualPersistent (flag booleano)
-   data4: casterTargetSpell (Spell Id de [Spell.dbc](spell))
-   data5: casterTargetSpellTargets (flag booleano)
-   data6: castersGrouped (flag booleano)
-   data7: ritualNoTargetCheck
-   data8: conditionID1

**GAMEOBJECT\_TYPE\_MAILBOX = 19**

No se usan datos, todos son siempre 0

**GAMEOBJECT\_TYPE\_AUCTIONHOUSE = 20**

-   data0: actionHouseID (¿De [AuctionHouse.dbc](auctionhouse)?)

**GAMEOBJECT\_TYPE\_GUARDPOST = 21**

-   data0: CreatureID
-   data1: unk

**GAMEOBJECT\_TYPE\_SPELLCASTER = 22**

-   data0: spell (Spell Id de [Spell.dbc](spell))
-   data1: charges
-   data2: partyOnly (flag booleano, hay que estar en grupo para usarlo)
-   data3: allowMounted
-   data4: GiganticAOI
-   data5: conditionID1
-   data6: playerCast
-   data7: NeverUsableWhileMounted

**GAMEOBJECT\_TYPE\_MEETINGSTONE = 23**

-   data0: minLevel
-   data1: maxLevel
-   data2: areaID (De [AreaTable.dbc](areatable))

**GAMEOBJECT\_TYPE\_FLAGSTAND = 24**

-   data0: open (LockId de [Lock.dbc](lock))
-   data1: pickupSpell (Spell Id de [Spell.dbc](spell))
-   data2: radius (distancia)
-   data3: returnAura (Spell Id de [Spell.dbc](spell))
-   data4: returnSpell (Spell Id de [Spell.dbc](spell))
-   data5: noDamageImmune (flag booleano)
-   data6: openTextID
-   data7: losOK (flag booleano)
-   data8: conditionID1
-   data9: playerCast
-   data10: GiganticAOI
-   data11: InfiniteAOI
-   data12: cooldown

**GAMEOBJECT\_TYPE\_FISHINGHOLE = 25**

-   data0: radius (distancia)
-   data1: chestLoot ([gameobject\_loot\_template.entry](http://www.azerothcore.org/wiki/loot_template#loot_template-Entry))
-   data2: minRestock
-   data3: maxRestock
-   data4: open

**GAMEOBJECT\_TYPE\_FLAGDROP = 26**

-   data0: open (LockId de [Lock.dbc](lock))
-   data1: eventID (Event ID desconocido)
-   data2: pickupSpell (Spell Id de [Spell.dbc](spell))
-   data3: noDamageImmune (flag booleano)
-   data4: openTextID
-   data5: playerCast
-   data6: ExpireDuration
-   data7: GiganticAOI
-   data8: InfiniteAOI
-   data9: cooldown

**GAMEOBJECT\_TYPE\_MINIGAME = 27**

Tipo de objeto sin usar. Reutilizado en el core para CUSTOM\_TELEPORT

-   data0: [areatrigger\_teleport.id](http://www.azerothcore.org/wiki/areatrigger_teleport#id)

**GAMEOBJECT\_TYPE\_LOTTERYKIOSK = 28**

Tipo de objeto sin usar

**GAMEOBJECT\_TYPE\_CAPTUREPOINT = 29**

-   data0: radius (distancia)
-   data1: spell (ID desconocido, no es un spell id del archivo dbc, quizá un hechizo solo del lado del servidor)
-   data2: worldState1
-   data3: worldstate2
-   data4: winEventID1 (Event ID desconocido)
-   data5: winEventID2 (Event ID desconocido)
-   data6: contestedEventID1 (Event ID desconocido)
-   data7: contestedEventID2 (Event ID desconocido)
-   data8: progressEventID1 (Event ID desconocido)
-   data9: progressEventID2 (Event ID desconocido)
-   data10: neutralEventID1 (Event ID desconocido)
-   data11: neutralEventID2 (Event ID desconocido)
-   data12: neutralPercent
-   data13: worldstate3
-   data14: minSuperiority
-   data15: maxSuperiority
-   data16: minTime (en segundos)
-   data17: maxTime (en segundos)
-   data18: large? (flag booleano)
-   data19: highlight
-   data20: startingValue
-   data21: unidirectional
-   data22: killbonustime
-   data23: speedWorldState1

**GAMEOBJECT\_TYPE\_AURAGENERATOR = 30**

-   data0: startOpen (flag booleano)
-   data1: radius (distancia)
-   data2: auraID1 (Spell Id de [Spell.dbc](spell))
-   data3: conditionID1 (ID desconocido)
-   data4: auraID2
-   data5: conditionID2
-   data6: serverOnly

**GAMEOBJECT\_TYPE\_DUNGEONDIFFICULTY = 31**

-   data0: mapID (De [Map.dbc](map))
-   data1: difficulty
-   data2: DifficultyHeroic
-   data3: DifficultyEpic
-   data4: DifficultyLegendary
-   data5: HeroicAttachment
-   data6: ChallengeAttachment
-   data7: DifficultyAnimations
-   data8: LargeAOI
-   data9: GiganticAOI
-   data10: Legacy

     

    | Value | Comment                     |
    | ----- | --------------------------- |
    | 0     | 5 jugadores normal, 10 jugadores normal |
    | 1     | 5 jugadores heroico, 25 normal |
    | 2     | 10 jugadores heroico        |
    | 3     | 25 jugadores heroico        |

     

**GAMEOBJECT\_TYPE\_BARBER\_CHAIR = 32**

-   data0: chairheight
-   data1: HeightOffset
-   data2: SitAnimKit

**GAMEOBJECT\_TYPE\_DESTRUCTIBLE\_BUILDING = 33**

-   data0: intactNumHits
-   data1: creditProxyCreature
-   data2: state1Name
-   data3: intactEvent
-   data4: damagedDisplayId
-   data5: damagedNumHits
-   data6: empty3
-   data7: empty4
-   data8: empty5
-   data9: damagedEvent
-   data10: destroyedDisplayId
-   data11: empty7
-   data12: empty8
-   data13: empty9
-   data14: destroyedEvent
-   data15: empty10
-   data16: debuildingTimeSecs
-   data17: empty11
-   data18: destructibleData
-   data19: rebuildingEvent
-   data20: empty12
-   data21: empty13
-   data22: damageEvent
-   data23: empty14

**GAMEOBJECT\_TYPE\_GUILD\_BANK = 34**

No se usan datos, todos son siempre 0

**GAMEOBJECT\_TYPE\_TRAPDOOR = 35**

-   data0: whenToPause
-   data1: startOpen
-   data2: autoClose
-   data3: BlocksPathsDown
-   data4: PathBlockerBump

### AIName

Este campo es sobrescrito por el campo ScriptName si ambos están establecidos.
Nota: solo puede usarse `SmartGameObjectAI` en este campo, no uses `SmartAI`.

### ScriptName

Nombre del script que usa este objeto si es necesario

`WDBVerified`

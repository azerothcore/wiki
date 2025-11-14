
# Criterios de los Logros

[`Volver a:DBC`](dbc-index)

**Achievement\_Criteria.dbc**

Este tipo de DBC (DataBaseClient) fue añadido en la versión del WoW 3.0.1.8303 y contiene los criterios necesarios para obtener un logro.

**Versión : 3.3.5a**

## Estructura

| Columna | Campo             | Tipo    | Notas                                                                                                      |
| ------  | ----------------- | ------- | ---------------------------------------------------------------------------------------------------------- |
| 1       | ID                | Integer | Identificador (ID) del criterio en cuestión.                                                               |
| 2       | Achievement       | iRefID  | Es necesario hacer una referencia al logro perteneciente a éste criterio.                                  |
| 3       | Type              | Integer | ¿De qué tipo es el criterio? Este apartado es definido en las filas de abajo. Véase en la descripción.     |
| 4       | asset_id          | Integer | Requisito principal del criterio.                                                                          |
| 5       | Quantity          | Integer | Cantidad del requisito principal.                                                                          |
| 6       | start_event       | Integer | Requisito adicional del criterio 1.                                                                        |
| 7       | start_asset       | Integer | Valor del requisito adicional número 1.                                                                    |
| 8       | fail_event        | Integer | Requisito adicional del criterio 2.                                                                        |
| 9       | fail_asset        | Integer | Valor del requisito adicional número 2.                                                                    |
| 10-25   | Description       | Loc     | Descripción del criterio.                                                                                  |
| 26      | ?                 |         | La mayoría de veces es 16712190, sin embargo no siempre se cumple.                                         |
| 27      | Flags             | Integer | Marcadores (flags) de visualización: 1: Muestra la Barra de Progreso (desconozco otro tipo de marcadores). |
| 28      | timer_start_event | Integer |                                                                                                            |
| 29      | timer_asset_id    | Integer |                                                                                                            |
| 30      | timer_time        | Integer | Completar la misión en %i segundos.                                                                        |
| 31      | ui_order          | Integer |                                                                                                            |

**Descripción de los Campos**

Esto describe las filas 3 hasta la 9 por tipo (fila 2). Puede que existan más tipos. Los campos no listados son cero.

Esta información es recuperada de DBCStructure.h.

#### KILL\_CREATURE = 0

*Tambien usado para muertes de jugadores.*

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 4      | creatureID | Integer |
| 5      | killCount  | Integer |

#### WIN\_BG = 1

*Existen criterios adicionales a simplemente ganar*

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 4      | [Map](map) | iRefID  |
| 5      | winCount   | Integer |

#### REACH\_LEVEL = 5

Alcanza un nivel especificado.

| Column | Field  | Type    |
| ------ | ------ | ------- |
| 4      | unused | Integer |
| 5      | level  | Integer |

#### REACH\_SKILL\_LEVEL = 7

Alcanza un nivel especificado en habilidad.

| Column | Field      | Type    | Notes                               |
| ------ | ---------- | ------- | ----------------------------------- |
| 4      | skillID    | iRefID  | [SkillLine.dbc](skillline)?         |
| 5      | skillLevel | Integer |                                     |

#### COMPLETE\_ACHIEVEMENT = 8

Completa un logro.

| Column | Field                      | Type   |
| ------ | -------------------------- | ------ |
| 4      | [Achievement](achievement) | iRefID |

#### COMPLETE\_QUEST\_COUNT = 9

Completa cierta cantidad de misiones.

| Column | Field           | Type    |
| ------ | --------------- | ------- |
| 4      | unused          | Integer |
| 5      | totalQuestCount | Integer |

#### COMPLETE\_DAILY\_QUEST\_DAILY = 10

Completa cierta cantidad de misiones diarias cada día.

| Column | Field        | Type    |
| ------ | ------------ | ------- |
| 4      | unused       | Integer |
| 5      | numberOfDays | Integer |

#### COMPLETE\_QUESTS\_IN\_ZONE = 11

Completa cierta cantidad de misiones en una zona.

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 4      | zoneID     | Integer |
| 5      | questCount | Integer |

#### DAMAGE\_DONE = 13

Cantidad de daño infligido.

#### COMPLETE\_DAILY\_QUEST = 14

Completa cierta cantidad de misiones diarias.

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 4      | unused     | Integer |
| 5      | questCount | Integer |

#### COMPLETE\_BATTLEGROUND = 15

Campos de batalla completados.

#### DEATH\_AT\_MAP = 16

Muerte en un mapa.

| Column | Field      | Type   |
| ------ | ---------- | ------ |
| 4      | [Map](map) | iRefID |

#### DEATH\_IN\_DUNGEON = 18

Muerte en una Mazmorra.

| Column | Field    | Type    |
| ------ | -------- | ------- |
| 4      | manLimit | Integer |

#### COMPLETE\_RAID = 19

Banda (Raid) completada

| Column | Field     | Type    | Notes                |
| ------ | --------- | ------- | -------------------- |
| 4      | groupSize | Integer | Puede ser 5, 10 o 25 |

#### KILLED\_BY\_CREATURE = 20

Asesinado por una criatura.

| Column | Field         | Type    |
| ------ | ------------- | ------- |
| 4      | creatureEntry | Integer |

#### FALL\_WITHOUT\_DYING = 24

Caer sin morir.

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 4      | unused     | Integer |
| 5      | fallHeight | Integer |

#### DEATHS\_FROM = 26

Muertes desde:

| Column | Field               | Type   |
| ------ | ------------------- | ------ |
| 4      | EnvironmentalDamage | iRefID |

#### COMPLETE\_QUEST = 27

Misión completada.

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 4      | questID    | Integer |
| 5      | questCount | Integer |

#### BE\_SPELL\_TARGET = 28

Hechizo lanzado a un jugador.

#### BE\_SPELL\_TARGET2 = 69

Hechizo lanzado a un jugador 2.

| Column | Field          | Type    |
| ------ | -------------- | ------- |
| 4      | [Spell](spell) | iRefID  |
| 5      | spellCount     | Integer |

#### CAST\_SPELL = 29

Hechizo lanzado.

#### CAST\_SPELL2 = 110

Hechizo lanzado 2.

| Column | Field          | Type    |
| ------ | -------------- | ------- |
| 4      | [Spell](spell) | iRefID  |
| 5      | castCount      | Integer |

#### BG\_OBJECTIVE\_CAPTURE = 30

Captura de Objetivo del Campo de Batalla

| Column | Field    | Type    | Notes                         |
| ------ | -------- | ------- | ----------------------------- |
| 4      | unknow   | Integer | Valor 42 = captura la bandera |
| 5      | count(?) | Integer | Cuantas veces fue capturada   |

#### HONORABLE\_KILL\_AT\_AREA = 31

Muerte honorable en un área.

| Column | Field             | Type    |
| ------ | ----------------- | ------- |
| 4      | [Area](areatable) | iRefID  |
| 5      | killCount         | Integer |

#### WIN\_ARENA = 32

Arenas ganadas.

#### PLAY\_ARENA = 33

Arenas jugadas.

| Column | Field      | Type   |
| ------ | ---------- | ------ |
| 4      | [Map](map) | iRefID |

#### LEARN\_SPELL = 34

Hechizos aprendidos.

| Column | Field          | Type   |
| ------ | -------------- | ------ |
| 4      | [Spell](spell) | iRefID |

#### OWN\_ITEM = 36

Item propio.

#### WIN\_RATED\_ARENA = 37

Ganar la arena clasificada

| Column | Field  | Type    | Notes          |
| ------ | ------ | ------- | -------------- |
| 4      | unused | Integer |                |
| 5      | count  | Integer |                |
| 6      | flag   | Integer | 4= en una fila |

#### HIGHEST\_TEAM\_RATING = 38

Mayor Índice de arena.

| Column | Field    | Type    | Notes   |
| ------ | -------- | ------- | ------- |
| 4      | teamtype | Integer | {2,3,5} |

#### REACH\_TEAM\_RATING = 39

Cantidad de Índice de arena.

| Column | Field      | Type    | Notes   |
| ------ | ---------- | ------- | ------- |
| 4      | teamtype   | Integer | {2,3,5} |
| 5      | teamrating | Integer |         |

#### LEARN\_SKILL\_LEVEL = 40

Aprender nivel de habilidad.

| Column | Field      | Type    | Notes                                                                    |
| ------ | ---------- | ------- | ------------------------------------------------------------------------ |
| 4      | skillID    | iRefID  | [SkillLine.dbc](skillline)?                                              |
| 5      | skillLevel | Integer | Aprendiz=1. Oficial=2. Experto=3. Artesano=4. Maestro=5. Gran Maestro=6. |

#### USE\_ITEM = 41

Item usado.

#### LOOT\_ITEM = 42

Item despojado.

#### EXPLORE\_AREA = 43

areaReference  **NO** es el índice de [AreaTable.dbc.](areatable), proviene de WorldMapOverlay.dbc.

| Column | Field         | Type    |
| ------ | ------------- | ------- |
| 4      | areaReference | Integer |

#### OWN\_RANK = 44

Este rango **NO** es el índice de [CharTitles.dbc](chartitles)

| Column | Field | Type    |
| ------ | ----- | ------- |
| 4      | rank  | Integer |

#### BUY\_BANK\_SLOT = 45

Comprar casillas en el banco.

| Column | Field         | Type    |
| ------ | ------------- | ------- |
| 4      | unused        | Integer |
| 5      | numberOfSlots | Integer |

#### GAIN\_REPUTATION = 46

Obtener reputación.

| Column | Field              | Type    | Notes                                                                  |
| ------ | ------------------ | ------- | ---------------------------------------------------------------------- |
| 4      | [Faction](faction) | iRefID  |                                                                        |
| 5      | reputationAmount   | Integer | Cantidad total de reputación, teniendo en cuenta que 42000 es exaltado |

#### GAIN\_EXALTED\_REPUTATION= 47

Obtener reputación exaltada.

| Column | Field                   | Type    |
| ------ | ----------------------- | ------- |
| 4      | unused                  | Integer |
| 5      | numberOfExaltedFactions | Integer |

#### VISIT\_BARBER\_SHOP = 48

Visitar al peluquero.

| Column | Field          | Type    |
| ------ | -------------- | ------- |
| 4      | unused         | Integer |
| 5      | numberOfVisits | Integer |

#### EQUIP\_EPIC\_ITEM = 49

Nivel de Item para ser considerado épico. Véase [itemlevel](item_template#itemlevel).

| Column | Field    | Type    |
| ------ | -------- | ------- |
| 4      | itemSlot | Integer |

#### ROLL\_NEED\_ON\_LOOT = 50

Número de dados necesarios para el botín.

#### ROLL\_GREED\_ON\_LOOT = 51

Número de dados necesarios en modo codicia para el botín.

| Column | Field     | Type    |
| ------ | --------- | ------- |
| 4      | rollValue | Integer |
| 5      | count     | Integer |

#### HK\_CLASS = 52

Muertes honorables por clase.

| Column | Field               | Type    |
| ------ | ------------------- | ------- |
| 4      | [Class](chrclasses) | iRefID  |
| 5      | count               | Integer |

#### HK\_RACE = 53

Muertes honorables por raza.

| Column | Field            | Type    |
| ------ | ---------------- | ------- |
| 4      | [Race](chrraces) | iRefID  |
| 5      | count            | Integer |

#### DO\_EMOTE = 54

[Emotes](emotes#ID).

| Column | Field           | Type    | Notes                                                           |
| ------ | --------------- | ------- | --------------------------------------------------------------- |
| 4      | [Emote](emotes) | iRefID  |                                                                 |
| 5      | count           | Integer | Número de emotes, siempre se requiere un objetivo (jugador) o requisitos especiales. |

#### HEALING\_DONE = 55

Sanación realizada.

#### GET\_KILLING\_BLOWS = 56

Hacer Golpes de Gracia.

| Column | Field          | Type    | Notes                               |
| ------ | -------------- | ------- | ----------------------------------- |
| 4      | unused         | Integer |                                     |
| 5      | count          | Integer |                                     |
| 6      | flag           | Integer | 3 para sanación en Campo de Batalla |
| 7      | [Map](Map.dbc) | iRefID  |                                     |

#### EQUIP\_ITEM = 57

Equipar Item.

| Column | Field        | Type    |
| ------ | ------------ | ------- |
| 4      | [Item](item) | iRefID  |
| 5      | itemCount    | Integer |

#### MONEY\_FROM\_QUEST\_REWARD= 62

Dinero de misiones obtenido (Medido en monedas de cobre).

#### LOOT\_MONEY = 67

Dinero obtenido (Medido en monedas de cobre).

| Column | Field        | Type    |
| ------ | ------------ | ------- |
| 4      | unused       | Integer |
| 5      | goldInCopper | Integer |

#### USE\_GAMEOBJECT = 68

Activar cierto Objeto del Juego (GameObject), ya sea puerta, caja, etc.

| Column | Field    | Type    |
| ------ | -------- | ------- |
| 4      | goEntry  | Integer |
| 5      | useCount | Integer |

#### SPECIAL\_PVP\_KILL = 70

¿Acaso son Criterios de Logros especiales almacenados en los DBC?

| Column | Field     | Type    |
| ------ | --------- | ------- |
| 4      | unused    | Integer |
| 5      | killCount | Integer |

#### FISH\_IN\_GAMEOBJECT = 72

Pescar en cierto Objeto del Juego (GameObject).

| Column | Field     | Type    |
| ------ | --------- | ------- |
| 4      | goEntry   | Integer |
| 5      | lootCount | Integer |

#### LEARN\_SKILLLINE\_SPELLS = 75

Aprender hechizos de habilidad.

| Column | Field                  | Type    |
| ------ | ---------------------- | ------- |
| 4      | [SkillLine](skillline) | iRefID  |
| 5      | spellCount             | Integer |

#### WIN\_DUEL = 76

Ganar duelo (s).

| Column | Field     | Type    |
| ------ | --------- | ------- |
| 4      | unused    | Integer |
| 5      | duelCount | Integer |

#### HIGHEST\_POWER = 96

Mayor número de poder.

| Column | Field     | Type    | Notes                                     |
| ------ | --------- | ------- | ----------------------------------------- |
| 4      | powerType | Integer | 0=Maná. 1=Ira. 3=Energía. 6=Poder Rúnico. |

#### HIGHEST\_STAT = 97

Mayor número de estadística.

| Column | Field    | Type    | Notes                                                    |
| ------ | -------- | ------- | -------------------------------------------------------- |
| 4      | statType | Integer | 4=Espíritu. 3=Intelecto, 2=Aguante, 1=Agilidad, 0=Fuerza |

#### HIGHEST\_SPELLPOWER = 98

Mayor número de poder de hechizos.

| Column | Field       | Type   | Notes                                 |
| ------ | ----------- | ------ | ------------------------------------- |
| 4      | spellSchool | iRefID | [SkillLine](skillline) o resistencias |

#### HIGHEST\_RATING = 100

Mayor número.

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 4      | ratingType | Integer |

#### LOOT\_TYPE = 109

Tipo de botín.

| Column | Field         | Type    | Notes                                  |
| ------ | ------------- | ------- | -------------------------------------- |
| 4      | lootType      | Integer | 3=Pescar, 2=Robar, 4=Desencantar       |
| 5      | lootTypeCount | Integer |                                        |

#### LEARN\_SKILL\_LINE = 112

Aprender línea de habilidad.

| Column | Field                  | Type    |
| ------ | ---------------------- | ------- |
| 4      | [SkillLine](skillline) | iRefID  |
| 5      | spellCount             | Integer |

#### EARN\_HONORABLE\_KILL = 113

Muertes honorables obtenidas.

| Column | Field     | Type    |
| ------ | --------- | ------- |
| 4      | unused    | Integer |
| 5      | killCount | Integer |

#### ACCEPTED\_SUMMONS = 114

Invocaciones aceptadas.

| Column | Field                                       | Type    |
| ------ | ------------------------------------------- | ------- |
| 4      | unused                                      | Integer |
| 5      | Aquí viene un 1, porque es una Estadística  | Integer |

#### ACHIVEMENTPOINTS\_REACHED = 115

Puntos de logro alcanzados.

| Column | Field  | Type    |
| ------ | ------ | ------- |
| 4      | unused | Integer |
| 5      | unused | Integer |

// Esta parte suele ser confusa... Tal vez porque sólo debe usarse para "más de noventa mil", ya que en ninguna parte de AchPoints (Puntos de Logros) se especifica.

#### RANDOM\_DUNGEON\_PLAYERCOUNT = 119

Número de mazmorras aleatorias.

| Column | Field       | Type    |
| ------ | ----------- | ------- |
| 4      | unused      | Integer |
| 5      | PlayerCount | Integer |

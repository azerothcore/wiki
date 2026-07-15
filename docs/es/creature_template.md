# creature_template

[<-Volver a: World](database-world)

**Tabla `creature_template`**

Esta tabla contiene la descripción de las criaturas. Cada criatura generada es una instancia de una plantilla presente en esta tabla; esto significa que toda criatura DEBE estar definida en esta tabla.

**Estructura**

| Field                                              | Type               | Null | Key | Default | Extra | Comment                              |
| -------------------------------------------------- | ------------------ | ---- | --- | ------- | ----- | ------------------------------------ |
| [entry](#entry)                                    | MEDIUMINT UNSIGNED | NO   | PRI | 0       |       |                                      |
| [difficulty_entry_1](#difficultyentryx)            | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [difficulty_entry_2](#difficultyentryx)            | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [difficulty_entry_3](#difficultyentryx)            | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [KillCredit1](#killcredit1)                        | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [KillCredit2](#killcredit2)                        | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [name](#name)                                      | char(100)          | NO   | MUL | 0       |       |                                      |
| [subname](#subname)                                | char(100)          | YES  |     | (NULL)  |       |                                      |
| [IconName](#iconname)                              | char(100)          | YES  |     | (NULL)  |       |                                      |
| [gossip_menu_id](#gossipmenuid)                    | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [minlevel](#minlevel)                              | TINYINT UNSIGNED   | NO   |     | 1       |       |                                      |
| [maxlevel](#maxlevel)                              | TINYINT UNSIGNED   | NO   |     | 1       |       |                                      |
| [exp](#exp)                                        | SMALLINT           | NO   |     | 0       |       |                                      |
| [faction](#faction)                                | SMALLINT UNSIGNED  | NO   |     | 0       |       |                                      |
| [npcflag](#npcflag)                                | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [speed_walk](#speedwalk)                           | FLOAT              | NO   |     | 1       |       | Result of 2.5/2.5, most common value |
| [speed_run](#speedrun)                             | FLOAT              | NO   |     | 1.14286 |       | Result of 8.0/7.0, most common value |
| [speed_swim](#speedswim)                           | FLOAT              | NO   |     | 1       |       |                                      |
| [speed_swim](#speedflight)                         | FLOAT              | NO   |     | 1       |       |                                      |
| [detection_range](#detectionrange)                 | FLOAT              | NO   |     | 20      |       |                                      |
| [scale](#scale)                                    | FLOAT              | NO   |     | 1       |       |                                      |
| [rank](#rank)                                      | TINYINT UNSIGNED   | NO   |     | 0       |       |                                      |
| [dmgschool](#dmgschool)                            | TINYINT            | NO   |     | 0       |       |                                      |
| [BaseAttackTime](#baseattacktime)                  | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [RangeAttackTime](#rangeattacktime)                | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [BaseVariance](#basevariance)                      | FLOAT              | NO   |     | 1       |       |                                      |
| [RangeVariance](#rangevariance)                    | FLOAT              | NO   |     | 1       |       |                                      |
| [unit_class](#unitclass)                           | TINYINT UNSIGNED   | NO   |     | 0       |       |                                      |
| [unit_flags](#unitflags)                           | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [unit_flags2](#unitflags2)                         | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [dynamicflags](#dynamicflags)                      | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [family](#family)                                  | TINYINT            | NO   |     | 0       |       |                                      |
| [type](#type)                                      | TINYINT UNSIGNED   | NO   |     | 0       |       |                                      |
| [type_flags](#typeflags)                           | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [lootid](#lootid)                                  | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [pickpocketloot](#pickpocketloot)                  | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [skinloot](#skinloot)                              | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [PetSpellDataId](#petspelldataid)                  | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [VehicleId](#vehicleid)                            | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [mingold](#mingold)                                | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [maxgold](#maxgold)                                | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [AIName](#ainame)                                  | char(64)           | NO   |     |         |       |                                      |
| [MovementType](#movementtype)                      | TINYINT UNSIGNED   | NO   |     | 0       |       |                                      |
| [HoverHeight](#hoverheight)                        | FLOAT              | NO   |     | 1       |       |                                      |
| [HealthModifier](#healthmodifier)                  | FLOAT              | NO   |     | 1       |       |                                      |
| [ManaModifier](#manamodifier)                      | FLOAT              | NO   |     | 1       |       |                                      |
| [ArmorModifier](#armormodifier)                    | FLOAT              | NO   |     | 1       |       |                                      |
| [DamageModifier](#damagemodifier)                  | FLOAT              | NO   |     | 1       |       |                                      |
| [ExperienceModifier](#experiencemodifier)          | FLOAT              | NO   |     | 1       |       |                                      |
| [RacialLeader](#racialleader)                      | TINYINT UNSIGNED   | NO   |     | 0       |       |                                      |
| [movementId](#movementid)                          | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [RegenHealth](#regenhealth)                        | TINYINT UNSIGNED   | NO   |     | 1       |       |                                      |
| [CreatureImmunitiesId](#creatureimmunitiesid)      | INT UNSIGNED       | NO   |     | 0       |       | Reference to creature_immunities table |
| [flags_extra](#flagsextra)                         | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [ScriptName](#scriptname)                          | char(64)           | NO   |     |         |       |                                      |
| [VerifiedBuild](#verifiedbuild)                    | SMALLINT           | YES  |     | 0       |       |                                      |

---

**Descripción de los campos**

#### entry

Id único de la criatura.

#### difficulty_entry_x

| name                                                      | entry | difficulty_entry_1 | difficulty_entry_2 | difficulty_entry_3 |
| --------------------------------------------------------- | ----- | ------------------ | ------------------ | ------------------ |
| [Anomalus](http://www.wowhead.com/npc=26763/anomalus)     | 26763 | 30529              | 0                  | 0                  |
| [Sindragosa](http://www.wowhead.com/npc=36853/sindragosa) | 36853 | 38265              | 38266              | 38267              |

Anomalus es un jefe de 5 jugadores ubicado en El Nexo. Puedes luchar contra él en dos tipos de dificultades (mazmorra normal y mazmorra heroica). Según el tipo de dificultad, los jefes tienen estadísticas diferentes como salud y daño. En el caso de Anomalus, la información del entry 26763 se usa cuando luchas contra él en dificultad normal y el entry 30529 se usa cuando luchas contra él en dificultad heroica.

Sindragosa, un encuentro de jefe de banda ubicado en la Ciudadela de la Corona de Hielo, puede combatirse en 4 dificultades diferentes debido a la introducción de los modos heroicos de banda en el Parche 3.2 (10 jugadores normal/heroico, 25 jugadores normal/heroico). Según el tipo de dificultad, debe tener estadísticas diferentes. Así que si la ves en una banda normal de 10 jugadores usará la información del entry 36853, en una banda normal de 25 jugadores se usará el entry 38265, y así sucesivamente. Esto contrasta fuertemente con jefes de banda como Patchwerk y XT-002 Deconstructor, ubicados en Naxxramas y Ulduar respectivamente, que solo tienen dos modos de banda diferentes (10 jugadores 'normal'/25 jugadores 'normal'). Los modos difíciles (hardmodes) dentro de la banda de Ulduar no tienen su propia plantilla, debido a que las mecánicas de juego activan la dificultad más alta durante el propio encuentro.

Aquí hay un caso especial con el campo de batalla Valle de Alterac. Hay 4 rangos de nivel donde los NPC se hacen más fáciles o más difíciles, según tu rango de nivel (añadido en el parche 3.2.2 de WoW cuando los personajes de nivel 80 recibieron su propio rango para este campo de batalla y todos los rangos por debajo del nivel 80 recibieron su propio nivel de dificultad). El mismo concepto se aplica al campo de batalla Isla de la Conquista, con solo dos rangos.

Si miras la base de datos notarás un patrón muy característico que se resume en la tabla siguiente:

| name             | entry             | difficulty_entry_1 | difficulty_entry_2 | difficulty_entry_3 |
| ---------------- | ----------------- | ------------------ | ------------------ | ------------------ |
| Normal Creature  | Different than 0  | 0                  | 0                  | 0                  |
| Dungeon Creature | Normal Dungeon    | Heroic Dungeon     | 0                  | 0                  |
| Raid Creature    | 10man Normal Raid | 25man Normal Raid  | 10man Heroic Raid  | 25man Heroic Raid  |
| Battleground     | 51- 59            | 60-69              | 70-79              | 80                 |

#### KillCredit1

Si esta es una plantilla de crédito de muerte (kill credit) —una plantilla ficticia que se usa cuando más de una criatura puede contar como muerte en una misión—, entonces este es un enlace al primer [entry](#entry) de la criatura que podría matarse para dar crédito de misión.

#### KillCredit2

Si esta es una plantilla de crédito de muerte (kill credit) —una plantilla ficticia que se usa cuando más de una criatura puede contar como muerte en una misión—, entonces este es un enlace al segundo [entry](#entry) de la criatura que podría matarse para dar crédito de misión. Si se pueden matar más de dos criaturas y cuentan para un único objetivo, se requerirá un smart script o un script en C++.

#### name

Nombre base de la criatura.

#### subname

El subnombre de la criatura que aparece entre &lt;&gt; debajo del nombre de la criatura.

#### IconName

Se usa para indicar al jugador qué tipo de NPC es esta criatura.

| IconName           | description                                                                        |
| ------------------ | ---------------------------------------------------------------------------------- |
| **Directions**     | Se usa para guardias y NPC de teletransporte.                                      |
| **Gunner**         | Indicador de un NPC/jugador que controla una torreta.                              |
| **vehichleCursor** | Indicador de que esto es un PCV (vehículo controlado por el jugador).              |
| **Driver**         | Muestra un icono de volante al pasar el ratón por encima.                          |
| **Attack**         | Muestra un icono de espada indicando que puedes atacar este objetivo.             |
| **Buy**            | Muestra un icono de bolsa marrón, normalmente si el NPC solo vende cosas.         |
| **Speak**          | Muestra un icono de burbuja de chat si este NPC tiene opciones de misión/gossip.  |
| **Pickup**         | Muestra un icono de mano agarrando si este NPC puede recogerse para misión/objetos. |
| **Interact**       | Muestra un icono de engranaje comúnmente usado para misión/transporte.            |
| **Trainer**        | Muestra un icono de libro, identificando este NPC como entrenador.                |
| **Taxi**           | Muestra un icono de bota con alas identificando este NPC como taxi.               |
| **Repair**         | Muestra un icono de yunque identificando que este NPC puede reparar.              |
| **LootAll**        | Muestra un icono de varias bolsas marrones (igual que mantener shift antes de saquear una criatura). |
| **Quest**          | Sin uso o desconocido (ver entry 32870 "The Real Ronakada").                      |
| **PVP**            | Sin uso o desconocido (ver entry 29387 "Arena Master: Dalaran Arena").            |

**¡Atención!** Esto no es necesario para que el NPC funcione a menos que estés usando scripts u opciones de gossip. Los nombres distinguen mayúsculas de minúsculas; si tienes dudas, usa un ejemplo de arriba.

#### gossip_menu_id

El ID de gossip de esta criatura. Este campo se obtiene del sniff (update fields). Si no puedes sniffear este valor y necesitas inventar uno, debe ser &gt; 50000. Este campo es el enlace a [gossip_menu.MenuID](gossip_menu#menu_id).

#### minlevel

El nivel mínimo de la criatura si la criatura tiene un rango de nivel.

#### maxlevel

El nivel máximo de la criatura si la criatura tiene un rango de nivel. Al añadirse al mundo, se elige un nivel dentro del rango de nivel especificado.

#### exp

La tabla de expansión de la que se toma el valor de salud de la criatura. Los valores van de 0 a 2. Ver creature_classlevelstats.

| exp | name                   |
| --- | ---------------------- |
| 0   | Classic                |
| 1   | The Burning Crusade    |
| 2   | Wrath of The Lich King |

#### faction

La facción de la criatura. Ver [FactionTemplate](factiontemplate). Que más de una facción tenga el mismo nombre no significa nada: las relaciones entre facciones pueden ser diferentes.

Nota: Este campo también controla la mecánica de asistencia de la familia de criaturas. Solo las criaturas con la misma facción se ayudarán entre sí.

#### npcflag

Un bitmask que representa qué flags de NPC tiene la criatura. Cada bit controla un flag diferente y, para combinar flags, puedes sumar cada flag que quieras, activando así los bits respectivos.

| Flag     |            | Name               | Comment                                                                          |
| -------- | ---------- | ------------------ | -------------------------------------------------------------------------------- |
| 1        | 0x00000001 | Gossip             | Si la criatura tiene más opciones de gossip, añade este flag para mostrar un menú. |
| 2        | 0x00000002 | Quest Giver        | Cualquier criatura que dé o reciba misiones necesita tener este flag.            |
| 16       | 0x00000010 | Trainer            | Permite que la criatura tenga una lista de entrenador para enseñar hechizos      |
| 32       | 0x00000020 | Class Trainer      | Es entrenador de clase                                                           |
| 64       | 0x00000040 | Profession Trainer | Es entrenador de profesión                                                       |
| 128      | 0x00000080 | Vendor             | Es vendedor (genérico). Cualquier criatura que venda objetos necesita este flag. |
| 256      | 0x00000100 | Vendor Ammo        | Es vendedor (munición)                                                           |
| 512      | 0x00000200 | Vendor Food        | Es vendedor (comida)                                                             |
| 1024     | 0x00000400 | Vendor Poison      | Es vendedor (veneno)                                                             |
| 2048     | 0x00000800 | Vendor Reagent     | Es vendedor (reactivos)                                                          |
| 4096     | 0x00001000 | Repairer           | Las criaturas con este flag pueden reparar objetos.                              |
| 8192     | 0x00002000 | Flight Master      | Cualquier criatura que sirva de maestro de vuelo tiene esto.                     |
| 16384    | 0x00004000 | Spirit Healer      | Hace invisible a la criatura para los personajes vivos y tiene la función de resucitar. |
| 32768    | 0x00008000 | Spirit Guide       | Es guía espiritual                                                               |
| 65536    | 0x00010000 | Innkeeper          | Las criaturas con este flag pueden fijar la ubicación de la piedra de hogar.     |
| 131072   | 0x00020000 | Banker             | Las criaturas con este flag pueden mostrar el banco                             |
| 262144   | 0x00040000 | Petitioner         | Gestiona peticiones de hermandad/arena                                          |
| 524288   | 0x00080000 | Tabard Designer    | Permite el diseño de tabardos de hermandad.                                     |
| 1048576  | 0x00100000 | Battlemaster       | Las criaturas con este flag transportan jugadores a campos de batalla.          |
| 2097152  | 0x00200000 | Auctioneer         | Permite que la criatura muestre la lista de subastas.                            |
| 4194304  | 0x00400000 | Stable Master      | Tiene la opción de guardar mascotas para cazadores.                              |
| 8388608  | 0x00800000 | Guild Banker       | Es banquero de hermandad                                                         |
| 16777216 | 0x01000000 | Spellclick         | Necesita datos en la tabla npc_spellclick_spells                                |
| 67108864 | 0x04000000 | Mailbox            | El NPC actuará como buzón (abre el buzón con click derecho)                      |

Así, si quieres un NPC que dé misiones (2), sea vendedor (128) y pueda reparar (4096), simplemente sumas los flags específicos: 2+128+4096=4226

#### speed_walk

Controla la velocidad a la que puede caminar la criatura. Para vehículos: aumenta la velocidad de vuelo.

#### speed_run

Controla la velocidad a la que puede correr la criatura. Para vehículos: aumenta la velocidad de movimiento en tierra.

#### speed_swim

Controla la velocidad a la que puede nadar la criatura.

#### speed_flight

Controla la velocidad a la que puede volar la criatura.

#### detection_range

Controla el rango al que las criaturas detectan y ven a los jugadores.

#### scale

Si es distinto de cero, este campo define el tamaño con el que aparece el modelo de la criatura en el juego. Si es cero, usará el tamaño de modelo por defecto tomado del DBC.

#### rank

El rango de la criatura:

| Rank | Name       | Default Respawn Time Creature.spawntimesecs | Corpse Decay Time Worldserver.conf (Corpse.Decay) | Total Default Respawn spawntimesecs + Corpse.Decay |
| ---- | ---------- | ------------------------------------------- | ------------------------------------------------- | -------------------------------------------------- |
| 0    | Normal     | 5 min                                       | 60 seg                                            | 6 min                                              |
| 1    | Elite      | 5 min                                       | 5 min                                             | 10 min                                             |
| 2    | Rare Elite | 5 min                                       | 5 min                                             | 10 min                                             |
| 3    | Boss       | 5 min                                       | 1 hora                                            | 1 hora, 5 min                                      |
| 4    | Rare       | 5 min                                       | 5 min                                             | 10 min                                             |

**Nota 1:** El rango de un NPC es principalmente visual (lo cual también requiere que se limpie tu Cache para ver los cambios). Cambiar este valor no cambiará su salud, daño ni botín. Sin embargo, cambiará el tiempo de reaparición de la criatura.

**Nota 2:** Los tiempos de reaparición pueden modificarse en otros dos sitios: [Creature.spawntimesecs](creature#spawntimesecs) (solo para ese GUID concreto de la criatura) y en el archivo worldserver.conf bajo la opción "Corpse.Decay" (para TODAS las criaturas del mismo rango). El `spawntimesecs` por defecto para todas las criaturas generadas es de 300 segundos (5 minutos). Por ejemplo, usar el comando ".npc add" para generar un NPC "Normal" le dará un tiempo de reaparición por defecto de 6 minutos (spawntimesecs + tiempo de Corpse.Decay). Además, la criatura debe descomponerse (decay) primero antes de poder reaparecer. Por esta razón, el tiempo de descomposición del cadáver de la criatura es también su tiempo mínimo de reaparición, ya que poner el Creature.spawntimesecs de la criatura = 0 eliminará el tiempo de reaparición por defecto. En el ejemplo de arriba, poner el spawntimesecs de nuestro NPC Normal = 0 hará que el tiempo de reaparición de la criatura disminuya de 6 minutos a 60 segundos.

**Nota 3:** Si quieres que la criatura muestre una calavera o "??" en el retrato (a menudo con jefes), pon los [type_flags](#type_flags) a 4.

#### dmgschool

La escuela de daño cuerpo a cuerpo de la criatura.

| ID  | Name                |
| --- | ------------------- |
| 0   | SPELL_SCHOOL_NORMAL |
| 1   | SPELL_SCHOOL_HOLY   |
| 2   | SPELL_SCHOOL_FIRE   |
| 3   | SPELL_SCHOOL_NATURE |
| 4   | SPELL_SCHOOL_FROST  |
| 5   | SPELL_SCHOOL_SHADOW |
| 6   | SPELL_SCHOOL_ARCANE |

#### BaseAttackTime

Este es el tiempo base que determina cuánto debe esperar una criatura entre ataques cuerpo a cuerpo. Este tiempo está en milisegundos.

#### RangeAttackTime

Este es el tiempo base que determina cuánto debe esperar una criatura entre ataques a distancia. Este tiempo está en milisegundos.

#### BaseVariance

Valor para personalizar la producción de daño de la criatura. Ver [DamageModifier](#damagemodifier).

Las criaturas no personalizadas siempre deben dejar esto en 1.

#### RangeVariance

Valor para personalizar la producción de daño de la criatura. Ver [DamageModifier](#damagemodifier).

Las criaturas no personalizadas siempre deben dejar esto en 1.

#### unit_class

Esta es la clase de la criatura, y dicta los niveles de salud y maná. Ten en cuenta también que la salud y el maná cambiarán según [exp](#exp), [HealthModifier](#healthmodifier) y [ManaModifier](#manamodifier). No establecer este valor generará una advertencia menor en el "DB_Errors.log".

| Value | Name          | Power Shown                                            |
| ----- | ------------- | ------------------------------------------------------ |
| 1     | CLASS_WARRIOR | solo salud (igual que rogue)                           |
| 2     | CLASS_PALADIN | salud y maná (más salud que mage pero menos maná)      |
| 4     | CLASS_ROGUE   | Solo salud (igual que warrior)                         |
| 8     | CLASS_MAGE    | salud y maná (menos salud que paladin pero más maná)   |

#### unit_flags

Permite la aplicación manual de flags de unidad a las criaturas. De nuevo, este es un campo bitmask y, para aplicar más de un flag, simplemente suma los diferentes números. Algunos flags posibles son:

| Flag       |            | Name                                    | Comments                                                                                                                                                                                                                                     |
| ---------- | ---------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1          | 0x00000001 | UNIT_FLAG_SERVER_CONTROLLED             | se establece solo cuando el movimiento de la unidad está controlado por el servidor - mediante paquetes SPLINE/MONSTER_MOVE, junto con UNIT_FLAG_STUNNED; solo se establece en unidades controladas por el cliente; la función de cliente CGUnit_C::IsClientControlled devuelve false cuando está establecido para el propietario |
| 2          | 0x00000002 | UNIT_FLAG_NON_ATTACKABLE                | No atacable                                                                                                                                                                                                                                  |
| 4          | 0x00000004 | UNIT_FLAG_DISABLE_MOVE                  |                                                                                                                                                                                                                                              |
| 8          | 0x00000008 | UNIT_FLAG_PLAYER_CONTROLLED             | Controlado por el jugador, usa _IMMUNE_TO_PC en lugar de _IMMUNE_TO_NPC                                                                                                                                                                       |
| 16         | 0x00000010 | UNIT_FLAG_RENAME                        |                                                                                                                                                                                                                                              |
| 32         | 0x00000020 | UNIT_FLAG_PREPARATION                   | No consume reactivos para hechizos con SPELL_ATTR_EX5_NO_REAGENT_WHILE_PREP                                                                                                                                                                  |
| 64         | 0x00000040 | UNIT_FLAG_UNK_6                         | no está claro qué hace, pero es necesario para lanzar hechizos no activados en smart_scripts                                                                                                                                                 |
| 128        | 0x00000080 | UNIT_FLAG_NOT_ATTACKABLE_1              | ?? (UNIT_FLAG_PLAYER_CONTROLLED                                                                                                                                                                                                              |
| 256        | 0x00000100 | UNIT_FLAG_IMMUNE_TO_PC                  | Deshabilita el combate/asistencia con personajes jugadores (PC)                                                                                                                                                                              |
| 512        | 0x00000200 | UNIT_FLAG_IMMUNE_TO_NPC                 | Deshabilita el combate/asistencia con personajes no jugadores (NPC)                                                                                                                                                                          |
| 1024       | 0x00000400 | UNIT_FLAG_LOOTING                       | Animación de saqueo                                                                                                                                                                                                                          |
| 2048       | 0x00000800 | UNIT_FLAG_PET_IN_COMBAT                 | ¿En combate? 2.0.8                                                                                                                                                                                                                           |
| 4096       | 0x00001000 | UNIT_FLAG_PVP                           | Cambiado en 3.0.3                                                                                                                                                                                                                            |
| 8192       | 0x00002000 | UNIT_FLAG_SILENCED                      | No puede lanzar hechizos                                                                                                                                                                                                                     |
| 16384      | 0x00004000 | UNIT_FLAG_CANNOT_SWIM                   | 2.0.8                                                                                                                                                                                                                                        |
| 32768      | 0x00008000 | UNIT_FLAG_SWIMMING                      | Muestra la animación de nado en el agua                                                                                                                                                                                                      |
| 65536      | 0x00010000 | UNIT_FLAG_NON_ATTACKABLE_2              | Elimina el icono de atacable; si es sobre ti mismo, no puedes asistirte a ti mismo pero puedes lanzar hechizos TARGET_SELF - añadido por SPELL_AURA_MOD_UNATTACKABLE                                                                         |
| 131072     | 0x00020000 | UNIT_FLAG_PACIFIED                      | La criatura no atacará                                                                                                                                                                                                                       |
| 262144     | 0x00040000 | UNIT_FLAG_STUNNED                       | 3.0.3 ok                                                                                                                                                                                                                                     |
| 524288     | 0x00080000 | UNIT_FLAG_IN_COMBAT                     | ('AffectingCombat' de UnitFlags.cs en WPP)                                                                                                                                                                                                   |
| 1048576    | 0x00100000 | UNIT_FLAG_TAXI_FLIGHT                   | Deshabilita el lanzamiento en el lado del cliente de hechizos no permitidos durante vuelo en taxi (¿montado?), probablemente usado con el flag 0x4                                                                                           |
| 2097152    | 0x00200000 | UNIT_FLAG_DISARMED                      | 3.0.3, deshabilita el lanzamiento de hechizos cuerpo a cuerpo..., "Se requiere arma cuerpo a cuerpo" añadido al tooltip de los hechizos cuerpo a cuerpo.                                                                                     |
| 4194304    | 0x00400000 | UNIT_FLAG_CONFUSED                      | Confundido.                                                                                                                                                                                                                                  |
| 8388608    | 0x00800000 | UNIT_FLAG_FLEEING                       | ('Feared' de UnitFlags.cs en WPP)                                                                                                                                                                                                            |
| 16777216   | 0x01000000 | UNIT_FLAG_POSSESSED                     | Bajo control directo del cliente por un jugador (posesión o vehículo)                                                                                                                                                                        |
| 33554432   | 0x02000000 | UNIT_FLAG_NOT_SELECTABLE                | No puede seleccionarse con el ratón ni con el comando /target {nombre}.                                                                                                                                                                      |
| 67108864   | 0x04000000 | UNIT_FLAG_SKINNABLE                     | Desollable                                                                                                                                                                                                                                   |
| 134217728  | 0x08000000 | UNIT_FLAG_MOUNT                         | El cliente parece manejarlo perfectamente. También se usa al crear monturas personalizadas.                                                                                                                                                  |
| 268435456  | 0x10000000 | UNIT_FLAG_UNK_28                        | (PreventKneelingWhenLooting de UnitFlags.cs en WPP)                                                                                                                                                                                          |
| 536870912  | 0x20000000 | UNIT_FLAG_PREVENT_EMOTES_FROM_CHAT_TEXT | Impide reproducir emotes automáticamente al parsear el texto del chat, por ejemplo "lol" en /say, terminar un mensaje con ? o !, o usar /yell                                                                                               |
| 1073741824 | 0x40000000 | UNIT_FLAG_SHEATHE                       |                                                                                                                                                                                                                                              |
| 2147483648 | 0x80000000 | UNIT_FLAG_IMMUNE                        | Inmune al daño                                                                                                                                                                                                                               |

#### unit_flags2

Permite la aplicación adicional de flags de unidad a las criaturas. De nuevo, este es un campo bitmask y, para aplicar más de un flag, simplemente suma los diferentes números. Algunos flags posibles son:


| Flag   |            | Name                                  | Comments                                                                    |
| ------ | ---------- | ------------------------------------- | --------------------------------------------------------------------------- |
| 1      | 0x00000001 | UNIT_FLAG2_FEIGN_DEATH                |                                                                             |
| 2      | 0x00000002 | UNIT_FLAG2_HIDE_BODY                  | Oculta el modelo de la unidad (muestra solo el equipo del jugador)          |
| 4      | 0x00000004 | UNIT_FLAG2_IGNORE_REPUTATION          |                                                                             |
| 8      | 0x00000008 | UNIT_FLAG2_COMPREHEND_LANG            |                                                                             |
| 16     | 0x00000010 | UNIT_FLAG2_MIRROR_IMAGE               |                                                                             |
| 32     | 0x00000020 | UNIT_FLAG2_DO_NOT_FADE_IN             | El modelo de la unidad aparece instantáneamente al ser invocado (no se desvanece al aparecer) |
| 64     | 0x00000040 | UNIT_FLAG2_FORCE_MOVEMENT             |                                                                             |
| 128    | 0x00000080 | UNIT_FLAG2_DISARM_OFFHAND             |                                                                             |
| 256    | 0x00000100 | UNIT_FLAG2_DISABLE_PRED_STATS         | El jugador ha deshabilitado las estadísticas predichas (usado por los marcos de banda) |
| 1024   | 0x00000400 | UNIT_FLAG2_DISARM_RANGED              | esto no deshabilita la visualización del arma a distancia (¿quizá se necesite un flag adicional?) |
| 2048   | 0x00000800 | UNIT_FLAG2_REGENERATE_POWER           |                                                                             |
| 4096   | 0x00001000 | UNIT_FLAG2_RESTRICT_PARTY_INTERACTION | Restringe la interacción al grupo o banda                                   |
| 8192   | 0x00002000 | UNIT_FLAG2_PREVENT_SPELL_CLICK        | Impide el spellclick                                                        |
| 16384  | 0x00004000 | UNIT_FLAG2_ALLOW_ENEMY_INTERACT       |                                                                             |
| 32768  | 0x00008000 | UNIT_FLAG2_CANNOT_TURN                |                                                                             |
| 65536  | 0x00010000 | UNIT_FLAG2_UNK2                       |                                                                             |
| 131072 | 0x00020000 | UNIT_FLAG2_PLAY_DEATH_ANIM            | Reproduce una animación de muerte especial al morir                        |
| 262144 | 0x00040000 | UNIT_FLAG2_ALLOW_CHEAT_SPELLS         | permite lanzar hechizos con AttributesEx7 & SPELL_ATTR7_IS_CHEAT_SPELL      |

#### dynamicflags

Flags que controlan la apariencia visual de la criatura.

Algunos flags conocidos y su uso son:


| Flag |      | Name                                   | Comments                                                                                            |
| ---- | ---- | -------------------------------------- | --------------------------------------------------------------------------------------------------- |
| 0    | 0x00 | UNIT_DYNFLAG_NONE                      |                                                                                                     |
| 1    | 0x01 | UNIT_DYNFLAG_LOOTABLE                  |                                                                                                     |
| 2    | 0x02 | UNIT_DYNFLAG_TRACK_UNIT                | La ubicación de la criatura se verá como un pequeño punto en el minimapa                            |
| 4    | 0x04 | UNIT_DYNFLAG_TAPPED                    | Hace que el nombre de la criatura aparezca en gris (Lua_UnitIsTapped)                               |
| 8    | 0x08 | UNIT_DYNFLAG_TAPPED_BY_PLAYER          | Lua_UnitIsTappedByPlayer, normalmente usado por los PCV (vehículos controlados por el jugador)      |
| 16   | 0x10 | UNIT_DYNFLAG_SPECIALINFO               |                                                                                                     |
| 32   | 0x20 | UNIT_DYNFLAG_DEAD                      | Hace que la criatura parezca muerta (esto NO hace que el nombre de la criatura sea gris ni que no ataque a los jugadores). |
| 64   | 0x40 | UNIT_DYNFLAG_REFER_A_FRIEND            |                                                                                                     |
| 128  | 0x80 | UNIT_DYNFLAG_TAPPED_BY_ALL_THREAT_LIST | Lua_UnitIsTappedByAllThreatList                                                                     |

#### family

La familia a la que pertenece esta criatura.

| ID  | Family       | ID  | Family         |
| --- | ------------ | --- | -------------- |
| 1.  | Wolf         | 26. | Owl            |
| 2.  | Cat          | 27. | Wind Serpent   |
| 3.  | Spider       | 28. | Remote Control |
| 4.  | Bear         | 29. | Felguard       |
| 5.  | Boar         | 30. | Dragonhawk     |
| 6.  | Crocolisk    | 31. | Ravager        |
| 7.  | Carrion Bird | 32. | Warp Stalker   |
| 8.  | Crab         | 33. | Sporebat       |
| 9.  | Gorilla      | 34. | Nether Ray     |
| 11. | Raptor       | 35. | Serpent        |
| 12. | Tallstrider  | 37. | Moth           |
| 15. | Felhunter    | 38. | Chimaera       |
| 16. | Voidwalker   | 39. | Devilsaur      |
| 17. | Succubus     | 40. | Ghoul          |
| 19. | Doomguard    | 41. | Silithid       |
| 20. | Scorpid      | 42. | Worm           |
| 21. | Turtle       | 43. | Rhino          |
| 23. | Imp          | 44. | Wasp           |
| 24. | Bat          | 45. | Core Hound     |
| 25. | Hyena        | 46. | Spirit Beast   |

#### type

El tipo de la criatura.

| ID  | Type           |
| --- | -------------- |
| 0   | None           |
| 1   | Beast          |
| 2   | Dragonkin      |
| 3   | Demon          |
| 4   | Elemental      |
| 5   | Giant          |
| 6   | Undead         |
| 7   | Humanoid       |
| 8   | Critter        |
| 9   | Mechanical     |
| 10  | Not specified  |
| 11  | Totem          |
| 12  | Non-Combat Pet |
| 13  | Gas Cloud      |

#### type_flags

Este campo puede controlar si un mob puede minarse, herborizarse o saquearse por un ingeniero. Si es cualquiera de esas tres cosas, el botín obtenido al desollarlo/minarlo se almacenará en la tabla [skinning_loot_template](loot_template). También controla si este mob puede ser domado por un cazador. Los demás campos no tienen un significado especial en el lado del servidor. El campo entero se enviará al cliente en el SMSG_CREATURE_QUERY_RESPONSE

| Flag       |            | Name                                                 | Comments                                                                                   |
| ---------- | ---------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| 1          | 0x00000001 | CREATURE_TYPE_FLAG_TAMEABLE                          | Hace que el mob sea domable (también debe ser una bestia y tener family establecido)       |
| 2          | 0x00000002 | CREATURE_TYPE_FLAG_VISIBLE_TO_GHOSTS                 | Las criaturas también son visibles para jugadores no vivos. ¿Permite interacción de gossip si npcflag lo permite? |
| 4          | 0x00000004 | CREATURE_TYPE_FLAG_BOSS_MOB                          | Cambia el nivel visible de la criatura a "??" en el retrato de la criatura - Inmune a la repulsión (Knockback). |
| 8          | 0x00000008 | CREATURE_TYPE_FLAG_DO_NOT_PLAY_WOUND_PARRY_ANIMATION | No reproduce la animación de herida al parar.                                              |
| 16         | 0x00000010 | CREATURE_TYPE_FLAG_NO_FACTION_TOOLTIP                | Oculta la facción del tooltip.                                                             |
| 32         | 0x00000020 | CREATURE_TYPE_FLAG_MORE_AUDIBLE                      |                                                                                            |
| 64         | 0x00000040 | CREATURE_TYPE_FLAG_SPELL_ATTACKABLE                  | Atacable con hechizos.                                                                     |
| 128        | 0x00000080 | CREATURE_TYPE_FLAG_INTERACT_WHILE_DEAD               | El jugador puede interactuar con la criatura si está muerta (no el jugador muerto)         |
| 256        | 0x00000100 | CREATURE_TYPE_FLAG_SKIN_WITH_HERBALISM               | Hace el mob herborizable                                                                   |
| 512        | 0x00000200 | CREATURE_TYPE_FLAG_SKIN_WITH_MINING                  | Hace el mob minable                                                                        |
| 1024       | 0x00000400 | CREATURE_TYPE_FLAG_NO_DEATH_MESSAGE                  | No registra la muerte en el combatlog.                                                     |
| 2048       | 0x00000800 | CREATURE_TYPE_FLAG_ALLOW_MOUNTED_COMBAT              | La criatura puede permanecer montada al entrar en combate                                  |
| 4096       | 0x00001000 | CREATURE_TYPE_FLAG_CAN_ASSIST                        | ¿Puede ayudar a cualquier jugador en combate si está en rango?                             |
| 8192       | 0x00002000 | CREATURE_TYPE_FLAG_NO_PET_BAR                        | Usa la barra de mascota.                                                                   |
| 16384      | 0x00004000 | CREATURE_TYPE_FLAG_MASK_UID                          |                                                                                            |
| 32768      | 0x00008000 | CREATURE_TYPE_FLAG_SKIN_WITH_ENGINEERING             | Hace el mob saqueable por un ingeniero                                                     |
| 65536      | 0x00010000 | CREATURE_TYPE_FLAG_TAMEABLE_EXOTIC                   | Domable como mascota exótica. También debe estar establecido el flag domable normal.       |
| 131072     | 0x00020000 | CREATURE_TYPE_FLAG_USE_MODEL_COLLISION_SIZE          | Relacionado con la colisión. (¿usa siempre la caja de colisión por defecto?)              |
| 262144     | 0x00040000 | CREATURE_TYPE_FLAG_ALLOW_INTERACTION_WHILE_IN_COMBAT | Es un arma de asedio.                                                                      |
| 524288     | 0x00080000 | CREATURE_TYPE_FLAG_COLLIDE_WITH_MISSILES             | Los proyectiles pueden colisionar con esta criatura - interactúa con TARGET_DEST_TRAJ      |
| 1048576    | 0x00100000 | CREATURE_TYPE_FLAG_NO_NAME_PLATE                     | Oculta la placa de nombre.                                                                 |
| 2097152    | 0x00200000 | CREATURE_TYPE_FLAG_DO_NOT_PLAY_MOUNTED_ANIMATIONS    | No reproduce animaciones montadas.                                                         |
| 4194304    | 0x00400000 | CREATURE_TYPE_FLAG_IS_LINK_ALL                       |                                                                                            |
| 8388608    | 0x00800000 | CREATURE_TYPE_FLAG_INTERACT_ONLY_WITH_CREATOR        | Solo puede interactuar con su creador.                                                     |
| 16777216   | 0x01000000 | CREATURE_TYPE_FLAG_DO_NOT_PLAY_UNIT_EVENT_SOUNDS     |                                                                                            |
| 33554432   | 0x02000000 | CREATURE_TYPE_FLAG_HAS_NO_SHADOW_BLOB                |                                                                                            |
| 67108864   | 0x04000000 | CREATURE_TYPE_FLAG_TREAT_AS_RAID_UNIT                | La criatura puede ser objetivo de hechizos que requieren que el objetivo esté en el grupo/banda del lanzador |
| 134217728  | 0x08000000 | CREATURE_TYPE_FLAG_FORCE_GOSSIP                      | Permite que la criatura muestre una única opción de gossip.                                |
| 268435456  | 0x10000000 | CREATURE_TYPE_FLAG_DO_NOT_SHEATHE                    |                                                                                            |
| 536870912  | 0x20000000 | CREATURE_TYPE_FLAG_DO_NOT_TARGET_ON_INTERACTION      |                                                                                            |
| 1073741824 | 0x40000000 | CREATURE_TYPE_FLAG_DO_NOT_RENDER_OBJECT_NAME         |                                                                                            |
| 2147483648 | 0x80000000 | CREATURE_TYPE_FLAG_UNIT_IS_QUEST_BOSS                |                                                                                            |

#### lootid

El ID de la plantilla de botín que esta criatura debe usar para generar botines. Ver [creature_loot_template.entry](loot_template#loot_template-entry)

#### pickpocketloot

El ID de la plantilla de botín de robo (pickpocketing) que esta criatura debe usar para generar botines de robo. Ver [pickpocketing_loot_template.entry](loot_template#loot_template-entry)

#### skinloot

El ID de la plantilla de botín de desollado (skinning) que esta criatura debe usar para generar botines de desollado. Ver [skinning_loot_template.entry](loot_template#loot_template-entry)

#### PetSpellDataId

ID, encontrado en CreatureSpellData.dbc, que muestra qué hechizos tiene la mascota en el cliente.

#### VehicleId

Entry del vehículo si la criatura es/tiene una entrada de vehículo. Este campo determina cómo aparece el jugador en el vehículo, cómo se mueve el vehículo, y si se muestra o no la barra de acción del vehículo. Por ejemplo, un vehicleID de 292 hará invisible al jugador, impedirá que el vehículo se desplace lateralmente (pero permitirá adelante/atrás), y mostrará los hechizos de la barra de acción del vehículo (que se definen en [spell1-8](http://trinitycore.atlassian.net#spell)). Debe crearse una entrada de npc_spellclick_spells para este entry de criatura para que esto funcione.

#### mingold

Dinero mínimo que la criatura suelta al ser matada, en cobre.

#### maxgold

Dinero máximo que la criatura suelta al ser matada, en cobre.

#### AIName

Este campo es sobrescrito por el campo ScriptName si ambos están establecidos.

| Name           | Description                                                                                         |
| -------------- | --------------------------------------------------------------------------------------------------- |
| NullCreatureAI | IA vacía, la criatura no hace nada; no puede ser encantada.                                         |
| TriggerAI      | Igual que "NullCreatureAI", excepto que la criatura lanza el hechizo del campo spell1 al ser invocada. |
| AggressorAI    | La criatura ataca al entrar en el radio de aggro; usa solo ataques cuerpo a cuerpo.                |
| ReactorAI      | La criatura ataca solo si es agredida (aggroed); usa solo ataques cuerpo a cuerpo.                  |
| PassiveAI      | La criatura se comporta de forma pasiva, no puede atacar.                                          |
| CritterAI      | Bicho (critter) que huye si es atacado.                                                            |
| GuardAI        | La criatura es un guardia de zona.                                                                 |
| PetAI          | La criatura es una mascota.                                                                        |
| TotemAI        | La criatura lanza el hechizo del campo spell1; no se mueve.                                        |
| CombatAI       | La criatura ataca en cuanto algo está en rango de aggro; también usa hechizos.                     |
| ArcherAI       | La criatura lanza el hechizo del campo spell1; persigue a la víctima.                              |
| TurretAI       | La criatura ataca usando el hechizo del campo spell1; no se mueve.                                 |
| VehicleAI      | La criatura actúa como vehículo del jugador.                                                       |
| SmartAI        | La criatura usa la tabla "[smart_scripts](smart_scripts)" para especificar su comportamiento.      |

#### MovementType

El tipo de movimiento por defecto de la criatura.

| ID  | Type                                              |
| --- | ------------------------------------------------- |
| 0   | Inactivo; permanece en un sitio                   |
| 1   | Movimiento aleatorio dentro del radio wander_distance |
| 2   | Movimiento por waypoints                          |

#### HoverHeight

Distancia sobre el suelo a la que la criatura flotará si tiene habilitado MOVEMENTFLAG_DISABLE_GRAVITY. Valor tomado de sniffs.

#### HealthModifier

Se usa para modificar la salud base de Nivel/Clase de una criatura. Este campo proviene de WDB.

#### ManaModifier

Se usa para modificar el maná base de Nivel/Clase de una criatura. Este campo proviene de WDB.

#### ArmorModifier

Se usa para modificar la armadura base de Nivel/Clase de una criatura.

#### DamageModifier

Se usa para modificar el daño Mínimo/Máximo de una criatura.

Las fórmulas para calcular la producción de daño son:

MINDAMAGE = ((([damage_base](creature_classlevelstats#damage_base) + ([attackpower](creature_classlevelstats#attackpower) / 14) * [BaseVariance](#basevariance)) * DamageModifier) * ([BaseAttackTime](#baseattacktime) / 1000))  
MAXDAMAGE = (((([damage_base](creature_classlevelstats#damage_base) * 1.5) + ([attackpower](creature_classlevelstats#attackpower) / 14) * [BaseVariance](creature_template#basevariance)) * DamageModifier) * ([BaseAttackTime](#baseattacktime) / 1000))

damage_base proviene de la tabla creature_classlevelstats y toma su valor de [damage_base](creature_classlevelstats#damage_base), [damage_exp1](creature_classlevelstats#damage_exp1) o [damage_exp2](creature_classlevelstats#damage_exp2) según el valor de la criatura en [exp](#exp) (0 = base_damage, 1 = damage_exp1, 2 = damage_exp2).

BaseAttackTime es [BaseAttackTime](#baseattacktime) o [RangeAttackTime](#rangeattacktime) dependiendo del tipo de ataque.

attackpower es [attackpower](creature_classlevelstats#attackpower) o [rangedattackpower](creature_classlevelstats#rangedattackpower) dependiendo del tipo de ataque.

BaseVariance es [BaseVariance](#basevariance) o [RangeVariance](#rangevariance) dependiendo del tipo de ataque.


#### ExperienceModifier

¡TODO!

#### RacialLeader

Un flag con dos valores posibles: '1' o '0' que indica si la criatura es un líder racial o no. Matar líderes raciales otorga 100 de honor.

| entry | name                     |
| ----- | ------------------------ |
| 2784  | King Magni Bronzebeard   |
| 3057  | Cairne Bloodhoof         |
| 4949  | Thrall                   |
| 7999  | Tyrande Whisperwind      |
| 10181 | Lady Sylvanas Windrunner |
| 16802 | Lor'themar Theron        |
| 17468 | Prophet Velen            |
| 29611 | King Varian Wrynn        |
| 36648 | Baine Bloodhoof (Leader) |
| 37764 | Lor'themar Theron        |

#### movementId

No tenemos ni idea de qué hace este campo. Se pasa directamente al cliente.

#### RegenHealth

Booleano '1' o '0' que controla si la criatura debe regenerar su salud o no.

#### CreatureImmunitiesId

Referencia a la tabla `creature_immunities`, que centraliza las inmunidades basadas en hechizos y en mecánicas.

Para la lista detallada de mecánicas y bits de escuela de hechizo, ver [creature_immunities](creature_immunities.md).

#### flags_extra

Estos flags controlan ciertos atributos específicos de la criatura. Los flags pueden sumarse para aplicar más de uno.

**Ejemplo:** 32+64=96

| Flag       | Type                                                |            |                                                                                                                                        |
| ---------- | --------------------------------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 1          | CREATURE_FLAG_EXTRA_INSTANCE_BIND                   | 0x00000001 | matar la criatura vincula la instancia al que la mata y a su grupo                                                                     |
| 2          | CREATURE_FLAG_EXTRA_CIVILIAN                        | 0x00000002 | la criatura no hace aggro (ignora la hostilidad de facción/reputación)                                                                 |
| 4          | CREATURE_FLAG_EXTRA_NO_PARRY                        | 0x00000004 | la criatura no para (parry)                                                                                                            |
| 8          | CREATURE_FLAG_EXTRA_NO_PARRY_HASTEN                 | 0x00000008 | la criatura no contraataca al parar                                                                                                    |
| 16         | CREATURE_FLAG_EXTRA_NO_BLOCK                        | 0x00000010 | la criatura no bloquea                                                                                                                 |
| 32         | CREATURE_FLAG_EXTRA_NO_CRUSHING_BLOWS               | 0x00000020 | la criatura no hace golpes aplastantes (crush)                                                                                         |
| 64         | CREATURE_FLAG_EXTRA_NO_XP                           | 0x00000040 | matar la criatura no da XP                                                                                                             |
| 128        | CREATURE_FLAG_EXTRA_TRIGGER                         | 0x00000080 | la criatura es un NPC-trigger (invisible solo para los jugadores)                                                                      |
| 256        | CREATURE_FLAG_EXTRA_NO_TAUNT                        | 0x00000100 | la criatura es inmune a las auras de provocación (taunt) y a los efectos "attack me"                                                   |
| 512        | CREATURE_FLAG_EXTRA_NO_MOVE_FLAGS_UPDATE            | 0x00000200 | (CREATURE_FLAG_EXTRA_UNUSED_10 No implementado) la criatura no actualizará los flags de movimiento                                     |
| 1024       | CREATURE_FLAG_EXTRA_GHOST_VISIBILITY                | 0x00000400 | la criatura solo será visible para jugadores muertos                                                                                   |
| 2048       | CREATURE_FLAG_EXTRA_USE_OFFHAND_ATTACK              | 0x00000800 | la criatura usará ataques de mano secundaria (offhand)                                                                                 |
| 4096       | CREATURE_FLAG_EXTRA_NO_SELL_VENDOR                  | 0x00001000 | los jugadores no pueden vender objetos a este vendedor                                                                                 |
| 8192       | CREATURE_FLAG_EXTRA_CANNOT_ENTER_COMBAT             | 0x00002000 | la criatura no puede entrar en combate (no atacará ni será atacada)                                                                    |
| 16384      | CREATURE_FLAG_EXTRA_WORLDEVENT                      | 0x00004000 | flag personalizado para eventos del mundo (espacio dejado para hacer merge)                                                            |
| 32768      | CREATURE_FLAG_EXTRA_GUARD                           | 0x00008000 | la criatura es un guardia (ignorará finta de muerte y desvanecerse)                                                                    |
| 65536      | CREATURE_FLAG_EXTRA_IGNORE_FEIGN_DEATH              | 0x00010000 | la criatura ignora la finta de muerte (feign death)                                                                                    |
| 131072     | CREATURE_FLAG_EXTRA_NO_CRIT                         | 0x00020000 | la criatura no hace golpes críticos                                                                                                    |
| 262144     | CREATURE_FLAG_EXTRA_NO_SKILL_GAINS                  | 0x00040000 | la criatura no aumentará las habilidades de arma                                                                                       |
| 524288     | CREATURE_FLAG_EXTRA_OBEYS_TAUNT_DIMINISHING_RETURNS | 0x00080000 | la provocación (taunt) de la criatura está sujeta a rendimientos decrecientes                                                          |
| 1048576    | CREATURE_FLAG_EXTRA_ALL_DIMINISH                    | 0x00100000 | La criatura está sujeta a todos los rendimientos decrecientes                                                                          |
| 2097152    | CREATURE_FLAG_EXTRA_NO_PLAYER_DAMAGE_REQ            | 0x00200000 | la criatura no necesita recibir daño del jugador para dar crédito de muerte                                                            |
| 4194304    | CREATURE_FLAG_EXTRA_AVOID_AOE                       | 0x00400000 | ignorada por ataques de área (para el npc del icc blood prince council - Dark Nucleus)                                                 |
| 8388608    | CREATURE_FLAG_EXTRA_NO_DODGE                        | 0x00800000 | el objetivo no puede esquivar                                                                                                          |
| 16777216   | CREATURE_FLAG_EXTRA_MODULE                          | 0x01000000 | Usado por criaturas de módulos para evitar comprobaciones de tipo blizzlike.                                                           |
| 33554432   | CREATURE_FLAG_EXTRA_DONT_CALL_ASSISTANCE            | 0x02000000 | Impide que las criaturas pidan asistencia al hacer aggro inicial                                                                       |
| 67108864   | CREATURE_FLAG_EXTRA_IGNORE_ALL_ASSISTANCE_CALLS     | 0x04000000 | Impide que la criatura responda a las peticiones de asistencia                                                                         |
| 134217728  | CREATURE_FLAG_EXTRA_DONT_OVERRIDE_SAI_ENTRY         | 0x08000000 | Permite a las criaturas usar SAI específico tanto por GUID como por ENTRY sin que uno sobrescriba al otro                              |
| 268435456  | CREATURE_FLAG_EXTRA_DUNGEON_BOSS                    | 0x10000000 | La criatura es un jefe de mazmorra. Este flag lo establece genéricamente el core en tiempo de ejecución. Establecerlo en la base de datos te dará un error de arranque. |
| 536870912  | CREATURE_FLAG_EXTRA_IGNORE_PATHFINDING              | 0x20000000 | La criatura ignorará el pathfinding. Esto es como deshabilitar los Mmaps, solo para una criatura.                                      |
| 1073741824 | CREATURE_FLAG_EXTRA_IMMUNITY_KNOCKBACK              | 0x40000000 | la criatura será inmune a todos los efectos de repulsión (knockback)                                                                   |
| 2147483648 | CREATURE_FLAG_EXTRA_HARD_RESET                      | 0x80000000 | La criatura desaparecerá al evadir                                                                                                     |

#### ScriptName

El nombre del script que usa esta criatura, si lo hay. Esto vincula un script de un motor de scripting a esta criatura.

#### VerifiedBuild

Este campo se usaba para determinar si una plantilla ha sido verificada a partir de archivos WDB.

Si el valor es 0, entonces aún no ha sido parseada.

Si el valor es mayor que 0, entonces ha sido parseada con archivos WDB de esa build de cliente específica.

Si el valor es -1, entonces es solo un marcador de posición hasta que se encuentren datos adecuados en los WDB.

Si el valor es -Client Build, entonces fue parseada con archivos WDB de esa [build de cliente](http://archive.trinitycore.info/DB:Auth:realmlist#gamebuild "DB:Auth:realmlist") específica y editada manualmente después por alguna necesidad especial.

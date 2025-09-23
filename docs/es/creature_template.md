# creature_template

[<-Volver a:World](database-world)

**Tabla \`creature_template\`**

Esta tabla contiene la descripción de las criaturas. Cada criatura generada es una instancia de una plantilla presente en esta tabla, lo que significa que todas las criaturas DEBEN estar definidas en esta tabla.

**Estructura**

| Campo                                              | Tipo               | Nulo | Llave | Por defecto | Extra | Comentario                            |
| -------------------------------------------------- | ------------------ | ---- | ----- | ----------- | ----- | ------------------------------------  |
| [entry](#entry)                                    | MEDIUMINT UNSIGNED | NO   | PRI   | 0           |       |                                       |
| [difficulty_entry_1](#difficultyentryx)            | MEDIUMINT UNSIGNED | NO   |       | 0           |       |                                       |
| [difficulty_entry_2](#difficultyentryx)            | MEDIUMINT UNSIGNED | NO   |       | 0           |       |                                       |
| [difficulty_entry_3](#difficultyentryx)            | MEDIUMINT UNSIGNED | NO   |       | 0           |       |                                       |
| [KillCredit1](#killcredit1)                        | INT UNSIGNED       | NO   |       | 0           |       |                                       |
| [KillCredit2](#killcredit2)                        | INT UNSIGNED       | NO   |       | 0           |       |                                       |
| [name](#name)                                      | char(100)          | NO   | MUL   | 0           |       |                                       |
| [subname](#subname)                                | char(100)          | Si   |       | (NULL)      |       |                                       |
| [IconName](#iconname)                              | char(100)          | Si   |       | (NULL)      |       |                                       |
| [gossip_menu_id](#gossipmenuid)                    | MEDIUMINT UNSIGNED | NO   |       | 0           |       |                                       |
| [minlevel](#minlevel)                              | TINYINT UNSIGNED   | NO   |       | 1           |       |                                       |
| [maxlevel](#maxlevel)                              | TINYINT UNSIGNED   | NO   |       | 1           |       |                                       |
| [exp](#exp)                                        | SMALLINT           | NO   |       | 0           |       |                                       |
| [faction](#faction)                                | SMALLINT UNSIGNED  | NO   |       | 0           |       |                                       |
| [npcflag](#npcflag)                                | INT UNSIGNED       | NO   |       | 0           |       |                                       |
| [speed_walk](#speedwalk)                           | FLOAT              | NO   |       | 1           |       | Resultado de 2,5/2,5, valor más común |
| [speed_run](#speedrun)                             | FLOAT              | NO   |       | 1.14286     |       | Resultado de 8.0/7.0, valor más común |
| [speed_swim](#speedswim)                           | FLOAT              | NO   |       | 1           |       |                                       |
| [speed_swim](#speedflight)                         | FLOAT              | NO   |       | 1           |       |                                       |
| [detection_range](#detectionrange)                 | FLOAT              | NO   |       | 20          |       |                                       |
| [scale](#scale)                                    | FLOAT              | NO   |       | 1           |       |                                       |
| [rank](#rank)                                      | TINYINT UNSIGNED   | NO   |       | 0           |       |                                       |
| [dmgschool](#dmgschool)                            | TINYINT            | NO   |       | 0           |       |                                       |
| [BaseAttackTime](#baseattacktime)                  | INT UNSIGNED       | NO   |       | 0           |       |                                       |
| [RangeAttackTime](#rangeattacktime)                | INT UNSIGNED       | NO   |       | 0           |       |                                       |
| [BaseVariance](#basevariance)                      | FLOAT              | NO   |       | 1           |       |                                       |
| [RangeVariance](#rangevariance)                    | FLOAT              | NO   |       | 1           |       |                                       |
| [unit_class](#unitclass)                           | TINYINT UNSIGNED   | NO   |       | 0           |       |                                       |
| [unit_flags](#unitflags)                           | INT UNSIGNED       | NO   |       | 0           |       |                                       |
| [unit_flags2](#unitflags2)                         | INT UNSIGNED       | NO   |       | 0           |       |                                       |
| [dynamicflags](#dynamicflags)                      | INT UNSIGNED       | NO   |       | 0           |       |                                       |
| [family](#family)                                  | TINYINT            | NO   |       | 0           |       |                                       |
| [trainer_type](#trainertype)                       | TINYINT            | NO   |       | 0           |       |                                       |
| [trainer_spell](#trainerspell)                     | MEDIUMINT UNSIGNED | NO   |       | 0           |       |                                       |
| [trainer_class](#trainerclass)                     | TINYINT UNSIGNED   | NO   |       | 0           |       |                                       |
| [trainer_race](#trainerrace)                       | TINYINT UNSIGNED   | NO   |       | 0           |       |                                       |
| [type](#type)                                      | TINYINT UNSIGNED   | NO   |       | 0           |       |                                       |
| [type_flags](#typeflags)                           | INT UNSIGNED       | NO   |       | 0           |       |                                       |
| [lootid](#lootid)                                  | MEDIUMINT UNSIGNED | NO   |       | 0           |       |                                       |
| [pickpocketloot](#pickpocketloot)                  | MEDIUMINT UNSIGNED | NO   |       | 0           |       |                                       |
| [skinloot](#skinloot)                              | MEDIUMINT UNSIGNED | NO   |       | 0           |       |                                       |
| [PetSpellDataId](#petspelldataid)                  | MEDIUMINT UNSIGNED | NO   |       | 0           |       |                                       |
| [VehicleId](#vehicleid)                            | MEDIUMINT UNSIGNED | NO   |       | 0           |       |                                       |
| [mingold](#mingold)                                | MEDIUMINT UNSIGNED | NO   |       | 0           |       |                                       |
| [maxgold](#maxgold)                                | MEDIUMINT UNSIGNED | NO   |       | 0           |       |                                       |
| [AIName](#ainame)                                  | char(64)           | NO   |       |             |       |                                       |
| [MovementType](#movementtype)                      | TINYINT UNSIGNED   | NO   |       | 0           |       |                                       |
| [HoverHeight](#hoverheight)                        | FLOAT              | NO   |       | 1           |       |                                       |
| [HealthModifier](#healthmodifier)                  | FLOAT              | NO   |       | 1           |       |                                       |
| [ManaModifier](#manamodifier)                      | FLOAT              | NO   |       | 1           |       |                                       |
| [ArmorModifier](#armormodifier)                    | FLOAT              | NO   |       | 1           |       |                                       |
| [DamageModifier](#damagemodifier)                  | FLOAT              | NO   |       | 1           |       |                                       |
| [ExperienceModifier](#experiencemodifier)          | FLOAT              | NO   |       | 1           |       |                                       |
| [RacialLeader](#racialleader)                      | TINYINT UNSIGNED   | NO   |       | 0           |       |                                       |
| [movementId](#movementid)                          | INT UNSIGNED       | NO   |       | 0           |       |                                       |
| [RegenHealth](#regenhealth)                        | TINYINT UNSIGNED   | NO   |       | 1           |       |                                       |
| [mechanic_immune_mask](#mechanicimmunemask)        | INT UNSIGNED       | NO   |       | 0           |       |                                       |
| [spell_school_immune_mask](#spellschoolimmunemask) | INT UNSIGNED       | NO   |       | 0           |       |                                       |
| [flags_extra](#flagsextra)                         | INT UNSIGNED       | NO   |       | 0           |       |                                       |
| [ScriptName](#scriptname)                          | char(64)           | NO   |       |             |       |                                       |
| [VerifiedBuild](#verifiedbuild)                    | SMALLINT           | Si   |       | 0           |       |                                       |

---

**Descripción de los campos**

#### entry

Identificación única de la criatura.

#### difficulty_entry_x

| nombre                                                    | entrada | difficulty_entry_1 | difficulty_entry_2 | difficulty_entry_3 |
| --------------------------------------------------------- | ------- | ------------------ | ------------------ | ------------------ |
| [Anomalus](http://www.wowhead.com/npc=26763/anomalus)     | 26763   | 30529              | 0                  | 0                  |
| [Sindragosa](http://www.wowhead.com/npc=36853/sindragosa) | 36853   | 38265              | 38266              | 38267              |

Anomalus es un jefe de 5 personajes ubicado en El Nexo. Puedes enfrentarte a él en dos niveles de dificultad (mazmorra normal y mazmorra heroica). Dependiendo de la dificultad, los jefes tienen diferentes estadísticas, como salud y daño. En el caso de Anomalus, la información de la entrada 26763 se usa al enfrentarlo en dificultad normal y la de la entrada 30529 al enfrentarlo en dificultad heroica.

Sindragosa, un jefe de incursión ubicado en la Ciudadela de la Corona de Hielo, se puede combatir en 4 dificultades diferentes debido a la introducción de los modos de incursión heroica en el parche 3.2 (normal/heroico de 10 jugadores, normal/heroico de 25 jugadores). Dependiendo del tipo de dificultad, debe tener diferentes estadísticas. Por lo tanto, si la ves en una incursión normal de 10 jugadores, usará la información de la entrada 36853, en una incursión normal de 25 jugadores se usará la entrada 38265, y así sucesivamente. Esto contrasta marcadamente con jefes de incursión como Patchwerk y XT-002 Deconstructor, ubicados en Naxxramas y Ulduar respectivamente, que solo tienen dos modos de incursión diferentes (normal de 10 jugadores y normal de 25 jugadores). Los modos difíciles dentro de la incursión de Ulduar no tienen su propia plantilla, debido a que la mecánica del juego activa la dificultad más alta durante el propio encuentro.

Aquí tenemos un caso especial con el campo de batalla del Valle de Alterac. Hay cuatro niveles donde los PNJ son más fáciles o más difíciles según tu nivel (añadido en el parche 3.2.2 de WoW, cuando los personajes de nivel 80 recibieron su propio nivel para este campo de batalla y todos los niveles inferiores recibieron su propio nivel de dificultad). El mismo concepto se aplica al campo de batalla de la Isla de la Conquista, con solo dos niveles.

Si observa la base de datos, notará un patrón muy característico que se resume en la siguiente tabla:

| nombre                  | entrada                        | difficulty_entry_1             | difficulty_entry_2               | difficulty_entry_3              |
| ----------------------- | ------------------------------ | ------------------------------ | -------------------------------- | ------------------------------- |
| Criatura normal         | Diferente a 0                  | 0                              | 0                                | 0                               |
| Criatura de la mazmorra | Mazmorra normal                | Mazmorra heroica               | 0                                | 0                               |
| Raid Creature           | Incursión normal de 10 hombres | Incursión normal de 25 hombres | Incursión heroica de 10 hombres  | Incursión heroica de 25 hombres |
| Criatura de incursión   | 51- 59                         | 60-69                          | 70-79                            | 80                              |

#### KillCredit1

Si esta es una plantilla de crédito por muerte (una plantilla ficticia que se usa cuando más de una criatura puede contar como muerte en una misión), entonces este es un enlace a la primera [entrada](#entrada) de la criatura que podría ser asesinada para dar crédito a la misión.

#### KillCredit2

Si se trata de una plantilla de crédito por muerte (una plantilla ficticia que se usa cuando más de una criatura puede contar como muerte en una misión), este es un enlace a la segunda [entrada](#entrada) de la criatura que podría matarse para dar crédito por la misión. Si se pueden matar más de dos criaturas y contar para un solo objetivo, se requerirá un script inteligente o de C++.

#### name

Nombre base de la criatura.

#### subname

El subnombre de la criatura que aparece en &lt;&gt; debajo del nombre de la criatura.

#### IconName

Se utiliza para indicar al jugador qué tipo de PNJ es esta criatura.

| IconName           | Descripción                                                                                                            |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **Directions**     | Se utiliza para guardias y NPC teletransportadores.                                                                    |
| **Gunner**         | Indicador de una torreta controlada por un NPC o jugador.                                                              |
| **vehichleCursor** | Indicador de que se trata de un PCV (vehículo controlado por el jugador)                                               |
| **Driver**         | Muestra un icono de volante cuando pasa el mouse sobre él.                                                             |
| **Attack**         | Muestra un icono de espada que indica que puedes atacar a este objetivo.                                               |
| **Buy**            | Generalmente muestra un ícono de bolsa marrón si el NPC solo vende cosas.                                              |
| **Speak**          | Muestra un icono de burbuja de chat si este NPC tiene opciones de misión o chismes.                                    |
| **Pickup**         | Muestra un ícono de una mano agarrando si este NPC puede recogerse para realizar misiones o conseguir objetos.         |
| **Interact**       | Muestra el ícono de engranaje que se usa comúnmente para misiones/transporte.                                          |
| **Trainer**        | Muestra un ícono de libro que identifica a este NPC como entrenador.                                                   |
| **Taxi**           | Muestra un ícono de bota con alas que identifica a este NPC como un taxi.                                              |
| **Repair**         | Muestra un icono de yunque que identifica que este NPC puede reparar.                                                  |
| **LootAll**        | Muestra un ícono de bolsa marrón múltiple (igual que mantener presionada la tecla Shift antes de saquear una criatura).|
| **Quest**          | Sin usar o desconocido (ver entrada 32870 "La verdadera Ronakada").                                                    |
| **PVP**            | Sin usar o desconocido (ver entrada 29387 "Arena Master: Dalaran Arena").                                              |

**¡Atención!** Esto no es necesario para que funcione el NPC a menos que estés usando scripts u opciones de chismes. Los nombres distinguen entre mayúsculas y minúsculas. En caso de duda, utiliza un ejemplo anterior.

#### gossip_menu_id

El ID de chisme de esta criatura. Este campo se obtiene de sniff (actualizar campos). Si no puedes rastrear este valor y necesitas crear uno, debe ser > 50000. Este campo es el enlace a [gossip_menu.MenuID](gossip_menu#menu_id).

#### minlevel

El nivel mínimo de la criatura si la criatura tiene un rango de nivel.

#### maxlevel

El nivel máximo de la criatura si tiene un rango de nivel. Al añadirse al mundo, se elige un nivel dentro del rango especificado.

#### exp

La tabla de expansión de la que se toma el valor de salud de las criaturas. Los valores van de 0 a 2. Ver creature_classlevelstats.

| exp | Nombre                 |
| --- | ---------------------- |
| 0   | Classic                |
| 1   | The Burning Crusade    |
| 2   | Wrath of The Lich King |

#### faction

La facción de la criatura. Ver [FactionTemplate](FactionTemplate). El hecho de que más de una facción tenga el mismo nombre implica que las relaciones entre facciones pueden ser diferentes.

Nota: Este campo también controla la mecánica de asistencia de familias de criaturas. Solo las criaturas de la misma facción se asistirán entre sí.

#### npcflag

Una máscara de bits que representa las banderas de PNJ que posee la criatura. Cada bit controla una bandera diferente y, para combinar banderas, puedes agregar las que quieras, activando así los bits respectivos.

| Bandera  |            | Nombre                    | Comentario                                                                                       |
| -------- | ---------- | ------------------------- | ------------------------------------------------------------------------------------------------ |
| 1        | 0x00000001 | Chisme                    | Si la criatura tiene más opciones de chismes, agrega esta bandera para que aparezca un menú.     |
| 2        | 0x00000002 | Dador de misiones         | Cualquier criatura que dé o reciba misiones debe tener esta bandera.                             |
| 16       | 0x00000010 | Entrenador                | Permite que la criatura tenga una lista de entrenadores para enseñar hechizos.                   |
| 32       | 0x00000020 | Entrenador de clase       | Es un entrenador de clase                                                                        |
| 64       | 0x00000040 | Entrenador de Profesiones | Es un formador profesional                                                                       |
| 128      | 0x00000080 | Proveedor                 | Es un vendedor (genérico). Cualquier criatura que venda objetos debe tener esta bandera.         |
| 256      | 0x00000100 | Munición del vendedor     | Es un vendedor (munición)                                                                        |
| 512      | 0x00000200 | Comida de vendedor        | Es un vendedor (de comida)                                                                       |
| 1024     | 0x00000400 | Vendedor de veneno        | Es un vendedor (veneno)                                                                          |
| 2048     | 0x00000800 | Reactivo del proveedor    | Es un proveedor (Reactivo)                                                                       |
| 4096     | 0x00001000 | Reparador                 | Las criaturas con esta bandera pueden reparar objetos.                                           |
| 8192     | 0x00002000 | Maestro de vuelo          | Cualquier criatura que actúe como maestro de vuelo tiene esto.                                   |
| 16384    | 0x00004000 | Sanador espiritual        | Hace que la criatura sea invisible para los personajes vivos y tiene la función de resurrección. |
| 32768    | 0x00008000 | Guía espiritual           | Es un guía espiritual                                                                            |
| 65536    | 0x00010000 | Posadero                  | Las criaturas con esta bandera pueden establecer ubicaciones de piedras de hogar.                |
| 131072   | 0x00020000 | Banquero                  | Las criaturas con esta bandera pueden mostrar el banco                                           |
| 262144   | 0x00040000 | Peticionario              | Maneja peticiones de gremios/arenas                                                              |
| 524288   | 0x00080000 | Diseñador de tabardos     | Permite el diseño de tabardos de gremio.                                                         |
| 1048576  | 0x00100000 | Maestro de batalla        | Las criaturas con esta bandera transportan jugadores a los campos de batalla.                    |
| 2097152  | 0x00200000 | Subastador                | Permite que la criatura muestre la lista de subastas.                                            |
| 4194304  | 0x00400000 | Maestro de establos       | Tiene la opción de tener mascotas estables para los cazadores.                                   |
| 8388608  | 0x00800000 | Banquero del gremio       | Es banquero del gremio                                                                           |
| 16777216 | 0x01000000 | Clic ortográfico          | Necesita datos en la tabla npc_spellclick_spells                                                 |
| 67108864 | 0x04000000 | Buzón                     | El NPC actuará como un buzón (abre el buzón con un clic derecho)                                 |

Entonces, si quieres un NPC que sea dador de misiones (2), vendedor (128) y pueda reparar (4096), simplemente suma banderas específicas: 2 + 128 + 4096 = 4226

#### speed_walk

Controla la velocidad de la criatura al caminar. Para vehículos: aumenta la velocidad de vuelo.

#### speed_run

Controla la velocidad de carrera de la criatura. Para vehículos: aumenta la velocidad de movimiento terrestre.

#### speed_swim

Controla qué tan rápido puede nadar la criatura.

#### speed_flight

Controla qué tan rápido puede volar la criatura.

#### detection_range

Controla el rango en el que las criaturas detectan y ven a los jugadores.

#### scale

Si es distinto de cero, este campo define el tamaño del modelo de la criatura en el juego. Si es cero, se usará el tamaño predeterminado del modelo, tomado del DBC.

#### rank

El rango de la criatura:

| Rango | Nombre     | Tiempo de reaparición predeterminado Creature.spawntimesecs | Tiempo de descomposición de cadáveres Worldserver.conf (Corpse.Decay) | Tiempo total de reaparición predeterminado en segundos + descomposición del cadáver |
| ----- | ---------- | ----------------------------------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| 0     | Normal     | 5 min                                                       | 60 sec                                                                | 6 min                                                                               |
| 1     | Élite      | 5 min                                                       | 5 min                                                                 | 10 min                                                                              |
| 2     | Élite rara | 5 min                                                       | 5 min                                                                 | 10 min                                                                              |
| 3     | Jefe       | 5 min                                                       | 1 hour                                                                | 1 hour, 5 min                                                                       |
| 4     | Extraño    | 5 min                                                       | 5 min                                                                 | 10 min                                                                              |

**Nota 1:** El rango de un PNJ es principalmente visual (lo que también requiere que tu caché esté vacía para ver los cambios). Cambiar este valor no cambiará su salud, daño ni botín. Sin embargo, cambiará el tiempo de reaparición de la criatura.

**Nota 2:** Los tiempos de reaparición se pueden modificar en otros dos lugares: [Creature.spawntimesecs](creature#spawntimesecs) (solo para ese GUID único de la criatura) y en el archivo worldserver.conf bajo la configuración de "Corpse.Decay" (para TODAS las criaturas del mismo rango). El \`spawntimesecs\` predeterminado para todas las criaturas generadas es de 300 segundos (5 minutos). Por ejemplo, usar el comando ".npc add" para generar un PNJ "Normal" le dará un tiempo de reaparición predeterminado de 6 minutos (spawntimesecs + tiempo de Corpse.Decay). Además, la criatura debe descomponerse primero antes de poder reaparecer. Por esta razón, el Tiempo de Descomposición del Cadáver de la criatura también es su tiempo mínimo de reaparición, ya que establecer Creature.spawntimesecs = 0 eliminará el Tiempo de Reaparición Predeterminado. En el ejemplo anterior, establecer spawntimesecs = 0 para nuestro NPC normal significará que el tiempo de reaparición de la criatura disminuirá de 6 minutos a 60 segundos.

**Nota 3:** Si quieres que la criatura muestre una calavera o "??" en el retrato (a menudo con los jefes), establece [type_flags](#type_flags) en 4.

#### dmgschool

Escuela de daño cuerpo a cuerpo de la criatura.

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

Este es el tiempo base que determina cuánto debe esperar una criatura entre ataques cuerpo a cuerpo. Este tiempo se expresa en milisegundos.

#### RangeAttackTime

Este es el tiempo base que determina cuánto debe esperar una criatura entre ataques a distancia. Este tiempo se expresa en milisegundos.

#### BaseVariance

Valor para personalizar el daño de la criatura. Ver [DamageModifier](#damagemodifier).

Las criaturas no personalizadas siempre deben dejar esto en 1.

#### RangeVariance

Valor para personalizar el daño de la criatura. Ver [DamageModifier](#damagemodifier).

Las criaturas no personalizadas siempre deben dejar esto en 1.

#### unit_class

Esta es la clase de la criatura y determina los niveles de salud y maná. Ten en cuenta que la salud y el maná cambiarán según [exp](#exp), [HealthModifier](#healthmodifier) ​​y [ManaModifier](#manamodifier). Si no se establece este valor, se mostrará una pequeña advertencia en el archivo "DB_Errors.log".

| Valor | Nombre        | Poder mostrado                                          |
| ----- | ------------- | ------------------------------------------------------- |
| 1     | CLASS_WARRIOR | Solo salud (igual que pícaro)                           |
| 2     | CLASS_PALADIN | Salud y maná (más salud que el mago pero menos maná)    |
| 4     | CLASS_ROGUE   | Solo salud (igual que guerrero)                         |
| 8     | CLASS_MAGE    | Salud y maná (menos salud que el paladín pero más maná) |

#### unit_flags

Permite la aplicación manual de indicadores de unidad a las criaturas. Este campo es una máscara de bits y, para aplicar más de un indicador, simplemente suma los diferentes números. Algunos indicadores posibles son:

| Bandera       |            | Nombre                                    | Comentarios                                                                                                                                                                                                                                                                                                         |
| ---------- | ---------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1          | 0x00000001 | UNIT_FLAG_SERVER_CONTROLLED             | Se establece solo cuando el movimiento de la unidad está controlado por el servidor (por paquetes SPLINE/MONSTER_MOVE, junto con UNIT_FLAG_STUNNED); solo se establece en unidades controladas por el cliente; la función de cliente CGUnit_C::IsClientControlled devuelve falso cuando se establece para el propietario |
| 2          | 0x00000002 | UNIT_FLAG_NON_ATTACKABLE                | No atacable                                                                                                                                                                                                                                                                                                              |
| 4          | 0x00000004 | UNIT_FLAG_DISABLE_MOVE                  |                                                                                                                                                                                                                                                                                                                          |
| 8          | 0x00000008 | UNIT_FLAG_PLAYER_CONTROLLED             | Controlado por el jugador, use _IMMUNE_TO_PC en lugar de _IMMUNE_TO_NPC                                                                                                                                                                                                                                                  |
| 16         | 0x00000010 | UNIT_FLAG_RENAME                        |                                                                                                                                                                                                                                                                                                                          |
| 32         | 0x00000020 | UNIT_FLAG_PREPARATION                   | No tomes reactivos para hechizos con SPELL_ATTR_EX5_NO_REAGENT_WHILE_PREP                                                                                                                                                                                                                                                |
| 64         | 0x00000040 | UNIT_FLAG_UNK_6                         | No estoy seguro de qué hace, pero es necesario para lanzar hechizos no activados en smart_scripts                                                                                                                                                                                                                        |
| 128        | 0x00000080 | UNIT_FLAG_NOT_ATTACKABLE_1              | ?? (UNIT_FLAG_PLAYER_CONTROLLED                                                                                                                                                                                                                                                                                          |
| 256        | 0x00000100 | UNIT_FLAG_IMMUNE_TO_PC                  | Combate/asistencia deshabilitados con personajes jugadores (PC)                                                                                                                                                                                                                                                          |
| 512        | 0x00000200 | UNIT_FLAG_IMMUNE_TO_NPC                 | Combate/asistencia deshabilitados con personajes no jugadores (NPC)                                                                                                                                                                                                                                                      |
| 1024       | 0x00000400 | UNIT_FLAG_LOOTING                       | Animación de botín                                                                                                                                                                                                                                                                                                       |
| 2048       | 0x00000800 | UNIT_FLAG_PET_IN_COMBAT                 | ¿En combate? 2.0.8                                                                                                                                                                                                                                                                                                       |
| 4096       | 0x00001000 | UNIT_FLAG_PVP                           | Cambiado en 3.0.3                                                                                                                                                                                                                                                                                                        |
| 8192       | 0x00002000 | UNIT_FLAG_SILENCED                      | No puedo lanzar hechizos                                                                                                                                                                                                                                                                                                 |
| 16384      | 0x00004000 | UNIT_FLAG_CANNOT_SWIM                   | 2.0.8                                                                                                                                                                                                                                                                                                                    |
| 32768      | 0x00008000 | UNIT_FLAG_SWIMMING                      | Muestra animación de natación en el agua.                                                                                                                                                                                                                                                                                |
| 65536      | 0x00010000 | UNIT_FLAG_NON_ATTACKABLE_2              | Elimina el ícono atacable; si está sobre ti, no puede ayudarse a sí mismo, pero puede lanzar hechizos TARGET_SELF (agregado por SPELL_AURA_MOD_UNATTACKABLE)                                                                                                                                                             |
| 131072     | 0x00020000 | UNIT_FLAG_PACIFIED                      | La criatura no atacará                                                                                                                                                                                                                                                                                                   |
| 262144     | 0x00040000 | UNIT_FLAG_STUNNED                       | 3.0.3 ok                                                                                                                                                                                                                                                                                                                 |
| 524288     | 0x00080000 | UNIT_FLAG_IN_COMBAT                     | ('AffectingCombat' de UnitFlags.cs en WPP)                                                                                                                                                                                                                                                                               |
| 1048576    | 0x00100000 | UNIT_FLAG_TAXI_FLIGHT                   | Deshabilitar el lanzamiento en el lado del cliente de hechizos no permitidos por el vuelo de taxi (¿montado?), probablemente usado con la bandera 0x4                                                                                                                                                                    |
| 2097152    | 0x00200000 | UNIT_FLAG_DISARMED                      | 3.0.3, deshabilitar el lanzamiento de hechizos cuerpo a cuerpo..., se agregó "Arma cuerpo a cuerpo requerida" a la descripción de los hechizos cuerpo a cuerpo.                                                                                                                                                          |
| 4194304    | 0x00400000 | UNIT_FLAG_CONFUSED                      | Confundido.                                                                                                                                                                                                                                                                                                              |
| 8388608    | 0x00800000 | UNIT_FLAG_FLEEING                       | ('Feared' de UnitFlags.cs en WPP)                                                                                                                                                                                                                                                                                        |
| 16777216   | 0x01000000 | UNIT_FLAG_POSSESSED                     | Bajo control directo del cliente por parte de un jugador (posesión o vehículo)                                                                                                                                                                                                                                           |
| 33554432   | 0x02000000 | UNIT_FLAG_NOT_SELECTABLE                | No se puede seleccionar con el mouse ni con el comando /target {name}.                                                                                                                                                                                                                                                   |
| 67108864   | 0x04000000 | UNIT_FLAG_SKINNABLE                     | Personalizable                                                                                                                                                                                                                                                                                                           |
| 134217728  | 0x08000000 | UNIT_FLAG_MOUNT                         | El cliente parece manejarlo a la perfección. También se utiliza para crear monturas personalizadas.                                                                                                                                                                                                                      |
| 268435456  | 0x10000000 | UNIT_FLAG_UNK_28                        | (PreventKneelingWhenLooting de UnitFlags.cs en WPP)                                                                                                                                                                                                                                                                      |
| 536870912  | 0x20000000 | UNIT_FLAG_PREVENT_EMOTES_FROM_CHAT_TEXT | Evitar que los gestos que se reproducen automáticamente analicen el texto del chat, por ejemplo, "lol" en /say, finalizar el mensaje con ? o !, o usar /yell                                                                                                                                                             |
| 1073741824 | 0x40000000 | UNIT_FLAG_SHEATHE                       |                                                                                                                                                                                                                                                                                                                          |
| 2147483648 | 0x80000000 | UNIT_FLAG_IMMUNE                        | Inmune al daño                                                                                                                                                                                                                                                                                                           |

#### unit_flags2

Permite la aplicación adicional de indicadores de unidad a las criaturas. Se trata de un campo de máscara de bits, por lo que para aplicar más de un indicador, basta con sumar los diferentes números. Algunos indicadores posibles son:


| Bandera |            | Nombre                                  | Comentarios                                                                                         |
| ------- | ---------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 1      | 0x00000001 | UNIT_FLAG2_FEIGN_DEATH                |                                                                                                        |
| 2      | 0x00000002 | UNIT_FLAG2_HIDE_BODY                  | Ocultar el modelo de la unidad (mostrar solo el equipo del jugador)                                    |
| 4      | 0x00000004 | UNIT_FLAG2_IGNORE_REPUTATION          |                                                                                                        |
| 8      | 0x00000008 | UNIT_FLAG2_COMPREHEND_LANG            |                                                                                                        |
| 16     | 0x00000010 | UNIT_FLAG2_MIRROR_IMAGE               |                                                                                                        |
| 32     | 0x00000020 | UNIT_FLAG2_DO_NOT_FADE_IN             | El modelo de unidad aparece instantáneamente cuando se lo invoca (no se desvanece)                     |
| 64     | 0x00000040 | UNIT_FLAG2_FORCE_MOVEMENT             |                                                                                                        |
| 128    | 0x00000080 | UNIT_FLAG2_DISARM_OFFHAND             |                                                                                                        |
| 256    | 0x00000100 | UNIT_FLAG2_DISABLE_PRED_STATS         | El jugador ha desactivado las estadísticas predichas (usadas por los marcos de incursión)              |
| 1024   | 0x00000400 | UNIT_FLAG2_DISARM_RANGED              | Esto no deshabilita la visualización de armas a distancia (¿quizás se necesite una bandera adicional?) |
| 2048   | 0x00000800 | UNIT_FLAG2_REGENERATE_POWER           |                                                                                                        |
| 4096   | 0x00001000 | UNIT_FLAG2_RESTRICT_PARTY_INTERACTION | Restringir la interacción al grupo o a la incursión                                                    |
| 8192   | 0x00002000 | UNIT_FLAG2_PREVENT_SPELL_CLICK        | Prevenir clics ortográficos                                                                            |
| 16384  | 0x00004000 | UNIT_FLAG2_ALLOW_ENEMY_INTERACT       |                                                                                                        |
| 32768  | 0x00008000 | UNIT_FLAG2_CANNOT_TURN                |                                                                                                        |
| 65536  | 0x00010000 | UNIT_FLAG2_UNK2                       |                                                                                                        |
| 131072 | 0x00020000 | UNIT_FLAG2_PLAY_DEATH_ANIM            | Reproduce una animación de muerte especial al morir.                                                   |
| 262144 | 0x00040000 | UNIT_FLAG2_ALLOW_CHEAT_SPELLS         | Permite lanzar hechizos con AttributesEx7 y SPELL_ATTR7_IS_CHEAT_SPELL                                 |

#### dynamicflags

Banderas que controlan la apariencia visual de la criatura.

Algunas banderas conocidas y su uso son:


| Bandera |      | Nombre                                   | Comentarios                                                                                                           |
| ---- | ---- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 0    | 0x00 | UNIT_DYNFLAG_NONE                      |                                                                                                                            |
| 1    | 0x01 | UNIT_DYNFLAG_LOOTABLE                  |                                                                                                                            |
| 2    | 0x02 | UNIT_DYNFLAG_TRACK_UNIT                | La ubicación de la criatura se verá como un pequeño punto en el minimapa.                                                  |
| 4    | 0x04 | UNIT_DYNFLAG_TAPPED                    | Hace que el nombre de las criaturas aparezca en gris (Lua_UnitIsTapped)                                                    |
| 8    | 0x08 | UNIT_DYNFLAG_TAPPED_BY_PLAYER          | Lua_UnitIsTappedByPlayer generalmente utilizado por los PCV (vehículos controlados por el jugador)                         |
| 16   | 0x10 | UNIT_DYNFLAG_SPECIALINFO               |                                                                                                                            |
| 32   | 0x20 | UNIT_DYNFLAG_DEAD                      | Hace que la criatura parezca muerta (ESTO NO hace que el nombre de la criatura sea gris ni que no ataque a los jugadores). |
| 64   | 0x40 | UNIT_DYNFLAG_REFER_A_FRIEND            |                                                                                                                            |
| 128  | 0x80 | UNIT_DYNFLAG_TAPPED_BY_ALL_THREAT_LIST | Lua_UnitIsTappedByAllThreatList                                                                                            |

#### family

The family this creature belongs to.

| ID  | Familia          | ID  | Familia              |
| --- | ---------------- | --- | --------------       |
| 1.  | Lobo             | 26. | Búho                 |
| 2.  | Gato             | 27. | Serpiente del viento |
| 3.  | Araña            | 28. | Mando a distancia    |
| 4.  | Oso              | 29. | Felguard             |
| 5.  | Verraco          | 30. | Dragonhawk           |
| 6.  | Crocolisco       | 31. | Ravager              |
| 7.  | Pájaro carroñero | 32. | Warp Stalker         |
| 8.  | Cangrejo         | 33. | Sporebat             |
| 9.  | Gorila           | 34. | Nether Ray           |
| 11. | Rapaz            | 35. | Serpiente            |
| 12. | Tallstrider      | 37. | Polilla              |
| 15. | Felhunter        | 38. | Quimera              |
| 16. | Voidwalker       | 39. | Devilsaur            |
| 17. | Succubus         | 40. | Demonio necrófago    |
| 19. | Doomguard        | 41. | Silithid             |
| 20. | Escorpión        | 42. | Gusano               |
| 21. | Tortuga          | 43. | Rinoceronte          |
| 23. | Diablillo        | 44. | Avispa               |
| 24. | Murciélago       | 45. | Core Hound           |
| 25. | Hiena            | 46. | Bestia espiritual    |

#### trainer_type

Si el PNJ es entrenador (tiene la bandera de entrenador), este campo indica qué tipo de entrenador es. Tanto este campo como el campo relacionado deben completarse para que un entrenador funcione correctamente.

| ID  | Tipo                     | Campo relacionado               | Comentarios                             |
| --- | ------------------------ | ------------------------------- | --------------------------------------- |
| 0   | TRAINER_TYPE_CLASS       | [trainer_class](#trainer_class) | Hechizos de clase de trenes             |
| 1   | TRAINER_TYPE_MOUNTS      | [trainer_race](#trainer_race)   | Habilidad para conducir trenes          |
| 2   | TRAINER_TYPE_TRADESKILLS | [trainer_spell](#trainer_spell) | Profesiones de trenes                   |
| 3   | TRAINER_TYPE_PETS        | [trainer_class](#trainer_class) | Entrena las habilidades de las mascotas |

#### trainer_spell

Si el NPC es un entrenador que enseña profesiones ([trainer_type](#trainer_type) = 2), entonces el jugador ya debe saber el ID del hechizo especificado aquí para poder hablar con este NPC.

#### trainer_class

Si el NPC es un entrenador de clase o de mascotas ([trainer_type](#trainer_type) = 0 o 3), la clase del jugador debe ser la misma que el valor especificado aquí para hablar con este entrenador. Para los entrenadores de mascotas, este valor debe ser 3 (cazador). Consulta [characters.class](characters#class)

#### trainer_race

Si el NPC es un entrenador de monturas ([trainer_type](#trainer_type) = 1), entonces la raza del jugador debe ser la misma que el valor especificado aquí para hablar con este entrenador. Ver [characters.race](characters#race)

#### type

El tipo de criatura.

| ID  | Tipo                   |
| --- | ---------------------- |
| 0   | Ninguno                |
| 1   | Bestia                 |
| 2   | Dragonkin              |
| 3   | Demonio                |
| 4   | Elemental              |
| 5   | Gigante                |
| 6   | No muertos             |
| 7   | Humanoide              |
| 8   | Bicho                  |
| 9   | Mecánico               |
| 10  | No especificado        |
| 11  | Tótem                  |
| 12  | Mascota que no combate |
| 13  | Nube de gas            |

#### type_flags

Este campo controla si un monstruo se puede minar, herborizar o saquear por un ingeniero. Si es cualquiera de estos tres, el botín obtenido al desollarlo o minarlo se almacenará en la tabla [skinning_loot_template](loot_template). También controla si un cazador puede domarlo. Los demás campos no tienen un significado especial en el servidor. El campo completo se enviará al cliente en SMSG_CREATURE_QUERY_RESPONSE.

| Bandera    |            | Nombre                                               | Comentarios                                                                                                               |
| ---------- | ---------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 1          | 0x00000001 | CREATURE_TYPE_FLAG_TAMEABLE                          | Hace que la mafia sea domesticable (también debe ser una bestia y tener un conjunto familiar)                             |
| 2          | 0x00000002 | CREATURE_TYPE_FLAG_VISIBLE_TO_GHOSTS                 | Las criaturas también son visibles para jugadores no vivos. ¿Se permite la interacción con chismes si npcflag lo permite? |
| 4          | 0x00000004 | CREATURE_TYPE_FLAG_BOSS_MOB                          | Cambia el nivel visible de la criatura a "??" en el retrato de la criatura - Inmune al retroceso.                         |
| 8          | 0x00000008 | CREATURE_TYPE_FLAG_DO_NOT_PLAY_WOUND_PARRY_ANIMATION | No reproduce la animación de herida al parar.                                                                             |
| 16         | 0x00000010 | CREATURE_TYPE_FLAG_NO_FACTION_TOOLTIP                | Oculta la información sobre herramientas de la facción.                                                                   |
| 32         | 0x00000020 | CREATURE_TYPE_FLAG_MORE_AUDIBLE                      |                                                                                                                           |
| 64         | 0x00000040 | CREATURE_TYPE_FLAG_SPELL_ATTACKABLE                  | Hechizo atacable.                                                                                                         |
| 128        | 0x00000080 | CREATURE_TYPE_FLAG_INTERACT_WHILE_DEAD               | El jugador puede interactuar con la criatura si está muerta (no si el jugador está muerto)                                |
| 256        | 0x00000100 | CREATURE_TYPE_FLAG_SKIN_WITH_HERBALISM               | Hace que la turba sea herbácea                                                                                            |
| 512        | 0x00000200 | CREATURE_TYPE_FLAG_SKIN_WITH_MINING                  | Hace que la mafia sea minable                                                                                             |
| 1024       | 0x00000400 | CREATURE_TYPE_FLAG_NO_DEATH_MESSAGE                  | No combate la muerte.                                                                                                     |
| 2048       | 0x00000800 | CREATURE_TYPE_FLAG_ALLOW_MOUNTED_COMBAT              | La criatura puede permanecer montada al entrar en combate.                                                                |
| 4096       | 0x00001000 | CREATURE_TYPE_FLAG_CAN_ASSIST                        | ¿Puede ayudar a cualquier jugador en combate si está dentro del alcance?                                                  |
| 8192       | 0x00002000 | CREATURE_TYPE_FLAG_NO_PET_BAR                        | Esta usando barra para mascotas.                                                                                          |
| 16384      | 0x00004000 | CREATURE_TYPE_FLAG_MASK_UID                          |                                                                                                                           |
| 32768      | 0x00008000 | CREATURE_TYPE_FLAG_SKIN_WITH_ENGINEERING             | Hace que la mafia sea saqueable por el ingeniero                                                                          |
| 65536      | 0x00010000 | CREATURE_TYPE_FLAG_TAMEABLE_EXOTIC                   | Se puede domesticar como mascota exótica. También se debe establecer la bandera de domesticación normal.                  |
| 131072     | 0x00020000 | CREATURE_TYPE_FLAG_USE_MODEL_COLLISION_SIZE          | Relacionado con colisiones. (¿siempre usando el cuadro de colisión predeterminado?)                                       |
| 262144     | 0x00040000 | CREATURE_TYPE_FLAG_ALLOW_INTERACTION_WHILE_IN_COMBAT | Es un arma de asedio.                                                                                                     |
| 524288     | 0x00080000 | CREATURE_TYPE_FLAG_COLLIDE_WITH_MISSILES             | Los proyectiles pueden colisionar con esta criatura: interactúa con TARGET_DEST_TRAJ                                      |
| 1048576    | 0x00100000 | CREATURE_TYPE_FLAG_NO_NAME_PLATE                     | Oculta la placa de identificación.                                                                                        |
| 2097152    | 0x00200000 | CREATURE_TYPE_FLAG_DO_NOT_PLAY_MOUNTED_ANIMATIONS    | No reproduce animaciones montadas.                                                                                        |
| 4194304    | 0x00400000 | CREATURE_TYPE_FLAG_IS_LINK_ALL                       |                                                                                                                           |
| 8388608    | 0x00800000 | CREATURE_TYPE_FLAG_INTERACT_ONLY_WITH_CREATOR        | Sólo puede interactuar con su creador.                                                                                    |
| 16777216   | 0x01000000 | CREATURE_TYPE_FLAG_DO_NOT_PLAY_UNIT_EVENT_SOUNDS     |                                                                                                                           |
| 33554432   | 0x02000000 | CREATURE_TYPE_FLAG_HAS_NO_SHADOW_BLOB                |                                                                                                                           |
| 67108864   | 0x04000000 | CREATURE_TYPE_FLAG_TREAT_AS_RAID_UNIT                | La criatura puede ser el objetivo de hechizos que requieren que el objetivo esté en el grupo/banda del lanzador.          |
| 134217728  | 0x08000000 | CREATURE_TYPE_FLAG_FORCE_GOSSIP                      | Permite que la criatura muestre una única opción de chisme.                                                               |
| 268435456  | 0x10000000 | CREATURE_TYPE_FLAG_DO_NOT_SHEATHE                    |                                                                                                                           |
| 536870912  | 0x20000000 | CREATURE_TYPE_FLAG_DO_NOT_TARGET_ON_INTERACTION      |                                                                                                                           |
| 1073741824 | 0x40000000 | CREATURE_TYPE_FLAG_DO_NOT_RENDER_OBJECT_NAME         |                                                                                                                           |
| 2147483648 | 0x80000000 | CREATURE_TYPE_FLAG_UNIT_IS_QUEST_BOSS                |                                                                                                                           |

#### lootid

El ID de la plantilla de botín que esta criatura debe usar para generar botín. Ver [creature_loot_template.entry](loot_template#loot_template-entry)

#### pickpocketloot

El ID de la plantilla de botín de carterismo que esta criatura debe usar para generar botín de carterismo. Ver [pickpocketing_loot_template.entry](loot_template#loot_template-entry)

#### skinloot

El ID de la plantilla de botín de desuello que esta criatura debe usar para generar botín de desuello. Ver [skinning_loot_template.entry](loot_template#loot_template-entry)

#### PetSpellDataId

ID, que se encuentra en CreatureSpellData.dbc, que muestra qué hechizos tiene la mascota en el cliente.

#### VehicleId

Entrada de vehículo si la criatura es/tiene una entrada de vehículo. Este campo determina cómo aparece el jugador en el vehículo, cómo se mueve el vehículo y si se muestra o no la barra de acción del vehículo. Por ejemplo, un vehicleID de 292 hará al jugador invisible, evitará que el vehículo se desplace a la izquierda/derecha (pero permitirá hacia adelante/atrás) y mostrará los hechizos de la barra de acción del vehículo (que se definen en [spell1-8](http://trinitycore.atlassian.net#spell)). Se debe crear una entrada npc_spellclick_spells para esta entrada de criatura para que esto funcione.

#### mingold

Dinero mínimo que la criatura deja caer al morir, en cobre.

#### maxgold

Dinero máximo que la criatura suelta al morir, en cobre.

#### AIName

Este campo es reemplazado por el campo ScriptName si ambos están configurados.

| Nombre         | Descripción                                                                                                      |
| -------------- | ---------------------------------------------------------------------------------------------------------------- |
| NullCreatureAI | IA vacía, la criatura no hace nada; no puede ser encantada.                                                      |
| TriggerAI      | Igual que "NullCreatureAI", excepto que la criatura lanza el hechizo desde el campo hechizo1 cuando es invocada. |
| AggressorAI    | La criatura ataca cuando entra en el radio de agresión; utiliza solo ataques cuerpo a cuerpo.                    |
| ReactorAI      | La criatura ataca solo si se le ataca; utiliza solo ataques cuerpo a cuerpo.                                     |
| PassiveAI      | La criatura se comporta pasivamente, no puede atacar.                                                            |
| CritterAI      | Criatura que huye si es atacada.                                                                                 |
| GuardAI        | La criatura es un guardia de zona.                                                                               |
| PetAI          | La criatura es una mascota.                                                                                      |
| TotemAI        | La criatura lanza un hechizo desde el campo hechizo1; no se mueve.                                               |
| CombatAI       | La criatura ataca tan pronto como algo está dentro del alcance de agresión; también usa hechizos.                |
| ArcherAI       | La criatura lanza un hechizo desde el campo hechizo1; persigue a la víctima.                                     |
| TurretAI       | La criatura ataca usando un hechizo del Campo hechizo1; no se mueve.                                             |
| VehicleAI      | La criatura actúa como vehículo del jugador.                                                                     |
| SmartAI        | La criatura usa la tabla "[smart_scripts](smart_scripts)" para especificar su comportamiento.                    |

#### MovementType

El tipo de movimiento predeterminado de la criatura.

| ID  | Tipo                                                     |
| --- | -------------------------------------------------------- |
| 0   | Ocioso; permanecer en un lugar                           |
| 1   | Movimiento aleatorio dentro del radio de wander_distance |
| 2   | Movimiento de puntos de referencia                       |

#### HoverHeight

Distancia sobre el suelo a la que se mantendrá la criatura si tiene activada la función MOVEMENTFLAG_DISABLE_GRAVITY. Valor obtenido de los olfateos.

#### HealthModifier

Se utiliza para modificar la salud base de nivel/clase de una criatura. Este campo proviene de WDB.

#### ManaModifier

Se utiliza para modificar el maná base de nivel/clase de una criatura. Este campo proviene de WDB.

#### ArmorModifier

Se utiliza para modificar la armadura base de nivel/clase de una criatura.

#### DamageModifier

Se utiliza para modificar el daño mínimo/máximo de una criatura.

Las fórmulas para calcular el daño producido son:

MINDAMAGE = ((([damage_base](creature_classlevelstats#damage_base) + ([attackpower](creature_classlevelstats#attackpower) / 14) * [BaseVariance](#basevariance)) * DamageModifier) * ([BaseAttackTime](#baseattacktime) / 1000))  
MAXDAMAGE = (((([damage_base](creature_classlevelstats#damage_base) * 1.5) + ([attackpower](creature_classlevelstats#attackpower) / 14) * [BaseVariance](creature_template#basevariance)) * DamageModifier) * ([BaseAttackTime](#baseattacktime) / 1000))

damage_base proviene de la tabla creature_classlevelstats y toma su valor de [damage_base](creature_classlevelstats#damage_base), [damage_exp1](creature_classlevelstats#damage_exp1) o [damage_exp2](creature_classlevelstats#damage_exp2) de acuerdo al valor de la criatura en [exp](#exp) (0 = base_damage, 1 = damage_exp1, 2 = damage_exp2).

BaseAttackTime es [BaseAttackTime](#baseattacktime) o [RangeAttackTime](#rangeattacktime) dependiendo del tipo de ataque.

El poder de ataque es [attackpower](creature_classlevelstats#attackpower) o [rangedattackpower](creature_classlevelstats#rangedattackpower) dependiendo del tipo de ataque.

BaseVariance es [BaseVariance](#basevariance) o [RangeVariance](#rangevariance) dependiendo del tipo de ataque.


#### ExperienceModifier

¡HACER!

#### RacialLeader

Una bandera con dos valores posibles: '1' o '0', que indica si la criatura es un líder racial o no. Matar líderes raciales otorga 100 puntos de honor.

| Entrada | Nombre                   |
| ------- | ------------------------ |
| 2784    | King Magni Bronzebeard   |
| 3057    | Cairne Bloodhoof         |
| 4949    | Thrall                   |
| 7999    | Tyrande Whisperwind      |
| 10181   | Lady Sylvanas Windrunner |
| 16802   | Lor'themar Theron        |
| 17468   | Prophet Velen            |
| 29611   | King Varian Wrynn        |
| 36648   | Baine Bloodhoof (Leader) |
| 37764   | Lor'themar Theron        |

#### movementId

No tenemos idea de qué hace este campo. Se pasa directamente al cliente.

#### RegenHealth

Booleano '1' o '0' que controla si la criatura debe regenerar su salud o no.

#### mechanic_immune_mask

Esto hace que la criatura sea inmune a hechizos de naturaleza específica. Consulta Spell.dbc en la fila effect_X_mechanic_id.

Utiliza referencias de SpellMechanic.dbc.

| Bandera    |            | Tipo                     | Comentario                                                           |
| ---------- | ---------- | ------------------------ | -------------------------------------------------------------------- |
| 1          | 0x00000001 | MECHANIC_CHARM           |                                                                      |
| 2          | 0x00000002 | MECHANIC_DISORIENTED     |                                                                      |
| 4          | 0x00000004 | MECHANIC_DISARM          |                                                                      |
| 8          | 0x00000008 | MECHANIC_DISTRACT        |                                                                      |
| 16         | 0x00000010 | MECHANIC_FEAR            |                                                                      |
| 32         | 0x00000020 | MECHANIC_GRIP            | Death Grip y efectos similares                                       |
| 64         | 0x00000040 | MECHANIC_ROOT            |                                                                      |
| 128        | 0x00000080 | MECHANIC_SLOW_ATTACK     |                                                                      |
| 256        | 0x00000100 | MECHANIC_SILENCE         |                                                                      |
| 512        | 0x00000200 | MECHANIC_SLEEP           |                                                                      |
| 1024       | 0x00000400 | MECHANIC_SNARE           |                                                                      |
| 2048       | 0x00000800 | MECHANIC_STUN            |                                                                      |
| 4096       | 0x00001000 | MECHANIC_FREEZE          |                                                                      |
| 8192       | 0x00002000 | MECHANIC_KNOCKOUT        | Efectos incapacitantes como Repetición (Paladín)                     |
| 16384      | 0x00004000 | MECHANIC_BLEED           |                                                                      |
| 32768      | 0x00008000 | MECHANIC_BANDAGE         | Curación, etc.                                                       |
| 65536      | 0x00010000 | MECHANIC_POLYMORPH       |                                                                      |
| 131072     | 0x00020000 | MECHANIC_BANISH          |                                                                      |
| 262144     | 0x00040000 | MECHANIC_SHIELD          |                                                                      |
| 524288     | 0x00080000 | MECHANIC_SHACKLE         | Solo grilletes no muertos                                            |
| 1048576    | 0x00100000 | MECHANIC_MOUNT           | Cualquier efecto que invoque una montura                             |
| 2097152    | 0x00200000 | MECHANIC_INFECTED        | Fiebre de escarcha, plaga de sangre, etc.                            |
| 4194304    | 0x00400000 | MECHANIC_TURN            | p. ej. Volverse malvado                                              |
| 8388608    | 0x00800000 | MECHANIC_HORROR          | p. ej. Death Coil (Brujo)                                            |
| 16777216   | 0x01000000 | MECHANIC_INVULNERABILITY | Tolerancia, Protección del Nether, Inmunidad Diplomática únicamente  |
| 33554432   | 0x02000000 | MECHANIC_INTERRUPT       |                                                                      |
| 67108864   | 0x04000000 | MECHANIC_DAZE            |                                                                      |
| 134217728  | 0x08000000 | MECHANIC_DISCOVERY       | Cualquier efecto de Crear elemento                                   |
| 268435456  | 0x10000000 | MECHANIC_IMMUNE_SHIELD   | Escudo Divino, Bloque de Hielo, Mano de Protección...                |
| 536870912  | 0x20000000 | MECHANIC_SAPPED          |                                                                      |
| 1073741824 | 0x40000000 | MECHANIC_ENRAGED         |                                                                      |

Para combinar inmunidades, basta con sumar valores. Inmune a todo corresponde al valor 2147483647 (0x3FFF FFFF).

#### spell_school_immune_mask 

Esto hace que la criatura sea inmune a escuelas de hechizos específicas.

| Bandera | Tipo                |
| ------- | ------------------- |
| 1       | SPELL_SCHOOL_NORMAL |
| 2       | SPELL_SCHOOL_HOLY   |
| 4       | SPELL_SCHOOL_FIRE   |
| 8       | SPELL_SCHOOL_NATURE |
| 16      | SPELL_SCHOOL_FROST  |
| 32      | SPELL_SCHOOL_SHADOW |
| 64      | SPELL_SCHOOL_ARCANE |

Para combinar inmunidades, simplemente suma valores. Inmune a todo corresponde al valor 127.

#### flags_extra

Estas banderas controlan ciertos atributos específicos de las criaturas. Se pueden combinar para aplicar más de una.

**Ejemplo:** 32+64=96

| Bandera    | Tipo                                                |            |                                                                                                                                                                                       |
| ---------- | --------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1          | CREATURE_FLAG_EXTRA_INSTANCE_BIND                   | 0x00000001 | La criatura asesina vincula la instancia al asesino y al grupo del asesino.                                                                                                           |
| 2          | CREATURE_FLAG_EXTRA_CIVILIAN                        | 0x00000002 | La criatura no genera agresión (ignora la hostilidad de facción/reputación).                                                                                                          |
| 4          | CREATURE_FLAG_EXTRA_NO_PARRY                        | 0x00000004 | La criatura no para                                                                                                                                                                   |
| 8          | CREATURE_FLAG_EXTRA_NO_PARRY_HASTEN                 | 0x00000008 | La criatura no contraataca al parar                                                                                                                                                   |
| 16         | CREATURE_FLAG_EXTRA_NO_BLOCK                        | 0x00000010 | La criatura no bloquea                                                                                                                                                                |
| 32         | CREATURE_FLAG_EXTRA_NO_CRUSHING_BLOWS               | 0x00000020 | La criatura no realiza ataques de aplastamiento.                                                                                                                                      |
| 64         | CREATURE_FLAG_EXTRA_NO_XP                           | 0x00000040 | Matar criaturas no otorga XP                                                                                                                                                          |
| 128        | CREATURE_FLAG_EXTRA_TRIGGER                         | 0x00000080 | La criatura es un NPC activador (invisible solo para los jugadores)                                                                                                                   |
| 256        | CREATURE_FLAG_EXTRA_NO_TAUNT                        | 0x00000100 | La criatura es inmune a las auras de provocación y a los efectos de "atacame".                                                                                                        |
| 512        | CREATURE_FLAG_EXTRA_NO_MOVE_FLAGS_UPDATE            | 0x00000200 | (CREATURE_FLAG_EXTRA_UNUSED_10 No implementado) la criatura no actualizará las banderas de movimiento                                                                                 |
| 1024       | CREATURE_FLAG_EXTRA_GHOST_VISIBILITY                | 0x00000400 | La criatura solo será visible para los jugadores muertos.                                                                                                                             |
| 2048       | CREATURE_FLAG_EXTRA_USE_OFFHAND_ATTACK              | 0x00000800 | La criatura usará ataques con la mano izquierda                                                                                                                                       |
| 4096       | CREATURE_FLAG_EXTRA_NO_SELL_VENDOR                  | 0x00001000 | Los jugadores no pueden vender artículos a este vendedor.                                                                                                                             |
| 8192       | CREATURE_FLAG_EXTRA_IGNORE_COMBAT                   | 0x00002000 |                                                                                                                                                                                       |
| 16384      | CREATURE_FLAG_EXTRA_WORLDEVENT                      | 0x00004000 | Bandera personalizada para eventos mundiales (deja espacio para fusionar)                                                                                                             |
| 32768      | CREATURE_FLAG_EXTRA_GUARD                           | 0x00008000 | La criatura es un guardia (Ignorará fingir muerte y desaparecerá)                                                                                                                     |
| 65536      | CREATURE_FLAG_EXTRA_IGNORE_FEIGN_DEATH              | 0x00010000 | La criatura ignora la muerte fingida                                                                                                                                                  |
| 131072     | CREATURE_FLAG_EXTRA_NO_CRIT                         | 0x00020000 | La criatura no realiza golpes críticos.                                                                                                                                               |
| 262144     | CREATURE_FLAG_EXTRA_NO_SKILL_GAINS                  | 0x00040000 | La criatura no aumentará las habilidades con las armas.                                                                                                                               |
| 524288     | CREATURE_FLAG_EXTRA_OBEYS_TAUNT_DIMINISHING_RETURNS | 0x00080000 | La burla de las criaturas está sujeta a rendimientos decrecientes.                                                                                                                    |
| 1048576    | CREATURE_FLAG_EXTRA_ALL_DIMINISH                    | 0x00100000 | La criatura está sujeta a todos los rendimientos decrecientes.                                                                                                                        |
| 2097152    | CREATURE_FLAG_EXTRA_NO_PLAYER_DAMAGE_REQ            | 0x00200000 | La criatura no necesita recibir daño del jugador para obtener crédito por la muerte.                                                                                                  |
| 4194304    | CREATURE_FLAG_EXTRA_AVOID_AOE                       | 0x00400000 | Ignorado por ataques de área de efecto (para el NPC del Consejo del Príncipe Sangriento de la ICC - Núcleo Oscuro)                                                                    |
| 8388608    | CREATURE_FLAG_EXTRA_NO_DODGE                        | 0x00800000 | El objetivo no puede esquivar                                                                                                                                                         |
| 16777216   | CREATURE_FLAG_EXTRA_MODULE                          | 0x01000000 | Utilizado por criaturas modulares para evitar controles tipo ventisca.                                                                                                                |
| 33554432   | CREATURE_FLAG_EXTRA_DONT_CALL_ASSISTANCE            | 0x02000000 | Evita que las criaturas pidan ayuda en el agresor inicial.                                                                                                                            |
| 67108864   | CREATURE_FLAG_EXTRA_IGNORE_ALL_ASSISTANCE_CALLS     | 0x04000000 | Prevents creature from responding to assistance calls                                                                                                                                 |
| 134217728  | CREATURE_FLAG_EXTRA_DONT_OVERRIDE_SAI_ENTRY         | 0x08000000 | Permite que las criaturas utilicen SAI específicos de GUID y ENTRY sin que uno sobrescriba al otro                                                                                    |
| 268435456  | CREATURE_FLAG_EXTRA_DUNGEON_BOSS                    | 0x10000000 | La criatura es un jefe de mazmorra. Esta bandera la establece el núcleo de forma genérica durante la ejecución. Si se configura en la base de datos, se generará un error de inicio.  |
| 536870912  | CREATURE_FLAG_EXTRA_IGNORE_PATHFINDING              | 0x20000000 | La criatura ignorará la búsqueda de rutas. Esto es como deshabilitar los mapas M, pero para una sola criatura.                                                                        |
| 1073741824 | CREATURE_FLAG_EXTRA_IMMUNITY_KNOCKBACK              | 0x40000000 | La criatura será inmune a todos los efectos de retroceso.                                                                                                                             |
| 2147483648 | CREATURE_FLAG_EXTRA_HARD_RESET                      | 0x80000000 | La criatura desaparecerá al evadir.                                                                                                                                                   |

#### ScriptName

El nombre del script que usa esta criatura, si lo hay. Esto vincula un script de un motor de scripts a esta criatura.

#### VerifiedBuild

Este campo se utilizó para determinar si una plantilla ha sido verificada a partir de archivos WDB.

Si el valor es 0, entonces aún no se ha analizado.

Si el valor es superior a 0, se ha analizado con archivos WDB de esa compilación de cliente específica.

Si el valor es -1, entonces es solo un marcador de posición hasta que se encuentren los datos adecuados en las WDB.

Si el valor es -Compilación del cliente entonces se analizó con archivos WDB de esa [compilación del cliente](http://archive.trinitycore.info/DB:Auth:realmlist#gamebuild "DB:Auth:realmlist") específica y luego se editó manualmente para satisfacer alguna necesidad especial.

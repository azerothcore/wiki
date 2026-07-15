# Introducción a SmartAI

## Índice
- [Parte I: Scriptear una patrulla scripteada simple](#part-i-scripting-a-simple-scripted-patrol)
- [Parte II: Event Phases y Links](#part-ii-event-phases-and-links)
- [Parte III: Conditions, IA única y Data Set](#part-iii-conditions-unique-ai-and-data-set)

---

## Parte I: Scriptear una patrulla scripteada simple

Para esto scriptearemos un RP de patrulla simple, un script que se ejecuta de vez en cuando con un temporizador e implica una ruta.

Al hacer scripts blizzlike, la mayoría de estos datos se pueden recopilar en sniffs. Usando herramientas como un parser, WDBE o WaypointCreator podemos extraer waypoints, y luego scriptear qué acciones se van a realizar.

En un archivo parseado, puedes buscar el GUID único de la creature, y ver qué acciones se realizan. Por ejemplo, NPCFlag, UnitFlag, StandState, EmoteState y los Oneshot Emotes se pueden encontrar todos en el archivo parseado. Algunas acciones acabarán estando ocultas, pero entonces podemos ser creativos o incluso investigar más a fondo. En el Templo Oscuro, por ejemplo, hay creatures que ejecutan un Eat Emote lanzando un hechizo serverside, pero eso no es común.

El evento que vamos a implementar contiene solo StandStates y líneas habladas.

Primero detallamos qué ocurrirá y cuándo:

```sql
UPDATE `creature` SET `MovementType` = 2 WHERE `id1` = 23600 AND `guid` = 18604;

DELETE FROM `creature_addon` WHERE (`guid` IN (18604));
INSERT INTO `creature_addon` (`guid`, `path_id`, `mount`, `bytes1`, `bytes2`, `emote`, `visibilityDistanceType`, `auras`) VALUES
(18604, 186040, 0, 0, 1, 0, 0, NULL);

DELETE FROM `waypoint_data` WHERE `id` = 186040;
INSERT INTO `waypoint_data` (`id`, `point`, `position_x`, `position_y`, `position_z`, `orientation`, `delay`) VALUES
(186040, 1, -4044.12, -3393.59, 38.1363, NULL, 6000), -- 1s, Talk 0, 5s, Talk 1
(186040, 2, -4044.21, -3394.23, 38.3905, NULL, 0),
(186040, 3, -4042.96, -3396.48, 38.3905, NULL, 0),
(186040, 4, -4041.71, -3397.23, 38.3905, NULL, 0),
(186040, 5, -4040.8, -3396.88, 38.1447, NULL, 16000), -- 2s, Emote 16, 6s, Talk 2, 6s, Garion Talk 0
(186040, 6, -4043.67, -3395.27, 38.1634, NULL, 0),
(186040, 7, -4043.67, -3395.27, 38.1634, 3.87463, 240000);
```

Desglosándolo línea por línea:

```sql
UPDATE `creature` SET `MovementType` = 2 WHERE `id1` = 23600 AND `guid` = 18604;
```

No estamos colocando una nueva creature, solo añadiendo comportamiento a una existente, así que simplemente modificaremos su MovementType, que le indica que usará la ruta establecida en su entry de creature_addon.

```sql
DELETE FROM `creature_addon` WHERE (`guid` IN (18604));
INSERT INTO `creature_addon` (`guid`, `path_id`, `mount`, `bytes1`, `bytes2`, `emote`, `visibilityDistanceType`, `auras`) VALUES
(18604, 186040, 0, 0, 1, 0, 0, NULL);
```

Este es su entry de creature_addon. Las patrullas tienen, por convención, ids iguales a GUID*10. El valor más común para bytes2, también conocido como SheateState, es 1, que representa las armas cuerpo a cuerpo de la creature. Esto también contiene items relacionados con RP, como faroles, botellas y demás.

```sql
DELETE FROM `waypoint_data` WHERE `id` = 186040;
INSERT INTO `waypoint_data` (`id`, `point`, `position_x`, `position_y`, `position_z`, `orientation`, `delay`) VALUES
(186040, 1, -4044.12, -3393.59, 38.1363, NULL, 6000), -- 1s, Talk 0, 5s, Talk 1
(186040, 2, -4044.21, -3394.23, 38.3905, NULL, 0),
(186040, 3, -4042.96, -3396.48, 38.3905, NULL, 0),
(186040, 4, -4041.71, -3397.23, 38.3905, NULL, 0),
(186040, 5, -4040.8, -3396.88, 38.1447, NULL, 16000), -- 2s, Emote 16, 6s, Talk 2, 6s, Garion Talk 0
(186040, 6, -4043.67, -3395.27, 38.1634, NULL, 0),
(186040, 7, -4043.67, -3395.27, 38.1634, 3.87463, 180000);
```

Esta es la patrulla de waypoints a la que está asignada la creature. La he acortado para que no contenga columnas que no usaremos.

Los valores x,y,z se explican por sí solos. Un cambio de orientación requiere un punto extra copiado del anterior; de lo contrario es null. El delay dictará el tiempo de espera después de alcanzar ese waypoint, de modo que, después de que la creature termine la ruta en el punto 7, esperará 3 minutos antes de empezar la patrulla de nuevo.

También añadí unos pocos comentarios detallando qué acciones se realizan en qué waypoints. Es una versión simplificada de lo que escribiremos en la Actionlist.

Yo uso Keira para editar SmartAI, así que eso es lo que usaremos en este tutorial.

![Keira Editor](assets/images/sai_tutorial/sai_tutor_1.png)

Como estamos usando patrullas, usaremos un evento llamado WAYPOINT_REACHED. También podríamos usar MOVEMENTINFORM, especialmente útil cuando trabajamos con puntos individuales en lugar de rutas completas.

Keira generará entonces una salida que copiaremos y pegaremos.

```sql
UPDATE `creature_template` SET `AIName` = 'SmartAI' WHERE `entry` = 23600;
DELETE FROM `smart_scripts` WHERE (`source_type` = 0 AND `entryorguid` = 23600);
INSERT INTO `smart_scripts` (`entryorguid`, `source_type`, `id`, `link`, `event_type`, `event_phase_mask`, `event_chance`, `event_flags`, `event_param1`, `event_param2`, `event_param3`, `event_param4`, `event_param5`, `event_param6`, `action_type`, `action_param1`, `action_param2`, `action_param3`, `action_param4`, `action_param5`, `action_param6`, `target_type`, `target_param1`, `target_param2`, `target_param3`, `target_param4`, `target_x`, `target_y`, `target_z`, `target_o`, `comment`) VALUES
(23600, 0, 0, 0, 108, 0, 100, 0, 1, 0, 0, 0, 0, 0, 80, 2360000, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - On Point 1 of Path Any Reached - Run Script'),
(23600, 0, 1, 0, 108, 0, 100, 0, 5, 0, 0, 0, 0, 0, 80, 2360001, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - On Point 5 of Path Any Reached - Run Script');
```

Esto parece más simple que lo que describí en los comentarios. Esto es porque en realidad no realizamos las acciones aquí. Usaremos un mecanismo diferente de SmartAI, llamado Actionlists, o Script9, que es una secuencia de acciones realizadas con los temporizadores proporcionados. Así podemos hacer acciones retrasadas mucho más fácilmente. Los Script IDs de las Actionlists están, por convención, numerados CreatureEntry*100, añadiendo +1 a cada lista única. Como usaremos 2 conjuntos diferentes de acciones, usamos los IDs 2360000 y 2360001.

En los parámetros del evento, dejamos el parámetro pathId como 0, porque no esperamos ninguna patrulla aparte de la que añadimos, así que si no lo dejáramos como 0 sería una comprobación trivial que siempre devolvería true de todos modos, así que lo ignoraremos.

Para los parámetros de target lo dejaremos como 1, ya que la acción de llamar a las Actionlists no toma ningún target aparte de sí mismo.

Ahora abriremos el editor de Actionlist y haremos ambos scripts.

```sql
DELETE FROM `smart_scripts` WHERE (`source_type` = 9 AND `entryorguid` IN (2360000, 2360001));
INSERT INTO `smart_scripts` (`entryorguid`, `source_type`, `id`, `link`, `event_type`, `event_phase_mask`, `event_chance`, `event_flags`, `event_param1`, `event_param2`, `event_param3`, `event_param4`, `event_param5`, `event_param6`, `action_type`, `action_param1`, `action_param2`, `action_param3`, `action_param4`, `action_param5`, `action_param6`, `target_type`, `target_param1`, `target_param2`, `target_param3`, `target_param4`, `target_x`, `target_y`, `target_z`, `target_o`, `comment`) VALUES
(2360000, 9, 0, 0, 0, 0, 100, 0, 1000, 1000, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - Actionlist - Say Line 0'),
(2360000, 9, 1, 0, 0, 0, 100, 0, 5000, 5000, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - Actionlist - Say Line 1'),

(2360001, 9, 0, 0, 0, 0, 100, 0, 2000, 2000, 0, 0, 0, 0, 5, 16, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - Actionlist - Play Emote 16'),
(2360001, 9, 1, 0, 0, 0, 100, 0, 6000, 6000, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - Actionlist - Say Line 2'),
(2360001, 9, 2, 0, 0, 0, 100, 0, 6000, 6000, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 19, 23601, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - Actionlist - Say Line 0 (Apprentice Garion)');
```

Ahora aquí está la parte central del script. El primer script es simple, con solo acciones de habla.

El segundo script reproduce un emote, hace que Morlann, nuestra creature, hable, y luego hace que hable una creature *diferente*. Cuando usamos un target para la acción TALK, y dejamos el tercer parámetro como 0, podemos hacer que la(s) creature(s) objetivo hablen de forma remota sin hacer un script más complejo o pesado. El tercer parámetro, cuando se establece en 1 y con un target válido, hará por ejemplo que se dirija al target por su nombre o clase, como llamar al jugador por su nombre.

Así que esto es lo que ocurrirá:
1. La creature aparece y empieza la patrulla por primera vez
2. Cuando se alcanza un punto, disparará el evento, comprueba si el punto alcanzado es el 1 o el 5, y si es así, se reproduce la acción
3. La acción se realiza y a la creature se le asigna una Actionlist, que reproducirá una secuencia de acciones retrasadas
4. Una vez que la patrulla termina, esperará 3 minutos y luego reiniciará

## Parte II: Event Phases y Links

La mayoría de las creatures enemigas son bastante simples, siguiendo uno o dos temporizadores y lanzando un par de hechizos, lo cual es bastante fácil de hacer en unos minutos. El poder de SmartAI no viene de seguir simples temporizadores de hechizos. Para ilustrar un ejemplo, vamos a ver el script de algunas creatures de Terrallende que me parecen bastante interesantes. En Terrallende hay varias creatures Void, de las cuales los casters tienen una estructura de script particular que comparten entre ellos.

Al principio, solo lanzan Descarga de las Sombras y no tienen resistencias especiales. Sin embargo, una vez que el jugador les golpea con, por ejemplo, un Descarga de Escarcha, se lanzarán a sí mismos un hechizo de Reducción de daño: Escarcha, dirán una línea, y luego empezarán a lanzarle Descarga de Escarcha de vuelta al jugador. Así que, ¿cómo implementamos eso en SmartAI?

Un ejemplo listo que podemos usar es el Voidshrieker.

![Voidshrieker Script](assets/images/sai_tutorial/sai_tutor_2.png)

Ilegible, ¿verdad? Pero intentaré hacerlo más fácil de analizar. Pero primero necesitamos entender cómo funcionan las Event Phases.

Dicho de forma simple, las phases nos permiten, de una manera, dictar qué tipo de eventos se pueden reproducir, ya que a cada evento se le asigna una phase. La Phase 0 es la phase general. Cualquier cosa colocada en la Phase 0 se reproduce, independientemente de en qué phase esté actualmente la creature.

Configurar la Event Phase de la creature es una acción, y se resetea cuando la creature evade, muere o respawnea, así que es bueno resetear también la Event Phase a lo que queramos.

Mira el id 2 del script. En el Aggro la Event Phase se establecerá en 1, así que ¿qué eventos pertenecen al conjunto de la Event Phase 1? En resumen, todas las filas de la 3 a la 18, una gran parte del script.

![Event Phase Logic](assets/images/sai_tutorial/sai_tutor_3.png)

Estas. Después de que el Voidshrieker sea golpeado por un hechizo de las escuelas de arriba, reproducirá una secuencia de acciones, enlazadas entre sí con EVENT_LINK, y luego cambiará su propia phase. Ten en cuenta que la Event Phase 1 solo se establece en el Aggro, así que este comportamiento solo se puede reproducir UNA VEZ por combate. Si lo golpeo con un hechizo de fuego, el evento se reproducirá y cambiará de phase, así que si lo golpeo de nuevo con un hechizo de escarcha en su lugar, no lanzará `Reducción de daño: Escarcha` porque no está en la Phase 1, ahora está en la Phase 3.

Además, aunque no se muestra en este ejemplo, las Event Phases son una máscara, no un valor enum. Es decir, que podemos superponer event phases unas sobre otras. Si quisiéramos, podríamos hacer que el Voidshrieker acumulara resistencias y fuera capaz de lanzar todo el gradiente elemental de hechizos acumulando event phases en lugar de reemplazándolas.

P.D.: ¡El Event Flag 1 (No Repeat) se resetea una vez que el combate termina! Para nunca resetear y asegurar que la creature NUNCA JAMÁS vuelva a reproducir el evento, ¡usa el flag 256 (Don't Reset)!

Con estos eventos en mano, los usaremos para hacer que la creature lance diferentes hechizos dependiendo de en qué phase esté.

![Spell Cast Events](assets/images/sai_tutorial/sai_tutor_4.png)

Todos estos eventos de arriba están ligados a temporizadores, no a disparadores como On Spellhit. ¿Ves `Cast 'Shadow Bolt`? Ese está ligado a dos Event Phases, como en el ejemplo del diagrama de Venn que mencioné. Si el jugador no lanza un hechizo, o es un guerrero, por ejemplo, el Voidshrieker lanzará Descarga de las Sombras por defecto, además de lanzarlo si el jugador sí lanzó un hechizo de las Sombras. ¿Y Grito Psíquico? Ese está ligado a la Event Phase 0, lo que significa que sin importar en qué phase esté la creature actualmente, ejecutará el temporizador y realizará el evento.

Volviendo al diagrama de flujo, aún no expliqué bien cómo se enlazan estas acciones entre sí. En la Parte 1 introduje el concepto de Actionlists. Esto es similar.

Los Links nos permiten reproducir varias acciones en orden instantáneamente, así que no nos permitirán hacer delays. Para trabajar con esto, necesitas establecer el id del evento que se va a enlazar en el campo `link`.

[Linked Events](assets/images/sai_tutorial/sai_tutor_5.png)

Como puedes ver, el Evento 3 enlaza con el Evento 4, así que cuando se ejecuta el Evento 3, el Evento 4 también se ejecutará automáticamente. El evento que se enlaza necesita ser, necesariamente, del tipo de evento 61, EVENT_LINK.

Varios eventos pueden enlazar con el mismo evento. Por ejemplo, si una creature dice la misma línea después de lanzar varios hechizos diferentes, todos los hechizos pueden enlazarse a la misma acción Talk.

Si hacemos demasiados links, hacen que sea más difícil mantener el script, ya que cambiar una fila podría requerir cambiarlas todas. Para más de un link en una serie, a menudo me gusta usar Timed Actionlists en su lugar, usando el TimerType 2 para asegurar que también se reproduzca en combate. Esto hace más fácil encapsular mini-scripts dentro del script principal de la creature, sin hacer links espagueti.

## Parte III: Conditions, IA única y Data Set

En las Salas Destrozadas, hay una creature llamada Legionario de la Mano Destrozada.

Bueno, en realidad hay 8 de ellos. Y todos. tienen. IA. diferente.

Las mecánicas de combate y los hechizos que usan son comunes entre ellos. Todos Enfurecen, todos Aporrean a los casters, y todos lanzan Aura de Disciplina.

![Shattered Hand Legionnaire](assets/images/sai_tutorial/sai_tutor_6.png)

Pero veamos, por ejemplo, la IA del GUID 151010; para eso comprobamos su entry específica del guid. Ve al panel de SmartAI y busca por entidad como abajo.

![SmartAI Search Panel](assets/images/sai_tutorial/sai_tutor_7.png)

Verás varias filas, todas con ids numerados >1000, y con un comportamiento que es único de este GUID específico

![GUID Specific Scripts](assets/images/sai_tutorial/sai_tutor_8.png)

Las líneas 1001 a 1004 son scripts de RP. Céntrate en las de abajo. Por ejemplo, en el script general de la primera imagen, vemos que una vez que la creature recibe DATA SET -- una acción que nos permite comunicarnos entre creatures -- Enfurecerá. Cualquier otra creature de este dungeon, una vez que muere, tiene un script para hacer SET DATA en el Legionario más cercano, de modo que todos Enfurezcan. Pero si incluyes este script específico del guid, este Legionario en particular no solo Enfurecerá, sino que también dirá una línea especial e invocará una creature en una posición única. Luego usamos Event Phases para permitir que solo aparezca una creature a la vez.

Ahora, la parte importante es que normalmente estos scripts específicos del guid sobrescriben el script normal de la creature, haciendo que tengamos que copiarlo, creando mucho relleno. Pero por la época en que estábamos reescribiendo las Salas Destrozadas, un amigo mío añadió un flag extra a las creatures, que hará que carguen tanto su SmartAI general ligado a su entry, como el SmartAI ligado a su guid.

![Creature Template Flags](assets/images/sai_tutorial/sai_tutor_9.png)

Esto es extremadamente importante, ya que MUCHAS creatures tienen comportamientos únicos, así que para evitar cantidades enormes de filas inútiles, usamos este flag. Ten en cuenta que usamos ids 1000+ al hacer SAI específico del guid en estos casos, ¡porque los ids de fila no deben solaparse!

Ahora. Veamos estas invocaciones. ¿Cómo funcionan? Bueno, resulta que ¡cada una **también** tiene un comportamiento único! Porque varios legionarios las invocan en diferentes posiciones. Y cada una puede hacer algo diferente.

![Summon Scripts](assets/images/sai_tutorial/sai_tutor_10.png)

El problema es que las invocaciones no tienen guid para el que pudiéramos crear un script específico del guid.

El script de arriba es para las invocaciones; ten en cuenta que cuando están On Summoned, ejecutan varios scripts diferentes. ¿No se solaparán? Deberían, sí. Pero en este caso no lo hacen, porque usamos conditions.

Las conditions son herramientas muy potentes, y podemos ligarlas directamente a SmartAI, para todas y cada una de las filas.

![Conditions Panel](assets/images/sai_tutorial/sai_tutor_11.png)

¿Ves dónde el ConditionValue es 151010? Eso significa que en el SmartAI id 10 (11 - 1), ese evento solo se reproducirá cuando el Invoker (en este caso, el invocador) sea el Legionario del GUID 151010.

Deberías empezar a ver cuánto más potente puede ser SmartAI ahora. Cada fila individual se puede condicionar. Otro caso de estudio interesante es un objeto de quest que detecta cuánto ha progresado el jugador para poder realizar líneas e invocar creatures. En él, cada vez que el jugador interactúa se llama al script, pero solo prosigue cuando se cumplen las conditions. 

Los Invokers son algo que no todos los eventos tienen. Al usar el evento OOC_LOS, que comprueba si un jugador entra en la línea de visión de nuestra creature, el Invoker es el jugador que entró en la línea de visión, por ejemplo. Cuando haces Summon Creature, el Invoker es el invocador. Los Invokers también se pueden usar como un target_type. Cuando se ejecuta el evento On Quest Accepted, por ejemplo, podría ser bueno usar la Acción 64 (STORE_TARGET_LIST) para guardar al Invoker o incluso a todo el grupo del Invoker con el target_type 16.

Podrías preguntarte por qué se necesita entonces el SAI específico del guid si pudiéramos usar conditions. Es porque tendríamos que comprobar cada vez que se dispara el evento. Eso podría estar bien para una o dos creatures con IA específica del guid, pero en el Laberinto de las Sombras, tienes docenas. Tendrías desde docenas hasta un centenar de comprobaciones cada pocos segundos.

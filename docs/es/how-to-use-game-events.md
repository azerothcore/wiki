# Cómo usar los game events

Este es un ejemplo sencillo que demuestra cómo usar las tablas `game_event` y `game_event_creature` para disparar un evento repetitivo dentro del juego. Es un ejemplo simple, pero debería bastar para dar al lector una idea de lo que se necesita para empezar a usar eventos dentro del juego.

**Nota:** por favor, haz un backup de la base de datos antes de hacer cualquier cambio en ella, incluidos los de abajo. Esto es por si sobrescribes algo o haces cambios que rompan algo.

## Primeros pasos

A continuación hay algunos cambios SQL que se pueden hacer en la base de datos \`acore_world\` que harán que tres NPCs "Defias Cutpurse" aparezcan y desaparezcan cada dos (2) minutos en el Bosque de Elwynn. Esto está diseñado como un ejemplo simple y no representa una mejora del mundo del juego de ninguna manera.

Vamos a asumir que estás usando la herramienta de línea de comandos `mysql` para manipular la base de datos, pero puedes usar cualquier herramienta que quieras que te permita ejecutar consultas SQL personalizadas.

Entra al mundo del juego usando el cliente de WoW y empieza teletransportándote al área en la que pretendemos trabajar. Usa el siguiente comando GM, que podría requerir `.gm on` primero: `.go xyz -9168.486 86.90783 77.05649 0 0.006`. Verás tres NPCs caminando alrededor de una tienda de campaña, así:

![NPCs Visible](assets/images/tutorials/game_event_example/npcs.png)

A continuación, conéctate a la base de datos MySQL de AzerothCore y asegúrate de estar usando la tabla correcta: \`use acore_world\`.

Luego, aplica el siguiente SQL para crear un nuevo evento con ID 91 en tu mundo (**nota**: esto eliminará cualquier entrada de evento existente con un ID de 91):

```sql
DELETE FROM game_event WHERE eventEntry = 91;
INSERT INTO game_event (
	eventEntry,
	start_time,
	end_time,
	occurence,
	length,
	holiday,
	holidayStage,
	description,
	world_event,
	announce
) VALUES (
	91,
	"2000-01-01 14:00:00",
	"2030-12-31 14:00:00",
	2,
	1,
	0,
	0,
	"TESTING EVENT",
	0,
	1
);
```

Esto se dispara una vez cada `occurence` minutos, o `2` minutos en este caso. El evento durará `length` minutos, o `1` minuto para nosotros, lo que significa que después de un (`1`) minuto los NPCs se volverán a añadir al mundo del juego.

Ahora actualiza la tabla `game_event_creature` aplicando el siguiente SQL:

```sql
DELETE FROM game_event_creature WHERE guid=79888;
DELETE FROM game_event_creature WHERE guid=79889;
DELETE FROM game_event_creature WHERE guid=79890;

INSERT INTO game_event_creature (eventEntry,guid) VALUES (-91,79888);
INSERT INTO game_event_creature (eventEntry,guid) VALUES (-91,79889);
INSERT INTO game_event_creature (eventEntry,guid) VALUES (-91,79890);
```

Esto define los GUIDs específicos de los NPCs que queremos que el game event **despawnee** _del_ mundo por nosotros. No spawnea las creatures, ya que estas ya existen. Hay otras tablas `game_event_*` para gestionar también otras cosas, cosas mucho más complejas, pero solo estamos eligiendo esta tabla porque es fácil de trabajar con ella y de usar para demostrar cómo funcionan los eventos. Ten en cuenta que hemos puesto el campo `eventEntry` a un valor **negativo** -- es decir `-91` -- y no (positivo) `91`, porque queremos que este evento **elimine** los NPCs. No te preocupes, cuando el evento termine tras `length` minutos, los NPCs volverán a spawnear. Si quieres que el evento spawnee creatures que hayas definido, entonces usarías un GUID positivo.

Finalmente, reinicia tu world server de AzerothCore. Como el mundo del juego se ha reiniciado, y tuviste que volver a entrar al juego, te habrás perdido la primera ejecución del evento y por tanto el anuncio (que está puesto en `1` en nuestro SQL de ejemplo, arriba). Esto significa que, dependiendo de lo rápido que te teletransportes a las coordenadas de arriba, puede que encuentres que los NPCs siguen ahí o que ya hayan sido eliminados.

Cuando te quedes por el área en las coordenadas de arriba, eventualmente verás a los NPCs despawnear:

![No NPCs Visible](assets/images/tutorials/game_event_example/no-npcs.png)

## Deshacer todo

Si ahora quieres eliminar este evento de tu base de datos, se puede usar el siguiente SQL:

```sql
DELETE FROM game_event WHERE eventEntry = 91;
DELETE FROM game_event_creature WHERE guid=79888;
DELETE FROM game_event_creature WHERE guid=79889;
DELETE FROM game_event_creature WHERE guid=79890;
```

Puede que necesites recargar el "World Server" de AzerothCore para que los cambios de arriba surtan efecto.

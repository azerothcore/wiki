# gameobject\_respawn

[<-Volver a:Characters](database-characters)

**Tabla \`gameobject\_respawn\`**

La tabla alberga la hora de reaparición de los objetos del juego (GameObjects) en el mundo. En caso de caída del servidor, la tabla guarda datos de reaparición para que los objetos no reaparezcan inmediatamente al reiniciar el servidor. La frecuencia con la que se guarda el tiempo de reaparición de los objetos puede controlarse directamente en worldserver.conf.dist o worldserver.conf, específicamente en SaveRespawnTimeImmediately. Normalmente los únicos objetos que desaparecen directamente y necesitan ser reaparecidos son los cofres y las puertas.

**Estructura**

| Field            | Type     | Attributes | Key | Null | Default | Extra | Comment                  |
| ---------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]        | INT      | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [respawnTime][2] | INT      | UNSIGNED   |     | NO   | 0       |       |                          |
| [mapId][3]       | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [instanceId][4]  | INT      | UNSIGNED   | PRI | NO   | 0       |       | Instance Identifier      |

[1]: #guid
[2]: #respawntime
[3]: #mapid
[4]: #instanceid

**Descripción de los Campos**

### guid

GUID o Identificador Global Único del objeto del juego (GameObject). Véase [gameobject.guid](gameobject#guid).

### respawnTime

El tiempo en el cual el objeto del juego (GameObject) debería reaparecer, medida en tiempo Unix.

### mapid

Generalmente esta tabla se usaría para guardar la ID del mapa en el cual cierto objeto del juego (GameObject) se encontrase actualmente, pero, como ciertos GameObjects no están definidos por este medio, es posible que se establezca un valor por defecto en este campo, como lo puede ser 0 (cero).

### instanceId

En caso de que el objeto fuese activado en una instancia cualquiera, este campo contiene la ID de la instancia dónde el objeto debe reaparecer pasado cierto tiempo. Cada instancia es diferente dependiendo del grupo, por lo que este campo es vital para saber qué objetos deben reaparecer, para qué tipo jugadores y en qué momento.

# creature\_respawn

[<-Volver a:Characters](database-characters)

**Tabla \`creature\_respawn\`**

La tabla alberga la hora de reaparición de las criaturas en el mundo. En caso de caída del servidor, la tabla guarda datos de reaparición para que las criaturas muertas no reaparezcan inmediatamente al reiniciar el servidor. La frecuencia con la que se guarda el tiempo de reaparición de las criaturas puede controlarse directamente en worldserver.conf.dist o worldserver.conf, específicamente en SaveRespawnTimeImmediately.

**Estructura**

| Campo            | Tipo     | Atributos | Llave | Nulo | Por defecto | Extra | Comentario                  |
| ---------------- | -------- | --------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]        | INT      | UNSIGNED  | PRI | NO   | 0       |       | Global Unique Identifier |
| [respawnTime][2] | INT      | UNSIGNED  |     | NO   | 0       |       |                          |
| [mapId][3]       | SMALLINT | UNSIGNED  |     | NO   | 0       |       |                          |
| [instanceId][4]  | INT      | UNSIGNED  | PRI | NO   | 0       |       | Instance Identifier      |

[1]: #guid
[2]: #respawntime
[3]: #mapid
[4]: #instance

**Descripción de los Campos**

### guid

GUID o Identificador Global Único del personaje. Véase [characters.guid](characters#guid).

### respawnTime

El tiempo en el cual la criatura debería reaparecer, medida en tiempo Unix.

### mapId

Generalmente esta tabla se usaría para guardar la ID del mapa en el cual cierta criatura se encuentra actualmente, pero, como ciertos npc´s no están definidos por este medio, es posible que se establezca un valor por defecto en este campo, como lo puede ser 0 (cero).

### instance

En caso de que la criatura fuese asesinada en una instancia cualquiera, este campo contiene la ID de la instancia dónde la criatura debe reaparecer pasado cierto tiempo. Cada instancia es diferente dependiendo del grupo, por lo que este campo es vital para saber qué criaturas deben reaparecer, para qué tipo jugadores y en qué momento.

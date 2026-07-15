# spawn\_group\_template

[<-Volver a:World](database-world)

**Tabla \`spawn\_group\_template\`**

Esta tabla define las plantillas de grupos de spawn con sus nombres y flags de comportamiento. Los grupos de spawn permiten agrupar lógicamente los spawns de creatures y gameobjects con control del comportamiento de respawn por grupo.

**Estructura**

| Field                     | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [groupId](#groupid)       | INT          | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [groupName](#groupname)   | VARCHAR(100) |            |     | NO   | NULL    |       |         |
| [groupFlags](#groupflags) | INT          | UNSIGNED   |     | NO   | 0       |       |         |

**Descripción de los campos**

### groupId

Este es el ID de grupo del grupo. Debe ser un número único. Los grupos 0 y 1 son grupos de sistema reservados:

- Grupo 0: "Default Group" — Grupo de sistema que usa respawn dinámico por defecto.
- Grupo 1: "Legacy Group" — Grupo de sistema que usa el modo de compatibilidad (comportamiento de respawn heredado).

### groupName

Este es un nombre descriptivo para el grupo.

### groupFlags

Estos son los flags que se aplicarán al grupo.

| Flag                                   | Number | Description                                                                                                                                          |
| -------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| SPAWNGROUP\_FLAG\_NONE                 | 0x00   | No se aplica ningún flag                                                                                                                             |
| SPAWNGROUP\_FLAG\_SYSTEM               | 0x01   | Este grupo es un grupo de sistema. Los grupos de sistema no pueden aparecer ni desaparecer manualmente mediante comandos de GM.                       |
| SPAWNGROUP\_FLAG\_COMPATIBILITY\_MODE  | 0x02   | Este grupo usa el comportamiento de respawn heredado: el cadáver de la creature permanece en el mapa hasta que expira el temporizador de respawn, y entonces la creature reaparece en el sitio. Cuando este flag no está activado, las creatures se eliminan por completo al morir y el planificador de respawn las recrea de nuevo. |
| SPAWNGROUP\_FLAG\_MANUAL\_SPAWN        | 0x04   | Este grupo no aparecerá por defecto por parte del core. Los scripts pueden hacer aparecer/desaparecer estos grupos bajo demanda usando acciones de SmartAI o comandos de GM. |
| SPAWNGROUP\_FLAG\_DYNAMIC\_SPAWN\_RATE | 0x08   | A este grupo se le aplicarán tasas de spawn dinámicas (por defecto lo usan las creatures/gos de interés para quests y los nodos de recolección)      |
| SPAWNGROUP\_FLAG\_ESCORTQUESTNPC       | 0x10   | Este grupo contiene NPCs de quests de escolta. Esto mejora aún más el spawn dinámico para empezar el tiempo de respawn en el punto en que se toma una quest y empieza la escolta |

> La opción de configuración de worldserver `Respawn.ForceCompatibilityMode` puede forzar que todos los spawns usen el comportamiento heredado (modo de compatibilidad) sin importar los flags del grupo.

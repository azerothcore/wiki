# transports

[<-Volver a:World](database-world)

**Tabla \`transports\`**

Esta tabla contiene todos los transportes de tipo 15 (barcos y zepelines). Todos los demás tipos de transporte leen su tiempo de frame de TransportAnimation.dbc.

**Estructura**

| Field           | Type      | Attributes | Key    | Null | Default        | Extra | Comment |
| --------------- | --------- | ---------- | ------ | ---- | -------------- | ----- | ------- |
| [Guid][1]       | INT       | UNSIGNED   | PRI    | NO   | AUTO_INCREMENT |       |         |
| [Entry][2]      | MEDIUMINT | UNSIGNED   | UNIQUE | NO   | 0              |       |         |
| [Name][3]       | TEXT      |            |        | YES  | NULL           |       |         |
| [ScriptName][4] | CHAR(64)  |            |        | NO   | ' '            |       |         |

[1]: #guid
[2]: #entry
[3]: #name
[4]: #scriptname

**Descripción de los campos**

### guid

Identificador único del transporte. Cada vez que añadas un nuevo guid simplemente suma uno (1) al guid máximo.

### entry

[gameobject_template.entry](gameobject_template#entry) a usar para este transporte. Debe ser un gameobject de tipo 15.

### name

Este es un nombre arbitrario para describir el entry del transporte.

### ScriptName

El nombre de script de este transporte. Referencia a un script de ScriptDev o SmartAI.

**Nota:** Los transportes tienen su propio mapa: https://wow.tools/dbc/?dbc=map&build=3.3.5.12340#page=1&colFilter[1]=Transport

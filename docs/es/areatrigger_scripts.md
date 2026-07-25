# areatrigger\_scripts

[<-Volver a:World](database-world)

**Tabla \`areatrigger\_scripts\`**

Permite que un area trigger se scripte con Trinity Script.

**Estructura**

| Field           | Type      | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]      | MEDIUMINT |            | PRI | NO   |         |       |         |
| [ScriptName][2] | char(64)  |            |     | NO   |         |       |         |

[1]: #entry
[2]: #scriptname

**Descripción de los campos**

### entry

Este es el identificador del trigger de [AreaTrigger.dbc](DBC-AreaTrigger)

### ScriptName

El ScriptName para cuando lo scriptes en el core.
También puede ser 'SmartTrigger'. Entonces usará [SmartAI](smart_scripts).

### Examples

| entry | ScriptName        |
| ----- | ----------------- |
| 302   | at_sentry_point   |
| 962   | SmartTrigger      |
| 1447  | SmartTrigger      |
| 1526  | at_ring_of_law    |
| 1726  | at_scent_larkorwi |

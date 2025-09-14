# areatrigger\_scripts

[<-Voler a:World](database-world)

**The \`areatrigger\_scripts\` table**

Permite que un disparador de área sea programado con Trinity Script.

**Estructura**

| Campo           | Tipo      | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| --------------- | --------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [entry][1]      | MEDIUMINT |           | PRI   | NO   |             |       |            |
| [ScriptName][2] | char(64)  |           |       | NO   |             |       |            |

[1]: #entry
[2]: #scriptname

**Descripción de los campos**

### entry

This is the trigger identifier from [AreaTrigger.dbc](DBC-AreaTrigger)

### ScriptName

El nombre del script para la creación de scripts en el núcleo. También podría ser "SmartTrigger". Entonces usará [SmartAI](smart_scripts).

### Ejemplo

| entry | ScriptName        |
| ----- | ----------------- |
| 302   | at_sentry_point   |
| 962   | SmartTrigger      |
| 1447  | SmartTrigger      |
| 1526  | at_ring_of_law    |
| 1726  | at_scent_larkorwi |

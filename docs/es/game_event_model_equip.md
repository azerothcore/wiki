# game_event_model_equip

[<-Volver a:World](database-world)

**Tabla \`game_event_model_equip\`**

Contiene todas las instancias de creature que necesitan cambiar su display id y/o su equipamiento durante los eventos de juego definidos.

**Estructura**

| Field                         | Type      | Attributes | Key | Null | Default | Extra  | Comment                  |
| ----------------------------- | --------- | ---------- | --- | ---- | ------- | ------ | ------------------------ |
| [eventEntry](#evententry)     | SMALLINT  | SIGNED     |     | NO   | 0       |        | Entry del evento de juego. |
| [guid](#guid)                 | INT       | UNSIGNED   | PRI | NO   | 0       | Unique |                          |
| [modelid](#modelid)           | MEDIUMINT | UNSIGNED   |     | NO   | 0       |        |                          |
| [equipment_id](#equipment_id) | MEDIUMINT | UNSIGNED   |     | NO   | 0       |        |                          |

**Descripción de los campos**

### eventEntry

Se refiere a: [game_event.entry](game_event#entry).

Solo se puede usar un valor **positivo**.

### guid

Se refiere a: [creature.guid](creature#guid).

### modelid

Se refiere a [creature_model_info.displayid](creature_model_info#displayid) para cambiar el [modelo](creature_model_info#displayid) de la [creature](creature#guid) mientras el evento está activo.

### equipment_id

Se refiere a [creature_equip_template.creatureid](creature_equip_template#creatureid) para cambiarlo mientras el evento está activo.

Si no quieres añadir o cambiar el equipamiento que se está usando actualmente, fija el valor a `0`. Usará [creature_equip_template](creature_equip_template#CreatureID) para la [creature_template](creature_template#entry) donde coincida con [creature.id1](creature#id1) de [creature.guid](creature#guid).

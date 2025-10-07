# game_event_model_equip

[<-Volver a:World](database-world)

**Tabla \`game_event_model_equip\`**

Contiene todas las instancias de criaturas que necesitan cambiar la identificación de visualización y/o el equipo durante eventos de juego definidos.

**Estructura**

| Campo                         | Tipo      | Atributos | Llave | Nulo | Por defecto | Extra  | Comentario                    |
| ----------------------------- | --------- | --------- | ----- | ---- | ----------- | ------ | ----------------------------- |
| [eventEntry](#evententry)     | SMALLINT  | SIGNED    |       | NO   | 0           |        | Entrada del evento del juego. |
| [guid](#guid)                 | INT       | UNSIGNED  | PRI   | NO   | 0           | Único  |                               |
| [modelid](#modelid)           | MEDIUMINT | UNSIGNED  |       | NO   | 0           |        |                               |
| [equipment_id](#equipment_id) | MEDIUMINT | UNSIGNED  |       | NO   | 0           |        |                               |

**Descripción de los campos**

### eventEntry

Se refiere a: [game_event.entry](game_event#entry).

Sólo se puede utilizar un valor **positivo**.

### guid

Se refiere a: [creature.guid](creature#guid).

### modelid

Se refiere a: [creature_model_info.displayid](creature_model_info#displayid) para cambiar el [modelo](creature_model_info#displayid) de la [criatura](creature#guid) cuando se ejecuta el evento.

### equipment_id

Se refiere a: [creature_equip_template.creatureid](creature_equip_template#creatureid) para cambiar cuando se ejecuta el evento.

Si no desea agregar o cambiar el equipo actual que se está utilizando, configure el valor en "0". Se utilizará [creature_equip_template](creature_equip_template#CreatureID) para la [creature_template](creature_template#entry) donde coincida con [creature.id1](creature#id1) de [creature.guid](creature#guid).

# game\_event\_prerequisite

[<-Volver a:World](database-world)

**Tabla \`game\_event\_prerequisite\`**

Esta tabla contiene los eventos que deben haberse completado para iniciar el evento dado. Puedes tener más de un evento que deba completarse antes de que empiece el siguiente.

**Estructura**

| Field                   | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [eventEntry][1]         | TINYINT   | UNSIGNED   | PRI | NO   |         |       |         |
| [prerequisite_event][2] | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |

[1]: #evententry
[2]: #prerequisite_event

**Descripción de los campos**

### eventEntry

Este es el evento que empezará cuando todos los eventos prerrequisito se hayan completado.

### prerequisite\_event

Este es el evento que debe completarse antes de que empiece el siguiente [evento](#game_event_prerequisite-eventEntry).

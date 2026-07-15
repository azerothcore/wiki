# character_achievement_offline_updates

[<-Volver a: Characters](database-characters)

**Tabla \`character_achievement_offline_updates\`**

Almacena las actualizaciones de los logros de un personaje cuando el personaje estaba desconectado.

**Estructura**

| Field                       | Type    | Attributes | Key | Null | Default | Extra | Comment |
| --------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid](#guid)               | INT     | UNSIGNED   | IDX | NO   |         |       |         |
| [update_type](#update_type) | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [arg1](#arg1)               | INT     | UNSIGNED   |     | NO   |         |       |         |
| [arg2](#arg2)               | INT     | UNSIGNED   |     | YES  | NULL    |       |         |
| [arg3](#arg3)               | INT     | UNSIGNED   |     | YES  | NULL    |       |         |

**Descripción de los campos**

### guid

El GUID del personaje. Véase [characters.guid](characters#guid).

### update_type

Tipos soportados: 1 - COMPLETE_ACHIEVEMENT; 2 - UPDATE_CRITERIA

### arg1

Para el tipo 1: ID del logro; para el tipo 2: ACHIEVEMENT_CRITERIA_TYPE

### arg2

Para el tipo 2: miscValue1 para actualizar el criterio del logro

### arg3

Para el tipo 2: miscValue1 para actualizar el criterio del logro

# character_achievement_offline_updates

[<-Volver a:Characters](database-characters)

**Tabla \`character_achievement_offline_updates\`**

Almacena actualizaciones de los logros del personaje cuando el personaje estaba desconectado.

**Table Structure**

| Campo                       | Tipo    | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| --------------------------- | ------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [guid](#guid)               | INT     | UNSIGNED  | IDX   | NO   |             |       |            |
| [update_type](#update_type) | TINYINT | UNSIGNED  |       | NO   |             |       |            |
| [arg1](#arg1)               | INT     | UNSIGNED  |       | NO   |             |       |            |
| [arg2](#arg2)               | INT     | UNSIGNED  |       | YES  | NULL        |       |            |
| [arg3](#arg3)               | INT     | UNSIGNED  |       | YES  | NULL        |       |            |

**Descripción de los campos**

### guid

El GUID del personaje. Véase [characters.guid](characters#guid).

### update_type

Tipos admitidos: 1 - COMPLETE_ACHIEVEMENT; 2 - UPDATE_CRITERIA

### arg1

Para el tipo 1: achievement ID; para el tipo 2: ACHIEVEMENT_CRITERIA_TYPE

### arg2

Para el tipo 2: miscValue1 para actualizar los criterios de logro

### arg3

Para el tipo 2: miscValue1 para actualizar los criterios de logro

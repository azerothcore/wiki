# achievement\_reward\_locale

[<-Volver a:World](database-world)

**Tabla \`achievement\_reward\_locale\`**

Es la tabla que almacena las traducciones de la tabla `achievement_reward`, para que el cliente del juego pueda mostrar los mensajes en diferentes idiomas.

**Estructura**

| Field        | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ------------ | ---------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]      | MEDIUMINT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Locale][2]  | VARCHAR(4) |            | PRI | NO   |         |       |         |
| [Subject][3] | text       |            |     | YES  |         |       |         |
| [Text][4]    | text       |            |     | YES  |         |       |         |

[1]: #id
[2]: #locale
[3]: #subject
[4]: #text

**Descripción de los campos**

### ID

Es el [ID](achievement_reward#id) del logro obtenido de `achievement_reward`

### Locale

Este es el idioma del cliente del juego.

| ID  | Language |
| --- | -------- |
| 0   | enUS     |
| 1   | koKR     |
| 2   | frFR     |
| 3   | deDE     |
| 4   | zhCN     |
| 5   | zhTW     |
| 6   | esES     |
| 7   | esMX     |
| 8   | ruRU     |

### Subject

Es el texto de la columna [Subject](achievement_reward#subject) de la tabla `achievement_reward`

### Text

Es el texto de la columna [Body](achievement_reward#body) de la tabla `achievement_reward`

### Example
```sql
DELETE FROM `achievement_reward_locale` WHERE `ID`=13 AND `Locale`="esES";
INSERT INTO `achievement_reward_locale` (`ID`, `Locale`, `Subject`, `Text`) VALUES
(13, "esES", "Nivel 80", "Alcanza el nivel 80.");
```

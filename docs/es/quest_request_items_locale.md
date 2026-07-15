# quest\_request\_items\_locale

**Tabla: quest\_request\_items\_locale**

[<-Volver a: World](database-world)

**Estructura**

| Field               | Type       | Attribute | Key | Null | Default | Extra | Comment |
| ------------------- | ---------- | --------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]             | INT        | UNSIGNED  | PRI | NO   |         |       |         |
| [locale][2]         | VARCHAR(4) |           | PRI | NO   |         |       |         |
| [CompletionText][3] | text       |           |     | YES  | NULL    |       |         |
| [VerifiedBuild][4]  | SMALLINT   |           |     | NO   |         |       |         |

[1]: #id
[2]: #locale
[3]: #completiontext
[4]: #verifiedbuild

**Descripción de los campos**

### ID

Es el ID de la misión, obtenido de quest_template

### locale

Es el idioma en el que quieres hacer la traducción.
Puedes elegir entre los siguientes:

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

### CompletionText

Es el texto que se muestra mientras la misión no está completada.

### VerifiedBuild

### Example
```sql
DELETE FROM `quest_request_items_locale` WHERE `ID`=2 AND `locale`='esES';
INSERT INTO `quest_request_items_locale` (`ID`, `locale`, `CompletionText`, `VerifiedBuild`) VALUES`ID`, `locale`, `CompletionText`, `VerifiedBuild`
(2, "esES", "Sí, $gpoderoso:poderosa; $c, he presentido tu llegada. Confío que tienes más noticias que darme sobre tu caza.", 0);
```

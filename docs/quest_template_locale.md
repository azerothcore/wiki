# quest\_template\_locale

[<-Back-to:World](database-world.md)

**The \`quest\_template\_locale\` table**

This table is used to provide to localized clients with localized string for quest templates.

**Structure**

| Field          | Type                  | Collation       | Null | Key | Default | Extra | Comment |
|----------------|-----------------------|-----------------|------|-----|---------|-------|---------|
| ID             | mediumint(8) unsigned | (NULL)          | NO   | PRI | 0       |       |         |
| locale         | varchar(4)            | utf8_general_ci | NO   | PRI | (NULL)  |       |         |
| Title          | text                  | utf8_general_ci | YES  |     | (NULL)  |       |         |
| Details        | text                  | utf8_general_ci | YES  |     | (NULL)  |       |         |
| Objectives     | text                  | utf8_general_ci | YES  |     | (NULL)  |       |         |
| EndText        | text                  | utf8_general_ci | YES  |     | (NULL)  |       |         |
| CompletedText  | text                  | utf8_general_ci | YES  |     | (NULL)  |       |         |
| ObjectiveText1 | text                  | utf8_general_ci | YES  |     | (NULL)  |       |         |
| ObjectiveText2 | text                  | utf8_general_ci | YES  |     | (NULL)  |       |         |
| ObjectiveText3 | text                  | utf8_general_ci | YES  |     | (NULL)  |       |         |
| ObjectiveText4 | text                  | utf8_general_ci | YES  |     | (NULL)  |       |         |
| VerifiedBuild  | smallint(5)           | (NULL)          | YES  |     | 0       |       |         |

**Description of the fields**

### ID

This is the ID of the quest to be translated.

### locale

| ID | Language |
|----|----------|
| 0  | enUS     |
| 1  | koKR     |
| 2  | frFR     |
| 3  | deDE     |
| 4  | zhCN     |
| 5  | zhTW     |
| 6  | esES     |
| 7  | esMX     |
| 8  | ruRU     |

### Title

The title of the quest in the respective language.

### Details

Detail of the quest.

### Objectives

This is the text that is displayed when it is completed.

### EndText

This is the text that is displayed until the quest is completed.

### ObjectiveText1, ObjectiveText2, ObjectiveText3, ObjectiveText4

These are the objectives of the quest.
In other words, it is the text that accompanies the counters.

### VerifiedBuild

### Example
```sql
DELETE FROM `quest_template_locale` WHERE `ID`=62 AND `locale`="esES";

INSERT INTO `quest_template_locale` (`ID`, `locale`, `Title`, `Details`, `Objectives`, `EndText`, `CompletedText`, `ObjectiveText1`, `ObjectiveText2`, `ObjectiveText3`, `ObjectiveText4`, `VerifiedBuild`) VALUES
(62, "esES", "La Mina Abisal", "¡La mina de Villanorte no es la única que tiene problemas! Según mis informes, la Mina Abisal de Elwynn también ha sido ocupada por los kóbolds.$B$BExplora la mina y comprueba la veracidad de mis informes. Luego vuelve aquí. La mina está hacia el sur de Villadorada, entre La Granja Pedregosa y la granja Maclure.", "Explora la Mina Abisal y vuelve junto al alguacil Dughan a Villadorada.", "Explora la Mina Abisal", "Vuelve con: Alguacil Dughan. Zona: Villadorada, Bosque de Elwynn.", "", "", "", "", 18019);
```

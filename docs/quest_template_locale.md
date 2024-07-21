# quest\_template\_locale

[<-Back-to:World](database-world)

**The \`quest\_template\_locale\` table**

This table is used to provide to localized clients with localized string for quest templates.

**Table Structure**

| Field                | Type       | Attribute | Key | Null | Default | Extra | Comment |
| -------------------- | ---------- | --------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]              | MEDIUMINT  | UNSIGNED  | PRI | NO   | 0       |       |         |
| [locale][2]          | VARCHAR(4) |           | PRI | NO   |         |       |         |
| [Title][3]           | text       |           |     | YES  |         |       |         |
| [Details][4]         | text       |           |     | YES  |         |       |         |
| [Objectives][5]      | text       |           |     | YES  |         |       |         |
| [EndText][6]         | text       |           |     | YES  |         |       |         |
| [CompletedText][7]   | text       |           |     | YES  |         |       |         |
| [ObjectiveText1][8]  | text       |           |     | YES  |         |       |         |
| [ObjectiveText2][9]  | text       |           |     | YES  |         |       |         |
| [ObjectiveText3][10] | text       |           |     | YES  |         |       |         |
| [ObjectiveText4][11] | text       |           |     | YES  |         |       |         |
| [VerifiedBuild][12]  | SMALLINT   |           |     | YES  | 0       |       |         |

[1]: #id
[2]: #locale
[3]: #title
[4]: #details
[5]: #objectives
[6]: #endtext
[7]: #completedtext
[8]: #objectivetext1
[9]: #objectivetext2
[10]: #objectivetext3
[11]: #objectivetext4
[12]: #verifiedbuild

**Description of the fields**

### ID

This is the ID of the quest to be translated.

### locale

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

### Title

The title of the quest in the respective language.

### Details

Detail of the quest.

### Objectives

This is the text that is displayed when it is completed.

### EndText

This is the text that is displayed until the quest is completed.

### ObjectiveText1

This is objective 1 of the search.
In other words, it is the text that accompanies the counters.

### ObjectiveText2

This is objective 2 of the search.
In other words, it is the text that accompanies the counters.

### ObjectiveText3

This is objective 3 of the search.
In other words, it is the text that accompanies the counters.

### ObjectiveText4

This is objective 4 of the search.
In other words, it is the text that accompanies the counters.

### VerifiedBuild

### Example
```sql
DELETE FROM `quest_template_locale` WHERE `ID`=62 AND `locale`="esES";

INSERT INTO `quest_template_locale` (`ID`, `locale`, `Title`, `Details`, `Objectives`, `EndText`, `CompletedText`, `ObjectiveText1`, `ObjectiveText2`, `ObjectiveText3`, `ObjectiveText4`, `VerifiedBuild`) VALUES
(62, "esES", "La Mina Abisal", "¡La mina de Villanorte no es la única que tiene problemas! Según mis informes, la Mina Abisal de Elwynn también ha sido ocupada por los kóbolds.$B$BExplora la mina y comprueba la veracidad de mis informes. Luego vuelve aquí. La mina está hacia el sur de Villadorada, entre La Granja Pedregosa y la granja Maclure.", "Explora la Mina Abisal y vuelve junto al alguacil Dughan a Villadorada.", "Explora la Mina Abisal", "Vuelve con: Alguacil Dughan. Zona: Villadorada, Bosque de Elwynn.", "", "", "", "", 18019);
```

# quest\_template\_locale

[<-返回至:World](database-world)

**`quest\_template\_locale` 表**

此表用于为本地化客户端提供任务模板的本地化字符串。

**表结构**

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

**字段说明**

### ID

这是要翻译的任务的 ID。

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

任务在相应语言中的标题。

### Details

任务的详情。

### Objectives

这是任务完成时显示的文本。

### EndText

这是任务完成之前一直显示的文本。

### ObjectiveText1

这是目标 1 的文本。
换句话说，它是伴随计数器的文本。

### ObjectiveText2

这是目标 2 的文本。
换句话说，它是伴随计数器的文本。

### ObjectiveText3

这是目标 3 的文本。
换句话说，它是伴随计数器的文本。

### ObjectiveText4

这是目标 4 的文本。
换句话说，它是伴随计数器的文本。

### VerifiedBuild

### 示例
```sql
DELETE FROM `quest_template_locale` WHERE `ID`=62 AND `locale`="esES";

INSERT INTO `quest_template_locale` (`ID`, `locale`, `Title`, `Details`, `Objectives`, `EndText`, `CompletedText`, `ObjectiveText1`, `ObjectiveText2`, `ObjectiveText3`, `ObjectiveText4`, `VerifiedBuild`) VALUES
(62, "esES", "La Mina Abisal", "¡La mina de Villanorte no es la única que tiene problemas! Según mis informes, la Mina Abisal de Elwynn también ha sido ocupada por los kóbolds.$B$BExplora la mina y comprueba la veracidad de mis informes. Luego vuelve aquí. La mina está hacia el sur de Villadorada, entre La Granja Pedregosa y la granja Maclure.", "Explora la Mina Abisal y vuelve junto al alguacil Dughan a Villadorada.", "Explora la Mina Abisal", "Vuelve con: Alguacil Dughan. Zona: Villadorada, Bosque de Elwynn.", "", "", "", "", 18019);
```

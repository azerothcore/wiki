# player\_shapeshift\_model

[<-Back-to:World](database-world)

**The \`player\_shapeshift\_model\` table**

This table holds the information on what values are used for the druid shapeshift models, based on the shapeshift, race, character customization, and the gender of the player character.

**Table: player\_shapeshift\_model's Structure**

| Field                               | Type    |          | Null | Key | Default | Extra | Comment |
| :---------------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ShapeshiftID](#shapeshiftid)       | TINYINT | UNSIGNED | NO   | PRI |         |       |         |
| [RaceID](#raceid)                   | TINYINT | UNSIGNED | NO   | PRI |         |       |         |
| [CustomizationID](#customizationid) | TINYINT | UNSIGNED | NO   | PRI |         |       |         |
| [GenderID](#genderid)               | TINYINT | UNSIGNED | NO   | PRI |         |       |         |
| [ModelID](#modelid)                 | INT     | UNSIGNED | NO   |     |         |       |         |

**Description of the table's fields**

### ShapeshiftID

| FormID | Description      |
| ------ | ---------------- |
| 1      | Cat Form         |
| 5      | Bear Form        |
| 8      | Dire Bear Form   |
| 27     | Epic Flight Form |
| 29     | Flight Form      |

### RaceID

| RaceID | Description |
| ------ | ----------- |
| 4      | Night Elf   |
| 6      | Tauren      |

For `RaceID` you can refer to the [chrraces](chrraces) "ID" column.

### CustomizationID

If you're an Alliance character (only Night Elves with stock races), the customization ID is based off of [haircolor](characters#haircolor) of your character.

If you're a Horde character (only Tauren with stock races), the customization ID is based off of [skin colour](characters#skin) of your character.

### GenderID

| [GenderID](characters#gender) | Description |
| ----------------------------- | ----------- |
| 0                             | Male        |
| 1                             | Female      |
| 2                             | Any gender  |

### ModelID

Refer to [creature_model_info](creature_model_info#displayid)

# player_shapeshift_model

[<-Back-to:World](database-world)

**The \`player_shapeshift_model\` table**

This table holds the information on what values are used for the druid shapeshift models, based on the shapeshift, race, character customization, and the gender of the player character.


**Table Structure**

| Field                              | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| ShapeshiftID (#shapeshiftid)       | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| RaceID (#raceid)                   | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| CustomizationID (#customizationid) | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| GenderID (#genderid)               | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| ModelID (#modelid)                 | INT     | UNSIGNED   |     | NO   |         |       |         |

**Description of the fields**

### ShapeshiftID

| FormID |   Description    |
| :----: | :--------------: |
|   1    |     Cat Form     |
|   5    |    Bear Form     |
|   8    |  Dire Bear Form  |
|   27   | Epic Flight Form |
|   29   |   Flight Form    |

### RaceID

| RaceID | Description |
| :----: | :---------: |
|   4    |  Night Elf  |
|   6    |   Tauren    |

You also may refer to [chrraces](chrraces) "ID" column.

### CustomizationID

If you're an Alliance character (only Night Elves with stock races), the customization ID is based off of [haircolor](characters#haircolor) of your character.

If you're a Horde character (only Tauren with stock races), the customization ID is based off of [skin colour](characters#skin) of your character.

### GenderID

| [GenderID](characters#gender) | Description |
| :---------------------------: | :---------: |
|               0               |    Male     |
|               1               |   Female    |
|               2               |  Any gender |

### ModelID

Refer to [creature_model_info](#creature_model_info#displayid)



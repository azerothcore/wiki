# emotestextsound\_dbc

[<-Back-to:World](database-world)

**The \`emotestextsound\_dbc\` table**

This DBC links a text emote (from [EmotesText.dbc](emotes)) to the sound played when that text emote is used, per race and sex. The server looks these entries up through `FindTextSoundEmoteFor(emote, race, gender)`, indexed by (EmotesTextID, RaceID, SexID).

**Version is : 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)

**Table: emotestextsound\_dbc's Structure**

| Field                         | Type |     | Null | Key | Default | Extra | Comment        |
| :---------------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------------- |
| [ID](#id)                     | INT  |     | NO   | PRI | 0       |       | Unique ID      |
| [EmotesTextID](#emotestextid) | INT  |     | NO   |     | 0       |       | Text emote ID  |
| [RaceID](#raceid)             | INT  |     | NO   |     | 0       |       |                |
| [SexID](#sexid)               | INT  |     | NO   |     | 0       |       |                |
| [SoundID](#soundid)           | INT  |     | NO   |     | 0       |       | Sound entry ID |

**Description of the table's fields**

### ID

This is the ID from EmotesTextSound.dbc.

### EmotesTextID

ID of the text emote (`EmotesText.dbc`) this sound is associated with.

### RaceID

ID from [ChrRaces.dbc](chrraces).

### SexID

| ID  | Name   |
| --- | ------ |
| 0   | Male   |
| 1   | Female |

### SoundID

ID of the sound entry played when the text emote is used by a unit of the given race/sex.

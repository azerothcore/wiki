# emotestextsound\_dbc

[`Back-to:DBC`](dbc-index)

**The \`emotestextsound\_dbc\` table**

This DBC links a text emote (from [EmotesText.dbc](emotes)) to the sound played when that text emote is used, per race and sex. The server looks these entries up through `FindTextSoundEmoteFor(emote, race, gender)`, indexed by (EmotesTextID, RaceID, SexID).

**Version is : 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)

**Table Structure**

| Field             | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]            | INT  | SIGNED     | PRI | NO   | 0       |       | Unique ID |
| [EmotesTextID][2]  | INT  | SIGNED     |     | NO   | 0       |       | Text emote ID |
| [RaceID][3]        | INT  | SIGNED     |     | NO   | 0       |       | |
| [SexID][4]         | INT  | SIGNED     |     | NO   | 0       |       | |
| [SoundID][5]       | INT  | SIGNED     |     | NO   | 0       |       | Sound entry ID |

[1]: #id
[2]: #emotestextid
[3]: #raceid
[4]: #sexid
[5]: #soundid

**Description of the fields**

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

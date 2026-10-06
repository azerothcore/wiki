# quest\_greeting

[<-Back-to:World](database-world)

**The \`quest\_greeting\` table**

This table add greeting behavior to an NPC or an Gameobject.

**Table: quest\_greeting's Structure**

| Field                               | Type     |          | Null | Key | Default | Extra | Comment |
| :---------------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                           | INT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [type](#type)                       | TINYINT  | UNSIGNED | NO   | PRI | 0       |       |         |
| [GreetEmoteType](#greetemotetype)   | SMALLINT | UNSIGNED | NO   |     | 0       |       |         |
| [GreetEmoteDelay](#greetemotedelay) | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [Greeting](#greeting)               | TEXT     |          | YES  |     | NULL    |       |         |
| [VerifiedBuild](#verifiedbuild)     | INT      |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### ID

Unique ID ([creature_template.entry](creature_template#entry) or [gameobject\_template.entry](gameobject_template#entry))

### Type

-   0=Creature (The ID is point to creature\_template.entry)
-   1=GameObject (The ID is point to gameobject\_template.entry)

### GreetEmoteType

Quest NPC [Emote](emotes)

### GreetEmoteDelay

Emote delay in milliseconds

### Greeting

Text to show

### VerifiedBuild

This field was used to determine whether a template has been verified from WDB files.

- If value is 0 then it has not been parsed yet.
- If value is above 0 then it has been parsed with WDB files from that specific client build.
- If value is -1 then it is just a place holder until proper data are found on WDBs.
- If value is -Client Build then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.

# quest\_details

[<-Back-to:World](database-world)

**The \`quest\_details\` table**

This table handles Quest NPC emotes with emote delays.

**Table: quest\_details's Structure**

| Field                           | Type     |          | Null | Key | Default | Extra | Comment                                             |
| :------------------------------ | :------- | :------- | :--: | :-: | :-----: | :---: | :-------------------------------------------------- |
| [ID](#id)                       | INT      | UNSIGNED | NO   | PRI | 0       |       | Unique ID ([quest\_template.ID](quest_template#id)) |
| [Emote1](#emote1)               | SMALLINT | UNSIGNED | NO   |     | 0       |       | Quest NPC [Emote](emotes)                           |
| [Emote2](#emote2)               | SMALLINT | UNSIGNED | NO   |     | 0       |       | Quest NPC [Emote](emotes)                           |
| [Emote3](#emote3)               | SMALLINT | UNSIGNED | NO   |     | 0       |       | Quest NPC [Emote](emotes)                           |
| [Emote4](#emote4)               | SMALLINT | UNSIGNED | NO   |     | 0       |       | Quest NPC [Emote](emotes)                           |
| [EmoteDelay1](#emotedelay1)     | INT      | UNSIGNED | NO   |     | 0       |       | Emote delay in milliseconds                         |
| [EmoteDelay2](#emotedelay2)     | INT      | UNSIGNED | NO   |     | 0       |       | Emote delay in milliseconds                         |
| [EmoteDelay3](#emotedelay3)     | INT      | UNSIGNED | NO   |     | 0       |       | Emote delay in milliseconds                         |
| [EmoteDelay4](#emotedelay4)     | INT      | UNSIGNED | NO   |     | 0       |       | Emote delay in milliseconds                         |
| [VerifiedBuild](#verifiedbuild) | INT      |          | YES  |     | NULL    |       | Game client Build number or manually set value      |

**Description of the table's fields**

### ID

Unique ID ([quest\_template.ID](quest_template#id))

### Emote1

Emote (from [Emotes.dbc](emotes)) played by NPC

### Emote2

Emote (from [Emotes.dbc](emotes)) played by NPC

### Emote3

Emote (from [Emotes.dbc](emotes)) played by NPC

### Emote4

Emote (from [Emotes.dbc](emotes)) played by NPC

### EmoteDelay1

Emote delay in milliseconds

### EmoteDelay2

Emote delay in milliseconds

### EmoteDelay3

Emote delay in milliseconds

### EmoteDelay4

Emote delay in milliseconds

### VerifiedBuild

This field is used by the TrinityCore DB Team to determine whether a template has been verified from WDB files.

-   If value is 0, it has not been parsed yet.
-   If value is &gt; 0, it has been parsed with WDB files from that specific [Client Build](realmlist#gamebuild).
-   If value is -1, it is just a place holder until proper data are found on WDBs.
-   If value is -[Client Build](realmlist#gamebuild), it was parsed with WDB files from that specific [client build](realmlist#gamebuild) and manually edited later for some specific necessity.

 

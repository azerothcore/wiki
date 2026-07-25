# quest\_details

[<-Volver a: World](database-world)

**Tabla \`quest_details\`**

Esta tabla gestiona los emotes del NPC de misión con sus retrasos (delays).

**Estructura**

| Field                           | Type      | Attributes | Key | NULL | Default | Comment                                             |
| ------------------------------- | --------- | ---------- | --- | ---- | ------- | --------------------------------------------------- |
| [ID](#id)                       | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       | Unique ID ([quest\_template.ID](quest_template#id)) |
| [Emote1](#emote1)               | SMALLINT  | UNSIGNED   |     | NO   | 0       | Quest NPC [Emote](emotes)                           |
| [Emote2](#emote2)               | SMALLINT  | UNSIGNED   |     | NO   | 0       | Quest NPC [Emote](emotes)                           |
| [Emote3](#emote3)               | SMALLINT  | UNSIGNED   |     | NO   | 0       | Quest NPC [Emote](emotes)                           |
| [Emote4](#emote4)               | SMALLINT  | UNSIGNED   |     | NO   | 0       | Quest NPC [Emote](emotes)                           |
| [EmoteDelay1](#emotedelay1)     | INT       | UNSIGNED   |     | NO   | 0       | Emote delay in milliseconds                         |
| [EmoteDelay2](#emotedelay2)     | INT       | UNSIGNED   |     | NO   | 0       | Emote delay in milliseconds                         |
| [EmoteDelay3](#emotedelay3)     | INT       | UNSIGNED   |     | NO   | 0       | Emote delay in milliseconds                         |
| [EmoteDelay4](#emotedelay4)     | INT       | UNSIGNED   |     | NO   | 0       | Emote delay in milliseconds                         |
| [VerifiedBuild](#verifiedbuild) | SMALLINT  |            |     | NO   | 0       | Game client Build number or manually set value      |

**Descripción de los campos**

### ID

ID único ([quest\_template.ID](quest_template#id))

### Emote1

Emote (de [Emotes.dbc](emotes)) reproducido por el NPC

### Emote2

Emote (de [Emotes.dbc](emotes)) reproducido por el NPC

### Emote3

Emote (de [Emotes.dbc](emotes)) reproducido por el NPC

### Emote4

Emote (de [Emotes.dbc](emotes)) reproducido por el NPC

### EmoteDelay1

Retraso del emote en milisegundos

### EmoteDelay2

Retraso del emote en milisegundos

### EmoteDelay3

Retraso del emote en milisegundos

### EmoteDelay4

Retraso del emote en milisegundos

### VerifiedBuild

Este campo lo usa el equipo de BD de TrinityCore para determinar si una plantilla ha sido verificada a partir de archivos WDB.

-   Si el valor es 0, aún no ha sido parseada.
-   Si el valor es &gt; 0, ha sido parseada con archivos WDB de esa [Client Build](realmlist#realmlist-gamebuild) específica.
-   Si el valor es -1, es solo un marcador de posición hasta que se encuentren datos adecuados en los WDB.
-   Si el valor es -[Client Build](realmlist#realmlist-gamebuild), fue parseada con archivos WDB de esa [build de cliente](realmlist#realmlist-gamebuild) específica y editada manualmente después por alguna necesidad específica.

 

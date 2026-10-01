# quest\_request\_items

[<-Volver a: World](database-world)

**Tabla \`quest\_request\_items\`**

Esta tabla gestiona básicamente 3 detalles de la misión:

1.  Emote del NPC cuando la misión se completa
2.  Emote del NPC cuando la misión está incompleta
3.  Texto de finalización para misiones que requieren objetos de misión

**Estructura**

| Field                                   | Type      | Attributes | Key | NULL | Default | Comment |
| --------------------------------------- | --------- | ---------- | --- | ---- | ------- | ------- |
| [ID](#id)                               | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |         |
| [EmoteOnComplete](#emoteoncomplete)     | SMALLINT  | UNSIGNED   |     | NO   | 0       |         |
| [EmoteOnIncomplete](#emoteonincomplete) | SMALLINT  | UNSIGNED   |     | NO   | 0       |         |
| [CompletionText](#completiontext)       | text      |            |     | YES  | NULL    |         |
| [VerifiedBuild](#verifiedbuild)         | SMALLINT  |            |     | NO   | 0       |         |

**Descripción de los campos**

### ID

ID de misión para misiones que muestran un texto de finalización al entregar una misión de entrega de objetos.
Clave primaria de esta tabla. Cada ID de misión debe ser único.

### EmoteOnComplete

Emote (de [Emotes.dbc](emotes)) reproducido por el NPC que finaliza la misión cuando se completan todos los objetivos de la misión.

### EmoteOnIncomplete

Emote (de [Emotes.dbc](https://trinitycore.atlassian.net/wiki/display/tc/Emotes)) reproducido por el NPC que finaliza la misión si alguno de los objetivos de la misión está incompleto.

### CompletionText

Texto de gossip de misión que se muestra en la ventana final de diálogo de gossip al entregar una misión de entrega de objetos.
El/los objeto(s) de misión implicados en la misión pueden ser proporcionados por el que da la misión o recogidos por el jugador.

### VerifiedBuild

Este campo lo usa el equipo de BD de TrinityCore para determinar si una plantilla ha sido verificada a partir de archivos WDB.

-   Si el valor es 0, aún no ha sido parseada.
-   Si el valor es &gt; 0, ha sido parseada con archivos WDB de esa [Client Build](https://trinitycore.atlassian.net/wiki/display/tc/realmlist#realmlist-gamebuild) específica.
-   Si el valor es -1, es solo un marcador de posición hasta que se encuentren datos adecuados en los WDB.
-   Si el valor es -[Client Build](https://trinitycore.atlassian.net/wiki/display/tc/realmlist#realmlist-gamebuild), fue parseada con archivos WDB de esa [build de cliente](https://trinitycore.atlassian.net/wiki/display/tc/realmlist#realmlist-gamebuild) específica y editada manualmente después por alguna necesidad específica.

 

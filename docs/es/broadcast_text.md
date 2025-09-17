# broadcast\_text

**The \`broadcast\_text\` table**

Esta tabla (ref <https://github.com/TrinityCore/TrinityCore/commit/60e87db>) tendrá **todo** lo que necesitas para los textos de tus scripts, como: [gossips](gossip_menu_option), [creature texts](creature_text) y [npc\_text](npc_text)s.

Su propósito es (será) utilizado como una tabla globalizada que contiene los textos mencionados anteriormente, y cosas como sus sonidos, sus gestos y los idiomas en que deben decirse los textos.

Todos los valores provienen de sniffs (ADBVerified), por lo tanto, no agregues cosas. - Kinzcool.

 **Los valores de esta tabla provienen de rastreos (datos minoristas) y no deben cambiarse a menos que esté absolutamente seguro de que se han cambiado incorrectamente antes.**
 
 **En la mayoría de los casos, los valores aquí son correctos y su script necesita ser corregido. Asegúrese de que su script funcione correctamente antes de sugerir cambios en esta tabla.**

**Estructura**

| Campo                                    | Tipo     | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| ---------------------------------------- | -------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [ID](#broadcast_text-ID)                 | INT      | UNSIGNED  | PRI   | NO   | 0           |       |            |
| [LanguageID](#broadcast_text-Language)   | INT      | UNSIGNED  |       | NO   | 0           |       |            |
| [MaleText](#broadcast_text-MaleText)     | text     | SIGNED    |       | YES  | NULL        |       |            |
| [FemaleText](#broadcast_text-FemaleText) | text     | SIGNED    |       | YES  | NULL        |       |            |
| EmoteID1                                 | INT      | UNSIGNED  |       | NO   | 0           |       |            |
| EmoteID2                                 | INT      | UNSIGNED  |       | NO   | 0           |       |            |
| EmoteID3                                 | INT      | UNSIGNED  |       | NO   | 0           |       |            |
| EmoteDelay1                              | INT      | UNSIGNED  |       | NO   | 0           |       |            |
| EmoteDelay2                              | INT      | UNSIGNED  |       | NO   | 0           |       |            |
| EmoteDelay3                              | INT      | UNSIGNED  |       | NO   | 0           |       |            |
| SoundEntriesId                           | INT      | UNSIGNED  |       | NO   | 0           |       |            |
| EmotesID                                 | INT      | UNSIGNED  |       | NO   | 0           |       |            |
| Flags                                    | INT      | UNSIGNED  |       | NO   | 0           |       |            |
| WDBVerified                              | SMALLINT | SIGNED    |       | NO   | 0           |       |            |

### Description of the fields

### ID

El valor de identificación único para el texto.

### LanguageID

El idioma en que se transmitirá el texto.

Identificadores de Languages.dbc

### MaleText

El texto que la criatura masculina transmitirá, o los personajes masculinos pueden leer desde el menú de chismes.

### FemaleText

El texto que transmitirá la criatura femenina, o los personajes femeninos pueden leer desde el menú de chismes.

### EmoteID\[1-3\]

Los emotes que se reproducen cuando se transmiten los textos.

Identificadores de Emotes.dbc

### EmoteDelay\[1-3\]

Los retrasos de los emoticones de transmisión.

### SoundId

Los sonidos que se reproducen cuando se transmiten los textos.

Identificadores de SoundEntries.dbc

### EmotesID

Un emoticón.

### Flags

#### WDBVerified

Este campo se utilizó para determinar si una plantilla ha sido verificada a partir de archivos WDB (archivos ADB para este caso).

Si el valor es 0, entonces aún no se ha analizado.

Si el valor es superior a 0, se ha analizado con archivos WDB de esa compilación de cliente específica.

Si el valor es -1, entonces es solo un marcador de posición hasta que se encuentren los datos adecuados en las WDB.

Si el valor es -Compilación del cliente entonces se analizó con archivos WDB de esa [compilación del cliente](http://archive.trinitycore.info/DB:Auth:realmlist#gamebuild "DB:Auth:realmlist") específica y luego se editó manualmente para satisfacer alguna necesidad especial.


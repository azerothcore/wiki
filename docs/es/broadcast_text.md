# broadcast\_text

**Tabla \`broadcast\_text\`**

 

Esta tabla (ref <https://github.com/TrinityCore/TrinityCore/commit/60e87db>) tendrá **todo** lo que necesitas para los textos de tus scripts, como: [gossips](gossip_menu_option), [textos de creatures](creature_text) y [npc\_text](npc_text)s.

Su propósito es (será) usarse como una tabla globalizada que contiene los textos mencionados arriba, y cosas como sus sonidos, sus emotes y los idiomas en los que deberían decirse los textos.

 **Los valores de esta tabla provienen de sniffs (datos de retail) y no deberían cambiarse a menos que estés absolutamente seguro de que se cambiaron mal antes.**
 
 **La mayoría de las veces, los valores de aquí son correctos y lo que hay que arreglar es tu script. Por favor, asegúrate de que tu script funciona correctamente antes de sugerir cambios en esta tabla.**

**Estructura**

| Field                                    | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#broadcast_text-ID)                 | INT      | UNSIGNED   | PRI | NO   | 0       |       |         |
| [LanguageID](#broadcast_text-Language)   | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [MaleText](#broadcast_text-MaleText)     | text     | SIGNED     |     | YES  | NULL    |       |         |
| [FemaleText](#broadcast_text-FemaleText) | text     | SIGNED     |     | YES  | NULL    |       |         |
| EmoteID1                                 | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EmoteID2                                 | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EmoteID3                                 | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EmoteDelay1                              | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EmoteDelay2                              | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EmoteDelay3                              | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| SoundEntriesId                           | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| EmotesID                                 | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| Flags                                    | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| WDBVerified                              | SMALLINT | SIGNED     |     | NO   | 0       |       |         |

### Descripción de los campos

 

### ID

El valor de ID único del texto.

### LanguageID

El idioma en el que se emitirá (broadcast) el texto.

IDs de Languages.dbc

### MaleText

El texto que emitirá la creature masculina, o que los personajes masculinos pueden leer en el menú de gossip.

### FemaleText

El texto que emitirá la creature femenina, o que los personajes femeninos pueden leer en el menú de gossip.

### EmoteID\[1-3\]

Los emotes que se reproducen cuando se emiten los textos.

IDs de Emotes.dbc

### EmoteDelay\[1-3\]

Los retardos de los emotes de la emisión.

### SoundId

Los sonidos que se reproducen cuando se emiten los textos.

IDs de SoundEntries.dbc

### EmotesID

Un emote.

### Flags

 

#### WDBVerified

Este campo se usaba para determinar si una plantilla ha sido verificada a partir de archivos WDB (archivos ADB en este caso).

Si el valor es 0 entonces aún no se ha parseado.

Si el valor es mayor que 0 entonces se ha parseado con archivos WDB de esa build de cliente concreta.

Si el valor es -1 entonces es solo un marcador de posición hasta que se encuentren los datos correctos en los WDB.

Si el valor es -Client Build entonces se parseó con archivos WDB de esa [build de cliente](http://archive.trinitycore.info/DB:Auth:realmlist#gamebuild "DB:Auth:realmlist") concreta y se editó manualmente después por alguna necesidad especial.

 

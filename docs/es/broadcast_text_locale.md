# broadcast\_text\_locale

**Tabla \`broadcast\_text\_locale\`**

 

Esta tabla tendrá los **textos localizados** de la tabla \`broadcast\_text\`. Se usa en [gossips](gossip_menu_option), [textos de creatures](creature_text) y [npc\_text](npc_text)s.

Su propósito es (será) usarse como una tabla globalizada que contiene los textos localizados mencionados arriba.


**Estructura**

| Field                     | Type       | Key | Null | Default | Extra | Comment |
| ------------------------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#ID)                 | MEDIUMINT  | PRI | NO   | 0       |       |         |
| [locale](#locale)         | VARCHAR(4) | PRI | NO   | NULL    |       |         |
| [MaleText](#MaleText)     | text       |     | YES  | NULL    |       |         |
| [FemaleText](#FemaleText) | text       |     | YES  | NULL    |       |         |
| VerifiedBuild             | SMALLINT   |     | YES  | 0       |       |         |

**Descripción de los campos**

### ID

El valor de ID único del texto, que apunta al ID del texto en la tabla broadcast_text.

### locale

El idioma en el que se emitirá (broadcast) el texto.
Puede tener 8 valores : deDE, esES, esMX, frFR, koKR, ruRU, zhCN, zhTW

### MaleText

El texto localizado que emitirá la creature masculina, o que los jugadores masculinos pueden leer en el menú de gossip.

### FemaleText

El texto localizado que emitirá la creature femenina, o que los jugadores femeninos pueden leer en el menú de gossip.

#### WDBVerified

Este campo lo usa el equipo de AzerothCore para determinar si una plantilla ha sido verificada a partir de archivos WDB (archivos ADB en este caso).

Si el valor es 0 entonces aún no se ha parseado.

Si el valor es mayor que 0 entonces se ha parseado con archivos WDB de esa build de cliente concreta.

Si el valor es -1 entonces es solo un marcador de posición hasta que se encuentren los datos correctos en los WDB.

Si el valor es -Client Build entonces se parseó con archivos WDB de esa [build de cliente](realmlist#gamebuild "DB:Auth:realmlist") concreta y se editó manualmente después por alguna necesidad especial.

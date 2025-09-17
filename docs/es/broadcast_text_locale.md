# broadcast\_text\_locale

**Tabla \`broadcast\_text\_locale\`**

Esta tabla tendrá **textos localizados** para la tabla \`broadcast\_text\`. Se utiliza en [chismes](gossip_menu_option), [textos de criaturas](creature_text) y [npc\_text](npc_text).

Su propósito es (será) utilizado como una tabla globalizada que contiene los textos localizados como se mencionó anteriormente.

**Estructura**

| Campo                     | Tipo       | Llave | Nulo | Por defecto | Extra | Comentario |
| ------------------------- | ---------- | ----- | ---- | ----------- | ----- | ---------- |
| [ID](#ID)                 | MEDIUMINT  | PRI   | NO   | 0           |       |            |
| [locale](#locale)         | VARCHAR(4) | PRI   | NO   | NULL        |       |            |
| [MaleText](#MaleText)     | text       |       | YES  | NULL        |       |            |
| [FemaleText](#FemaleText) | text       |       | YES  | NULL        |       |            |
| VerifiedBuild             | SMALLINT   |       | YES  | 0           |       |            |

**Descripción de los campos**

### ID

El valor de identificación único para el texto, que apunta al ID del texto en la tabla broadcast_text.

### locale

El idioma en que se transmitirá el texto.
Puede tener 8 valores : deDE, esES, esMX, frFR, koKR, ruRU, zhCN, zhTW

### MaleText

The localized text that the male creature will broadcast, or male players can read from gossip menu.

### FemaleText

El texto localizado que la criatura femenina transmitirá, o las jugadoras pueden leer desde el menú de chismes.

#### WDBVerified

El equipo de AzerothCore utiliza este campo para determinar si una plantilla ha sido verificada a partir de archivos WDB (archivos ADB en este caso).

Si el valor es 0, entonces aún no se ha analizado.

Si el valor es superior a 0, se ha analizado con archivos WDB de esa compilación de cliente específica.

Si el valor es -1, entonces es solo un marcador de posición hasta que se encuentren los datos adecuados en las WDB.

Si el valor es -Compilación del cliente entonces se analizó con archivos WDB de esa [compilación del cliente](realmlist#gamebuild "DB:Auth:realmlist") específica y luego se editó manualmente para satisfacer alguna necesidad especial.

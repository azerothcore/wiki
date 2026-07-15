# creature_text_locale

[<-Volver a: World](database-world)

**Tabla \`creature_text_locale\`**

Esta tabla se usa para proporcionar a los clientes localizados las cadenas localizadas de los textos de las criaturas.

**Estructura**

| Field           | Type       | Attributes | Key | Null | Default | Extra | Comment |
|-----------------|------------|------------|-----|------|---------|-------|---------|
| [CreatureID][1] | MEDIUMINT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [GroupID][2]    | TINYINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [ID][3]         | TINYINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Locale][4]     | VARCHAR(4) |            | PRI | NO   |         |       |         |
| [Text][5]       | TEXT       |            |     | YES  | NULL    |       |         |

[1]: #creatureid
[2]: #groupid
[3]: #id
[4]: #locale
[5]: #text

**Descripción de los campos**

### CreatureID

Este es el [creature\_template.entry](creature_template#entry) al que está enlazado el script.

### GroupID

Si hay más de una entrada con el mismo entry (más de un texto que dice la criatura), esta columna se usa para elegir si es un texto aleatorio o una lista ordenada. Si una criatura tiene más de un texto para mostrar en un orden determinado, debe incrementarse por cada nueva entrada coincidente (ej. 0, 1, 2, 3...). Si solo hay una entrada o un único grupo, este valor debería ser 0. Si hay varios grupos de textos, este valor se mantiene igual dentro del grupo mientras que el id se incrementa dentro del mismo grupo.

### ID

Entrada para cada grupo de textos. Este es el identificador único cuando el entry (criatura) es el mismo y el groupid no cambia; debe incrementarse (ej. 0, 1, 2, 3...). Un texto de la criatura se seleccionará aleatoriamente de esta lista según el groupid al que pertenezca.

### Locale

Es el idioma en el que quieres hacer la traducción.
Puedes elegir entre los siguientes:

| ID | Language |
|----|----------|
| 1  | koKR     |
| 2  | frFR     |
| 3  | deDE     |
| 4  | zhCN     |
| 5  | zhTW     |
| 6  | esES     |
| 7  | esMX     |
| 8  | ruRU     |

### Text

El texto traducido que dirá la criatura.

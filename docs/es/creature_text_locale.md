# creature_text_locale

[<-Volver a:World](database-world)

**Tabla \`creature_text_locale\`**

Esta tabla se utiliza para proporcionar a los clientes localizados cadenas localizadas para los textos de las criaturas.

**Estructura**

| Campo           | Tipo       | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
|-----------------|------------|-----------|-------|------|-------------|-------|------------|
| [CreatureID][1] | MEDIUMINT  | UNSIGNED  | PRI   | NO   | 0           |       |            |
| [GroupID][2]    | TINYINT    | UNSIGNED  | PRI   | NO   | 0           |       |            |
| [ID][3]         | TINYINT    | UNSIGNED  | PRI   | NO   | 0           |       |            |
| [Locale][4]     | VARCHAR(4) |           | PRI   | NO   |             |       |            |
| [Text][5]       | TEXT       |           |       | Si   | NULL        |       |            |

[1]: #creatureid
[2]: #groupid
[3]: #id
[4]: #locale
[5]: #text

**Descripción de los campos**

### CreatureID

Esta es la [creature\_template.entry](creature_template#entry) a la que está vinculado el script.

### GroupID

Si hay más de una entrada igual (más de un texto que dice la criatura), esta columna se usa para elegir si es una palabra aleatoria o una lista ordenada. Si una criatura tiene más de un texto de palabra para mostrar en un orden determinado, debe incrementarse para cada nueva entrada coincidente (p. ej. 0, 1, 2, 3...). Si solo hay una entrada o solo un grupo, este valor debe ser 0. Si hay varios grupos de textos, este valor permanece igual dentro del grupo mientras que el id se incrementa dentro del mismo grupo.

### ID

Entrada para cada grupo de textos. Este es el identificador único cuando la entrada (criatura) es la misma y el groupid no cambia, debe incrementarse (ej. 0, 1, 2, 3...). Una criatura, por ejemplo, será seleccionada aleatoriamente de esta lista en función del groupid al que pertenece.

### Locale

Es el idioma al que desea realizar la traducción. Puede elegir entre las siguientes opciones:

| ID | Idioma |
|----|--------|
| 1  | koKR   |
| 2  | frFR   |
| 3  | deDE   |
| 4  | zhCN   |
| 5  | zhTW   |
| 6  | esES   |
| 7  | esMX   |
| 8  | ruRU   |

### Text

El texto traducido lo dirá la criatura.

# character\_pet\_declinedname

[<-Volver a:Characters](database-characters)

**Tabla \`character\_pet\_declinedname\`**

**Estructura**

| Field              | Type        | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]            | INT         | UNSIGNED   | PRI | NO   | 0       |       |         |
| [owner][2]         | INT         | UNSIGNED   |     | NO   | 0       |       |         |
| [genitive][3]      | VARCHAR(12) | SIGNED     |     | NO   | NULL    |       |         |
| [dative][4]        | VARCHAR(12) | SIGNED     |     | NO   | NULL    |       |         |
| [accusative][5]    | VARCHAR(12) | SIGNED     |     | NO   | NULL    |       |         |
| [instrumental][6]  | VARCHAR(12) | SIGNED     |     | NO   | NULL    |       |         |
| [prepositional][7] | VARCHAR(12) | SIGNED     |     | NO   | NULL    |       |         |

[1]: #id
[2]: #owner
[3]: #genitive
[4]: #dative
[5]: #accusative
[6]: #instrumental
[7]: #prepositional

**Descripción de los Campos**

### id

ID o dentificador de la mascota.

### owner

ID o Identificador del jugador.

### genitive

https://es.wikipedia.org/wiki/Caso_genitivo

### dative

https://es.wikipedia.org/wiki/Caso_dativo

### accusative

https://es.wikipedia.org/wiki/Caso_acusativo

### instrumental

https://es.wikipedia.org/wiki/Caso_instrumental

### prepositional

https://es.wikipedia.org/wiki/Sintagma_preposicional

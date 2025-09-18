# character\_glyphs

[<-Volver a:Characters](database-characters)

**Tabla \`character\_glyphs\`**

Alberga todos los datos de aquellos glifos individuales para cada personaje en la Base de Datos.

**Estructura**

| Campo            | Tipo     | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| ---------------- | -------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [guid][1]        | INT      | UNSIGNED  | PRI   | NO   |             |       |            |
| [talentGroup][2] | TINYINT  | UNSIGNED  | PRI   | NO   | 0           |       |            |
| [glyph1][3]      | SMALLINT | UNSIGNED  |       | YES  | 0           |       |            |
| [glyph2][4]      | SMALLINT | UNSIGNED  |       | YES  | 0           |       |            |
| [glyph3][5]      | SMALLINT | UNSIGNED  |       | YES  | 0           |       |            |
| [glyph4][6]      | SMALLINT | UNSIGNED  |       | YES  | 0           |       |            |
| [glyph5][7]      | SMALLINT | UNSIGNED  |       | YES  | 0           |       |            |
| [glyph6][8]      | SMALLINT | UNSIGNED  |       | YES  | 0           |       |            |

[1]: #guid
[2]: #talentgroup
[3]: #glyph
[4]: #glyph
[5]: #glyph
[6]: #glyph
[7]: #glyph
[8]: #glyph

**Descripción de los Campos**

### guid

GUID o Identificador Global Único del personaje. Véase [characters.guid](characters.guid).

### talentGroup

| ID | Nombre                              |
| -- | ----------------------------------- |
| 0  | Primera Especialización de Talentos |
| 1  | Segunda Especialización de Talentos |

### glyph 

Identificador (Entry) de 'GlyphProperties' del 1 al 6 de aquellos glifos con la Especialización de Talentos particular.

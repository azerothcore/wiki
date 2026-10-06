# character\_glyphs

[<-Back-to:Characters](database-characters)

**The \`character\_glyphs\` table**

Contains all the individual glyph data for each character.

**Table: character\_glyphs's Structure**

| Field                       | Type     |          | Null | Key | Default | Extra | Comment |
| :-------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guid](#guid)               | INT      | UNSIGNED | NO   | PRI |         |       |         |
| [talentGroup](#talentgroup) | TINYINT  | UNSIGNED | NO   | PRI | 0       |       |         |
| [glyph1](#glyph)            | SMALLINT | UNSIGNED | YES  |     | 0       |       |         |
| [glyph2](#glyph)            | SMALLINT | UNSIGNED | YES  |     | 0       |       |         |
| [glyph3](#glyph)            | SMALLINT | UNSIGNED | YES  |     | 0       |       |         |
| [glyph4](#glyph)            | SMALLINT | UNSIGNED | YES  |     | 0       |       |         |
| [glyph5](#glyph)            | SMALLINT | UNSIGNED | YES  |     | 0       |       |         |
| [glyph6](#glyph)            | SMALLINT | UNSIGNED | YES  |     | 0       |       |         |

**Description of the table's fields**

### guid

The GUID of the character. See [characters.guid](characters#guid).

### talentGroup

| ID | Name               |
| -- | ------------------ |
| 0  | is the first spec  |
| 1  | is the second spec |

### glyph 

The 1-6 GlyphProperties entry of the glyphs in that particular spec.

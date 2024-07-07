# character\_glyphs

[<-Back-to:Characters](database-characters)

**The \`character\_glyphs\` table**

Contains all the individual glyph data for each character.

**Table Structure**

| Field            | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]        | INT      | UNSIGNED   | PRI | NO   |         |       |         |
| [talentGroup][2] | TINYINT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [glyph1][3]      | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |
| [glyph2][4]      | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |
| [glyph3][5]      | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |
| [glyph4][6]      | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |
| [glyph5][7]      | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |
| [glyph6][8]      | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |

[1]: #guid
[2]: #talentgroup
[3]: #glyph
[4]: #glyph
[5]: #glyph
[6]: #glyph
[7]: #glyph
[8]: #glyph

**Description of the fields**

### guid

The GUID of the character. See [characters.guid](characters.guid).

### talentGroup

| ID | Name               |
| -- | ------------------ |
| 0  | is the first spec  |
| 1  | is the second spec |

### glyph 

The 1-6 GlyphProperties entry of the glyphs in that particular spec.

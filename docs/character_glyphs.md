# character\_glyphs

[<-Back-to:Characters](database-characters.md)

**The \`character\_glyphs\` table**

Contains all the individual glyph data for each character.

**Structure**

| Field       | Type        | Attributes | Key | Null | Default | Extra | Comment |
|-------------|-------------|------------|-----|------|---------|-------|---------|
| [guid][1]   | INT     | UNSIGNED   | PRI | NO   |         |       |         |
| [spec][2]   | TINYINT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [glyph1][3] | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |
| [glyph2][4] | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |
| [glyph3][5] | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |
| [glyph4][6] | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |
| [glyph5][7] | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |
| [glyph6][8] | SMALLINT | UNSIGNED   |     | YES  | 0       |       |         |

[1]: #guid
[2]: #spec
[3]: #glyph1
[4]: #glyph2
[5]: #glyph3
[6]: #glyph4
[7]: #glyph5
[8]: #glyph6

**Description of the fields**

### guid

The GUID of the character. See characters.guid

### spec

spec = 0 is the first spec, spec = 1 is the second spec.

### glyph 1-6

The GlyphProperties entry of the glyphs in that particular spec.

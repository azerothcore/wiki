# spelldifficulty\_dbc

[<-Volver a: World](database-world)

**Tabla \`spelldifficulty\_dbc\`**

Esta tabla determina qué ID de hechizo debe usarse según la dificultad de la mazmorra o banda.  

{% include note.html content="El valor de dificultad EPIC existe pero actualmente no se usa." %}

**Estructura**

| Field         | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]       | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [DifficultySpellID_1][2] | INT  | UNSIGNED   |     | NO   | 0       |       | Spell ID for normal dungeon / 10-player normal raid |
| [DifficultySpellID_2][3] | INT  | UNSIGNED   |     | NO   | 0       |       | Spell ID for heroic dungeon / 25-player normal raid |
| [DifficultySpellID_3][4] | INT  | UNSIGNED   |     | NO   | 0       |       | Spell ID for epic dungeon (unused) / 10-player heroic raid |
| [DifficultySpellID_4][5] | INT  | UNSIGNED   |     | NO   | 0       |       | Spell ID for 25-player heroic raid |

[1]: #id
[2]: #difficultyspellid_1
[3]: #difficultyspellid_2
[4]: #difficultyspellid_3
[5]: #difficultyspellid_4

**Descripción de los campos**

### ID
Referencia de ID de hechizo en scripts/SmartAI

### DifficultySpellID_1

ID de hechizo a usar en mazmorra normal o banda normal de 10 jugadores.

### DifficultySpellID_2

ID de hechizo a usar en mazmorra heroica o banda normal de 25 jugadores.

### DifficultySpellID_3

ID de hechizo a usar en mazmorra épica (sin usar) o banda heroica de 10 jugadores.

### DifficultySpellID_4

ID de hechizo a usar en banda heroica de 25 jugadores.

# skill\_discovery\_template

[<-Back-to:World](database-world)

**The \`skill\_discovery\_template\` table**

This table controls the so called "discovery" system of learning spells. This system is solely used by the alchemy profession and controls the chance for a player to "discover" another recipe while creating items with other recipes.

**Table: skill\_discovery\_template's Structure**

| Field                           | Type     |          | Null | Key | Default | Extra | Comment                           |
| :------------------------------ | :------- | :------- | :--: | :-: | :-----: | :---: | :-------------------------------- |
| [spellId](#spellid)             | INT      | UNSIGNED | NO   | PRI | 0       |       | SpellId of the discoverable spell |
| [reqSpell](#reqspell)           | INT      | UNSIGNED | NO   | PRI | 0       |       | spell requirement                 |
| [reqSkillValue](#reqskillvalue) | SMALLINT | UNSIGNED | NO   |     | 0       |       | skill points requirement          |
| [chance](#chance)               | FLOAT    |          | NO   |     | 0       |       | chance to discover                |

**Description of the table's fields**

### spellId

The recipe spell ID that has a chance to be automatically discovered. See Spell.dbc

### reqSpell

If nonzero, this field controls what spell must be specifically used to trigger the discovery (eg, spell 41458 will only be discovered while using spell 28575). If it is zero, then any recipe use can trigger the discovery. See Spell.dbc

### reqSkillValue

The minimum skill level required in the relevant profession to be able to discover this recipe.

### chance

The chance, in percent, that a recipe has of being automatically "discovered", whether by any recipe use or by the specific recipe use defined in [reqSpell](#reqspell)

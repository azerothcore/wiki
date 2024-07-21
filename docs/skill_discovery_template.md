# skill\_discovery\_template

[<-Back-to:World](database-world)

**The \`skill\_discovery\_template\` table**

This table controls the so called "discovery" system of learning spells. This system is solely ![(question)](images/icons/emoticons/help_16.png){.emoticon .emoticon-question} used by the alchemy profession and controls the chance for a player to "discover" another recipe while creating items with other recipes.

**Table Structure**

| Field              | Type      | Attributes | Key | Null | Default | Extra | Comment                           |
| ------------------ | --------- | ---------- | --- | ---- | ------- | ----- | --------------------------------- |
| [spellId][1]       | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | SpellId of the discoverable spell |
| [reqSpell][2]      | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | spell requirement                 |
| [reqSkillValue][3] | SMALLINT  | UNSIGNED   |     | NO   | 0       |       | skill points requirement          |
| [chance][4]        | FLOAT     | SIGNED     |     | NO   | 0       |       | chance to discover                |

[1]: #spellid
[2]: #reqspell
[3]: #reqskillvalue
[4]: #chance

**Description of the fields**

### spellId

The recipe spell ID that has a chance to be automatically discovered. See Spell.dbc

### reqSpell

If nonzero, this field controls what spell must be specifically used to trigger the discovery (eg, spell 41458 will only be discovered while using spell 28575). If it is zero, then any recipe use can trigger the discovery. See Spell.dbc

### reqSkillValue

`field-no-description|3`

### chance

The chance, in percent, that a recipe has of being automatically "discovered", whether by any recipe use or by the specific recipe use defined in [reqSpell](#skill_discovery_template-reqSpell)

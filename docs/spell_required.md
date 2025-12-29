# spell\_required

[<-Back-to:World](database-world)

**The \`spell\_required\` table**

Table used to add restrictions for learning spells from trainer. Player can't learn spell 'spell\_id' till he learns 'req\_spell', when he loses 'req\_spell' 'spell\_id' will be lost too. Table is used also for profession specialisations as specialisations require profession of certain rank to learn.

**Table Structure**

| Field          | Type      | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [spell_id][1]  | MEDIUMINT | SIGNED     | PRI | NO   | 0       |       |         |
| [req_spell][2] | MEDIUMINT | SIGNED     | PRI | NO   | 0       |       |         |

[1]: #spellid
[2]: #reqspell

**Description of the fields**

### spell\_id

Spell ID from [Spell.dbc](spell), which require knowing \`req\_spell\` to learn from trainer.

### req\_spell

Spell ID from [Spell.dbc](spell), which is required to be known before \`spell\_id\` can be learned from trainer.

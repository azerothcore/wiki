# spell\_bonus\_data

[<-Back-to:World](database-world)

**The \`spell\_bonus\_data\` table**

Table used for storing custom damage/healing bonus coefficients.

**Table: spell\_bonus\_data's Structure**

| Field                        | Type         |          | Null | Key | Default | Extra | Comment |
| :--------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [entry](#entry)              | INT          | UNSIGNED | NO   | PRI | 0       |       |         |
| [direct_bonus](#directbonus) | FLOAT        |          | NO   |     | 0       |       |         |
| [dot_bonus](#dotbonus)       | FLOAT        |          | NO   |     | 0       |       |         |
| [ap_bonus](#apbonus)         | FLOAT        |          | NO   |     | 0       |       |         |
| [ap_dot_bonus](#apdotbonus)  | FLOAT        |          | NO   |     | 0       |       |         |
| [comments](#comments)        | VARCHAR(255) |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### entry

Spell ID. See Spell.dbc.

Only the first rank of the spell needs data if spell exists in Spell\_ranks and coefficients are same for each rank.

### direct\_bonus

Direct spell power damage.

If < 0

Calculate default spell power coefficient.

If = 0

Don't apply any spell power coefficient. (Don't scale damage with spellpower)

If > 0

Use this as new spell power coefficient.

### dot\_bonus

Spell damage over time.

If < 0
Calculate default spell power coefficient.
If = 0
Don't apply any spell power coefficient. (Don't scale damage with spellpower)
If > 0
Use this as new spell power coefficient.

### ap\_bonus

Direct Melee/Ranged damage.

If < 0

Calculate default attack power coefficient.

If = 0

Don't apply any attack power coefficient. (Don't scale damage with attack power)

If > 0

Use this as new attack power coefficient.

### ap\_dot\_bonus

Melee/Ranged damage over time.

If < 0

Calculate default attack power coefficient.

If = 0

Don't apply any attack power coefficient. (Don't scale damage with attack power)

If > 0

Use this as new attack power coefficient.

### comments

Comment as why it has such values and name of the spell.

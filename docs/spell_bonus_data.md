# spell\_bonus\_data

[<-Back-to:World](database-world)

**The \`spell\_bonus\_data\` table**

Table used for storing custom damage/healing bonus coefficients.

**Table Structure**

| Field             | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]        | MEDIUMINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [direct_bonus][2] | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [dot_bonus][3]    | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [ap_bonus][4]     | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [ap_dot_bonus][5] | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [comments][6]     | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |

[1]: #entry
[2]: #direct_bonus
[3]: #dot_bonus
[4]: #ap_bonus
[5]: #ap_dot_bonus
[6]: #comments

**Description of the fields**

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

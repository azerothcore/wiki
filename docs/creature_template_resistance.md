# creature\_template\_resistance

[<-Back-to:World](database-world)

**The \`creature\_template\_resistance\` table**

Holds the resistance of a creature template to each spell school.

**Table: creature\_template\_resistance's Structure**

| Field                           | Type     |          | Null | Key | Default | Extra | Comment |
| :------------------------------ | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [CreatureID](#creatureid)       | INT      | UNSIGNED | NO   | PRI |         |       |         |
| [School](#school)               | TINYINT  | UNSIGNED | NO   | PRI |         |       |         |
| [Resistance](#resistance)       | SMALLINT |          | YES  |     | NULL    |       |         |
| [VerifiedBuild](#verifiedbuild) | INT      |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### CreatureID

Creature entry from [creature_template.entry](creature_template#entry).

### School

Value must be within this range. If above or under the SQL will fail on `creature_template_resistance_chk_1`.

| Value | Name                |
| :---- | :------------------ |
| 1     | SPELL_SCHOOL_HOLY   |
| 2     | SPELL_SCHOOL_FIRE   |
| 3     | SPELL_SCHOOL_NATURE |
| 4     | SPELL_SCHOOL_FROST  |
| 5     | SPELL_SCHOOL_SHADOW |
| 6     | SPELL_SCHOOL_ARCANE |

### Resistance

Resistance value.

### VerifiedBuild

This field was used to determine whether a template has been verified from WDB files.

If value is 0 then it has not been parsed yet.

If value is above 0 then it has been parsed with WDB files from that specific client build.

If value is -1 then it is just a place holder until proper data are found on WDBs.

If value is -Client Build then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.

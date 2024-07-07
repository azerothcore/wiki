# creature_template_resistance

[<-Back-to:World](database-world)

**The \`creature_template_resistance\` table**

**Table Structure**

| Field              | Type      | Attribute | Key | Null | Default | Extra | Comment |
| ------------------ | --------- | --------- | --- | ---- | ------- | ----- | ------- |
| [CreatureID][1]    | MEDIUMINT | UNSIGNED  | PRI | NO   |         |       |         |
| [School][2]        | TINYINT   | UNSIGNED  | PRI | NO   |         |       |         |
| [Resistance][3]    | SMALLINT  | SIGNED    |     | YES  | NULL    |       |         |
| [VerifiedBuild][4] | SMALLINT  | SIGNED    |     | YES  | 0       |       |         |

[1]: #creatureid
[2]: #school
[3]: #resistance
[4]: #verifiedbuild

**Description of the fields**

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

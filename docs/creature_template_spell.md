# creature_template_spell

[<-Back-to:World](database-world)

**The \`creature_template_spell\` table**

**Table Structure**

| Field              | Type      | Attribute | Key  | Null | Default | Extra | Comment |
| ------------------ | --------- | --------- | ---- | ---- | ------- | ----- | ------- |
| [CreatureID][1]    | MEDIUMINT | UNSIGNED  | PRI  | NO   |         |       |         |
| [Index][2]         | TINYINT   | UNSIGNED  | PRI  | NO   | 0       |       |         |
| [Spell][3]         | MEDIUMINT | UNSIGNED  |      | YES  | Null    |       |         |
| [VerifiedBuild][4] | SMALLINT  | SIGNED    |      | YES  | 0       |       |         |

[1]: #creatureid
[2]: #index
[3]: #spell
[4]: #verifiedbuild

**Description of the fields**

### CreatureID

Creature entry from [creature_template.entry](creature_template#entry).

### Index

Value must be within this range. If above or under the SQL will fail on `creature_template_spell_chk_1`.

Index 0 - 7.

Spell position on actionbar for vehicle creatures.

### Spell

Spell ID that can be used for Mind Control of a creature.

### VerifiedBuild

This field was used to determine whether a template has been verified from WDB files.

If value is 0 then it has not been parsed yet.

If value is above 0 then it has been parsed with WDB files from that specific client build.

If value is -1 then it is just a place holder until proper data are found on WDBs.

If value is -Client Build then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.

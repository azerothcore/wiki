# creature\_template\_spell

[<-Back-to:World](database-world)

**The \`creature\_template\_spell\` table**

Holds the spells assigned to a creature template. They are used by the creature's AI, or by a player who controls the creature.

**Table: creature\_template\_spell's Structure**

| Field                           | Type    |          | Null | Key | Default | Extra | Comment |
| :------------------------------ | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [CreatureID](#creatureid)       | INT     | UNSIGNED | NO   | PRI |         |       |         |
| [Index](#index)                 | TINYINT | UNSIGNED | NO   | PRI | 0       |       |         |
| [Spell](#spell)                 | INT     | UNSIGNED | YES  |     | NULL    |       |         |
| [VerifiedBuild](#verifiedbuild) | INT     |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

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

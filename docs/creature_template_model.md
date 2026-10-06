# creature\_template\_model

[<-Back-to:World](database-world)

**The \`creature\_template\_model\` table**

This table describes which model is assigned to a specific creature.

**Table: creature\_template\_model's Structure**

| Field                                   | Type     |          | Null | Key | Default | Extra | Comment |
| :-------------------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [CreatureID](#creatureid)               | INT      | UNSIGNED | NO   | PRI |         |       |         |
| [Idx](#idx)                             | SMALLINT | UNSIGNED | NO   | PRI | 0       |       |         |
| [CreatureDisplayID](#creaturedisplayid) | INT      | UNSIGNED | NO   |     |         |       |         |
| [DisplayScale](#displayscale)           | FLOAT    |          | NO   |     | 1       |       |         |
| [Probability](#probability)             | FLOAT    |          | NO   |     | 0       |       |         |
| [VerifiedBuild](#verifiedbuild)         | INT      |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### CreatureID

[creature_template.entry](creature_template#entry)

### Idx

Index 0-3.

### CreatureDisplayID

DisplayID from CreatureDisplayInfo.dbc.

### DisplayScale

Modifies the model scale.

### Probability

0-1

If it exceeds or fall short of 1 the core will correct it during startup to equal 1.

### VerifiedBuild

This field was used to determine whether a template has been verified from WDB files.

If value is 0 then it has not been parsed yet.

If value is above 0 then it has been parsed with WDB files from that specific client build.

If value is -1 then it is just a place holder until proper data are found on WDBs.

If value is [client build](realmlist#gamebuild) then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.

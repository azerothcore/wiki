# creature_template_model

[<-Back-to:World](database-world)

**The `creature_template_model` table**

This table describes which model is assigned to a specific creature.

**Table Structure**

| Field                  | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [CreatureID][1]        | INT      | UNSIGNED   | PRI | NO   |         |       |         |
| [Idx][2]               | SMALLINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [CreatureDisplayID][3] | INT      | UNSIGNED   |     | NO   |         |       |         |
| [DisplayScale][4]      | FLOAT    |            |     | NO   | 1       |       |         |
| [Probability][5]       | FLOAT    |            |     | NO   | 0       |       |         |
| [VerifiedBuild][6]     | SMALLINT |            |     | YES  |         |       |         |

[1]: #creatureid
[2]: #idx
[3]: #creaturedisplayid
[4]: #displayscale
[5]: #probability
[6]: #verifiedbuild

**Description of the fields**

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

# gameobject_questitem

[<-Back-to:World](database-world)

**The \`gameobject_questitem\` table**

**Table Structure**

| Field                               | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [GameObjectEntry](#gameobjectentry) | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Idx](#idx)                         | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [ItemId](#itemid)                   | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [VerifiedBuild](#verifiedbuild)     | INT  | UNSIGNED   |     | YES  | NULL    |       |         |

**Description of the fields**

### GameObjectEntry

[gameobject_template.entry](gameobject_template#entry).

### Idx

Index 0-3

### ItemId

[item_template.entry](item_template#entry).

### VerifiedBuild

This field was used to determine whether the data has been verified from WDB files.

If value is 0 then it has not been parsed yet.

If value is above 0 then it has been parsed with WDB files from that specific client build.

If value is -1 then it is just a place holder until proper data are found on WDBs.

If value is -Client Build then it was parsed with WDB files from that specific [client build](realmlist#gamebuild) and manually edited later for some special necessity.

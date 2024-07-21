# creature_questitem

[<-Back-to:World](database-world)

**The \`creature_questitem\` table**

Holds NPC quest ender relations on which NPCs finishes which quests.
| Field                           | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [CreatureEntry](#creatureEntry) | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Idx](#idx)                     | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [ItemId](#itemid)               | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [VerifiedBuild](#verifiedbuild) | INT  |            |     | YES  | NULL    |       |         |

**Description of the fields**

### CreatureEntry

[creature_template.entry](creature_template#entry).

### Idx

Index 0-3

### ItemId

[item_template.entry](item_template#entry).

### VerifiedBuild

This field is used to determine if the data originates from verified sniffs.

If value is 0 then it has not been parsed yet or it has been inherited from an older DB or another Core.

If value is above 0 then it has been parsed with sniffs from that specific client build.

If value is -Client Build then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.

# trainer_spell

[<-Back-to:World](database-world)

**The \`trainer_spell\` table**

This table contains the trainer spell entries.

**Table Structure**

| Field                           | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [TrainerId](#trainerid)         | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [SpellId](#spellid)             | INT     | UNSIGNED   | PRI | NO   | 2       |       |         |
| [MoneyCost](#moneycost)         | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqSkillLine](#reqskillline)   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqSkillRank](#reqskillrank)   | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqAbility1](#reqability)      | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqAbility2](#reqability)      | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqAbility3](#reqability)      | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [ReqLevel](#reqlevel)           | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |
| [VerifiedBuild](#verifiedbuild) | INT     |            |     | YES  | 0       |       |         |

**Description of the fields**

### TrainerId

[trainer.Id](trainer#id).

### SpellId

The Spell ID to teach.

### MoneyCost

The cost in copper to learn the spell.

### ReqSkillLine

The [SkillLine ID](skillline) the player is required to know to learn the spell.

| ID  | Name           |
| --- | -------------- |
| 129 | First Aid      |
| 164 | Blacksmithing  |
| 165 | Leatherworking |
| 171 | Alchemy        |
| 182 | Herbalism      |
| 185 | Cooking        |
| 186 | Mining         |
| 197 | Tailoring      |
| 202 | Engineering    |
| 333 | Enchanting     |
| 356 | Fishing        |
| 393 | Skinning       |
| 633 | Lockpicking    |
| 755 | Jewelcrafting  |
| 773 | Inscription    |
| 776 | Runeforging    |

### ReqSkillRank

The minimum level of skill points in [ReqSkillLine](#reqskillline) required to learn the spell.

### ReqAbility

Required Spell ID the player needs to learn the spell.

### ReqLevel

Required player level to learn this spell.

### VerifiedBuild

This field is used to determine if this gameobject originates from verified sniffs.

If value is 0 then it has not been parsed yet or it has been inherited from an older DB or another Core.

If value is above 0 then it has been parsed with sniffs from that specific client build.

If value is -Client Build then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.

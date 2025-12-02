# trainer_spell

[<-Back-to:World](database-world)

**The \`trainer_spell\` table**

This table contains all the trainer spell entries.

**Table Structure**

| Field                           | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ------- | ---------- | :-: | :--: | ------- | ----- | ------- |
| [TrainerId](#trainerid)         | int     | unsigned   | PRI |  NO  | 0       |       |         |
| [SpellId](#spellid)             | int     | unsigned   | PRI |  NO  | 0       |       |         |
| [MoneyCost](#moneycost)         | int     | unsigned   |     |  NO  | 0       |       |         |
| [ReqSkillLine](#reqskillline)   | int     | unsigned   |     |  NO  | 0       |       |         |
| [ReqSkillRank](#reqskillrank)   | int     | unsigned   |     |  NO  | 0       |       |         |
| [ReqAbility1](#reqability1-3)   | int     | unsigned   |     |  NO  | 0       |       |         |
| [ReqAbility2](#reqability1-3)   | int     | unsigned   |     |  NO  | 0       |       |         |
| [ReqAbility3](#reqability1-3)   | int     | unsigned   |     |  NO  | 0       |       |         |
| [ReqLevel](#reqlevel)           | tinyint | unsigned   |     |  NO  | 0       |       |         |
| [VerifiedBuild](#verifiedbuild) | int     | signed     |     | YES  | 0       |       |         |

**Description of fields**

### TrainerId

References [trainer.id](trainer#id).

### SpellId

The [Spell ID](#spell) being taught.

### MoneyCost

The cost in copper for the spell being taught.

### ReqSkillLine

The [SkillLine ID](skillline#content) the player is required to have.

[SkillLine](skillline) excerpt
| ID | Name |
|----|------|
| 129 | First Aid |
| 164 | Blacksmithing |
| 165 | Leatherworking |
| 171 | Alchemy |
| 182 | Herbalism |
| 185 | Cooking |
| 186 | Mining |
| 197 | Tailoring |
| 202 | Engineering |
| 333 | Enchanting |
| 356 | Fishing |
| 393 | Skinning |
| 633 | Lockpicking |
| 755 | Jewelcrafting |
| 773 | Inscription |
| 776 | Runeforging |
{.dense}

### ReqSkillRank

The minimum level of skill points in **ReqSkillLine** required to be taught the spell.

### ReqAbility\[1-3\]

A [Spell ID](#spell) the player is required to know.

### ReqLevel

The required player level to learn this spell.

### VerifiedBuild

Used by AzerothCore to indicate whether this entry was verified against WDB files.

- `0` = not parsed
- `>0` = parsed with WDB files from that client build
- `-1` = placeholder until proper data is found
- -[Client Build](realmlist#gamebuild) = parsed with WDB files from that specific client build and manually edited for special reasons

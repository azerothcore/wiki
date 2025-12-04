# creature_default_trainer

[<-Back-to:World](database-world)

**The \`creature_default_trainer\` table**

This table maps creatures to a default trainer type. Each row associates a creature entry with a trainer template ID.

**Table Structure**

| Field                     | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------- | ---- | ---------- | :-: | :--: | ------- | ----- | ------- |
| [CreatureId](#creatureid) | int  | unsigned   | PRI |  NO  |         |       |         |
| [TrainerId](#trainerid)   | int  | unsigned   |     |  NO  | 0       |       |         |

**Description of fields**

### CreatureId

References a [creature entry](creature_template).

### TrainerId

References a [trainer Id](trainer#id).

| ID  | Comment               |
| --- | --------------------- |
| 1   | Trainer Warrior       |
| 3   | Trainer Paladin       |
| 7   | Trainer Hunter        |
| 9   | Trainer Rogue         |
| 11  | Trainer Priest        |
| 13  | Trainer Death Knight  |
| 14  | Trainer Shaman        |
| 16  | Trainer Mage          |
| 31  | Trainer Warlock       |
| 33  | Trainer Druid         |
| 36  | Trainer Mount and Fly |

{.dense}

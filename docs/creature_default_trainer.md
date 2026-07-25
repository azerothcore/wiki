# creature_default_trainer

[<-Back-to:World](database-world)

**The \`creature_default_trainer\` table**

**Table Structure**

| Field                     | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [CreatureId](#creatureid) | INT  | UNSIGNED   | PRI | NO   |         |       |         |
| [TrainerId](#trainerid)   | INT  | UNSIGNED   |     | NO   | 0       |       |         |

**Description of the fields**

### CreatureId

[creature_template.entry](creature_template#entry).

### TrainerId

[trainer.Id](trainer#id).

| ID  | Comment              |
| --- | -------------------- |
| 1   | Warrior trainer      |
| 3   | Paladin trainer      |
| 7   | Hunter trainer       |
| 9   | Rogue trainer        |
| 11  | Priest trainer       |
| 13  | Death Knight trainer |
| 14  | Shaman trainer       |
| 16  | Mage trainer         |
| 31  | Warlock trainer      |
| 33  | Druid trainer        |
| 36  | Mount & Fly trainer  |

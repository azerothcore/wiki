# creature\_default\_trainer

[<-Back-to:World](database-world)

**The \`creature\_default\_trainer\` table**

Links a creature to the trainer in the [trainer](trainer) table that it uses.

**Table: creature\_default\_trainer's Structure**

| Field                     | Type |          | Null | Key | Default | Extra | Comment |
| :------------------------ | :--- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [CreatureId](#creatureid) | INT  | UNSIGNED | NO   | PRI |         |       |         |
| [TrainerId](#trainerid)   | INT  | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

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

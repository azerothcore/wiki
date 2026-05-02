# trainer

[<-Back-to:World](database-world)

**The \`trainer\` table**

This table contains the unique trainer template.

**Table Structure**

| Field                           | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Id](#id)                       | INT        | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Type](#type)                   | TINYINT    | UNSIGNED   |     | NO   | 2       |       |         |
| [Requirement](#requirement)     | MEDIUMINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [Greeting](#greeting)           | MEDIUMTEXT |            |     | NO   |         |       |         |
| [VerifiedBuild](#verifiedbuild) | INT        |            |     | YES  | 0       |       |         |

**Description of the fields**

### ID

Unique Trainer ID

### Type

| Type | Description |
| ---- | ----------- |
| 0    | Class       |
| 1    | Mount       |
| 2    | Tradeskill  |
| 3    | Pet         |

### Requirement

Keep 0 for no requirement.

| Type       | Requirement                              | Description                                             |
| ---------- | ---------------------------------------- | ------------------------------------------------------- |
| Class      | [ChrClasses.Content](chrclasses#content) | Player need to be this class to train from the trainer. |
| Mount      | [ChrRaces](chrraces#content)             | Player need to be this race to train from the trainer.  |
| TradeSkill | Spell ID                                 | Player must know this spell to train from this trainer. |
| Pet        | [ChrClasses.Content](chrclasses#content) | Player need to be this class to train from the trainer. |

### Greeting

The text shown when the trainer window is opened.

This is not gossip text.

### VerifiedBuild

This field is used to determine if this gameobject originates from verified sniffs.

If value is 0 then it has not been parsed yet or it has been inherited from an older DB or another Core.

If value is above 0 then it has been parsed with sniffs from that specific client build.

If value is -Client Build then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.

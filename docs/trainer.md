# trainer

[<-Back-to:World](database-world)

**The \`trainer\` table**

This table lists trainer templates (a trainer identifier and metadata). Spells a trainer can teach are stored in the related [trainer_spell](trainer_spell) table.

**Table Structure**

| Field                           | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ---------- | ---------- | :-: | :--: | ------- | ----- | ------- |
| [Id](#id)                       | INT        | unsigned   | PRI |  NO  | 0       |       |         |
| [Type](#type)                   | TINYINT    | unsigned   |     |  NO  | 2       |       |         |
| [Requirement](#requirement)     | MEDIUMINT  | unsigned   |     |  NO  | 0       |       |         |
| [Greeting](#greeting)           | MEDIUMTEXT |            |     | YES  | NULL    |       |         |
| [VerifiedBuild](#verifiedbuild) | INT        | signed     |     | YES  | NULL    |       |         |

**Description of fields**

### Id

Unique trainer ID. This ID is referenced by the [trainer_spell](trainer_spell) table to link spells to a trainer template.

### Type

Trainer type determines the meaning of **Requirement** (use `0` for no requirement).

#### Type::Class (0)

Requirement is a [ChrClass ID](chrclasses#content) or `0`.
| Requirement | Description |
|-------------|-------------|
| 1 | Warrior |
| 2 | Paladin |
| 3 | Hunter |
| 4 | Rogue |
| 5 | Priest |
| 6 | Death Knight |
| 7 | Shaman |
| 8 | Mage |
| 9 | Warlock |
| 11 | Druid |

#### Type::Mount (1)

Requirement is a [ChrRace ID](chrraces#content) or `0`.
| Requirement | Description |
|-------------|-------------|
| 1 | Human |
| 2 | Orc |
| 3 | Dwarf |
| 4 | Night Elf |
| 5 | Undead |
| 6 | Tauren |
| 7 | Gnome |
| 8 | Troll |
| 10 | Blood Elf |
| 11 | Draenei |

#### Type::Tradeskill (2)

Requirement is a [Spell ID](spell) or `0`. The player must know this spell to learn from this trainer.

#### Type::Pet (3)

Requirement is a [ChrClass ID](chrclasses#content) or `0`.

### Greeting

Text shown at the top of the trainer window when opened.

{% include note.html content="This is not the gossip text." %}

### VerifiedBuild

Used by AzerothCore to indicate whether this template was verified against WDB files.

- `0` = not parsed
- `>0` = parsed with WDB files from that client build
- `-1` = placeholder until proper data is found
- -[Client Build](realmlist#gamebuild) = parsed with WDB files from that specific client build and manually edited for special reasons

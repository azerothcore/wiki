# creature\_text\_option\_sets

[<-Back-to:World](database-world)

**The \`creature\_text\_option\_sets\` table**

This table defines reusable option rulesets for creature text groups. Each ruleset controls cooldown, trigger chance, and player-only filtering for `SendChat()`. Rulesets are assigned to specific (CreatureID, GroupID) pairs via the [creature\_text\_options](creature_text_options) table.

**Table: creature\_text\_option\_sets's Structure**

| Field                           | Type         |          | Null | Key | Default | Extra | Comment                                       |
| :------------------------------ | :----------- | :------- | :--: | :-: | :-----: | :---: | :-------------------------------------------- |
| [SetID](#setid)                 | TINYINT      | UNSIGNED | NO   | PRI |         |       |                                               |
| [Cooldown](#cooldown)           | INT          | UNSIGNED | NO   |     | 0       |       | Group cooldown in ms before it can fire again |
| [TriggerChance](#triggerchance) | TINYINT      | UNSIGNED | NO   |     | 100     |       | 0-100 pct chance to fire at all               |
| [PlayerOnly](#playeronly)       | TINYINT      | UNSIGNED | NO   |     | 0       |       | Only fire if target is a player               |
| [comment](#comment)             | VARCHAR(255) |          | YES  |     | ''      |       |                                               |

**Description of the table's fields**

### SetID

Unique identifier for this option ruleset. Referenced by [creature\_text\_options.OptionSetID](creature_text_options#optionsetid).

### Cooldown

The minimum time in milliseconds that must pass before the same text group can fire again on a given creature. Set to `0` to disable cooldown enforcement.

### TriggerChance

A percentage value from `0` to `100` that represents the chance the text group will be triggered at all. A value of `100` means the text always fires when called; a value of `30` means it fires approximately 30% of the time.

### PlayerOnly

When set to `1`, the text group will only fire if the target that triggered it is a player. When set to `0`, the text will fire regardless of target type (players, pets, guardians, etc.).

### comment

An optional human-readable label for this ruleset.

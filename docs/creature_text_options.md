# creature\_text\_options

[<-Back-to:World](database-world)

**The \`creature\_text\_options\` table**

This table assigns a reusable option ruleset (defined in [creature\_text\_option\_sets](creature_text_option_sets)) to a specific (CreatureID, GroupID) pair from [creature\_text](creature_text). This enables data-driven control of cooldown, trigger chance, and player-only filtering for `SendChat()` calls without requiring per-script boilerplate.

When `SendChat()` is called for a creature text group, the engine automatically:
1. Checks whether the group is on cooldown (if `Cooldown > 0`).
2. Rolls against `TriggerChance` to decide whether the text fires.
3. Checks whether the target is a player (if `PlayerOnly = 1`).

If any check fails, the text is silently skipped. If all checks pass, the text fires and the cooldown timer is started.

## Structure

| Field                  | Type    | Attributes | Key | Null | Default | Extra | Comment |
|------------------------|---------|------------|-----|------|---------|-------|---------|
| [CreatureID][1]        | INT     | UNSIGNED   | PRI | NO   |         |       |         |
| [GroupID][2]           | TINYINT | UNSIGNED   | PRI | NO   |         |       |         |
| [OptionSetID][3]       | TINYINT | UNSIGNED   |     | NO   |         |       |         |

[1]: #creatureid
[2]: #groupid
[3]: #optionsetid

## Description of the fields

### CreatureID

The entry of the creature from [creature\_template.entry](creature_template#entry) to which this option assignment applies.

### GroupID

The text group ID from [creature\_text.GroupID](creature_text#groupid) to which this option assignment applies.

### OptionSetID

The ID of the ruleset from [creature\_text\_option\_sets.SetID](creature_text_option_sets#setid) that defines the cooldown, trigger chance, and player-only behaviour for this (CreatureID, GroupID) pair.

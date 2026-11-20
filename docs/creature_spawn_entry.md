# creature_spawn_entry

[<-Back-to:World](database-world)

**The `creature_spawn_entry` table**

Lists the entries a single creature spawn point can spawn as, each with a relative weight. It works like [creature_template_model](creature_template_model), which lists the displays of a template, but it is keyed by the spawn ([creature.guid](creature#guid)), not by the template.

A spawn with rows here rolls among them every time it spawns or respawns. The rows are the spawn's **whole** roll, so its own [creature.id](creature#id) has to be one of them: if it is missing, the spawn never appears as that entry and the server logs an error at startup. A spawn with no rows here always uses its own `id`.

There is no limit on the number of entries. The same table exists for gameobjects: [gameobject_spawn_entry](gameobject_spawn_entry).

If the spawn belongs to a [spawn group](spawn_group) that has rows in [spawn_group_entry](spawn_group_entry), the group sets the entry and the rows here are ignored.

**Table Structure**

| Field                           | Type    | Attributes | Key | Null | Default | Extra | Comment                                 |
| ------------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | --------------------------------------- |
| [guid](#guid)                   | INT     | UNSIGNED   | PRI | NO   |         |       | creature.guid                             |
| [Idx](#idx)                     | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |                                         |
| [entry](#entry)                 | INT     | UNSIGNED   | MUL | NO   |         |       | creature_template.entry                        |
| [Probability](#probability)     | FLOAT   |            |     | NO   | 1       |       | Relative weight; all 0 means equal odds |
| [VerifiedBuild](#verifiedbuild) | INT     |            |     | YES  | NULL    |       |                                         |

The pair (`guid`, `entry`) is unique: an entry can be listed only once per spawn.

**Description of the fields**

### guid

The spawn this row belongs to. See [creature.guid](creature#guid).

### Idx

Position of the row in the spawn's list, starting at 0. It only orders the rows; it has no effect on the odds. By convention the spawn's own `id` is at `Idx` 0.

### entry

A template the spawn can appear as. See [creature_template.entry](creature_template#entry).

The entry must exist, and must not be a difficulty entry of another template (`difficulty_entry_1` to `difficulty_entry_3`). The equipment set of the spawn ([creature.equipment_id](creature#equipment_id)) should exist for every listed entry.

### Probability

The relative weight of this entry. The chance of an entry is its weight divided by the sum of the weights of all rows of the spawn, so the values do not have to add up to 1 or 100.

- Three rows with weights `1`, `1`, `1` each have a 1 in 3 chance.
- Two rows with weights `3` and `1` have a 75% and a 25% chance.
- If every row of a spawn has weight `0`, all its entries have equal odds.

Negative values are not allowed.

### VerifiedBuild

The client build of the sniff in which this entry was seen on this spawn point.

- `NULL` or `0`: this entry was not confirmed by a sniff on this spawn point.
- Above `0`: the client build that showed it.

# spawn\_group\_entry

[<-Back-to:World](database-world)

**The \`spawn\_group\_entry\` table**

Lets a [spawn group](spawn_group) set the entries of its members, with limits on how many members can hold each entry. It is meant for packs whose composition varies but follows rules, for example "3 or 4 snakes, at least one of each kind". The mechanism follows the spawn groups of cMaNGOS.

A group with rows here decides the entry of each of its members. The members' own [creature.id](creature#id) / [gameobject.id](gameobject#id), and any rows they have in [creature\_spawn\_entry](creature_spawn_entry) / [gameobject\_spawn\_entry](gameobject_spawn_entry), are ignored.

**How a group is rolled**

1. The first time a member of the group spawns on a map (or in an instance), the whole group is rolled at once, in random member order.
2. A member whose [spawn\_group.chance](spawn_group#chance) fails does not spawn and takes no entry.
3. For each remaining member, an entry is picked:
   - first, at random among the entries that have not reached their [minCount](#mincount) yet;
   - then by [chance](#chance), among the entries that are still under their [maxCount](#maxcount);
   - then at equal odds among the entries with `chance` 0 that are still under their `maxCount`.
4. If no entry is left for a member, it does not spawn.
5. When a member respawns, only that member is rolled again, within what the other members leave open. The others keep their entry.

The roll is kept in memory per map. An instance rolls again when it is created; a continent rolls again after a server restart.

**Table Structure**

| Field                   | Type    | Attributes | Key | Null | Default | Extra | Comment                                                |
| ----------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------------------------------------------------------ |
| [groupId](#groupid)     | INT     | UNSIGNED   | PRI | NO   |         |       | spawn\_group\_template.groupId                         |
| [spawnType](#spawntype) | TINYINT | UNSIGNED   | PRI | NO   |         |       | 0 = creature, 1 = gameobject                           |
| [entry](#entry)         | INT     | UNSIGNED   | PRI | NO   |         |       | creature\_template.entry or gameobject\_template.entry |
| [minCount](#mincount)   | INT     | UNSIGNED   |     | NO   | 0       |       | Members that take this entry before any random pick    |
| [maxCount](#maxcount)   | INT     | UNSIGNED   |     | NO   | 0       |       | Members that can hold this entry at once, 0 = no limit |
| [chance](#chance)       | FLOAT   |            |     | NO   | 0       |       | Percent, 0 = equal odds among the entries left         |

**Description of the fields**

### groupId

The group these limits apply to. It must exist in [spawn\_group\_template](spawn_group_template) and must not be a system group (0 or 1).

### spawnType

Which members of the group the row applies to:

| Value | Type       |
| ----- | ---------- |
| 0     | Creature   |
| 1     | GameObject |

### entry

An entry the members of that type can spawn as. See [creature\_template.entry](creature_template#entry) or [gameobject\_template.entry](gameobject_template#entry).

### minCount

How many members must hold this entry. Entries below their minimum are handed out before any random pick.

The sum of `minCount` over a group's rows should not be larger than its number of members; the server logs an error at startup when it is.

### maxCount

How many members can hold this entry at the same time. `0` means no limit. A value below `minCount` is raised to `minCount` at startup.

### chance

The percent chance (0 to 100) that a member takes this entry, once all minimums are filled. Entries with `chance` 0 share what is left at equal odds.

**Example**

The snake pack at the entrance of Zul'Gurub has four spawn points and two possible entries. It always has at least one Razzashi Serpent and one Razzashi Adder, and one of its points is empty half of the time:

```sql
INSERT INTO `spawn_group_template` (`groupId`, `groupName`, `groupFlags`) VALUES
(105, 'Zul''Gurub - Entrance Snake Pack', 0);

INSERT INTO `spawn_group` (`groupId`, `spawnType`, `spawnId`, `chance`) VALUES
(105, 0, 86963, 0),
(105, 0, 86964, 50),
(105, 0, 86965, 0),
(105, 0, 86966, 0);

INSERT INTO `spawn_group_entry` (`groupId`, `spawnType`, `entry`, `minCount`, `maxCount`, `chance`) VALUES
(105, 0, 11371, 1, 0, 0), -- Razzashi Serpent
(105, 0, 11372, 1, 0, 0); -- Razzashi Adder
```

Before this table existed, the same pack needed 20 pools and 72 creature rows, one pool per possible arrangement.

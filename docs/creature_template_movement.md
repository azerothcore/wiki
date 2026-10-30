# creature\_template\_movement

[<-Back-to:World](database-world)

This table contains the description of creatures movements, where the creature can move and attack.

This table can be overriden by \`creature_movement_override\`

**Table: creature\_template\_movement's Structure**

| Field                                           | Type    |          | Null | Key | Default | Extra | Comment                                                                                  |
| :---------------------------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :--------------------------------------------------------------------------------------- |
| [CreatureId](#creatureid)                       | INT     | UNSIGNED | NO   | PRI | 0       |       |                                                                                          |
| [Ground](#ground)                               | TINYINT | UNSIGNED | YES  |     | NULL    |       |                                                                                          |
| [Swim](#swim)                                   | TINYINT | UNSIGNED | YES  |     | NULL    |       |                                                                                          |
| [Flight](#flight)                               | TINYINT | UNSIGNED | YES  |     | NULL    |       |                                                                                          |
| [Rooted](#rooted)                               | TINYINT | UNSIGNED | YES  |     | NULL    |       |                                                                                          |
| [Chase](#chase)                                 | TINYINT | UNSIGNED | YES  |     | NULL    |       |                                                                                          |
| [Random](#random)                               | TINYINT | UNSIGNED | YES  |     | NULL    |       |                                                                                          |
| [InteractionPauseTimer](#interactionpausetimer) | INT     | UNSIGNED | YES  |     | NULL    |       | Time (in milliseconds) during which creature will not move after interaction with player |

**Description of the table's fields**

### CreatureId

This is the [creature\_template.entry](creature_template#entry) to which the script is linked to.

### Ground

| State | Value |
| ----- | ----- |
| None  | 0     |
| Run   | 1     |
| Hover | 2     |

### Swim

| State | Value |
| ----- | ----- |
| None  | 0     |
| Swim  | 1     |

### Flight

| State          | Value |
| -------------- | ----- |
| None           | 0     |
| DisableGravity | 1     |
| CanFly         | 2     |

### Rooted

| State  | Value |
| ------ | ----- |
| None   | 0     |
| Rooted | 1     |

Notice:

Rooted creature that doesn't fall once dead must use \`Ground\`=1, \`Swim\`=0, \`Flight\`=0, \`Rooted\`=1 (\`Swim\`=1 if above water)

Rooted creature that falls once dead must use \`Ground\`=0, \`Swim\`=0, \`Flight\`=1, \`Rooted\`=1

### Chase

| State      | Value |
| ---------- | ----- |
| Run        | 0     |
| CanWalk    | 1     |
| AlwaysWalk | 2     |

### Random

| State     | Value |
| --------- | ----- |
| Walk      | 0     |
| CanRun    | 1     |
| AlwaysRun | 2     |

### InteractionPauseTimer

Time (in milliseconds) during which creature will not move after interaction with player.

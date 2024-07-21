# creature_template_movement

[<-Back-to:World](database-world)

This table contains the description of creatures movements, where the creature can move and attack.

This table can be overriden by \`creature_movement_override\`

**Table Structure**

| Field                      | Type    | Attributes | Key | Null | Default | Extra | Comment |
| -------------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [CreatureId][1]            | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Ground][2]                | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [Swim][3]                  | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [Flight][4]                | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [Rooted][5]                | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [Chase][6]                 | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [Random][7]                | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |
| [InteractionPauseTimer][8] | TINYINT | UNSIGNED   |     | YES  | NULL    |       |         |

[1]: #creatureid
[2]: #ground
[3]: #swim
[4]: #flight
[5]: #rooted
[6]: #chase
[7]: #random
[8]: #interactionpausetimer

**Description of the fields**

#### CreatureId

This is the [creature\_template.entry](creature_template#entry) to which the script is linked to.

#### Ground

| State | Value |
| ----- | ----- |
| None  | 0     |
| Run   | 1     |
| Hover | 2     |

#### Swim

| State | Value |
| ----- | ----- |
| None  | 0     |
| Swim  | 1     |

#### Flight

| State          | Value |
| -------------- | ----- |
| None           | 0     |
| DisableGravity | 1     |
| CanFly         | 2     |

#### Rooted

| State  | Value |
| ------ | ----- |
| None   | 0     |
| Rooted | 1     |

Notice:

Rooted creature that doesn't fall once dead must use \`Ground\`=1, \`Swim\`=0, \`Flight\`=0, \`Rooted\`=1 (\`Swim\`=1 if above water)

Rooted creature that falls once dead must use \`Ground\`=0, \`Swim\`=0, \`Flight\`=1, \`Rooted\`=1

#### Chase

| State      | Value |
| ---------- | ----- |
| Run        | 0     |
| CanWalk    | 1     |
| AlwaysWalk | 2     |

#### Random

| State     | Value |
| --------- | ----- |
| Walk      | 0     |
| CanRun    | 1     |
| AlwaysRun | 2     |

#### InteractionPauseTimer

Time (in milliseconds) during which creature will not move after interaction with player.

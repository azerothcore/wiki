# creature\_template\_movement

**The \`creature\_template\_movement\` table**

This table contains the description of creatures movements, where the creature can move and attack.

**Structure**

| Field           | Type       | Attributes | Key | Null | Default | Extra | Comment |
|-----------------|------------|------------|-----|------|---------|-------|---------|
| [CreatureId][1] | int(10)    | unsigned   | PRI | NO   | 0       |       |         |
| [Ground][2]     | tinyint(3) | unsigned   |     | NO   | 0       |       |         |
| [Swim][3]       | tinyint(3) | unsigned   |     | NO   | 0       |       |         |
| [Flight][4]     | tinyint(3) | unsigned   |     | NO   | 0       |       |         |
| [Rooted][5]     | tinyint(3) | unsigned   |     | NO   | 0       |       |         |

[1]: #creatureid
[2]: #ground
[3]: #swim
[4]: #flight
[5]: #rooted

### CreatureId

This is the [creature\_template.entry](http://www.azerothcore.org/wiki/creature_template#creature_template-entry) to which the script is linked to.

### Ground

- "None"=0
- "Run"=1
- "Hover"=2

### Swim
- "None"=0
- "Swim"=1

### Flight
- "None"=0
- "DisableGravity"=1
- "CanFly" =2

### Rooted
- "None"=0
- "Rooted"=1

Notice:

Rooted creature that doesn't fall once dead must use \`Ground\`=1, \`Swim\`=0, \`Flight\`=0, \`Rooted\`=1 (\`Swim\`=1 if above water)

Rooted creature that falls once dead must use \`Ground\`=0, \`Swim\`=0, \`Flight\`=1, \`Rooted\`=1

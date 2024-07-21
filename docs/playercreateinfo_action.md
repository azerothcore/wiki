# playercreateinfo\_action

[<-Back-to:World](database-world)

**The \`playercreateinfo_action\` table**

This table holds information on what default actions a brand new character should start out with. Each race-class combination can have a different default starting setup.

**Table Structure**

| Field       | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [race][1]   | TINYINT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [class][2]  | TINYINT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [button][3] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [action][4] | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [type][5]   | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #race
[2]: #class
[3]: #button
[4]: #action
[5]: #type

**Field Descriptions**

### race

The character's [race](ChrRaces#content).

### class

The character's [class](ChrClasses#content).

### button

The ID of the slot on the action bar where the action icon will be placed.

Special bars are used for stances, auras, pets, stealth, and other similar special modes.

| Button IDs | Set (key)                          |
| ---------- | ---------------------------------- |
| 0-11       | 1 (SHIFT + 1)                      |
| 12-23      | 2 (SHIFT + 2)                      |
| 24-35      | 3 (SHIFT + 3) h1. Right Side Bar   |
| 36-47      | 4 (SHIFT + 4) Right Side Bar 2     |
| 48-59      | 5 (SHIFT + 5) h1. Bottom Right Bar |
| 60-71      | 6 (SHIFT + 6) Bottom Left Bar      |
| 72-83      | 1 SpecialA                         |
| 84-95      | 1 SpecialB                         |
| 96-107     | 1 SpecialC                         |
| 108-119    | 1 SpecialD                         |

### action

Depending on the type value, this could be either the [spell ID](Spell#id), the [item ID](item_template#entry) or macro ID.

### type

The type of action:

| ID  | Type  |
| --- | ----- |
| 0   | Spell |
| 64  | Macro |
| 128 | Item  |

# playercreateinfo\_action

[<-Back-to:World](database-world)

**The \`playercreateinfo\_action\` table**

This table holds information on what default actions a brand new character should start out with. Each race-class combination can have a different default starting setup.

**Table: playercreateinfo\_action's Structure**

| Field             | Type     |          | Null | Key | Default | Extra | Comment |
| :---------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [race](#race)     | TINYINT  | UNSIGNED | NO   | PRI | 0       |       |         |
| [class](#class)   | TINYINT  | UNSIGNED | NO   | PRI | 0       |       |         |
| [button](#button) | SMALLINT | UNSIGNED | NO   | PRI | 0       |       |         |
| [action](#action) | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [type](#type)     | SMALLINT | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### race

The character's [race](chrraces#content).

### class

The character's [class](chrclasses#content).

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

Depending on the type value, this could be either the [spell ID](spell), the [item ID](item_template#entry) or macro ID.

### type

The type of action:

| ID  | Type  |
| --- | ----- |
| 0   | Spell |
| 64  | Macro |
| 128 | Item  |

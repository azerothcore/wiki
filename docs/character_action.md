# character\_action

[<-Back-to:Characters](database-characters)

**The \`character\_action\` table**

Contains all the individual button data for each character. A button is any of the places in the GUI where you can place for example a spell, item, or macro as a shortcut.

**Table Structure**

| Field       | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]   | INT        | UNSIGNED   | PRI | NO   | 0       |       |         |
| [spec][2]   | TINYINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [button][3] | TINYINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [action][4] | INT        | UNSIGNED   |     | NO   | 0       |       |         |
| [type][5]   | TINYINT    | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #spec
[3]: #button
[4]: #action
[5]: #type

**Description of the fields**

### guid

The GUID of the character. See [characters.guid](characters#guid).

### spec

spec = 0 is the first spec, spec = 1 is the second spec.

### button

The ID of the button on the action bar where the action icon will be placed.

Special bars are used for stances, auras, pets, stealth, and other similar special modes.

**Possible values**

| Button IDs | Set (key)                          |
| ---------- | ---------------------------------- |
| 1-11       | 1 (SHIFT + 1)                      |
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

Depending on the type value, this could be either the spell ID (Spell.dbc), the item ID or macro ID.

### type

The type of action:

**Possible types**

| Value | Description |
| ----- | ----------- |
| 0     | Spell       |
| 1     | Click       |
| 32    | Eq set      |
| 64    | Macro       |
| 65    | Click macro |
| 128   | Item        |

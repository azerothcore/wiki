# outdoorpvp\_template

[<-Back-to:World](database-world)

**The \`outdoorpvp\_template\` table**

Links each outdoor PvP zone type to the script that handles it.

**Table: outdoorpvp\_template's Structure**

| Field                     | Type     |          | Null | Key | Default | Extra | Comment |
| :------------------------ | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [TypeId](#typeid)         | TINYINT  | UNSIGNED | NO   | PRI |         |       |         |
| [ScriptName](#scriptname) | CHAR(64) |          | NO   |     | ''      |       |         |
| [comment](#comment)       | TEXT     |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### TypeId
Id defined in the emulator for each PvP zone in the world.

### ScriptName
The name of the script that this outdoor pvp uses. This ties a script from a scripting engine to this outdoor pvp.

### comment
The script name for the given outdoorpvp_template.

### Example

| TypeId | ScriptName    | comment             |
| ------ | ------------- | ------------------- |
| 1      | outdoorpvp_hp | Hellfire Peninsula  |
| 2      | outdoorpvp_na | Nagrand             |
| 3      | outdoorpvp_tf | Terokkar Forest     |
| 4      | outdoorpvp_zm | Zangarmarsh         |
| 5      | outdoorpvp_si | Silithus            |
| 6      | outdoorpvp_ep | Eastern Plaguelands |
| 7      | outdoorpvp_gh | Grizzly Hills       |

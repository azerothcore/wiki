# outdoorpvp_template

[<-Back-to:World](database-world)

**The \`outdoorpvp_template\` table**

**Table Structure**

| Field           | Type     | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [TypeId][1]     | TINYINT  | unasigned  | PRI | NO   |         |       |         |
| [ScriptName][2] | char(64) | SIGNED     |     | NO   | 0       |       |         |
| [comment][3]    | text     | SIGNED     |     | YES  | NULL    |       |         |

[1]: #typeid
[2]: #scriptname
[3]: #comment

**Description of the fields**

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

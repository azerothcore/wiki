# outdoorpvp_template

[<-Volver a: World](es/database-world)

**Tabla \`outdoorpvp_template\`**

**Estructura**

| Field           | Type     | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [TypeId][1]     | TINYINT  | unasigned  | PRI | NO   |         |       |         |
| [ScriptName][2] | char(64) | SIGNED     |     | NO   | 0       |       |         |
| [comment][3]    | text     | SIGNED     |     | YES  | NULL    |       |         |

[1]: #typeid
[2]: #scriptname
[3]: #comment

**Descripción de los campos**

### TypeId
Id definido en el emulador para cada zona PvP del mundo.

### ScriptName
El nombre del script que usa este outdoor pvp. Vincula un script de un motor de scripting con este outdoor pvp.

### comment
El nombre del script para el outdoorpvp_template dado.

### Ejemplo

| TypeId | ScriptName    | comment             |
| ------ | ------------- | ------------------- |
| 1      | outdoorpvp_hp | Hellfire Peninsula  |
| 2      | outdoorpvp_na | Nagrand             |
| 3      | outdoorpvp_tf | Terokkar Forest     |
| 4      | outdoorpvp_zm | Zangarmarsh         |
| 5      | outdoorpvp_si | Silithus            |
| 6      | outdoorpvp_ep | Eastern Plaguelands |
| 7      | outdoorpvp_gh | Grizzly Hills       |

# groups

[<-Volver a:Characters](database-characters)

**Tabla \`groups\`**

La tabla alberga información básica acerca de los grupos.

**Estructura**

| Field                  | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]              | INT     | UNSIGNED   | PRI | NO   |         |       |         |
| [leaderGuid][2]        | INT     | UNSIGNED   |     | NO   |         |       |         |
| [lootMethod][3]        | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [looterGuid][4]        | INT     | UNSIGNED   |     | NO   |         |       |         |
| [lootThreshold][5]     | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [icon1][6]             | BIGINT  | UNSIGNED   |     | NO   |         |       |         |
| [icon2][7]             | BIGINT  | UNSIGNED   |     | NO   |         |       |         |
| [icon3][8]             | BIGINT  | UNSIGNED   |     | NO   |         |       |         |
| [icon4][9]             | BIGINT  | UNSIGNED   |     | NO   |         |       |         |
| [icon5][10]            | BIGINT  | UNSIGNED   |     | NO   |         |       |         |
| [icon6][11]            | BIGINT  | UNSIGNED   |     | NO   |         |       |         |
| [icon7][12]            | BIGINT  | UNSIGNED   |     | NO   |         |       |         |
| [icon8][13]            | BIGINT  | UNSIGNED   |     | NO   |         |       |         |
| [groupType][14]        | TINYINT | UNSIGNED   |     | NO   |         |       |         |
| [difficulty][15]       | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |
| [raiddifficulty][16]   | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |
| [masterLooterGuid][17] | INT     | UNSIGNED   |     | NO   |         |       |         |

[1]: #guid
[2]: #leaderguid
[3]: #lootmethod
[4]: #looterguid
[5]: #lootthreshold
[6]: #icon
[7]: #icon
[8]: #icon
[9]: #icon
[10]: #icon
[11]: #icon
[12]: #icon
[13]: #icon
[14]: #grouptype
[15]: #difficulty
[16]: #raiddifficulty
[17]: #masterlooterguid

**Descripción de los Campos**

### guid

ID del respectivo grupo. Este número es único para cada grupo y es el principal método para identificar un grupo.

### leaderGuid

GUID o Identificador Global Único del personaje. Véase [characters.guid](characters#guid).

### lootMethod

| Valor | Nombre              | Comentarios                          |
|------ | ------------------- | ------------------------------------ |
| 0     | FREE_FOR_ALL        | Botín Libre                          |
| 1     | ROUND_ROBIN         | Por Turnos                           |
| 2     | MASTER_LOOT         | Maestro de Botín                     |
| 3     | GROUP_LOOT          | Botín de Grupo                       |
| 4     | NEED_BEFORE_GREED   | Necesidad antes que codicia          |

### looterGuid

GUID o Identificador Global Único del Maestro de Botín. Véase [characters.guid](characters#guid).
Si [lootMethod](groups#lootmethod) no es 2, entonces es el GUID del líder del grupo.

### lootThreshold

`field-no-description|5` (¿Umbral o límite del botín?

### icon

`field-no-description|6-13` (¿?)

### groupType

| Valor | Nombre             | Comentarios                                                              |
|------ | ------------------ | ------------------------------------------------------------------------ |
| 0     | GROUPTYPE_NORMAL   | Grupo Normal                                                             |
| 1     | GROUPTYPE_BG       | Campo de Batalla                                                         |
| 2     | GROUPTYPE_RAID     | Raid                                                                     |
| 3     | GROUPTYPE_BGRAID   | GROUPTYPE_BG + GROUPTYPE_RAID, // Suma de ambas máscaras/tablas de bits  |
| 4     | GROUPTYPE_UNK1     | Desconocido                                                              |
| 8     | GROUPTYPE_LFG      | Buscador de Grupos                                                       |

### difficulty

`field-no-description|15` (¿Dificultad de Grupo?)

### raiddifficulty

`field-no-description|16` (¿Dificultad de Banda?)

### masterLooterGuid

`field-no-description|17` (¿?)

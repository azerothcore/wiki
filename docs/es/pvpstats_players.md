# pvpstats\_players

[<-Volver a:Characters](database-characters)

Leer en: [English :gb:](../pvpstats_players) [Spanish :es:](pvpstats_players)

**Tabla \`pvpstats\_players\`**

Esta tabla contiene datos sobre las puntuaciones de BattleGrounds. Para habilitar el almacenamiento de este tipo de información, configure **Battleground.StoreStatistics.Enable = 1** en el archivo **worldserver.config.dist**.

**Estructura**

| Field                      | Type      | Attributes | Key | Null | Default | Extra | Comment |
| -------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [battleground_id][1]       | BIGINT    | UNSIGNED   | PRI | NO   |         |       |         |
| [character_guid][2]        | INT       | UNSIGNED   | PRI | NO   |         |       |         |
| [winner][3]                | BIT       | SIGNED     |     | NO   |         |       |         |
| [score_killing_blows][4]   | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [score_deaths][5]          | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [score_honorable_kills][6] | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [score_bonus_honor][7]     | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [score_damage_done][8]     | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [score_healing_done][9]    | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [attr_1][10]               | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [attr_2][11]               | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [attr_3][12]               | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [attr_4][13]               | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [attr_5][14]               | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #battlegroundid
[2]: #characterguid
[3]: #winner
[4]: #score
[5]: #score
[6]: #score
[7]: #score
[8]: #score
[9]: #score
[10]: #attr
[11]: #attr
[12]: #attr
[13]: #attr
[14]: #attr

**Descripción de los campos**

### battleground\_id

Enlace a [pvpstats\_battlegrounds.id](pvpstats_battlegrounds#id).

### character\_guid

Enlace a [characters.guid](characters#guid).

### winner

1 cuando el jugador ha ganado el BG, 0 en caso contrario.

### score\_\*

Todas las puntuaciones que son comunes entre todos los Campos de Batalla.

### attr\_\*

Todos los puntajes que no son comunes entre todos los Campos de Batalla. Este campo cambia su media de acuerdo con [pvpstats\_battlegrounds.type](pvpstats_battlegrounds#type).

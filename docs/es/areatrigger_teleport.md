# areatrigger\_teleport

[<-Volver a:World](database-world)

**Tabla \`areatrigger\_teleport\`**

Contiene la definición de todos los triggers de teletransporte. Esta tabla se usa para completar la información del archivo .dbc.

**Estructura**

| Field                   | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]                 | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Name][2]               | text      |            | MUL | YES  |         |       |         |
| [target_map][3]         | SMALLINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [target_position_x][4]  | FLOAT     |            |     | NO   | 0       |       |         |
| [target_position_y][5]  | FLOAT     |            |     | NO   | 0       |       |         |
| [target_position_z][6]  | FLOAT     |            |     | NO   | 0       |       |         |
| [target_orientation][7] | FLOAT     |            |     | NO   | 0       |       |         |

[1]: #id
[2]: #name
[3]: #target_map
[4]: #target_position_x
[5]: #target_position_y
[6]: #target_position_z
[7]: #target_orientation

**Descripción de los campos**

### ID

Este es el identificador del trigger, debe coincidir con el de [AreaTrigger.dbc](DBC-AreaTrigger)

### name

Nombre del trigger. Puede ser un nombre arbitrario, y es solo con fines descriptivos.

### target\_map

Mapa de destino del trigger (ver Maps.dbc).

### target\_position\_x

Coordenada X del destino del trigger

### target\_position\_y

Coordenada Y del destino del trigger

### target\_position\_z

Coordenada Z del destino del trigger

### target\_orientation

Orientación que tendrá el jugador al aparecer en esta ubicación

### Examples

| ID  | Name                                     | target_map | target_position_x | target_position_y | target_position_z | target_orientation |
| --- | ---------------------------------------- | ---------- | ----------------- | ----------------- | ----------------- | ------------------ |
| 45  | Scarlet Monastery - Graveyard (Entrance) | 189        | 1688.99           | 1053.48           | 18.6775           | 0.00117            |
| 78  | DeadMines Entrance                       | 36         | -16.4             | -383.07           | 61.78             | 1.86               |
| 101 | Stormwind Stockades Entrance             | 34         | 54.23             | 0.28              | -18.34            | 6.26               |
| 107 | Stormwind Vault Entrance                 | 35         | -0.91             | 40.57             | -24.23            | 0                  |
| 109 | Stormwind Vault Instance                 | 0          | -8653.45          | 606.19            | 91.16             | 0                  |

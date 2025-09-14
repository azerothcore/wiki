# areatrigger\_teleport

[<-Back-to:World](database-world)

**The \`areatrigger\_teleport\` table**

Contiene todas las definiciones de los activadores de teletransporte. Esta tabla se utiliza para completar la información del archivo .dbc.

**Estructura**

| Campo                   | Tipo      | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| ----------------------- | --------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [ID][1]                 | MEDIUMINT | UNSIGNED  | PRI   | NO   | 0           |       |            |
| [Name][2]               | text      |           | MUL   | YES  |             |       |            |
| [target_map][3]         | SMALLINT  | UNSIGNED  |       | NO   | 0           |       |            |
| [target_position_x][4]  | FLOAT     |           |       | NO   | 0           |       |            |
| [target_position_y][5]  | FLOAT     |           |       | NO   | 0           |       |            |
| [target_position_z][6]  | FLOAT     |           |       | NO   | 0           |       |            |
| [target_orientation][7] | FLOAT     |           |       | NO   | 0           |       |            |

[1]: #id
[2]: #name
[3]: #target_map
[4]: #target_position_x
[5]: #target_position_y
[6]: #target_position_z
[7]: #target_orientation

**Description of the fields**

### ID

Este es el identificador del disparador, debe coincidir con el de [AreaTrigger.dbc](DBC-AreaTrigger)

### name

Nombre del disparador. Puede ser un nombre arbitrario y su uso es meramente descriptivo.

### target\_map

Mapa de destino del disparador (ver Maps.dbc).

### target\_position\_x

Coordenada X para el destino objetivo del disparador.

### target\_position\_y

Coordenada Y para el destino objetivo del disparador.

### target\_position\_z

Coordenada Z para el destino objetivo del disparador.

### target\_orientation

Orientación que obtendrá el jugador al aparecer en esta ubicación.

### Ejemplo

| ID  | Nombre                                     | target_map | target_position_x | target_position_y | target_position_z | target_orientation |
| --- | ---------------------------------------- | ---------- | ----------------- | ----------------- | ----------------- | ------------------ |
| 45  | Scarlet Monastery - Graveyard (Entrance) | 189        | 1688.99           | 1053.48           | 18.6775           | 0.00117            |
| 78  | DeadMines Entrance                       | 36         | -16.4             | -383.07           | 61.78             | 1.86               |
| 101 | Stormwind Stockades Entrance             | 34         | 54.23             | 0.28              | -18.34            | 6.26               |
| 107 | Stormwind Vault Entrance                 | 35         | -0.91             | 40.57             | -24.23            | 0                  |
| 109 | Stormwind Vault Instance                 | 0          | -8653.45          | 606.19            | 91.16             | 0                  |

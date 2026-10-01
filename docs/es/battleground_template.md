# battleground\_template

[<-Volver a:World](database-world)

**Tabla \`battleground\_template\`**

Contiene información sobre los distintos campos de batalla, como cuántos jugadores se necesitan para empezar, cuántos pueden estar dentro de uno mismo, y las ubicaciones donde empieza cada bando.

**Estructura**

| Field                  | Type      | Atributes | Key | Null | Default | Extra | Comment |
| ---------------------- | --------- | --------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]                | MEDIUMINT | UNSIGNED  | PRI | NO   | 0       |       |         |
| [MinPlayersPerTeam][2] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [MaxPlayersPerTeam][3] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [MinLvl][4]            | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [MaxLvl][5]            | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [AllianceStartLoc][6]  | MEDIUMINT | UNSIGNED  |     | NO   |         |       |         |
| [AllianceStartO][7]    | FLOAT     | SIGNED    |     | NO   |         |       |         |
| [HordeStartLoc][8]     | MEDIUMINT | UNSIGNED  |     | NO   |         |       |         |
| [HordeStartO][9]       | FLOAT     | SIGNED    |     | NO   |         |       |         |
| [StartMaxDist][10]     | FLOAT     | SIGNED    |     | NO   | 0       |       |         |
| [Weight][11]           | TINYINT   | UNSIGNED  |     | NO   | 1       |       |         |
| [ScriptName][12]       | char(64)  |           |     | NO   |         |       |         |
| [Comment][13]          | char(38)  |           |     | NO   |         |       |         |

[1]: #id
[2]: #minplayersperteam
[3]: #maxplayersperteam
[4]: #minlvl
[5]: #maxlvl
[6]: #alliancestartloc
[7]: #alliancestarto
[8]: #hordestartloc
[9]: #hordestarto
[10]: #startmaxdist
[11]: #weight
[12]: #scriptname
[13]: #comment

**Descripción de los campos**

### id

El ID del campo de batalla.

| ID  | Type                   |
| --- | ---------------------- |
| 1   | Alterac Valley         |
| 2   | Warsong Gulch          |
| 3   | Arathi Basin           |
| 4   | Nagrand Arena          |
| 5   | Blade's Edge Arena     |
| 6   | All Arena              |
| 7   | Eye of the Storm       |
| 8   | Ruins of Lordaeron     |
| 9   | Strand of the Ancients |
| 10  | Dalaran Sewers         |
| 11  | The Ring of Valor      |
| 30  | Isle of Conquest       |
| 32  | Random battleground    |

### MinPlayersPerTeam

Controla el número mínimo de jugadores que deben unirse al campo de batalla por cada bando de facción para que el campo de batalla empiece. Para que el campo de batalla empiece, todos los personajes (entre los valores mínimo y máximo de jugadores) deben estar en el mismo tramo (tier). Los tramos se organizan en rangos de 10 niveles excepto el nivel 80. Así que el primer tramo es 10-19, los siguientes son 20-29, 30-39, 40-49, 50-59, 60-69, 70-79 y por último 80. Si personajes de distintos tramos se unen a la cola, entrarán en la cola de su tramo respectivo y esperarán a que se unan más jugadores de su tramo. Los personajes de distintos tramos nunca pueden unirse al mismo campo de batalla.

### MaxPlayersPerTeam

Controla cuántos jugadores de cada equipo pueden unirse al campo de batalla.

NOTA2: Si se deja en 0, trinity usará el valor por defecto del DBC.

### MinLvl

El nivel mínimo que deben tener los jugadores para unirse al campo de batalla.

NOTA: Si se deja en 0, trinity usará el valor por defecto del DBC.

### MaxLvl

El nivel máximo que pueden tener los jugadores para entrar en el campo de batalla.

NOTA: Si se deja en 0, trinity usará el valor por defecto del DBC.

### AllianceStartLoc

La ubicación a la que se teletransportan los jugadores de la Alianza cuando el campo de batalla empieza por primera vez. Ver WorldSafeLocs.dbc

### AllianceStartO

La orientación de los jugadores de la Alianza al teletransportarse al campo de batalla. El norte es 0, el sur es Pi (3.14159).

### HordeStartLoc

La ubicación a la que se teletransportan los jugadores de la Horda cuando el campo de batalla empieza por primera vez. Ver WorldSafeLocs.dbc

### HordeStartO

La orientación de los jugadores de la Horda al teletransportarse al campo de batalla. El norte es 0, el sur es Pi (3.14159).

### Weight

Determina qué campo(s) de batalla se elegirán con más frecuencia al usar Campo de Batalla Aleatorio.
Por ejemplo: si quieres que AV se elija con menos frecuencia, dale 2 y a todos los demás dales 3.

### Example

| ID  | MinPlayersPerTeam | MaxPlayersPerTeam | MinLvl | MaxLvl | AllianceStartLoc | AllianceStartO | HordeStartLoc | HordeStartO | StartMaxDist | Weight | ScriptName | Comment                                |
| --- | ----------------- | ----------------- | ------ | ------ | ---------------- | -------------- | ------------- | ----------- | ------------ | ------ | ---------- | -------------------------------------- |
| 1   | 20                | 40                | 51     | 80     | 611              | 3.16312        | 610           | 0.715504    | 100          | 1      |            | Alterac Valley (battleground)          |
| 2   | 5                 | 10                | 10     | 80     | 769              | 3.14159        | 770           | 0.151581    | 75           | 1      |            | Warsong Gulch (battleground)           |
| 3   | 8                 | 15                | 20     | 80     | 890              | 3.91571        | 889           | 0.813671    | 75           | 1      |            | Arathi Basin (battleground)            |
| 4   | 0                 | 5                 | 10     | 80     | 929              | 0              | 936           | 3.14159     | 0            | 1      |            | Nagrand Arena / Ring of Trials (arena) |
| 5   | 0                 | 5                 | 10     | 80     | 939              | 0              | 940           | 3.14159     | 0            | 1      |            | Blades's Edge Arena (arena)            |

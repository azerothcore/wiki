# battleground\_template

[<-Volver a:World](database-world)

**Tabla \`battleground\_template\`**

Contiene información sobre los diferentes campos de batalla, como cuántos jugadores se necesitan para comenzar, cuántos pueden estar dentro del mismo y las ubicaciones donde comienza cada bando.

**Estructura**

| Campo                  | Tipo      | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| ---------------------- | --------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [ID][1]                | MEDIUMINT | UNSIGNED  | PRI   | NO   | 0           |       |            |
| [MinPlayersPerTeam][2] | SMALLINT  | UNSIGNED  |       | NO   | 0           |       |            |
| [MaxPlayersPerTeam][3] | SMALLINT  | UNSIGNED  |       | NO   | 0           |       |            |
| [MinLvl][4]            | TINYINT   | UNSIGNED  |       | NO   | 0           |       |            |
| [MaxLvl][5]            | TINYINT   | UNSIGNED  |       | NO   | 0           |       |            |
| [AllianceStartLoc][6]  | MEDIUMINT | UNSIGNED  |       | NO   |             |       |            |
| [AllianceStartO][7]    | FLOAT     | SIGNED    |       | NO   |             |       |            |
| [HordeStartLoc][8]     | MEDIUMINT | UNSIGNED  |       | NO   |             |       |            |
| [HordeStartO][9]       | FLOAT     | SIGNED    |       | NO   |             |       |            |
| [StartMaxDist][10]     | FLOAT     | SIGNED    |       | NO   | 0           |       |            |
| [Weight][11]           | TINYINT   | UNSIGNED  |       | NO   | 1           |       |            |
| [ScriptName][12]       | char(64)  |           |       | NO   |             |       |            |
| [Comment][13]          | char(38)  |           |       | NO   |             |       |            |

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

El identificador del campo de batalla.

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

Controla el número mínimo de jugadores que deben unirse al campo de batalla de cada facción para que comience. Para que comience, todos los personajes (entre el valor mínimo y el máximo) deben estar en el mismo nivel. Los niveles se establecen en rangos de 10 niveles, excepto el nivel 80. Así, el primer nivel es del 10 al 19, los siguientes del 20 al 29, 30 al 39, 40 al 49, 50 al 59, 60 al 69, 70 al 79 y, finalmente, el 80. Si personajes de diferentes niveles se unen a la cola, se unirán a la de su respectivo nivel y esperarán a que se unan más jugadores de su nivel. Los personajes de diferentes niveles nunca pueden unirse al mismo campo de batalla.

### MaxPlayersPerTeam

Controla cuántos jugadores de cada equipo pueden unirse al campo de batalla.

NOTA: Si se deja en 0, Trinity utilizará el valor DBC predeterminado.

### MinLvl

El nivel mínimo que los jugadores deben tener para unirse al campo de batalla.

NOTA: Si se deja en 0, Trinity utilizará el valor DBC predeterminado.

### MaxLvl

El nivel máximo que los jugadores pueden tener para ingresar al campo de batalla.

NOTA: Si se deja en 0, Trinity utilizará el valor DBC predeterminado.

### AllianceStartLoc

The location where the alliance players get teleported to when the battleground first starts. See WorldSafeLocs.dbc

### AllianceStartO

Orientación de los jugadores de la alianza al teletransportarse al campo de batalla: Norte es 0, sur es Pi (3.14159).

### HordeStartLoc

El lugar al que se teletransportan los jugadores de la Horda al iniciar el campo de batalla. Ver WorldSafeLocs.dbc

### HordeStartO

Orientación de los jugadores de la Horda al teletransportarse al campo de batalla: Norte es 0, sur es Pi (3.14159).

### Weight

Determina qué campo(s) de batalla se elegirán con más frecuencia al usar Campo de batalla aleatorio.
Por ejemplo: si quieres que AV sea elegido con menos frecuencia, dale 2 y para todos los demás dale 3.

### Ejemplo

| ID  | MinPlayersPerTeam | MaxPlayersPerTeam | MinLvl | MaxLvl | AllianceStartLoc | AllianceStartO | HordeStartLoc | HordeStartO | StartMaxDist | Weight | ScriptName | Comentario                             |
| --- | ----------------- | ----------------- | ------ | ------ | ---------------- | -------------- | ------------- | ----------- | ------------ | ------ | ---------- | -------------------------------------- |
| 1   | 20                | 40                | 51     | 80     | 611              | 3.16312        | 610           | 0.715504    | 100          | 1      |            | Alterac Valley (campo de batalla)      |
| 2   | 5                 | 10                | 10     | 80     | 769              | 3.14159        | 770           | 0.151581    | 75           | 1      |            | Warsong Gulch (campo de batalla)       |
| 3   | 8                 | 15                | 20     | 80     | 890              | 3.91571        | 889           | 0.813671    | 75           | 1      |            | Arathi Basin (campo de batalla)        |
| 4   | 0                 | 5                 | 10     | 80     | 929              | 0              | 936           | 3.14159     | 0            | 1      |            | Nagrand Arena / Ring of Trials (arena) |
| 5   | 0                 | 5                 | 10     | 80     | 939              | 0              | 940           | 3.14159     | 0            | 1      |            | Blades's Edge Arena (arena)            |

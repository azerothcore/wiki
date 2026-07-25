# creature\_summon\_groups

[<-Volver a: World](database-world)

# Tabla: creature\_summon\_groups

Esta tabla contiene datos sobre criaturas invocadas temporalmente. Es posible agrupar invocaciones y crear oleadas de adds de jefes, etc.

## Estructura

| Field             | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [summonerId][1]   | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [summonerType][2] | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [groupId][3]      | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [entry][4]        | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [position_x][5]   | FLOAT        |            |     | NO   | 0       |       |         |
| [position_y][6]   | FLOAT        |            |     | NO   | 0       |       |         |
| [position_z][7]   | FLOAT        |            |     | NO   | 0       |       |         |
| [orientation][8]  | FLOAT        |            |     | NO   | 0       |       |         |
| [summonType][9]   | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [summonTime][10]  | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| [Comment][11]     | VARCHAR(255) |            |     | NO   | ''      |       |         |

[1]: #summonerid
[2]: #summonertype
[3]: #groupid
[4]: #entry
[5]: #position_x
[6]: #position_y
[7]: #position_z
[8]: #orientation
[9]: #summontype
[10]: #summontime
[11]: #comment

## **Descripción de los campos**

### summonerId

ID del invocador, dependiendo de [summonerType](#summonertype)

### summonerType

Tipo del invocador:

| Value | Type                     |
| ----- | ------------------------ |
| 0     | SUMMONER_TYPE_CREATURE   |
| 1     | SUMMONER_TYPE_GAMEOBJECT |
| 2     | SUMMONER_TYPE_MAP        |

### groupId

Identificador del grupo; todas las criaturas con el mismo [groupId](#groupid) serán invocadas a la vez

### entry

Entry de la criatura invocada, de [creature\_template.entry](creature_template#entry)

### position\_x

Coordenada X de la posición donde se generará la criatura

### position\_y

Coordenada Y de la posición donde se generará la criatura

### position\_z

Coordenada Z de la posición donde se generará la criatura

### orientation

Orientación que tendrá la criatura invocada al generarse

### summonType

| Value | Name                                   | Comments                                                            |
| ----- | -------------------------------------- | ------------------------------------------------------------------- |
| 1     | TEMPSUMMON_TIMED_OR_DEAD_DESPAWN       | Desaparece tras un tiempo especificado O cuando la criatura desaparece |
| 2     | TEMPSUMMON_TIMED_OR_CORPSE_DESPAWN     | Desaparece tras un tiempo especificado O cuando la criatura muere   |
| 3     | TEMPSUMMON_TIMED_DESPAWN               | Desaparece tras un tiempo especificado                              |
| 4     | TEMPSUMMON_TIMED_DESPAWN_OUT_OF_COMBAT | Desaparece tras un tiempo especificado después de que la criatura sale de combate |
| 5     | TEMPSUMMON_CORPSE_DESPAWN              | Desaparece al instante tras la muerte                               |
| 6     | TEMPSUMMON_CORPSE_TIMED_DESPAWN        | Desaparece tras un tiempo especificado después de la muerte         |
| 7     | TEMPSUMMON_DEAD_DESPAWN                | Desaparece cuando la criatura desaparece                            |
| 8     | TEMPSUMMON_MANUAL_DESPAWN              | Desaparece cuando se llama a UnSummon()                             |

### summonTime

Temporizador vinculado a summontype

### Comment

Comentario

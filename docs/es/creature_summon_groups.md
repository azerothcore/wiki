# creature\_summon\_groups

[<-Volver a:World](database-world)

**Tabla creature\_summon\_groups**

Esta tabla contiene datos sobre las criaturas invocadas temporalmente. Es posible agrupar invocaciones y crear oleadas de enemigos adicionales para jefes, etc.

**Estructura**

| Campo             | Tipo         | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| ----------------- | ------------ | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [summonerId][1]   | MEDIUMINT    | UNSIGNED  |       | NO   | 0           |       |            |
| [summonerType][2] | TINYINT      | UNSIGNED  |       | NO   | 0           |       |            |
| [groupId][3]      | TINYINT      | UNSIGNED  |       | NO   | 0           |       |            |
| [entry][4]        | MEDIUMINT    | UNSIGNED  |       | NO   | 0           |       |            |
| [position_x][5]   | FLOAT        |           |       | NO   | 0           |       |            |
| [position_y][6]   | FLOAT        |           |       | NO   | 0           |       |            |
| [position_z][7]   | FLOAT        |           |       | NO   | 0           |       |            |
| [orientation][8]  | FLOAT        |           |       | NO   | 0           |       |            |
| [summonType][9]   | TINYINT      | UNSIGNED  |       | NO   | 0           |       |            |
| [summonTime][10]  | INT          | UNSIGNED  |       | NO   | 0           |       |            |
| [Comment][11]     | VARCHAR(255) |           |       | NO   | ''          |       |            |

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

ID del invocador según [summonerType](#creature_summon_groups-summonerType)

### summonerType

Tipo de invocador:

| Valor | Tipo                     |
| ----- | ------------------------ |
| 0     | SUMMONER_TYPE_CREATURE   |
| 1     | SUMMONER_TYPE_GAMEOBJECT |
| 2     | SUMMONER_TYPE_MAP        |

### groupId

Identificador de grupo, todas las criaturas con el mismo [groupId](#creature_summon_groups-groupId) serán invocadas a la vez

### entry

Entrada de criatura invocada desde [creature\_template.entry](creature_template#entry)

### position\_x

Coordenada X de la posición donde se generará la criatura.

### position\_y

Coordenada Y de la posición donde se generará la criatura

### position\_z

Coordenada Z de la posición donde se generará la criatura

### orientation

Orientación que obtendrá la criatura invocada cuando aparezca

### summonType

| Valor | Nombre                                 | Comentarios                                                                                  |
| ----- | -------------------------------------- | -------------------------------------------------------------------------------------------- |
| 1     | TEMPSUMMON_TIMED_OR_DEAD_DESPAWN       | Desaparece después de un tiempo específico O cuando la criatura desaparece                   |
| 2     | TEMPSUMMON_TIMED_OR_CORPSE_DESPAWN     | Desaparece después de un tiempo específico O cuando la criatura muere                        |
| 3     | TEMPSUMMON_TIMED_DESPAWN               | Desaparece después de un tiempo específico                                                   |
| 4     | TEMPSUMMON_TIMED_DESPAWN_OUT_OF_COMBAT | Desaparece después de un tiempo específico después de que la criatura esté fuera de combate. |
| 5     | TEMPSUMMON_CORPSE_DESPAWN              | Desaparece instantáneamente después de morir.                                                |
| 6     | TEMPSUMMON_CORPSE_TIMED_DESPAWN        | Desaparece después de un tiempo específico después de la muerte.                             |
| 7     | TEMPSUMMON_DEAD_DESPAWN                | Desaparece cuando la criatura desaparece.                                                    |
| 8     | TEMPSUMMON_MANUAL_DESPAWN              | Desaparece cuando se llama a UnSummon()                                                      |

### summonTime

Temporizador vinculado al tipo de invocación

### Comment

Comentario


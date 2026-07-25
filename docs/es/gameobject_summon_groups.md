# gameobject\_summon\_groups

[<-Volver a: World](database-world)

# Tabla: gameobject\_summon\_groups

Esta tabla contiene datos sobre gameobjects que se invocan temporalmente como grupo. Funciona de forma similar a [creature\_summon\_groups](creature_summon_groups) pero para gameobjects.

## Estructura

| Field               | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [summonerId](#summonerid)     | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| [summonerType](#summonertype) | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [groupId](#groupid)           | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [entry](#entry)               | INT          | UNSIGNED   |     | NO   | 0       |       |         |
| [position\_x](#positionx)     | FLOAT        |            |     | NO   | 0       |       |         |
| [position\_y](#positiony)     | FLOAT        |            |     | NO   | 0       |       |         |
| [position\_z](#positionz)     | FLOAT        |            |     | NO   | 0       |       |         |
| [orientation](#orientation)   | FLOAT        |            |     | NO   | 0       |       |         |
| [rotation0](#rotation0)       | FLOAT        |            |     | NO   | 0       |       |         |
| [rotation1](#rotation1)       | FLOAT        |            |     | NO   | 0       |       |         |
| [rotation2](#rotation2)       | FLOAT        |            |     | NO   | 0       |       |         |
| [rotation3](#rotation3)       | FLOAT        |            |     | NO   | 1       |       |         |
| [respawnTime](#respawntime)   | INT          | UNSIGNED   |     | NO   | 120     |       |         |
| [Comment](#comment)           | VARCHAR(255) |            |     | NO   | ''      |       |         |

## Descripción de los campos

### summonerId

El ID de entry del objeto que activa la invocación, según [summonerType](#summonertype).

### summonerType

El tipo del objeto invocador:

| Value | Type                     |
| ----- | ------------------------ |
| 0     | SUMMONER_TYPE_CREATURE   |
| 1     | SUMMONER_TYPE_GAMEOBJECT |
| 2     | SUMMONER_TYPE_MAP        |

### groupId

Identificador de grupo. Todos los gameobjects con el mismo `groupId` y `summonerId` se invocarán a la vez cuando se active el grupo.

### entry

Entry del gameobject a invocar, de [gameobject\_template.entry](gameobject_template#entry).

### position\_x

Coordenada X de la posición donde se generará el gameobject.

### position\_y

Coordenada Y de la posición donde se generará el gameobject.

### position\_z

Coordenada Z de la posición donde se generará el gameobject.

### orientation

Ángulo de orientación del gameobject generado. Se conserva por compatibilidad; los campos cuaternión se usan para la rotación precisa.

### rotation0

El componente X de la rotación cuaternión aplicada al gameobject generado. El valor por defecto es 0.

### rotation1

El componente Y de la rotación cuaternión. El valor por defecto es 0.

### rotation2

El componente Z de la rotación cuaternión. El valor por defecto es 0.

### rotation3

El componente W (escalar) de la rotación cuaternión. El valor por defecto es 1, que junto con los demás componentes puestos a 0 representa el cuaternión identidad (sin rotación).

### respawnTime

Tiempo en segundos antes de que el gameobject invocado desaparezca. El valor por defecto es 120. Usa 0 para permanente.

### Comment

Una descripción opcional legible por humanos de esta entrada.

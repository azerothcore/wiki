# gameobject\_summon\_groups

[<-Back-to:World](database-world)

# Table: gameobject\_summon\_groups

This table holds data about gameobjects that are temporarily summoned as a group. It works similarly to [creature\_summon\_groups](creature_summon_groups) but for gameobjects.

## Structure

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

## Description of the fields

### summonerId

The entry ID of the object that triggers the summon, depending on [summonerType](#summonertype).

### summonerType

The type of the summoning object:

| Value | Type                     |
| ----- | ------------------------ |
| 0     | SUMMONER_TYPE_CREATURE   |
| 1     | SUMMONER_TYPE_GAMEOBJECT |
| 2     | SUMMONER_TYPE_MAP        |

### groupId

Group identifier. All gameobjects with the same `groupId` and `summonerId` will be summoned at once when the group is triggered.

### entry

Entry of the gameobject to summon from [gameobject\_template.entry](gameobject_template#entry).

### position\_x

X coordinate of the position where the gameobject will be spawned.

### position\_y

Y coordinate of the position where the gameobject will be spawned.

### position\_z

Z coordinate of the position where the gameobject will be spawned.

### orientation

Facing angle of the spawned gameobject. Kept for compatibility; quaternion fields are used for precise rotation.

### rotation0

The X component of the quaternion rotation applied to the spawned gameobject. Default is 0.

### rotation1

The Y component of the quaternion rotation. Default is 0.

### rotation2

The Z component of the quaternion rotation. Default is 0.

### rotation3

The W (scalar) component of the quaternion rotation. Default is 1, which together with the other components set to 0 represents the identity quaternion (no rotation).

### respawnTime

Time in seconds before the summoned gameobject despawns. Default is 120. Use 0 for permanent.

### Comment

An optional human-readable description of this entry.

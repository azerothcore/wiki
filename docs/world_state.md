# world_state

[<-Back-to:Characters](database-characters)

**The `world_state` table**

Persists server-wide world state values so they survive restarts. Each row holds a serialized blob of world-state data keyed by an internal save `Id`.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Id](#id) | INT | UNSIGNED | PRI | NO |  |  | Internal save ID |
| [Data](#data) | LONGTEXT |  |  | YES | (NULL) |  |  |

**Description of the fields**

### Id

Internal world-state save identifier.

### Data

Serialized world-state payload.

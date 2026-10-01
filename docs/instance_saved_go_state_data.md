# instance_saved_go_state_data

[<-Back-to:Characters](database-characters)

**The `instance_saved_go_state_data` table**

Persists the saved state of gameobjects inside a bound instance (for example doors or levers left open), so the state is restored when the instance is reloaded. Keyed by instance `id` and gameobject `guid`.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id](#id) | INT | UNSIGNED | PRI | NO |  |  | instance.id |
| [guid](#guid) | INT | UNSIGNED | PRI | NO |  |  | gameobject.guid |
| [state](#state) | TINYINT | UNSIGNED |  | YES | 0 |  | gameobject.state |

**Description of the fields**

### id

References `instance.id` – the saved instance.

### guid

References `gameobject.guid` – the gameobject whose state is saved.

### state

Saved `GOState` of the gameobject (e.g. active/ready).

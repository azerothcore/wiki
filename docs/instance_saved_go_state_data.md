# instance\_saved\_go\_state\_data

[<-Back-to:Characters](database-characters)

**The \`instance\_saved\_go\_state\_data\` table**

Persists the saved state of gameobjects inside a bound instance (for example doors or levers left open), so the state is restored when the instance is reloaded. Keyed by instance `id` and gameobject `guid`.

**Table: instance\_saved\_go\_state\_data's Structure**

| Field           | Type    |          | Null | Key | Default | Extra | Comment          |
| :-------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :--------------- |
| [id](#id)       | INT     | UNSIGNED | NO   | PRI |         |       | instance.id      |
| [guid](#guid)   | INT     | UNSIGNED | NO   | PRI |         |       | gameobject.guid  |
| [state](#state) | TINYINT | UNSIGNED | YES  |     | 0       |       | gameobject.state |

**Description of the table's fields**

### id

References `instance.id` – the saved instance.

### guid

References `gameobject.guid` – the gameobject whose state is saved.

### state

Saved `GOState` of the gameobject (e.g. active/ready).

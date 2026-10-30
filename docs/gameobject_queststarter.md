# gameobject\_queststarter

[<-Back-to:World](database-world)

**The \`gameobject\_queststarter\` table**

Holds game object quest giver relations. The game objects in this table should all be of type QUESTGIVER (2).

**Table: gameobject\_queststarter's Structure**

| Field           | Type |          | Null | Key | Default | Extra | Comment          |
| :-------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :--------------- |
| [id](#id)       | INT  | UNSIGNED | NO   | PRI | 0       |       |                  |
| [quest](#quest) | INT  | UNSIGNED | NO   | PRI | 0       |       | Quest Identifier |

**Description of the table's fields**

### id

The template ID of the game object. See [gameobject\_template.entry](gameobject_template#entry)

### quest

The quest ID that this game object starts. See [quest\_template.id](quest_template#id)

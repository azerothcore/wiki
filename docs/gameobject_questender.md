# gameobject\_questender

[<-Back-to:World](database-world)

**The \`gameobject\_questender\` table**

Holds game object quest taker relations. The game objects in this table should all be of type QUESTGIVER (2).

**Table: gameobject\_questender's Structure**

| Field           | Type |          | Null | Key | Default | Extra | Comment          |
| :-------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :--------------- |
| [id](#id)       | INT  | UNSIGNED | NO   | PRI | 0       |       |                  |
| [quest](#quest) | INT  | UNSIGNED | NO   | PRI | 0       |       | Quest Identifier |

**Description of the table's fields**

### id

The template ID of the game object. See [gameobject\_template.entry](http://www.azerothcore.org/wiki/gameobject_template#entry)

### quest

The quest ID that this game object finishes. See [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id)

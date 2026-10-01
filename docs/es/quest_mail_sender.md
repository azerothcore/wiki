# quest\_mail\_sender

[<-Volver a: World](database-world)

**Tabla \`quest\_mail\_sender\`**

**Estructura**

| Field                      | Type | Attribute | Key | Null | Default | Extra | Comment |
| -------------------------- | ---- | --------- | --- | ---- | ------- | ----- | ------- |
| [QuestId][1]               | INT  | UNSIGNED  | PRI | NO   | 0       |       |         |
| [RewardMailSenderEntry][2] | INT  | UNSIGNED  |     | NO   | 0       |       |         |

[1]: #questid
[2]: #rewardmailsenderentry

**Descripción de los campos**

### QuestId

Es el ID de la misión, obtenido de quest_template

### RewardMailSenderEntry

Es el ID del correo que debe enviarse al jugador una vez que la misión lo ha recomendado.

### Example
```sql
DELETE FROM `quest_mail_sender` WHERE `QuestId`=10588 AND `RewardMailSenderEntry`=18166;
INSERT INTO `quest_mail_sender` (`QuestId`, `RewardMailSenderEntry`) VALUES
(10588, 18166);
```

![WoWScrnShot_010521_114722](https://user-images.githubusercontent.com/2810187/103660200-18603880-4f4c-11eb-995e-e2994353532e.jpg)
![WoWScrnShot_010521_114806](https://user-images.githubusercontent.com/2810187/103660207-19916580-4f4c-11eb-854f-e2d043127a90.jpg)

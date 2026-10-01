# quest\_mail\_sender

[<-返回至:World](database-world)

**`quest\_mail\_sender` 表**

**表结构**

| Field                      | Type | Attribute | Key | Null | Default | Extra | Comment |
| -------------------------- | ---- | --------- | --- | ---- | ------- | ----- | ------- |
| [QuestId][1]               | INT  | UNSIGNED  | PRI | NO   | 0       |       |         |
| [RewardMailSenderEntry][2] | INT  | UNSIGNED  |     | NO   | 0       |       |         |

[1]: #questid
[2]: #rewardmailsenderentry

**字段说明**

### QuestId

任务 ID，取自 quest_template。

### RewardMailSenderEntry

任务完成后需要发送给玩家的邮件 ID。

### 示例
```sql
DELETE FROM `quest_mail_sender` WHERE `QuestId`=10588 AND `RewardMailSenderEntry`=18166;
INSERT INTO `quest_mail_sender` (`QuestId`, `RewardMailSenderEntry`) VALUES
(10588, 18166);
```

![WoWScrnShot_010521_114722](https://user-images.githubusercontent.com/2810187/103660200-18603880-4f4c-11eb-995e-e2994353532e.jpg)
![WoWScrnShot_010521_114806](https://user-images.githubusercontent.com/2810187/103660207-19916580-4f4c-11eb-854f-e2d043127a90.jpg)

# quest\_offer\_reward\_locale

[<-返回至:World](database-world)

**`quest\_offer\_reward\_locale` 表**

**表结构**

| Field              | Type       | Attribute | Key | Null | Default | Extra | Comment |
| ------------------ | ---------- | --------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]            | INT        | UNSIGNED  | PRI | NO   | 0       |       |         |
| [locale][2]        | VARCHAR(4) |           | PRI | NO   | NULL    |       |         |
| [RewardText][3]    | text       |           |     | YES  | NULL    |       |         |
| [VerifiedBuild][4] | SMALLINT   |           |     | NO   | 0       |       |         |

[1]: #id
[2]: #locale
[3]: #rewardtext
[4]: #verifiedbuild

**字段说明**

### ID

任务 ID，取自 quest_template。

### locale

这是你想要进行翻译的语言。
你可以从以下选项中选择：

| ID  | Language |
| --- | -------- |
| 0   | enUS     |
| 1   | koKR     |
| 2   | frFR     |
| 3   | deDE     |
| 4   | zhCN     |
| 5   | zhTW     |
| 6   | esES     |
| 7   | esMX     |
| 8   | ruRU     |

### RewardText

这是任务交付时显示的文本。也就是说，在获得奖励之前显示的文本。

### VerifiedBuild

### 示例
```sql
DELETE FROM `quest_offer_reward_locale` WHERE `ID`=2 AND `locale`='esES';
INSERT INTO `quest_offer_reward_locale` (`ID`, `locale`, `RewardText`, `VerifiedBuild`) VALUES
(2, "esES", "De lo más impresionante, $n... ¡no puede haber sido un paseo conseguir la garra de Garrafilada! ¡La Caza de Vallefresno te está yendo bien!$B$BGarrafilada lleva muchos años aterrorizando a los peones de los aserraderos cuando se trasladan a Puesto del Hachazo y se cruzan en su ruta. No lo dudes, cuando se corra la voz de que doblegaste a ese monstruo, ¡se escucharán muchas canciones alabando tu valor en los campamentos y aserraderos de todo Vallefresno!", 0);
```

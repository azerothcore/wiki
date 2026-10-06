# quest\_offer\_reward\_locale

[<-Back-to:World](database-world)

**The \`quest\_offer\_reward\_locale\` table**

Holds translations of the reward text in [quest_offer_reward](quest_offer_reward).

**Table: quest\_offer\_reward\_locale's Structure**

| Field                           | Type       |          | Null | Key | Default | Extra | Comment |
| :------------------------------ | :--------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                       | INT        | UNSIGNED | NO   | PRI | 0       |       |         |
| [locale](#locale)               | VARCHAR(4) |          | NO   | PRI |         |       |         |
| [RewardText](#rewardtext)       | TEXT       |          | YES  |     | NULL    |       |         |
| [VerifiedBuild](#verifiedbuild) | INT        |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### ID

Is the quest ID, obtained from quest_template

### locale

It is the language in which you want to make the translation.
You can choose from the following:

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

This is the text that is displayed when the quest is delivered. That is, before the reward is obtained.

### VerifiedBuild

This field is used to determine if this translation originates from verified sniffs.

If value is 0 then it has not been parsed yet or it has been inherited from an older DB or another Core.

If value is above 0 then it has been parsed with sniffs from that specific client build.

### Example
```sql
DELETE FROM `quest_offer_reward_locale` WHERE `ID`=2 AND `locale`='esES';
INSERT INTO `quest_offer_reward_locale` (`ID`, `locale`, `RewardText`, `VerifiedBuild`) VALUES
(2, "esES", "De lo más impresionante, $n... ¡no puede haber sido un paseo conseguir la garra de Garrafilada! ¡La Caza de Vallefresno te está yendo bien!$B$BGarrafilada lleva muchos años aterrorizando a los peones de los aserraderos cuando se trasladan a Puesto del Hachazo y se cruzan en su ruta. No lo dudes, cuando se corra la voz de que doblegaste a ese monstruo, ¡se escucharán muchas canciones alabando tu valor en los campamentos y aserraderos de todo Vallefresno!", 0);
```

# quest\_offer\_reward\_locale

[<-Volver a: World](database-world)

**Tabla \`quest\_offer\_reward\_locale\`**

**Estructura**

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

**Descripción de los campos**

### ID

Es el ID de la misión, obtenido de quest_template

### locale

Es el idioma en el que quieres hacer la traducción.
Puedes elegir entre los siguientes:

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

Este es el texto que se muestra cuando se entrega la misión. Es decir, antes de obtener la recompensa.

### VerifiedBuild

### Example
```sql
DELETE FROM `quest_offer_reward_locale` WHERE `ID`=2 AND `locale`='esES';
INSERT INTO `quest_offer_reward_locale` (`ID`, `locale`, `RewardText`, `VerifiedBuild`) VALUES
(2, "esES", "De lo más impresionante, $n... ¡no puede haber sido un paseo conseguir la garra de Garrafilada! ¡La Caza de Vallefresno te está yendo bien!$B$BGarrafilada lleva muchos años aterrorizando a los peones de los aserraderos cuando se trasladan a Puesto del Hachazo y se cruzan en su ruta. No lo dudes, cuando se corra la voz de que doblegaste a ese monstruo, ¡se escucharán muchas canciones alabando tu valor en los campamentos y aserraderos de todo Vallefresno!", 0);
```

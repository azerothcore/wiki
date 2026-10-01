# character\_pet

[<-返回:Characters](database-characters)

**\`character\_pet\` 表**

该表保存了游戏中任何玩家所召唤的每个宠物的宠物数据。

**表结构**

| Field               | Type        | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]             | INT         | UNSIGNED   | PRI | NO   | 0       |       |         |
| [entry][2]          | INT         | UNSIGNED   |     | NO   | 0       |       |         |
| [owner][3]          | INT         | UNSIGNED   |     | NO   | 0       |       |         |
| [modelid][4]        | INT         | UNSIGNED   |     | YES  | 0       |       |         |
| [CreatedBySpell][5] | MEDIUMINT   | UNSIGNED   |     | NO   | 0       |       |         |
| [PetType][6]        | TINYINT     | UNSIGNED   |     | NO   | 0       |       |         |
| [level][7]          | SMALLINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [exp][8]            | INT         | UNSIGNED   |     | NO   | 1       |       |         |
| [Reactstate][9]     | TINYINT     | UNSIGNED   |     | NO   | 0       |       |         |
| [name][10]          | VARCHAR(21) | SIGNED     |     | NO   | 0       |       |         |
| [renamed][11]       | TINYINT     | UNSIGNED   |     | NO   | Pet     |       |         |
| [slot][12]          | TINYINT     | UNSIGNED   |     | NO   | 0       |       |         |
| [curhealth][13]     | INT         | UNSIGNED   |     | NO   | 0       |       |         |
| [curmana][14]       | INT         | UNSIGNED   |     | NO   | 1       |       |         |
| [curhappiness][15]  | INT         | UNSIGNED   |     | NO   | 0       |       |         |
| [savetime][16]      | INT         | UNSIGNED   |     | NO   | 0       |       |         |
| [abdata][17]        | TEXT        | SIGNED     |     | YES  | 0       |       |         |

[1]: #id
[2]: #entry
[3]: #owner
[4]: #modelid
[5]: #createdbyspell
[6]: #pettype
[7]: #level
[8]: #exp
[9]: #reactstate
[10]: #name
[11]: #renamed
[12]: #slot
[13]: #curhealth
[14]: #curmana
[15]: #curhappiness
[16]: #savetime
[17]: #abdata

**字段说明**

### id

特殊宠物 ID。这是所有宠物中唯一的标识符。

### entry

该宠物的生物 entry。参见 [creature\_template.entry](creature_template#entry)。

### owner

宠物主人的 GUID。参见 [characters.guid](characters#guid)。

### modelid

用于显示该宠物的模型 ID。

### CreatedBySpell

创建该宠物的法术 ID。对于猎人来说，通常是驯服野兽（Tame Beast）法术。对于术士或其他职业（法师），则是召唤该生物的法术 ID。参见 [Spell.dbc](spell) 第 1 列。

### PetType

该宠物的类型。0 = 召唤宠物，1 = 驯服宠物

### level

宠物当前等级。

### exp

该宠物当前拥有的经验值。对于召唤宠物，此字段始终为 0。

### Reactstate

宠物当前的战斗反应状态（被动、主动攻击等）。

### name

宠物的名字。

### renamed

布尔值 1 或 0。1 = 宠物已被重命名，0 = 宠物从未被重命名，仍使用被驯服生物的名字。

### slot

- 宠物所在的宠物槽位。
- 当前激活的宠物（跟随玩家的宠物）槽位为 0；
- 1-4 为兽栏（stable）中的宠物（槽位 1-4）；
- 100 为跟随玩家但当前已被解散（dismissed）的宠物。

### curhealth

宠物在保存到数据库时的当前生命值。

### curmana

宠物在保存到数据库时的当前法力值。

### curhappiness

宠物当前的好感度。

### savetime

宠物上次保存的时间，使用 Unix 时间表示。

### abdata

`field-no-description|17`

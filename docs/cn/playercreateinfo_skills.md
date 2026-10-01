# playercreateinfo_skills

[<-返回至:World](database-world)

# playercreateinfo_skills 表

该表保存了新建角色应拥有的技能信息。此表中的角色由其种族和职业组合定义。

## 结构

| Field          | Type         | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [racemask][1]  | INT          | UNSIGNED   | PRI | NO   |         |       |         |
| [classmask][2] | INT          | UNSIGNED   | PRI | NO   |         |       |         |
| [skill][3]     | SMALLINT     | UNSIGNED   | PRI | NO   |         |       |         |
| [rank][4]      | SMALLINT     | UNSIGNED   |     | NO   | 0       |       |         |
| [Comment][5]   | VARCHAR(255) |            |     | YES  |         |       |         |

[1]: #racemask
[2]: #classmask
[3]: #spell
[4]: #rank
[5]: #comment

## 字段说明

### racemask

一个或多个角色种族。参见 [ChrRaces.dbc](chrraces)。

### classmask

一个或多个角色职业。参见 [ChrClasses.dbc](chrclasses)。

### Spell

技能 ID。参见 [Skill.dbc](skillline)

### Rank

技能等级。

### Comment

技能描述。

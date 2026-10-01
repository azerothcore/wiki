# skill\_fishing\_base\_level

[<-返回至:World](database-world)

**`skill\_fishing\_base\_level` 表**

此表控制在特定区域钓鱼所需的最低钓鱼技能等级。

**表结构**

| Field      | Type     | Attributes | Key | Null | Default | Extra | Comment          |
|------------|----------|------------|-----|------|---------|-------|------------------|
| [entry][1] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | 区域标识         |
| [skill][2] | SMALLINT  | SIGNED     |     | NO   | 0       |       | 基础技能等级要求 |

[1]: #entry
[2]: #skill

**字段说明**

### entry

区域 ID，参见 [AreaTable.dbc](areatable)。

### skill

在此区域钓鱼所需的最低钓鱼技能点数。

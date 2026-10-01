# playercreateinfo_spell_custom

[<-返回至:World](database-world)

**`playercreateinfo_spell_custom` 表**

该表保存了当 worldserver.conf 中启用 PlayerStart.AllSpells 设置时，新建角色应拥有的法术信息。此表中的角色由其种族和职业组合定义。

请注意，你必须在配置中将 PlayerStart.CustomSpells 设置为 1，否则此表不会生效。

**表结构**

| Field          | Type         | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [racemask][1]  | INT          | UNSIGNED   | PRI | NO   | 0       |       |         |
| [classmask][2] | INT          | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Spell][3]     | MEDIUMINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Note][4]      | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |

[1]: #racemask
[2]: #classmask
[3]: #spell
[4]: #note

**字段说明**

### racemask

一个或多个角色种族。参见 [ChrRaces.dbc](chrraces)。

### classmask

一个或多个角色职业。参见 [ChrClasses.dbc](chrclasses)

### Spell

法术 ID。参见 [Spell.dbc](spell)

### Note

基本上就是对你查询作用的注释。

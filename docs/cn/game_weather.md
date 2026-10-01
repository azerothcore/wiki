# game\_weather

[<-返回:世界](database-world)

**表结构**

该表保存着各个区域发生天气变化的百分比几率。并非所有区域都能改变天气。对于任何给定的区域，每个季节的所有天气类型的百分比之和应等于 100%，且不能超过 100%。

| 字段 (Field)                | 类型 (Type) | 属性 (Attributes) | 键 (Key) | 空 (Null) | 默认 (Default) | 额外 (Extra) | 注释 (Comment) |
| --------------------------- | ----------- | ----------------- | -------- | --------- | -------------- | ------------ | -------------- |
| [zone][1]                   | MEDIUMINT   | UNSIGNED          | PRI      | NO        |                |              |                |
| [spring_rain_chance][2]     | TINYINT     | UNSIGNED          |          | NO        |                |              |                |
| [spring_snow_chance][3]     | TINYINT     | UNSIGNED          |          | NO        |                |              |                |
| [spring_storm_chance][4]    | TINYINT     | UNSIGNED          |          | NO        |                |              |                |
| [summer_rain_chance][5]     | TINYINT     | UNSIGNED          |          | NO        |                |              |                |
| [summer_snow_chance][6]     | TINYINT     | UNSIGNED          |          | NO        |                |              |                |
| [summer_storm_chance][7]    | TINYINT     | UNSIGNED          |          | NO        |                |              |                |
| [fall_rain_chance][8]       | TINYINT     | UNSIGNED          |          | NO        |                |              |                |
| [fall_snow_chance][9]       | TINYINT     | UNSIGNED          |          | NO        |                |              |                |
| [fall_storm_chance][10]     | TINYINT     | UNSIGNED          |          | NO        |                |              |                |
| [winter_rain_chance][11]    | TINYINT     | UNSIGNED          |          | NO        |                |              |                |
| [winter_snow_chance][12]    | TINYINT     | UNSIGNED          |          | NO        |                |              |                |
| [winter_storm_chance][13]   | TINYINT     | UNSIGNED          |          | NO        |                |              |                |
| [ScriptName][14]            | CHAR(64)    |                   |          | NO        |                |              |                |

[1]: #zone
[2]: #springrainchance
[3]: #springsnowchance
[4]: #springstormchance
[5]: #summerrainchance
[6]: #summersnowchance
[7]: #summerstormchance
[8]: #fallrainchance
[9]: #fallsnowchance
[10]: #fallstormchance
[11]: #winterrainchance
[12]: #wintersnowchance
[13]: #winterstormchance
[14]: #scriptname

**字段说明**

### zone

该字段包含你想要为其改变天气的区域 ID，来自 [AreaTable DBC 文件](areatable)。

### spring\_rain\_chance

春季降雨的百分比几率

### spring\_snow\_chance

春季降雪的百分比几率

### spring\_storm\_chance

春季发生沙尘暴的百分比几率

### summer\_rain\_chance

夏季降雨的百分比几率

### summer\_snow\_chance

夏季降雪的百分比几率

### summer\_storm\_chance

夏季发生沙尘暴的百分比几率

### fall\_rain\_chance

秋季降雨的百分比几率

### fall\_snow\_chance

秋季降雪的百分比几率

### fall\_storm\_chance

秋季发生沙尘暴的百分比几率

### winter\_rain\_chance

冬季降雨的百分比几率

### winter\_snow\_chance

冬季降雪的百分比几率

### winter\_storm\_chance

冬季发生沙尘暴的百分比几率

### ScriptName

与该区域天气相关联的脚本名称，注册在核心（core）中以允许自定义天气处理。

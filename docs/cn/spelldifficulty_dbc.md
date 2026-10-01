# spelldifficulty\_dbc

[<-返回:世界数据库](database-world)

**\`spelldifficulty\_dbc\` 表**

该表根据地下城或团队副本的难度决定应使用哪个法术 ID。  

{% include note.html content="EPIC 难度值存在但目前尚未使用。" %}

**表结构**

| Field         | Type | Attributes | Key | Null | Default | Extra | Comment |
| ------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]       | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [DifficultySpellID_1][2] | INT  | UNSIGNED   |     | NO   | 0       |       | 普通地下城 / 10 人普通团队副本的法术 ID |
| [DifficultySpellID_2][3] | INT  | UNSIGNED   |     | NO   | 0       |       | 英雄地下城 / 25 人普通团队副本的法术 ID |
| [DifficultySpellID_3][4] | INT  | UNSIGNED   |     | NO   | 0       |       | 史诗地下城（未使用）/ 10 人英雄团队副本的法术 ID |
| [DifficultySpellID_4][5] | INT  | UNSIGNED   |     | NO   | 0       |       | 25 人英雄团队副本的法术 ID |

[1]: #id
[2]: #difficultyspellid1
[3]: #difficultyspellid2
[4]: #difficultyspellid3
[5]: #difficultyspellid4

**字段说明**

### ID
在脚本/SmartAI 中引用的法术 ID

### DifficultySpellID_1

在普通地下城或 10 人普通团队副本中使用的法术 ID。

### DifficultySpellID_2

在英雄地下城或 25 人普通团队副本中使用的法术 ID。

### DifficultySpellID_3

在史诗地下城（未使用）或 10 人英雄团队副本中使用的法术 ID。

### DifficultySpellID_4

在 25 人英雄团队副本中使用的法术 ID。

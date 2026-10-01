# autobroadcast_locale

[<-返回:Auth](database-auth)

**\`autobroadcast_locale\` 表**

**表结构**

| Field        | Type        | Attributes | Key | Null | Default | Extra | Comment |
| ------------ | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [realmid][1] | INT         |            | PRI | NO   |         |       |         |
| [id][2]      | INT         |            | PRI | NO   |         |       |         |
| [locale][3]  | VARCHAR(4)  |            | PRI | NO   |         |       |         |
| [text][4]    | VARCHAR(45) |            |     | YES  |         |       |         |


[1]: #realmid
[2]: #id
[3]: #locale
[4]: #text

## 字段说明

### realmid

要发送自动广播的 RealmID

-1 表示所有服务器

指定的服务器优先于 -1（所有服务器）

### id

自动广播 ID

### locale

自动广播的语言区域（locale）。
你可以从以下选项中选择：

| ID  | Language |
| --- | -------- |
| 1   | koKR     |
| 2   | frFR     |
| 3   | deDE     |
| 4   | zhCN     |
| 5   | zhTW     |
| 6   | esES     |
| 7   | esMX     |
| 8   | ruRU     |


### text

自动广播的文本。

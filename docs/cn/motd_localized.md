# motd_localized

[<-返回至:Auth](database-auth)

**\`motd_localized\` 表**

**表结构**

| Field        | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ------------ | ---------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [realmid][1] | INT        | SIGNED     | PRI | NO   |         |       |         |
| [locale][2]  | VARCHAR(4) |            |     | NO   |         |       |         |
| [text][3]    | LONGTEXT   |            |     | YES  | NULL    |       |         |


[1]: #realmid
[2]: #locale
[3]: #text

## 字段说明

### realmid

要发送的服务器公告（Motd）所对应的 RealmID

-1 表示所有服务器（全部领域）

指定特定领域优先于 -1（所有领域）

### locale

本地化服务器公告（motd）的语言。
你可以从以下选项中选择：

| ID | 语言 |
|----|------|
| 1  | koKR |
| 2  | frFR |
| 3  | deDE |
| 4  | zhCN |
| 5  | zhTW |
| 6  | esES |
| 7  | esMX |
| 8  | ruRU |


### text

本地化服务器公告（Motd）的文本内容

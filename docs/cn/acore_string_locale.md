# acore\_string\_locale

[<-返回:World](database-world)

**\`acore\_string\_locale\` 表**

此表保存 [acore\_string](acore_string) 文本的翻译，每个字符串和 locale 一行。英文文本仍保存在 [acore\_string.content\_default](acore_string#contentdefault) 中。

**表结构**

| Field               | Type       | Attributes | Key | Null | Default | Extra | Comment            |
| ------------------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------------------ |
| [entry](#entry)     | INT        | UNSIGNED   | PRI | NO   |         |       | acore_string.entry |
| [locale](#locale)   | VARCHAR(4) |            | PRI | NO   |         |       |                    |
| [content](#content) | TEXT       |            |     | NO   |         |       |                    |

**字段描述**

### entry

要翻译的字符串，对应 [acore\_string.entry](acore_string#entry)。

### locale

翻译的 locale 名称。

| Locale |
| ------ |
| koKR   |
| frFR   |
| deDE   |
| zhCN   |
| zhTW   |
| esES   |
| esMX   |
| ruRU   |

也可以使用由模块添加的 locale，例如 `itIT`。

### content

[acore\_string.content\_default](acore_string#contentdefault) 的翻译文本。

### 示例

```sql
DELETE FROM `acore_string_locale` WHERE `entry` = 1 AND `locale` = 'esES';
INSERT INTO `acore_string_locale` (`entry`, `locale`, `content`) VALUES
(1, 'esES', 'Debes seleccionar un personaje o una criatura.');
```

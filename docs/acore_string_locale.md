# acore\_string\_locale

[<-Back-to:World](database-world)

**The \`acore\_string\_locale\` table**

This table holds the translations of the [acore\_string](acore_string) texts, one row per string and locale. The English text stays in [acore\_string.content\_default](acore_string#contentdefault).

**Table Structure**

| Field               | Type       | Attributes | Key | Null | Default | Extra | Comment            |
| ------------------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------------------ |
| [entry](#entry)     | INT        | UNSIGNED   | PRI | NO   |         |       | acore_string.entry |
| [locale](#locale)   | VARCHAR(4) |            | PRI | NO   |         |       |                    |
| [content](#content) | TEXT       |            |     | NO   |         |       |                    |

**Description of the fields**

### entry

The string to translate, from [acore\_string.entry](acore_string#entry).

### locale

The locale name of the translation.

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

A locale added by a module, for example `itIT`, can be used too.

### content

The translated text of [acore\_string.content\_default](acore_string#contentdefault).

### Example

```sql
DELETE FROM `acore_string_locale` WHERE `entry` = 1 AND `locale` = 'esES';
INSERT INTO `acore_string_locale` (`entry`, `locale`, `content`) VALUES
(1, 'esES', 'Debes seleccionar un personaje o una criatura.');
```

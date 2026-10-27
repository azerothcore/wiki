# acore\_string\_locale

[<-Volver a:World](database-world)

**Tabla \`acore\_string\_locale\`**

Esta tabla contiene las traducciones de los textos de [acore\_string](acore_string), una fila por cadena y localización. El texto en inglés se queda en [acore\_string.content\_default](acore_string#contentdefault).

**Estructura**

| Field               | Type       | Attributes | Key | Null | Default | Extra | Comment            |
| ------------------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------------------ |
| [entry](#entry)     | INT        | UNSIGNED   | PRI | NO   |         |       | acore_string.entry |
| [locale](#locale)   | VARCHAR(4) |            | PRI | NO   |         |       |                    |
| [content](#content) | TEXT       |            |     | NO   |         |       |                    |

**Descripción de los campos**

### entry

La cadena a traducir, de [acore\_string.entry](acore_string#entry).

### locale

El nombre de la localización de la traducción.

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

También se puede usar una localización añadida por un módulo, por ejemplo `itIT`.

### content

El texto traducido de [acore\_string.content\_default](acore_string#contentdefault).

### Ejemplo

```sql
DELETE FROM `acore_string_locale` WHERE `entry` = 1 AND `locale` = 'esES';
INSERT INTO `acore_string_locale` (`entry`, `locale`, `content`) VALUES
(1, 'esES', 'Debes seleccionar un personaje o una criatura.');
```

# guild

[<-Volver a:Characters](database-characters)

**Tabla \`guild\`**

En ésta tabla se alberga la información principal de cualquier hermandad del juego. Todas las hermandades creadas o en proceso de creación tienen un registro en esta tabla.

**Estructura**

| Field                | Type         | Attributes | Key | Null | Default | Extra  | Comment |
| -------------------- | ------------ | ---------- | --- | ---- | ------- | ------ | ------- |
| [guildid][1]         | INT          | UNSIGNED   | PRI | NO   | 0       |        |         |
| [name][2]            | VARCHAR(24)  | SIGNED     |     | NO   | ''      |        |         |
| [leaderguid][3]      | INT          | UNSIGNED   |     | NO   | 0       |        |         |
| [EmblemStyle][4]     | TINYINT      | UNSIGNED   |     | NO   | 0       |        |         |
| [EmblemColor][5]     | TINYINT      | UNSIGNED   |     | NO   | 0       |        |         |
| [BorderStyle][6]     | TINYINT      | UNSIGNED   |     | NO   | 0       |        |         |
| [BorderColor][7]     | TINYINT      | UNSIGNED   |     | NO   | 0       |        |         |
| [BackgroundColor][8] | TINYINT      | UNSIGNED   |     | NO   | 0       |        |         |
| [info][9]            | VARCHAR(500) | SIGNED     |     | NO   | ''      |        |         |
| [motd][10]           | VARCHAR(128) | SIGNED     |     | NO   | ''      |        |         |
| [createdate][11]     | INT          | UNSIGNED   |     | NO   | 0       |        |         |
| [BankMoney][12]      | BIGINT       | UNSIGNED   |     | NO   | 0       |        |         |

[1]: #guildid
[2]: #name
[3]: #leaderguid
[4]: #emblemstyle
[5]: #emblemcolor
[6]: #borderstyle
[7]: #bordercolor
[8]: #backgroundcolor
[9]: #info
[10]: #motd
[11]: #createdate
[12]: #bankmoney

**Descripción de los Campos**

### guildid

El ID correspondiente de la hermandad. Este número debe ser único, ya que es el principal método para poder identificarla.

### name

El nombre de la hermandad.

### leaderguid

GUID o Identificador Global Único del personaje que creó la hermandad. Véase [characters.guid](characters#guid).

### EmblemStyle

El estilo del emblema del tabardo de la hermandad.

### EmblemColor

El color del emblema del tabardo de la hermandad.

### BorderStyle

El tipo de bordado del tabardo de la hermandad.

### BorderColor

El color del bordado del tabardo de la hermandad.

### BackgroundColor

El color de fondo del tabardo del de la hermandad.

### info

El mensaje de texto que aparece en el recuadro de información de la hermandad.

### motd

El texto que aparece en el recuadro del mensaje diario de la hermandad.

### createdate

Fecha de creación de la hermandad.

### BankMoney

El dinero total, medido en monedas de cobre, que hay actualmente en el banco de la hermandad

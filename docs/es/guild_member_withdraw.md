# guild\_member\_withdraw

[<-Volver a:Characters](database-characters.md)

**Tabla \`guild\_member\_withdraw\`**

La tabla registra los objetos o dinero extraídos por el jugador.

**Estructura**

| Field      | Type  | Attributes | Key | Null | Default | Extra  | Comment |
| ---------- | ----- | ---------- | --- | ---- | ------- | ------ | ------- |
| [guid][1]  | INT   | UNSIGNED   | PRI | NO   |         |        |         |
| [tab1][2]  | INT   | UNSIGNED   |     | NO   | 0       |        |         |
| [tab1][3]  | INT   | UNSIGNED   |     | NO   | 0       |        |         |
| [tab2][4]  | INT   | UNSIGNED   |     | NO   | 0       |        |         |
| [tab3][5]  | INT   | UNSIGNED   |     | NO   | 0       |        |         |
| [tab4][6]  | INT   | UNSIGNED   |     | NO   | 0       |        |         |
| [tab5][7]  | INT   | UNSIGNED   |     | NO   | 0       |        |         |
| [money][8] | INT   | UNSIGNED   |     | NO   | 0       |        |         |

[1]: #guid
[2]: #tab
[3]: #tab
[4]: #tab
[5]: #tab
[6]: #tab
[7]: #tab
[8]: #money

**Descripción de los Campos**

### guid

`field-no-description|1` (¿Posiblemente el Identificador Global Único del jugador?)

### tab

`field-no-description|2-7` (¿La pestaña en dónde extrajo el item? Recordemos que son 6 columnas a partir de ésta que poseen el mismo nombre.)

### money

`field-no-description|8` (¿Dinero extraído por el jugador? Medido en monedas de cobre.)

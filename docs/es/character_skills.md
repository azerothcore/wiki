# character\_skills

[<-Volver a:Characters](database-characters.md)

**Tabla \`character\_skills\`**

La tabla contiene un listado de todas las habilidades de cada personaje.

**Estructura**

| Field      | Type     | Attributes | Key | Null | Default | Extra | Comment                  |
| ---------- | -------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]  | INT      | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [skill][2] | SMALLINT | UNSIGNED   | PRI | NO   | 0       |       |                          |
| [value][3] | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |
| [max][4]   | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #skill
[3]: #value
[4]: #max

**Descripción de los Campos**

### guid

Globally Unique Identifier o Identificador Global Único del personaje. Véase [characters.guid](characters#guid).

### skill

La habilidad que posee el personaje. Un listado de las mismas puede hallarse aquí mismo.

### value

El rango (valor) actual que posee el personaje de cierta habilidad.

### max

El valor más alto posible para la habilidad dada dentro de un rango determinado.

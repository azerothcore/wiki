# character\_queststatus\_monthly

[<-Volver a:Characters](database-characters)

**Tabla \`character\_queststatus\_monthly\`**

**Estructura**

| Campo       | Tipo | Atributos | Llave | Nulo | Por defecto | Extra  | Comentario                 |
| ----------- | ---- | --------- | ----- | ---- | ----------- | ------ | -------------------------- |
| [guid][1]   | INT  | UNSIGNED  | PRI   | NO   | 0           |        | Identificador único global |
| [quest][2]  | INT  | UNSIGNED  | PRI   | NO   | 0           |        | Identificador de misión    |

[1]: #guid
[2]: #quest

**Descripción de los campos**

### guid

El guid del personaje. Ver [characters.guid](characters#guid).

### quest

El ID de misión de la misión recompensada. Ver [quest\_template.id](quest_template#id).

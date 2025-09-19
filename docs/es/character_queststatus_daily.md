# character\_queststatus\_daily

[<-Volver a:Characters](database-characters)

**Tabla \`character\_queststatus\_daily\`**

Contiene información sobre el estado de las misiones diarias de cada jugador. La misión debe tener el tipo = 87 o la bandera 4096 en QuestFlags.

**Estructura**

| Campo      | Tipo    | Atributos | Llave | Nulo | Por defecto | Extra | Comentario                 |
|----------- | ------- | --------- | ----- | ---- | ----------- | ----- | -------------------------- |
| [guid][1]  | INT     | UNSIGNED  | PRI   | NO   | 0           |       | Identificador único global |
| [quest][2] | INT     | UNSIGNED  | PRI   | NO   | 0           |       | Identificador de misión    |
| [time][3]  | INT     | UNSIGNED  |       | NO   | 0           |       |                            |

[1]: #guid
[2]: #quest
[3]: #time

**Descripción de los campos**

### guid

El GUID del carácter. Consulte [characters.guid](characters#guid).

### quest

El ID de misión de la misión diaria. Ver  [quest\_template.entry](quest\_template#entry).

### time

El momento en que se realizó la búsqueda, en tiempo Unix.

# character\_battleground\_data

[<-Volver a:Characters](database-characters)

**Tabla \`character\_battleground\_data\`**

Esta tabla contiene información de cada personaje en un campo de batalla. También contiene información sobre su última posición antes de unirse al campo de batalla.

**Estructura**

| Campo            | Tipo      | Atributos | Llave | Nulo | Por defecto | Extra | Comentario                 |
|------------------|-----------|-----------|-------|------|-------------|-------|----------------------------|
| [guid][1]        | INT       | UNSIGNED  | PRI   | NO   | 0           |       | Identificador único global |
| [instanceId][2]  | INT       | UNSIGNED  |       | NO   | 0           |       | Identificador de instancia |
| [team][3]        | SMALLINT  | UNSIGNED  |       | NO   |             |       |                            |
| [joinX][4]       | FLOAT     | SIGNED    |       | NO   | 0           |       |                            |
| [joinY][5]       | FLOAT     | SIGNED    |       | NO   | 0           |       |                            |
| [joinZ][6]       | FLOAT     | SIGNED    |       | NO   | 0           |       |                            |
| [joinO][7]       | FLOAT     | SIGNED    |       | NO   | 0           |       |                            |
| [joinMapId][8]   | SMALLINT  | UNSIGNED  |       | NO   | 0           |       | Identificador de mapa      |
| [taxiStart][9]   | INT       | UNSIGNED  |       | NO   | 0           |       |                            |
| [taxiEnd][10]    | INT       | UNSIGNED  |       | NO   | 0           |       |                            |
| [mountSpell][11] | MEDIUMINT | UNSIGNED  |       | NO   | 0           |       |                            |

[1]: #guid
[2]: #instanceid
[3]: #team
[4]: #joinx
[5]: #joiny
[6]: #joinz
[7]: #joino
[8]: #joinmapid
[9]: #taxistart
[10]: #taxiend
[11]: #mountspell

**Descripción de los campos**

### guid

La guía de personajes. Ver [characters.guid](2129969.html#characters(table)-id).

### instanceId

Esta es la instancia Id. del campo de batalla. Se comparte con [instance.id](instance_2130197.html#instance-id), pero en lugar de poner los datos en esa tabla, están aquí.

### team

Identificación del equipo.:

| ID  | Descripción |
|-----|-------------|
| 0   | GM          |
| 67  | Horde       |
| 469 | Alliance    |

### joinX

Última posición X del personaje antes de unirse a un campo de batalla.

### joinY

Última posición Y del personaje antes de unirse a un campo de batalla.

### joinZ

Última posición Z del personaje antes de unirse a un campo de batalla.

### joinO

Última orientación del personaje antes de unirse a un campo de batalla.

### joinMapId

Último mapId del personaje antes de unirse a un campo de batalla.

### taxiStart

Último nodo de taxi del personaje antes de unirse a un campo de batalla.

### taxiEnd

El personaje se dirige al nodo de taxi antes de unirse a un campo de batalla.

### mountSpell

El ID del hechizo de montura. Véase la columna 1 de Spell.dbc.

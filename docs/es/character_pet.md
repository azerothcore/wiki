# character\_pet

[<-Volver a:Characters](database-characters)

**Tabla \`character\_pet\`**

La tabla alberga datos de cada mascota invocada por cualquier jugador dentro del juego.

**Estructura**

| Field               | Type        | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]             | INT         | UNSIGNED   | PRI | NO   | 0       |       |         |
| [entry][2]          | INT         | UNSIGNED   |     | NO   | 0       |       |         |
| [owner][3]          | INT         | UNSIGNED   |     | NO   | 0       |       |         |
| [modelid][4]        | INT         | UNSIGNED   |     | YES  | 0       |       |         |
| [CreatedBySpell][5] | MEDIUMINT   | UNSIGNED   |     | NO   | 0       |       |         |
| [PetType][6]        | TINYINT     | UNSIGNED   |     | NO   | 0       |       |         |
| [level][7]          | SMALLINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [exp][8]            | INT         | UNSIGNED   |     | NO   | 1       |       |         |
| [Reactstate][9]     | TINYINT     | UNSIGNED   |     | NO   | 0       |       |         |
| [name][10]          | VARCHAR(21) | SIGNED     |     | NO   | 0       |       |         |
| [renamed][11]       | TINYINT     | UNSIGNED   |     | NO   | Pet     |       |         |
| [slot][12]          | TINYINT     | UNSIGNED   |     | NO   | 0       |       |         |
| [curhealth][13]     | INT         | UNSIGNED   |     | NO   | 0       |       |         |
| [curmana][14]       | INT         | UNSIGNED   |     | NO   | 1       |       |         |
| [curhappiness][15]  | INT         | UNSIGNED   |     | NO   | 0       |       |         |
| [savetime][16]      | INT         | UNSIGNED   |     | NO   | 0       |       |         |
| [abdata][17]        | TEXT        | SIGNED     |     | YES  | 0       |       |         |

[1]: #id
[2]: #entry
[3]: #owner
[4]: #modelid
[5]: #createdbyspell
[6]: #pettype
[7]: #level
[8]: #exp
[9]: #reactstate
[10]: #name
[11]: #renamed
[12]: #slot
[13]: #curhealth
[14]: #curmana
[15]: #curhappiness
[16]: #savetime
[17]: #abdata

**Descripción de los Campos**

### id

ID (Identificador único) de la mascota en cuestión. Se trata de una ID única dentre todas las mascotas.

### entry

Entry de la criatura (mascota). Véase [creature\_template.entry](creature_template#entry).

### owner

GUID o Identificador Global único del personaje dueño de la mascota. Véase [characters.guid](characters#guid).

### modelid

ID de aquél modelo que será utilizado para mostrarse en la mascota en cuestión.

### CreatedBySpell

ID del hechizo en cuestión que ha invocado la mascota del jugador. Para los cazadores, suele ser el hechizo Domesticar bestia. Para los brujos u otras clases (magos), es la ID del hechizo que invocó a la criatura. Véase [Spell.dbc](spell) columna número 1.

### PetType

Tipo de mascota. 0 = mascota invocada, 1 = mascota domesticada.

### level

El nivel actual de la misma.

### exp

Experiencia actual que posée la mascota en cuestión. Para mascotas invocadas, este campo es siempre 0.

### Reactstate

El estado actual de ataque de la mascota (pasivo, agresivo, etc).

### name

El nombre de la mascota.

### renamed

Booleano del 0 al 1. 1 = La mascota ha sido renombrada, 0 = La mascota nunca ha sido renombrada y sigue usando el mismo nombre con el que la criatura que fue domesticada.

### slot

Ranura en la que se encuentra la mascota.

- La ranura número 0 es para una mascota activa, quiere decir que se encuentra con el jugador.
- Las ranuras del 1 al 4 es para mascotas en se encuentren en el establo.
- La ranura número '100' es para aquella mascota que se encuentra con el jugador, pero que actualmente está retirada.

### curhealth

Salud actual de la mascota, en el momento que se guardó la Base de Datos.

### curmana

Maná actual de la mascota, en el momento que se guardó la Base de Datos.

### curhappiness

Felicidad actual de la mascota.

### savetime

La hora en que se guardó la mascota por última vez, medido en tiempo Unix.

### abdata

`field-no-description|17` (¿?)

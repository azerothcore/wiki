# guild\_bank\_tab

[<-Volver a:Characters](database-characters)

**Tabla \`guild\_bank\_tab\`**

La tabla alberga información acerca de todas las pestañas que se encuentren en uso actualmente, para todas las hermandades que hacen uso del banco de hermandad.

**Estructura**

| Field        | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------ | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [guildid][1] | INT          | UNSIGNED   | PRI | NO   | 0       |       |         |
| [TabId][2]   | TINYINT      | UNSIGNED   | PRI | NO   | 0       |       |         |
| [TabName][3] | VARCHAR(16)  | SIGNED     |     | NO   | "       |       |         |
| [TabIcon][4] | VARCHAR(100) | SIGNED     |     | NO   | "       |       |         |
| [TabText][5] | VARCHAR(500) | SIGNED     |     | YES  |         |       |         |

[1]: #guildid
[2]: #tabid
[3]: #tabname
[4]: #tabicon
[5]: #tabtext

**Descripción de los Campos**

### guildid

ID de la hermandad a la que pertenece el banco de hermandad.

### TabId

ID de la pestaña del banco de hermandad.

### TabName

El nombre asignado a la pestaña correspondiente.

### TabIcon

El ícono asignado a la pestaña correspondiente.

### TabText

El texto asignado a la pestaña correspondiente.

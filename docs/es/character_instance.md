# character\_instance

[<-Volver a:Characters](database-characters.md)

**Tabla \`character\_instance\`**

Alberga datos de instancia para los personajes en cuestión.

**Estructura**

| Field          | Type    | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]      | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [instance][2]  | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [permanent][3] | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |
| [extended][4]  | TINYINT | UNSIGNED   |     | NO   |         |       |         |

[1]: #guid
[2]: #instance
[3]: #permanent
[4]: #extended

**Descripción de los Campos**

### guid

GUID o Identificador Global Único del personaje. Véase [characters.guid](characters#guid).

### instance

Identificador (ID) de la instancia correspondiente. Véase [instance.id](instance#id).

### permanent

Booleano del 0 al 1 que controla si el jugador ha sido vinculado en alguna instancia en particular. Un jugador está vinculado a la instancia sólo cuando él (o su Grupo/Raid) asesina a una criatura con el marcador o 'flag' CREATURE\_FLAG\_EXTRA\_INSTANCE\_BIND establecido en el campo [flags\_extras](creature_template#creature_template-flags_extra).

### extended

`field-no-description|4` (¿?)

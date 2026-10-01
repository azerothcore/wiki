# spawn\_group

[<-Volver a:World](database-world)

**Tabla \`spawn\_group\`**

Esta tabla asigna los spawns individuales de creatures y gameobjects a sus grupos de spawn. Cada spawn puede pertenecer a un grupo, que controla su comportamiento de respawn mediante los flags definidos en [spawn\_group\_template](spawn_group_template).

**Estructura**

| Field                   | Type    | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [groupId](#groupid)     | INT     | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [spawnType](#spawntype) | TINYINT | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [spawnId](#spawnid)     | INT     | UNSIGNED   | PRI | NO   | NULL    |       |         |

**Descripción de los campos**

### groupId

Este es el ID de grupo del grupo. Debe coincidir con un grupo que ya exista en la tabla [spawn\_group\_template](spawn_group_template).

### spawnType

Este es el tipo de spawn:

| Value | Type       |
| ----- | ---------- |
| 0     | Creature   |
| 1     | GameObject |

### spawnId

Este es el ID de spawn (GUID) de la creature o gameobject que debe incluirse en el grupo. El ID debe existir en las tablas [creature](creature) o [gameobject](gameobject) respectivamente.

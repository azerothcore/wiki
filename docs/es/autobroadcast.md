# autobroadcast

[<-Volver a:Auth](database-auth)

**Tabla \`autobroadcast\`**

Esta tabla contiene las entradas de autobroadcast para tus reinos. Los valores como su actividad, posición y temporizador (\*.On, \*.Center, \*.Timer) se definen dentro de [worldserver.conf](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/worldserver/worldserver.conf.dist). Se eligen al azar, en función de su tamaño.

**Estructura**

| Campo        | Tipo     | Atributos | Llave | Nulo | Por defecto | Extra          | Comentario |
| ------------ | -------- | --------- | ----- | ---- | ----------- | -------------- | ---------- |
| [realmid][1] | INT      | SIGNED    | PRI   | NO   | -1          |                |            |
| [id][2]      | TINYINT  | UNSIGNED  | PRI   | NO   |             | AUTO_INCREMENT |            |
| [weight][3]  | TINYINT  | UNSIGNED  |       | YES  | 1           |                |            |
| [text][4]    | LONGTEXT | SIGNED    |       | NO   |             |                |            |

[1]: #realmid
[2]: #id
[3]: #weight
[4]: #text

**Descripción de los campos**

### realmid

El [realmlist.id](realmlist#id). Define a qué reino pertenece esta entrada. Utilice **-1** para que todos los reinos la usen.

### id

Clave de identificación única por reino. Las entradas con el mismo ID se anularán entre sí sin advertencias - esto se puede utilizar para reemplazar la entrada -1 en un reino específico.

### weight

Un número entero no negativo. Las entradas con mayor peso tienen más posibilidades de aparecer.

### text

El texto a emitir. Se pueden utilizar códigos de color y de formación de items/hechizos/quests.

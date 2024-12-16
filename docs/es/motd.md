# motd

[<-Back-to:Auth](database-auth)

**La tabla `motd`**

**Estructura de la tabla**

| Campo        | Tipo       | Atributos | Clave | Nulo | Predeterminado | Extra | Comentario |
| ------------ | ---------- | --------- | ----- | ---- | -------------- | ----- | ---------- |
| [realmid][1] | INT        | SIGNED    | PRI   | NO   |                |       |            |
| [text][2]    | LONGTEXT   |           |       | SÍ   | NULL           |       |            |


[1]: #realmid
[2]: #text

## Descripción de los campos

### realmid

ID del Realm para el Motd que se enviará

-1 para todos los realms

Un realm específico tiene prioridad sobre -1 (Todos los Realms)

### text

El texto para el Motd

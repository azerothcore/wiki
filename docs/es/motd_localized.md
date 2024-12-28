# motd

[<-Back-to:Auth](database-auth)

**La tabla `motd_localized`**

**Estructura de la tabla**

| Campo        | Tipo       | Atributos | Clave | Nulo | Predeterminado | Extra | Comentario |
| ------------ | ---------- | --------- | ----- | ---- | -------------- | ----- | ---------- |
| [realmid][1] | INT        | SIGNED    | PRI   | NO   |                |       |            |
| [locale][2]  | VARCHAR(4) |           |       | NO   |                |       |            |
| [text][3]    | LONGTEXT   |           |       | SÍ   | NULL           |       |            |


[1]: #realmid
[2]: #locale
[3]: #text

## Descripción de los campos

### realmid

ID del Realm para el Motd que se enviará

-1 para todos los realms

Un realm específico tiene prioridad sobre -1 (Todos los Realms)

### locale

El locale para el Motd localizado.
Puedes elegir entre los siguientes:

| ID | Idioma |
|----|--------|
| 1  | koKR   |
| 2  | frFR   |
| 3  | deDE   |
| 4  | zhCN   |
| 5  | zhTW   |
| 6  | esES   |
| 7  | esMX   |
| 8  | ruRU   |


### text

El texto para el Motd localizado

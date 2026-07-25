# autobroadcast_locale

[<-Volver a:Auth](database-auth)

**Tabla \`autobroadcast_locale\`**

**Estructura**

| Field        | Type        | Attributes | Key | Null | Default | Extra | Comment |
| ------------ | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [realmid][1] | INT         |            | PRI | NO   |         |       |         |
| [id][2]      | INT         |            | PRI | NO   |         |       |         |
| [locale][3]  | VARCHAR(4)  |            | PRI | NO   |         |       |         |
| [text][4]    | VARCHAR(45) |            |     | YES  |         |       |         |


[1]: #realmid
[2]: #id
[3]: #locale
[4]: #text

## Descripción de los campos

### realmid

RealmID al que se enviará el autobroadcast

-1 para todos los realms

Un realm especificado tiene prioridad sobre -1 (Todos los realms)

### id

ID del autobroadcast

### locale

La localización del autobroadcast. 
Puedes elegir entre las siguientes:

| ID  | Language |
| --- | -------- |
| 1   | koKR     |
| 2   | frFR     |
| 3   | deDE     |
| 4   | zhCN     |
| 5   | zhTW     |
| 6   | esES     |
| 7   | esMX     |
| 8   | ruRU     |


### text

El texto del autobroadcast.

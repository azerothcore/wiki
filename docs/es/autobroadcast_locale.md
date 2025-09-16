# autobroadcast_locale

[<-Volver a:Auth](database-auth)

**La \`autobroadcast_locale\` tabla**

**Estructura**

| Campo        | Tipo        | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| ------------ | ----------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [realmid][1] | INT         |           | PRI   | NO   |             |       |            |
| [id][2]      | INT         |           | PRI   | NO   |             |       |            |
| [locale][3]  | VARCHAR(4)  |           | PRI   | NO   |             |       |            |
| [text][4]    | VARCHAR(45) |           |       | YES  |             |       |            |


[1]: #realmid
[2]: #id
[3]: #locale
[4]: #text

## Descripción de los campos

### realmid

RealmID para el envío de la transmisión automática

-1 para todos los reinos

Un reino específico es superior a -1 (Todos los reinos)

### id

ID de transmisión automática

### locale

La configuración regional para la transmisión automática. 
Puede elegir entre las siguientes opciones:

| ID  | Language |
| --- | -------- |
| 1   | ko\_KR   |
| 2   | fr\_FR   |
| 3   | de\_DE   |
| 4   | zh\_CN   |
| 5   | zh\_TW   |
| 6   | es\_ES   |
| 7   | es\_MX   |
| 8   | ru\_RU   |

### text

El texto para la transmisión automática.

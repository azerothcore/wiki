# realmcharacters

[<-Volver a:Auth](database-auth.md)

Leer en: [English :gb:](../realmcharacters) [Spanish :es:](realmcharacters)

**Tabla \`realmcharacters\`**

Esta tabla contiene información sobre el número de personajes que tiene cada cuenta para cada reino.
Los datos de esta tabla son mantenidos por el núcleo.

**Estructura**

| Field         | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ------------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [realmid][1]  | INT        | UNSIGNED   | PRI | NO   | 0       |       |         |
| [acctid][2]   | INT        | UNSIGNED   | PRI | NO   |         |       |         |
| [numchars][3] | TINYINT    | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #realmid
[2]: #acctid
[3]: #numchars

**Descripción de los campos**

### realmid

El ID del reino. Ver [realmlist.id](realmlist#id).

### acctid

El ID de la cuenta. Ver [account.id](account#id).

### numchars

El número de personajes que tiene la cuenta en el reino.

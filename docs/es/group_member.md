# group\_member

[<-Volver a:Characters](database-characters.md)

**Tabla \`group\_member\`**

La tabla alberga información acerca de los miembros de un grupo creado.

**Estructura**

| Field            | Type    | Attributes | Key | Null | Default | Extra  | Comment |
| ---------------- |-------- | ---------- | --- | ---- | ------- | ------ | ------- |
| [guid][1]        | INT     | UNSIGNED   |     | NO   |         |        |         |
| [memberGuid][2]  | INT     | UNSIGNED   | PRI | NO   |         | Unique |         |
| [memberFlags][3] | TINYINT | UNSIGNED   |     | NO   | 0       |        |         |
| [subgroup[4]     | TINYINT | UNSIGNED   |     | NO   | 0       |        |         |
| [roles][5]       | TINYINT | UNSIGNED   |     | NO   | 0       |        |         |

[1]: #guid
[2]: #memberguid
[3]: #memberflags
[4]: #subgroup
[5]: #roles

**Descripción de los Campos**

#### guid

GUID o Identificador Global Único del grupo. Véase [groups.guid](groups#guid).

#### memberGuid

GUID o Identificador Global Único del jugador miembro del grupo. Véase [characters.guid](characters#guid).

| Nombre                   | Valor | Único  | Comentarios
|------------------------- | ----- | ------ | -------------------------------- |
| MEMBER_FLAG_ASSISTANT    | 0x01  |        | Asistente                        |
| MEMBER_FLAG_MAINTANK     | 0x02  | (U)    | Tanque Principal                 |
| MEMBER_FLAG_MAINASSIST   | 0x04  | (U)    | Asistente Principal              |

*(U) = Único por grupo.*

### subgroup

Con un rango de 0 a 7 (1-8 en el cliente), representan los subgrupos de un grupo de Banda.
Sólo pueden haber 5 miembros en un subgrupo por grupo de Banda.

### roles

| Valor | Nombre      | Comentarios                                                                            |
|------ | ----------- | -------------------------------------------------------------------------------------- |
| 0     | ROLE_NONE   |                                                                                        |
| 1     | ROLE_LEADER | El personaje ha sido asignado en un Buscador de Mazmorras Aleatorio como experimentado |
| 2     | ROLE_TANK   | El personaje ha sido asignado en un Buscador de Mazmorras Aleatorio como Tanque        |
| 4     | ROLE_HEALER | El personaje ha sido asignado en un Buscador de Mazmorras Aleatorio como Sanador       |
| 8     | ROLE_DAMAGE | El personaje ha sido asignado en un Buscador de Mazmorras Aleatorio como Daño          |

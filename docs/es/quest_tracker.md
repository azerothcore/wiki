# quest\_tracker

[<-Back-to:Character](database-character.md)

Leer en: [English :gb:](../quest_tracker) [Spanish :es:](quest_tracker)

**Tabla \`quest\_tracker\`**

**Estructura**

| Field                   | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
|[id][1]                  | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
|[character_guid][2]      | INT          | UNSIGNED   |     | NO   | 0       |       |         |
|[quest_accept_time][3]   | DATETIME     | SIGNED     |     | NO   |         |       |         |
|[quest_complete_time][4] | DATETIME     | SIGNED     |     | YES  |         |       |         |
|[quest_abandon_time][5]  | DATETIME     | SIGNED     |     | YES  |         |       |         |
|[completed_by_gm][6]     | TINYINT      | SIGNED     |     | NO   | 0       |       |         |
|[core_hash][7]           | VARCHAR(120) | SIGNED     |     | NO   | 0       |       |         |
|[core_revision][8]       | VARCHAR(120) | SIGNED     |     | NO   | 0       |       |         |

[1]: #id
[2]: #characterguid
[3]: #questaccepttime
[4]: #questcompletetime
[5]: #questabandontime
[6]: #completedbygm
[7]: #corehash
[8]: #corerevision

**Descripción de los campos**

### id

`campo-sin-descripción|1`

### character\_guid

Ver [characters.guid](characters#guid).

### quest\_accept\_time

Cuando la misión fue aceptada.

### quest\_complete\_time

Cuando se completó la misión.

### quest\_abandon\_time

Cuando la misión fue abandonada.

### completed\_by\_gm

`campo-sin-descripción|6`

### core\_hash

`campo-sin-descripción|7`

### core\_revision

`campo-sin-descripción|8`

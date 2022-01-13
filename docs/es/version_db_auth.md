# version\_db\_auth

[<-Volver a:Auth](database-auth.md)

Leer en: [English :gb:](../version_db_auth) [Spanish :es:](version_db_auth)

**Tabla \`version\_db\_auth\`**

| Field              | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [sql_rev][1]       | VARCHAR(100) | SIGNED     | PRI | NO   |         |       |         |
| [required_rev][2]  | VARCHAR(100) | SIGNED     | MUL | YES  |         |       |         |
| [date][3]          | VARCHAR(50)  | SIGNED     |     | YES  |         |       |         |
| [2021_06_17_00][4] | BIT(1)       | SIGNED     |     | YES  |         |       |         |

[1]: #sqlrev
[2]: #requiredrev
[3]: #date
[4]: #2021061700

**Descripción de los campos**

### sql\_rev

Revisión sql.

### required\_rev

Revisión requerida.

### date 

Fecha de las actualizaciones sql.

### 2021\_06\_17\_00

La fecha de la última actualizacion de la base datos auth.

**Nota** Esta columna cambia automaticamente acuerdo a la última actualizacion de la base de datos auth.

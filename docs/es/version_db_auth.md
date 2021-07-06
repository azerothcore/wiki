# version_db_auth

[<-Volver a:Auth](database-auth.md)

**Tabla \`version_db_auth\`**

| Field              | Type         | Attributes | Key | Null | Default | Extra | Comment |
|--------------------|--------------|------------|-----|------|---------|-------|---------|
| [sql_rev][1]       | VARCHAR(100) |            | PRI | NO   |         |       |         |
| [required_rev][2]  | VARCHAR(100) |            | MUL | YES  |         |       |         |
| [date][3]          | VARCHAR(50)  |            |     | YES  |         |       |         |
| [2021_06_17_00][4] | BIT(1)       |            |     | YES  |         |       |         |

[1]: #sqlrev
[2]: #requiredrev
[3]: #date
[4]: #2021061700

**Descripción de los campos**

### sql_rev

Revisión sql.

### required_rev

Revisión requerida.

### date 

Fecha de las actualizaciones sql.

### 2021_06_17_00

La fecha de la última actualizacion de la base datos auth.

**Nota** Esta columna cambia automaticamnete acuerdo a la última actualizacion de la base de datos auth 
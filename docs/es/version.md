# version

[<-Volver a: World](es/database-world)

**Tabla \`version\`**

Incluye información sobre la versión actual del core y de la base de datos.

**Estructura**

| Field               | Type         | Attributes | Key | Null | Default | Extra | Comment                         |
| ------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------------------------- |
| [core_version][1]   | VARCHAR(120) | SIGNED     |     | YES  | NULL    |       | Core revision dumped at startup |
| [core_revision][2]  | BIGINT       | UNSIGNED   |     | YES  | NULL    |       | Core revision hash              |
| [db_version][3]     | VARCHAR(120) | SIGNED     |     | YES  | NULL    |       | Version of world DB             |
| [script_version][4] | VARCHAR(120) | SIGNED     |     | YES  | NULL    |       | Version of scripts DB           |
| [cache_id][5]       | INT          | SIGNED     |     | YES  | 0       |       | Minor DB version                |

[1]: #core_version
[2]: #core_revision
[3]: #db_version
[4]: #script_version
[5]: #cache_id

**Descripción de los campos**

### core\_version

Descripción de texto completo de la versión del core en la que se está ejecutando actualmente tu servidor.
Ejemplo: TrinityCore rev. 8e48ef7863c5 2015-03-22 01:28:02 +0100 (6.x branch) (Win64, Release)

### core\_revision

Hash de la revisión del core en la que se está ejecutando actualmente tu servidor, p. ej. **Unknown** u **8e48ef7863c5**

### db\_version

Versión de la base de datos en la que se está ejecutando actualmente tu servidor. Ejemplo: **TDB .58**

### script\_version

`Version of scripts DB`

### cache\_id

`Minor DB version. Example: 58`

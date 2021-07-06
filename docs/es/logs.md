# logs

[<-Volver a:Auth](database-auth.md)

**Tabla \`logs\`**

Esta tabla almacena los registros de la base de datos de tipo `Appender` en el archivo de configuración.
Ejemplo de db appender:
```ini
Appender.DB=3,5,0
```

**Estructura**

| Field       | Type         | Attributes | Key | Null | Default | Extra | Comment |
|-------------|--------------|------------|-----|------|---------|-------|---------|
| [time][1]   | INT          | UNSIGNED   |     | NO   |         |       |         |
| [realm][2]  | INT          | UNSIGNED   |     | NO   |         |       |         |
| [type][3]   | VARCHAR(250) |            |     | NO   |         |       |         |
| [level][4]  | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [string][5] | text         |            |     | YES  |         |       |         |

[1]: #time
[2]: #realm
[3]: #type
[4]: #level
[5]: #string

**Descripción de los campos**

### time

Una marca de tiempo unixtime que indica cuándo se registró esta cadena.

### realm

El [RealmID](realmlist#id) del reino del que procede esta cadena de registro. 0 sí es realmd.

### type

El nombre del `Logger` de la configuración
Ejemplo de logger:
```ini
Logger.server=4,Console Server
```

### level

Depende del LogLevel en authserver.conf

| Valor | Descripción |
|-------|-------------|
| 1     | (Fatal)     |
| 2     | (Error)     |
| 3     | (Warning)   |
| 4     | (Info)      |
| 5     | (Debug)     |
| 6     | (Trace)     |

### string

La cadena real que se ha registrado.
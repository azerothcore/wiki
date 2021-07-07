# updates_include

[<-Volver a:Auth](database-auth.md)
[<-Volver a:Characters](database-characters.md)
[<-Volver a:World](database-world.md)

**Tabla \`updates_include\`**

**Estructura**

| Field      | Type         | Attributes               | Key | Null | Default  | Extra | Comment                                                         |
| ---------- | ------------ | ------------------------ | --- | ---- | -------- | ----- | --------------------------------------------------------------- |
| [path][1]  | VARCHAR(200) |                          | PRI | NO   |          |       | Directory to include. $ means relative to the source directory. |
| [state][2] | ENUM         | RELEASED,CUSTOM,ARCHIVED |     | NO   | RELEASED |       | Defines if the directory contains released or archived updates. |

[1]: #path
[2]: #state

## Descripción de los campos

### path

El directorio para incluir en las actualizaciones.

$ significa relativo al directorio de origen.

### state

Define si el directorio tiene actualizaciones publicadas, personalizadas o archivadas.

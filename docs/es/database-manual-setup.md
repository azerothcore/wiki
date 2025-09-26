---
redirect_from: "/Database-Manual-Setup"
---

# Configuración manual de la base de datos

##  Cómo configurar la base de datos AzerothCore manualmente

### Herramienta cliente MySQL

Para configurar su base de datos, puede usar el cliente MySQL que prefiera. Algunos ejemplos [aquí](database-management-tool).

Damos por hecho que ya sabes cómo realizar las tareas básicas, como crear una nueva base de datos, seleccionarla e importar un archivo de volcado de SQL. Si no es así, no te preocupes: es muy fácil y encontrarás muchas guías en Google, independientemente de la herramienta cliente MySQL que uses.

### Creando las bases de datos

Crea tres bases de datos vacías:

- `acore_world`
- `acore_characters`
- `acore_auth`


### Importando los archivos SQL

Los archivos SQL se encuentran en el directorio `/data/sql/`.

En `data/sql/base` están los archivos para crear la estructura base y el contenido para las 3 bases de datos (mundial, auth y characters).

De manera similar, en `data/sql/updates` están las actualizaciones que nuestros desarrolladores agregan con el tiempo.

Importar esos archivos manualmente uno por uno es un proceso largo que puede automatizarse. El script `apps/db_assembler/db_assembler.sh` permite ensamblarlos (es decir, fusionarlos), lo que agiliza el proceso de importación.

---
redirect_from: "/Database-Manual-Setup"
---

# Configuración manual de la base de datos

##  Cómo configurar la base de datos de AzerothCore manualmente

### Cliente MySQL

Para configurar tu base de datos, puedes usar el cliente MySQL que prefieras. Algunos ejemplos [aquí](es/Database-client).

Asumiremos que ya sabes cómo realizar las tareas básicas como crear una nueva base de datos, seleccionar una base de datos e importar un archivo de volcado SQL. Si no lo sabes, no te preocupes: es muy fácil y encontrarás muchas guías en Google, sea cual sea el cliente MySQL que uses.

### Crear las bases de datos

Crea tres bases de datos vacías:

- `acore_world`
- `acore_characters`
- `acore_auth`


### Importar los archivos SQL

Los archivos SQL están ubicados en el directorio `/data/sql/`.

En `data/sql/base` están los archivos para crear la estructura base y el contenido de las 3 bases de datos (world, auth y characters).

De forma similar, en `data/sql/updates` están las actualizaciones que nuestros desarrolladores añaden con el tiempo.

Importar esos archivos manualmente uno por uno es un proceso largo que se puede automatizar. El script `apps/db_assembler/db_assembler.sh` te permite ensamblar esos archivos (es decir, fusionarlos), de modo que el proceso de importarlos sea más rápido.

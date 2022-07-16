---
redirect_from: "/SQL-Versioning"
---

# Control de versiones SQL

Tenemos dos tipos de versiones:

- Versionado cronológico, Para los archivos sql aceptados
- Versionado por id, principalmente utilizado para sql pendientes

## Versionado cronológico

Utilizamos el viejo método `MaNGOS` para asegurarnos de que todos los archivos **/data/sql/updates/** se importan en el orden correcto, evitando la doble importación o la omisión de archivos. Para ello, utilizamos una **convención específica para los nombres de los archivos** y añadimos una **cabecera SQL** especial al principio de su contenido.

### Nombres de archivos

El nombre del archivo no debe ser renombrado y debe mantenerse como el nombre que `create_sql.sh` ha creado para el archivo.

El nombre del archivo tendrá este aspecto: `rev_XXXXXXXXXXXXXXXXXXX`

### Cabecera SQL

La cabecera SQL es una consulta especial que **debe** añadirse al principio del contenido de **cada** archivo de actualización sql.

El formato es el siguiente:

```sql
ALTER TABLE version_db_[database] CHANGE COLUMN [previous_file_name] [this_file_name] bit;
```

Sustituyendo:

- **[database]** con **world**, **character** o **auth**
- **[previous_file_name]** con el nombre del último archivo (sin extensión)
- **[this_file_name]** con el nombre del nuevo archivo en sí (sin extensión)

El siguiente es un ejemplo de la consulta del encabezado SQL (para la base de datos `auth`):

```sql
ALTER TABLE `version_db_auth` CHANGE COLUMN 2016_07_09_01 2016_07_10_00 bit;
```

## Control de versiones por ID

Los archivos sql pendientes no pueden utilizar el sistema de protección descrito anteriormente porque no podemos saber previamente la fecha en que serán aceptados. Así que estamos usando un versionado opcional (pero recomendado para los devs y especialmente para los pull requests).

Hemos introducido un campo dentro de las tablas `version_db_*` que es una cadena de clave primaria, y también un campo `required_rev` que se puede utilizar para permitir la relación por versiones.

Por ejemplo, puede crear una versión "X" que esté relacionada con una versión "Y" que no sea necesariamente la anterior.

actualmente utilizamos este comando bash para evitar, en la medida de lo posible, las colisiones entre revisiones:

```bash
date +%s%N
```

si se produce una colisión (extremadamente difícil), se puede resolver fácilmente de forma manual sin embargo.

La consulta final será:

```sql
INSERT INTO `version_db_auth` (`sql_rev`, `required_rev`) VALUES ('1472557015805232200','1472557004102672900');
```

o en caso de que no se requiera: `required_rev`:

```sql
INSERT INTO `version_db_auth` (`sql_rev`) VALUES ('1472557015805232200');
```

Añadiéndolo en la primera línea de su sql, genera un error en caso de doble importación; como por ejemplo para el versionado cronológico.

Hay un script bash en las carpetas pending_* que creará un sql con esta fila en la primera línea para usted, además nombrará el archivo que será reconocido por nuestro sistema de importación. Le sugerimos que lo utilice.

## El sistema de importación pendiente

Como se ha dicho antes, tenemos un flujo de trabajo especial para PR para permitir la consistencia de los datos de la base de datos para los desarrolladores. Requiere que se hagan algunas cosas en el sql de su RP para que sea compatible con nuestro sistema de importación y le permita evitar la doble importación de las mismas consultas.

La forma de hacerlo se describe en el artículo [Cómo crear un pull request](How-to-create-a-PR)

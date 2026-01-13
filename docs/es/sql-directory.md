# Directorio SQL

$ es relativo al directorio de origen.

## Crear y soltar archivos

Todos los archivos de creación y eliminación se encuentran en el directorio $\data\sql\create\.

`create_mysql.sql` contiene las consultas para crear el usuario acore y las bases de datos.

`drop_mysql.sql` elimina el usuario acore y todas las bases de datos.

## Archivos básicos

Todos los archivos base se encuentran en el directorio $\data\sql\base\.

Estos archivos contienen todos los datos de los últimos archivos de actualización comprimidos.

Los archivos de este directorio se importan automáticamente con el [Actualizador automático de bases de datos](database-installation#actualizador-automático-de-bases-de-datos).

## Actualizar archivos

Todos los archivos de actualización se encuentran en el directorio $\data\sql\updates\.

Estos archivos contienen todas las actualizaciones realizadas.

Los archivos de este directorio se importan automáticamente con el [Actualizador automático de bases de datos](database-installation#actualizador-automático-de-bases-de-datos).

## Archivos de actualización pendientes

Todos los archivos de actualización pendientes se encuentran en el directorio $\data\sql\updates\pending_db_*\.

Todos los cambios de SQL que realice para solucionar un problema en AzerothCore se incluyen aquí.

Para crear el archivo de actualización pendiente, ejecute el script create_sql.sh.

## Archivos personalizados

Todos los archivos personalizados se encuentran en el directorio $\data\sql\custom\.

Todas las actualizaciones personalizadas que realice en la base de datos deben almacenarse en archivos SQL dentro de este directorio para asegurarse de que no se pierdan al actualizar su servidor.

Los archivos de este directorio se importan automáticamente con el [Actualizador automático de bases de datos](database-installation#actualizador-automático-de-bases-de-datos).

## Archivos archivados

Directorio no utilizado.

## Archivos antiguos

Todos los archivos de actualización anteriores a ACDB 10.0.0 se almacenan aquí. A partir de ACDB 10.0.0, se introdujo un nuevo método para actualizar los archivos base.

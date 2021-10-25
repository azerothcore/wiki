# ESTÁNDARES de la WIKI

## NOMBRANDO LOS ARCHIVOS:

Los archivos de TABLAS DE BASE DE DATOS deben ser nombrados exactamente como están en la base de datos,

TODOS LOS DEMÁS ARCHIVOS deben ser nombrados en `minúsculas` y usar` -` (guiones) para los espacios.

LOS ARCHIVOS SHOLD NO contienen ningún carácter especial que no sea `-` (guiones). Si queremos un archivo llamado C++, lo llamamos cpp.

TODOS LOS ARCHIVOS WIKI deben terminar con `.md`.

## ARCHIVOS DE TABLA DE BASE DE DATOS:

TODOS LOS ARCHIVOS DE TABLA DE BASE DE DATOS deben estar presentes en su ARCHIVO DE BASE DE DATOS correcto.

Al agregar o eliminar una tabla, también debe actualizarse en `database-auth.md`` database-characters.md` `database-world.md`

## ENCABEZADOS DE ARCHIVOS

EL ARCHIVO DEBE EMPEZAR SIEMPRE CON `# Nombre de archivo`. (Esto es para mostrar la información correcta en la pestaña).

## TRADUCCIÓN

TODAS LAS TRADUCCIONES deben estar en un subdirectorio de /docs/ con la configuración regional abreviada del idioma. es decir, /docs/es/. Si no ha habido traducciones antes, debe permitir la ruta del directorio en el archivo config. Vea [este comentario sobre cómo hacerlo](https://github.com/azerothcore/wiki/commit/8b897c3384298674e82108357ee5e655f788229f).

¡TODOS LOS ARCHIVOS deben llamarse ** exactamente igual que las versiones en inglés **! Nunca traduzca los nombres de los archivos, solo el contenido que contiene.

## PÁGINAS ARCHIVADAS: (Aún no implementado)

TODAS LAS PÁGINAS ARCHIVADAS que potencialmente podrían tener algún tipo de valor deben agregarse en la lista `archive.md` y los enlaces a estas páginas deben eliminarse de otros lugares de la wiki.

También deben moverse a la carpeta /docs/archive/.

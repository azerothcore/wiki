# Estándares de la Wiki

## Nombres de los Archivos:

Los archivos de las tablas de la Base de Datos deben ser nombrados exactamente como están en la base de datos.

Todos los demás archivos deben ser nombrados en `minúsculas` y usar` -` (guiones) para los espacios.

Los archivos no deberían contener ningún carácter especial que no sea `-` (guiones). Si queremos un archivo llamado C++, lo llamamos CPP.

Todos los archivos Wiki deben terminar con `.md`.

## Codificación de Archivos

Todos los archivos deben ser codificados en UTF-8 para que funcionen en la Wiki.

## Encabezados de los Archivos 

El archivo debería iniciar siempre con `# Nombre del archivo`. (Esto para mostrar la información correcta en la pestaña.)

## Archivos de las tablas de la Base de Datos 

Todos los archivos de las tablas de la Base de Datos deben estar presentes en el archivo de Base de Datos correcto.

Al añadir o remover una tabla, también debe actualizarse en `database-auth.md` `database-characters.md` `database-world.md`

## Enlaces dentro de la Wiki

Al enlazar alguna página en la Wiki, usamos [enlaces relativos](https://semify.com/?Relative-Link&AID=1373#:~:text=For%20example%2C%20a%20relative%20link%20would%20only%20include%20/images%20/puppies.gif%20in%20the%20a%20href%20tag.). (`[home](home#overview)`).

Al enlazar a una página fuera de la wiki, usamos [enlaces absolutos](https://semify.com/?Relative-Link&AID=1373#:~:text=An%20absolute%20link%2C%20on%20the%20other%20hand%2C%20would%20include%20https%3A//%20www.%20example.com/%20image/%20puppies.gif%20in%20it.). (`[Google](https://google.com)`).

## Traducción

Todas las traducciones deberían estar en un sub directorio de /docs/ con el locale acortado del idioma. Por ejemplo: /docs/es/. Si no hay traducciones previas, debe habilitarse la ruta al directorio en la configuración. Véase [este commit de cómo hacerlo](https://github.com/azerothcore/wiki/commit/8b897c3384298674e82108357ee5e655f788229f).

Todos los archivos deben nombrarse **¡exactamente igual que las versiones en inglés. exact same as the English versions!** Nunca traduzca los nombres de los archivos, solo el contenido dentro de ellos..

## Paginas archivadas: (Sin implementar aún)

Todas las páginas archivadas que puedan, potencialmente, contener alguna clase de valor, deberían ser añadidas en la  lista `archive.md` y los enlaces a estas páginas deberían ser removidos de otros lugares en la Wiki.

Deberían también ser movidas a la carpeta /docs/archive/.

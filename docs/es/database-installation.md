# Instalación de la Base de Datos

| Guía de Instalación | |
| :- | :- |
| Este artículo es parte de la Guía de Instalación. Puede leerlo solo o hacer click en los links previos para navegar con facilidad entre los pasos. |
| [<< Paso 3: Configuración del Servidor](server-setup) | [Paso 5: Redes >>](networking) |

## Creación de la Base de Datos en MySQL

### Creación de la Base de Datos y el Usuario

Primero que todo, necesita crear el usuario acore usando el siguiente script.

https://github.com/azerothcore/azerothcore-wotlk/blob/master/data/sql/create/create_mysql.sql

Puede realizarlo con un cliente de MySQL o con la interfaz de comandos de MySQL (CLI).

Necesitará usar una cuenta root de MySQL con su cliente de  MySQL o con MySQL CLI antes de empezar a correr el servidor y usar alguno de esos archivos. (use un usuario root de MySQL solo para importar uno de esos archivos, NUNCA inicie el servidor con usuario root o administrator).

*Consejo: Puede cambiar la contraseña del usario que está creando para incrementar la seguridad.*

## Cargan de información a la Base de Datos

Puede hacer esto de dos maneras:
- Automatic Database Updater (Actualizador autmático de la base datos: predeterminado, recomendado)

Si quiere saber cómo funciona el directorio SQL o planea hacer cambios custom, le recomendamos leer [esto](sql-directory).

### Automatic Database Updater (Actualizador autmático de bases de datos: predeterminado, recomendado)

Por defecto, Worldserver y Authserver van a revisar e importar los nuevos archivos dentro de la base de datos que estén especificados en la configuración.

Esta es la forma recomendada y la más facil, para asegurarse de que siempre tiene la base de datos al día con el Core.

Para editar el actualizador automático de bases de datos, encontrará las configuraciones necesarias en authserver.conf y worldserver.conf en la opción [UPDATE SETTINGS](https://github.com/azerothcore/azerothcore-wotlk/commit/2d2857ce81db5297eb63d388d2e2f252ef52412d#diff-56b141374cf0384a2887c9fd490c6a79a3d2f31fb020ee0e423a5685344b59d3R30).

<br>

## Ayuda

Si sigue teniendo inconvenientes, revise:

* [Preguntas frecuentes](faq)

* [Errores Comunes](common-errors)

* [Cómo solicitar ayuda](how-to-ask-for-help)

* [Unase a nuestro discord](https://discord.gg/gkt4y2x). Aunque no es un canal de soporte 24/7, un miembro del staff le responderá siempre que tenga tiempo.


| Guía de Instalación | |
| :- | :- |
| Este artículo es parte de la Guía de Instalación. Puede leerlo solo o hacer click en los links previos para navegar con facilidad entre los pasos. |
| [<< Paso 3: Configuración del Servidor](server-setup) | [Paso 5: Redes >>](networking) |

# Instalación de la Base de Datos

| Guía de Instalación | |
| :- | :- |
| Este artículo es parte de la Guía de Instalación. Puede leerlo solo o hacer click en los links previos para navegar con facilidad entre los pasos. |
| [<< Paso 3: Configuración del Servidor](server-setup) | [Paso 5: Redes >>](networking) |

## Creación de la Base de Datos en MySQL

### Creación de la Base de Datos y el Usuario

Primero, debe crear el usuario acore. Debe ejecutar el siguiente script en un cliente MySQL o con la interfaz de línea de comandos (CLI) de MySQL.
Debe ejecutar el script como usuario **root** de MySQL dentro de un cliente MySQL o la CLI de MySQL.

https://github.com/azerothcore/azerothcore-wotlk/blob/master/data/sql/create/create_mysql.sql

{% include important_es.html content="Utilice el usuario root de MySQL SOLAMENTE para ejecutar el script anterior, ¡nunca ejecute el núcleo como root o administrador!" %}

{% include tip_es.html content="Puedes cambiar la contraseña del usuario que estás creando para mayor seguridad." %}

## Cargan de información a la Base de Datos

Si desea saber cómo funciona el directorio SQL o planea realizar cambios personalizados, le recomendamos leer [esto](sql-directory).

### Actualizador automático de bases de datos

La autorización y Worldserver verifican y aplican todos los archivos de base de datos necesarios al inicio.

Para editar el actualizador automático de la base de datos, encontrará las configuraciones necesarias en authserver.conf y worldserver.conf en **CONFIGURACIÓN DE ACTUALIZACIÓN**.

1. Inicie Authserver.exe, en la carpeta Build que creó, en la carpeta \bin\RelWithDebInfo o \bin\Debug.
2. Inicie Worldserver.exe, en la misma ubicación.

Si recibe el siguiente mensaje en su consola, presione Enter para crear y completar las bases de datos.

```
Database "acore_auth" does not exist
Do you want to create it? [yes (default) / no]:
```

<br>

## Ayuda

{% include help_es.html %}

| Guía de Instalación | |
| :- | :- |
| Este artículo es parte de la Guía de Instalación. Puede leerlo solo o hacer click en los links previos para navegar con facilidad entre los pasos. |
| [<< Paso 3: Configuración del Servidor](server-setup) | [Paso 5: Redes >>](networking) |

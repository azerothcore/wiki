# Instalación de la base de datos

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 3: Configuración del servidor](es/server-setup) | [Paso 5: Red >>](es/networking) |

## Crear la base de datos en MySQL

### Crear las bases de datos y el usuario

Primero, necesitas crear el usuario acore. Necesitas ejecutar el script de abajo dentro de un cliente de MySQL o con la interfaz de línea de comandos (CLI) de MySQL.
Necesitas ejecutar el script como el usuario **root** de MySQL dentro de un cliente de MySQL o de la CLI de MySQL.

https://github.com/azerothcore/azerothcore-wotlk/blob/master/data/sql/create/create_mysql.sql

{% include important.html content="¡Usa el usuario root de MySQL SOLO para ejecutar el script de arriba; nunca ejecutes el core como root o administrador!" %}

{% include tip.html content="Puedes cambiar la contraseña del usuario que estás creando para mayor seguridad." %}

## Cargar datos en la base de datos

Si quieres saber cómo funciona el directorio SQL o planeas hacer cambios personalizados, te recomendamos leer [esto](es/sql-directory).

#### Actualizador automático de la base de datos

El Auth- y el Worldserver comprueban y aplican todos los archivos de base de datos necesarios al iniciar.

Para editar el actualizador automático de la base de datos, encontrarás las configuraciones necesarias en authserver.conf y worldserver.conf bajo **UPDATE SETTINGS**.

1. Inicia Authserver.exe, en la carpeta Build que creaste, dentro de \bin\RelWithDebInfo o \bin\Debug.
2. Inicia Worldserver.exe, en la misma ubicación.

Si obtienes el siguiente mensaje en tu consola, presiona enter para crear y poblar las bases de datos.

```
Database "acore_auth" does not exist
Do you want to create it? [yes (default) / no]:
```

## Ayuda

Si sigues teniendo problemas, comprueba:

- [Preguntas frecuentes](es/faq)
- [Errores comunes](es/common-errors)
- [Cómo pedir ayuda](es/how-to-ask-for-help)
- [Únete a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del staff te responderá cuando tenga tiempo.

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 3: Configuración del servidor](es/server-setup) | [Paso 5: Red >>](es/networking) |

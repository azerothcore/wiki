# Configuración del servidor en Windows

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 2: Instalación del Core](es/windows-core-installation) | [Paso 4: Instalación de la base de datos >>](es/database-installation) |

**Tabla de contenidos**
- [Archivos de datos del cliente (descargar pre-extraídos)](#option-1-download-pre-extracted-files)
- [Extractores de datos del cliente (extraer los archivos tú mismo)](#option-2-extract-files-yourself)
- [Archivos de configuración: Worldserver y Authserver](#config-files-worldserver-and-authserver)

Ahora que tienes el código fuente compilado, necesitas añadir los datos del cliente necesarios. Puedes descargar los archivos ya extraídos o usar los extractores compilados para extraer los archivos tú mismo. Una vez que los datos estén listos, debes actualizar la opción **DataDir** en tu archivo **worldserver.conf** para que apunte al directorio que contiene los datos.

Algunos archivos son opcionales pero muy recomendados:

| Directorio | |
| :- | :- |
| dbc | Obligatorio |
| maps | Obligatorio |
| vmaps | MUY RECOMENDADO |
| mmaps | MUY RECOMENDADO |
| cameras | Recomendado |

## Opción 1: Descargar archivos pre-extraídos {#option-1-download-pre-extracted-files}

Si tienes intención de usar un cliente enUS, puedes descargar los archivos de datos de abajo. Si tienes intención de usar un cliente en cualquier otro idioma, necesitarás [extraer](#option-2-extract-files-yourself) los datos tú mismo.

<a class="no-icon" href="https://github.com/wowgaming/client-data/releases/" target="_blank"><i class="fa-solid fa-download"></i> Archivos de datos enUS (AC Data v19)</a>

1. Descarga los archivos de arriba.

2. Crea una nueva carpeta dentro de la carpeta de build llamada **Data**, p. ej. **C:\Build\bin\RelWithDebInfo\Data**

3. Extrae los archivos del zip y colócalos dentro de la carpeta **Data**.

4. Edita la opción de configuración [DataDir](#updating-datadir) con la ubicación de tu carpeta.

## Opción 2: Extraer los archivos tú mismo {#option-2-extract-files-yourself}

**(No es necesario si descargaste los archivos de arriba)**

1. Entra en tu directorio de build (**C:\Build\bin\RelWithDebInfo\\**) y copia los siguientes archivos en tu carpeta de World of Warcraft (donde se encuentra el wow.exe).
```
mapextractor.exe
mmaps_generator.exe
vmap4extractor.exe
vmap4assembler.exe
mmaps-config.yaml
```

2. Entra en **C:\Azerothcore\apps\extractor** y copia "**extractor.bat**" en tu carpeta de World of Warcraft junto con los archivos anteriores.

3. Crea las carpetas **mmaps** y **vmaps** en tu directorio de World of Warcraft.

4. Ejecuta extractor.bat y selecciona tus opciones de extracción.

**Importante:**

- ¡**dbc**, **maps** y **vmaps** son necesarios para que el servidor funcione correctamente!

- No intentes detener el proceso de extracción de **vmaps**. Termina cuando imprime "Press any key...". Creará dos carpetas nuevas: **buildings** y **vmaps**. La carpeta **buildings** es completamente inútil una vez ejecutado el proceso y se puede borrar sin problema.

- No ejecutes otra tarea antes de que la primera termine o tendrás errores.

- Si detienes vmap4extractor antes de que termine, necesitarás borrar el directorio Buildings antes de empezar de nuevo.

- **Opcional pero extremadamente recomendado: extrae los mmaps.** No intentes detener este proceso mientras extrae.

5. Crea una nueva carpeta en **C:\Build\bin\RelWithDebInfo** llamada **Data**

6. Mueve los vmaps, maps, dbc y cameras dentro de la carpeta **Data**.

## Archivos de configuración: Worldserver y Authserver {#config-files-worldserver-and-authserver}

Primero, localiza los dos archivos de configuración por defecto (llamados **worldserver.conf.dist** y **authserver.conf.dist**) y cópialos. Luego renombra las copias con sus mismos nombres pero sin la extensión .dist. Puedes encontrarlos en C:\Build\bin\RelWithDebInfo\configs\ (puede variar).

Abre los archivos .conf y baja hasta LoginDatabaseInfo, WorldDatabaseInfo y CharacterDatabaseInfo, e introduce la información de acceso de MySQL para que el servidor pueda acceder a tu base de datos.

En una configuración recién compilada, tendrás los siguientes valores por defecto:
```
LoginDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_auth" worldserver.conf / authserver.conf
WorldDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_world" worldserver.conf
CharacterDatabaseInfo = "127.0.0.1;3306;acore;acore;acore_characters" worldserver.conf
```

Siguen esta estructura:

```
Variablename = "MySQLIP;Port;Username;Password;database"
```

Deben verificarse los siguientes pasos:

- El hostname (127.0.0.1) puede quedarse igual si AzerothCore se está instalando en el mismo equipo en el que ejecutas WoW.
  Si no, sigue las instrucciones de la [tabla Realmlist](es/realmlist).

- El puerto (3306) es el valor estándar configurado. Si cambiaste el puerto por defecto en tu configuración de MySQL, debes cambiarlo en consecuencia.
  El usuario y la contraseña pueden variar. Puedes elegir entre:

    - usar el par de usuario y contraseña por defecto acore / acore.

    - crear un acceso único dentro del gestor de usuarios de tu herramienta de gestión de base de datos preferida (normalmente identificado por un icono con forma de una persona o personas) y darle los permisos necesarios (los permisos SELECT, INSERT, UPDATE, DELETE son suficientes, y es mucho más seguro).

### Actualizar DataDir {#updating-datadir}

1. En tu archivo **worldserver.conf** localiza la opción **DataDir**.

1. Edítala con la ruta de tu carpeta, p. ej. **C:\Build\bin\RelWithDebInfo\Data**

{% include tip.html content="Para la mayoría de los cambios de configuración de **worldserver.conf**, simplemente puedes escribir .reload config dentro del juego para ver los cambios al instante sin reiniciar el servidor." %}

{% include warning.html content="El equipo y los propietarios de AzerothCore NO patrocinan ni apoyan en ningún caso servidores públicos ilegales. Si utilizas estos proyectos para ejecutar un servidor público ilegal y no para probar y aprender, es tu propia elección personal." %}

### (Opcional) Opciones de configuración por variable de entorno

Es posible cargar opciones de configuración mediante variables de entorno, sobre lo que puedes leer [aquí](es/config-overrides-with-env-var).

## Ayuda

Si sigues teniendo problemas, comprueba:

- [Preguntas frecuentes](es/faq)
- [Errores comunes](es/common-errors)
- [Cómo pedir ayuda](es/how-to-ask-for-help)
- [Únete a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del staff te responderá cuando tenga tiempo.

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer clic en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 2: Instalación del Core](es/windows-core-installation) | [Paso 4: Instalación de la base de datos >>](es/database-installation) |

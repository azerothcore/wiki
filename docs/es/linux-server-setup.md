# Configuración del servidor en Linux

| Guía de instalación | |
| :- | :- |
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 2: Instalación del Core](es/linux-core-installation) | [Paso 4: Instalación de la base de datos >>](es/database-installation) |

**Tabla de contenidos**
- [Archivos de datos del cliente (descargar pre-extraídos)](#option-1-download-pre-extracted-files)
- [Extractores de datos del cliente (extraer los archivos tú mismo)](#option-2-extract-files-yourself)
- [Archivos de configuración: Worldserver y Authserver](#config-files-worldserver-and-authserver)

Ahora que tienes el código fuente compilado, necesitas añadir los datos del cliente necesarios. Puedes descargar los archivos ya extraídos o usar los extractores compilados para extraer los archivos tú mismo. Una vez que los datos estén listos, debes verificar que la opción **DataDir** en tu archivo **worldserver.conf** apunte al directorio que contiene los datos.

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

1. Descarga el archivo `data.zip`.

2. Extrae el contenido directamente en el directorio por defecto **$AC_CODE_DIR/env/dist/bin/**, tal como especifica la opción DataDir en **worldserver.conf**. Puedes elegir otra carpeta, pero necesitarás editar la opción de configuración [DataDir](#updating-datadir) con la ubicación de tu carpeta.

Estructura de carpetas por defecto de **$AC_CODE_DIR/env/dist/bin** (como la muestra `tree -L 1`):
```
.
├── authserver
├── Cameras
├── data-version
├── dbc
├── maps
├── mmaps
├── vmaps
└── worldserver
```

## Opción 2: Extraer los archivos tú mismo {#option-2-extract-files-yourself}

**(No es necesario si descargaste los archivos de arriba)**

1. Entra en tu directorio de instalación (p. ej. **$AC_CODE_DIR/env/dist/bin/**) y copia los siguientes archivos en tu carpeta de World of Warcraft (donde se encuentra el Wow.exe).
```
map_extractor
mmaps_generator
vmap4_assembler
vmap4_extractor
```

2. Entra en **$AC_CODE_DIR/apps/extractor/** y copia "**extractor.sh**" en tu carpeta de World of Warcraft junto con los archivos anteriores.

3. Crea (`mkdir`) las carpetas **mmaps** y **vmaps** en tu directorio de World of Warcraft.

4. Ejecuta extractor.sh y selecciona tus opciones de extracción.

**Importante:**

- ¡**dbc**, **maps** y **vmaps** son necesarios para que el servidor funcione correctamente!

- No intentes detener el proceso de extracción de **vmaps**. Termina cuando imprime "Press any key...". Creará dos carpetas nuevas: **buildings** y **vmaps**. La carpeta **buildings** es completamente inútil una vez ejecutado el proceso y se puede borrar sin problema.

- No ejecutes otra tarea antes de que la primera termine o tendrás errores.

- Si detienes vmap4extractor antes de que termine, necesitarás borrar el directorio Buildings antes de empezar de nuevo.

- **Opcional pero extremadamente recomendado: extrae los mmaps.** No intentes detener este proceso mientras extrae.

5. Mueve los archivos extraídos **vmaps**, **maps**, **dbc** y **Cameras** a la carpeta **$AC_CODE_DIR/env/dist/bin/** o a un directorio de tu elección (recuerda actualizar tu [DataDir](#updating-datadir))

Cuando esto se complete, recibirás el siguiente mensaje, que puedes ignorar sin problema.

## Archivos de configuración: Worldserver y Authserver {#config-files-worldserver-and-authserver}

Primero, localiza los dos archivos de configuración por defecto (llamados **worldserver.conf.dist** y **authserver.conf.dist**) y cópialos. Luego renombra las copias con sus mismos nombres pero sin la extensión .dist. Puedes encontrarlos dentro del directorio de instalación **$AC_CODE_DIR/env/dist/etc/**.

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

> **Nota:** El valor por defecto de DataDir es `"."`. Esto significa que si tus archivos del cliente (dbc, maps, mmaps,...) están en el mismo directorio que el binario worldserver, no hay necesidad de actualizar esta opción.

1. En tu archivo **worldserver.conf** localiza la opción **DataDir**.

1. Edita DataDir con la ruta absoluta o relativa de tu carpeta, p. ej. **/home/acore/azerothcore/data/** o **./data**

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
| Este artículo es parte de la Guía de instalación. Puedes leerlo solo o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |
| [<< Paso 2: Instalación del Core](es/linux-core-installation) | [Paso 4: Instalación de la base de datos >>](es/database-installation) |

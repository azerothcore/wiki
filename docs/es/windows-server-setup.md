# Configuración del Servidor en Windows

| Guía de Instalación | |
| :- | :- |
| Este artículo es parte de la Guía de Instalación. Puede leerlo solo o hacer click en los links previos para navegar con facilidad entre los pasos. |
| [<< Paso 2: Instalación del Core](core-installation.md) | [Paso 4: Instalación de la base de datos >>](database-installation.md) |

## Extrayendo los archivos DBC, Maps, VMaps & MMaps

1. Busque dentro del directorio de su build (**C:\Build\RelWithDebInfo\\** \*) y copie los siguientes archivos dentro de la carpeta de World of Warcraft. (en donde esté ubicado el archivo wow.exe).

```
mapextractor.exe
mmaps_generator.exe
vmap4extractor.exe
vmap4assembler.exe
```

2. Busque dentro de **C:\Azerothcore\apps\extractor** y copie "**extractor.bat**" dentro de su carpeta de World of Warcraft folder con los archivos previos.

3. Cree las carpetas **mmaps** y **vmaps** en su directorio de World of Warcraft.

4. Ejecute extractor.bat y seleccione las opciones de extracción que requiera.

**Notas importantes**

- ¡**dbc**, **maps** AND **vmaps** son requeridos para que el servidor funcione apropiadamente!.

- No intente detener la extracción de **vmaps**. Se finaliza cuando imprime en pantalla "Press any key...". Se crearán dos nuevas carpetas: **buildings** y **vmaps**. La carpeta **buildings** es completamente innecesaria y puede ser borrada con tranquilidad.
 
- No inicie otra tarea antes de que finalice la primera. Arrojará errores.

- Si detiene vmap4extractor antes de que finalice, necesitará borrar la carpeta Buildings antes de comenzar de nuevo.

- **Opcional, pero extremadamente recomendado: Extraer mmaps.** No intente detener este proceso mientras está extrayendo.

5. Cree una nueva carpeta en **C:\Build\RelWithDebInfo** \* llamada **Data**

6. Mueva los archivos vmaps, maps, dbc, cameras dentro de la carpeta **Data** que creó.

\* Puede ubicarla en RelWithDebInfo, Debug o Release.

## Modificar los archivos de configuración

Primero que todo, necesitará encontrar los dos archivos de configuración (named worldserver.conf.dist and authserver.conf.dist) y copiarlos. Luego renombre las copias removiendo la extensión .dist. Los puede encontrar en /build/configs/ (puede variar).

Abra los archivos .conf y ubique LoginDatabaseInfo, WorldDatabaseInfo, and CharacterDatabaseInfo. Ingrese la información de inicio de sesión para que el servidor pueda acceder a su base de datos.

En una configuración recién compilada, tendrá los siguientes valores por defecto:
```
LoginDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_auth" worldserver.conf / authserver.conf
WorldDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_world" worldserver.conf
CharacterDatabaseInfo = "127.0.0.1;3306;acore;acore;acore_characters" worldserver.conf
```

Estos tienen la siguiente estructura:

```
Variablename = "MySQLIP;Port;Username;Password;database"  
``` 


<br>

## Ayuda

Si sigue teniendo inconvenientes, revise:

* [Preguntas frecuentes](faq.md)

* [Errores Comunes](common-errors.md)

* [Cómo solicitar ayuda](how-to-ask-for-help.md)

* [Unase a nuestro discord](https://discord.gg/gkt4y2x). Aunque no es un canal de soporte 24/7, un miembro del staff le responderá siempre que tenga tiempo.


| Guía de Instalación | |
| :- | :- |
| Este artículo es parte de la Guía de Instalación. Puede leerlo solo o hacer click en los links previos para navegar con facilidad entre los pasos. |
| [<< Paso 2: Instalación del Core](core-installation.md) | [Paso 4: Instalación de la base de datos >>](database-installation.md) |


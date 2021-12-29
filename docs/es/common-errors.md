# Errores comunes

| ¿Esta página no respondió sus dudas? Lea [Cómo solicitar ayuda](how-to-ask-for-help.md) para saber cómo proceder con su pregunta de la mejor manera. |
| --- |

## Errores relacionados con la base de datos

**ACE00001** No puedo iniciar mi Auth/WorldServer, me aparece el siguiente error:
```
[ERROR]: Table 'acore_world.table' doesn't exist
Your database structure is not up to date. Please make sure you've executed all queries in the sql/updates folders.
```
Simplemente no ha actualizado su base de datos. Necesita [Actualizar su base de datos](database-keeping-the-server-up-to-date.md).

---------------------------------------------------------

**ACE00002** No puedo iniciar mi Auth/WorldServer, me aparece el siguiente error:
```
[ERROR]: DatabasePool world NOT opened. There were errors opening the MySQL connections. Check your SQLDriverLogFile for specific errors.
[ERROR]: Cannot connect to world database 127.0.0.1;3306;acore;acore;acore_world
```
Esto puede significar muchas cosas. Ya sea que su base de datos no está online, ingresó los datos de inicio de sesión erroneos o la estructura de la base de datos es erronea.

Necesitará activar el SQLDriverLogFile en Worldserver.conf para obtener un reporte preciso de lo que está fallando.

Para hacer esto, remueva el comentario de Logger.sql.driver y luego ejecute el WorldServer de nuevo.

---------------------------------------------------------

**ACE00003** No puedo iniciar mi Auth/WorldServer, me aparece el siguiente error:
```
> Loaded 0 acore strings. DB table `acore_string` is empty.
```
Esto sucede porque no tiene importada la base de datos en lo absoluto. Siga las instrucciones dadas en [Instalación de la base de datos](database-installation.md)

---------------------------------------------------------

**ACE00004** No puedo iniciar mi Auth/WorldServer, me aparece el siguiente error:
```
Unknown column 'level' in 'field list'

Your database structure is not up to date. Please make sure you've executed all queries in the sql/updates folders.
```
Esto puede significar varias cosas:

1. Usted actualizó su base de datos pero olvidó actualizar los binarios recompilando.
2. Usted actualizó los binarios, pero olvidó actualizar la base de datos. 
3. Usted está intentando usar un parche custom o un modulo, pero olvidó actualizar la base de datos.
4. Usted está tratando de usar un parche SQL de otro proyecto (incompatible).

---------------------------------------------------------

## Errores relacionados con la actualización de la base de datos.

**ACE00020** Mi ensamblador de base de datos se cierra y no importa todas las actualizaciones, me aparece el siguiente error:
```
ERROR 1054 (42522) at line 14062: Unknown column 'resistance2' in 'field list'
```
Este error se debe a que usted cambió manualmente la estructura de la base de datos y está generando conflicto con las actualizaciones.

La forma más fácil de arreglar esto es eliminar la base de datos (drop) e importarla nuevamente.

---------------------------------------------------------

**ACE0021** Mi ensamblador de base de datos se cierra y no importa todas las actualizaciones, me aparece el siguiente error:

Esto puede deberse a varias razones:

1. Usted tiene los configurados los datos de inicio de sesión de forma incorrecta para el ensamblador de base de datos.
2. La estructura de su base de datos ha sido modificada manualmente y genera conflicto con las actualizaciones. La forma más fácil de arreglar esto es eliminar la base de datos (drop) e importarla nuevamente.

---------------------------------------------------------

**ACE00022** Mi ensamblador de base de datos se cierra y no importa todas las actualizaciones, me aparece el siguiente error:
```
ERROR 1067 (42000) at line 181: Invalid default value for 'start_time'.
```
Desactive el modo estricto de MySQL strict mode, lea [Cómo activar/desactivar el modo estricto de MySQL en localhost(xampp)? StackOverflow](https://stackoverflow.com/questions/40881773/how-to-turn-on-off-mysql-strict-mode-in-localhost-xampp).

## Errores relacionados con el Core

**ACE00040** El Core no inicia, me aparece el siguiente error:
```
dbc exists, and has 13 field(s) (expected 12). Extracted file might be from wrong client version or a database-update has been forgotten.
```
Necesita extraer los archivos DBC de la misma versión (no modificada) que su servidor. Esto es 3.3.5a.

---------------------------------------------------------

**ACE00041** El Core no inicia, se cierra tan pronto lo abro.

Inice el servidor usando la terminal para que no se cierre y saber el error exacto.

---------------------------------------------------------

**ACE00042** El Core no inicia, me aparece la siguiente ventana de error:

```
The code execution cannot proceed because libmysql.dll was not found. Reinstalling the program may fix this problem.

Or similar error.
```
Usted no copió el archivo .dll necesario dentro del directorio de los binarios o copió uno incorrecto.

---------------------------------------------------------

**ACE00043** El Core no inicia, me aparece el siguiente error:
```
AzerothCore does not support MySQL versions below 5.7 and MariaDB versions below 10.5
```
Actualice su MySQL/MariaDB.

---------------------------------------------------------

**ACE00044** Me aparece el siguiente error:
```
-- Performing Test boost_filesystem_copy_links_without_NO_SCOPED_ENUM - Failed error
```
Puede ignorarlo. Es un error que no podemos ocultar.

---------------------------------------------------------

**ACE00045** Me aparece el siguiente error cuando WorldServer se está ejecutando:
```
Map file './maps/0004331.map' is from an incompatible map version (MAPS v9), MAPS v10 is expected
```
Recompile con herramientas (Tools), copie los extractores en la carpeta de WoW y recree los mapas usando la herramienta de extracción actualizada (mapextractor). Luego remplace sus archivos viejos con los recien extraidos.

---------------------------------------------------------

**ACE00046** Me aparece el siguiente error cuando inicio WorldServer:
```
Used MySQL library version (8.0.19 id 80019) does not match the version id used to compile AzerothCore (id 80024)
```` 
Necesita usar exactamente la misma versión de libmysql.dll de la versión que usó para compilar su fuente. La obtiene de **C:\Program Files\MySQL\MySQL Server 8.x\lib\\** o siga la [Guía de Instalación](https://www.azerothcore.org/wiki/windows-core-installation#compiling-the-source).

---------------------------------------------------------

**ACE00047** Me aparece el siguiente error cuando estoy tratando de iniciar Worldserver o Authserver
```
This application was unable to start correctly (0xc000007b). Click OK to close the application.
```
Esto usualmente se debe a la mezcla de DLLs de 32/64bit con sus binarios compilados. Los DLLs necesitan ser de la misma versión que sus binarios compilados.

---------------------------------------------------------

## Errores relacionados con la compilación del Core

**ACE00060** No obtengo un hash de AzerothCore 

Lea cómo instalar Git para Windows adecuadamente.

---------------------------------------------------------

**ACE00061** No puedo instalar AzerothCore en CentOS/Ubtuntu/Debian etc.

AzerothCore requiere GCC 8.0 o una versión mayor y CLang 7 o una versión mayor.	

---------------------------------------------------------

**ACE00062** No puedo instalar AzerothCore en Windows XP/Vista

AzerothCore requiere [Visual Studio 2019](https://docs.microsoft.com/en-us/visualstudio/releases/2019/system-requirements), por lo tanto,  necesita actualizar a Windows 7 o superior.

---------------------------------------------------------

**ACE00063** No puedo instalar AzerothCore en Linuyx, me aparece el siguiente error:
```
c++: internal compiler error: Segmentation fault (program cc1plus)
```
Esto puede deberse a:
1. Kernels fortalecidos de Selinux: cambie a kernel estándar, compile con clang en vez de gcc o compile sin pch.
2. Poca memoria ram/swap, increméntela.

---------------------------------------------------------

**ACE00064** Cómo \<inserte su pregunta\> en mi sistema operativo.

Use google o compre un libro para aprender cómo funciona el sistema operativo que está usando.

---------------------------------------------------------

**ACE00065** No puedo compilar, me aparece el siguiente error:
```
fatal error C1060: compiler is out of heap space
C1076: compiler limit : internal heap limit reached; use /Zm to specify a higher limit
```
Lea [Cómo Habilitar un conjunto de herramientas de 64-Bit, x664 hosted MSVC en la linea de comandos. Microsoft](https://docs.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?redirectedfrom=MSDN&view=msvc-160).

---------------------------------------------------------

**ACE00066** No puedo compilar, me aparece el siguiente error:
```
C1001: An internal error has occurred in the compiler.
```
Actualice su Visual Studio.

---------------------------------------------------------

**ACE00067** No puedo generar mis archivos CMake, me aparece lo siguiente:
```
Could NOT find Boost (missing: system filesystem program_options iostreams regex) (found suitable version "1.74.0", minimum required is "1.70")
```
Ubique su carpeta de Boost 
1. Ejecute el archivo Bootstrap.bat
1. Ejecute el archivo b2.exe 

## Errores relacionados con los extractores

**ACE00080** Estoy buscando los extractores de mapas, pero son para la versión 4 de WoW.

No es así. El nombre "vmap4extractor"/"vmap4assambler" representa la verisón de la herramienta. Todos son para WoW 3.3.5a.

---------------------------------------------------------

**ACE00081** No se pudo abrir RootWmo mientras el extractor está ejecutandose. (Couldn't open RootWmo while running extractor).

No es un error, ignórelo.

---------------------------------------------------------

**ACE00082** No puedo usar el Vmap extractor.

Debe extraer los mapas (maps) primero.

---------------------------------------------------------

**ACE00083** Tengo mapas de ManGOS o TrinityCore, puedo usarlos?

No. Son incompatibles.

| ¿Esta página no respondió sus dudas? Lea [Cómo solicitar ayuda](how-to-ask-for-help.md) para saber cómo proceder con su pregunta de la mejor manera. |
| --- |

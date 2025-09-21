---
tableofcontents: 1
---

# Errores comunes

| ¿Esta página no respondió sus dudas? Lea [Cómo solicitar ayuda](how-to-ask-for-help) para saber cómo proceder con su pregunta de la mejor manera. |
| --- |

## Errores relacionados con la base de datos

#### [ACE00001](#a-hreface00001ace00001a)
No puedo iniciar mi Auth/WorldServer, me aparece:
```
[ERROR]: Table 'acore_world.table' doesn't exist
Your database structure is not up to date. Please make sure you've executed all queries in the sql/updates folders.
```
Simplemente no ha actualizado su base de datos. Necesita [Actualizar su base de datos](database-keeping-the-server-up-to-date).

---------------------------------------------------------

#### [ACE00002](#a-hreface00002ace00002a)
No puedo iniciar mi Auth/WorldServer, obtengo:
```
[ERROR]: DatabasePool world NOT opened. There were errors opening the MySQL connections. Check your SQLDriverLogFile for specific errors.
[ERROR]: Cannot connect to world database 127.0.0.1;3306;acore;acore;acore_world
```
Esto puede significar muchas cosas. Ya sea que su base de datos no está online, ingresó los datos de inicio de sesión erroneos o la estructura de la base de datos es erronea.

Necesitará activar el SQLDriverLogFile en Worldserver.conf para obtener un reporte preciso de lo que está fallando.

Para hacer esto, remueva el comentario de Logger.sql.driver y luego ejecute el WorldServer de nuevo.

---------------------------------------------------------

#### [ACE00003](#a-hreface00003ace00003a)
No puedo iniciar mi Auth/WorldServer, obtengo:
```
> Loaded 0 acore strings. DB table `acore_string` is empty.
```
Esto sucede porque no tiene importada la base de datos en lo absoluto. Siga las instrucciones dadas en [Instalación de la base de datos](database-installation)

---------------------------------------------------------

#### [ACE00004](#a-hreface00004ace00004a)
No puedo iniciar mi Auth/WorldServer, obtengo:
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

## Errores relacionados con el Core

#### [ACE00040](#a-hreface00040ace00040a)
El núcleo no arranca y obtengo:
```
dbc exists, and has 13 field(s) (expected 12). Extracted file might be from wrong client version or a database-update has been forgotten.
```
Necesita extraer los archivos DBC de la misma versión (no modificada) que su servidor. Esto es 3.3.5a.

---------------------------------------------------------

#### [ACE00041](#a-hreface00041ace00041a)
El núcleo no arranca, se cierra en cuanto lo abro.

Inice el servidor usando la terminal para que no se cierre y saber el error exacto.

---------------------------------------------------------

#### [ACE00042](#a-hreface00042ace00042a)
El núcleo no se inicia y aparece esta ventana de error.

```
The code execution cannot proceed because libmysql.dll was not found. Reinstalling the program may fix this problem.

Or similar error.
```
Usted no copió el archivo .dll necesario dentro del directorio de los binarios o copió uno incorrecto.

---------------------------------------------------------

#### [ACE00043](#a-hreface00043ace00043a)
El núcleo no arranca y obtengo:
```
AzerothCore does not support MySQL versions below 8.0
```
Actualice su MySQL.

---------------------------------------------------------

#### [ACE00044](#a-hreface00044ace00044a)
Me sale:
```
-- Performing Test boost_filesystem_copy_links_without_NO_SCOPED_ENUM - Failed error
```
Puede ignorarlo. Es un error que no podemos ocultar.

---------------------------------------------------------

#### [ACE00045](#a-hreface00045ace00045a)
Recibo un error cuando se ejecuta WorldServer:
```
Map file './maps/0004331.map' is from an incompatible map version (MAPS v9), MAPS v10 is expected
```
Recompile con herramientas (Tools), copie los extractores en la carpeta de WoW y recree los mapas usando la herramienta de extracción actualizada (mapextractor). Luego remplace sus archivos viejos con los recien extraidos.

---------------------------------------------------------

#### [ACE00046](#a-hreface00046ace00046a)
Recibo un error al iniciar WorldServer:
```
Used MySQL library version (8.0.19 id 80019) does not match the version id used to compile AzerothCore (id 80024)
```` 
Necesita usar exactamente la misma versión de libmysql.dll de la versión que usó para compilar su fuente. La obtiene de **C:\Program Files\MySQL\MySQL Server 8.x\lib\\** o siga la [Guía de Instalación](windows-core-installation#compiling-the-source).

---------------------------------------------------------

#### [ACE00047](#a-hreface00047ace00047a)
I get an error when I am trying to start Worldserver or Authserver
```
This application was unable to start correctly (0xc000007b). Click OK to close the application.
```
Esto usualmente se debe a la mezcla de DLLs de 32/64bit con sus binarios compilados. Los DLLs necesitan ser de la misma versión que sus binarios compilados.

---------------------------------------------------------

#### [ACE00048](#a-hreface00047ace00047a)
Recibo un error cuando intento iniciar Worldserver o Authserver
```
{}DatabaseInfo is not specified in configuration file!

{} = World/Character/Auth
```
Esto significa que falta la información de conexión de la base de datos en el archivo .conf.

Vaya a la base de datos DatabaseInfo especificada en .conf y agregue la información de conexión.

---------------------------------------------------------

## Errores relacionados con la compilación del Core

#### [ACE00060](#a-hreface00060ace00060a)
No obtengo un hash de AzerothCore

Lea cómo instalar Git para Windows adecuadamente.

---------------------------------------------------------

#### [ACE00061](#a-hreface00061ace00061a)
No puedo instalar AzerothCore en CentOS/Ubuntu/Debian, etc.

AzerothCore requiere GCC 8.0 o una versión mayor y CLang 7 o una versión mayor.	

---------------------------------------------------------

#### [ACE00062](#a-hreface00062ace00062a)
No puedo instalar AzerothCore en Windows XP/Vista/7

AzerothCore requiere [Visual Studio 2019](https://docs.microsoft.com/en-us/visualstudio/releases/2019/system-requirements), por lo tanto,  necesita actualizar a Windows 7 o superior.

---------------------------------------------------------

#### [ACE00063](#a-hreface00063ace00063a)
No puedo instalar AzerothCore en Linux. Me aparece:
```
c++: internal compiler error: Segmentation fault (program cc1plus)
```
Esto puede deberse a:
1. Kernels fortalecidos de Selinux: cambie a kernel estándar, compile con clang en vez de gcc o compile sin pch.
2. Poca memoria ram/swap, increméntela.

---------------------------------------------------------

#### [ACE00064](#a-hreface00064ace00064a)
¿Cómo puedo <insertar pregunta> en mi sistema operativo?

Use google o compre un libro para aprender cómo funciona el sistema operativo que está usando.

---------------------------------------------------------

#### [ACE00065](#a-hreface00065ace00065a)
No puedo compilar, obtengo:
```
fatal error C1060: compiler is out of heap space
C1076: compiler limit : internal heap limit reached; use /Zm to specify a higher limit
```
Lea [Cómo Habilitar un conjunto de herramientas de 64-Bit, x664 hosted MSVC en la linea de comandos. Microsoft](https://docs.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?redirectedfrom=MSDN&view=msvc-160).

---------------------------------------------------------

#### [ACE00066](#a-hreface00066ace00066a)
No puedo compilar, obtengo:
```
C1001: An internal error has occurred in the compiler.
```
Actualice su Visual Studio.

---------------------------------------------------------

#### [ACE00067](#a-hreface00067ace00067a)
I can't generate my CMake files, I get:
```
Could NOT find Boost (missing: system filesystem program_options iostreams regex) (found suitable version "1.74.0", minimum required is "1.70")
```
Ubique su carpeta de Boost 
1. Ejecute el archivo Bootstrap.bat
1. Ejecute el archivo b2.exe 

## Errores relacionados con los extractores

#### [ACE00080](#a-hreface00080ace00080a)
I am looking for map extractors but they are for wow version 4.

No es así. El nombre "vmap4extractor"/"vmap4assambler" representa la verisón de la herramienta. Todos son para WoW 3.3.5a.

---------------------------------------------------------

#### [ACE00081](#a-hreface00081ace00081a)
Couldn't open RootWmo while running extractor.

No es un error, ignórelo.

---------------------------------------------------------

#### [ACE00082](#a-hreface00082ace00082a)
No puedo usar el extractor Vmap.

Debe extraer los mapas (maps) primero.

---------------------------------------------------------

#### [ACE00083](#a-hreface00083ace00083a)
Tengo mapas de ManGOS o TrinityCore, ¿puedo usarlos?

No.

## Core installation errors

#### [ACE00100](#ace00100)
Si CMake no encuentra MySQL, es necesario configurar

**MYSQL_INCLUDE_DIR = C:/XX/MySQL/MySQL Server X.X/include** y

**MYSQL_LIBRARY = C:/XX/MySQL/MySQL Server X.X/lib(_XX)/libmysql.lib**.

- X.X depende de la versión de MySQL que utilices.

- (Si no ve los campos MYSQL en CMake, marque la casilla Avanzado).

---------------------------------------------------------

[ACE00102](#ace00102)
Si recibe un error que indica que *CMake NO pudo encontrar OpenSSL*

- Marque la casilla de verificación **Avanzado**.

- Busque las dos entradas de OpenSSL en la lista y señale los directorios correctos:

    - OPENSSL_ROOT_DIR es la ruta de instalación (por defecto, **C:/OpenSSL-Win32** o **C:/OpenSSL-Win64**)

    - OPENSSL_INCLUDE_DIR es la carpeta "include" en la ruta de instalación (por defecto, **C:/OpenSSL-Win32/include** o **C:/OpenSSL-Win64/include**)

---------------------------------------------------------

[ACE00103](#ace00103)
- Si recibe un error que indica que CMake *NO se pudo encontrar Boost (falta: sistema de archivos, opciones de programa, expresiones regulares de iostreams) (se encontró la versión adecuada "1.74.0", la mínima requerida es "1.70")

    - Localiza tu carpeta Boost
    
        - Ejecute el archivo Bootstrap.bat

        - Ejecute el archivo b2.exe

---------------------------------------------------------

[ACE00104](#ace00104)
- Si recibes un error que indica que *Git NO SE ENCONTRÓ en tu sistema*:

    - Marque la casilla de verificación **Avanzado**.

    - Busca y encuentra **GIT_EXECUTABLE**
    
        - Especifique la ruta a git.exe, por ejemplo, `C:/Archivos de programa/Git/cmd/git.exe`

    - Si no tiene git.exe, debe instalarlo. Consulte los requisitos.

---------------------------------------------------------

[ACE00105](#ace00105)
- Si encuentra un error como **fatal: early EOF** o **fatal: fetch-pack: invalid index-pack output**
    - Intente actualizar reiniciando su Github Desktop.
    - Considere usar Git Bash
        - Ejecutar Git Bash
        - Ejecute `cd "D:/Ruta/A/Su/Directorio/"`
        - Ejecute `git clone https://github.com/azerothcore/azerothcore-wotlk.git`
        - Tu repositorio ahora se encontrará en `D:/Path/To/Your/Dir/azerothcore-wotlk`

---------------------------------------------------------

| ¿Esta página no respondió sus dudas? Lea [Cómo solicitar ayuda](how-to-ask-for-help) para saber cómo proceder con su pregunta de la mejor manera. |
| --- |

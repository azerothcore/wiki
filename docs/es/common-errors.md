---
tableofcontents: 1
---

# Errores comunes

| ¿Esta página no respondió a tus dudas? Lee [Cómo pedir ayuda](es/how-to-ask-for-help) sobre cómo proceder con tu pregunta de la mejor manera. |
| --- |

## Errores relacionados con la base de datos

#### ACE00001 {#ace00001}

No puedo iniciar mi Auth/WorldServer, me aparece:
```
[ERROR]: Table 'acore_world.table' doesn't exist
Your database structure is not up to date. Please make sure you've executed all queries in the sql/updates folders.
```
Simplemente no estás actualizado y necesitas [actualizar tu base de datos](es/database-keeping-the-server-up-to-date).

---

#### ACE00002 {#ace00002}

No puedo iniciar mi Auth/WorldServer, me aparece:
```
[ERROR]: DatabasePool world NOT opened. There were errors opening the MySQL connections. Check your SQLDriverLogFile for specific errors.
[ERROR]: Cannot connect to world database 127.0.0.1;3306;acore;acore;acore_world
```
Esto puede significar muchas cosas distintas: puede que tu base de datos no esté online, que hayas introducido credenciales incorrectas o que la estructura de la base de datos sea incorrecta.

Necesitas activar el SQLDriverLogFile en Worldserver.conf para obtener un reporte preciso de qué está mal.

Para ello, descomenta Logger.sql.driver y luego ejecuta el WorldServer de nuevo.

---

#### ACE00003 {#ace00003}

No puedo iniciar mi Auth/WorldServer, me aparece:
```
> Loaded 0 acore strings. DB table `acore_string` is empty.
```
Esto se debe a que no has importado la base de datos en absoluto. Sigue las instrucciones de [Instalación de la base de datos](es/database-installation)

---

#### ACE00004 {#ace00004}

No puedo iniciar mi Auth/WorldServer, me aparece:
```
Unknown column 'level' in 'field list'

Your database structure is not up to date. Please make sure you've executed all queries in the sql/updates folders.
```
Esto puede significar varias cosas:

1. Has actualizado tu base de datos pero olvidaste actualizar tus binarios recompilando.
2. Has actualizado tus binarios pero olvidaste actualizar tu base de datos.
3. Estás intentando usar un parche o módulo personalizado pero olvidaste actualizar tu base de datos.
4. Estás intentando usar un parche SQL de otro proyecto.

## Errores relacionados con el Core

#### ACE00040 {#ace00040}

El Core no inicia, me aparece:
```
dbc exists, and has 13 field(s) (expected 12). Extracted file might be from wrong client version or a database-update has been forgotten.
```
Necesitas extraer los archivos DBC de la misma versión del cliente sin modificar que tu servidor, es decir, 3.3.5a.

---

#### ACE00041 {#ace00041}

El Core no inicia, se cierra tan pronto lo abro.

Inicia el servidor usando la línea de comandos para obtener el error exacto.

---

#### ACE00042 {#ace00042}

El Core no inicia, me aparece esta ventana de error.

```
The code execution cannot proceed because libmysql.dll was not found. Reinstalling the program may fix this problem.

Or similar error.
```
No has copiado los archivos .dll necesarios en el directorio de los binarios. Consulta [Instalación del Core](es/core-installation).

---

#### ACE00043 {#ace00043}

El Core no inicia, me aparece:
```
AzerothCore does not support MySQL versions below 8.0
```
Actualiza tu MySQL.

Nota: AzerothCore no soporta MariaDB.

---

#### ACE00044 {#ace00044}

Me aparece:
```
-- Performing Test boost_filesystem_copy_links_without_NO_SCOPED_ENUM - Failed error
```
Puedes ignorarlo. Es un error que no podemos ocultar.

---

#### ACE00045 {#ace00045}

Me aparece un error cuando el WorldServer se está ejecutando:
```
Map file './maps/0004331.map' is from an incompatible map version (MAPS v9), MAPS v10 is expected
```
Descarga el código fuente, recompila las tools, copia los extractores a tus binarios de wow y vuelve a crear los maps usando el mapextractor actualizado. Luego reemplaza tus archivos de maps viejos por los nuevos.

---

#### ACE00046 {#ace00046}

Me aparece un error cuando inicia el WorldServer:
```
Used MySQL library version (8.0.19 id 80019) does not match the version id used to compile AzerothCore (id 80024)
```
Necesitas usar exactamente la misma versión de libmysql.dll que la versión que usaste para compilar tu código fuente. La obtienes de **C:\Program Files\MySQL\MySQL Server 8.x\lib\\** o siguiendo la [guía de instalación](es/windows-core-installation#compiling-the-source).

Esto se debe a que has actualizado tu servidor MySQL pero no has recompilado ni añadido el nuevo archivo libmysql.dll.

---

#### ACE00047 {#ace00047}

Me aparece un error cuando intento iniciar el Worldserver o el Authserver
```
This application was unable to start correctly (0xc000007b). Click OK to close the application.
```
Esto normalmente se debe a mezclar DLLs de 32/64 bits con tus binarios compilados. Tus DLLs deben ser de la misma versión de bits que tus binarios compilados.

---

#### ACE00048 {#ace00048}

Me aparece un error cuando intento iniciar el Worldserver o el Authserver
```
{}DatabaseInfo is not specified in configuration file!

{} = World/Character/Auth
```
Esto significa que falta la información de conexión a la base de datos en el archivo .conf.

Ve al DatabaseInfo especificado en el .conf y añade la información de conexión.

## Errores relacionados con la compilación del Core

#### ACE00060 {#ace00060}

No obtengo un hash de AzerothCore

Reinstala Git para Windows y selecciona "Git from the command line and also 3rd party software" cuando te pregunte sobre ajustar tu PATH.

---

#### ACE00061 {#ace00061}

No puedo instalar AzerothCore en CentOS/Ubuntu/Debian, etc.

AzerothCore requiere GCC 8.0 o superior y CLang 7 o superior.

---

#### ACE00062 {#ace00062}

No puedo instalar AzerothCore en Windows XP/Vista/7

AzerothCore requiere [Visual Studio 2022](https://docs.microsoft.com/en-us/visualstudio/releases/2022/system-requirements), por lo tanto necesitas actualizar a Windows 10 o superior.

---

#### ACE00063 {#ace00063}

No puedo instalar AzerothCore en Linux, me aparece:
```
c++: internal compiler error: Segmentation fault (program cc1plus)
```
Esto puede deberse a:
1. Kernels reforzados con SELinux; solución: cambia a un kernel estándar, compila con clang en vez de gcc o compila sin pch.
2. Poca memoria ram/swap, increméntala.

---

#### ACE00064 {#ace00064}

Cómo \<inserta tu pregunta\> en mi sistema operativo.

Usa google o compra un libro para aprender el sistema operativo que estás usando.

---

#### ACE00065 {#ace00065}

No puedo compilar, me aparece:
```
fatal error C1060: compiler is out of heap space
C1076: compiler limit : internal heap limit reached; use /Zm to specify a higher limit
```
Lee [How to: Enable a 64-Bit, x64 hosted MSVC toolset on the command line. Microsoft](https://docs.microsoft.com/en-us/cpp/build/how-to-enable-a-64-bit-visual-cpp-toolset-on-the-command-line?redirectedfrom=MSDN&view=msvc-160).

---

#### ACE00066 {#ace00066}

No puedo compilar, me aparece:
```
C1001: An internal error has occurred in the compiler.
```
Actualiza tu Visual Studio.

---

#### ACE00067 {#ace00067}

No puedo generar mis archivos de CMake, me aparece:
```
Could NOT find Boost (missing: system filesystem program_options iostreams regex) (found suitable version "1.74.0", minimum required is "1.70")
```

Asegúrate de que la versión que tienes instalada es compatible.

Si no descargaste boost precompilado, localiza tu carpeta de Boost
1. Ejecuta el archivo Bootstrap.bat
1. Ejecuta el archivo b2.exe

## Errores relacionados con los extractores

#### ACE00080 {#ace00080}

Estoy buscando extractores de mapas pero son para la versión 4 de WoW.

No, no lo son. El nombre "vmap4extractor"/"vmap4Assembler" refleja la versión de la herramienta. Todos son para WoW 3.3.5a.

---

#### ACE00081 {#ace00081}

Couldn't open RootWmo mientras se ejecuta el extractor.

No es un error, ignóralo.

---

#### ACE00082 {#ace00082}

No puedo usar el Vmap extractor.

Extrae los maps primero.

---

#### ACE00083 {#ace00083}

Tengo maps de ManGOS o TrinityCore, ¿puedo usarlos?

No.

## Errores de instalación del Core {#core-installation-errors}

#### ACE00100 {#ace00100}

Si CMake no encuentra MySQL, es necesario establecer

**MYSQL_INCLUDE_DIR = C:/XX/MySQL/MySQL Server X.X/include** y

**MYSQL_LIBRARY = C:/XX/MySQL/MySQL Server X.X/lib(_XX)/libmysql.lib**.

- X.X depende de qué versión de MySQL uses.

- (Si no ves los campos MYSQL en CMake, marca la casilla Advanced).

---

#### ACE00101 {#ace00101}

Si obtienes errores del linker (p. ej. "error LNK2019: unresolved external symbol mysql_server_init"), asegúrate de que MYSQL_LIBRARY apunte al libmysql.lib que coincide con tu modo de compilación.

- (Si no ves los campos MYSQL en CMake, marca la casilla Advanced).

---

#### ACE00102 {#ace00102}

Si obtienes un error de que *CMake could NOT find OpenSSL*

- Marca la casilla **Advanced**.

- Encuentra las dos entradas de OpenSSL en la lista y apunta a los directorios correctos:

    - OPENSSL_ROOT_DIR es la ruta de instalación (por defecto, **C:/OpenSSL-Win32** o **C:/OpenSSL-Win64**)

    - OPENSSL_INCLUDE_DIR es la carpeta "include" dentro de la ruta de instalación (por defecto, **C:/OpenSSL-Win32/include** o **C:/OpenSSL-Win64/include**)

---

#### ACE00103 {#ace00103}

- Si obtienes un error de que CMake *Could NOT find Boost (missing: system filesystem program_options iostreams regex) (found suitable version "1.74.0", minimum required is "1.70")*

    - Localiza tu carpeta de Boost

        - Ejecuta el archivo Bootstrap.bat

        - Ejecuta el archivo b2.exe

---

#### ACE00104 {#ace00104}

- Si obtienes un error de que *Git was NOT FOUND on your system*:

    - Marca la casilla **Advanced**.

    - Busca y encuentra **GIT_EXECUTABLE**

        - Especifica la ruta a git.exe, p. ej. `C:/Program Files/Git/cmd/git.exe`

    - Si no tienes git.exe, necesitas instalar git. Consulta [requisitos](es/requirements)

---

#### ACE00105 {#ace00105}

- Si te encuentras con un error como **fatal: early EOF** o **fatal: fetch-pack: invalid index-pack output**
  - Prueba a reiniciar tu GitHub Desktop.
  - Considera usar Git Bash
    - Ejecuta Git Bash
    - Ejecuta `cd "D:/Path/To/Your/Dir/"`
    - Ejecuta `git clone https://github.com/azerothcore/azerothcore-wotlk.git`
    - Tu repositorio se encontrará ahora en `D:/Path/To/Your/Dir/azerothcore-wotlk`

---

| ¿Esta página no respondió a tus dudas? Lee [Cómo pedir ayuda](es/how-to-ask-for-help) sobre cómo proceder con tu pregunta de la mejor manera. |
| --- |

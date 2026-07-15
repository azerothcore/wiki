# Instalación del Core con VSC en Windows

| Guía de instalación | |
| :- | :- |
| [<< Paso 1: Requisitos de VSC](es/vsc-requirements) | [Paso 3: Configuración del servidor >>](es/server-setup) |

## Software requerido

Consulta los [Requisitos](es/requirements) antes de continuar.

## Descargar y compilar la fuente

### Descargar el código

1. Crea el directorio donde estarán ubicados los archivos fuente. En esta guía usaremos **C:\Azerothcore**.

1. Haz click derecho en la carpeta y selecciona **GitExt Clone...**

1. Rellena los datos como sigue:

```
Repository to clone: https://github.com/azerothcore/azerothcore-wotlk
Destination: C:\Azerothcore
Subdirectory to create: <none>*
Branch: master
Repository type: Personal repository
```

Haz click en **Clone**. En unos pocos minutos los archivos fuente de Azerothcore se clonarán en **C:\Azerothcore**.

### Configurar y generar la solución de Visual C++ con CMake

Antes de empezar, crea un nuevo directorio llamado **Build**. En esta guía usaremos **C:\Build**.

1. Abre CMake

1. Haz click en **Browse Source...** → Selecciona el directorio fuente (**C:\Azerothcore**)

1. Haz click en **Browse Build...** → Selecciona el directorio de build (**C:\Build**)

1. Haz click en **Configure**.

1. En el menú desplegable, elige la versión del compilador que descargaste en la sección de [Requisitos](es/windows-requirements). Asegúrate de elegir la versión **Win64** si trabajas en una compilación de 64 bits.

1. Asegúrate de que **Use default native compilers** esté marcado.

1. Haz click en **Finish**.

1. Asegúrate de que **TOOLS** esté marcado. Esto compilará los extractores necesarios más adelante en la configuración.

1. Haz click en **Configure** de nuevo. Mientras tengas error(es) escritos en rojo en la ventana del log, tendrás que revisar tus parámetros y volver a ejecutarlo.

1. Haz click en **Generate**. Esto instalará los archivos de build seleccionados en tu carpeta **C:\Build**.

#### Algunas soluciones de errores

- Si CMake no encuentra MySQL, es necesario establecer **MYSQL_INCLUDE_DIR = C:/XX/MySQL/MySQL Server X.X/include** y **MYSQL_LIBRARY = C:/XX/MySQL/MySQL Server X.X/lib(_XX)/libmysql.lib**.

    - XX depende de qué versión de MySQL uses.
    
    - (Si no ves los campos MYSQL en CMake, marca la casilla Advanced).
    
- Si obtienes errores del linker (p. ej. "error LNK2019: unresolved external symbol mysql_server_init"), asegúrate de que MYSQL_LIBRARY apunte al libmysql.lib que coincide con tu modo de compilación (x64 vs 32 bits).

    - (Si no ves los campos MYSQL en CMake, marca la casilla Advanced).

- Si obtienes un error de que *CMake could NOT find OpenSSL*:
  
    - Marca la casilla **Advanced**.
    
    - Encuentra las dos entradas OPENSSL en la lista y apunta a los directorios correctos:

        - OPENSSL_ROOT_DIR es el path de instalación (por defecto, **C:/OpenSSL-Win32** o **C:/OpenSSL-Win64**)
        
        - OPENSSL_INCLUDE_DIR es la carpeta "include" en el path de instalación (por defecto, **C:/OpenSSL-Win32/include** o **C:/OpenSSL-Win64/include**)

### Compilar la fuente

1. En Visual Studio Code abre el directorio con la fuente de AC.
1. En el menú de la parte inferior, haz click en **all** (espera unos segundos) y selecciona **ALL_BUILD** en el diálogo superior.
1. haz click en **BUILD** 

El tiempo de build difiere de una máquina a otra, pero puedes esperar que tarde entre 5 y 30 minutos.

Cuando el build se complete encontrarás un mensaje en la salida que se parece a esto:

```
Build finished with exit code 0
```

Encontrarás tus binarios recién compilados en la carpeta **C:\Build\bin\Release** o **C:\Build\bin\Debug**. Todos ellos se usan para ejecutar tu servidor al final de estas instrucciones.

Necesitarás los siguientes archivos para que el core funcione correctamente:

```
\configs\
authserver.exe
authserver.pdb
worldserver.exe
worldserver.pdb
libmysql.dll
libeay32.dll / libcrypto-1_1.dll / libcrypto-1_1-x64.dll
ssleay32.dll / libssl-1_1.dll / libssl-1_1-x64.dll
```

En la carpeta **configs** deberías encontrar:

```
authserver.conf.dist
worldserver.conf.dist
```

Hay tres archivos DLL que deben añadirse manualmente a esta carpeta, y tienes que copiarlos de los siguientes directorios de instalación/bin:

**libmysql.dll** → C:\Program Files\MySQL\MySQL Server 8.x\lib\

*Nota: necesitas la versión exacta de libmysql que corresponda al MySQL que has descargado. Por esto no puedes descargar la DLL de la web y necesitas sacarla de la carpeta.*

OpenSSL _anterior_ a la versión 1.1.0:

**libeay32.dll**
**ssleay32.dll** → C:\OpenSSL-Win64\ o C:\OpenSSL-Win32\ *(depende de si tu core es de 64 bits o de 32 bits)*.

OpenSSL 1.1.0 y más reciente instalado, los nombres han cambiado:

**libssl-1_1.dll**
**libcrypto-1_1.dll** → C:\OpenSSL-Win32\bin

**libssl-1_1-x64.dll**
**libcrypto-1_1-x64.dll** → C:\OpenSSL-Win64\bin

#### Sobre el log y el reporte de compilación

los archivos pdb solo existen si compilas en modo Debug o RelWithDebInfo; no es obligatorio, pero se recomienda compilar el core al menos en modo RelWithDebInfo para obtener crashlogs adecuados. Si compilas en modo Release, los archivos pdb no son necesarios.

Para reportar crashlogs es OBLIGATORIO compilar en modo Debug o RelWithDebInfo.

| Guía de instalación | |
| :- | :- |
| [<< Paso 1: Requisitos de VSC](es/vsc-requirements) | [Paso 3: Configuración del servidor >>](es/server-setup) |

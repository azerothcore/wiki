# Instalación del Core en Windows

| Guía de Instalación | |
| :- | :- |
| Este artículo es parte de la Guía de Instalación. Puede leerlo solo o hacer click en los links previos para navegar con facilidad entre los pasos. |
| [<< Paso 1: Requisitos](requirements.md) | [Paso 3: Instalación del Servidor >>](server-setup.md) |

## Software requerido

Véase [Requisitos](requirements.md) antes de continuar.

## Obtener y Compilar la fuente

### Obtener el código fuente

1. Cree el directorio en donde almacenará los archivos. En esta guia usaremos **C:\Azerothcore**.

1. Haga click derecho dentro de la carpeta y seleccione **GitExt Clone...**

1. Llene la información de las siguiente forma:

```
Repository to clone: https://github.com/azerothcore/azerothcore-wotlk
Destination: C:\Azerothcore
Subdirectory to create: <none>*
Branch: master
Repository type: Personal repository
```

Haga click en **Clone**. Dentro de pocos minutos los archivos de la fuente de AzerothCore serán clonados dentro de **C:\Azerothcore**.

### Configurando y generando la solución para Visual C++ con CMAKE

Antes de empezar, cree un nuevo directorio llamado **Build**. En esta guía usaremos **C:\Build**.

1. Abra CMake

1. Haga click en **Browse Source...** → Seleccione el directorio que contiene la fuente (**C:\Azerothcore**)

1. Haga click en  **Browse Build...** → Seleccione la carpeta de la build (**C:\Build**)

1. Haga click en  **Configure**.

1. En el menú desplegable, seleccione la versión del compilador que descargó en [Requisitos](windows-requirements.md). Asegúrese de seleccionar **Win64** si etá trabajando con una compilación de 64-bits.

1. Asegurese de marcar **Use default native compilers**.

1. Haga click en  **Finish**.

1. Asegurese de marcar **TOOLS_BUILD**. Esto compilará los binarios necesarios para la extracción de archivos requeridos más adelante.

1. Haga click en **Configure** otra vez. Siempre que tenga errores marcados en rojo en la ventana, deberá revisar los parametros y ejecutar **Configure**.

1. Haga click en **Generate**. Esto instalará los archivos seleccionados en la carpeta **C:\Build**.

#### Algunos posibles errores y su solución

- Si CMake no encuentra MySQL, tendrá que configurar **MYSQL_INCLUDE_DIR = C:/XX/MySQL/MySQL Server X.X/include** y **MYSQL_LIBRARY = C:/XX/MySQL/MySQL Server X.X/lib(_XX)/libmysql.lib**.

    - XX depende de qué versión de MySQL está usando.
    
    - (Si no ve los campos de MySQL en CMake, marque **Advanced box**).
    
- Si obtiene errores de vinculo (e.g "error LNK2019: unresolved external symbol mysql_server_init"), asegurese de que MYSQL_LIBRARY está configurada con el libmysql.lib que corresponde con su modo de compilación(x64 o 32 bits).

    - (Si no ve los campos de MySQL en CMake, marque **Advanced box**).

- Si obtiene un error como *CMake could NOT find OpenSSL*:
    
    - Marque **Advanced**.
    
    - Busque las dos entradas de OPENSSL en la lista y enrutelas con los directorios correspondientes:

        - OPENSSL_ROOT_DIR es la ruta de instalación (por defecto, **C:/OpenSSL-Win32** o **C:/OpenSSL-Win64**)
        
        - OPENSSL_INCLUDE_DIR es la carpeta "include" en la ruta de instalación (por defecto **C:/OpenSSL-Win32/include** o **C:/OpenSSL-Win64/include**)

- Si obtiene un error como *Could NOT find Boost (missing: system filesystem program_options iostreams regex) (found suitable version "1.74.0", minimum required is "1.70")

    - Ubique su carpeta de Boost

        - Ejecute el archivo Bootstrap.bat

        - Ejecute el archivo b2.exe 

### Compilando la fuente

1. En CMake, presione **Open Project** para abrir la solución **AzerothCore.sln** directamente con Visual Studio.

1. En el menú de arriba, haga click en **Build** y seleccione **Configuration Manager**.

1. Configure **Active Solution Configuration** con **RelWithDebInfo**.

1. In the list menus below "Help", set **Active Solution Platform** to **x64** and then click Close (settings automatically save).

    1. If you set 32-bit compilation during CMake configuration, select **x86**.

1. Haga click derecho en **ALL_BUILD** en Solution Explorer a la derecha y seleccione **Clean**.
 
1. Haga click derecho en **ALL_BUILD** y seleccione **Build**. (Ctrl + Shift + B)

    1. Si su interfaz (GUI) no muestra el Solution Explorer, haga click en el menú **Build** y seleccione **Clean Solution** luego **Build**.

El tiempo que requerirá el proceso varía de una maquina a otra, pero puede tomar entre 5 y 30 minutos.

Si se le solicita "Reload build files" durante o después de la compilación, hágalo.

Cuando la Build esté terminada, recibirá un mensaje similar al siguiente:

```
========== Build: 22 succeeded, 0 failed, 0 up-to-date, 1 skipped ==========
```

Encontrará sus binarios recien compilados en **C:\Build\bin\RelWithDebInfo** o **C:\Build\bin\Debug**. Estos son los archivos usados para iniciar su servidor al final de esta guía.

Necesitará los siguientes archivos en orden para que el core funcione apropiadamente:

```
\configs\
authserver.exe
authserver.pbd
worldserver.exe
worldserver.pdb
libmysql.dll
libeay32.dll / libcrypto-1_1.dll / libcrypto-1_1-x64.dll
ssleay32.dll / libssl-1_1.dll / libssl-1_1-x64.dll
```

En la carpeta **configs** debería encontrar:

```
authserver.conf.dist
worldserver.conf.dist
```

Hay tres archivos DLL que deben ser añadidos manualmente a esta carpeta, los tendrá que copiar de los siguientes directorios:

**libmysql.dll** → C:\Program Files\MySQL\MySQL Server 8.x\lib\

*Nota: Necesita la versión exacta de libmysql que corresponda con el MySQL que descargó. Por esta razón, no puede descargar el DLL de internet*

OpenSLL _before_ versión 1.1.0:

**libeay32.dll** y
**ssleay32.dll** → C:\OpenSSL-Win64\ or C:\OpenSSL-Win32\ *(depende de si su Core es 64-bit o 32-bit)*.

En OpenSSL 1.1.0 y los más recientes, los nombres cambiaron:

Para la versión de 32-bits:
**libssl-1_1.dll** y
**libcrypto-1_1.dll** → C:\OpenSSL-Win32\bin

Para la versión de 64-bits:
**libssl-1_1-x64.dll** y
**libcrypto-1_1-x64.dll** → C:\OpenSSL-Win64\bin

#### Sobre el reporte de la compilación

Los archivos pdb solo existirán si compiló en modo Debug o RelWithDebInfo, no es obligatorio, pero sí es recomendado compilar por lo menos en modo RelWithDebInfo para obtener los logs de los errores (crashlogs). Si compila en modo Release, los archivos pdb no son necesarios.

Para reportar los errores es OBLIGATORIO compilar en modo Debug o RelWithDebInfo.

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
| [<< Paso 1: Requisitos](requirements.md) | [Paso 3: Instalación del Servidor >>](server-setup.md) |

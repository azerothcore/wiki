# Windows: Requisitos

| Guía de Instalación                                                                                                                                |                                                         |
| :-                                                                                                                                                 | :-                                                      |
| Este artículo es parte de la Guía de Instalación. Puede leerlo solo o hacer click en los links previos para navegar con facilidad entre los pasos. |
| [<< Inicio: Guía de Instalación](classic-installation.md)                                                                                                  | [Paso 2: Instalación del Core >>](windows-core-installation.md) |

|                                                                             |
| :-                                                                          |
| Boost ≥ 1.74                                                                |
| MySQL ≥ 5.7.0                                                               |
| OpenSLL ≥ 1.0.x (OpenSSL 3.0 no es soportado)                               |
| CMake ≥ 3.16                                                                |
| MS Visual Studio (Community) ≥ 16.11 (2019) (Escritorio) (Sin vista previa) |

1. Extensiones de Git

    1. Necesitará tener Git instalado. Puede obtener la [versión más reciente](https://sourceforge.net/projects/gitextensions/).

1. Instale el compilador / IDE [Visual Studio (17) Community 2020](https://visualstudio.microsoft.com/downloads/)

   Necesitará instalar el compilador de C++.
   
   Para hacer esto, seleccione **Desktop development for C++** dentro de **Workloads -> Desktop & Mobile**.

   <a href="/wiki/images/visualstudio.jpg" target="_blank">
   <img src="/wiki/images/visualstudio.jpg" height="50%" width="50%">
   </a>

1. [MySQL Server Community Edition](https://dev.mysql.com/downloads/mysql/8.0.html) (**Use una version ≥ 5.7** con configuración de mysql server)

    1. Descargue el instalador de Windows (MSI).
    
    1. Baje hasta el fondo y de click en "No thanks, just take me to the downloads!"
    
    1. Cuando la instalación esté casi completa, asegurese de marcar "Launch the MySQL Instance Configuration Wizard", luego haga click en "Finish".
    
    1. Cuando inicie la configuración de MySQL, la mayoría de las configuraciones por defecto funcionarán, pero recuerde el nombre de usuario y contraseña que usará (root // whatever). Los necesitará para iniciar sesión en su administrador de bases de datos elegido (abajo) para importar los archivos SQL más adelante. 
    
    1. Para probar si MySQL está instalado correctamente, presione CTRL+ALT+SUPR en su teclado, entre en el Administrador de Tareas y seleccione la pestaña de "Servicios". En la lista debería aparecer MySQL con el estado de "En ejecución" 

    1. Añada MySQL a las Variables de Entorno.
    
        1. Vaya al Panel de Control -> Sistema
        
        1. Vaya a Configuracion Avanzada del Sistema

        1. Vaya a Variables de Entorno
        
        1. Dentro de "Variables del Sistema" seleccione **Path**
        
        1. Edite y añada sus ruta de instalación de MySQL, i.e **C:\Program Files\MySQL\MySQL Server 8.0\bin\\**

1. Seleccione la herramienta de admnistración de bases de datos

    - mysql cli (La más rápida)
    
    - [SQLYog Community Edition](https://github.com/webyog/sqlyog-community/wiki/Downloads)
    
    - [HeidiSQL](https://www.heidisql.com/download.php) (La mejor para principiantes)
    
    - MySQL Workbench (Ya instalada si eligió instalar el paquete completo de MySQL)
    
    - [DBeaver](https://dbeaver.io/) (Herramienta de administración de bases de datos multiplataforma)

    1. Intente conectarse a su base de datos. Puede encontrar "Connect to Host" o "New Connection" o "Session Manager" dependiendo de qué programa esté usando.

    1. Cree una nueva conexión/sesión. El nombre del Host/Dirección  IP "127.0.0.1" o "localhost" funciona si instaló MySQL en el mismo computador que instaló HeidiSQL o SQLYog. Simplemente llene su usuario y contraseña con los que configuró y entonces ya podrá conectarse a su base de datos.

1. [CMake](https://cmake.org/)

    1. Descargue e instale la ultima verisón **(Latest Release)** del archivo win32-x86.exe, **Nunca descargue la versión (Release Candidate).**
    
    1. Recomendamos compilar en modo de 64 bits. 

1. Archivos de desarrollo MySQL development

    1. Estos archivos están incluidos en MySQL Server, busquelos en el directorio de Archivos de programa, MySQL\MySQL Server 8.0\lib / MySQL\MySQL Server 5.7\lib.

1. [OpenSSL](http://www.slproweb.com/products/Win32OpenSSL.html) Descargue la versión de 64 bits. O puede obtener ambas en caso de que quiera compilar tanto 32 como 64 bits, ambas versiones pueden coexistir.

    - **OpenSSL 3.0 no es soportado.**

    - Encuentre la versión de 64 bits buscando el último 1.0.x o 1.1.x Win64 OpenSSL que no sea la verisón "light". (Ejemplo: Win64 OpenSSL v1.1.1g)
    
    - Encuentre la versión de 32 bits buscando el último 1.0.x o 1.1.x Win32 OpenSSL que no sea la versión "light". (Ejemplo: Win32 OpenSSL v1.1.1g)

    - *Nota #1: Si aparece un error como: "Missing Microsoft Visual C++ ... Redistributable" mientras está instalanod OpenSSL:*
      *Descargue [Microsoft Visual C++ 2017/2019/2022 Redistributable Package (x64)](https://aka.ms/vs/17/release/vc_redist.x64.exe) (1.7MB Instalador) e instalelo*
      *Si necesita soporte para 32 bits, descargue e instale [Microsoft Visual C++ 2017/2019/2022 Redistributable Package (x86)](https://aka.ms/vs/17/release/vc_redist.x86.exe).*
       
    - *Nota #2: Mientras esté instalando OpenSSL, seleccione el directiorio de los binarios de OpenSSL (/bin) (NO "The Windows system directory")*
      *Cuando deba elegir dónde ubicar los DLLs de OpenSSL. Estos deben ubicarse en donde sean encontrados con facilidad para la [Instalación del Core](windows-core-installation).*
  
1. [Boost](https://www.boost.org/).

    1. Descargue la versión precompilada de Windows Binary for Visual Studio 2022

    1. [64bit](https://sourceforge.net/projects/boost/files/boost-binaries/1.74.0/boost_1_74_0-msvc-14.2-64.exe/download)

    1. [32bit](https://sourceforge.net/projects/boost/files/boost-binaries/1.74.0/boost_1_74_0-msvc-14.2-32.exe/download)

    1. Añada una variable de entorno "System", llamada "BOOST_ROOT" y como valor, ingrese el directorio de instalación de Boost. Por ejemplo: `E:/Programs/boost_1_74_0`. Es importante usar '**/**' y no '**\\**' al momento de señalar el directorio. (Asegurese de no quede un slash al final. (final de la ruta). Si sigue presentado inconvenientes, añada la misma variable de entorno en la sección de variables `USER`, tal como la siguiente imagen)

    <a href="/wiki/images/boost.jpg" target="_blank">
    <img src="/wiki/images/boost.jpg" height="50%" width="50%">
    </a>

    1. Tenga en cuenta que la imagen muestra la versión número `1.72.0` - use la versión que corresponda con su confirguración.
  
<br>

## Ayuda

Si sigue teniendo inconvenientes, revise:

* [Preguntas frecuentes](faq.md)

* [Errores Comunes](common-errors.md)

* [Cómo solicitar ayuda](how-to-ask-for-help.md)

* [Unase a nuestro discord](https://discord.gg/gkt4y2x). Aunque no es un canal de soporte 24/7, un miembro del staff le responderá siempre que tenga tiempo.

| Guía de Instalación                                                                                                                                |                                                         |
| :-                                                                                                                                                 | :-                                                      |
| Este artículo es parte de la Guía de Instalación. Puede leerlo solo o hacer click en los links previos para navegar con facilidad entre los pasos. |
| [<< Inicio: Guía de Instalación](classic-installation.md)                                                                                                  | [Paso 2: Instalación del Core >>](windows-core-installation.md) |

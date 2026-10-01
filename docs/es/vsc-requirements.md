# Requisitos de VSC

| Guía de instalación | |
| :- | :- |
| [<< Inicio: Guía de instalación](installation) | [Paso 2: Instalación del Core con VSC >>](windows-vsc-core-installation) |

| |
| :- |
| Boost ≥ 1.70 - 1.74          |
| MySQL ≥ 8.0.0                |
| OpenSLL ≥ 1.0.x              |
| CMake ≥ 3.16                 |
| MS Visual Studio Build Tools |

1. Git Extensions
   
   1. Necesitarás Git instalado. Puedes obtener la última versión aquí https://git-scm.com/download/win
   
1. Instala las [Visual Studio 2022 Build Tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022)

   Necesitarás instalar el compilador de C++.

   Para hacerlo, selecciona **Desktop development for C++** en **Workloads -> Desktop & Mobile**.

   <a href="/wiki/images/visualstudio_tools.png" target="_blank">
   <img src="/wiki/images/visualstudio_tools.png" height="50%" width="50%">
   </a>
   
1. [Visual Studio Code](https://code.visualstudio.com/)

	1. Descarga e instala la **Última Versión**
	1. Instala las extensiones
		1. Haz click en **View**->**Extensions**
			
				<a href="/wiki/images/vsc_extensions.png.png" target="_blank"><img src="/wiki/images/vsc_extensions.png"></a>
		1. En la barra de búsqueda escribe **C/C++ Extension Pack**
		1. Haz click en el botón verde de instalar	
				
				<a href="/wiki/images/visualstudio_tools.png" target="_blank"><img src="/wiki/images/vcs_extension_pack_install.png" height="50%" width="50%"></a>

1. [CMake](https://cmake.org/)

    1. Descarga e instala el archivo win32-x86.exe de la **Última Release**, **NUNCA las versiones RC (Release Candidate).**
    
    1. Recomendamos compilar en modo 64 bits. 

1. Archivos de desarrollo de MySQL

    1. Estos archivos vienen incluidos con MySQL Server; búscalos en el directorio de program files, MySQL\MySQL Server 8.0\lib / MySQL\MySQL Server 5.7\lib.

1. [OpenSSL](http://www.slproweb.com/products/Win32OpenSSL.html) Descarga la versión de 64 bits. O puedes obtener ambas si planeas compilar tanto en 32 como en 64 bits; pueden coexistir una junto a la otra.

    1. Encuentra la versión de 64 bits buscando el OpenSSL Win64 1.0.x o 1.1.x más reciente que NO sea la versión "light". (Ejemplo: Win64 OpenSSL v1.1.1g)
    
    1. Encuentra la versión de 32 bits buscando el OpenSSL Win32 1.0.x o 1.1.x más reciente que NO sea la versión "light". (Ejemplo: Win32 OpenSSL v1.1.1g)

    1. *Nota #1: Si obtienes un mensaje de error "Missing Microsoft Visual C++ 2008 Redistributable" al instalar OpenSSL,*
       *descarga el [Microsoft Visual C++ 2008 Redistributable Package (x64)](http://www.microsoft.com/en-us/download/details.aspx?id=29) (instalador de 1.7MB) e instálalo.*
       *Si necesitas soporte de 32 bits, descarga e instala el [Microsoft Visual C++ 2008 Redistributable Package (x86)](http://www.microsoft.com/en-us/download/details.aspx?id=15336).*
       
    1. *Nota #2: Al instalar OpenSSL, elige el directorio de binarios de OpenSSL (/bin) (NO "The Windows system directory")*
       *cuando se te dé a elegir dónde copiar las DLLs de OpenSSL. Estas DLLs deberán poder localizarse fácilmente para la [Instalación del Core](windows-core-installation).*

1. [Boost](https://www.boost.org/).

    1. Descarga el binario precompilado para Windows para Visual Studio Tools

    1. `1.70.0` es la versión mínima requerida para Visual Studio Tool, pero se recomienda la versión `1.74.0`

    1. 64bit: https://sourceforge.net/projects/boost/files/boost-binaries/1.74.0/boost_1_74_0-msvc-14.2-64.exe/download

    1. 32bit: https://sourceforge.net/projects/boost/files/boost-binaries/1.74.0/boost_1_74_0-msvc-14.2-32.exe/download

    1. Añade una variable de entorno a las variables de "System" llamada "BOOST_ROOT" y como valor tu directorio de instalación de Boost, p. ej. `E:/Programs/boost_1_74_0`. Es importante usar '**/**', no '**\\**' al apuntar al directorio. (Asegúrate de que no tenga una barra final (al final del path). Si sigues teniendo problemas, añade la misma variable también en la sección de variables de `USER`, como se muestra en la imagen de abajo.)

    <a href="/wiki/images/boost.jpg" target="_blank">
    <img src="/wiki/images/boost.jpg" height="50%" width="50%">
    </a>

    1. Ten en cuenta que esta imagen muestra el número de versión `1.72.0`; usa tu número de versión real en tu configuración.

# Ejemplo de NUEVOS requisitos de Windows

| Guía de instalación                                                                                                                   |                                                           |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| Este artículo forma parte de la Guía de instalación. Puedes leerlo por separado o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |                                                           |
| [<< Inicio: Guía de instalación](es/classic-installation)                                                                                 | [Paso 2: Instalación del Core >>](es/windows-core-installation) |

{% include callout.html content="Windows ≥ 10<br/>
Boost ≥ 1.78<br/>
MySQL ≥ 8.0 (Recommended 8.4)<br/>
OpenSSL ≥ 3.x.x<br/>
CMake ≥ 3.16<br/>
MS Visual Studio (Community) ≥ 17 (2022) (Desktop) (No preview)" type="info" %}

|                            Header                             |
| :-----------------------------------------------------------: |
|                          [Git](#git)                          |
|               [Github Desktop](#github-desktop)               |
| [Visual Studio Community 2022](#visual-studio-community-2022) |
|                        [MySQL](#mysql)                        |
|                 [MySQL Client](#mysql-client)                 |
|                        [CMake](#cmake)                        |
|                      [OpenSSL](#openssl)                      |
|                        [Boost](#boost)                        |

## [Git](#git)

### Descarga

- https://git-scm.com/download/win

### Instalación

- Ejecuta el instalador standalone

{% include note.html content="During the installation, you will be prompt to Adjust your PATH environment. Pick 'Git from the command line and also from 3rd-party software'." %}

## [Github Desktop](#github-desktop)

### Descarga

- https://desktop.github.com

### Instalación

- Descarga el instalador y sigue los pasos para configurarlo.

## [Visual Studio Community 2022](#visual-studio-community-2022)

### Descarga

- https://visualstudio.microsoft.com/downloads

{% include note.html content="Make sure you're getting 'Visual Studio 2022 Community' and not 'Visual Studio Code'." %}

### Instalación

- Instala el compilador de C++.
  Necesitarás instalar el compilador de C++.

  Para hacerlo, selecciona **Desktop development for C++** en **Workloads -> Desktop & Mobile**.

   <a href="/wiki/images/visualstudio.jpg" target="_blank">
    <img src="/wiki/images/visualstudio.jpg" height="50%" width="50%">
   </a>

## [MySQL](#mysql)

### Descarga

- https://dev.mysql.com/downloads/mysql/8.4.html

### Instalación

1. Ejecuta el instalador MSI de Windows.
2. Baja hasta el final y haz click en "No thanks, just take me to the downloads!"
3. Cuando la instalación esté casi terminada, asegúrate de que "Launch the MySQL Instance Configuration Wizard" esté marcado, y luego haz click en "Finish".
4. Cuando se lance el MySQL Instance Configuration Wizard, la mayoría de las opciones por defecto están bien, pero recuerda el nombre de usuario y la contraseña que uses (root // lo que sea). Los necesitarás para iniciar sesión en tu herramienta de gestión de base de datos elegida (abajo) para importar archivos SQL más adelante.
5. Para comprobar si MySQL está configurado correctamente, pulsa CTRL+ALT+DEL en tu teclado, entra en el Administrador de tareas, y selecciona la pestaña "Servicios". En la lista de servicios deberías ver "MySQL" con el estado "En ejecución".

6. Añade MySQL a las variables de entorno.

   1. Ve a Panel de control -> Sistema
   2. Ve a Configuración avanzada del sistema

   3. Ve a Variables de entorno
   4. En "Variables del sistema" selecciona **Path**
   5. Edita y añade tu path de instalación de MySQL, es decir **C:\Program Files\MySQL\MySQL Server 8.0\bin\\**

{% include note.html content="MySQL development files: These files are shipped with MySQL Server, search for them in the program files directory, MySQL\MySQL Server 8.0\lib / MySQL\MySQL Server 5.7\lib. You will need them later on for the server." %}

## [MySQL Client](#mysql-client)

### Descarga

- [HeidiSQL](https://www.heidisql.com/download.php) (Mejor para principiantes)

- MySQL CLI (El más rápido, viene con tu instalación de MySQL)

- [DBeaver](https://dbeaver.io/) (Herramienta multiplataforma de gestión de bases de datos)

- [SQLYog Community Edition](https://github.com/webyog/sqlyog-community/wiki/Downloads)

{% include note.html content="You only have to pick one of the options on top." %}

### Instalación

1. Intenta conectarte a tu base de datos. Puede que busques "Connect to Host", "New Connection" o "Session Manager" según el programa que uses.

2. Crea una nueva conexión/sesión. El Hostname/dirección IP "127.0.0.1" o "localhost" está bien si instalaste MySQL en el mismo ordenador en el que instalaste HeidiSQL o SQLYog. Simplemente rellena tu contraseña root // lo que sea y ahora deberías poder conectarte a tu base de datos. Es la información usada en este paso [MySQL](#mysql)

## [CMake](#cmake)

### Descarga

- https://cmake.org/download

{% include note.html content="NEVER download and install the RC (Release Candidate), ALWAYS the Latest Release" %}

### Instalación

- Ejecuta el instalador MSI de Windows.

{% include note.html content="We recommend compiling in 64-bit mode." %}

## [OpenSSL](#openssl)

### Descarga

- http://www.slproweb.com/products/Win32OpenSSL.html

{% include note.html content="Find the 64-bit version by finding the latest 3.x.x Win64 OpenSSL that is NOT the `light` version." %}

### Instalación

- Ejecuta el instalador EXE/MSI de Windows.

{{site.data.alerts.note}}
If you get the error 'Missing Microsoft Visual C++ .... Redistributable' while installing OpenSSL, download the <a href="https://aka.ms/vs/17/release/vc_redist.x64.exe">Microsoft Visual C++ 2017/2019/2022 Redistributable Package (x64) (Direct Download)</a> (1.7MB Installer) and install it.
{{site.data.alerts.end}}

{{site.data.alerts.note}}
While installing OpenSSL, choose The OpenSSL binaries (/bin) directory (NOT "The Windows system directory") when given the choice of where to copy the OpenSSL DLLs. These DLLs will need to be located easily for <a href="windows-core-installation">Core Installation</a>.
{{site.data.alerts.end}}

## [Boost](#boost)

### Descarga

- https://www.boost.org

- [1.81.0](https://sourceforge.net/projects/boost/files/boost-binaries/1.81.0/boost_1_81_0-msvc-14.3-64.exe/download)

{% include note.html content="You only have to pick one of the options on top. The one that has the specific number, it's direct download to that version." %}

### Instalación

- Añade una variable de entorno a las variables de "System" llamada "BOOST_ROOT" y con el valor siendo tu directorio de instalación de Boost, p. ej. `C:/local/boost_1_81_0`. Es importante usar '**/**', no '**\\**' al apuntar al directorio. (Asegúrate de que no tenga una barra final (al final del path). Si sigues teniendo problemas, añade la misma variable también en la sección de variables de `USER`, como se muestra en la imagen de abajo.)

<a href="/wiki/images/boost.jpg" target="_blank">
    <img src="/wiki/images/boost.jpg" height="50%" width="50%">
</a>

{% include note.html content="Notice that this image shows the version number 1.72.0 - use your actual version number in your settings." %}

{% include note.html content="Make sure your BOOST_ROOT variable value has it's / facing the correct way. Like/this/that not\this\that" %}

<br>

|                            Header                             |
| :-----------------------------------------------------------: |
|                          [Git](#git)                          |
|               [Github Desktop](#github-desktop)               |
| [Visual Studio Community 2022](#visual-studio-community-2022) |
|                        [MySQL](#mysql)                        |
|                 [MySQL Client](#mysql-client)                 |
|                        [CMake](#cmake)                        |
|                      [OpenSSL](#openssl)                      |
|                        [Boost](#boost)                        |

## Ayuda

Si sigues teniendo problemas, revisa:

- [FAQ](es/faq)

- [Errores comunes](es/common-errors)

- [Cómo pedir ayuda](es/how-to-ask-for-help)

- [Únete a nuestro servidor de Discord](https://discord.gg/gkt4y2x), pero no es un canal de soporte 24/7. Un miembro del staff te responderá cuando tenga tiempo.

| Guía de instalación                                                                                                                   |                                                           |
| :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| Este artículo forma parte de la Guía de instalación. Puedes leerlo por separado o hacer click en el enlace anterior para moverte fácilmente entre los pasos. |                                                           |
| [<< Inicio: Guía de instalación](es/classic-installation)                                                                                 | [Paso 2: Instalación del Core >>](es/windows-core-installation) |
